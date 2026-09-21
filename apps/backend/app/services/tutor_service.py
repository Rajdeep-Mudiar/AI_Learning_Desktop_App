import httpx
import json
import re
from typing import List, Dict, Any, Optional
from app.schemas.tutor import (
    TutorChatRequest,
    TutorChatResponse,
    TutorModelsResponse,
    OllamaModelItem
)

# Mode System Directives
MODE_PROMPTS = {
    "socratic": (
        "You are an inspiring, rigorous Computer Science and Engineering Professor using the Socratic method.\n"
        "RULES:\n"
        "1. DO NOT immediately give the final solution or entire code blocks.\n"
        "2. Guide the student by asking 1-2 probing diagnostic questions that nudge them toward realizing the answer.\n"
        "3. Provide intuition and visual analogies before mathematical notation.\n"
        "4. Encourage the student to think through asymptotic complexity (Big-O), memory allocation, and edge cases."
    ),
    "explain_mistake": (
        "You are an expert technical debugging mentor.\n"
        "RULES:\n"
        "1. Directly pinpoint the mathematical, algorithmic, or security flaw in the student's code or reasoning.\n"
        "2. Explain WHY it failed (e.g. index out of bounds, off-by-one, race condition, lack of sanitization, shape mismatch).\n"
        "3. Offer a corrected conceptual framework with clear, actionable guidance."
    ),
    "math_derivation": (
        "You are a theoretical computer scientist and mathematical researcher.\n"
        "RULES:\n"
        "1. Provide step-by-step mathematical proofs, recurrence relations (Master Theorem), or complexity derivations.\n"
        "2. Annotate asymptotic boundaries ($O, \\Omega, \\Theta$) and algebraic steps clearly.\n"
        "3. Connect the algebraic equations to algorithmic intuition and geometric representations."
    ),
    "code_review": (
        "You are a Principal Software Engineer and Systems Architect.\n"
        "RULES:\n"
        "1. Review the provided code for time/space efficiency, edge cases, and memory leaks.\n"
        "2. Check clean architecture, idiomatic patterns, typing, and defensiveness.\n"
        "3. Provide clean, well-commented code snippets with complexity analysis."
    )
}

DOMAIN_DESCRIPTIONS = {
    "dsa": "Data Structures & Algorithms (Arrays, Linked Lists, Trees, BSTs, Graphs, Dynamic Programming, Greedy, Backtracking, Sorting, Heaps)",
    "cybersecurity": "Cybersecurity & Ethical Hacking (OWASP Top 10, SQLi, XSS, CSRF, JWT, Cryptography, RSA, AES, SHA-256, Firewalls, Port Scanning, Zero Trust)",
    "ai-ml": "Machine Learning & Deep Learning (Neural Networks, Backpropagation, CNNs, Transformers, Optimization, PyTorch, NumPy)",
    "system-design": "Distributed Systems & System Design (Scalability, Sharding, Replication, CAP Theorem, Caching, Rate Limiting, Microservices)",
    "web-dev": "Modern Full-Stack Web Development (React, Next.js, Node.js, TypeScript, REST, GraphQL, CSS Architecture)",
    "app-dev": "Mobile App Development (Flutter, React Native, State Management, Offline Sync, Native Bridges)",
    "github": "Git & GitHub Engineering (Branching Strategies, Interactive Rebase, Merge Conflicts, CI/CD Actions, Internals)"
}

NON_CHAT_KEYWORDS = ["embed", "nomic-embed", "mxbai-embed", "bert", "clip"]


def is_chat_model(name: str) -> bool:
    """Filter out embedding-only models."""
    name_lower = name.lower()
    return not any(kw in name_lower for kw in NON_CHAT_KEYWORDS)


async def fetch_available_models(base_url: str = "http://localhost:11434") -> TutorModelsResponse:
    try:
        async with httpx.AsyncClient(timeout=3.0) as client:
            resp = await client.get(f"{base_url}/api/tags")
            if resp.status_code == 200:
                data = resp.json()
                raw_models = data.get("models", [])
                
                chat_models = []
                for m in raw_models:
                    m_name = m.get("name", "")
                    if is_chat_model(m_name):
                        chat_models.append(
                            OllamaModelItem(
                                name=m_name,
                                size=str(round(m.get("size", 0) / (1024**3), 1)) + " GB" if m.get("size") else None,
                                family=m.get("details", {}).get("family", "LLM"),
                                is_available=True
                            )
                        )
                
                # Priority order for fastest default model: llama3.2:1b -> gemma3:1b -> qwen2.5-coder -> qwen3 -> any first
                default_m = "llama3.2:1b"
                model_names = [m.name for m in chat_models]
                for preferred in ["llama3.2:1b", "gemma3:1b", "qwen2.5-coder:7b", "qwen3:latest", "phi:latest", "llama3:latest"]:
                    for mn in model_names:
                        if preferred in mn:
                            default_m = mn
                            break
                    if default_m in model_names:
                        break
                
                if not default_m and chat_models:
                    default_m = chat_models[0].name

                return TutorModelsResponse(
                    available_models=chat_models if chat_models else [
                        OllamaModelItem(name=m.get("name", "unknown"), size="4.0 GB", is_available=True) for m in raw_models
                    ],
                    is_ollama_online=True,
                    default_model=default_m or "llama3.2:1b"
                )
    except Exception:
        pass

    # Fallback offline preset models
    fallback_models = [
        OllamaModelItem(name="llama3.2:1b", size="1.3 GB", family="llama", is_available=False),
        OllamaModelItem(name="qwen2.5-coder:7b", size="4.7 GB", family="qwen2", is_available=False),
        OllamaModelItem(name="qwen3:latest", size="5.2 GB", family="qwen3", is_available=False),
        OllamaModelItem(name="gemma3:1b", size="0.8 GB", family="gemma3", is_available=False),
        OllamaModelItem(name="phi:latest", size="1.6 GB", family="phi", is_available=False),
    ]
    return TutorModelsResponse(
        available_models=fallback_models,
        is_ollama_online=False,
        default_model="llama3.2:1b"
    )


async def call_cloud_llm(req: TutorChatRequest, system_prompt: str) -> Optional[TutorChatResponse]:
    """Execute LLM call against OpenAI-compatible APIs (OpenAI, Groq, OpenRouter, etc.)"""
    if not req.api_key:
        return None

    api_base = req.api_base or "https://api.openai.com/v1"
    model = req.model_name or "gpt-4o-mini"

    messages = [{"role": "system", "content": system_prompt}]
    for msg in req.history[-6:]:
        messages.append({"role": msg.role, "content": msg.content})
    messages.append({"role": "user", "content": req.message})

    try:
        async with httpx.AsyncClient(timeout=30.0) as client:
            resp = await client.post(
                f"{api_base}/chat/completions",
                headers={
                    "Authorization": f"Bearer {req.api_key}",
                    "Content-Type": "application/json"
                },
                json={
                    "model": model,
                    "messages": messages,
                    "temperature": 0.5
                }
            )
            if resp.status_code == 200:
                data = resp.json()
                content = data["choices"][0]["message"]["content"]
                return TutorChatResponse(
                    response=content,
                    mode_used=req.mode,
                    provider_used="cloud_api",
                    model_used=model,
                    suggested_followups=[
                        "Can you give me an example with code?",
                        "What is the time and space complexity?",
                        "How would I solve this in a technical interview?"
                    ],
                    referenced_concepts=["Cloud Neural Inference", req.mode.replace("_", " ").title()]
                )
    except Exception:
        pass
    return None


def generate_dynamic_semantic_response(req: TutorChatRequest) -> TutorChatResponse:
    """
    Intelligent, domain-aware dynamic fallback generator.
    Handles greetings, DSA queries, Security topics, System Design, AI/ML, and debugging.
    """
    query = req.message.strip().lower()
    mode = req.mode
    ctx = req.context
    domain = (ctx.active_domain if ctx and ctx.active_domain else "all").lower()

    # 1. Greetings & Conversational Queries
    if re.match(r"^(hi|hello|hey|greetings|howdy|good morning|good afternoon|good evening|yo)\b", query) or len(query) < 4:
        domain_label = DOMAIN_DESCRIPTIONS.get(domain, "Computer Science & Engineering")
        if domain == "dsa":
            ans = (
                "👋 **Hello! I'm your Data Structures & Algorithms AI Tutor.**\n\n"
                "I'm here to help you master algorithms, data structures, complexity analysis, and interview problem-solving!\n\n"
                "Here are some great topics we can explore:\n"
                "- 🚀 **Two Pointers & Sliding Window** optimization patterns\n"
                "- 🌲 **Binary Search Trees & Graph Traversals** (BFS, DFS, Dijkstra)\n"
                "- 🧩 **Dynamic Programming** state formulation and memoization\n"
                "- ⚡ **Big-O Asymptotics** and time/space complexity tradeoffs\n\n"
                "What algorithm or problem would you like to tackle today?"
            )
            followups = [
                "How do I recognize when to use Sliding Window vs Two Pointers?",
                "Explain the time complexity of QuickSort vs MergeSort",
                "How do I break down 0/1 Knapsack using Dynamic Programming?"
            ]
            concepts = ["Two Pointers", "Binary Search Trees", "Dynamic Programming", "Time Complexity"]
        elif domain == "cybersecurity":
            ans = (
                "🛡️ **Hello! I'm your Cybersecurity & Defensive Engineering AI Tutor.**\n\n"
                "I can guide you through offensive security, defensive safeguards, cryptographic algorithms, and vulnerability mitigation.\n\n"
                "Key security pillars we can dive into:\n"
                "- 💉 **OWASP Top 10**: Preventing SQL Injection, XSS, CSRF, and Broken Access Control\n"
                "- 🔐 **Applied Cryptography**: RSA, AES-GCM, SHA-256 Avalanche effect, and Zero-Knowledge Proofs\n"
                "- 🌐 **Network Defense**: Stateful Firewalls, SYN Floods, Port Scanning, and TLS 1.3 Handshakes\n"
                "- 🎫 **Identity & Auth**: JWT verification, OAuth 2.0 flows, and Zero-Trust architectures\n\n"
                "What security challenge or vulnerability would you like to explore?"
            )
            followups = [
                "How does SQL Injection work and how do Prepared Statements eliminate it?",
                "Explain how the SHA-256 avalanche effect guarantees cryptographic integrity",
                "What is the difference between Symmetric (AES) and Asymmetric (RSA) encryption?"
            ]
            concepts = ["OWASP Top 10", "Cryptographic Hashing", "SQLi Prevention", "Zero Trust"]
        else:
            ans = (
                "👋 **Hello! I'm your Context-Aware Engineering AI Tutor.**\n\n"
                f"I'm actively grounded in **{domain_label}**.\n\n"
                "You can ask me conceptual questions, paste buggy code for debugging, request mathematical derivations, or do mock interview practice!\n\n"
                "How can I assist your learning right now?"
            )
            followups = [
                "Give me a challenge problem for my active topic",
                "Explain the core mental model for this domain",
                "Review my code snippet for performance and edge cases"
            ]
            concepts = ["Interactive Learning", "Socratic Guidance", "Code Review"]

        return TutorChatResponse(
            response=ans,
            mode_used=mode,
            provider_used="semantic_reasoning_engine",
            model_used="AI Lab Semantic Reasoning Engine",
            suggested_followups=followups,
            referenced_concepts=concepts
        )

    # 2. DSA Topics
    if any(k in query for k in ["two pointer", "sliding window", "two sum", "subarray", "window"]):
        if mode == "socratic":
            ans = (
                "### 🔍 Socratic Exploration: Two Pointers & Sliding Window\n\n"
                "When you are asked to find a subarray with sum $K$ or find two elements that sum to a target in a sorted array:\n\n"
                "**Consider these diagnostic questions:**\n"
                "1. If you check every pair or subarray with nested loops, what is the brute-force time complexity? ($O(N^2)$)\n"
                "2. If the array is **sorted**, how does moving the right pointer inward vs left pointer outward change the sum?\n"
                "3. In a **variable-size sliding window**, what condition dictates expanding `right` vs contracting `left`?\n\n"
                "👉 *Intuition:* Two pointers transform an $O(N^2)$ exhaustive search into a linear $O(N)$ sweep because each pointer traverses the array at most once."
            )
        else:
            ans = (
                "### ⚡ Two Pointers & Sliding Window Pattern\n\n"
                "**1. Two Pointers (Convergent / Sorted Array)**:\n"
                "Used on sorted collections to achieve $O(N)$ time and $O(1)$ space.\n"
                "```python\ndef two_sum_sorted(nums: list[int], target: int) -> tuple[int, int]:\n"
                "    left, right = 0, len(nums) - 1\n"
                "    while left < right:\n"
                "        curr_sum = nums[left] + nums[right]\n"
                "        if curr_sum == target:\n"
                "            return left, right\n"
                "        elif curr_sum < target:\n"
                "            left += 1   # Need a larger sum\n"
                "        else:\n"
                "            right -= 1  # Need a smaller sum\n"
                "    return -1, -1\n```\n\n"
                "**2. Sliding Window (Subarray / Substring)**:\n"
                "- **Fixed Window**: Maintain window size $K$, slide by `+1` per step.\n"
                "- **Dynamic Window**: Expand `right` until valid, shrink `left` while constraint is violated."
            )
        followups = [
            "How do we handle duplicate elements in 3Sum using Two Pointers?",
            "What is the difference between Kadane's Algorithm and Sliding Window?",
            "Show me how to solve Longest Substring Without Repeating Characters"
        ]
        concepts = ["Two Pointers", "Sliding Window", "Amortized O(N)", "Sorted Array Optimization"]

    elif any(k in query for k in ["tree", "bst", "binary search tree", "inorder", "preorder", "postorder", "traversal"]):
        ans = (
            "### 🌲 Binary Search Tree (BST) & Invariant Properties\n\n"
            "**BST Invariant Rule**:\n"
            "For every node $X$ in the tree:\n"
            "- All values in the **Left Subtree** are strictly $< X.val$\n"
            "- All values in the **Right Subtree** are strictly $> X.val$\n\n"
            "**Traversals & Applications**:\n"
            "1. **In-order (Left $\\to$ Node $\\to$ Right)**: Yields elements in **strictly sorted ascending order** in $O(N)$ time.\n"
            "2. **Pre-order (Node $\\to$ Left $\\to$ Right)**: Ideal for serializing and cloning tree structures.\n"
            "3. **Post-order (Left $\\to$ Right $\\to$ Node)**: Ideal for bottom-up computation (e.g. subtree heights, memory deallocation, syntax trees).\n\n"
            "**Complexity**:\n"
            "- Average search/insert: $O(\\log N)$\n"
            "- Degenerate (skewed list): $O(N) \\to$ requires AVL or Red-Black self-balancing trees."
        )
        followups = [
            "How does an AVL Tree maintain balancing through LL, RR, LR, and RL rotations?",
            "How can we validate if a Binary Tree is a valid BST in O(N) time?",
            "Show me the iterative In-order traversal using an explicit Stack"
        ]
        concepts = ["Binary Search Tree", "In-Order Traversal", "Tree Balance Factor", "Logarithmic Search"]

    elif any(k in query for k in ["dynamic programming", "dp", "memoization", "knapsack", "tabulation"]):
        ans = (
            "### 🧩 Dynamic Programming: The 4-Step Framework\n\n"
            "Dynamic Programming solves problems with **Overlapping Subproblems** and **Optimal Substructure**.\n\n"
            "**The 4-Step Recipe**:\n"
            "1. **State Definition**: Clearly define `dp[i]` or `dp[i][w]` (e.g. max profit using first `i` items with weight capacity `w`).\n"
            "2. **Recurrence Relation**: Formulate the transition between subproblems:\n"
            "   $$\\text{dp}[i][w] = \\max(\\text{dp}[i-1][w], \\,\\text{val}[i] + \\text{dp}[i-1][w - \\text{wt}[i]])$$\n"
            "3. **Base Cases**: Initialize boundaries (e.g. `dp[0][w] = 0` and `dp[i][0] = 0`).\n"
            "4. **Computation Order**: Top-down with Memoization vs Bottom-up with Tabulation."
        )
        followups = [
            "How do we optimize 0/1 Knapsack space complexity from O(N*W) to O(W)?",
            "What is the difference between Top-Down Memoization and Bottom-Up Tabulation?",
            "Walk me through the Coin Change problem using DP"
        ]
        concepts = ["Dynamic Programming", "Optimal Substructure", "Overlapping Subproblems", "State Transition"]

    # 3. Cybersecurity Topics
    elif any(k in query for k in ["sqli", "sql injection", "injection", "prepared statement"]):
        ans = (
            "### 🛡️ SQL Injection (SQLi) Vulnerability & Defense\n\n"
            "**The Flaw**: Mixing untrusted user input directly into executable SQL queries.\n"
            "```sql\n-- Vulnerable String Concatenation:\n"
            "query = \"SELECT * FROM users WHERE user = '\" + user_input + \"' AND pass = '\" + pass_input + \"'\"\n"
            "-- Attacker enters: admin' OR '1'='1\n"
            "-- Resulting SQL:\n"
            "SELECT * FROM users WHERE user = 'admin' OR '1'='1' AND pass = ''\n```\n\n"
            "**The Ultimate Defense: Parameterized Queries (Prepared Statements)**\n"
            "Prepared statements send the SQL query template to the database engine to be compiled *before* parameters are bound.\n"
            "```python\n# Secure Parameter Binding (e.g. with psycopg2 / asyncpg):\n"
            "cursor.execute(\n"
            "    \"SELECT id, username, email FROM users WHERE username = %s AND password_hash = %s\",\n"
            "    (user_input, computed_hash)\n"
            ")\n```\n"
            "Because parameters are treated strictly as literal data strings, SQL parsing never interprets quotes as command delimiters."
        )
        followups = [
            "What is Second-Order SQL Injection and how does it happen?",
            "How do ORMs like SQLAlchemy protect against SQLi by default?",
            "What are Blind SQL Injection attacks and how do attackers extract data using boolean/time delays?"
        ]
        concepts = ["SQL Injection", "Prepared Statements", "Parameterized Queries", "OWASP Top 10"]

    elif any(k in query for k in ["sha256", "hash", "avalanche", "salt", "entropy", "rsa", "aes", "crypto"]):
        ans = (
            "### 🔐 Cryptographic Principles: Hashing vs Encryption\n\n"
            "| Property | Cryptographic Hashing (e.g. SHA-256) | Symmetric Encryption (AES-GCM) | Asymmetric (RSA / ECC) |\n"
            "| :--- | :--- | :--- | :--- |\n"
            "| **Direction** | One-way (Irreversible) | Two-way (Reversible) | Two-way (Reversible) |\n"
            "| **Keys** | No key (or HMAC secret) | Single shared secret key | Public Key / Private Key Pair |\n"
            "| **Purpose** | Integrity, Password Verification | High-throughput data confidentiality | Key exchange, Digital Signatures |\n\n"
            "**The Avalanche Effect**:\n"
            "A secure cryptographic hash guarantees that flipping even a single bit in the input changes roughly **50% of the output bits** unpredictably."
        )
        followups = [
            "Why is SHA-256 unsuitable for direct password storage without Argon2 or bcrypt?",
            "How does Salt prevent Rainbow Table attacks?",
            "How does the TLS 1.3 Handshake combine RSA/ECC and AES-GCM?"
        ]
        concepts = ["SHA-256", "Avalanche Effect", "Argon2/bcrypt Salting", "Public Key Cryptography"]

    # 4. System Design / Web Dev Topics
    elif any(k in query for k in ["cap", "sharding", "replication", "system design", "load balancer", "redis", "cache"]):
        ans = (
            "### 🏗️ Distributed Systems: The CAP & PACELC Theorems\n\n"
            "**The CAP Theorem** states that in any distributed data store, across a network **Partition (P)**, you must choose between:\n"
            "1. **Consistency (C)**: Every read receives the most recent write or an error.\n"
            "2. **Availability (A)**: Every non-failing node returns a non-error response, but without a guarantee that it contains the latest write.\n\n"
            "**PACELC Extension**:\n"
            "If there is a **P**artition: choose between **A**vailability and **C**onsistency.\n"
            "**E**lse (normal operation): choose between **L**atency and **C**onsistency.\n\n"
            "**Examples**:\n"
            "- **CP Systems**: Apache HBase, MongoDB (majority write/read), ZooKeeper/Raft.\n"
            "- **AP Systems**: Apache Cassandra, Amazon DynamoDB (eventual consistency mode), CouchDB."
        )
        followups = [
            "How does Consistent Hashing minimize data movement during cluster re-sharding?",
            "Explain the Cache-Aside vs Write-Through vs Write-Back caching strategies",
            "How does the Raft consensus algorithm handle split-brain during leader election?"
        ]
        concepts = ["CAP Theorem", "PACELC Theorem", "Distributed Consensus", "Eventual Consistency"]

    # 5. Machine Learning Topics
    elif any(k in query for k in ["attention", "transformer", "gradient", "backprop", "ols", "loss", "overfitting"]):
        ans = (
            "### 🧠 Neural Network & Machine Learning Fundamentals\n\n"
            f"You asked about: *\"{req.message}\"*\n\n"
            "**Core Principles**:\n"
            "1. **Optimization Objective**: Minimizing empirical risk $L(\\theta) = \\frac{1}{N} \\sum_{i=1}^N \\ell(f(x_i; \\theta), y_i) + \\lambda \\Omega(\\theta)$.\n"
            "2. **Gradient Flow**: Backpropagating error signals using the multivariate chain rule across computational graphs.\n"
            "3. **Numerical Stability**: Preventing vanishing/exploding gradients with normalization (LayerNorm, BatchNorm) and residual skip connections ($x + f(x)$).\n"
            "4. **Generalization**: Controlling model capacity through weight decay ($L_2$), dropout, data augmentation, and early stopping."
        )
        followups = [
            "Why does Scaled Dot-Product Attention divide by √d_k?",
            "How does Adam combine Momentum with RMSProp for adaptive learning rates?",
            "Show me a vectorized NumPy implementation of backpropagation"
        ]
        concepts = ["Backpropagation", "Gradient Flow", "Residual Connections", "Attention Mechanism"]

    # 6. General Intelligent Fallback
    else:
        lesson_str = f" in context of **{ctx.current_lesson_title}**" if ctx and ctx.current_lesson_title else ""
        ans = (
            f"### 💡 Conceptual Analysis & Architecture{lesson_str}\n\n"
            f"**Regarding your inquiry:** *\"{req.message}\"*\n\n"
            "To approach this with rigorous software engineering and computer science principles, let's break it down:\n\n"
            "1. **Underlying Mental Model**: Identify the core state transformations and data invariants at play.\n"
            "2. **Time & Space Complexity**: Evaluate worst-case, average-case, and amortized resource bounds.\n"
            "3. **Failure Modes & Edge Cases**: Consider null inputs, boundary values, race conditions, or security exploits.\n"
            "4. **Practical Implementation**: Implement with modular, idiomatic, and testable code.\n\n"
            "Which aspect would you like to explore deeper or write code for?"
        )
        followups = [
            "Walk me through a concrete code example step-by-step",
            "What are the most common bugs or performance pitfalls here?",
            "How would this be asked or evaluated in a FAANG / Tier-1 interview?"
        ]
        concepts = ["System Modeling", "Complexity Analysis", "Edge Cases", "Idiomatic Implementation"]

    return TutorChatResponse(
        response=ans,
        mode_used=mode,
        provider_used="semantic_reasoning_engine",
        model_used="AI Lab Semantic Reasoning Engine",
        suggested_followups=followups,
        referenced_concepts=concepts
    )


async def generate_tutor_response(req: TutorChatRequest) -> TutorChatResponse:
    # Build System Prompt with mode and domain context
    system_prompt = MODE_PROMPTS.get(req.mode, MODE_PROMPTS["socratic"])
    
    if req.context:
        domain = req.context.active_domain or "all"
        if domain in DOMAIN_DESCRIPTIONS:
            system_prompt += f"\nActive Engineering Domain: {DOMAIN_DESCRIPTIONS[domain]}"
        if req.context.current_lesson_title:
            system_prompt += f"\nActive Student Lesson: {req.context.current_lesson_title}"
        if req.context.active_code:
            system_prompt += f"\nActive Student Code:\n```\n{req.context.active_code}\n```"
        if req.context.active_error:
            system_prompt += f"\nActive Error Traceback:\n{req.context.active_error}"
        if req.context.recent_quiz_mistake:
            system_prompt += f"\nRecent Quiz Concept Mistake: {req.context.recent_quiz_mistake}"

    # 1. If API Key provided or cloud provider requested, try Cloud LLM
    if req.provider == "cloud_api" or req.api_key:
        cloud_res = await call_cloud_llm(req, system_prompt)
        if cloud_res:
            return cloud_res

    # 2. Try Ollama local inference if provider is "auto" or "ollama"
    if req.provider in ["auto", "ollama"]:
        try:
            ollama_url = req.ollama_base_url or "http://localhost:11434"
            
            # Fetch tags to determine valid installed chat model
            target_model = req.model_name
            installed_models = []
            
            async with httpx.AsyncClient(timeout=3.0) as client:
                tags_resp = await client.get(f"{ollama_url}/api/tags")
                if tags_resp.status_code == 200:
                    installed_models = [m.get("name", "") for m in tags_resp.json().get("models", []) if is_chat_model(m.get("name", ""))]

            if installed_models:
                # If requested model not installed, pick best installed model
                if not target_model or target_model not in installed_models:
                    for pref in ["llama3.2:1b", "gemma3:1b", "qwen2.5-coder:7b", "qwen3:latest", "phi:latest"]:
                        found = [im for im in installed_models if pref in im]
                        if found:
                            target_model = found[0]
                            break
                    if not target_model and installed_models:
                        target_model = installed_models[0]

            if not target_model:
                target_model = "llama3.2:1b"

            messages = [{"role": "system", "content": system_prompt}]
            for msg in req.history[-6:]:
                messages.append({"role": msg.role, "content": msg.content})
            messages.append({"role": "user", "content": req.message})

            async with httpx.AsyncClient(timeout=60.0) as client:
                resp = await client.post(
                    f"{ollama_url}/api/chat",
                    json={
                        "model": target_model,
                        "messages": messages,
                        "stream": False,
                        "options": {
                            "temperature": 0.4 if req.mode == "math_derivation" else 0.7
                        }
                    }
                )
                if resp.status_code == 200:
                    data = resp.json()
                    ai_content = data.get("message", {}).get("content", "")
                    if ai_content:
                        return TutorChatResponse(
                            response=ai_content,
                            mode_used=req.mode,
                            provider_used="ollama",
                            model_used=target_model,
                            suggested_followups=[
                                "Can you break this down with a visual code example?",
                                "What are the common edge cases or security gotchas?",
                                "Give me a practice problem to test my understanding"
                            ],
                            referenced_concepts=[f"Local Ollama ({target_model})", req.mode.replace("_", " ").title()]
                        )
        except Exception as e:
            # Fall back to intelligent dynamic reasoning engine
            pass

    return generate_dynamic_semantic_response(req)
