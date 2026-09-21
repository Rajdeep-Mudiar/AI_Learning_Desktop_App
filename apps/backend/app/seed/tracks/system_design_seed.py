"""
System Design & Distributed Architecture Track Seed Data
Levels 1 - 6 covering:
- Level 1: System Design Fundamentals & Latency Numbers
- Level 2: Database Architecture, Indexing & Sharding
- Level 3: High-Scale Caching (Redis), Load Balancing & Messaging (Kafka)
- Level 4: Distributed Systems (CAP, PACELC, Raft Consensus, Saga Pattern)
- Level 5: Microservices, API Gateways & Observability
- Level 6: Real-World Case Studies (TinyURL, Google Drive, WhatsApp, YouTube, Stripe Payments)
"""

COURSES_DATA = [
    {
        "id": "course-sys-lvl1",
        "title": "System Design Level 1: Foundations, Latency & Scale Estimation",
        "slug": "system-design-level-1-foundations",
        "domain": "system-design",
        "color": "#10B981",
        "icon": "Network",
        "is_published": True,
        "skills_taught": ['Scale Math', 'Consistent Hashing', 'Redis Caching', 'Distributed Systems'],
        "description": "Master client-server mechanics, stateless vs stateful architectures, latency numbers every engineer should know, and back-of-the-envelope scale estimations.",
        "category": "System Design",
        "level": "beginner",
        "estimated_hours": 12,
        "thumbnail_url": "/assets/courses/sys-foundations.png",
        "modules": [
            {
                "id": "mod-sys-1-1",
                "title": "Module 1: Latency Numbers & Scale Estimation",
                "description": "L1/L2 cache vs RAM vs SSD vs Network latencies, QPS calculations, and bandwidth estimation.",
                "order": 1,
                "lesson_ids": ["sys-latency-numbers-scale-estimation", "sys-stateless-vs-stateful-architecture"]
            }
        ]
    },
    {
        "id": "course-sys-lvl2",
        "title": "System Design Level 2: Database Design, Indexing & Sharding",
        "slug": "system-design-level-2-databases-sharding",
        "domain": "system-design",
        "color": "#10B981",
        "icon": "Network",
        "is_published": True,
        "skills_taught": ['Scale Math', 'Consistent Hashing', 'Redis Caching', 'Distributed Systems'],
        "description": "SQL vs NoSQL trade-offs, B-Trees vs LSM-Trees, Read Replicas, and Consistent Hashing database sharding rings.",
        "category": "System Design",
        "level": "intermediate",
        "estimated_hours": 16,
        "thumbnail_url": "/assets/courses/sys-databases.png",
        "modules": [
            {
                "id": "mod-sys-2-1",
                "title": "Module 1: Storage Engines & Consistent Hashing",
                "description": "B+ Tree vs LSM Tree writes, master-slave replication lag, and virtual node consistent hashing.",
                "order": 1,
                "lesson_ids": ["sys-storage-engines-btree-lsm", "sys-consistent-hashing-sharding-rings"]
            }
        ]
    },
    {
        "id": "course-sys-lvl3",
        "title": "System Design Level 3: High-Scale Caching, Load Balancing & Queues",
        "slug": "system-design-level-3-caching-queues",
        "domain": "system-design",
        "color": "#10B981",
        "icon": "Network",
        "is_published": True,
        "skills_taught": ['Scale Math', 'Consistent Hashing', 'Redis Caching', 'Distributed Systems'],
        "description": "Redis Cache-Aside, Cache Stampede protection, Layer 4 (TCP) vs Layer 7 (HTTP) Load Balancers, and Kafka log partitioning.",
        "category": "System Design",
        "level": "advanced",
        "estimated_hours": 18,
        "thumbnail_url": "/assets/courses/sys-scaling.png",
        "modules": [
            {
                "id": "mod-sys-3-1",
                "title": "Module 1: Caching Strategies & Event Streams",
                "description": "Cache-Aside vs Write-Through vs Write-Back, Redis clusters, and Apache Kafka consumer groups.",
                "order": 1,
                "lesson_ids": ["sys-redis-cache-aside-stampede-defense", "sys-kafka-event-streaming-queues"]
            }
        ]
    },
    {
        "id": "course-sys-lvl4",
        "title": "System Design Level 4: Distributed Systems & Consensus (Raft)",
        "slug": "system-design-level-4-distributed-consensus",
        "domain": "system-design",
        "color": "#10B981",
        "icon": "Network",
        "is_published": True,
        "skills_taught": ['Scale Math', 'Consistent Hashing', 'Redis Caching', 'Distributed Systems'],
        "description": "CAP & PACELC theorems, Eventual Consistency, 2-Phase Commit (2PC) vs Saga orchestration, and Raft leader election.",
        "category": "System Design",
        "level": "advanced",
        "estimated_hours": 20,
        "thumbnail_url": "/assets/courses/sys-distributed.png",
        "modules": [
            {
                "id": "mod-sys-4-1",
                "title": "Module 1: CAP Theorem, Raft Consensus & Idempotency",
                "description": "Network partition trade-offs, Raft log replication, and idempotency key token generation.",
                "order": 1,
                "lesson_ids": ["sys-cap-pacelc-theorems", "sys-raft-consensus-leader-election"]
            }
        ]
    },
    {
        "id": "course-sys-lvl5",
        "title": "System Design Level 5: Microservices Architecture & Observability",
        "slug": "system-design-level-5-microservices",
        "domain": "system-design",
        "color": "#10B981",
        "icon": "Network",
        "is_published": True,
        "skills_taught": ['Scale Math', 'Consistent Hashing', 'Redis Caching', 'Distributed Systems'],
        "description": "API Gateways (Kong/Envoy), Circuit Breaker pattern (Resilience4j), Distributed Tracing (OpenTelemetry), and Prometheus metrics.",
        "category": "System Design",
        "level": "expert",
        "estimated_hours": 20,
        "thumbnail_url": "/assets/courses/sys-microservices.png",
        "modules": [
            {
                "id": "mod-sys-5-1",
                "title": "Module 1: Circuit Breakers & Distributed Tracing",
                "description": "Cascading failure prevention, API gateway token bucket rate limiting, and OpenTelemetry trace spans.",
                "order": 1,
                "lesson_ids": ["sys-circuit-breaker-api-gateways", "sys-distributed-tracing-opentelemetry"]
            }
        ]
    },
    {
        "id": "course-sys-lvl6",
        "title": "System Design Level 6: Real-World Production Case Studies",
        "slug": "system-design-level-6-case-studies",
        "domain": "system-design",
        "color": "#10B981",
        "icon": "Network",
        "is_published": True,
        "skills_taught": ['Scale Math', 'Consistent Hashing', 'Redis Caching', 'Distributed Systems'],
        "description": "End-to-end architecture blueprints: Global TinyURL, WhatsApp End-to-End Chat, YouTube Video Transcoding Pipeline, and Stripe Payment Processing.",
        "category": "System Design",
        "level": "expert",
        "estimated_hours": 24,
        "thumbnail_url": "/assets/courses/sys-case-studies.png",
        "modules": [
            {
                "id": "mod-sys-6-1",
                "title": "Module 1: Large-Scale System Architectural Blueprints",
                "description": "Architecture diagrams, scale estimations, schema designs, and failure mode analysis for Tier-1 apps.",
                "order": 1,
                "lesson_ids": ["sys-case-study-tinyurl-drive", "sys-case-study-whatsapp-youtube-stripe"]
            }
        ]
    }
]

LESSONS_DATA = [
    {
        "id": "sys-latency-numbers-scale-estimation",
        "title": "Latency Numbers Every Programmer Should Know & Scale Math",
        "slug": "sys-latency-numbers-scale-estimation",
        "domain": "system-design",
        "color": "#10B981",
        "icon": "Network",
        "is_published": True,
        "skills_taught": ['Scale Math', 'Consistent Hashing', 'Redis Caching', 'Distributed Systems'],
        "course_id": "course-sys-lvl1",
        "order": 1,
        "xp_reward": 50,
        "visual_diagram_type": "two_pointers_array",
        "content": """# Latency Comparison Numbers (Jeff Dean)

- L1 cache reference: $0.5 \\text{ ns}$
- Branch mispredict: $5 \\text{ ns}$
- L2 cache reference: $7 \\text{ ns}$
- Mutex lock/unlock: $25 \\text{ ns}$
- Main memory reference (RAM): $100 \\text{ ns}$
- Read 1 MB sequentially from RAM: $250 \\mu\\text{s}$
- SSD random read: $150 \\mu\\text{s}$
- Datacenter round trip (same rack): $500 \\mu\\text{s}$
- Cross-country round trip (SF to NY): $40 \\text{ ms}$
- Cross-continent round trip (US to Europe): $150 \\text{ ms}$

### Back-of-the-Envelope Calculation Rule:
$1 \\text{ million requests / day} \\approx 12 \\text{ requests / second (QPS)}$.
Peak QPS is typically estimated at $2 \\times$ to $5 \\times$ average QPS.
"""
    },
    {
        "id": "sys-stateless-vs-stateful-architecture",
        "title": "Stateless Application Tiers & Shared-Nothing Scaling",
        "slug": "sys-stateless-vs-stateful-architecture",
        "domain": "system-design",
        "color": "#10B981",
        "icon": "Network",
        "is_published": True,
        "skills_taught": ['Scale Math', 'Consistent Hashing', 'Redis Caching', 'Distributed Systems'],
        "course_id": "course-sys-lvl1",
        "order": 2,
        "xp_reward": 55,
        "visual_diagram_type": "two_pointers_array",
        "content": """# Stateless Web Tier Architecture

By delegating state to external distributed datastores (Redis, PostgreSQL), application servers can scale horizontally behind a load balancer with auto-scaling groups based on CPU/RPS thresholds.
"""
    },
    {
        "id": "sys-storage-engines-btree-lsm",
        "title": "Storage Engines: B+ Trees (Read-Heavy) vs LSM Trees (Write-Heavy)",
        "slug": "sys-storage-engines-btree-lsm",
        "domain": "system-design",
        "color": "#10B981",
        "icon": "Network",
        "is_published": True,
        "skills_taught": ['Scale Math', 'Consistent Hashing', 'Redis Caching', 'Distributed Systems'],
        "course_id": "course-sys-lvl2",
        "order": 1,
        "xp_reward": 65,
        "visual_diagram_type": "two_pointers_array",
        "content": """# Storage Engines: B+ Tree vs Log-Structured Merge (LSM) Tree

- **B+ Tree (PostgreSQL, MySQL InnoDB)**: In-place page updates, optimal for $O(\\log N)$ random reads.
- **LSM Tree (RocksDB, Cassandra, Bigtable)**: Sequential append-only writes to MemTable (RAM) and WAL, flushed to immutable SSTables on disk. Optimized for high-throughput writes.
"""
    },
    {
        "id": "sys-consistent-hashing-sharding-rings",
        "title": "Consistent Hashing & Virtual Nodes for Sharding",
        "slug": "sys-consistent-hashing-sharding-rings",
        "domain": "system-design",
        "color": "#10B981",
        "icon": "Network",
        "is_published": True,
        "skills_taught": ['Scale Math', 'Consistent Hashing', 'Redis Caching', 'Distributed Systems'],
        "course_id": "course-sys-lvl2",
        "order": 2,
        "xp_reward": 70,
        "visual_diagram_type": "two_pointers_array",
        "content": """# Consistent Hashing on a 32-Bit Ring

Maps servers and data keys to a circular ring $[0, 2^{32}-1]$. When a new node is added, only $\\frac{K}{N}$ keys are migrated on average. **Virtual Nodes** ensure uniform distribution across the ring.
"""
    },
    {
        "id": "sys-redis-cache-aside-stampede-defense",
        "title": "Redis Caching Patterns, Cache Stampede & Thundering Herd",
        "slug": "sys-redis-cache-aside-stampede-defense",
        "domain": "system-design",
        "color": "#10B981",
        "icon": "Network",
        "is_published": True,
        "skills_taught": ['Scale Math', 'Consistent Hashing', 'Redis Caching', 'Distributed Systems'],
        "course_id": "course-sys-lvl3",
        "order": 1,
        "xp_reward": 75,
        "visual_diagram_type": "two_pointers_array",
        "content": """# Caching Patterns & Stampede Mitigation

### 1. Cache-Aside Pattern
1. App looks in Redis cache.
2. On cache hit: returns cached payload.
3. On cache miss: queries database, writes result into Redis with TTL, returns response.

### 2. Defeating Cache Stampede (Thundering Herd)
- Distributed Mutex lock (`SET key val NX EX 10`) so only 1 request recalculates the missing key while others await.
- Early probabilistic expiration (XFetch algorithm).
"""
    },
    {
        "id": "sys-kafka-event-streaming-queues",
        "title": "Apache Kafka: Distributed Commit Logs & Partitioning",
        "slug": "sys-kafka-event-streaming-queues",
        "domain": "system-design",
        "color": "#10B981",
        "icon": "Network",
        "is_published": True,
        "skills_taught": ['Scale Math', 'Consistent Hashing', 'Redis Caching', 'Distributed Systems'],
        "course_id": "course-sys-lvl3",
        "order": 2,
        "xp_reward": 80,
        "visual_diagram_type": "two_pointers_array",
        "content": """# Apache Kafka Distributed Streaming Architecture

Topics are divided into **Partitions** replicated across broker clusters. Consumers in the same consumer group process partitions in parallel, guaranteeing total ordering *within* each partition.
"""
    },
    {
        "id": "sys-cap-pacelc-theorems",
        "title": "The CAP & PACELC Theorems in Distributed Systems",
        "slug": "sys-cap-pacelc-theorems",
        "domain": "system-design",
        "color": "#10B981",
        "icon": "Network",
        "is_published": True,
        "skills_taught": ['Scale Math', 'Consistent Hashing', 'Redis Caching', 'Distributed Systems'],
        "course_id": "course-lvl4",
        "order": 1,
        "xp_reward": 85,
        "visual_diagram_type": "two_pointers_array",
        "content": """# The CAP & PACELC Theorems

### PACELC Formulation:
- **If Partition (P)**: Trade off between **Availability (A)** and **Consistency (C)**.
- **Else (E)**: Trade off between **Latency (L)** and **Consistency (C)**.

Examples:
- **PA/EL**: DynamoDB, Cassandra
- **PC/EC**: Spanner, CockroachDB, Raft
"""
    },
    {
        "id": "sys-raft-consensus-leader-election",
        "title": "Distributed Consensus: Raft Protocol & Idempotency",
        "slug": "sys-raft-consensus-leader-election",
        "domain": "system-design",
        "color": "#10B981",
        "icon": "Network",
        "is_published": True,
        "skills_taught": ['Scale Math', 'Consistent Hashing', 'Redis Caching', 'Distributed Systems'],
        "course_id": "course-sys-lvl4",
        "order": 2,
        "xp_reward": 90,
        "visual_diagram_type": "two_pointers_array",
        "content": """# Raft Consensus & Idempotent Transactions

Raft achieves consensus via:
1. **Leader Election**: Randomized election timers preventing split votes.
2. **Log Replication**: Leader forces follower logs to match its own before committing entries once a quorum (majority $> N/2$) acknowledges.
"""
    },
    {
        "id": "sys-circuit-breaker-api-gateways",
        "title": "Circuit Breakers, Bulkheads & API Gateways",
        "slug": "sys-circuit-breaker-api-gateways",
        "domain": "system-design",
        "color": "#10B981",
        "icon": "Network",
        "is_published": True,
        "skills_taught": ['Scale Math', 'Consistent Hashing', 'Redis Caching', 'Distributed Systems'],
        "course_id": "course-sys-lvl5",
        "order": 1,
        "xp_reward": 85,
        "visual_diagram_type": "two_pointers_array",
        "content": """# Resilience Patterns in Microservices

- **Circuit Breaker**: Transitions between `CLOSED` $\\to$ `OPEN` $\\to$ `HALF-OPEN` states when downstream error rates exceed $50\\%$, returning fast fallbacks rather than exhausting thread pools.
- **Bulkhead Pattern**: Isolates resource pools per downstream service.
"""
    },
    {
        "id": "sys-distributed-tracing-opentelemetry",
        "title": "Observability: OpenTelemetry Distributed Traces & Metrics",
        "slug": "sys-distributed-tracing-opentelemetry",
        "domain": "system-design",
        "color": "#10B981",
        "icon": "Network",
        "is_published": True,
        "skills_taught": ['Scale Math', 'Consistent Hashing', 'Redis Caching', 'Distributed Systems'],
        "course_id": "course-sys-lvl5",
        "order": 2,
        "xp_reward": 90,
        "visual_diagram_type": "two_pointers_array",
        "content": """# Distributed Tracing with W3C Trace Context

Propagating `traceparent` headers across microservice RPC boundaries to reconstruct complete request waterfalls across asynchronous queues and database queries.
"""
    },
    {
        "id": "sys-case-study-tinyurl-drive",
        "title": "System Design Case Studies: TinyURL & Distributed File Storage",
        "slug": "sys-case-study-tinyurl-drive",
        "domain": "system-design",
        "color": "#10B981",
        "icon": "Network",
        "is_published": True,
        "skills_taught": ['Scale Math', 'Consistent Hashing', 'Redis Caching', 'Distributed Systems'],
        "course_id": "course-sys-lvl6",
        "order": 1,
        "xp_reward": 95,
        "visual_diagram_type": "two_pointers_array",
        "content": """# Case Study 1: Global URL Shortener (TinyURL)

1. **Requirements**: 100M URLs created/month, $100:1$ read/write ratio (10B reads/month $\\implies 3,800$ read QPS).
2. **Key Generation**: Pre-generated Base62 token server with range allocations.
3. **Storage**: NoSQL Key-Value store with Redis Cache-Aside.

# Case Study 2: Distributed File Storage (Google Drive)
- Chunking files into 4MB blocks
- Deduplication via SHA-256 block hash indexing
- Asynchronous cloud block storage (S3) with metadata databases
"""
    },
    {
        "id": "sys-case-study-whatsapp-youtube-stripe",
        "title": "System Design Case Studies: WhatsApp, YouTube & Stripe Payments",
        "slug": "sys-case-study-whatsapp-youtube-stripe",
        "domain": "system-design",
        "color": "#10B981",
        "icon": "Network",
        "is_published": True,
        "skills_taught": ['Scale Math', 'Consistent Hashing', 'Redis Caching', 'Distributed Systems'],
        "course_id": "course-sys-lvl6",
        "order": 2,
        "xp_reward": 100,
        "visual_diagram_type": "two_pointers_array",
        "content": """# Case Study 3: Real-Time Chat (WhatsApp)
- Persistent WebSocket gateway servers maintaining connection tables
- Erlang / Elixir message brokers
- End-to-end encryption (Signal Protocol)

# Case Study 4: Video Streaming (YouTube)
- Asynchronous DAG video transcoding pipelines (HLS / MPEG-DASH)
- Global Edge CDN multi-bitrate delivery

# Case Study 5: Distributed Idempotent Payment Processing (Stripe)
- Idempotency keys stored with atomic transactions
- Two-Phase Commit and Saga orchestrators handling bank webhooks
"""
    }
]

QUIZZES_DATA = [
    {
        "id": "quiz-sys-lvl1",
        "lesson_id": "sys-latency-numbers-scale-estimation",
        "title": "System Design & Distributed Architecture Diagnostic",
        "passing_score": 80,
        "questions": [
            {
                "id": "q-sys-1-1",
                "question": "In consistent hashing, what is the primary purpose of virtual nodes?",
                "options": [
                    "To encrypt all payload packets",
                    "To ensure uniform data distribution and prevent hotspot imbalances across the ring",
                    "To eliminate the need for load balancers",
                    "To convert SQL queries into NoSQL"
                ],
                "correct_option_index": 1,
                "explanation": "Virtual nodes map each physical server to multiple positions on the hash ring, smoothing out the statistical distribution of keys."
            }
        ]
    }
]

SKILLS_DATA = [
    {
        "id": "skill-sys-architecture",
        "name": "Distributed System Design & High Scale",
        "category": "System Design",
        "level": 1,
        "unlocked": True,
        "progress": 0.0,
        "prerequisites": [],
        "description": "Master Scale Estimation, Caching, Consistent Hashing, Raft Consensus, and Production Case Studies."
    }
]
