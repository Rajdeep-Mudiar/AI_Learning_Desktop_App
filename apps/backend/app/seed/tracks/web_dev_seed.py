"""
Web Development Track Seed Data
Levels 1 - 7 covering:
- Level 1: Internet Fundamentals & Protocols
- Level 2: Semantic HTML & Accessibility
- Level 3: Modern CSS Layouts (Flexbox, Grid) & Animations
- Level 4: JavaScript ES6+ & TypeScript Type Systems
- Level 5: React 18 & Next.js App Router Architecture
- Level 6: Backend Engineering (FastAPI / Express & WebSockets)
- Level 7: Databases (PostgreSQL, MongoDB) & Advanced Web Scale
"""

COURSES_DATA = [
    {
        "id": "course-web-lvl1",
        "title": "Web Dev Level 1: Internet Architecture, DNS & HTTP/HTTPS",
        "slug": "web-level-1-internet-fundamentals",
        "domain": "web-dev",
        "color": "#06B6D4",
        "icon": "Globe",
        "is_published": True,
        "skills_taught": ['HTML5/CSS3', 'TypeScript', 'React 18', 'Backend Systems', 'PostgreSQL'],
        "description": "Understand how the Internet works: IP routing, DNS resolution, TCP/UDP sockets, HTTP/2 & HTTP/3 request/response lifecycle, Cookies, and CORS headers.",
        "category": "Web Development",
        "level": "beginner",
        "estimated_hours": 12,
        "thumbnail_url": "/assets/courses/web-internet.png",
        "modules": [
            {
                "id": "mod-web-1-1",
                "title": "Module 1: The Request-Response Cycle & DNS",
                "description": "Client-server architecture, IP addressing, DNS hierarchy, and TLS certificates.",
                "order": 1,
                "lesson_ids": ["web-internet-lifecycle-dns", "web-http-headers-cors-cookies"]
            }
        ]
    },
    {
        "id": "course-web-lvl2",
        "title": "Web Dev Level 2: Semantic HTML5, Forms & Accessibility",
        "slug": "web-level-2-html5-semantics",
        "domain": "web-dev",
        "color": "#06B6D4",
        "icon": "Globe",
        "is_published": True,
        "skills_taught": ['HTML5/CSS3', 'TypeScript', 'React 18', 'Backend Systems', 'PostgreSQL'],
        "description": "Master semantic document outlines, ARIA roles, modern accessible forms, and search engine optimization (SEO) foundations.",
        "category": "Web Development",
        "level": "beginner",
        "estimated_hours": 10,
        "thumbnail_url": "/assets/courses/web-html.png",
        "modules": [
            {
                "id": "mod-web-2-1",
                "title": "Module 1: Semantic Structure & Accessibility (a11y)",
                "description": "Semantic landmarks (`<main>`, `<article>`), Accessible forms, and Core Web Vitals.",
                "order": 1,
                "lesson_ids": ["web-semantic-html-accessibility", "web-forms-validation-seo"]
            }
        ]
    },
    {
        "id": "course-web-lvl3",
        "title": "Web Dev Level 3: Modern CSS, Flexbox, Grid & Animations",
        "slug": "web-level-3-css-flexbox-grid",
        "domain": "web-dev",
        "color": "#06B6D4",
        "icon": "Globe",
        "is_published": True,
        "skills_taught": ['HTML5/CSS3', 'TypeScript', 'React 18', 'Backend Systems', 'PostgreSQL'],
        "description": "Master CSS Box Model, Stacking Contexts (z-index), Flexbox alignment, CSS Grid 2D templates, and hardware-accelerated animations.",
        "category": "Web Development",
        "level": "intermediate",
        "estimated_hours": 14,
        "thumbnail_url": "/assets/courses/web-css.png",
        "modules": [
            {
                "id": "mod-web-3-1",
                "title": "Module 1: Flexbox, CSS Grid & Stacking Contexts",
                "description": "2D layout geometry, subgrid, z-index mechanics, and responsive media queries.",
                "order": 1,
                "lesson_ids": ["web-css-box-stacking-context", "web-flexbox-grid-responsive"]
            }
        ]
    },
    {
        "id": "course-web-lvl4",
        "title": "Web Dev Level 4: JavaScript V8 Internals & TypeScript",
        "slug": "web-level-4-javascript-typescript",
        "domain": "web-dev",
        "color": "#06B6D4",
        "icon": "Globe",
        "is_published": True,
        "skills_taught": ['HTML5/CSS3', 'TypeScript', 'React 18', 'Backend Systems', 'PostgreSQL'],
        "description": "Event Loop, Microtasks vs Macrotasks, Closures, Promises, async/await, and TypeScript Generics, Utility Types & Narrowing.",
        "category": "Web Development",
        "level": "intermediate",
        "estimated_hours": 18,
        "thumbnail_url": "/assets/courses/web-js-ts.png",
        "modules": [
            {
                "id": "mod-web-4-1",
                "title": "Module 1: Event Loop, Closures & Async JS",
                "description": "Call stack execution, microtask queues, promises, and Fetch API.",
                "order": 1,
                "lesson_ids": ["web-event-loop-microtasks-closures", "web-typescript-generics-narrowing"]
            }
        ]
    },
    {
        "id": "course-web-lvl5",
        "title": "Web Dev Level 5: React 18 & Next.js App Router Architecture",
        "slug": "web-level-5-react-nextjs",
        "domain": "web-dev",
        "color": "#06B6D4",
        "icon": "Globe",
        "is_published": True,
        "skills_taught": ['HTML5/CSS3', 'TypeScript', 'React 18', 'Backend Systems', 'PostgreSQL'],
        "description": "React reconciliation, Fiber tree, Custom Hooks, Server Components (RSC), Server Actions, and SSR/SSG/ISR caching strategies.",
        "category": "Web Development",
        "level": "advanced",
        "estimated_hours": 20,
        "thumbnail_url": "/assets/courses/web-react.png",
        "modules": [
            {
                "id": "mod-web-5-1",
                "title": "Module 1: React Fiber & State Management",
                "description": "Virtual DOM diffing, useEffect lifecycle, Context API, and state machines.",
                "order": 1,
                "lesson_ids": ["web-react-fiber-reconciliation", "web-nextjs-app-router-rsc"]
            }
        ]
    },
    {
        "id": "course-web-lvl6",
        "title": "Web Dev Level 6: Backend Systems (FastAPI / Express & WebSockets)",
        "slug": "web-level-6-backend-systems",
        "domain": "web-dev",
        "color": "#06B6D4",
        "icon": "Globe",
        "is_published": True,
        "skills_taught": ['HTML5/CSS3', 'TypeScript', 'React 18', 'Backend Systems', 'PostgreSQL'],
        "description": "REST API design, JWT middleware, OAuth 2.0 PKCE, Real-time WebSockets, and distributed rate limiting.",
        "category": "Web Development",
        "level": "advanced",
        "estimated_hours": 18,
        "thumbnail_url": "/assets/courses/web-backend.png",
        "modules": [
            {
                "id": "mod-web-6-1",
                "title": "Module 1: High-Throughput REST & WebSockets",
                "description": "Asynchronous request pipelines, token bucket rate limiters, and full-duplex WebSocket sockets.",
                "order": 1,
                "lesson_ids": ["web-backend-rest-jwt-oauth", "web-realtime-websockets-streaming"]
            }
        ]
    },
    {
        "id": "course-web-lvl7",
        "title": "Web Dev Level 7: Databases, Redis Caching & Microservices",
        "slug": "web-level-7-databases-microservices",
        "domain": "web-dev",
        "color": "#06B6D4",
        "icon": "Globe",
        "is_published": True,
        "skills_taught": ['HTML5/CSS3', 'TypeScript', 'React 18', 'Backend Systems', 'PostgreSQL'],
        "description": "PostgreSQL indexing & ACID transactions, MongoDB aggregation pipelines, Redis Cache-Aside, Docker, and Nginx reverse proxies.",
        "category": "Web Development",
        "level": "expert",
        "estimated_hours": 22,
        "thumbnail_url": "/assets/courses/web-databases.png",
        "modules": [
            {
                "id": "mod-web-7-1",
                "title": "Module 1: SQL/NoSQL & Production Microservices",
                "description": "B-Tree indexes, isolation levels, Redis caching, Docker containerization, and CI/CD pipelines.",
                "order": 1,
                "lesson_ids": ["web-databases-sql-nosql-indexing", "web-microservices-docker-nginx"]
            }
        ]
    }
]

LESSONS_DATA = [
    {
        "id": "web-internet-lifecycle-dns",
        "title": "The Web Request Lifecycle: DNS, TCP Sockets & TLS 1.3",
        "slug": "web-internet-lifecycle-dns",
        "domain": "web-dev",
        "color": "#06B6D4",
        "icon": "Globe",
        "is_published": True,
        "skills_taught": ['HTML5/CSS3', 'TypeScript', 'React 18', 'Backend Systems', 'PostgreSQL'],
        "course_id": "course-web-lvl1",
        "order": 1,
        "xp_reward": 50,
        "visual_diagram_type": "two_pointers_array",
        "content": """# What Happens When You Type a URL in a Browser?

1. **DNS Resolution**: Browser Cache $\\to$ OS Cache $\\to$ Resolving Name Server $\\to$ Root DNS $\\to$ TLD Server $\\to$ Authoritative DNS.
2. **TCP 3-Way Handshake**: `SYN` $\\to$ `SYN-ACK` $\\to$ `ACK`.
3. **TLS 1.3 Handshake**: 1-RTT key exchange using Diffie-Hellman + AES-GCM symmetric session keys.
4. **HTTP Request & Response**: Headers, body streams, and browser DOM rendering.
"""
    },
    {
        "id": "web-http-headers-cors-cookies",
        "title": "HTTP/2, HTTP/3 QUIC, CORS Headers & Secure Cookies",
        "slug": "web-http-headers-cors-cookies",
        "domain": "web-dev",
        "color": "#06B6D4",
        "icon": "Globe",
        "is_published": True,
        "skills_taught": ['HTML5/CSS3', 'TypeScript', 'React 18', 'Backend Systems', 'PostgreSQL'],
        "course_id": "course-web-lvl1",
        "order": 2,
        "xp_reward": 55,
        "visual_diagram_type": "two_pointers_array",
        "content": """# Cross-Origin Resource Sharing (CORS) & Cookies

### CORS Preflight (`OPTIONS` request)
```http
OPTIONS /api/data HTTP/1.1
Origin: https://clientapp.com
Access-Control-Request-Method: POST
Access-Control-Request-Headers: Authorization

HTTP/1.1 204 No Content
Access-Control-Allow-Origin: https://clientapp.com
Access-Control-Allow-Methods: GET, POST, OPTIONS
Access-Control-Allow-Headers: Authorization
Access-Control-Allow-Credentials: true
```

### Secure Cookie Attributes:
`Set-Cookie: sessionId=abc123; Secure; HttpOnly; SameSite=Strict; Path=/`
"""
    },
    {
        "id": "web-semantic-html-accessibility",
        "title": "Semantic HTML5, ARIA Landmarks & Accessible Trees",
        "slug": "web-semantic-html-accessibility",
        "domain": "web-dev",
        "color": "#06B6D4",
        "icon": "Globe",
        "is_published": True,
        "skills_taught": ['HTML5/CSS3', 'TypeScript', 'React 18', 'Backend Systems', 'PostgreSQL'],
        "course_id": "course-web-lvl2",
        "order": 1,
        "xp_reward": 50,
        "visual_diagram_type": "two_pointers_array",
        "content": """# Semantic HTML5 & Web Accessibility (WCAG 2.2)

Semantic landmarks (`<header>`, `<nav>`, `<main>`, `<article>`, `<aside>`, `<footer>`) construct screen reader accessibility trees (AOM).
```html
<main id="content" role="main">
  <article>
    <header>
      <h1>Understanding Web Standards</h1>
      <time datetime="2026-09-21">Sept 21, 2026</time>
    </header>
    <p>Accessible semantic document flow ensures SEO and keyboard navigation.</p>
  </article>
</main>
```
"""
    },
    {
        "id": "web-forms-validation-seo",
        "title": "Modern Form Validation, OpenGraph & Core Web Vitals",
        "slug": "web-forms-validation-seo",
        "domain": "web-dev",
        "color": "#06B6D4",
        "icon": "Globe",
        "is_published": True,
        "skills_taught": ['HTML5/CSS3', 'TypeScript', 'React 18', 'Backend Systems', 'PostgreSQL'],
        "course_id": "course-web-lvl2",
        "order": 2,
        "xp_reward": 55,
        "visual_diagram_type": "two_pointers_array",
        "content": """# Form Validation & Technical SEO

- Constraint validation API (`checkValidity()`, `reportValidity()`)
- OpenGraph meta tags (`og:title`, `og:image`, `og:description`)
- Core Web Vitals: LCP (Largest Contentful Paint), INP (Interaction to Next Paint), CLS (Cumulative Layout Shift).
"""
    },
    {
        "id": "web-css-box-stacking-context",
        "title": "CSS Box Model, Specificity & Stacking Contexts",
        "slug": "web-css-box-stacking-context",
        "domain": "web-dev",
        "color": "#06B6D4",
        "icon": "Globe",
        "is_published": True,
        "skills_taught": ['HTML5/CSS3', 'TypeScript', 'React 18', 'Backend Systems', 'PostgreSQL'],
        "course_id": "course-web-lvl3",
        "order": 1,
        "xp_reward": 60,
        "visual_diagram_type": "two_pointers_array",
        "content": """# CSS Box Model & Stacking Contexts (z-index)

### Stacking Context Creation:
A new stacking context is created when an element has:
- `position: absolute/relative` and `z-index != auto`
- `position: fixed` or `position: sticky`
- `opacity < 1`
- `transform`, `filter`, or `perspective != none`
- `isolation: isolate`
"""
    },
    {
        "id": "web-flexbox-grid-responsive",
        "title": "Flexbox 1D & CSS Grid 2D Fractional Template Layouts",
        "slug": "web-flexbox-grid-responsive",
        "domain": "web-dev",
        "color": "#06B6D4",
        "icon": "Globe",
        "is_published": True,
        "skills_taught": ['HTML5/CSS3', 'TypeScript', 'React 18', 'Backend Systems', 'PostgreSQL'],
        "course_id": "course-web-lvl3",
        "order": 2,
        "xp_reward": 65,
        "visual_diagram_type": "two_pointers_array",
        "content": """# CSS Grid & Flexbox Alignment

```css
.dashboard-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: var(--space-md);
  align-items: stretch;
}
```
"""
    },
    {
        "id": "web-event-loop-microtasks-closures",
        "title": "JavaScript V8 Event Loop, Microtasks & Closures",
        "slug": "web-event-loop-microtasks-closures",
        "domain": "web-dev",
        "color": "#06B6D4",
        "icon": "Globe",
        "is_published": True,
        "skills_taught": ['HTML5/CSS3', 'TypeScript', 'React 18', 'Backend Systems', 'PostgreSQL'],
        "course_id": "course-web-lvl4",
        "order": 1,
        "xp_reward": 70,
        "visual_diagram_type": "two_pointers_array",
        "content": """# V8 Event Loop & Execution Priorities

1. Execute synchronous script in **Call Stack**.
2. Drain **Microtask Queue** (`Promise.then()`, `queueMicrotask()`, `MutationObserver`).
3. Execute one task from **Macrotask Queue** (`setTimeout()`, `setInterval()`, I/O).
4. Run browser render cycle (requestAnimationFrame, layout, paint).
"""
    },
    {
        "id": "web-typescript-generics-narrowing",
        "title": "TypeScript Generics, Conditional Types & Narrowing",
        "slug": "web-typescript-generics-narrowing",
        "domain": "web-dev",
        "color": "#06B6D4",
        "icon": "Globe",
        "is_published": True,
        "skills_taught": ['HTML5/CSS3', 'TypeScript', 'React 18', 'Backend Systems', 'PostgreSQL'],
        "course_id": "course-web-lvl4",
        "order": 2,
        "xp_reward": 75,
        "visual_diagram_type": "two_pointers_array",
        "content": """# TypeScript Advanced Type Systems

```typescript
type ApiResponse<T> = {
  data: T;
  status: 'success' | 'error';
  timestamp: number;
};

// Generic Repository Interface
interface Repository<T extends { id: string }> {
  findById(id: string): Promise<T | null>;
  save(entity: T): Promise<T>;
}
```
"""
    },
    {
        "id": "web-react-fiber-reconciliation",
        "title": "React 18 Fiber Reconciliation & Custom Hooks",
        "slug": "web-react-fiber-reconciliation",
        "domain": "web-dev",
        "color": "#06B6D4",
        "icon": "Globe",
        "is_published": True,
        "skills_taught": ['HTML5/CSS3', 'TypeScript', 'React 18', 'Backend Systems', 'PostgreSQL'],
        "course_id": "course-web-lvl5",
        "order": 1,
        "xp_reward": 80,
        "visual_diagram_type": "two_pointers_array",
        "content": """# React 18 Fiber & Concurrent Rendering

React Fiber decomposes component updates into interruptible work units, prioritizing urgent user inputs over background re-renders via `useTransition()` and `useDeferredValue()`.
"""
    },
    {
        "id": "web-nextjs-app-router-rsc",
        "title": "Next.js App Router, Server Components & Server Actions",
        "slug": "web-nextjs-app-router-rsc",
        "domain": "web-dev",
        "color": "#06B6D4",
        "icon": "Globe",
        "is_published": True,
        "skills_taught": ['HTML5/CSS3', 'TypeScript', 'React 18', 'Backend Systems', 'PostgreSQL'],
        "course_id": "course-web-lvl5",
        "order": 2,
        "xp_reward": 85,
        "visual_diagram_type": "two_pointers_array",
        "content": """# Next.js Server Components (RSC) vs Client Components

Server Components execute strictly on the Node.js server, streaming serialized JSON payloads to the browser without shipping component JavaScript bundles.
"""
    },
    {
        "id": "web-backend-rest-jwt-oauth",
        "title": "High-Throughput REST APIs, JWT Auth & Rate Limiting",
        "slug": "web-backend-rest-jwt-oauth",
        "domain": "web-dev",
        "color": "#06B6D4",
        "icon": "Globe",
        "is_published": True,
        "skills_taught": ['HTML5/CSS3', 'TypeScript', 'React 18', 'Backend Systems', 'PostgreSQL'],
        "course_id": "course-web-lvl6",
        "order": 1,
        "xp_reward": 85,
        "visual_diagram_type": "two_pointers_array",
        "content": """# FastAPI / Node.js REST API Architecture

Designing idempotent endpoints, Pydantic data validation, JWT token revocation, and Redis token bucket rate limiting.
"""
    },
    {
        "id": "web-realtime-websockets-streaming",
        "title": "Real-Time WebSockets & Server-Sent Events (SSE)",
        "slug": "web-realtime-websockets-streaming",
        "domain": "web-dev",
        "color": "#06B6D4",
        "icon": "Globe",
        "is_published": True,
        "skills_taught": ['HTML5/CSS3', 'TypeScript', 'React 18', 'Backend Systems', 'PostgreSQL'],
        "course_id": "course-web-lvl6",
        "order": 2,
        "xp_reward": 85,
        "visual_diagram_type": "two_pointers_array",
        "content": """# Full-Duplex WebSockets & Streaming

WebSocket protocol upgrade (`Connection: Upgrade`, `Upgrade: websocket`) allowing sub-millisecond bidirectional communication.
"""
    },
    {
        "id": "web-databases-sql-nosql-indexing",
        "title": "PostgreSQL Indexing, B-Trees, ACID & MongoDB Aggregation",
        "slug": "web-databases-sql-nosql-indexing",
        "domain": "web-dev",
        "color": "#06B6D4",
        "icon": "Globe",
        "is_published": True,
        "skills_taught": ['HTML5/CSS3', 'TypeScript', 'React 18', 'Backend Systems', 'PostgreSQL'],
        "course_id": "course-web-lvl7",
        "order": 1,
        "xp_reward": 90,
        "visual_diagram_type": "two_pointers_array",
        "content": """# Database Query Optimization & Indexing

- **B-Tree Indexes**: Logarithmic index lookups on primary/foreign keys.
- **ACID Isolation Levels**: Read Uncommitted, Read Committed, Repeatable Read, Serializable.
- **MongoDB Aggregation**: `$match`, `$group`, `$lookup`, `$unwind` pipelines.
"""
    },
    {
        "id": "web-microservices-docker-nginx",
        "title": "Microservices, Docker Containers & Nginx Reverse Proxy",
        "slug": "web-microservices-docker-nginx",
        "domain": "web-dev",
        "color": "#06B6D4",
        "icon": "Globe",
        "is_published": True,
        "skills_taught": ['HTML5/CSS3', 'TypeScript', 'React 18', 'Backend Systems', 'PostgreSQL'],
        "course_id": "course-web-lvl7",
        "order": 2,
        "xp_reward": 95,
        "visual_diagram_type": "two_pointers_array",
        "content": """# Microservices & Containerized Infrastructure

Multi-stage Docker builds, Kubernetes pods, and Nginx reverse proxy load balancing with upstream health checks.
"""
    }
]

QUIZZES_DATA = [
    {
        "id": "quiz-web-lvl1",
        "lesson_id": "web-internet-lifecycle-dns",
        "title": "Web Architecture & Protocol Diagnostic",
        "passing_score": 80,
        "questions": [
            {
                "id": "q-web-1-1",
                "question": "What is the primary benefit of TLS 1.3 over TLS 1.2?",
                "options": [
                    "It replaces TCP with UDP entirely",
                    "It reduces the cryptographic handshake latency from 2-RTT to 1-RTT",
                    "It eliminates the need for SSL certificates",
                    "It encodes all data with Base64"
                ],
                "correct_option_index": 1,
                "explanation": "TLS 1.3 optimizes the handshake key exchange to 1-RTT (and 0-RTT resumption), significantly reducing connection latency."
            }
        ]
    }
]

SKILLS_DATA = [
    {
        "id": "skill-web-frontend",
        "name": "Frontend & React Engineering",
        "category": "Web Development",
        "level": 1,
        "unlocked": True,
        "progress": 0.0,
        "prerequisites": [],
        "description": "Master HTML5, CSS Grid, TypeScript, and React 18 / Next.js."
    },
    {
        "id": "skill-web-backend-cloud",
        "name": "Backend Systems & Database Architecture",
        "category": "Web Development",
        "level": 2,
        "unlocked": True,
        "progress": 0.0,
        "prerequisites": ["skill-web-frontend"],
        "description": "Master REST APIs, WebSockets, PostgreSQL, MongoDB, and Docker."
    }
]
