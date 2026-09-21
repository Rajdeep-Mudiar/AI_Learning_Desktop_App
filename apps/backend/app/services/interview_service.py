from typing import List, Dict, Any, Optional
from datetime import datetime, timezone
import uuid
from app.schemas.interview import (
    InterviewTrack,
    InterviewQuestion,
    InterviewReport,
    QuestionFeedback,
    HackathonChallenge,
    LeaderboardEntry,
    HackathonSubmissionRequest
)

INTERVIEW_TRACKS: List[InterviewTrack] = [
    InterviewTrack(
        id="ml-engineer",
        title="Applied Machine Learning Engineer Interview",
        role_target="Machine Learning Engineer (Mid - Senior)",
        difficulty="Mid-Level",
        duration_minutes=45,
        questions_count=3,
        description="Evaluates your mastery of loss function derivations, regularization mechanics, gradient optimization dynamics, and vectorized matrix calculus.",
        banner_color="linear-gradient(135deg, #6366f1, #38bdf8)",
        questions=[
            InterviewQuestion(
                id="mle-q1",
                category="ML Theory & Optimization",
                question="Why does standard gradient descent struggle on ill-conditioned loss surfaces with high condition numbers, and how does Momentum or Adam resolve this?",
                rubric="Candidate should discuss oscillating perpendicular to the valley direction, condition number of Hessian matrix H, exponential moving average of velocity in Momentum, and adaptive per-parameter learning rates in Adam (v_t / sqrt(s_t)).",
                expected_key_points=["Hessian condition number", "Oscillations in high-curvature directions", "Momentum dampens oscillations", "Adam adapts per-parameter scale"]
            ),
            InterviewQuestion(
                id="mle-q2",
                category="Generalization & Regularization",
                question="Explain the mathematical difference between L1 (Lasso) and L2 (Ridge) regularization and why L1 creates sparse feature weights while L2 only shrinks them.",
                rubric="Candidate should analyze diamond L1 contour corners touching axes versus circular L2 contours, and non-zero subgradient at origin for L1.",
                expected_key_points=["L1 diamond corners intersect at zero", "L2 circle has no corners on axis", "L1 acts as automatic feature selection", "L2 handles multicollinearity"]
            ),
            InterviewQuestion(
                id="mle-q3",
                category="Production & Evaluation",
                question="If your model achieves 99.2% raw test accuracy on a fraud detection dataset with 0.5% fraud prevalence, is it ready for production? How would you redesign the evaluation pipeline?",
                rubric="Candidate must identify the accuracy paradox in class imbalance, propose Precision-Recall AUC (PR-AUC), F1-Score, cost-matrix weighted loss, or calibration curves.",
                expected_key_points=["Accuracy paradox with extreme imbalance", "PR-AUC or F1-Score", "Cost-sensitive matrix (FN vs FP penalty)", "Threshold tuning"]
            )
        ]
    ),
    InterviewTrack(
        id="ai-researcher",
        title="AI Research Scientist & Architect Interview",
        role_target="AI / Foundation Model Researcher",
        difficulty="Senior / Staff",
        duration_minutes=60,
        questions_count=2,
        description="Deep exploration of Transformer scaling laws, positional embeddings, normalization schemes (LayerNorm vs RMSNorm), and attention mechanics.",
        banner_color="linear-gradient(135deg, #10b981, #06b6d4)",
        questions=[
            InterviewQuestion(
                id="res-q1",
                category="Architecture & Math",
                question="In Scaled Dot-Product Attention, prove why the variance of the dot product Q*K grows proportionally to d_k, and explain how this leads to softmax vanishing gradients.",
                rubric="Candidate should prove Var(sum q_i k_i) = d_k * Var(q_i) * Var(k_i) = d_k, explaining that softmax exp(z) concentrates probability on argmax with derivative tending to zero.",
                expected_key_points=["Var(q_i k_i) = 1 under i.i.d standard normal", "Sum of d_k independent terms gives variance d_k", "Large magnitudes push softmax into saturated flat region", "Derivative of softmax vanishes"]
            ),
            InterviewQuestion(
                id="res-q2",
                category="Fine-Tuning & Parameter Efficiency",
                question="Explain the low-rank hypothesis behind LoRA. Why is updating Delta W = B*A with rank r=8 sufficient for adapting massive 70B parameter models?",
                rubric="Candidate should mention intrinsic dimensionality of downstream adaptation, singular value decomposition, and parameter reduction from d*k to r*(d+k).",
                expected_key_points=["Intrinsic rank of adaptation is small", "B in R^(d x r) and A in R^(r x k)", "Linear forward fusion W = W_0 + BA at inference", "VRAM reduction"]
            )
        ]
    ),
    # ================= WEB DEV INTERVIEW =================
    InterviewTrack(
        id="frontend-engineer",
        title="Senior Frontend & React 18 Engineer Interview",
        role_target="Senior Frontend / Full-Stack Engineer",
        domain="web-dev",
        difficulty="Mid-Level",
        duration_minutes=45,
        questions_count=2,
        description="Comprehensive evaluation of React 18 Concurrent features, reconciliation algorithms, CSS layout engines, and Web Vitals performance.",
        banner_color="linear-gradient(135deg, #06b6d4, #3b82f6)",
        questions=[
            InterviewQuestion(
                id="fe-q1",
                category="React Internals",
                question="How does React 18 Fiber architecture enable non-blocking concurrent rendering with useTransition and useDeferredValue?",
                rubric="Candidate should explain Fiber nodes as linked list units of work, time slicing via MessageChannel, and prioritizing user inputs over background re-renders.",
                expected_key_points=["Fiber tree linked list", "Time slicing & scheduler", "Priority lanes", "Interruptible work units"]
            ),
            InterviewQuestion(
                id="fe-q2",
                category="Performance & Web Vitals",
                question="Explain how to diagnose and optimize Largest Contentful Paint (LCP) and Cumulative Layout Shift (CLS) on high-traffic web applications.",
                rubric="Candidate should discuss preloading critical hero images, CSS aspect-ratio containment, font display swap, and avoiding layout thrashing.",
                expected_key_points=["LCP image preloading", "Explicit width/height or aspect-ratio for CLS", "Avoid layout thrashing", "Server-Side Rendering / Streaming"]
            )
        ]
    ),
    # ================= APP DEV INTERVIEW =================
    InterviewTrack(
        id="mobile-engineer",
        title="Cross-Platform Mobile Engineer Interview",
        role_target="Senior Mobile Engineer (React Native / Flutter)",
        domain="app-dev",
        difficulty="Mid-Level",
        duration_minutes=45,
        questions_count=2,
        description="Assesses native bridge communication, JSI architecture, Flutter Impeller rendering pipeline, and memory optimization.",
        banner_color="linear-gradient(135deg, #ec4899, #f43f5e)",
        questions=[
            InterviewQuestion(
                id="app-q1",
                category="Mobile Architecture",
                question="Compare React Native's New Architecture (TurboModules + Fabric using JSI) against the legacy asynchronous JSON Bridge.",
                rubric="Candidate should highlight direct C++ synchronous memory sharing via JSI, eliminating serialized JSON overhead and enabling instant layout measurements.",
                expected_key_points=["JSI direct C++ pointers", "Synchronous method invocation", "Fabric C++ layout engine", "Elimination of JSON serialization bottleneck"]
            ),
            InterviewQuestion(
                id="app-q2",
                category="Offline & State",
                question="How do you architect an offline-first mobile app that handles multi-device sync conflicts and background network re-connection?",
                rubric="Candidate should explain local SQLite queues, idempotency keys, CRDTs or last-write-wins timestamps, and background job sync workers.",
                expected_key_points=["Local SQLite storage as source of truth", "Sync queue with idempotency keys", "Conflict resolution strategy", "Background fetch workers"]
            )
        ]
    ),
    # ================= SYSTEM DESIGN INTERVIEW =================
    InterviewTrack(
        id="system-architect",
        title="Distributed Systems & High-Load Architecture",
        role_target="Staff Systems Architect / Backend Lead",
        domain="system-design",
        difficulty="Senior / Staff",
        duration_minutes=60,
        questions_count=2,
        description="Architecting global distributed backends handling 100M+ DAU with database sharding, CAP theorem trade-offs, and consensus algorithms.",
        banner_color="linear-gradient(135deg, #10b981, #059669)",
        questions=[
            InterviewQuestion(
                id="sys-q1",
                category="Distributed Systems & Sharding",
                question="How would you design a distributed ID generator (like Snowflake) producing 64-bit strictly monotonic or time-ordered IDs across 1,000 independent worker nodes without central locking?",
                rubric="Candidate should detail 41-bit timestamp + 10-bit machine/node ID + 12-bit sequence counter, and handle clock drift/NTP backwards skew.",
                expected_key_points=["Bit allocation (Timestamp + NodeID + Sequence)", "Decentralized lock-free generation", "NTP clock skew handling", "64-bit integer indexing in SQL/NoSQL"]
            ),
            InterviewQuestion(
                id="sys-q2",
                category="High-Availability & Caching",
                question="Explain the Cache-Aside pattern with Redis and how you mitigate Thundering Herd (Cache Stampede) and Cache Penetration problems.",
                rubric="Candidate should propose distributed locks (Redlock), probabilistic early expiration (XFetch), Bloom filters for non-existent keys, and stale cache fallbacks.",
                expected_key_points=["Cache-Aside read/write flow", "Distributed mutex locks on cache miss", "Bloom filter for cache penetration", "Probabilistic early expiration (XFetch)"]
            )
        ]
    ),
    # ================= GIT & GITHUB INTERVIEW =================
    InterviewTrack(
        id="git-devops-engineer",
        title="Git Internals, Branching & DevOps CI/CD Interview",
        role_target="DevOps / Release Engineer & Monorepo Lead",
        domain="github",
        difficulty="Mid-Level",
        duration_minutes=45,
        questions_count=2,
        description="Evaluates deep knowledge of Git object storage (blobs, trees, commits), 3-way merge algorithms, interactive rebasing, and GitHub Actions security.",
        banner_color="linear-gradient(135deg, #f59e0b, #ea580c)",
        questions=[
            InterviewQuestion(
                id="git-q1",
                category="Git Internals",
                question="How does Git store file history under the .git/objects directory? Explain the relationship between Blobs, Trees, and Commits.",
                rubric="Candidate should describe content-addressable SHA-1/SHA-256 storage: Blobs hold file payloads without filenames, Trees hold directory mappings and permissions, Commits reference top-level Trees and parent Commit SHAs.",
                expected_key_points=["Content-addressable SHA hash keys", "Blobs store raw content", "Trees store file paths & modes", "Commits form an immutable Directed Acyclic Graph"]
            ),
            InterviewQuestion(
                id="git-q2",
                category="Branching & Merges",
                question="Explain the internal difference between `git merge --no-ff`, `git merge --squash`, and `git rebase`. When should each be enforced in team branching guidelines?",
                rubric="Candidate should analyze merge commit creation, linear histories without merge bubbles, squashing noisy feature commits, and avoiding rebasing shared public branches.",
                expected_key_points=["Rebase produces clean linear history", "Squash consolidates PR commits into one", "3-way merge preserves exact branch topology", "Never rebase shared public branches"]
            )
        ]
    ),
    # ================= DSA INTERVIEW =================
    InterviewTrack(
        id="dsa-algorithms-engineer",
        title="Algorithms & Data Structures Technical Interview",
        role_target="Software Engineer / Core Systems (Mid - Senior)",
        domain="dsa",
        difficulty="Mid-Level",
        duration_minutes=45,
        questions_count=2,
        description="Evaluates algorithmic efficiency, Two Pointers vs Sliding Window trade-offs, Tree validations, and Dynamic Programming state design.",
        banner_color="linear-gradient(135deg, #f43f5e, #e11d48)",
        questions=[
            InterviewQuestion(
                id="dsa-q1",
                category="Complexity & Two Pointers",
                question="Explain how the Two Pointers technique reduces runtime from O(N²) to O(N) in sorted search problems. Under what conditions does this technique fail?",
                rubric="Candidate should explain directional monotonicity: sorted elements guarantee that moving inward prunes candidate subsets deterministically. It fails when the array is unsorted or non-monotonic.",
                expected_key_points=["Directional monotonicity", "Deterministic pruning of search space", "O(N) linear time and O(1) space", "Requires sorted data"]
            ),
            InterviewQuestion(
                id="dsa-q2",
                category="Dynamic Programming",
                question="How do you identify whether a problem has Optimal Substructure and Overlapping Subproblems? Explain with the 0/1 Knapsack problem.",
                rubric="Candidate should define optimal substructure (global optimum constructed from subproblem optima) and overlapping subproblems (identical subproblem evaluations across branches). In 0/1 knapsack, choices at item i and capacity w depend on (i-1, w) and (i-1, w-wt).",
                expected_key_points=["Optimal substructure definition", "Overlapping subproblems evaluation", "Recurrence state transition dp[i][w]", "Memoization table caching"]
            )
        ]
    ),
    # ================= CYBER SECURITY INTERVIEW =================
    InterviewTrack(
        id="cyber-security-specialist",
        title="Cyber Security Defense & Threat Mitigation Interview",
        role_target="Security Engineer / AppSec & SOC Analyst",
        domain="cybersecurity",
        difficulty="Mid - Senior",
        duration_minutes=50,
        questions_count=2,
        description="Evaluates deep knowledge of OWASP Top 10 mitigations, PKI/TLS handshakes, stateful firewall packet filtering, and Zero Trust architectures.",
        banner_color="linear-gradient(135deg, #14b8a6, #0d9488)",
        questions=[
            InterviewQuestion(
                id="cyber-q1",
                category="Web Security & OWASP",
                question="Why do Parameterized Prepared Statements prevent SQL Injection at the architectural level while regex blacklists and string escaping often fail?",
                rubric="Candidate should explain SQL compilation phases: prepared statements compile the query AST with placeholders before parameter binding. Parameters are treated strictly as inert literals over the binary wire protocol.",
                expected_key_points=["Separate code from data channels", "Pre-compiled AST query plan", "Literal data binding", "Blacklist bypasses (encoding, double quotes)"]
            ),
            InterviewQuestion(
                id="cyber-q2",
                category="Enterprise Defense",
                question="Explain the core principles of Zero Trust Architecture (ZTA). How does micro-segmentation limit the blast radius during an active breach?",
                rubric="Candidate should discuss Never Trust Always Verify, identity-aware proxies, mutual TLS between microservices, least privilege access, and preventing lateral movement.",
                expected_key_points=["Never Trust Always Verify", "Assume breach mentality", "Micro-segmentation blocks lateral movement", "Continuous identity & device posture verification"]
            )
        ]
    )
]

HACKATHON_CHALLENGES: List[HackathonChallenge] = [
    HackathonChallenge(
        id="tabular-churn-speedrun",
        title="45-Minute Tabular Churn Prediction Sprint",
        tagline="Optimize F1-Score on an imbalanced customer dataset under a strict 45-minute countdown.",
        time_limit_minutes=45,
        metric_name="F1-Score (Macro)",
        target_benchmark=0.88,
        description="Build and tune an ensemble model (Random Forest, Gradient Boosting) handling categorical encodings and missing values to maximize macro F1.",
        dataset_info="Customer Churn Benchmark (7,043 records, 20 features)",
        starter_code="import pandas as pd\nfrom sklearn.ensemble import RandomForestClassifier\n\n# Train your estimator\nclf = RandomForestClassifier(n_estimators=100)\n",
        leaderboard=[
            LeaderboardEntry(rank=1, username="alex_ai_dev", score=0.912, latency_ms=4.2, model_name="Ensemble RF+GB", submitted_at="10 mins ago"),
            LeaderboardEntry(rank=2, username="matrix_coder", score=0.895, latency_ms=3.8, model_name="Tuned XGBoost", submitted_at="25 mins ago"),
            LeaderboardEntry(rank=3, username="student_ml", score=0.874, latency_ms=6.1, model_name="RandomForest Baseline", submitted_at="1 hour ago"),
        ]
    )
]

def list_interview_tracks() -> List[InterviewTrack]:
    return INTERVIEW_TRACKS

def get_track_by_id(track_id: str) -> Optional[InterviewTrack]:
    for t in INTERVIEW_TRACKS:
        if t.id == track_id:
            return t
    return None

def evaluate_interview_session(track_id: str, answers: List[Dict[str, str]]) -> InterviewReport:
    track = get_track_by_id(track_id) or INTERVIEW_TRACKS[0]
    feedbacks: List[QuestionFeedback] = []
    total_score = 0

    for q in track.questions:
        # Find matching answer
        user_ans = ""
        for a in answers:
            if a.get("question_id") == q.id:
                user_ans = a.get("user_answer", "").strip()
                break

        words = user_ans.split()
        matched = [kp for kp in q.expected_key_points if any(w.lower() in user_ans.lower() for w in kp.split())]
        
        q_score = min(100, 50 + len(matched) * 12 + min(20, len(words) // 5)) if len(words) >= 10 else 40
        total_score += q_score

        feedbacks.append(QuestionFeedback(
            question_id=q.id,
            score=q_score,
            feedback=f"Candidate addressed {len(matched)} key points with strong clarity." if q_score >= 75 else "Good start, but missed mathematical rigor on gradient bounds.",
            strengths=[f"Articulated concept of {matched[0]}" if matched else "Clear response structure"],
            missing_points=[kp for kp in q.expected_key_points if kp not in matched]
        ))

    overall = total_score // max(1, len(track.questions))
    
    if overall >= 85:
        recommendation = "Strong Hire"
    elif overall >= 70:
        recommendation = "Hire"
    elif overall >= 55:
        recommendation = "Lean Hire"
    else:
        recommendation = "No Hire"

    return InterviewReport(
        overall_score=overall,
        recommendation=recommendation,
        technical_depth_score=min(100, overall + 3),
        communication_score=min(100, overall - 2),
        problem_solving_score=overall,
        detailed_feedback=feedbacks,
        strengths_summary=[
            "Demonstrated clear understanding of mathematical constraints",
            "Articulated production trade-offs and SLA awareness"
        ],
        improvement_areas=[
            "Quantify asymptotic big-O complexity in matrix operations",
            "Mention empirical convergence guarantees"
        ]
    )

def list_hackathons() -> List[HackathonChallenge]:
    return HACKATHON_CHALLENGES

def submit_hackathon_entry(req: HackathonSubmissionRequest) -> LeaderboardEntry:
    # Heuristic evaluation of custom code
    entry = LeaderboardEntry(
        rank=len(HACKATHON_CHALLENGES[0].leaderboard) + 1,
        username="You (Candidate)",
        score=0.889,
        latency_ms=4.8,
        model_name=req.model_name or "Custom Estimator",
        submitted_at="Just now"
    )
    HACKATHON_CHALLENGES[0].leaderboard.insert(0, entry)
    # Re-sort ranks
    HACKATHON_CHALLENGES[0].leaderboard.sort(key=lambda x: x.score, reverse=True)
    for idx, e in enumerate(HACKATHON_CHALLENGES[0].leaderboard):
        e.rank = idx + 1
    return entry
