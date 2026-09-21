"""
App Development (Flutter & Mobile) Track Seed Data
Levels 1 - 5 + Advanced covering:
- Level 1: Dart Fundamentals (OOP, Null Safety, Futures, Streams)
- Level 2: Flutter Widgets & Layouts (Stateless/Stateful, Row/Column/Stack, GridView)
- Level 3: APIs, Networking & Backend Integration (REST, JSON, WebSockets)
- Level 4: State Management (Provider, Riverpod, Bloc)
- Level 5: Databases & Offline Sync (SQLite, Hive, SharedPreferences, Firebase)
- Advanced: Clean Architecture, Native Bridges, Performance, Real-World Projects
"""

COURSES_DATA = [
    {
        "id": "course-app-lvl1",
        "title": "App Dev Level 1: Dart Language & Reactive Async Programming",
        "slug": "app-level-1-dart-foundations",
        "domain": "app-dev",
        "color": "#EC4899",
        "icon": "Smartphone",
        "is_published": True,
        "skills_taught": ['Dart 3', 'Flutter Layouts', 'BLoC Pattern', 'SQLite Drift', 'Clean Architecture'],
        "description": "Master Dart 3.0: Strong typing, Sound Null Safety, Object-Oriented patterns, Futures, Streams, and isolates.",
        "category": "App Development",
        "level": "beginner",
        "estimated_hours": 12,
        "thumbnail_url": "/assets/courses/app-dart.png",
        "modules": [
            {
                "id": "mod-app-1-1",
                "title": "Module 1: Dart OOP & Sound Null Safety",
                "description": "Classes, Mixins, Pattern matching, and Null safety boundaries.",
                "order": 1,
                "lesson_ids": ["app-dart-null-safety-oop", "app-dart-futures-streams-isolates"]
            }
        ]
    },
    {
        "id": "course-app-lvl2",
        "title": "App Dev Level 2: Flutter Rendering Pipeline & UI Layouts",
        "slug": "app-level-2-flutter-ui-layouts",
        "domain": "app-dev",
        "color": "#EC4899",
        "icon": "Smartphone",
        "is_published": True,
        "skills_taught": ['Dart 3', 'Flutter Layouts', 'BLoC Pattern', 'SQLite Drift', 'Clean Architecture'],
        "description": "Widget Tree, Element Tree, RenderObject pipeline, Impeller rendering, Flex layouts, CustomPaint, and responsive canvases.",
        "category": "App Development",
        "level": "beginner",
        "estimated_hours": 14,
        "thumbnail_url": "/assets/courses/app-flutter-ui.png",
        "modules": [
            {
                "id": "mod-app-2-1",
                "title": "Module 1: Flutter Three Trees & Custom Layouts",
                "description": "Stateless vs Stateful, RenderObjects, CustomPainter, and Slivers.",
                "order": 1,
                "lesson_ids": ["app-flutter-three-trees-impeller", "app-flutter-layouts-slivers-custompaint"]
            }
        ]
    },
    {
        "id": "course-app-lvl3",
        "title": "App Dev Level 3: Mobile Networking & REST/WebSocket APIs",
        "slug": "app-level-3-networking-apis",
        "domain": "app-dev",
        "color": "#EC4899",
        "icon": "Smartphone",
        "is_published": True,
        "skills_taught": ['Dart 3', 'Flutter Layouts', 'BLoC Pattern', 'SQLite Drift', 'Clean Architecture'],
        "description": "Dio HTTP client, JSON code generation, JWT token interceptors, offline caching, and real-time streaming.",
        "category": "App Development",
        "level": "intermediate",
        "estimated_hours": 14,
        "thumbnail_url": "/assets/courses/app-networking.png",
        "modules": [
            {
                "id": "mod-app-3-1",
                "title": "Module 1: Robust Networking & Interceptors",
                "description": "Dio interceptors, automatic retry with exponential backoff, and WebSocket streaming.",
                "order": 1,
                "lesson_ids": ["app-dio-networking-interceptors", "app-mobile-websockets-sync"]
            }
        ]
    },
    {
        "id": "course-app-lvl4",
        "title": "App Dev Level 4: State Management (Bloc, Riverpod & Provider)",
        "slug": "app-level-4-state-management",
        "domain": "app-dev",
        "color": "#EC4899",
        "icon": "Smartphone",
        "is_published": True,
        "skills_taught": ['Dart 3', 'Flutter Layouts', 'BLoC Pattern', 'SQLite Drift', 'Clean Architecture'],
        "description": "Unidirectional data flow, BLoC pattern (Events/States), Riverpod compile-safe dependency injection, and state restoration.",
        "category": "App Development",
        "level": "advanced",
        "estimated_hours": 18,
        "thumbnail_url": "/assets/courses/app-state.png",
        "modules": [
            {
                "id": "mod-app-4-1",
                "title": "Module 1: Enterprise BLoC & Riverpod Architecture",
                "description": "Event-driven state machines, selector rebuild optimization, and scoped dependency graphs.",
                "order": 1,
                "lesson_ids": ["app-bloc-event-driven-architecture", "app-riverpod-dependency-injection"]
            }
        ]
    },
    {
        "id": "course-app-lvl5",
        "title": "App Dev Level 5: Offline Storage, SQLite, Hive & Firebase",
        "slug": "app-level-5-databases-offline-sync",
        "domain": "app-dev",
        "color": "#EC4899",
        "icon": "Smartphone",
        "is_published": True,
        "skills_taught": ['Dart 3', 'Flutter Layouts', 'BLoC Pattern', 'SQLite Drift', 'Clean Architecture'],
        "description": "Embedded SQLite with Drift/Floor, ultra-fast Hive binary boxes, SharedPreferences, and Firebase Cloud Firestore integration.",
        "category": "App Development",
        "level": "advanced",
        "estimated_hours": 16,
        "thumbnail_url": "/assets/courses/app-storage.png",
        "modules": [
            {
                "id": "mod-app-5-1",
                "title": "Module 1: Embedded Databases & Cache Synchronization",
                "description": "SQLite relational schema migrations, Hive NoSQL boxes, and offline delta synchronization.",
                "order": 1,
                "lesson_ids": ["app-sqlite-drift-relational-storage", "app-hive-firebase-offline-sync"]
            }
        ]
    },
    {
        "id": "course-app-lvl6",
        "title": "App Dev Level 6: Clean Architecture & Native Platform Bridges",
        "slug": "app-level-6-clean-architecture-native",
        "domain": "app-dev",
        "color": "#EC4899",
        "icon": "Smartphone",
        "is_published": True,
        "skills_taught": ['Dart 3', 'Flutter Layouts', 'BLoC Pattern', 'SQLite Drift', 'Clean Architecture'],
        "description": "Domain-Driven Design (Presentation, Domain, Data layers), MethodChannels (Kotlin/Swift JNI), 120 FPS profiling, and App Store releases.",
        "category": "App Development",
        "level": "expert",
        "estimated_hours": 20,
        "thumbnail_url": "/assets/courses/app-clean-arch.png",
        "modules": [
            {
                "id": "mod-app-6-1",
                "title": "Module 1: Clean Architecture & Native JNI Bridges",
                "description": "Repository pattern, UseCase isolation, MethodChannels for native sensors, and CI/CD Fastlane deployment.",
                "order": 1,
                "lesson_ids": ["app-clean-architecture-repository-pattern", "app-methodchannels-native-bridges-fastlane"]
            }
        ]
    }
]

LESSONS_DATA = [
    {
        "id": "app-dart-null-safety-oop",
        "title": "Dart 3.0: Sound Null Safety, Records & Pattern Matching",
        "slug": "app-dart-null-safety-oop",
        "domain": "app-dev",
        "color": "#EC4899",
        "icon": "Smartphone",
        "is_published": True,
        "skills_taught": ['Dart 3', 'Flutter Layouts', 'BLoC Pattern', 'SQLite Drift', 'Clean Architecture'],
        "course_id": "course-app-lvl1",
        "order": 1,
        "xp_reward": 50,
        "visual_diagram_type": "two_pointers_array",
        "content": """# Dart 3.0 Sound Null Safety

Variables cannot contain `null` unless explicitly marked with `?`.
```dart
String? nullableName;
String nonNullableName = nullableName ?? 'Default User';

// Pattern matching and records
(int, int) swap((int, int) pair) {
  var (a, b) = pair;
  return (b, a);
}
```
"""
    },
    {
        "id": "app-dart-futures-streams-isolates",
        "title": "Dart Asynchronous Concurrency: Futures, Streams & Isolates",
        "slug": "app-dart-futures-streams-isolates",
        "domain": "app-dev",
        "color": "#EC4899",
        "icon": "Smartphone",
        "is_published": True,
        "skills_taught": ['Dart 3', 'Flutter Layouts', 'BLoC Pattern', 'SQLite Drift', 'Clean Architecture'],
        "course_id": "course-app-lvl1",
        "order": 2,
        "xp_reward": 55,
        "visual_diagram_type": "two_pointers_array",
        "content": """# Event Loop & Actor Model Isolates

Dart runs on a single thread event loop. CPU-intensive operations are offloaded to separate memory **Isolates** communicating via `SendPort` and `ReceivePort`.
"""
    },
    {
        "id": "app-flutter-three-trees-impeller",
        "title": "Flutter Architecture: Three Trees & The Impeller Engine",
        "slug": "app-flutter-three-trees-impeller",
        "domain": "app-dev",
        "color": "#EC4899",
        "icon": "Smartphone",
        "is_published": True,
        "skills_taught": ['Dart 3', 'Flutter Layouts', 'BLoC Pattern', 'SQLite Drift', 'Clean Architecture'],
        "course_id": "course-app-lvl2",
        "order": 1,
        "xp_reward": 60,
        "visual_diagram_type": "two_pointers_array",
        "content": """# Flutter Three Trees Architecture

1. **Widget Tree**: Immutable configuration objects.
2. **Element Tree**: Mutable bridge managing lifecycle and state.
3. **RenderObject Tree**: Responsible for geometry, layout constraints, and painting commands on the GPU via Impeller.
"""
    },
    {
        "id": "app-flutter-layouts-slivers-custompaint",
        "title": "Slivers, CustomPainter & 60/120 FPS Fluid Animations",
        "slug": "app-flutter-layouts-slivers-custompaint",
        "domain": "app-dev",
        "color": "#EC4899",
        "icon": "Smartphone",
        "is_published": True,
        "skills_taught": ['Dart 3', 'Flutter Layouts', 'BLoC Pattern', 'SQLite Drift', 'Clean Architecture'],
        "course_id": "course-app-lvl2",
        "order": 2,
        "xp_reward": 65,
        "visual_diagram_type": "two_pointers_array",
        "content": """# Advanced Flutter Layouts & Slivers

`CustomScrollView` and `SliverPersistentHeader` ensure viewport virtualization so only visible list items consume memory.
"""
    },
    {
        "id": "app-dio-networking-interceptors",
        "title": "Networking with Dio: Interceptors, Retries & Auth Tokens",
        "slug": "app-dio-networking-interceptors",
        "domain": "app-dev",
        "color": "#EC4899",
        "icon": "Smartphone",
        "is_published": True,
        "skills_taught": ['Dart 3', 'Flutter Layouts', 'BLoC Pattern', 'SQLite Drift', 'Clean Architecture'],
        "course_id": "course-app-lvl3",
        "order": 1,
        "xp_reward": 65,
        "visual_diagram_type": "two_pointers_array",
        "content": """# Dio Networking & Token Refresh Interceptors

Automatically captures 401 Unauthorized errors, pauses request queue, requests a refreshed JWT via refresh token, and re-executes queued requests transparently.
"""
    },
    {
        "id": "app-mobile-websockets-sync",
        "title": "Real-Time WebSocket Sync & Chat Architecture",
        "slug": "app-mobile-websockets-sync",
        "domain": "app-dev",
        "color": "#EC4899",
        "icon": "Smartphone",
        "is_published": True,
        "skills_taught": ['Dart 3', 'Flutter Layouts', 'BLoC Pattern', 'SQLite Drift', 'Clean Architecture'],
        "course_id": "course-app-lvl3",
        "order": 2,
        "xp_reward": 70,
        "visual_diagram_type": "two_pointers_array",
        "content": """# Mobile WebSockets & Connection Resilience

Managing socket reconnections, heartbeat pings, and optimistic UI rendering for real-time messaging applications.
"""
    },
    {
        "id": "app-bloc-event-driven-architecture",
        "title": "BLoC (Business Logic Component) Pattern & State Machines",
        "slug": "app-bloc-event-driven-architecture",
        "domain": "app-dev",
        "color": "#EC4899",
        "icon": "Smartphone",
        "is_published": True,
        "skills_taught": ['Dart 3', 'Flutter Layouts', 'BLoC Pattern', 'SQLite Drift', 'Clean Architecture'],
        "course_id": "course-app-lvl4",
        "order": 1,
        "xp_reward": 75,
        "visual_diagram_type": "two_pointers_array",
        "content": """# Unidirectional BLoC Pattern

`Event` $\\to$ `Bloc` $\\to$ `State`.
Ensures UI components are purely reactive and decoupled from business logic and network states.
"""
    },
    {
        "id": "app-riverpod-dependency-injection",
        "title": "Riverpod 2.0: Compile-Safe State & Dependency Injection",
        "slug": "app-riverpod-dependency-injection",
        "domain": "app-dev",
        "color": "#EC4899",
        "icon": "Smartphone",
        "is_published": True,
        "skills_taught": ['Dart 3', 'Flutter Layouts', 'BLoC Pattern', 'SQLite Drift', 'Clean Architecture'],
        "course_id": "course-app-lvl4",
        "order": 2,
        "xp_reward": 75,
        "visual_diagram_type": "two_pointers_array",
        "content": """# Riverpod Compile-Safe Providers

`NotifierProvider` and `AsyncNotifierProvider` handle asynchronous lifecycle states (Loading, Data, Error) with automatic disposal.
"""
    },
    {
        "id": "app-sqlite-drift-relational-storage",
        "title": "Embedded SQLite with Drift & Schema Migrations",
        "slug": "app-sqlite-drift-relational-storage",
        "domain": "app-dev",
        "color": "#EC4899",
        "icon": "Smartphone",
        "is_published": True,
        "skills_taught": ['Dart 3', 'Flutter Layouts', 'BLoC Pattern', 'SQLite Drift', 'Clean Architecture'],
        "course_id": "course-app-lvl5",
        "order": 1,
        "xp_reward": 80,
        "visual_diagram_type": "two_pointers_array",
        "content": """# Type-Safe SQLite Persistence

Writing relational SQLite schemas, indexes, and automated schema migration strategies on mobile devices.
"""
    },
    {
        "id": "app-hive-firebase-offline-sync",
        "title": "Hive Key-Value Box Storage & Firebase Cloud Sync",
        "slug": "app-hive-firebase-offline-sync",
        "domain": "app-dev",
        "color": "#EC4899",
        "icon": "Smartphone",
        "is_published": True,
        "skills_taught": ['Dart 3', 'Flutter Layouts', 'BLoC Pattern', 'SQLite Drift', 'Clean Architecture'],
        "course_id": "course-app-lvl5",
        "order": 2,
        "xp_reward": 80,
        "visual_diagram_type": "two_pointers_array",
        "content": """# Fast NoSQL Hive & Firebase Sync

Ultra-lightweight binary serialization storing documents locally and resolving sync conflicts with timestamps.
"""
    },
    {
        "id": "app-clean-architecture-repository-pattern",
        "title": "Clean Architecture: Presentation, Domain & Data Layers",
        "slug": "app-clean-architecture-repository-pattern",
        "domain": "app-dev",
        "color": "#EC4899",
        "icon": "Smartphone",
        "is_published": True,
        "skills_taught": ['Dart 3', 'Flutter Layouts', 'BLoC Pattern', 'SQLite Drift', 'Clean Architecture'],
        "course_id": "course-app-lvl6",
        "order": 1,
        "xp_reward": 85,
        "visual_diagram_type": "two_pointers_array",
        "content": """# Uncle Bob's Clean Architecture in Flutter

- **Presentation Layer**: Widgets, BLoC/Notifier
- **Domain Layer**: Entities, UseCases, Abstract Repository Interfaces
- **Data Layer**: DataSources (Remote/Local), Models, Repository Implementations
"""
    },
    {
        "id": "app-methodchannels-native-bridges-fastlane",
        "title": "MethodChannels, Native Bridges & Fastlane CI/CD",
        "slug": "app-methodchannels-native-bridges-fastlane",
        "domain": "app-dev",
        "color": "#EC4899",
        "icon": "Smartphone",
        "is_published": True,
        "skills_taught": ['Dart 3', 'Flutter Layouts', 'BLoC Pattern', 'SQLite Drift', 'Clean Architecture'],
        "course_id": "course-app-lvl6",
        "order": 2,
        "xp_reward": 90,
        "visual_diagram_type": "two_pointers_array",
        "content": """# MethodChannels (Kotlin / Swift) & Fastlane Deployments

Invoking native OS APIs (camera, Bluetooth, Secure Enclave) via asynchronous platform channels and automating Google Play / iOS App Store deployments with Fastlane.
"""
    }
]

QUIZZES_DATA = [
    {
        "id": "quiz-app-lvl1",
        "lesson_id": "app-dart-null-safety-oop",
        "title": "Dart & Flutter Mobile Foundations Diagnostic",
        "passing_score": 80,
        "questions": [
            {
                "id": "q-app-1-1",
                "question": "Which tree in Flutter is responsible for calculating geometric layout and issuing GPU paint commands?",
                "options": ["Widget Tree", "RenderObject Tree", "Element Tree", "State Tree"],
                "correct_option_index": 1,
                "explanation": "The RenderObject tree computes sizing constraints and issues drawing commands to the Impeller graphics engine."
            }
        ]
    }
]

SKILLS_DATA = [
    {
        "id": "skill-app-flutter",
        "name": "Flutter & Mobile Engineering",
        "category": "App Development",
        "level": 1,
        "unlocked": True,
        "progress": 0.0,
        "prerequisites": [],
        "description": "Master Dart 3, Flutter UI layouts, BLoC state management, and Clean Architecture."
    }
]
