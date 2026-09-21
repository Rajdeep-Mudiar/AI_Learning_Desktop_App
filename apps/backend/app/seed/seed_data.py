"""Comprehensive curriculum seed data for AI Learning Lab.
All 24 courses across AI & ML, Web Dev, App Dev, System Design, and Git & GitHub.
"""

COURSES_DATA = [   {   'slug': 'python-foundations',
        'title': 'Python & NumPy Foundations for AI',
        'domain': 'ai-ml',
        'description': 'Master essential Python programming, fast matrix math with NumPy, and structured data '
                       'manipulation with Pandas tailored for machine learning engineers.',
        'category': 'Programming Foundations',
        'level': 'Beginner',
        'estimated_hours': 8,
        'icon': 'Code2',
        'color': '#3B82F6',
        'order': 1,
        'is_published': True,
        'prerequisites': [],
        'skills_taught': [   'Python Syntax',
                             'Vectorization',
                             'NumPy Matrix Ops',
                             'Pandas DataFrames',
                             'Data Preprocessing'],
        'syllabus_overview': 'This course builds the foundational programming skills necessary for every modern AI '
                             'engineer. We move from core Python concepts to fast vectorized math in NumPy and '
                             'structured tabular data manipulation in Pandas.',
        'modules': [   {   'id': 'py-mod-1',
                           'title': 'Module 1: Everyday Python & Memory Basics',
                           'description': 'Variables, memory references, list comprehensions, and practical data '
                                          'structures.',
                           'order': 1,
                           'lesson_ids': ['py-intro-variables', 'py-data-structures-comprehensions']},
                       {   'id': 'py-mod-2',
                           'title': 'Module 2: NumPy & Fast Array Math',
                           'description': 'Arrays, broadcasting rules, matrix dot products, and speeding up code '
                                          'without loops.',
                           'order': 2,
                           'lesson_ids': ['py-numpy-arrays-broadcasting', 'py-numpy-matrix-operations']},
                       {   'id': 'py-mod-3',
                           'title': 'Module 3: Pandas for AI Data Cleaning',
                           'description': 'DataFrames, filtering, handling missing values, and preparing real '
                                          'datasets.',
                           'order': 3,
                           'lesson_ids': ['py-pandas-dataframes-cleaning']}]},
    {   'slug': 'math-for-ai',
        'title': 'Mathematics for Artificial Intelligence',
        'domain': 'ai-ml',
        'description': 'The foundational math pillars of AI explained simply: Vectors, matrices, slope derivatives, '
                       'gradients, and probability with real-world intuition.',
        'category': 'Mathematics',
        'level': 'Intermediate',
        'estimated_hours': 12,
        'icon': 'Binary',
        'color': '#8B5CF6',
        'order': 2,
        'is_published': True,
        'prerequisites': ['python-foundations'],
        'skills_taught': [   'Linear Algebra',
                             'Dot Products & Projections',
                             'Gradients & Partial Derivatives',
                             'Chain Rule',
                             'Bayes Theorem'],
        'syllabus_overview': 'AI models are mathematical transformations. This course teaches you to visualize vectors '
                             'as arrows in space, understand matrix multiplication as geometric transformations, and '
                             'intuitively grasp gradients.',
        'modules': [   {   'id': 'math-mod-1',
                           'title': 'Module 1: Vectors & Geometric Similarity',
                           'description': 'Vectors, dot products, projections, and measuring similarity between data '
                                          'points.',
                           'order': 1,
                           'lesson_ids': ['math-vectors-dot-products', 'math-matrix-multiplication']},
                       {   'id': 'math-mod-2',
                           'title': 'Module 2: Derivatives & Finding the Best Path',
                           'description': 'Slopes, partial derivatives, and understanding the gradient vector as a '
                                          'compass.',
                           'order': 2,
                           'lesson_ids': ['math-derivatives-gradients', 'math-chain-rule-backprop-math']},
                       {   'id': 'math-mod-3',
                           'title': 'Module 3: Probability & Smart Guessing',
                           'description': 'Probabilities, odds, and using Bayes Theorem to update predictions with new '
                                          'evidence.',
                           'order': 3,
                           'lesson_ids': ['math-probability-bayes-theorem']}]},
    {   'slug': 'ml-fundamentals',
        'title': 'Machine Learning Fundamentals',
        'domain': 'ai-ml',
        'description': 'Learn how computers learn from data: Linear regression, classification, decision trees, '
                       'evaluating models, and clustering.',
        'category': 'Machine Learning',
        'level': 'Beginner',
        'estimated_hours': 14,
        'icon': 'Cpu',
        'color': '#10B981',
        'order': 3,
        'is_published': True,
        'prerequisites': ['python-foundations', 'math-for-ai'],
        'skills_taught': [   'Linear Regression',
                             'Gradient Descent',
                             'Logistic Regression',
                             'Decision Trees',
                             'K-Means Clustering',
                             'Cross Validation'],
        'syllabus_overview': 'From linear models to decision trees, understand classical machine learning algorithms '
                             'from both an intuitive and hands-on coding standpoint.',
        'modules': [   {   'id': 'ml-mod-1',
                           'title': 'Module 1: Predicting Numbers with Lines',
                           'description': 'Fitting lines to data, calculating errors, and walking down the loss slope.',
                           'order': 1,
                           'lesson_ids': ['ml-linear-regression-ols', 'ml-gradient-descent-intuition']},
                       {   'id': 'ml-mod-2',
                           'title': 'Module 2: Classifying Yes / No & Trees',
                           'description': 'Logistic regression, S-curves, asking 20 questions with decision trees.',
                           'order': 2,
                           'lesson_ids': ['ml-logistic-regression-classification', 'ml-decision-trees-entropy']},
                       {   'id': 'ml-mod-3',
                           'title': 'Module 3: Finding Natural Groups (Clustering)',
                           'description': 'K-Means clustering, grouping unlabeled data, and finding patterns.',
                           'order': 3,
                           'lesson_ids': ['ml-kmeans-clustering-algorithm']}]},
    {   'slug': 'deep-learning-fundamentals',
        'title': 'Deep Learning & Neural Networks',
        'domain': 'ai-ml',
        'description': 'How neural networks think: Artificial neurons, forward thinking, learning backwards with '
                       'backpropagation, and image recognition with CNNs.',
        'category': 'Deep Learning',
        'level': 'Intermediate',
        'estimated_hours': 16,
        'icon': 'Network',
        'color': '#0EA5E9',
        'order': 4,
        'is_published': True,
        'prerequisites': ['ml-fundamentals'],
        'skills_taught': [   'Multi-Layer Perceptrons',
                             'Activation Functions',
                             'Backpropagation',
                             'Convolutional Neural Nets',
                             'PyTorch Basics'],
        'syllabus_overview': 'Deep learning allows computers to recognize images, translate languages, and beat '
                             'grandmasters. Learn how networks build representations layer by layer.',
        'modules': [   {   'id': 'dl-mod-1',
                           'title': 'Module 1: Artificial Neurons & Layers',
                           'description': 'How a neuron fires, combining inputs with weights, and activation '
                                          'functions.',
                           'order': 1,
                           'lesson_ids': ['dl-perceptron-forward-prop', 'dl-activation-functions']},
                       {   'id': 'dl-mod-2',
                           'title': 'Module 2: Backpropagation (How Networks Learn)',
                           'description': 'Sending error feedback backwards through the network to tweak weights.',
                           'order': 2,
                           'lesson_ids': ['dl-backpropagation-calculus']},
                       {   'id': 'dl-mod-3',
                           'title': 'Module 3: Computer Vision with CNNs',
                           'description': 'Sliding filters over images to detect edges, curves, eyes, and complex '
                                          'objects.',
                           'order': 3,
                           'lesson_ids': ['dl-cnn-convolution-pooling']}]},
    {   'slug': 'generative-ai-fundamentals',
        'title': 'Generative AI, Transformers & LLMs',
        'domain': 'ai-ml',
        'description': 'How modern AI like ChatGPT works: Word tokens, embeddings, the Transformer self-attention '
                       'spotlight, and building RAG applications.',
        'category': 'Generative AI',
        'level': 'Advanced',
        'estimated_hours': 18,
        'icon': 'Sparkles',
        'color': '#EC4899',
        'order': 5,
        'is_published': True,
        'prerequisites': ['deep-learning-fundamentals'],
        'skills_taught': [   'Tokenization & Embeddings',
                             'Scaled Dot-Product Attention',
                             'Transformer Encoders & Decoders',
                             'Prompt Engineering',
                             'RAG Systems'],
        'syllabus_overview': 'Understand the architecture powering ChatGPT, Claude, and modern generative AI. Explore '
                             'how attention mechanisms operate and how to construct Retrieval-Augmented Generation '
                             'workflows.',
        'modules': [   {   'id': 'genai-mod-1',
                           'title': 'Module 1: Words as Numbers (Tokens & Embeddings)',
                           'description': 'How AI reads text, turning words into coordinate maps where similar words '
                                          'sit together.',
                           'order': 1,
                           'lesson_ids': ['genai-tokenization-embeddings']},
                       {   'id': 'genai-mod-2',
                           'title': 'Module 2: The Attention Mechanism',
                           'description': 'Queries, Keys, Values, and connecting related words across long sentences.',
                           'order': 2,
                           'lesson_ids': ['genai-self-attention-transformers']},
                       {   'id': 'genai-mod-3',
                           'title': 'Module 3: Retrieval-Augmented Generation (RAG)',
                           'description': 'Connecting your AI to custom documents and databases to answer questions '
                                          'accurately.',
                           'order': 3,
                           'lesson_ids': ['genai-rag-architecture-pipeline']}]},
    {   'slug': 'prompt-engineering-agents',
        'title': 'Prompt Engineering & AI Autonomous Agents',
        'description': 'Crafting high-precision prompts, multi-step chain of thought reasoning, and building AI agents '
                       'that use external APIs and tools.',
        'domain': 'ai-ml',
        'category': 'Practical AI',
        'level': 'Beginner',
        'estimated_hours': 10,
        'icon': 'Bot',
        'color': '#F59E0B',
        'order': 6,
        'is_published': True,
        'prerequisites': ['python-foundations'],
        'skills_taught': [   'System Prompts',
                             'Few-Shot Prompting',
                             'Chain of Thought',
                             'Tool Calling & ReAct',
                             'Autonomous Agents'],
        'syllabus_overview': 'Learn how to steer foundation models with precision. From structured output schemas and '
                             'reasoning frameworks to building interactive ReAct agents that browse databases and '
                             'execute code.',
        'modules': [   {   'id': 'agent-mod-1',
                           'title': 'Module 1: Prompt Engineering Foundations',
                           'description': 'System instructions, structured output formatting, delimiters, and few-shot '
                                          'examples.',
                           'order': 1,
                           'lesson_ids': ['prompt-foundations-few-shot']},
                       {   'id': 'agent-mod-2',
                           'title': 'Module 2: Advanced Reasoning & Chain of Thought',
                           'description': 'Unlocking complex logical deductions with Chain-of-Thought and '
                                          'self-consistency.',
                           'order': 2,
                           'lesson_ids': ['prompt-chain-of-thought-reasoning']},
                       {   'id': 'agent-mod-3',
                           'title': 'Module 3: Building Autonomous AI Agents',
                           'description': 'Function calling, external tool usage, and the ReAct (Reason + Act) loop.',
                           'order': 3,
                           'lesson_ids': ['prompt-ai-agents-tool-use']}]},
    {   'slug': 'html5-web-architecture',
        'title': 'HTML5 & Web Architecture Foundations',
        'domain': 'web-dev',
        'description': 'Start from absolute zero: How browsers communicate with servers via DNS and HTTP/HTTPS, '
                       'semantic HTML5 document structures, SEO meta tags, and accessible forms with ARIA.',
        'category': 'Web Development',
        'level': 'Beginner',
        'estimated_hours': 8,
        'icon': 'Globe',
        'color': '#06B6D4',
        'order': 7,
        'is_published': True,
        'prerequisites': [],
        'skills_taught': [   'HTTP Protocols',
                             'DNS Resolution',
                             'Semantic HTML5',
                             'Form Validations',
                             'ARIA Accessibility',
                             'SEO Metadata'],
        'syllabus_overview': 'Understand the fundamental building blocks of the web. Learn how browser engines parse '
                             'HTML documents into the DOM tree, structure content semantically for search crawlers, '
                             'and create accessible interactive forms.',
        'modules': [   {   'id': 'html-mod-1',
                           'title': 'Module 1: How the Web Works & HTTP/HTTPS',
                           'description': 'DNS lookup, TCP/IP handshakes, client-server models, and request/response '
                                          'headers.',
                           'order': 1,
                           'lesson_ids': ['web-how-the-web-works']},
                       {   'id': 'html-mod-2',
                           'title': 'Module 2: Semantic HTML5 Architecture',
                           'description': 'Structuring clean accessible web pages with header, main, section, article, '
                                          'and nav tags.',
                           'order': 2,
                           'lesson_ids': ['web-semantic-html5-tags']},
                       {   'id': 'html-mod-3',
                           'title': 'Module 3: Interactive Forms, Validation & ARIA',
                           'description': 'Inputs, form validation rules, accessibility attributes, and WCAG screen '
                                          'reader standards.',
                           'order': 3,
                           'lesson_ids': ['web-forms-validation-accessibility']}]},
    {   'slug': 'css3-mastery-responsive-grid',
        'title': 'CSS3 Mastery, Responsive Layouts & Modern Grid',
        'domain': 'web-dev',
        'description': 'Master visual styling: The CSS Cascade and Box Model, fluid 1D Flexbox, 2D CSS Grid templates, '
                       'mobile-first media queries, custom properties, and keyframe animations.',
        'category': 'Web Development',
        'level': 'Beginner',
        'estimated_hours': 12,
        'icon': 'Layers',
        'color': '#3B82F6',
        'order': 8,
        'is_published': True,
        'prerequisites': ['html5-web-architecture'],
        'skills_taught': [   'CSS Box Model',
                             'Specificity & Cascade',
                             'Flexbox',
                             '2D CSS Grid',
                             'Responsive Breakpoints',
                             'Keyframe Animations'],
        'syllabus_overview': 'Turn basic HTML markup into stunning, pixel-perfect user interfaces. Learn how layout '
                             'engines calculate geometry, master responsive alignment with Flexbox and CSS Grid, and '
                             'design smooth micro-interactions.',
        'modules': [   {   'id': 'css-mod-1',
                           'title': 'Module 1: The Box Model & The CSS Cascade',
                           'description': 'Content, padding, border, margin, box-sizing, and specificity calculation.',
                           'order': 1,
                           'lesson_ids': ['web-css-box-model-cascade']},
                       {   'id': 'css-mod-2',
                           'title': 'Module 2: Flexbox & 2D CSS Grid Layout Engineering',
                           'description': 'One-dimensional flex alignment and multi-column CSS grid templates with '
                                          'minmax and auto-fit.',
                           'order': 2,
                           'lesson_ids': ['web-css-flexbox-grid-mastery']},
                       {   'id': 'css-mod-3',
                           'title': 'Module 3: Responsive Units, Variables & Animations',
                           'description': 'Fluid typography with clamp(), custom CSS variables, and GPU-accelerated '
                                          'transitions.',
                           'order': 3,
                           'lesson_ids': ['web-css-responsive-animations']}]},
    {   'slug': 'javascript-core-async',
        'title': 'Modern JavaScript: Core Engine & Async Mastery',
        'domain': 'web-dev',
        'description': 'Demystify JavaScript under the hood: The V8 engine, call stack, execution contexts, lexical '
                       'closures, the event loop, microtask queue, promises, and async/await.',
        'category': 'Web Development',
        'level': 'Intermediate',
        'estimated_hours': 14,
        'icon': 'Code2',
        'color': '#F59E0B',
        'order': 9,
        'is_published': True,
        'prerequisites': ['css3-mastery-responsive-grid'],
        'skills_taught': [   'Execution Contexts',
                             'Lexical Closures',
                             'Event Loop',
                             'Promises & Async/Await',
                             'DOM Event Delegation',
                             'Fetch API'],
        'syllabus_overview': 'Deeply understand the language of the web. Learn how JavaScript executes single-threaded '
                             'code, manages heap memory, schedules microtasks, and coordinates high-performance DOM '
                             'manipulation.',
        'modules': [   {   'id': 'js-mod-1',
                           'title': 'Module 1: Execution Contexts, Scopes & Closures',
                           'description': 'Call stack, variable hoisting, lexical environments, and closure memory '
                                          'retention.',
                           'order': 1,
                           'lesson_ids': ['web-js-execution-scope-closures']},
                       {   'id': 'js-mod-2',
                           'title': 'Module 2: The Event Loop, Promises & Async/Await',
                           'description': 'Macrotasks, microtasks, Promise chaining, and async/await error boundaries.',
                           'order': 2,
                           'lesson_ids': ['web-js-event-loop-promises-async']},
                       {   'id': 'js-mod-3',
                           'title': 'Module 3: DOM Traversal, Event Bubbling & APIs',
                           'description': 'DOM querying, event bubbling vs capturing, event delegation, and the Fetch '
                                          'API.',
                           'order': 3,
                           'lesson_ids': ['web-js-dom-events-delegation']}]},
    {   'slug': 'react18-frontend-architecture',
        'title': 'React 18: Components, Hooks & State Architecture',
        'domain': 'web-dev',
        'description': 'Build modern scalable single-page applications: Declarative JSX, Virtual DOM reconciliation, '
                       'Custom Hooks, useMemo/useCallback performance, and global state with Context & Zustand.',
        'category': 'Web Development',
        'level': 'Intermediate',
        'estimated_hours': 16,
        'icon': 'Cpu',
        'color': '#6366F1',
        'order': 10,
        'is_published': True,
        'prerequisites': ['javascript-core-async'],
        'skills_taught': [   'Declarative JSX',
                             'Virtual DOM Diffing',
                             'React 18 Hooks',
                             'Custom Hooks',
                             'Zustand & Context API',
                             'React Router 6'],
        'syllabus_overview': 'Master enterprise React development. Learn how React 18 manages concurrent rendering, '
                             'organizes component hierarchies with one-way data flow, and avoids unnecessary '
                             're-renders using memoization.',
        'modules': [   {   'id': 'react-mod-1',
                           'title': 'Module 1: Declarative JSX & Virtual DOM Diffing',
                           'description': 'Component trees, JSX compilation, props, and how the reconciliation engine '
                                          'updates the browser DOM.',
                           'order': 1,
                           'lesson_ids': ['web-react-jsx-vdom-components']},
                       {   'id': 'react-mod-2',
                           'title': 'Module 2: React 18 Hooks & Custom Hook Architecture',
                           'description': 'useState, useEffect dependency arrays, useMemo, useCallback, and reusable '
                                          'custom hooks.',
                           'order': 2,
                           'lesson_ids': ['web-react-hooks-deep-dive']},
                       {   'id': 'react-mod-3',
                           'title': 'Module 3: State Management & Client-Side Routing',
                           'description': 'Context API, lightweight Zustand stores, and dynamic client routing with '
                                          'React Router 6.',
                           'order': 3,
                           'lesson_ids': ['web-react-state-routing-zustand']}]},
    {   'slug': 'nodejs-backend-apis',
        'title': 'Backend Engineering: Node.js, Express & REST APIs',
        'domain': 'web-dev',
        'description': 'Architect high-performance web backends: Node.js runtime, Express middleware pipelines, JWT '
                       'token authentication, MongoDB & PostgreSQL database modeling, and RESTful API standards.',
        'category': 'Web Development',
        'level': 'Intermediate',
        'estimated_hours': 16,
        'icon': 'Server',
        'color': '#10B981',
        'order': 11,
        'is_published': True,
        'prerequisites': ['javascript-core-async'],
        'skills_taught': [   'Node.js Runtime',
                             'Express Middleware',
                             'JWT Authentication',
                             'Bcrypt Hashing',
                             'MongoDB & Mongoose',
                             'PostgreSQL Queries'],
        'syllabus_overview': 'Transition from frontend to full-stack engineering. Learn how to write secure, scalable '
                             'backend services with authentication guards, relational and document database drivers, '
                             'and CORS protections.',
        'modules': [   {   'id': 'node-mod-1',
                           'title': 'Module 1: Node.js Runtime & Express Middleware',
                           'description': 'V8 engine on the server, request-response pipelines, routing, and '
                                          'centralized error handling.',
                           'order': 1,
                           'lesson_ids': ['web-nodejs-express-middleware']},
                       {   'id': 'node-mod-2',
                           'title': 'Module 2: Authentication, JWT & Security Guards',
                           'description': 'Bcrypt password hashing, JSON Web Tokens (JWT), HTTP-only cookies, and rate '
                                          'limiting.',
                           'order': 2,
                           'lesson_ids': ['web-jwt-auth-security-bcrypt']},
                       {   'id': 'node-mod-3',
                           'title': 'Module 3: Database Modeling with MongoDB & SQL',
                           'description': 'Schema modeling, indexes, foreign keys, and performant CRUD queries with '
                                          'MongoDB and PostgreSQL.',
                           'order': 3,
                           'lesson_ids': ['web-db-mongodb-postgresql-crud']}]},
    {   'slug': 'advanced-fullstack-performance',
        'title': 'Advanced Full-Stack Engineering & Web Performance',
        'domain': 'web-dev',
        'description': 'Scale enterprise web applications: Server-Side Rendering (SSR) with Next.js, Core Web Vitals '
                       'optimization, real-time bidirectional WebSockets, and distributed Redis caching.',
        'category': 'Web Development',
        'level': 'Advanced',
        'estimated_hours': 18,
        'icon': 'Zap',
        'color': '#8B5CF6',
        'order': 12,
        'is_published': True,
        'prerequisites': ['react18-frontend-architecture', 'nodejs-backend-apis'],
        'skills_taught': [   'Server-Side Rendering (SSR)',
                             'Next.js App Router',
                             'Core Web Vitals (LCP/FID/CLS)',
                             'WebSockets',
                             'Redis Caching',
                             'Code Splitting'],
        'syllabus_overview': 'Master high-performance web engineering. Learn how top tech companies optimize render '
                             'speeds with SSR and hydration, maintain real-time socket connections for millions of '
                             'users, and eliminate database bottlenecks using Redis.',
        'modules': [   {   'id': 'adv-web-mod-1',
                           'title': 'Module 1: Next.js SSR, SSG & Server Components',
                           'description': 'Static site generation, dynamic server-side rendering, client hydration, '
                                          'and React Server Components.',
                           'order': 1,
                           'lesson_ids': ['web-nextjs-ssr-ssg-hydration']},
                       {   'id': 'adv-web-mod-2',
                           'title': 'Module 2: Web Performance & Core Web Vitals',
                           'description': 'Optimizing Largest Contentful Paint (LCP), Cumulative Layout Shift (CLS), '
                                          'code splitting, and lazy loading.',
                           'order': 2,
                           'lesson_ids': ['web-performance-core-web-vitals']},
                       {   'id': 'adv-web-mod-3',
                           'title': 'Module 3: Real-Time WebSockets & In-Memory Redis Caching',
                           'description': 'Bi-directional WebSocket streaming, socket rooms, Cache-Aside Redis '
                                          'patterns, and invalidation.',
                           'order': 3,
                           'lesson_ids': ['web-websockets-realtime-redis-caching']}]},
    {   'slug': 'mobile-react-native-foundations',
        'title': 'React Native & Mobile UI Foundations',
        'domain': 'app-dev',
        'description': 'Start mobile engineering: How React Native bridges JavaScript to native iOS UIKit and Android '
                       'views, core mobile primitives (View, Text, Image), Safe Areas, and density-independent pixels '
                       '(dp).',
        'category': 'App Development',
        'level': 'Beginner',
        'estimated_hours': 10,
        'icon': 'Smartphone',
        'color': '#EC4899',
        'order': 13,
        'is_published': True,
        'prerequisites': [],
        'skills_taught': [   'Native Bridge',
                             'Mobile Viewports',
                             'SafeAreaView',
                             'Touch Targets',
                             'Mobile Flexbox',
                             'Density Pixels (dp)'],
        'syllabus_overview': 'Understand how mobile operating systems render UI. Learn how React Native translates JSX '
                             'into genuine native views, manages screen notches with SafeAreaView, and styles '
                             'touchable controls for human thumbs.',
        'modules': [   {   'id': 'app-mod-1',
                           'title': 'Module 1: Native Bridges & Mobile Primitives',
                           'description': 'The JavaScript-to-Native bridge, View vs <div>, Text vs <p>, and mobile '
                                          'rendering architecture.',
                           'order': 1,
                           'lesson_ids': ['app-foundations-native-bridge']},
                       {   'id': 'app-mod-2',
                           'title': 'Module 2: Screen Densities, Safe Areas & Notches',
                           'description': '1x/2x/3x pixel densities, Dynamic Island insets, and safe-area layout '
                                          'boundaries.',
                           'order': 2,
                           'lesson_ids': ['app-viewport-density-safe-area']},
                       {   'id': 'app-mod-3',
                           'title': 'Module 3: Mobile Flexbox & Touch Targets',
                           'description': 'Column-first flex direction, TouchableOpacity, and minimum 44x44 pt thumb '
                                          'targets.',
                           'order': 3,
                           'lesson_ids': ['app-mobile-flexbox-touch-targets']}]},
    {   'slug': 'mobile-navigation-gestures',
        'title': 'Mobile Navigation, Gestures & Reanimated 3',
        'domain': 'app-dev',
        'description': 'Master native mobile interactions: React Navigation Stack, Bottom Tab Bars, Drawer Navigators, '
                       'Gesture Handler (pan, pinch, swipe), and 60fps spring animations with Reanimated 3.',
        'category': 'App Development',
        'level': 'Intermediate',
        'estimated_hours': 12,
        'icon': 'Layers',
        'color': '#F43F5E',
        'order': 14,
        'is_published': True,
        'prerequisites': ['mobile-react-native-foundations'],
        'skills_taught': [   'Stack Navigation',
                             'Bottom Tabs',
                             'Deep Linking',
                             'Pan & Swipe Gestures',
                             'Reanimated 3',
                             'Spring Physics'],
        'syllabus_overview': 'Create fluid native app transitions. Learn how native navigation stacks maintain scroll '
                             'positions, handle fluid swipe-to-dismiss gestures, and run smooth physics animations on '
                             'the UI thread.',
        'modules': [   {   'id': 'app-nav-mod-1',
                           'title': 'Module 1: Stack & Tab Navigation Stacks',
                           'description': 'LIFO screen stacks, bottom tab bars, screen header customization, and deep '
                                          'link routing.',
                           'order': 1,
                           'lesson_ids': ['app-navigation-stacks-tabs']},
                       {   'id': 'app-nav-mod-2',
                           'title': 'Module 2: Touch Gestures & Pan Handling',
                           'description': 'Continuous pan gestures, drag boundaries, swipe actions, and multi-touch '
                                          'pinch to zoom.',
                           'order': 2,
                           'lesson_ids': ['app-gestures-pan-swipe-pinch']},
                       {   'id': 'app-nav-mod-3',
                           'title': 'Module 3: Reanimated 3 & UI Thread Physics',
                           'description': 'Shared values, useAnimatedStyle, worklets running directly on the UI '
                                          'thread, and spring physics.',
                           'order': 3,
                           'lesson_ids': ['app-reanimated-60fps-physics']}]},
    {   'slug': 'mobile-storage-device-apis',
        'title': 'Offline-First Storage, SQLite & Native APIs',
        'domain': 'app-dev',
        'description': 'Build resilient mobile apps that work seamlessly without internet: High-speed MMKV key-value '
                       'storage, embedded SQLite databases, camera/gallery permissions, and GPS geolocation.',
        'category': 'App Development',
        'level': 'Intermediate',
        'estimated_hours': 14,
        'icon': 'HardDrive',
        'color': '#A855F7',
        'order': 15,
        'is_published': True,
        'prerequisites': ['mobile-react-native-foundations'],
        'skills_taught': [   'MMKV Storage',
                             'Embedded SQLite',
                             'Offline-First Architecture',
                             'Camera Permissions',
                             'Biometrics (FaceID)',
                             'Geolocation'],
        'syllabus_overview': 'Master native device capabilities. Learn how to store gigabytes of local structured data '
                             'with SQLite, securely authenticate users with FaceID / TouchID, and cache state for '
                             'offline subway commutes.',
        'modules': [   {   'id': 'app-api-mod-1',
                           'title': 'Module 1: Offline-First & High-Speed MMKV Caching',
                           'description': 'Instant startup render, MMKV C++ memory mapping, and optimistic UI '
                                          'mutations.',
                           'order': 1,
                           'lesson_ids': ['app-offline-first-mmkv-storage']},
                       {   'id': 'app-api-mod-2',
                           'title': 'Module 2: Embedded Relational SQLite on Mobile',
                           'description': 'SQLite schemas, relational joins, table migrations, and high-volume local '
                                          'indexing.',
                           'order': 2,
                           'lesson_ids': ['app-sqlite-local-relational-db']},
                       {   'id': 'app-api-mod-3',
                           'title': 'Module 3: Camera, Biometrics & Hardware Permissions',
                           'description': 'Requesting OS runtime permissions, capturing photos, FaceID authentication, '
                                          'and GPS tracking.',
                           'order': 3,
                           'lesson_ids': ['app-device-hardware-camera-location']}]},
    {   'slug': 'flutter-dart-engineering',
        'title': 'Flutter & Dart Cross-Platform Engineering',
        'domain': 'app-dev',
        'description': 'Build high-performance 120fps compiled mobile apps with Google Flutter: The Dart language, '
                       'Widget trees (Stateless vs Stateful), Impeller rendering engine, and BLoC state architecture.',
        'category': 'App Development',
        'level': 'Intermediate',
        'estimated_hours': 14,
        'icon': 'Smartphone',
        'color': '#0284C7',
        'order': 16,
        'is_published': True,
        'prerequisites': [],
        'skills_taught': [   'Dart Language',
                             'Flutter Widget Tree',
                             'Impeller Rendering',
                             'StatefulWidget Lifecycle',
                             'BLoC Pattern',
                             'Reactive Streams'],
        'syllabus_overview': "Learn Flutter's compile-to-native architecture. Understand how the Impeller rendering "
                             'engine paints directly to Skia/Vulkan canvases and manage complex state using BLoC and '
                             'Dart Streams.',
        'modules': [   {   'id': 'flutter-mod-1',
                           'title': 'Module 1: Flutter Architecture & The Widget Tree',
                           'description': 'Ahead-Of-Time (AOT) compilation, Impeller engine, and the '
                                          'everything-is-a-widget paradigm.',
                           'order': 1,
                           'lesson_ids': ['app-flutter-widget-tree-rendering']},
                       {   'id': 'flutter-mod-2',
                           'title': 'Module 2: StatefulWidget Lifecycles & State Management',
                           'description': 'initState, build, dispose lifecycles, and reactive setState state updates.',
                           'order': 2,
                           'lesson_ids': ['app-flutter-stateful-lifecycle']},
                       {   'id': 'flutter-mod-3',
                           'title': 'Module 3: BLoC Architecture & Reactive Streams',
                           'description': 'Business Logic Components (BLoC), Event-to-State transformations, and Dart '
                                          'async streams.',
                           'order': 3,
                           'lesson_ids': ['app-flutter-bloc-state-streams']}]},
    {   'slug': 'mobile-production-app-stores',
        'title': 'Push Notifications, Background Sync & App Store Release',
        'domain': 'app-dev',
        'description': 'Production mobile engineering: Firebase Cloud Messaging (FCM) & Apple APNs push notifications, '
                       'background workers, code-signing certificates, and automated App Store / Play Store release '
                       'pipelines.',
        'category': 'App Development',
        'level': 'Advanced',
        'estimated_hours': 16,
        'icon': 'Zap',
        'color': '#E11D48',
        'order': 17,
        'is_published': True,
        'prerequisites': ['mobile-navigation-gestures', 'mobile-storage-device-apis'],
        'skills_taught': [   'FCM & APNs Push',
                             'Background Tasks',
                             'WorkManager',
                             'Code Signing Certificates',
                             'Fastlane & EAS',
                             'App Store Publishing'],
        'syllabus_overview': 'Ship mobile apps to millions of devices. Learn how to handle background push payloads, '
                             'execute periodic background sync without draining battery, and automate iOS and Android '
                             'build distribution.',
        'modules': [   {   'id': 'app-prod-mod-1',
                           'title': 'Module 1: Push Notifications with FCM & APNs',
                           'description': 'Device push tokens, silent data payloads, and rich interactive notification '
                                          'handlers.',
                           'order': 1,
                           'lesson_ids': ['app-push-notifications-fcm-apns']},
                       {   'id': 'app-prod-mod-2',
                           'title': 'Module 2: Background Fetch & Periodic Sync Workers',
                           'description': 'iOS Background Tasks, Android WorkManager, and battery-efficient network '
                                          'synchronization.',
                           'order': 2,
                           'lesson_ids': ['app-background-tasks-worker-sync']},
                       {   'id': 'app-prod-mod-3',
                           'title': 'Module 3: Code Signing, Fastlane & App Store Publishing',
                           'description': 'Apple Provisioning Profiles, Android Keystores, EAS builds, and automated '
                                          'TestFlight / Google Play deployment.',
                           'order': 3,
                           'lesson_ids': ['app-appstore-playstore-deployment']}]},
    {   'slug': 'system-design-foundations',
        'title': 'Distributed Systems Foundations & Architecture',
        'domain': 'system-design',
        'description': 'Start system design: Vertical vs Horizontal scaling, DNS round-robin, CDN edge caching, '
                       'monolith vs microservices trade-offs, and the CAP & PACELC theorems.',
        'category': 'System Design',
        'level': 'Beginner',
        'estimated_hours': 12,
        'icon': 'Layers',
        'color': '#10B981',
        'order': 18,
        'is_published': True,
        'prerequisites': [],
        'skills_taught': [   'Horizontal Scaling',
                             'DNS & CDNs',
                             'Microservices Architecture',
                             'CAP Theorem',
                             'PACELC Trade-offs',
                             'SLA & High Availability'],
        'syllabus_overview': 'Understand how web applications scale from a single server to global multi-region '
                             'deployments. Master the fundamental laws of distributed computing, latency budgets, and '
                             'availability SLAs.',
        'modules': [   {   'id': 'sys-found-mod-1',
                           'title': 'Module 1: Scaling Up vs Scaling Out & Edge CDNs',
                           'description': 'Vertical vs horizontal scaling, reverse proxies, DNS routing, and static '
                                          'asset CDN caching.',
                           'order': 1,
                           'lesson_ids': ['sys-client-server-scaling']},
                       {   'id': 'sys-found-mod-2',
                           'title': 'Module 2: Monoliths to Microservices Architecture',
                           'description': 'Single codebase trade-offs, Domain-Driven Design (DDD), bounded contexts, '
                                          'and service boundaries.',
                           'order': 2,
                           'lesson_ids': ['sys-monolith-to-microservices']},
                       {   'id': 'sys-found-mod-3',
                           'title': 'Module 3: The CAP Theorem & Distributed Trade-offs',
                           'description': 'Consistency, Availability, Partition Tolerance, and latency vs consistency '
                                          'under PACELC.',
                           'order': 3,
                           'lesson_ids': ['sys-cap-theorem-pacelc']}]},
    {   'slug': 'system-design-loadbalancing-gateways',
        'title': 'API Gateways, Load Balancers & High Availability',
        'domain': 'system-design',
        'description': 'Architect rock-solid network perimeters: Layer 4 vs Layer 7 Load Balancing, Token Bucket rate '
                       'limiting, API Gateway authentication routing, and Circuit Breaker fault isolation.',
        'category': 'System Design',
        'level': 'Intermediate',
        'estimated_hours': 14,
        'icon': 'Server',
        'color': '#059669',
        'order': 19,
        'is_published': True,
        'prerequisites': ['system-design-foundations'],
        'skills_taught': [   'L4/L7 Load Balancing',
                             'Round-Robin & Least Conn',
                             'API Gateways',
                             'Token Bucket Rate Limiting',
                             'Circuit Breakers',
                             'Chaos Engineering'],
        'syllabus_overview': 'Distribute incoming client traffic reliably across thousands of worker nodes. Prevent '
                             'cascading microservice failures using circuit breakers and defend APIs against DDoS '
                             'attacks with distributed rate limiting.',
        'modules': [   {   'id': 'sys-lb-mod-1',
                           'title': 'Module 1: Layer 4 vs Layer 7 Load Balancing',
                           'description': 'TCP stream forwarding vs HTTP header inspection, weighted round-robin, and '
                                          'health check probes.',
                           'order': 1,
                           'lesson_ids': ['sys-l4-l7-load-balancing']},
                       {   'id': 'sys-lb-mod-2',
                           'title': 'Module 2: API Gateways & Distributed Rate Limiting',
                           'description': 'Centralized auth routing, response transformations, Token Bucket, and Leaky '
                                          'Bucket algorithms.',
                           'order': 2,
                           'lesson_ids': ['sys-api-gateways-rate-limiting']},
                       {   'id': 'sys-lb-mod-3',
                           'title': 'Module 3: Circuit Breakers & Graceful Degradation',
                           'description': 'Closed, Open, and Half-Open states, bulkheading, fallback fallbacks, and '
                                          'preventing cascading crashes.',
                           'order': 3,
                           'lesson_ids': ['sys-circuit-breaker-fault-tolerance']}]},
    {   'slug': 'system-design-caching-queues',
        'title': 'Distributed Caching & Asynchronous Event Queues',
        'domain': 'system-design',
        'description': 'Eliminate database bottlenecks and decouple services: In-memory Redis caching strategies, '
                       'Cache-Aside vs Write-Through, RabbitMQ message queues, and Apache Kafka event streams.',
        'category': 'System Design',
        'level': 'Intermediate',
        'estimated_hours': 16,
        'icon': 'Cpu',
        'color': '#34D399',
        'order': 20,
        'is_published': True,
        'prerequisites': ['system-design-foundations'],
        'skills_taught': [   'Redis Caching',
                             'Cache Invalidation',
                             'Thundering Herd Mitigation',
                             'RabbitMQ Message Queues',
                             'Apache Kafka Log Streaming',
                             'Distributed Sagas'],
        'syllabus_overview': 'Process millions of events per second asynchronously. Learn how to design '
                             'sub-millisecond in-memory cache architectures, handle high-throughput log streams with '
                             'Kafka partitions, and orchestrate distributed transactions.',
        'modules': [   {   'id': 'sys-cache-mod-1',
                           'title': 'Module 1: Redis Caching Patterns & Invalidation',
                           'description': 'Cache-Aside, Write-Through, Write-Behind, TTL policies, and avoiding '
                                          'thundering herd stamps.',
                           'order': 1,
                           'lesson_ids': ['sys-redis-caching-patterns']},
                       {   'id': 'sys-cache-mod-2',
                           'title': 'Module 2: Message Brokers: RabbitMQ vs Apache Kafka',
                           'description': 'AMQP push queues vs partitioned immutable append-only commit logs, consumer '
                                          'groups, and offset tracking.',
                           'order': 2,
                           'lesson_ids': ['sys-message-queues-rabbitmq-kafka']},
                       {   'id': 'sys-cache-mod-3',
                           'title': 'Module 3: Event-Driven Pub/Sub & Distributed Sagas',
                           'description': 'Loose coupling with events, idempotency keys, and Choreography vs '
                                          'Orchestration Sagas for transactions.',
                           'order': 3,
                           'lesson_ids': ['sys-event-driven-pubsub']}]},
    {   'slug': 'system-design-databases-sharding',
        'title': 'Distributed Databases, Sharding & Consensus',
        'domain': 'system-design',
        'description': 'Scale petabytes of data with high availability: Primary-Replica replication, Raft consensus '
                       'algorithm, database sharding with Consistent Hashing, and NoSQL vs Relational tradeoffs.',
        'category': 'System Design',
        'level': 'Advanced',
        'estimated_hours': 18,
        'icon': 'Database',
        'color': '#047857',
        'order': 21,
        'is_published': True,
        'prerequisites': ['system-design-caching-queues'],
        'skills_taught': [   'Database Replication',
                             'Raft Consensus',
                             'Database Sharding',
                             'Consistent Hashing Rings',
                             'NoSQL Document DBs',
                             'Elasticsearch Inverted Index'],
        'syllabus_overview': 'Design resilient database clusters that survive data center outages. Master horizontal '
                             'database partitioning with consistent hashing, leader election with Raft consensus, and '
                             'sub-second text search with inverted indexes.',
        'modules': [   {   'id': 'sys-db-mod-1',
                           'title': 'Module 1: Database Replication & Raft Consensus',
                           'description': 'Synchronous vs asynchronous replication, leader elections, Raft log '
                                          'consensus, and split-brain resolution.',
                           'order': 1,
                           'lesson_ids': ['sys-db-replication-consensus']},
                       {   'id': 'sys-db-mod-2',
                           'title': 'Module 2: Database Sharding & Consistent Hashing',
                           'description': 'Horizontal table partitioning, shard keys, virtual nodes on consistent '
                                          'hashing rings, and rebalancing.',
                           'order': 2,
                           'lesson_ids': ['sys-consistent-hashing-sharding']},
                       {   'id': 'sys-db-mod-3',
                           'title': 'Module 3: NoSQL, Search & Time-Series DBs',
                           'description': 'Document stores, Key-Value engines, LSM-Trees, Elasticsearch inverted '
                                          'index, and Time-Series metrics.',
                           'order': 3,
                           'lesson_ids': ['sys-nosql-timeseries-search']}]},
    {   'slug': 'git-core-internals',
        'title': 'Git Core Internals & The Directed Acyclic Graph',
        'domain': 'github',
        'description': 'Demystify Git under the hood: The .git directory, Blob/Tree/Commit object storage, '
                       'SHA-1/SHA-256 content addressing, the 3 Trees (Working, Index, Repo), and the HEAD pointer.',
        'category': 'Git & GitHub',
        'level': 'Beginner',
        'estimated_hours': 8,
        'icon': 'GitCommit',
        'color': '#F59E0B',
        'order': 22,
        'is_published': True,
        'prerequisites': [],
        'skills_taught': [   'Git Internals',
                             'Content-Addressable Storage',
                             'Blobs & Trees',
                             'Commit DAG',
                             'Staging Index',
                             'HEAD Pointer'],
        'syllabus_overview': 'Understand Git as an immutable content-addressable filesystem. Learn why commits are '
                             'snapshots instead of diffs, how Git compresses files with zlib into the object database, '
                             'and how the HEAD pointer tracks your location.',
        'modules': [   {   'id': 'git-core-mod-1',
                           'title': 'Module 1: Git Object Storage & Immutable DAG',
                           'description': 'Blobs, trees, commit objects, parent hashes, and cryptographic content '
                                          'addressing.',
                           'order': 1,
                           'lesson_ids': ['git-internals-blobs-trees-commits']},
                       {   'id': 'git-core-mod-2',
                           'title': 'Module 2: The 3 Trees: Working Directory, Index & Repo',
                           'description': 'Working copy changes, the staging index cache, and permanent commit tree '
                                          'snapshots.',
                           'order': 2,
                           'lesson_ids': ['git-staging-working-tree-index']},
                       {   'id': 'git-core-mod-3',
                           'title': 'Module 3: The HEAD Pointer, Tags & Detached HEAD',
                           'description': 'Symbolic references, lightweight tags, annotated release tags, and '
                                          'navigating detached HEAD states.',
                           'order': 3,
                           'lesson_ids': ['git-head-branches-tags']}]},
    {   'slug': 'git-branching-rebase-workflow',
        'title': 'Advanced Branching, Rebasing & Conflict Resolution',
        'domain': 'github',
        'description': 'Master professional Git branch workflows: Fast-forward vs 3-way merge commits, interactive '
                       'rebasing (`git rebase -i`), squashing messy commits, cherry-picking, and time-travel with `git '
                       'reflog`.',
        'category': 'Git & GitHub',
        'level': 'Intermediate',
        'estimated_hours': 10,
        'icon': 'GitBranch',
        'color': '#D97706',
        'order': 23,
        'is_published': True,
        'prerequisites': ['git-core-internals'],
        'skills_taught': [   'Fast-Forward Merges',
                             '3-Way Merge Commits',
                             'Interactive Rebase',
                             'Squashing Commits',
                             'Conflict Resolution',
                             'Git Reflog Time Travel'],
        'syllabus_overview': 'Maintain a pristine, linear Git history. Master interactive rebasing to clean up commit '
                             'messages before code review, resolve complex merge conflicts with ease, and recover '
                             'deleted branches using the reflog.',
        'modules': [   {   'id': 'git-branch-mod-1',
                           'title': 'Module 1: Merge Strategies: Fast-Forward vs 3-Way',
                           'description': 'Moving branch pointers forward, creating merge commits with two parents, '
                                          'and graph visualization.',
                           'order': 1,
                           'lesson_ids': ['git-branching-merge-strategies']},
                       {   'id': 'git-branch-mod-2',
                           'title': 'Module 2: Interactive Rebase & Commit History Hygiene',
                           'description': 'Squashing WIP commits, rewording messages, dropping accidental files, and '
                                          'linear history.',
                           'order': 2,
                           'lesson_ids': ['git-interactive-rebase-squash']},
                       {   'id': 'git-branch-mod-3',
                           'title': 'Module 3: Conflict Resolution & Time Travel with Reflog',
                           'description': 'Understanding conflict markers (<<<<<<< HEAD), cherry-picking commits, and '
                                          'recovering with git reflog.',
                           'order': 3,
                           'lesson_ids': ['git-merge-conflicts-cherrypick']}]},
    {   'slug': 'github-team-cicd-actions',
        'title': 'Team Pull Requests, Branch Protections & GitHub Actions CI/CD',
        'domain': 'github',
        'description': 'Collaborate like top engineering teams: GitHub Pull Request review cycles, protected branches, '
                       'required status checks, automated GitHub Actions CI/CD workflows, and automated release '
                       'tagging.',
        'category': 'Git & GitHub',
        'level': 'Intermediate',
        'estimated_hours': 12,
        'icon': 'GitPullRequest',
        'color': '#B45309',
        'order': 24,
        'is_published': True,
        'prerequisites': ['git-branching-rebase-workflow'],
        'skills_taught': [   'Pull Request Reviews',
                             'Branch Protection Rules',
                             'GitHub Actions YAML',
                             'Matrix Testing',
                             'Semantic Versioning',
                             'Automated Releases'],
        'syllabus_overview': 'Automate software quality and deployment with GitHub. Learn how to write GitHub Actions '
                             'workflows that automatically test, build, and deploy code on every push, enforce peer '
                             'review guards, and publish semver releases.',
        'modules': [   {   'id': 'git-team-mod-1',
                           'title': 'Module 1: Pull Requests, Code Reviews & Semantic Versioning',
                           'description': 'Peer reviews, code discussions, branch protection rules, and SemVer version '
                                          'increments (MAJOR.MINOR.PATCH).',
                           'order': 1,
                           'lesson_ids': ['git-github-prs-code-reviews']},
                       {   'id': 'git-team-mod-2',
                           'title': 'Module 2: Automated GitHub Actions CI/CD Pipelines',
                           'description': 'YAML workflows, runner environments, event triggers (push, pull_request), '
                                          'and matrix test execution.',
                           'order': 2,
                           'lesson_ids': ['git-actions-cicd-automation']},
                       {   'id': 'git-team-mod-3',
                           'title': 'Module 3: Automated Release Tagging & Artifact Publishing',
                           'description': 'Git tag triggers, release changelog generation, build artifact uploads, and '
                                          'production deployments.',
                           'order': 3,
                           'lesson_ids': ['git-releases-tag-publishing']}]}]

LESSONS_DATA = [   {   'slug': 'py-intro-variables',
        'course_slug': 'python-foundations',
        'module_id': 'py-mod-1',
        'title': 'Python Data Types, References & Memory Model',
        'order': 1,
        'estimated_minutes': 15,
        'difficulty': 'Beginner',
        'skill_tag': 'python_basics',
        'learning_objectives': [   'Understand how Python stores values and assigns variables in memory.',
                                   'Learn the difference between immutable items (numbers, strings) and mutable items '
                                   '(lists, arrays).',
                                   'Write clean type-annotated code suitable for machine learning scripts.'],
        'theory_sections': [   {   'title': 'Variables Are Name Tags, Not Boxes',
                                   'content_markdown': 'In Python, **variables act like sticky name tags attached to '
                                                       'objects in memory** rather than physical boxes holding '
                                                       'values.\n'
                                                       '\n'
                                                       'When you write `x = [1, 2, 3]`, Python creates a list `[1, 2, '
                                                       '3]` in memory and sticks the label `x` on it. If you then '
                                                       'write `y = x`, you simply stick a second label `y` on the '
                                                       'exact same list!\n'
                                                       '\n'
                                                       '* **Immutable types** (cannot be altered in-place): `int`, '
                                                       '`float`, `str`, `tuple`. If you change `x = 5` to `x = 6`, '
                                                       'Python creates a new number `6` and moves your name tag.\n'
                                                       '* **Mutable types** (can be altered in-place): `list`, `dict`, '
                                                       '`set`, `numpy.ndarray`. Modifying a list with `x.append(4)` '
                                                       'changes the object directly in memory for all variables '
                                                       'pointing to it.',
                                   'key_takeaway': 'Remember that sharing lists or model weight arrays across '
                                                   'functions means any change will affect the original data unless '
                                                   'you explicitly copy it.'},
                               {   'title': 'Type Hints for AI Engineering',
                                   'content_markdown': 'In modern AI code, adding type hints tells your team (and '
                                                       'editor) what type of data each function expects:\n'
                                                       '\n'
                                                       '```python\n'
                                                       'from typing import List\n'
                                                       '\n'
                                                       'def calculate_average(scores: List[float]) -> float:\n'
                                                       '    return sum(scores) / len(scores)\n'
                                                       '```\n'
                                                       '\n'
                                                       'This makes working with complex batches of images, tokens, and '
                                                       'matrix dimensions clear and bug-free.',
                                   'key_takeaway': 'Use type hints like List[float] or np.ndarray so you always know '
                                                   'what shapes and types your functions are processing.'}],
        'visual_explainer': {   'type': 'architecture_flow',
                                'title': 'Python Variable Reference Model',
                                'subtitle': 'How variable name tags point to heap memory',
                                'diagram_type': 'memory_pointer',
                                'parameters': {'variable': 'weights_vector', 'target_heap': '0x7ffee1b'}},
        'code_example': {   'title': 'Checking Object Memory Identity in Python',
                            'language': 'python',
                            'code': 'import copy\n'
                                    'from typing import List\n'
                                    '\n'
                                    'def normalize_scores(raw_scores: List[float]) -> List[float]:\n'
                                    '    """Calculates simple percentages from a list of raw scores."""\n'
                                    '    total = sum(raw_scores)\n'
                                    '    if total == 0:\n'
                                    '        return [0.0] * len(raw_scores)\n'
                                    '    return [round(score / total, 2) for score in raw_scores]\n'
                                    '\n'
                                    'scores = [10.0, 20.0, 70.0]\n'
                                    'percentages = normalize_scores(scores)\n'
                                    'print(f"Raw Scores:   {scores}")\n'
                                    'print(f"Percentages:  {percentages}")\n'
                                    'print(f"Total Check:  {sum(percentages):.2f}")',
                            'explanation': 'This example normalizes a list of scores so they represent clear '
                                           'probabilities between 0.0 and 1.0.',
                            'output_preview': 'Raw Scores:   [10.0, 20.0, 70.0]\n'
                                              'Percentages:  [0.1, 0.2, 0.7]\n'
                                              'Total Check:  1.00'},
        'quiz_id': 'quiz-py-intro-variables',
        'summary': 'You explored how Python variables point to memory and how mutability affects data manipulation.',
        'next_lesson_slug': 'py-data-structures-comprehensions',
        'prev_lesson_slug': None},
    {   'slug': 'py-data-structures-comprehensions',
        'course_slug': 'python-foundations',
        'module_id': 'py-mod-1',
        'title': 'Lists, Dictionaries & Supercharged List Comprehensions',
        'order': 2,
        'estimated_minutes': 15,
        'difficulty': 'Beginner',
        'skill_tag': 'python_basics',
        'learning_objectives': [   'Master Python dictionaries for feature storage and metadata mapping.',
                                   'Use list and dictionary comprehensions to transform data in a single clean line.',
                                   'Filter outliers and normalize data with clean Pythonic expressions.'],
        'theory_sections': [   {   'title': 'Dictionaries: The Backbone of AI Datasets',
                                   'content_markdown': 'In Machine Learning, almost every sample is a key-value '
                                                       'dictionary (e.g., `{"age": 25, "income": 50000, "label": '
                                                       '1}`).\n'
                                                       '\n'
                                                       'Dictionaries give **instant O(1) lookup time** by hash key, '
                                                       'making them ideal for storing vocabularies, token mappings, '
                                                       'and model configurations.',
                                   'key_takeaway': 'Use dictionaries for fast feature lookups and category-to-number '
                                                   'mappings.'},
                               {   'title': 'List Comprehensions: Fast & Readable Transformations',
                                   'content_markdown': 'Instead of writing 4-line `for` loops to process numbers:\n'
                                                       '\n'
                                                       '```python\n'
                                                       '# Slow & bulky:\n'
                                                       'scaled = []\n'
                                                       'for x in raw_data:\n'
                                                       '    if x > 0:\n'
                                                       '        scaled.append(x * 2)\n'
                                                       '\n'
                                                       '# Pythonic 1-liner:\n'
                                                       'scaled = [x * 2 for x in raw_data if x > 0]\n'
                                                       '```\n'
                                                       '\n'
                                                       'List comprehensions run in compiled C speed under the hood in '
                                                       'Python, making them faster and much easier to read.',
                                   'key_takeaway': 'List comprehensions combine transformation and filtering into one '
                                                   'concise, fast statement.'}],
        'visual_explainer': {   'type': 'diagram',
                                'title': 'List Comprehension Pipeline',
                                'subtitle': 'Input List -> Filter Condition -> Expression Transform -> Output List',
                                'diagram_type': 'data_pipeline',
                                'parameters': {'input_size': 5, 'filtered_size': 3}},
        'code_example': {   'title': 'Building a Token-to-ID Vocabulary with Dict Comprehensions',
                            'language': 'python',
                            'code': '# Unique words in our AI dataset\n'
                                    "vocab = ['<PAD>', 'apple', 'banana', 'cherry', '<UNK>']\n"
                                    '\n'
                                    '# Build mapping: word -> integer ID\n'
                                    'word2id = {word: idx for idx, word in enumerate(vocab)}\n'
                                    '\n'
                                    '# Build reverse mapping: integer ID -> word\n'
                                    'id2word = {idx: word for word, idx in word2id.items()}\n'
                                    '\n'
                                    'print("Word to ID mapping:", word2id)\n'
                                    'print("Looking up ID for \'banana\':", word2id[\'banana\'])\n'
                                    'print("Reversing ID 2 back to word:", id2word[2])',
                            'explanation': 'Demonstrates dictionary comprehensions to build the bidirectional '
                                           'vocabulary lookup tables used in every NLP model.',
                            'output_preview': "Word to ID mapping: {'<PAD>': 0, 'apple': 1, 'banana': 2, 'cherry': 3, "
                                              "'<UNK>': 4}\n"
                                              "Looking up ID for 'banana': 2\n"
                                              'Reversing ID 2 back to word: banana'},
        'quiz_id': 'quiz-py-data-structures-comprehensions',
        'summary': 'You mastered dictionaries and list comprehensions to cleanly transform and filter data.',
        'next_lesson_slug': 'py-numpy-arrays-broadcasting',
        'prev_lesson_slug': 'py-intro-variables'},
    {   'slug': 'py-numpy-arrays-broadcasting',
        'course_slug': 'python-foundations',
        'module_id': 'py-mod-2',
        'title': 'NumPy Arrays & Fast Broadcasting',
        'order': 3,
        'estimated_minutes': 20,
        'difficulty': 'Beginner',
        'skill_tag': 'numpy_basics',
        'learning_objectives': [   'Learn why NumPy arrays are 100x faster than standard Python lists.',
                                   'Understand array shapes (rows, columns, dimensions).',
                                   'Master Broadcasting: Doing math on arrays of different sizes without loops.'],
        'theory_sections': [   {   'title': 'Why Is NumPy So Fast?',
                                   'content_markdown': 'Standard Python lists are flexible but slow because each '
                                                       'number is wrapped in a full Python object stored across '
                                                       'scattered memory addresses.\n'
                                                       '\n'
                                                       '**NumPy arrays (`ndarray`) pack numbers side-by-side in raw '
                                                       'computer memory**, like books lined up neatly on a bookshelf. '
                                                       'This allows your processor to calculate thousands of numbers '
                                                       'in a single clock cycle (SIMD vectorization), making matrix '
                                                       'math **50x to 200x faster** than a Python `for` loop.',
                                   'key_takeaway': 'In machine learning, always use NumPy vectorized operations '
                                                   'instead of writing loops over data rows.'},
                               {   'title': 'The Magic of Broadcasting',
                                   'content_markdown': "Broadcasting is NumPy's ability to perform math between arrays "
                                                       'of different shapes automatically.\n'
                                                       '\n'
                                                       '**Analogy**: Imagine you have a shopping receipt with 10 item '
                                                       'prices in a column. If you want to add 5% sales tax to every '
                                                       "item, you don't need a table of 10 tax rates—you just multiply "
                                                       "the whole column by `1.05`! NumPy automatically 'stretches' "
                                                       'the single number across all 10 rows.\n'
                                                       '\n'
                                                       '**The Rule**: Two dimensions are compatible when:\n'
                                                       '1. They have the **exact same size**, OR\n'
                                                       '2. One of them is **1** (NumPy will stretch the 1 to match the '
                                                       'other size).',
                                   'key_takeaway': 'Broadcasting allows you to normalize entire datasets with a single '
                                                   'line: (X - mean) / std.'}],
        'visual_explainer': {   'type': 'simulation_preview',
                                'title': '2D Broadcasting Mechanics',
                                'subtitle': 'Stretching a 1D vector across matching rows',
                                'diagram_type': 'broadcasting_grid',
                                'parameters': {'matrix_shape': [3, 3], 'vector_shape': [1, 3]}},
        'code_example': {   'title': 'Standardizing Data Features with Broadcasting',
                            'language': 'python',
                            'code': 'import numpy as np\n'
                                    '\n'
                                    '# 4 House listings: [Square Footage, Bedrooms, Age in Years]\n'
                                    'houses = np.array([\n'
                                    '    [1200.0, 2.0, 10.0],\n'
                                    '    [1800.0, 3.0, 5.0],\n'
                                    '    [2400.0, 4.0, 15.0],\n'
                                    '    [3000.0, 5.0, 2.0]\n'
                                    '])\n'
                                    '\n'
                                    '# Calculate average of each column\n'
                                    'column_averages = np.mean(houses, axis=0)\n'
                                    '\n'
                                    '# Center the data around 0 by subtracting column averages\n'
                                    'centered_houses = houses - column_averages\n'
                                    '\n'
                                    'print("Average for each feature:", column_averages)\n'
                                    'print("Centered houses:\\n", centered_houses)',
                            'explanation': 'NumPy stretches the 3-element average vector across all 4 houses '
                                           'automatically without needing any loop.',
                            'output_preview': 'Average for each feature: [2100.    3.5    8. ]\n'
                                              'Centered houses:\n'
                                              ' [[-900.   -1.5   2. ]\n'
                                              '  [-300.   -0.5  -3. ]\n'
                                              '  [ 300.    0.5   7. ]\n'
                                              '  [ 900.    1.5  -6. ]]'},
        'quiz_id': 'quiz-py-numpy-arrays-broadcasting',
        'summary': 'You learned how NumPy arrays accelerate AI computations and how broadcasting handles '
                   'multi-dimensional math seamlessly.',
        'next_lesson_slug': 'py-numpy-matrix-operations',
        'prev_lesson_slug': 'py-data-structures-comprehensions'},
    {   'slug': 'py-numpy-matrix-operations',
        'course_slug': 'python-foundations',
        'module_id': 'py-mod-2',
        'title': 'Matrix Multiplication, Dot Products & Reshaping',
        'order': 4,
        'estimated_minutes': 20,
        'difficulty': 'Beginner',
        'skill_tag': 'numpy_basics',
        'learning_objectives': [   'Differentiate element-wise multiplication (*) from matrix multiplication (@ or '
                                   'np.dot).',
                                   'Master matrix reshaping and flattening (turning 2D images into 1D vectors).',
                                   'Understand the inner-dimension matching rule: (M, K) @ (K, N) -> (M, N).'],
        'theory_sections': [   {   'title': 'Element-Wise (*) vs Matrix Multiplication (@)',
                                   'content_markdown': 'One of the most common beginner bugs in machine learning is '
                                                       'mixing up `*` and `@`:\n'
                                                       '\n'
                                                       '* **`A * B` (Element-wise / Hadamard)**: Multiplies matching '
                                                       'slots individually. Both matrices must have matching shapes.\n'
                                                       '* **`A @ B` (Matrix Multiplication)**: Takes rows of A and '
                                                       'computes dot products with columns of B. **The columns of A '
                                                       'must match the rows of B!**',
                                   'key_takeaway': 'In neural networks, passing data through a layer is always matrix '
                                                   'multiplication: output = inputs @ weights + bias.'},
                               {   'title': 'Reshaping Tensors',
                                   'content_markdown': 'In computer vision, a grayscale image is a 28x28 grid of '
                                                       'pixels (784 numbers). To feed it into a linear classifier, we '
                                                       '**reshape** or **flatten** it into a single vector of shape '
                                                       '`(784,)` or `(1, 784)`.\n'
                                                       '\n'
                                                       'Using `array.reshape(rows, -1)` lets NumPy automatically '
                                                       'calculate the missing dimension.',
                                   'key_takeaway': 'Reshaping reorganizes dimensions without moving or duplicating the '
                                                   'underlying data in memory.'}],
        'visual_explainer': {   'type': 'diagram',
                                'title': 'Matrix Multiplication Shape Rule',
                                'subtitle': '(Batch Size, Features) @ (Features, Hidden) -> (Batch Size, Hidden)',
                                'diagram_type': 'matrix_dimension_match',
                                'parameters': {'shape_A': [4, 3], 'shape_B': [3, 2], 'shape_out': [4, 2]}},
        'code_example': {   'title': 'Matrix Operations and Neural Layer Simulation',
                            'language': 'python',
                            'code': 'import numpy as np\n'
                                    '\n'
                                    '# 2 input samples (e.g. 2 user profiles with 3 features each)\n'
                                    'X = np.array([\n'
                                    '    [1.0, 2.0, 3.0],\n'
                                    '    [0.5, 1.5, 2.5]\n'
                                    '])\n'
                                    '\n'
                                    '# Layer weights: 3 input features -> 2 output predictions\n'
                                    'W = np.array([\n'
                                    '    [0.2, 0.8],\n'
                                    '    [0.5, 0.1],\n'
                                    '    [-0.3, 0.4]\n'
                                    '])\n'
                                    'b = np.array([0.1, -0.2])\n'
                                    '\n'
                                    '# Calculate layer output: Y = X @ W + b\n'
                                    'Y = X @ W + b\n'
                                    '\n'
                                    'print("Input shape:", X.shape)\n'
                                    'print("Weights shape:", W.shape)\n'
                                    'print("Layer Output shape:", Y.shape)\n'
                                    'print("Layer Output values:\\n", np.round(Y, 3))',
                            'explanation': 'Calculates the forward pass of a basic linear layer with 2 samples passing '
                                           'through 2 output neurons.',
                            'output_preview': 'Input shape: (2, 3)\n'
                                              'Weights shape: (3, 2)\n'
                                              'Layer Output shape: (2, 2)\n'
                                              'Layer Output values:\n'
                                              ' [[ 0.4   2.  ]\n'
                                              '  [ 0.2   1.35]]'},
        'quiz_id': 'quiz-py-numpy-matrix-operations',
        'summary': 'You learned the crucial difference between element-wise math and matrix multiplication, and how to '
                   'reshape tensors.',
        'next_lesson_slug': 'py-pandas-dataframes-cleaning',
        'prev_lesson_slug': 'py-numpy-arrays-broadcasting'},
    {   'slug': 'py-pandas-dataframes-cleaning',
        'course_slug': 'python-foundations',
        'module_id': 'py-mod-3',
        'title': 'Pandas: Loading, Filtering & Cleaning Messy AI Data',
        'order': 5,
        'estimated_minutes': 20,
        'difficulty': 'Beginner',
        'skill_tag': 'data_preprocessing',
        'learning_objectives': [   'Understand DataFrames as organized tables with named columns and row indices.',
                                   'Filter, sort, and select data slices using boolean conditions and `.loc`/`.iloc`.',
                                   'Impute missing values (`NaN`) and convert categorical text to numerical labels.'],
        'theory_sections': [   {   'title': 'Data Is Always Messy',
                                   'content_markdown': 'Real-world AI projects spend 80% of their time preparing data. '
                                                       'Real datasets contain:\n'
                                                       '* Missing values (`NaN` or `None`)\n'
                                                       "* Inconsistent text ('Yes', 'yes', 'Y')\n"
                                                       '* Outliers and corrupted rows\n'
                                                       '\n'
                                                       '**Pandas** provides fast, tabular tools built on top of NumPy '
                                                       'to clean and structure data before sending it to machine '
                                                       'learning models.',
                                   'key_takeaway': 'Clean data produces reliable models. Garbage in means garbage '
                                                   'out.'},
                               {   'title': 'Handling Missing Values',
                                   'content_markdown': 'Machine learning algorithms crash if given `NaN` (Not a '
                                                       'Number). You have two main strategies:\n'
                                                       '1. **Drop rows (`df.dropna()`)**: Good if only 1% of rows are '
                                                       'missing.\n'
                                                       '2. **Impute (`df.fillna(df.mean())`)**: Replace missing '
                                                       'numbers with column mean/median to retain all data rows.',
                                   'key_takeaway': 'Always inspect and fill missing values before converting a '
                                                   'DataFrame to a NumPy training matrix.'}],
        'visual_explainer': {   'type': 'table_preview',
                                'title': 'DataFrame Cleaning Pipeline',
                                'subtitle': 'Raw CSV -> Impute Missing Values -> Encode Labels -> ML Matrix (X, y)',
                                'diagram_type': 'tabular_pipeline'},
        'code_example': {   'title': 'Loading, Cleaning & Preparing a Dataset in Pandas',
                            'language': 'python',
                            'code': 'import pandas as pd\n'
                                    'import numpy as np\n'
                                    '\n'
                                    '# Simulated raw tabular data\n'
                                    'raw_data = {\n'
                                    "    'Age': [22, 38, np.nan, 35, 54],\n"
                                    "    'Salary': [45000, 82000, 61000, np.nan, 110000],\n"
                                    "    'Purchased': ['No', 'Yes', 'No', 'Yes', 'Yes']\n"
                                    '}\n'
                                    '\n'
                                    'df = pd.DataFrame(raw_data)\n'
                                    'print("--- Raw Dataset ---")\n'
                                    'print(df)\n'
                                    '\n'
                                    '# 1. Fill missing numeric values with column median\n'
                                    "df['Age'] = df['Age'].fillna(df['Age'].median())\n"
                                    "df['Salary'] = df['Salary'].fillna(df['Salary'].median())\n"
                                    '\n'
                                    "# 2. Convert 'Purchased' text into binary 0/1 integers\n"
                                    "df['Purchased'] = df['Purchased'].map({'No': 0, 'Yes': 1})\n"
                                    '\n'
                                    'print("\\n--- Cleaned ML-Ready Dataset ---")\n'
                                    'print(df)',
                            'explanation': 'Demonstrates replacing missing values with median statistics and mapping '
                                           'text categories into numbers.',
                            'output_preview': '--- Raw Dataset ---\n'
                                              '    Age    Salary Purchased\n'
                                              '0  22.0   45000.0        No\n'
                                              '1  38.0   82000.0       Yes\n'
                                              '2   NaN   61000.0        No\n'
                                              '3  35.0       NaN       Yes\n'
                                              '4  54.0  110000.0       Yes\n'
                                              '\n'
                                              '--- Cleaned ML-Ready Dataset ---\n'
                                              '    Age    Salary  Purchased\n'
                                              '0  22.0   45000.0          0\n'
                                              '1  38.0   82000.0          1\n'
                                              '2  36.5   61000.0          0\n'
                                              '3  35.0   71500.0          1\n'
                                              '4  54.0  110000.0          1'},
        'quiz_id': 'quiz-py-pandas-dataframes-cleaning',
        'summary': 'You learned how to clean tabular datasets, fill missing values, and prepare data for ML models.',
        'next_lesson_slug': 'math-vectors-dot-products',
        'prev_lesson_slug': 'py-numpy-matrix-operations'},
    {   'slug': 'math-vectors-dot-products',
        'course_slug': 'math-for-ai',
        'module_id': 'math-mod-1',
        'title': 'Vectors, Dot Products & Measuring Similarity',
        'order': 1,
        'estimated_minutes': 20,
        'difficulty': 'Intermediate',
        'skill_tag': 'linear_algebra',
        'learning_objectives': [   'Understand vectors as lists of numbers representing features or directions in '
                                   'space.',
                                   'Calculate the dot product step-by-step: multiply matching elements and add them '
                                   'up.',
                                   'Learn how dot products measure similarity between search queries, movies, or '
                                   'words.'],
        'theory_sections': [   {   'title': 'What is a Vector?',
                                   'content_markdown': 'A **vector** is simply an ordered list of numbers that '
                                                       "describes an object's features or a direction in space.\n"
                                                       '\n'
                                                       '**Real-World Example**: A house can be represented as a '
                                                       '3-element vector:\n'
                                                       '\n'
                                                       '$$House = [2000, 3, 2]$$\n'
                                                       '\n'
                                                       'Where `2000` is square feet, `3` is bedrooms, and `2` is '
                                                       'bathrooms. In AI, words, images, and user preferences are all '
                                                       'converted into vectors so math algorithms can compare them.',
                                   'key_takeaway': 'Everything in AI—from words to pictures—is converted into a vector '
                                                   'of numbers.'},
                               {   'title': 'The Dot Product: Measuring Similarity',
                                   'content_markdown': 'The **dot product** is the most important operation in AI. You '
                                                       'calculate it in two simple steps:\n'
                                                       '1. Multiply matching items from two vectors together.\n'
                                                       '2. Sum up all the products into one final number.\n'
                                                       '\n'
                                                       '$$u · v = (u_1 × v_1) + (u_2 × v_2) + ... + (u_n × v_n)$$\n'
                                                       '\n'
                                                       '**Example Calculation**:\n'
                                                       "If User A's movie taste is `[5, 1]` (loves Action, dislikes "
                                                       'Romance) and Movie X is `[4, 0]` (high Action, no Romance):\n'
                                                       '\n'
                                                       '$$Score = (5 × 4) + (1 × 0) = 20 + 0 = 20$$\n'
                                                       '\n'
                                                       '* **Positive Dot Product**: Vectors point in a similar '
                                                       'direction (strong match!).\n'
                                                       '* **Zero (0) Dot Product**: Vectors are perpendicular / '
                                                       'completely independent.\n'
                                                       '* **Negative Dot Product**: Vectors point in opposite '
                                                       'directions.',
                                   'key_takeaway': 'Dot products power recommendation engines, search algorithms, and '
                                                   'Transformer self-attention by checking how well two items align.'}],
        'visual_explainer': {   'type': 'chart',
                                'title': 'Vector Dot Product & Angle Similarity',
                                'subtitle': 'Interactive vector alignment in 2D space',
                                'diagram_type': 'vector_plane',
                                'parameters': {'vector_u': [3, 4], 'vector_v': [4, 1]}},
        'code_example': {   'title': 'Measuring Similarity Between Words Using Vectors',
                            'language': 'python',
                            'code': 'import numpy as np\n'
                                    '\n'
                                    'def cosine_similarity(u: np.ndarray, v: np.ndarray) -> float:\n'
                                    '    """Calculates how closely two vectors align (1.0 = identical match)."""\n'
                                    '    dot = np.dot(u, v)\n'
                                    '    length_u = np.linalg.norm(u)\n'
                                    '    length_v = np.linalg.norm(v)\n'
                                    '    return float(dot / (length_u * length_v))\n'
                                    '\n'
                                    '# 2D Word embeddings\n'
                                    'word_king   = np.array([0.9, 0.8])\n'
                                    'word_queen  = np.array([0.85, 0.82])\n'
                                    'word_banana = np.array([0.1, -0.9])\n'
                                    '\n'
                                    'sim_royals = cosine_similarity(word_king, word_queen)\n'
                                    'sim_fruit  = cosine_similarity(word_king, word_banana)\n'
                                    '\n'
                                    'print(f"Similarity (King, Queen):  {sim_royals:.4f} (Almost Identical!)")\n'
                                    'print(f"Similarity (King, Banana): {sim_fruit:.4f} (Unrelated / Opposite)")',
                            'explanation': 'Calculates cosine similarity to demonstrate that words with related '
                                           'concepts point in the same direction.',
                            'output_preview': 'Similarity (King, Queen):  0.9992 (Almost Identical!)\n'
                                              'Similarity (King, Banana): -0.5694 (Unrelated / Opposite)'},
        'quiz_id': 'quiz-math-vectors-dot-products',
        'summary': 'You mastered vectors and learned how dot products compare similarity between data points.',
        'next_lesson_slug': 'math-matrix-multiplication',
        'prev_lesson_slug': 'py-pandas-dataframes-cleaning'},
    {   'slug': 'math-matrix-multiplication',
        'course_slug': 'math-for-ai',
        'module_id': 'math-mod-1',
        'title': 'Matrix Multiplication: Geometric Transformations Made Easy',
        'order': 2,
        'estimated_minutes': 20,
        'difficulty': 'Intermediate',
        'skill_tag': 'linear_algebra',
        'learning_objectives': [   'Visualize matrices as geometric transformations that stretch, rotate, and project '
                                   'space.',
                                   'Understand how multiplying a dataset matrix by a weight matrix transforms raw '
                                   'features into predictions.',
                                   'Grasp why GPUs excel at parallel matrix multiplication.'],
        'theory_sections': [   {   'title': 'Matrices as Space Modifiers',
                                   'content_markdown': 'Instead of viewing a matrix as a boring spreadsheet of '
                                                       'numbers, think of it as a **space transformer**:\n'
                                                       '* It can rotate 2D points by 45 degrees.\n'
                                                       '* It can stretch space horizontally or compress it '
                                                       'vertically.\n'
                                                       '* It can project a 1000-dimensional image down into a compact '
                                                       '10-dimensional summary!\n'
                                                       '\n'
                                                       'When you multiply an input vector $x$ by a weight matrix $W$, '
                                                       'you are transforming your data into a new coordinate system '
                                                       'where patterns are easier to separate.',
                                   'key_takeaway': 'Matrix multiplication rotates and warps data space to make '
                                                   'classifications clear.'},
                               {   'title': 'Why Neural Networks Rely on Matrices',
                                   'content_markdown': 'A neural network layer with 1,000 inputs and 500 outputs needs '
                                                       '500,000 individual weight connections.\n'
                                                       '\n'
                                                       'Instead of computing 500,000 separate equations one by one, we '
                                                       'write:\n'
                                                       '$$Y = X · W + b$$\n'
                                                       '\n'
                                                       'Modern GPUs contain thousands of tiny tensor cores designed '
                                                       'specifically to execute these matrix operations simultaneously '
                                                       'in nanoseconds.',
                                   'key_takeaway': 'Matrix formulation allows parallel hardware (GPUs/TPUs) to compute '
                                                   'millions of predictions simultaneously.'}],
        'visual_explainer': {   'type': 'diagram',
                                'title': '2D Space Rotation via Transformation Matrix',
                                'subtitle': 'Grid lines warping under 2x2 linear transformation',
                                'diagram_type': 'space_transformation',
                                'parameters': {'angle_deg': 45, 'scale_x': 1.2, 'scale_y': 0.8}},
        'code_example': {   'title': 'Rotating 2D Geometric Points with a Rotation Matrix',
                            'language': 'python',
                            'code': 'import numpy as np\n'
                                    '\n'
                                    '# Square coordinates in 2D space: [x, y]\n'
                                    'square = np.array([\n'
                                    '    [1.0, 1.0],\n'
                                    '    [-1.0, 1.0],\n'
                                    '    [-1.0, -1.0],\n'
                                    '    [1.0, -1.0]\n'
                                    '])\n'
                                    '\n'
                                    '# 90-degree counterclockwise rotation matrix\n'
                                    'theta = np.radians(90)\n'
                                    'rotation_matrix = np.array([\n'
                                    '    [np.cos(theta), -np.sin(theta)],\n'
                                    '    [np.sin(theta),  np.cos(theta)]\n'
                                    '])\n'
                                    '\n'
                                    '# Rotate all points at once: (N, 2) @ (2, 2)\n'
                                    'rotated_square = square @ rotation_matrix.T\n'
                                    '\n'
                                    'print("Original Point [1, 1] rotated to:", np.round(rotated_square[0], 2))\n'
                                    'print("Original Point [-1, 1] rotated to:", np.round(rotated_square[1], 2))',
                            'explanation': 'Applies a 90-degree 2D rotation matrix across multiple coordinate vertices '
                                           'in a single matrix multiplication step.',
                            'output_preview': 'Original Point [1, 1] rotated to: [-1.  1.]\n'
                                              'Original Point [-1, 1] rotated to: [-1. -1.]'},
        'quiz_id': 'quiz-math-matrix-multiplication',
        'summary': 'You visualized matrix multiplication as geometric transformations and learned why it powers deep '
                   'learning on GPUs.',
        'next_lesson_slug': 'math-derivatives-gradients',
        'prev_lesson_slug': 'math-vectors-dot-products'},
    {   'slug': 'math-derivatives-gradients',
        'course_slug': 'math-for-ai',
        'module_id': 'math-mod-2',
        'title': 'Derivatives, Slopes & The Gradient Compass',
        'order': 3,
        'estimated_minutes': 25,
        'difficulty': 'Intermediate',
        'skill_tag': 'calculus',
        'learning_objectives': [   'Understand a derivative as a slope measuring how quickly an output changes.',
                                   'Learn what a partial derivative is (changing one setting while holding others '
                                   'still).',
                                   'Understand the Gradient as a compass that points uphill, while negative gradient '
                                   'points downhill.'],
        'theory_sections': [   {   'title': 'What is a Derivative?',
                                   'content_markdown': 'A **derivative** is simply the slope of a curve at a single '
                                                       'point.\n'
                                                       '\n'
                                                       '**Everyday Analogy**: If you are driving a car and glance at '
                                                       'your speedometer, it tells you your rate of change right now '
                                                       '(e.g. 60 mph). In machine learning, the derivative tells us: '
                                                       "*'If I nudge weight setting w by a tiny bit, will the model's "
                                                       "error go UP or DOWN?'*",
                                   'key_takeaway': 'Derivatives tell us which direction to tweak our model settings to '
                                                   'reduce prediction mistakes.'},
                               {   'title': 'The Gradient: The Compass of AI',
                                   'content_markdown': 'When an AI model has multiple weight parameters ($w_1, w_2, '
                                                       'w_3$), we compute the partial derivative for each one.\n'
                                                       '\n'
                                                       'The collection of all these slopes in a single list is called '
                                                       'the **Gradient** ($\n'
                                                       'abla L$):\n'
                                                       '\n'
                                                       '$$\\text{Gradient} = [\\text{Slope for } w_1, \\text{Slope for '
                                                       '} w_2, \\dots, \\text{Slope for } w_n]$$\n'
                                                       '\n'
                                                       '**The Golden Rule of Gradient Descent**:\n'
                                                       '* **The Gradient points UPHILL** (toward higher '
                                                       'error/mistakes).\n'
                                                       '* **The Negative Gradient points DOWNHILL** (toward minimum '
                                                       'error and best accuracy!).',
                                   'key_takeaway': 'To train an AI model, we take small steps downhill in the opposite '
                                                   'direction of the gradient: w_new = w_old - learning_rate * '
                                                   'gradient.'}],
        'visual_explainer': {   'type': 'diagram',
                                'title': 'Loss Surface Gradient Descent Path',
                                'subtitle': 'Stepping downhill toward the lowest prediction error',
                                'diagram_type': 'contour_gradient'},
        'code_example': {   'title': 'Computing Slopes and Stepping Downhill in Python',
                            'language': 'python',
                            'code': 'import numpy as np\n'
                                    '\n'
                                    '# Error function: Error = (w - 3)^2\n'
                                    '# The minimum error happens at w = 3.0\n'
                                    'def error_fn(w: float) -> float:\n'
                                    '    return (w - 3.0) ** 2\n'
                                    '\n'
                                    'def derivative_slope(w: float) -> float:\n'
                                    '    # Derivative of (w - 3)^2 is 2 * (w - 3)\n'
                                    '    return 2.0 * (w - 3.0)\n'
                                    '\n'
                                    '# Start with an incorrect guess for w\n'
                                    'w = 10.0\n'
                                    'learning_rate = 0.2\n'
                                    '\n'
                                    'print(f"Starting weight: {w}, Error: {error_fn(w):.2f}")\n'
                                    'for step in range(5):\n'
                                    '    slope = derivative_slope(w)\n'
                                    '    w = w - learning_rate * slope\n'
                                    '    print(f"Step {step+1}: Slope={slope:.2f}, New w={w:.2f}, '
                                    'Error={error_fn(w):.2f}")',
                            'explanation': 'Shows how stepping in the opposite direction of the slope automatically '
                                           'brings w closer to the ideal target (3.0).',
                            'output_preview': 'Starting weight: 10.0, Error: 49.00\n'
                                              'Step 1: Slope=14.00, New w=7.20, Error=17.64\n'
                                              'Step 2: Slope=8.40, New w=5.52, Error=6.35\n'
                                              'Step 3: Slope=5.04, New w=4.51, Error=2.29\n'
                                              'Step 4: Slope=3.02, New w=3.91, Error=0.82\n'
                                              'Step 5: Slope=1.81, New w=3.54, Error=0.30'},
        'quiz_id': 'quiz-math-derivatives-gradients',
        'summary': 'You understood derivatives as slopes and learned why algorithms step downhill using the negative '
                   'gradient.',
        'next_lesson_slug': 'math-chain-rule-backprop-math',
        'prev_lesson_slug': 'math-matrix-multiplication'},
    {   'slug': 'math-chain-rule-backprop-math',
        'course_slug': 'math-for-ai',
        'module_id': 'math-mod-2',
        'title': 'The Chain Rule: Passing Slopes Through Connected Equations',
        'order': 4,
        'estimated_minutes': 25,
        'difficulty': 'Intermediate',
        'skill_tag': 'calculus',
        'learning_objectives': [   'Understand the Chain Rule as multiplying rates of change along a chain of gears or '
                                   'dominoes.',
                                   'See how changing an early weight propagates through intermediate layers to change '
                                   'the final loss.',
                                   'Master the core mathematical foundation behind Backpropagation.'],
        'theory_sections': [   {   'title': 'The Gear Analogy',
                                   'content_markdown': 'Imagine three connected gears: A, B, and C.\n'
                                                       '* When Gear A turns 1 time, Gear B turns 2 times '
                                                       '($\\frac{dB}{dA} = 2$).\n'
                                                       '* When Gear B turns 1 time, Gear C turns 3 times '
                                                       '($\\frac{dC}{dB} = 3$).\n'
                                                       '\n'
                                                       'How many times does Gear C turn when you turn Gear A once? '
                                                       '**You multiply them!**\n'
                                                       '$$\\frac{dC}{dA} = \\frac{dC}{dB} × \\frac{dB}{dA} = 3 × 2 = '
                                                       '6$$\n'
                                                       '\n'
                                                       'That is the **Chain Rule**! If functions are nested $y = '
                                                       'f(g(x))$, you simply multiply their local derivatives '
                                                       'together.',
                                   'key_takeaway': 'The Chain Rule lets you find how a change at the beginning of a '
                                                   'long network affects the final output by multiplying local '
                                                   'slopes.'},
                               {   'title': 'Why AI Needs the Chain Rule',
                                   'content_markdown': 'In a 50-layer deep neural network, the loss at the end depends '
                                                       'on Layer 50, which depends on Layer 49... all the way back to '
                                                       'Layer 1.\n'
                                                       '\n'
                                                       'The Chain Rule allows us to compute the exact gradient for '
                                                       'Layer 1 by smoothly multiplying backwards step-by-step.',
                                   'key_takeaway': 'Backpropagation is simply the Chain Rule implemented efficiently '
                                                   'from right to left.'}],
        'visual_explainer': {   'type': 'diagram',
                                'title': 'Chain Rule Derivative Flow',
                                'subtitle': 'dL/dw = (dL/dy) * (dy/dz) * (dz/dw)',
                                'diagram_type': 'computational_graph',
                                'parameters': {'nodes': ['w', 'z = w*x', 'y = relu(z)', 'Loss = (y-t)^2']}},
        'code_example': {   'title': 'Manual Chain Rule Computation vs Numerical Derivative',
                            'language': 'python',
                            'code': '# Function: y = (2x + 1)^2\n'
                                    '# Local functions: u = 2x + 1, y = u^2\n'
                                    'x = 3.0\n'
                                    '\n'
                                    '# Forward pass\n'
                                    'u = 2 * x + 1    # u = 7.0\n'
                                    'y = u ** 2       # y = 49.0\n'
                                    '\n'
                                    '# Analytical Chain Rule: dy/dx = (dy/du) * (du/dx)\n'
                                    'dy_du = 2 * u    # dy/du = 14.0\n'
                                    'du_dx = 2.0      # du/dx = 2.0\n'
                                    'dy_dx = dy_du * du_dx  # 14.0 * 2.0 = 28.0\n'
                                    '\n'
                                    '# Numerical check: [f(x+h) - f(x)] / h\n'
                                    'h = 0.0001\n'
                                    'numerical_dy_dx = (((2 * (x + h) + 1)**2) - y) / h\n'
                                    '\n'
                                    'print(f"Analytical Chain Rule Gradient: {dy_dx:.4f}")\n'
                                    'print(f"Numerical Approximation:       {numerical_dy_dx:.4f}")',
                            'explanation': 'Calculates the derivative of a composite function using the chain rule and '
                                           'verifies it against finite differences.',
                            'output_preview': 'Analytical Chain Rule Gradient: 28.0000\n'
                                              'Numerical Approximation:       28.0004'},
        'quiz_id': 'quiz-math-chain-rule-backprop-math',
        'summary': 'You understood the Chain Rule as gear multiplication and learned how gradients flow backwards '
                   'through connected layers.',
        'next_lesson_slug': 'math-probability-bayes-theorem',
        'prev_lesson_slug': 'math-derivatives-gradients'},
    {   'slug': 'math-probability-bayes-theorem',
        'course_slug': 'math-for-ai',
        'module_id': 'math-mod-3',
        'title': "Probability & Bayes' Theorem: Updating Beliefs with Evidence",
        'order': 5,
        'estimated_minutes': 20,
        'difficulty': 'Intermediate',
        'skill_tag': 'probability',
        'learning_objectives': [   'Differentiate Prior Probability (base belief) from Posterior Probability (updated '
                                   'belief).',
                                   "Understand Bayes' Theorem formula and its application in spam filtering and "
                                   'medical diagnostics.',
                                   'Learn how Naive Bayes classifiers make rapid text predictions.'],
        'theory_sections': [   {   'title': 'Updating Beliefs with Evidence',
                                   'content_markdown': 'In life and machine learning, you start with a **prior '
                                                       'belief** before seeing any evidence.\n'
                                                       '\n'
                                                       '* *Prior*: Only 1% of emails in your inbox are malicious '
                                                       'phishing attacks.\n'
                                                       '* *New Evidence*: An incoming email contains the phrase '
                                                       "*'CLAIM YOUR $1,000,000 PRIZE IMMEDIATELY'*\n"
                                                       '* *Posterior (Updated Belief)*: Given this strong evidence, '
                                                       'the probability this email is phishing jumps from 1% to '
                                                       '99.8%!\n'
                                                       '\n'
                                                       "**Bayes' Theorem** gives the exact mathematical formula to "
                                                       'update our belief:\n'
                                                       '$$P(A|B) = \\frac{P(B|A) · P(A)}{P(B)}$$',
                                   'key_takeaway': "Bayes' Theorem tells us how to rationally update our predictions "
                                                   'as new clues arrive.'},
                               {   'title': "Why 'Naive' Bayes Is So Powerful",
                                   'content_markdown': 'Naive Bayes assumes all word clues are independent of each '
                                                       "other (e.g., seeing *'lottery'* and *'free'* are evaluated as "
                                                       'separate independent multipliers).\n'
                                                       '\n'
                                                       "Even though words aren't completely independent in real "
                                                       'grammar, this simplification runs in microseconds and remains '
                                                       'one of the fastest, most effective baseline classifiers in '
                                                       'data science.',
                                   'key_takeaway': 'Naive Bayes multiplies individual feature probabilities to '
                                                   'classify text with extreme speed.'}],
        'visual_explainer': {   'type': 'diagram',
                                'title': 'Bayesian Probability Tree',
                                'subtitle': 'Prior Probability -> Likelihood of Evidence -> Posterior Probability',
                                'diagram_type': 'bayesian_tree',
                                'parameters': {'prior_spam': 0.1, 'evidence_hit': 0.95}},
        'code_example': {   'title': "Calculating Posterior Probability with Bayes' Theorem",
                            'language': 'python',
                            'code': '# Scenario: Medical diagnostic test\n'
                                    '# Disease prevalence in population (Prior): 1%\n'
                                    'p_disease = 0.01\n'
                                    'p_healthy = 0.99\n'
                                    '\n'
                                    '# Test accuracy:\n'
                                    '# True Positive Rate (Sensitivity): Test is positive given patient HAS disease = '
                                    '99%\n'
                                    'p_pos_given_disease = 0.99\n'
                                    '# False Positive Rate: Test is positive given patient is HEALTHY = 5%\n'
                                    'p_pos_given_healthy = 0.05\n'
                                    '\n'
                                    '# Total probability of testing positive P(Pos)\n'
                                    'p_pos = (p_pos_given_disease * p_disease) + (p_pos_given_healthy * p_healthy)\n'
                                    '\n'
                                    '# Bayes Theorem: P(Disease | Positive Test Result)\n'
                                    'p_disease_given_pos = (p_pos_given_disease * p_disease) / p_pos\n'
                                    '\n'
                                    'print(f"Prior probability of disease:               {p_disease*100:.1f}%")\n'
                                    'print(f"Posterior probability after testing positive: '
                                    '{p_disease_given_pos*100:.1f}%")',
                            'explanation': 'Demonstrates why a positive test result on a rare condition results in '
                                           '~16.6% actual infection probability due to base rates.',
                            'output_preview': 'Prior probability of disease:               1.0%\n'
                                              'Posterior probability after testing positive: 16.6%'},
        'quiz_id': 'quiz-math-probability-bayes-theorem',
        'summary': "You mastered Bayes' Theorem and learned how machine learning updates predictions with incoming "
                   'evidence.',
        'next_lesson_slug': 'ml-linear-regression-ols',
        'prev_lesson_slug': 'math-chain-rule-backprop-math'},
    {   'slug': 'ml-linear-regression-ols',
        'course_slug': 'ml-fundamentals',
        'module_id': 'ml-mod-1',
        'title': 'Linear Regression: Finding the Best-Fit Line',
        'order': 1,
        'estimated_minutes': 25,
        'difficulty': 'Beginner',
        'skill_tag': 'regression',
        'learning_objectives': [   'Learn the linear prediction formula: Prediction = (Weight × Feature) + Bias.',
                                   'Understand Mean Squared Error (MSE) as the average squared mistake.',
                                   'Train a model by iteratively nudging weights to minimize error.'],
        'theory_sections': [   {   'title': 'The Core Linear Equation',
                                   'content_markdown': 'Linear regression is the simplest way to predict a number '
                                                       '(like price, temperature, or sales).\n'
                                                       '\n'
                                                       '$$y_{predicted} = (w · x) + b$$\n'
                                                       '\n'
                                                       '* $x$ = Input Feature (e.g. Square footage of a house)\n'
                                                       '* $w$ = Weight / Multiplier (e.g. Cost per square foot)\n'
                                                       '* $b$ = Bias / Starting Baseline (e.g. Base land cost)\n'
                                                       '* $y$ = Final Prediction (e.g. Estimated House Price)\n'
                                                       '\n'
                                                       '**Intuition**: The goal of training is simply finding the best '
                                                       '$w$ and $b$ so the line passes right through the middle of '
                                                       'your training data points.',
                                   'key_takeaway': 'Linear regression models relationships as straight lines by '
                                                   'adjusting slope weight (w) and baseline intercept (b).'},
                               {   'title': 'Measuring Mistakes: Mean Squared Error (MSE)',
                                   'content_markdown': 'To measure how well our line fits the data, we calculate the '
                                                       '**Mean Squared Error (MSE)**:\n'
                                                       '1. Find the gap (residual) between predicted value and true '
                                                       'value: $(\\hat{y} - y)$.\n'
                                                       "2. Square the gap so negative errors don't cancel positive "
                                                       'errors: $(\\hat{y} - y)^2$.\n'
                                                       '3. Take the average across all training data points:\n'
                                                       '\n'
                                                       '$$MSE = \\frac{1}{N} \\sum_{i=1}^N (y_{pred}^{(i)} - '
                                                       'y_{true}^{(i)})^2$$\n'
                                                       '\n'
                                                       'A lower MSE score means our line makes much more accurate '
                                                       'predictions.',
                                   'key_takeaway': 'Squaring errors heavily penalizes large mistakes, pushing the '
                                                   'model to fit all points evenly.'}],
        'visual_explainer': {   'type': 'simulation_preview',
                                'title': 'Linear Regression Best-Fit Line & Residuals',
                                'subtitle': 'Scatter plot with dynamic regression line minimizing sum of squared '
                                            'residuals',
                                'diagram_type': 'linear_regression',
                                'parameters': {'slope': 1.8, 'intercept': 2.4, 'mse': 0.042}},
        'code_example': {   'title': 'Training Linear Regression with Gradient Descent in NumPy',
                            'language': 'python',
                            'code': 'import numpy as np\n'
                                    '\n'
                                    '# Sample dataset: House size (X) and Price (y)\n'
                                    'np.random.seed(42)\n'
                                    'X = np.array([[1.0], [2.0], [3.0], [4.0]])\n'
                                    'y = np.array([[6.5], [9.0], [11.5], [14.0]])\n'
                                    '\n'
                                    '# Initialize starting parameters\n'
                                    'w = 0.0\n'
                                    'b = 0.0\n'
                                    'learning_rate = 0.05\n'
                                    'epochs = 100\n'
                                    'N = len(X)\n'
                                    '\n'
                                    'for epoch in range(epochs):\n'
                                    '    # 1. Make predictions\n'
                                    '    y_pred = w * X + b\n'
                                    '    # 2. Compute error gradients\n'
                                    '    dw = (2 / N) * np.sum((y_pred - y) * X)\n'
                                    '    db = (2 / N) * np.sum(y_pred - y)\n'
                                    '    # 3. Update parameters downhill\n'
                                    '    w -= learning_rate * dw\n'
                                    '    b -= learning_rate * db\n'
                                    '\n'
                                    'print(f"Learned Weight (w): {w:.2f} (Target: ~2.50)")\n'
                                    'print(f"Learned Bias (b):   {b:.2f} (Target: ~4.00)")',
                            'explanation': 'Illustrates the complete optimization loop of Gradient Descent tuning '
                                           'weight w and bias b to fit the points.',
                            'output_preview': 'Learned Weight (w): 2.47 (Target: ~2.50)\n'
                                              'Learned Bias (b):   4.08 (Target: ~4.00)'},
        'quiz_id': 'quiz-ml-linear-regression-ols',
        'summary': 'You learned how linear regression fits lines to data points and minimizes Mean Squared Error.',
        'next_lesson_slug': 'ml-gradient-descent-intuition',
        'prev_lesson_slug': 'math-probability-bayes-theorem'},
    {   'slug': 'ml-gradient-descent-intuition',
        'course_slug': 'ml-fundamentals',
        'module_id': 'ml-mod-1',
        'title': 'Gradient Descent: Walking Down Foggy Mountains to Zero Error',
        'order': 2,
        'estimated_minutes': 20,
        'difficulty': 'Beginner',
        'skill_tag': 'optimization',
        'learning_objectives': [   'Visualize the loss landscape as a hilly valley terrain where lowest altitude '
                                   'equals lowest error.',
                                   'Understand Learning Rate (alpha): Why too big overshoots and too small crawls.',
                                   'Compare Batch, Mini-Batch, and Stochastic Gradient Descent (SGD).'],
        'theory_sections': [   {   'title': 'The Blind Hiker in the Fog',
                                   'content_markdown': 'Imagine you are dropped on a foggy mountain peak and need to '
                                                       'find the lowest valley lake.\n'
                                                       "* You can't see the lake through the dense fog.\n"
                                                       '* But you can feel the slope of the ground right under your '
                                                       'boots!\n'
                                                       '* If the ground slopes downward to your left, you take a step '
                                                       'to your left.\n'
                                                       '\n'
                                                       '**That is Gradient Descent**: At every step, the algorithm '
                                                       'feels the slope of the loss function and takes a step in the '
                                                       'steepest downward direction.',
                                   'key_takeaway': 'Gradient Descent navigates complex loss surfaces by taking small '
                                                   'steps downhill at each iteration.'},
                               {   'title': 'The Importance of Learning Rate (α)',
                                   'content_markdown': 'The **Learning Rate** determines how big each step is:\n'
                                                       '* **Too Small ($\x07lpha = 0.00001$)**: The hiker takes '
                                                       'microscopic baby steps. Training takes hours or days to '
                                                       'converge.\n'
                                                       '* **Too Large ($\x07lpha = 5.0$)**: The hiker leaps so far '
                                                       'they bounce across mountain peaks, causing the loss to explode '
                                                       'to infinity (`NaN`)!\n'
                                                       '* **Just Right ($\x07lpha = 0.01$)**: Steady, fast progress '
                                                       'down to the valley floor.',
                                   'key_takeaway': 'Always tune the learning rate first when training machine learning '
                                                   'and deep learning models.'}],
        'visual_explainer': {   'type': 'chart',
                                'title': 'Learning Rate Convergence Comparison',
                                'subtitle': 'Small vs Ideal vs Overshooting Learning Rate curves',
                                'diagram_type': 'learning_rate_curves',
                                'parameters': {'lr_small': 0.001, 'lr_ideal': 0.05, 'lr_large': 1.2}},
        'code_example': {   'title': 'Comparing Learning Rates on a 1D Quadratic Loss',
                            'language': 'python',
                            'code': 'def run_gd(lr, steps=5):\n'
                                    '    w = 10.0  # Start far from optimum (w=0)\n'
                                    '    trajectory = [w]\n'
                                    '    for _ in range(steps):\n'
                                    '        grad = 2 * w  # Derivative of w^2\n'
                                    '        w = w - lr * grad\n'
                                    '        trajectory.append(round(w, 2))\n'
                                    '    return trajectory\n'
                                    '\n'
                                    'print("Ideal LR (0.1):      ", run_gd(0.1))\n'
                                    'print("Too Small LR (0.01): ", run_gd(0.01))\n'
                                    'print("Too Large LR (1.05): ", run_gd(1.05))',
                            'explanation': 'Demonstrates stable convergence vs slow crawl vs exploding divergence '
                                           'depending on step size.',
                            'output_preview': 'Ideal LR (0.1):       [10.0, 8.0, 6.4, 5.12, 4.1, 3.28]\n'
                                              'Too Small LR (0.01):  [10.0, 9.8, 9.6, 9.41, 9.22, 9.04]\n'
                                              'Too Large LR (1.05):  [10.0, -11.0, 12.1, -13.31, 14.64, -16.11]'},
        'quiz_id': 'quiz-ml-gradient-descent-intuition',
        'summary': 'You understood how gradient descent optimizes parameters and how learning rate controls '
                   'convergence speed.',
        'next_lesson_slug': 'ml-logistic-regression-classification',
        'prev_lesson_slug': 'ml-linear-regression-ols'},
    {   'slug': 'ml-logistic-regression-classification',
        'course_slug': 'ml-fundamentals',
        'module_id': 'ml-mod-2',
        'title': 'Logistic Regression: The S-Curve for Yes/No Decisions',
        'order': 3,
        'estimated_minutes': 25,
        'difficulty': 'Beginner',
        'skill_tag': 'classification',
        'learning_objectives': [   'Learn why standard linear lines fail at classifying Yes/No (0 or 1) binary '
                                   'outcomes.',
                                   'Understand the Sigmoid activation function: Squeezing any number into a 0% to 100% '
                                   'probability.',
                                   'Master Decision Boundaries: Choosing threshold cutoffs (e.g. p > 0.5 -> Class 1).'],
        'theory_sections': [   {   'title': "Why Can't We Use a Straight Line for Yes/No?",
                                   'content_markdown': 'If you try to fit a straight line to predict whether a tumor '
                                                       'is malignant ($1$) or benign ($0$), large tumor values will '
                                                       'produce predicted numbers like $2.5$ or $-1.2$!\n'
                                                       '\n'
                                                       'Probabilities must always stay strictly between **0.0 (0%) and '
                                                       '1.0 (100%)**.',
                                   'key_takeaway': "Straight lines don't work for binary classification because "
                                                   'predictions can exceed 0 and 1.'},
                               {   'title': 'The Sigmoid S-Curve',
                                   'content_markdown': 'To fix this, we pass the linear output through the **Sigmoid '
                                                       'function** $\\sigma(z)$:\n'
                                                       '\n'
                                                       '$$\\sigma(z) = \\frac{1}{1 + e^{-z}}$$\n'
                                                       '\n'
                                                       '* If $z = 0$, $\\sigma(0) = 0.5$ (50% toss-up)\n'
                                                       '* If $z = +10$, $\\sigma(10) \\approx 0.9999$ (99.99% Yes!)\n'
                                                       '* If $z = -10$, $\\sigma(-10) \\approx 0.0001$ (0.01% No!)\n'
                                                       '\n'
                                                       'It bends the straight line into a smooth **S-shaped curve** '
                                                       'that guarantees valid probabilities.',
                                   'key_takeaway': 'Sigmoid squashes any input number into a valid probability between '
                                                   '0 and 1.'}],
        'visual_explainer': {   'type': 'chart',
                                'title': 'Sigmoid Probability Curve & Decision Threshold',
                                'subtitle': 'Binary data points with S-curve transition at z = 0',
                                'diagram_type': 'sigmoid_curve',
                                'parameters': {'threshold': 0.5}},
        'code_example': {   'title': 'Classifying Pass/Fail Exam Results with Sigmoid',
                            'language': 'python',
                            'code': 'import numpy as np\n'
                                    '\n'
                                    'def sigmoid(z):\n'
                                    '    return 1.0 / (1.0 + np.exp(-z))\n'
                                    '\n'
                                    '# Trained weights for exam prediction\n'
                                    '# z = (0.8 * study_hours) - 4.0\n'
                                    'study_hours = np.array([1.0, 3.0, 5.0, 8.0, 10.0])\n'
                                    'z = 0.8 * study_hours - 4.0\n'
                                    'probabilities = sigmoid(z)\n'
                                    '\n'
                                    'for hours, prob in zip(study_hours, probabilities):\n'
                                    '    prediction = "PASS" if prob >= 0.5 else "FAIL"\n'
                                    '    print(f"Studied {hours:4.1f} hrs -> Pass Probability: {prob*100:5.1f}% -> '
                                    'Decision: {prediction}")',
                            'explanation': 'Calculates pass/fail probabilities using Sigmoid with a 0.5 decision '
                                           'threshold.',
                            'output_preview': 'Studied  1.0 hrs -> Pass Probability:   3.9% -> Decision: FAIL\n'
                                              'Studied  3.0 hrs -> Pass Probability:  16.8% -> Decision: FAIL\n'
                                              'Studied  5.0 hrs -> Pass Probability:  50.0% -> Decision: PASS\n'
                                              'Studied  8.0 hrs -> Pass Probability:  91.7% -> Decision: PASS\n'
                                              'Studied 10.0 hrs -> Pass Probability:  98.2% -> Decision: PASS'},
        'quiz_id': 'quiz-ml-logistic-regression-classification',
        'summary': 'You mastered Logistic Regression and learned how Sigmoid squashes numbers into Yes/No '
                   'probabilities.',
        'next_lesson_slug': 'ml-decision-trees-entropy',
        'prev_lesson_slug': 'ml-gradient-descent-intuition'},
    {   'slug': 'ml-decision-trees-entropy',
        'course_slug': 'ml-fundamentals',
        'module_id': 'ml-mod-2',
        'title': 'Decision Trees: Asking 20 Smart Questions with Entropy',
        'order': 4,
        'estimated_minutes': 20,
        'difficulty': 'Beginner',
        'skill_tag': 'decision_trees',
        'learning_objectives': [   'Understand Decision Trees as flowcharts of sequential Yes/No questions.',
                                   'Understand Entropy (measure of disorder/impurity) and Information Gain.',
                                   'Learn why Random Forests combine hundreds of trees to prevent overfitting.'],
        'theory_sections': [   {   'title': 'The 20 Questions Game',
                                   'content_markdown': "When you play the game *'20 Questions'*, you don't guess "
                                                       'random animals immediately. You ask broad questions that split '
                                                       'the possibilities in half:\n'
                                                       "1. *'Is it a mammal?'*\n"
                                                       "2. *'Does it live in water?'*\n"
                                                       '\n'
                                                       '**A Decision Tree builds this exact question flowchart '
                                                       'automatically from your data!** It evaluates every feature and '
                                                       'picks the split that separates the classes most cleanly.',
                                   'key_takeaway': 'Decision trees create intuitive flowchart rules that are easy for '
                                                   'humans to interpret.'},
                               {   'title': 'Measuring Chaos: Entropy & Information Gain',
                                   'content_markdown': '**Entropy** measures how mixed up a basket of data is:\n'
                                                       '* If a basket contains **10 Red apples and 0 Green apples**: '
                                                       'Entropy is **0.0 (Pure)**.\n'
                                                       '* If a basket contains **5 Red apples and 5 Green apples**: '
                                                       'Entropy is **1.0 (Maximum Chaos)**.\n'
                                                       '\n'
                                                       'At each branch, the tree chooses the question that produces '
                                                       'the biggest drop in entropy (**Information Gain**).',
                                   'key_takeaway': 'Trees pick splits that maximize purity (drop entropy to near '
                                                   'zero).'}],
        'visual_explainer': {   'type': 'diagram',
                                'title': 'Interactive Decision Tree Flowchart',
                                'subtitle': 'Root Node -> Branch Splitting -> Pure Leaf Predictions',
                                'diagram_type': 'decision_tree_hierarchy',
                                'parameters': {'depth': 3, 'features': ['Age > 30', 'Income > 50k']}},
        'code_example': {   'title': 'Calculating Shannon Entropy in Python',
                            'language': 'python',
                            'code': 'import numpy as np\n'
                                    '\n'
                                    'def calculate_entropy(labels):\n'
                                    '    """Calculates Shannon Entropy for a list of class labels."""\n'
                                    '    _, counts = np.unique(labels, return_counts=True)\n'
                                    '    probabilities = counts / len(labels)\n'
                                    '    # Entropy = - sum(p * log2(p))\n'
                                    '    return -np.sum([p * np.log2(p) for p in probabilities if p > 0])\n'
                                    '\n'
                                    "pure_set = ['Cat', 'Cat', 'Cat', 'Cat']\n"
                                    "mixed_set = ['Cat', 'Dog', 'Cat', 'Dog']\n"
                                    '\n'
                                    'print(f"Entropy of Pure Basket:  {calculate_entropy(pure_set):.4f} (Zero '
                                    'Chaos)")\n'
                                    'print(f"Entropy of 50/50 Basket: {calculate_entropy(mixed_set):.4f} (Maximum '
                                    'Uncertainty)")',
                            'explanation': 'Demonstrates entropy calculation showing 0 for perfectly pure sets and 1.0 '
                                           'for equally split sets.',
                            'output_preview': 'Entropy of Pure Basket:  0.0000 (Zero Chaos)\n'
                                              'Entropy of 50/50 Basket: 1.0000 (Maximum Uncertainty)'},
        'quiz_id': 'quiz-ml-decision-trees-entropy',
        'summary': 'You understood how decision trees split data using entropy and information gain.',
        'next_lesson_slug': 'ml-kmeans-clustering-algorithm',
        'prev_lesson_slug': 'ml-logistic-regression-classification'},
    {   'slug': 'ml-kmeans-clustering-algorithm',
        'course_slug': 'ml-fundamentals',
        'module_id': 'ml-mod-3',
        'title': 'K-Means Clustering: Finding Natural Groups in Unlabeled Data',
        'order': 5,
        'estimated_minutes': 20,
        'difficulty': 'Beginner',
        'skill_tag': 'clustering',
        'learning_objectives': [   'Understand Unsupervised Learning: Discovering patterns without teacher labels.',
                                   'Learn the 3-step K-Means dance: Assign points, recalculate centroids, repeat.',
                                   'Use the Elbow Method to choose the ideal number of clusters (K).'],
        'theory_sections': [   {   'title': 'Clustering: Grouping Without Labels',
                                   'content_markdown': 'In Supervised Learning, every training row has a teacher label '
                                                       "(e.g. *'Spam'* or *'Not Spam'*).\n"
                                                       '\n'
                                                       'In **Unsupervised Learning**, we have raw unlabeled data—like '
                                                       '100,000 customer shopping receipts. **K-Means clustering** '
                                                       'groups these customers into $K$ distinct personas (e.g. '
                                                       '*Budget Shoppers*, *Tech Enthusiasts*, *Weekend Bargain '
                                                       'Hunters*) based on distance similarity.',
                                   'key_takeaway': 'K-Means discovers natural groupings in raw data without needing '
                                                   'human labels.'},
                               {   'title': 'The K-Means Dance in 3 Steps',
                                   'content_markdown': '1. **Initialize**: Drop $K$ random pins (centroids) on the '
                                                       'scatter plot.\n'
                                                       '2. **Assign**: Each data point joins the closest pin.\n'
                                                       '3. **Update**: Move each pin to the exact center average of '
                                                       'its newly joined points.\n'
                                                       '\n'
                                                       'Repeat steps 2 and 3 until the pins stop moving!',
                                   'key_takeaway': 'K-Means converges rapidly by alternating between assigning points '
                                                   'and recentering centroids.'}],
        'visual_explainer': {   'type': 'simulation_preview',
                                'title': 'K-Means 2D Voronoi Clustering',
                                'subtitle': 'Data points colored by nearest moving centroid',
                                'diagram_type': 'kmeans_voronoi',
                                'parameters': {'k': 3, 'iterations': 8}},
        'code_example': {   'title': 'Simple 1D K-Means Clustering Implementation',
                            'language': 'python',
                            'code': 'import numpy as np\n'
                                    '\n'
                                    '# 1D Customer spending scores\n'
                                    'data = np.array([10, 12, 15, 80, 85, 90])\n'
                                    '\n'
                                    '# Initialize 2 cluster centroids\n'
                                    'c1, c2 = 10.0, 50.0\n'
                                    '\n'
                                    'for iteration in range(3):\n'
                                    '    # 1. Assign points to closest centroid\n'
                                    '    group1 = [x for x in data if abs(x - c1) <= abs(x - c2)]\n'
                                    '    group2 = [x for x in data if abs(x - c2) < abs(x - c1)]\n'
                                    '    \n'
                                    '    # 2. Recalculate centroids as mean of groups\n'
                                    '    c1 = np.mean(group1)\n'
                                    '    c2 = np.mean(group2)\n'
                                    '    print(f"Iter {iteration+1}: Centroid 1={c1:4.1f} (Group: {group1}), Centroid '
                                    '2={c2:4.1f} (Group: {group2})")',
                            'explanation': 'Illustrates the iterative assignment and recentering of cluster centers.',
                            'output_preview': 'Iter 1: Centroid 1=12.3 (Group: [10, 12, 15]), Centroid 2=85.0 (Group: '
                                              '[80, 85, 90])\n'
                                              'Iter 2: Centroid 1=12.3 (Group: [10, 12, 15]), Centroid 2=85.0 (Group: '
                                              '[80, 85, 90])\n'
                                              'Iter 3: Centroid 1=12.3 (Group: [10, 12, 15]), Centroid 2=85.0 (Group: '
                                              '[80, 85, 90])'},
        'quiz_id': 'quiz-ml-kmeans-clustering-algorithm',
        'summary': 'You understood unsupervised clustering and how K-Means finds clusters using distance minimization.',
        'next_lesson_slug': 'dl-perceptron-forward-prop',
        'prev_lesson_slug': 'ml-decision-trees-entropy'},
    {   'slug': 'dl-perceptron-forward-prop',
        'course_slug': 'deep-learning-fundamentals',
        'module_id': 'dl-mod-1',
        'title': 'Artificial Neurons, Layers & Forward Propagation',
        'order': 1,
        'estimated_minutes': 25,
        'difficulty': 'Intermediate',
        'skill_tag': 'neural_networks',
        'learning_objectives': [   'Learn how an artificial neuron combines inputs with weights and bias.',
                                   'Understand why non-linear activation functions (ReLU, Sigmoid) are essential.',
                                   'See how stacking layers allows networks to recognize complex shapes and patterns.'],
        'theory_sections': [   {   'title': 'How a Single Neuron Thinks',
                                   'content_markdown': 'An **artificial neuron** is inspired by biological brain '
                                                       'cells:\n'
                                                       '1. It takes in multiple input numbers ($x_1, x_2, \\dots$).\n'
                                                       '2. Multiplies each input by an importance weight ($w_1, w_2, '
                                                       '\\dots$).\n'
                                                       '3. Adds a base threshold bias ($b$).\n'
                                                       '4. Passes the result through an **activation function** '
                                                       '$\\sigma(z)$ to decide how strongly to fire:\n'
                                                       '\n'
                                                       '$$z = (w_1 x_1 + w_2 x_2 + ... + w_n x_n) + b$$\n'
                                                       '$$\\text{Output } a = \\sigma(z)$$',
                                   'key_takeaway': 'Each neuron acts as a specialized pattern detector.'},
                               {   'title': 'Why Do We Need Activation Functions?',
                                   'content_markdown': 'If we only did addition and multiplication, stacking 100 '
                                                       'neural layers would still just equal one giant straight line!\n'
                                                       '\n'
                                                       '**Activation functions (like ReLU or Sigmoid)** introduce '
                                                       'curves and bends. For example, **ReLU** (Rectified Linear '
                                                       'Unit) has a simple rule:\n'
                                                       '\n'
                                                       '$$\\text{ReLU}(z) = \\max(0, z)$$\n'
                                                       '\n'
                                                       'If input $z$ is negative, output `0`. If positive, output $z$. '
                                                       'This simple on/off switch enables deep networks to bend '
                                                       'decision boundaries around complex shapes like circles, faces, '
                                                       'and speech patterns.',
                                   'key_takeaway': 'Activation functions bend the math, allowing networks to learn '
                                                   'complex non-linear patterns.'}],
        'visual_explainer': {   'type': 'diagram',
                                'title': 'Multi-Layer Perceptron (MLP) Architecture',
                                'subtitle': 'Input Layer -> Hidden Dense Layer (ReLU) -> Output Layer (Softmax)',
                                'diagram_type': 'neural_net',
                                'parameters': {'layers': [3, 4, 2]}},
        'code_example': {   'title': 'Building a 2-Layer Neural Network Forward Pass in NumPy',
                            'language': 'python',
                            'code': 'import numpy as np\n'
                                    '\n'
                                    'def relu(z):\n'
                                    '    """Zero out negative values, keep positive values unchanged."""\n'
                                    '    return np.maximum(0, z)\n'
                                    '\n'
                                    '# 2 input samples with 3 features each\n'
                                    'X = np.array([\n'
                                    '    [1.0, 2.0, -1.0],\n'
                                    '    [0.5, -1.5, 2.0]\n'
                                    '])\n'
                                    '\n'
                                    '# Layer 1 weights: 3 inputs -> 4 hidden neurons\n'
                                    'np.random.seed(42)\n'
                                    'W1 = np.random.randn(3, 4) * 0.1\n'
                                    'b1 = np.zeros((1, 4))\n'
                                    '\n'
                                    '# Forward pass through Layer 1\n'
                                    'Z1 = np.dot(X, W1) + b1\n'
                                    'A1 = relu(Z1)  # Apply ReLU activation\n'
                                    '\n'
                                    'print("Input batch shape:", X.shape)\n'
                                    'print("Hidden layer activation shape:", A1.shape)\n'
                                    'print("Sample 0 activations:\\n", np.round(A1[0], 3))',
                            'explanation': 'Demonstrates matrix multiplication followed by non-linear ReLU activation '
                                           'for a hidden layer.',
                            'output_preview': 'Input batch shape: (2, 3)\n'
                                              'Hidden layer activation shape: (2, 4)\n'
                                              'Sample 0 activations:\n'
                                              ' [0.082 0.    0.145 0.   ]'},
        'quiz_id': 'quiz-dl-perceptron-forward-prop',
        'summary': 'You explored artificial neurons, why non-linear activations are necessary, and how layers pass '
                   'signals forward.',
        'next_lesson_slug': 'dl-activation-functions',
        'prev_lesson_slug': 'ml-kmeans-clustering-algorithm'},
    {   'slug': 'dl-activation-functions',
        'course_slug': 'deep-learning-fundamentals',
        'module_id': 'dl-mod-1',
        'title': 'Activation Functions Showdown: ReLU, Leaky ReLU, Sigmoid & Softmax',
        'order': 2,
        'estimated_minutes': 20,
        'difficulty': 'Intermediate',
        'skill_tag': 'neural_networks',
        'learning_objectives': [   'Understand why ReLU became the default activation choice for modern deep learning.',
                                   "Learn what the 'Dying ReLU' problem is and how Leaky ReLU fixes it.",
                                   'Use Softmax on the final output layer to produce multi-class probability '
                                   'distributions.'],
        'theory_sections': [   {   'title': 'Why Did ReLU Replace Sigmoid in Deep Networks?',
                                   'content_markdown': 'In early neural networks, researchers used Sigmoid for every '
                                                       'hidden layer. But Sigmoid flattens out near 0 and 1, where its '
                                                       'derivative becomes practically zero.\n'
                                                       '\n'
                                                       'In a 20-layer network, multiplying 20 tiny derivatives '
                                                       'together causes the gradient to shrink to `0.000000001` '
                                                       '(**Vanishing Gradient Problem**)—freezing learning in early '
                                                       'layers!\n'
                                                       '\n'
                                                       '**ReLU (Rectified Linear Unit)** fixed this: its slope is '
                                                       'always **1.0** for all positive numbers, allowing gradients to '
                                                       'flow effortlessly across hundreds of layers.',
                                   'key_takeaway': 'ReLU prevents vanishing gradients and computes 10x faster than '
                                                   'exponential activations.'},
                               {   'title': 'Softmax: Multi-Class Probabilities',
                                   'content_markdown': 'When classifying images into 3 or more categories (e.g. Dog, '
                                                       'Cat, Bird), the output layer uses **Softmax**:\n'
                                                       '\n'
                                                       '$$\\text{Softmax}(z_i) = \\frac{e^{z_i}}{\\sum_{j} e^{z_j}}$$\n'
                                                       '\n'
                                                       'It turns raw scores (logits) into clean probabilities that are '
                                                       'guaranteed to sum up to exactly **1.0 (100%)**.',
                                   'key_takeaway': 'Use ReLU for hidden layers and Softmax for the final multi-class '
                                                   'output layer.'}],
        'visual_explainer': {   'type': 'chart',
                                'title': 'Activation Function Comparison Curves',
                                'subtitle': 'ReLU vs Leaky ReLU vs Sigmoid vs Tanh',
                                'diagram_type': 'activation_curves',
                                'parameters': {'functions': ['ReLU', 'Sigmoid', 'Tanh', 'LeakyReLU']}},
        'code_example': {   'title': 'Comparing Activations and Computing Softmax Probabilities',
                            'language': 'python',
                            'code': 'import numpy as np\n'
                                    '\n'
                                    'def softmax(logits):\n'
                                    '    exp_vals = np.exp(logits - np.max(logits))  # subtract max for numerical '
                                    'stability\n'
                                    '    return exp_vals / np.sum(exp_vals)\n'
                                    '\n'
                                    '# Raw output logits from a network for [Cat, Dog, Bird]\n'
                                    'raw_logits = np.array([2.5, 1.0, 0.2])\n'
                                    'probabilities = softmax(raw_logits)\n'
                                    '\n'
                                    'print("Raw Model Logits:     ", raw_logits)\n'
                                    'print("Softmax Probabilities: ", np.round(probabilities, 3))\n'
                                    'print(f"Sum of Probabilities:  {np.sum(probabilities):.2f}")\n'
                                    'print(f"Winning Prediction:    Class {np.argmax(probabilities)} (Confidence: '
                                    '{np.max(probabilities)*100:.1f}%)")',
                            'explanation': 'Demonstrates converting unbounded network logits into normalized class '
                                           'probabilities.',
                            'output_preview': 'Raw Model Logits:      [2.5 1.  0.2]\n'
                                              'Softmax Probabilities:  [0.751 0.168 0.081]\n'
                                              'Sum of Probabilities:   1.00\n'
                                              'Winning Prediction:     Class 0 (Confidence: 75.1%)'},
        'quiz_id': 'quiz-dl-activation-functions',
        'summary': 'You compared major activation functions and learned why ReLU and Softmax are the modern industry '
                   'standards.',
        'next_lesson_slug': 'dl-backpropagation-calculus',
        'prev_lesson_slug': 'dl-perceptron-forward-prop'},
    {   'slug': 'dl-backpropagation-calculus',
        'course_slug': 'deep-learning-fundamentals',
        'module_id': 'dl-mod-2',
        'title': 'Backpropagation Demystified: How Neural Networks Learn from Mistakes',
        'order': 3,
        'estimated_minutes': 30,
        'difficulty': 'Intermediate',
        'skill_tag': 'backpropagation',
        'learning_objectives': [   'Understand the training feedback loop: Forward pass -> Loss calculation -> '
                                   'Backward pass -> Weight update.',
                                   'Learn how error signals are passed backwards through each neuron proportionally to '
                                   'its contribution.',
                                   'Build an intuitive mental model of automatic differentiation.'],
        'theory_sections': [   {   'title': 'Assigning Blame Backwards',
                                   'content_markdown': 'Imagine a restaurant with a Head Chef (output layer), Sous '
                                                       'Chefs (hidden layers), and Prep Cooks (input layer).\n'
                                                       '\n'
                                                       "If a customer sends soup back because it's way too salty (High "
                                                       'Loss), the Head Chef looks at the Sous Chef who seasoned it, '
                                                       'who in turn looks at the Prep Cook who measured the salt.\n'
                                                       '\n'
                                                       '**Backpropagation is this blame assignment process**: It '
                                                       'computes how much each neuron in every layer contributed to '
                                                       'the final mistake so each weight can be adjusted.',
                                   'key_takeaway': 'Backpropagation distributes credit and blame backwards through '
                                                   'every layer using the chain rule.'},
                               {   'title': 'The 4 Steps of Training',
                                   'content_markdown': '1. **Forward Pass**: Feed inputs through weights to make a '
                                                       'prediction $\\hat{y}$.\n'
                                                       '2. **Loss Computation**: Measure how wrong the prediction was '
                                                       '($Loss = (\\hat{y} - y)^2$).\n'
                                                       '3. **Backward Pass (Backprop)**: Compute $\\frac{\\partial '
                                                       'Loss}{\\partial W}$ for every weight using the chain rule.\n'
                                                       '4. **Optimizer Step**: Update weights downhill ($W \\leftarrow '
                                                       'W - \\alpha \\cdot \\nabla W$).',
                                   'key_takeaway': 'Repeating this 4-step loop thousands of times turns a random '
                                                   'network into an intelligent classifier.'}],
        'visual_explainer': {   'type': 'diagram',
                                'title': 'Backpropagation Gradient Flow',
                                'subtitle': 'Error delta propagating backwards across dense layers',
                                'diagram_type': 'backprop_graph'},
        'code_example': {   'title': 'Complete 1-Neuron Backpropagation from Scratch in Python',
                            'language': 'python',
                            'code': 'import numpy as np\n'
                                    '\n'
                                    '# Single training sample: Input x=2.0, True Target y=10.0\n'
                                    'x = 2.0\n'
                                    'target = 10.0\n'
                                    '\n'
                                    '# Starting weight & bias\n'
                                    'w = 1.0\n'
                                    'b = 0.0\n'
                                    'lr = 0.1\n'
                                    '\n'
                                    'print(f"Initial: w={w:.2f}, b={b:.2f}")\n'
                                    'for step in range(4):\n'
                                    '    # 1. Forward Pass\n'
                                    '    y_pred = w * x + b\n'
                                    '    loss = (y_pred - target) ** 2\n'
                                    '    \n'
                                    '    # 2. Backward Pass (Chain Rule)\n'
                                    '    dloss_dpred = 2 * (y_pred - target)  # dLoss/dY_hat\n'
                                    '    dpred_dw = x                         # dY_hat/dw\n'
                                    '    dpred_db = 1.0                       # dY_hat/db\n'
                                    '    \n'
                                    '    dw = dloss_dpred * dpred_dw\n'
                                    '    db = dloss_dpred * dpred_db\n'
                                    '    \n'
                                    '    # 3. Update\n'
                                    '    w -= lr * dw\n'
                                    '    b -= lr * db\n'
                                    '    print(f"Step {step+1}: Loss={loss:6.2f} -> New w={w:.2f}, New b={b:.2f}")',
                            'explanation': 'Demonstrates forward pass, chain rule derivative calculation, and gradient '
                                           'descent update step.',
                            'output_preview': 'Initial: w=1.00, b=0.00\n'
                                              'Step 1: Loss= 64.00 -> New w=4.20, New b=1.60\n'
                                              'Step 2: Loss=  0.00 -> New w=4.20, New b=1.60\n'
                                              'Step 3: Loss=  0.00 -> New w=4.20, New b=1.60\n'
                                              'Step 4: Loss=  0.00 -> New w=4.20, New b=1.60'},
        'quiz_id': 'quiz-dl-backpropagation-calculus',
        'summary': 'You understood the full Backpropagation loop and how error gradients adjust network weights.',
        'next_lesson_slug': 'dl-cnn-convolution-pooling',
        'prev_lesson_slug': 'dl-activation-functions'},
    {   'slug': 'dl-cnn-convolution-pooling',
        'course_slug': 'deep-learning-fundamentals',
        'module_id': 'dl-mod-3',
        'title': "Convolutional Neural Networks (CNNs): How Computers 'See' Images",
        'order': 4,
        'estimated_minutes': 25,
        'difficulty': 'Intermediate',
        'skill_tag': 'computer_vision',
        'learning_objectives': [   'Understand why standard dense networks fail on large images (parameter explosion '
                                   'and losing spatial relations).',
                                   'Learn how sliding 2D convolution filters detect edges, textures, and object parts.',
                                   'Understand Max Pooling for spatial downsampling and translation invariance.'],
        'theory_sections': [   {   'title': 'The Flashlight Analogy (Convolution Filter)',
                                   'content_markdown': 'Imagine holding a small 3x3 square flashlight over a dark '
                                                       'photograph.\n'
                                                       '* You slide the flashlight across the picture row by row.\n'
                                                       '* If the 3x3 patch under your flashlight matches an edge '
                                                       'pattern, the flashlight glows brightly (high activation).\n'
                                                       "* If it's blank wall, the flashlight stays dim.\n"
                                                       '\n'
                                                       '**A Convolutional Filter (Kernel)** is this 3x3 pattern '
                                                       'detector! Early layers detect simple lines and curves, middle '
                                                       'layers detect eyes and wheels, and deep layers recognize whole '
                                                       'faces and cars.',
                                   'key_takeaway': 'Convolution filters slide across images to extract visual features '
                                                   'regardless of where they appear.'},
                               {   'title': 'Max Pooling: Compressing Without Losing Key Details',
                                   'content_markdown': '**Max Pooling** looks at each 2x2 patch of a feature map and '
                                                       'keeps only the **maximum number**.\n'
                                                       '\n'
                                                       'This cuts image dimensions in half (reducing memory by 75%) '
                                                       'while preserving the strongest detected features, making the '
                                                       'network invariant to small shifts or rotations.',
                                   'key_takeaway': 'Max Pooling downsamples feature maps to reduce computation and '
                                                   'improve generalization.'}],
        'visual_explainer': {   'type': 'simulation_preview',
                                'title': '2D Convolution Kernel Sliding & Feature Map',
                                'subtitle': '3x3 filter scanning a 5x5 input matrix to produce a feature map',
                                'diagram_type': 'cnn_kernel_stride',
                                'parameters': {'kernel_size': 3, 'stride': 1, 'padding': 0}},
        'code_example': {   'title': 'Applying a Vertical Edge Detection Filter in NumPy',
                            'language': 'python',
                            'code': 'import numpy as np\n'
                                    '\n'
                                    '# 4x4 grayscale image with a vertical bright stripe down the middle\n'
                                    'image = np.array([\n'
                                    '    [0, 10, 10, 0],\n'
                                    '    [0, 10, 10, 0],\n'
                                    '    [0, 10, 10, 0],\n'
                                    '    [0, 10, 10, 0]\n'
                                    '])\n'
                                    '\n'
                                    '# 3x3 Sobel vertical edge detection filter\n'
                                    'kernel = np.array([\n'
                                    '    [-1, 0, 1],\n'
                                    '    [-2, 0, 2],\n'
                                    '    [-1, 0, 1]\n'
                                    '])\n'
                                    '\n'
                                    '# Manual 2D convolution over the top-left 3x3 patch\n'
                                    'patch = image[0:3, 0:3]\n'
                                    'edge_score = np.sum(patch * kernel)\n'
                                    '\n'
                                    'print("Image 3x3 Patch:\\n", patch)\n'
                                    'print("Filter Kernel:\\n", kernel)\n'
                                    'print(f"Convolution Result for patch: {edge_score} (Strong Edge Detected!)")',
                            'explanation': 'Demonstrates how multiplying an image patch with a filter matrix detects '
                                           'the presence of vertical edges.',
                            'output_preview': 'Image 3x3 Patch:\n'
                                              ' [[ 0 10 10]\n'
                                              '  [ 0 10 10]\n'
                                              '  [ 0 10 10]]\n'
                                              'Filter Kernel:\n'
                                              ' [[-1  0  1]\n'
                                              '  [-2  0  2]\n'
                                              '  [-1  0  1]]\n'
                                              'Convolution Result for patch: 40 (Strong Edge Detected!)'},
        'quiz_id': 'quiz-dl-cnn-convolution-pooling',
        'summary': 'You understood convolutional filters, feature map hierarchies, and max pooling in Computer Vision.',
        'next_lesson_slug': 'genai-tokenization-embeddings',
        'prev_lesson_slug': 'dl-backpropagation-calculus'},
    {   'slug': 'genai-tokenization-embeddings',
        'course_slug': 'generative-ai-fundamentals',
        'module_id': 'genai-mod-1',
        'title': 'Words as Coordinates: Tokenization & Embedding Spaces',
        'order': 1,
        'estimated_minutes': 25,
        'difficulty': 'Intermediate',
        'skill_tag': 'nlp_embeddings',
        'learning_objectives': [   'Learn how Byte-Pair Encoding (BPE) tokenizers break text into subword chunks.',
                                   'Understand Embedding Spaces: Mapping words into multidimensional coordinate maps.',
                                   'Explore Word Vector Math: King - Man + Woman = Queen.'],
        'theory_sections': [   {   'title': 'How AI Reads: Tokenization',
                                   'content_markdown': "Computers don't read words or letters directly. A "
                                                       '**tokenizer** chops sentences into subword tokens and assigns '
                                                       'each one a unique integer ID.\n'
                                                       '\n'
                                                       "* *'unbelievable'* $\\rightarrow$ `['un', 'believ', 'able']` "
                                                       '$\\rightarrow$ `[428, 19203, 502]`\n'
                                                       '\n'
                                                       'Subword tokenization allows modern LLMs to handle rare words, '
                                                       'typos, code, and emojis without needing an infinite '
                                                       'dictionary.',
                                   'key_takeaway': 'Tokenizers turn raw text into lists of integer IDs.'},
                               {   'title': 'Embedding Space: The Mental Map of Words',
                                   'content_markdown': 'An **Embedding** replaces each integer ID with a rich vector '
                                                       'of numbers (e.g. 1,536 coordinates in GPT-4).\n'
                                                       '\n'
                                                       'In this space, words with similar meanings live close '
                                                       'together:\n'
                                                       "* *'puppy'* and *'dog'* have almost identical coordinates.\n"
                                                       '* Directions in space capture semantic concepts (e.g. Capital '
                                                       'city, Gender, Verb tense).\n'
                                                       '\n'
                                                       '$$\\vec{v}_{\\text{King}} - \\vec{v}_{\\text{Man}} + '
                                                       '\\vec{v}_{\\text{Woman}} \\approx \\vec{v}_{\\text{Queen}}$$',
                                   'key_takeaway': 'Embeddings convert discrete words into smooth geometric '
                                                   'coordinates where distance measures meaning.'}],
        'visual_explainer': {   'type': 'chart',
                                'title': '2D Semantic Word Embedding Space',
                                'subtitle': 'Word vectors clustered by category (Animals, Royalty, Tech)',
                                'diagram_type': 'embedding_scatter',
                                'parameters': {'clusters': ['Animals', 'Royalty', 'Countries']}},
        'code_example': {   'title': 'Semantic Vector Arithmetic in Python',
                            'language': 'python',
                            'code': 'import numpy as np\n'
                                    '\n'
                                    '# Simulated 3D embeddings: [Royalty, Gender (M=+1, F=-1), Power]\n'
                                    'king   = np.array([0.9,  0.8, 0.9])\n'
                                    'man    = np.array([0.1,  0.9, 0.2])\n'
                                    'woman  = np.array([0.1, -0.9, 0.2])\n'
                                    'queen  = np.array([0.9, -0.8, 0.9])\n'
                                    'apple  = np.array([0.0,  0.0, -0.9])\n'
                                    '\n'
                                    '# Word Math: King - Man + Woman\n'
                                    'result_vector = king - man + woman\n'
                                    '\n'
                                    'def similarity(a, b):\n'
                                    '    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))\n'
                                    '\n'
                                    'print("Similarity to Queen:", round(similarity(result_vector, queen), 4))\n'
                                    'print("Similarity to Apple:", round(similarity(result_vector, apple), 4))',
                            'explanation': 'Demonstrates how vector addition and subtraction preserves semantic '
                                           'relationships.',
                            'output_preview': 'Similarity to Queen: 0.9945 (Near Perfect Match!)\n'
                                              'Similarity to Apple: -0.6015 (Unrelated)'},
        'quiz_id': 'quiz-genai-tokenization-embeddings',
        'summary': 'You explored subword tokenization and learned how embedding spaces capture word meanings '
                   'geometrically.',
        'next_lesson_slug': 'genai-self-attention-transformers',
        'prev_lesson_slug': 'dl-cnn-convolution-pooling'},
    {   'slug': 'genai-self-attention-transformers',
        'course_slug': 'generative-ai-fundamentals',
        'module_id': 'genai-mod-2',
        'title': 'The Self-Attention Mechanism Behind ChatGPT',
        'order': 2,
        'estimated_minutes': 30,
        'difficulty': 'Advanced',
        'skill_tag': 'transformers',
        'learning_objectives': [   'Learn how Self-Attention allows words to look at surrounding words for context.',
                                   'Understand Query ($Q$), Key ($K$), and Value ($V$) with the filing cabinet '
                                   'analogy.',
                                   'Understand the Attention formula: Softmax(QKᵀ / √d_k) · V.'],
        'theory_sections': [   {   'title': 'Why Does Attention Matter?',
                                   'content_markdown': 'In human language, the meaning of a word depends entirely on '
                                                       'the words around it.\n'
                                                       '\n'
                                                       'Consider the sentence:\n'
                                                       "> *'The bank on the river was muddy.'* vs *'The bank approved "
                                                       "my loan.'*\n"
                                                       '\n'
                                                       "Without attention, the word *'bank'* would have the exact same "
                                                       'representation. **Self-Attention acts like a dynamic mental '
                                                       "spotlight** that connects *'bank'* to *'river'* in the first "
                                                       "sentence and *'bank'* to *'loan'* in the second sentence!",
                                   'key_takeaway': 'Self-attention lets words update their meaning based on all other '
                                                   'words in the sentence simultaneously.'},
                               {   'title': 'The Query, Key, and Value Analogy',
                                   'content_markdown': 'To compute attention, every word is projected into 3 vectors, '
                                                       'just like searching a library or YouTube:\n'
                                                       "1. **Query ($Q$)**: *What am I searching for?* (e.g. *'Who "
                                                       'does pronoun "it" refer to?\'*)\n'
                                                       '2. **Key ($K$)**: *The title tag / label on each file in the '
                                                       "library.* (e.g. *'animal'*, *'street'*)\n"
                                                       '3. **Value ($V$)**: *The actual content inside the matched '
                                                       'file.*\n'
                                                       '\n'
                                                       '$$\\text{Attention}(Q, K, V) = \\text{Softmax}\\left( \\frac{Q '
                                                       '· K^T}{\\sqrt{d_k}} \\right) · V$$\n'
                                                       '\n'
                                                       '1. Multiply $Q$ and $K^T$ to score how relevant each word is '
                                                       'to every other word.\n'
                                                       '2. Divide by $\\sqrt{d_k}$ to prevent numbers from blowing '
                                                       'up.\n'
                                                       '3. Pass scores through `Softmax` so all attention weights sum '
                                                       'up to 100% (`1.0`).\n'
                                                       '4. Multiply by $V$ to get the final context-aware word '
                                                       'representation.',
                                   'key_takeaway': 'The Attention equation simply calculates a weighted average of '
                                                   'word contents based on relevance scores.'}],
        'visual_explainer': {   'type': 'diagram',
                                'title': 'Scaled Dot-Product Attention Flow',
                                'subtitle': 'Q * K^T -> Scale -> Softmax -> Weight Values (V)',
                                'diagram_type': 'attention_matrix'},
        'code_example': {   'title': 'Computing Self-Attention in Pure NumPy',
                            'language': 'python',
                            'code': 'import numpy as np\n'
                                    '\n'
                                    'def softmax(x):\n'
                                    '    e_x = np.exp(x - np.max(x, axis=-1, keepdims=True))\n'
                                    '    return e_x / np.sum(e_x, axis=-1, keepdims=True)\n'
                                    '\n'
                                    'def self_attention(Q, K, V):\n'
                                    '    d_k = Q.shape[-1]\n'
                                    '    # 1. Similarity scores between queries and keys\n'
                                    '    scores = np.matmul(Q, K.T) / np.sqrt(d_k)\n'
                                    '    # 2. Convert to probabilities summing to 1.0\n'
                                    '    weights = softmax(scores)\n'
                                    '    # 3. Weighted blend of values\n'
                                    '    output = np.matmul(weights, V)\n'
                                    '    return output, weights\n'
                                    '\n'
                                    "# 3 Tokens: ['AI', 'is', 'awesome'], feature dim = 4\n"
                                    'np.random.seed(42)\n'
                                    'Q = np.random.randn(3, 4)\n'
                                    'K = np.random.randn(3, 4)\n'
                                    'V = np.random.randn(3, 4)\n'
                                    '\n'
                                    'context_output, attention_matrix = self_attention(Q, K, V)\n'
                                    'print("Attention Weights Matrix (3x3):\\n", np.round(attention_matrix, 3))\n'
                                    'print("Row 0 attention sum check:", np.sum(attention_matrix[0]))',
                            'explanation': 'Computes attention scores and verifies that every row of the attention '
                                           'matrix sums to 1.0 (100% attention distribution).',
                            'output_preview': 'Attention Weights Matrix (3x3):\n'
                                              ' [[0.219 0.443 0.338]\n'
                                              '  [0.495 0.384 0.121]\n'
                                              '  [0.428 0.301 0.271]]\n'
                                              'Row 0 attention sum check: 1.0'},
        'quiz_id': 'quiz-genai-self-attention-transformers',
        'summary': 'You mastered Query/Key/Value dynamics, attention matrix weighting, and how Transformers '
                   'contextualize language.',
        'next_lesson_slug': 'genai-rag-architecture-pipeline',
        'prev_lesson_slug': 'genai-tokenization-embeddings'},
    {   'slug': 'genai-rag-architecture-pipeline',
        'course_slug': 'generative-ai-fundamentals',
        'module_id': 'genai-mod-3',
        'title': 'RAG (Retrieval-Augmented Generation): Giving LLMs Real-Time Memory',
        'order': 3,
        'estimated_minutes': 25,
        'difficulty': 'Advanced',
        'skill_tag': 'rag_systems',
        'learning_objectives': [   'Understand the limitations of raw LLMs (knowledge cutoffs, hallucinations, private '
                                   'company data).',
                                   'Learn the complete RAG pipeline: Chunking -> Embedding -> Vector DB -> Prompt '
                                   'Injection -> LLM Answer.',
                                   'Explore semantic similarity search using cosine distance in Vector Databases.'],
        'theory_sections': [   {   'title': 'Why Foundation Models Need RAG',
                                   'content_markdown': 'Even the largest LLM suffers from two major problems:\n'
                                                       "1. **Knowledge Cutoff**: It doesn't know what happened "
                                                       'yesterday.\n'
                                                       "2. **Private Data**: It has never seen your company's internal "
                                                       'PDFs, HR manuals, or private codebases.\n'
                                                       '\n'
                                                       'Instead of retraining a $10M model, **RAG (Retrieval-Augmented '
                                                       'Generation)** acts like an **open-book exam**: When a user '
                                                       'asks a question, the system searches your private documents '
                                                       'for relevant snippets and pastes them directly into the '
                                                       'prompt!',
                                   'key_takeaway': "RAG eliminates hallucinations by grounding the LLM's response in "
                                                   'verified document chunks.'},
                               {   'title': 'The 5-Step RAG Pipeline',
                                   'content_markdown': '1. **Chunk**: Split long PDF documents into 500-word '
                                                       'paragraphs.\n'
                                                       '2. **Embed**: Convert each chunk into an embedding vector '
                                                       'using an embedding model.\n'
                                                       '3. **Index**: Store all chunk vectors in a **Vector Database** '
                                                       '(e.g. Chroma, Pinecone).\n'
                                                       '4. **Retrieve**: When the user asks a question, embed their '
                                                       'question and retrieve the Top-3 most similar chunks.\n'
                                                       "5. **Generate**: Ask the LLM: *'Answer the question based ONLY "
                                                       "on these 3 retrieved excerpts.'*",
                                   'key_takeaway': 'Vector search retrieves relevant knowledge in milliseconds, which '
                                                   'is then synthesized by the LLM.'}],
        'visual_explainer': {   'type': 'architecture_flow',
                                'title': 'End-to-End RAG Architecture',
                                'subtitle': 'User Query -> Vector Embed -> Vector DB Retrieval -> Prompt Context -> '
                                            'LLM Response',
                                'diagram_type': 'rag_pipeline'},
        'code_example': {   'title': 'Building an In-Memory Mini RAG System in Python',
                            'language': 'python',
                            'code': 'import numpy as np\n'
                                    '\n'
                                    '# Simulated knowledge base documents\n'
                                    'documents = [\n'
                                    '    "Antigravity IDE includes built-in terminal, Monaco editor, and AI tutor.",\n'
                                    '    "The refund policy allows returns within 30 days of purchase.",\n'
                                    '    "Python 3.13 introduces experimental free-threaded execution without the '
                                    'GIL."\n'
                                    ']\n'
                                    '\n'
                                    '# Simplified 3D embedding vectors for each doc\n'
                                    '# Coordinates: [Software/IDE, Company Policy, Python Internals]\n'
                                    'doc_embeddings = np.array([\n'
                                    '    [0.9, 0.1, 0.2],\n'
                                    '    [0.1, 0.9, 0.0],\n'
                                    '    [0.2, 0.0, 0.9]\n'
                                    '])\n'
                                    '\n'
                                    "# User query: 'How do I get my money back?'\n"
                                    'query_embedding = np.array([0.05, 0.95, 0.0])\n'
                                    '\n'
                                    '# Calculate similarity to all documents\n'
                                    'similarities = [np.dot(query_embedding, doc) for doc in doc_embeddings]\n'
                                    'best_idx = int(np.argmax(similarities))\n'
                                    '\n'
                                    'print(f"User Query: \'How do I get my money back?\'")\n'
                                    'print(f"Retrieved Document: \\"{documents[best_idx]}\\"")\n'
                                    'print(f"Similarity Score:   {similarities[best_idx]:.4f}")',
                            'explanation': 'Illustrates how vector cosine matching selects the most relevant document '
                                           'chunk to inject into the LLM prompt.',
                            'output_preview': "User Query: 'How do I get my money back?'\n"
                                              'Retrieved Document: "The refund policy allows returns within 30 days of '
                                              'purchase."\n'
                                              'Similarity Score:   0.8600'},
        'quiz_id': 'quiz-genai-rag-architecture-pipeline',
        'summary': 'You understood how RAG systems combine vector similarity search with LLM reasoning to answer '
                   'questions accurately.',
        'next_lesson_slug': 'prompt-foundations-few-shot',
        'prev_lesson_slug': 'genai-self-attention-transformers'},
    {   'slug': 'prompt-foundations-few-shot',
        'course_slug': 'prompt-engineering-agents',
        'module_id': 'agent-mod-1',
        'title': 'Prompt Engineering Mastery: Few-Shot, System Prompts & Delimiters',
        'order': 1,
        'estimated_minutes': 20,
        'difficulty': 'Beginner',
        'skill_tag': 'prompt_engineering',
        'learning_objectives': [   'Learn how System Prompts establish persistent role, tone, and guardrails for LLMs.',
                                   'Use clear delimiters (###, XML tags, ```) to prevent prompt injection and '
                                   'ambiguity.',
                                   'Apply Few-Shot Prompting: Providing 2-3 input/output examples to guarantee '
                                   'formatted responses.'],
        'theory_sections': [   {   'title': 'Directing the Model: Roles & Delimiters',
                                   'content_markdown': 'Large Language Models are probabilistic text prediction '
                                                       'engines. If your instructions are vague, the model guesses '
                                                       'what you want.\n'
                                                       '\n'
                                                       '**Three Essential Prompt Engineering Rules**:\n'
                                                       "1. **Assign a Persona**: *'You are a senior compiler engineer "
                                                       "explaining concepts to a college sophomore.'*\n"
                                                       '2. **Use Clear Delimiters**: Enclose user text in `"""` or '
                                                       '`<user_input>` so the model never confuses instructions with '
                                                       'data.\n'
                                                       '3. **Specify the Output Format**: Explicitly demand JSON, '
                                                       'Markdown tables, or bullet lists.',
                                   'key_takeaway': 'Clear delimiters and explicit personas dramatically reduce '
                                                   'formatting errors.'},
                               {   'title': 'Zero-Shot vs Few-Shot Prompting',
                                   'content_markdown': '* **Zero-Shot**: Asking the model to perform a task with zero '
                                                       "examples (*'Classify this sentiment'*).\n"
                                                       '* **Few-Shot**: Giving the model 2 or 3 completed examples '
                                                       'before the test input.\n'
                                                       '\n'
                                                       'Providing just 2 high-quality examples increases '
                                                       'classification accuracy on difficult domain-specific tasks '
                                                       'from ~65% to over **95%**.',
                                   'key_takeaway': 'Few-shot examples teach the model your exact expected format and '
                                                   'reasoning style.'}],
        'visual_explainer': {   'type': 'diagram',
                                'title': 'Few-Shot Prompt Structure',
                                'subtitle': 'System Prompt -> Example 1 (Input/Output) -> Example 2 (Input/Output) -> '
                                            'Target Query',
                                'diagram_type': 'prompt_anatomy'},
        'code_example': {   'title': 'Structuring a Robust Few-Shot Prompt in Python',
                            'language': 'python',
                            'code': 'def build_sentiment_prompt(user_review: str) -> str:\n'
                                    '    return f"""You are an automated customer feedback sentiment extractor.\n'
                                    "Output ONLY valid JSON with keys: 'sentiment' (POSITIVE/NEGATIVE/NEUTRAL) and "
                                    "'confidence' (0.0 - 1.0).\n"
                                    '\n'
                                    '### Examples:\n'
                                    "Review: 'The delivery arrived 3 days early and worked flawlessly!'\n"
                                    '{{"sentiment": "POSITIVE", "confidence": 0.98}}\n'
                                    '\n'
                                    "Review: 'It broke after 10 minutes of use. Very disappointed.'\n"
                                    '{{"sentiment": "NEGATIVE", "confidence": 0.95}}\n'
                                    '\n'
                                    '### New Task:\n'
                                    "Review: '{user_review}'\n"
                                    '"""\n'
                                    '\n'
                                    'test_review = "Great sound quality but battery life could be a little better."\n'
                                    'print(build_sentiment_prompt(test_review))',
                            'explanation': 'Demonstrates clear formatting, system instructions, few-shot examples, and '
                                           'strict JSON output schemas.',
                            'output_preview': 'You are an automated customer feedback sentiment extractor.\n'
                                              "Output ONLY valid JSON with keys: 'sentiment' "
                                              "(POSITIVE/NEGATIVE/NEUTRAL) and 'confidence' (0.0 - 1.0).\n"
                                              '\n'
                                              '### Examples:\n'
                                              "Review: 'The delivery arrived 3 days early and worked flawlessly!'\n"
                                              '{"sentiment": "POSITIVE", "confidence": 0.98}\n'
                                              '\n'
                                              "Review: 'It broke after 10 minutes of use. Very disappointed.'\n"
                                              '{"sentiment": "NEGATIVE", "confidence": 0.95}\n'
                                              '\n'
                                              '### New Task:\n'
                                              "Review: 'Great sound quality but battery life could be a little "
                                              "better.'"},
        'quiz_id': 'quiz-prompt-foundations-few-shot',
        'summary': 'You mastered system prompts, delimiters, and few-shot examples to reliably control AI output.',
        'next_lesson_slug': 'prompt-chain-of-thought-reasoning',
        'prev_lesson_slug': 'genai-rag-architecture-pipeline'},
    {   'slug': 'prompt-chain-of-thought-reasoning',
        'course_slug': 'prompt-engineering-agents',
        'module_id': 'agent-mod-2',
        'title': 'Chain-of-Thought & Step-by-Step Reasoning',
        'order': 2,
        'estimated_minutes': 20,
        'difficulty': 'Beginner',
        'skill_tag': 'prompt_engineering',
        'learning_objectives': [   "Learn why forcing LLMs to 'Think step-by-step' prevents mathematical and logical "
                                   'hallucinations.',
                                   'Understand Chain-of-Thought (CoT) prompting mechanics.',
                                   'Explore Self-Consistency: Generating multiple reasoning paths and taking the '
                                   'majority vote.'],
        'theory_sections': [   {   'title': 'Why AI Fails at Immediate Answers',
                                   'content_markdown': 'If you ask an LLM a complex riddle or word problem and demand '
                                                       'an immediate 1-word answer, it often guesses incorrectly '
                                                       'because it only generates one token at a time without '
                                                       "'planning'.\n"
                                                       '\n'
                                                       "When you instruct the model: **'Think step-by-step before "
                                                       "stating your final answer'**, you give the model **working "
                                                       'memory scratchpad space** (intermediate tokens) to work '
                                                       'through math calculations and check logic.',
                                   'key_takeaway': 'Encouraging step-by-step reasoning provides token scratchpad space '
                                                   'that drastically improves accuracy on logic and math.'},
                               {   'title': 'Self-Consistency (Majority Voting)',
                                   'content_markdown': 'For mission-critical answers, we run the reasoning prompt 5 '
                                                       'times at temperature `0.7` and take the **majority vote** '
                                                       'among the final answers.\n'
                                                       '\n'
                                                       'If 4 out of 5 reasoning paths arrive at `$42.50`, we can be '
                                                       'highly confident in the result.',
                                   'key_takeaway': 'Self-consistency uses multiple reasoning passes to filter out '
                                                   'random hallucinations.'}],
        'visual_explainer': {   'type': 'diagram',
                                'title': 'Chain of Thought Reasoning Tree',
                                'subtitle': 'Prompt -> Step 1 Deduction -> Step 2 Math Check -> Final Answer',
                                'diagram_type': 'chain_of_thought'},
        'code_example': {   'title': 'Chain-of-Thought Reasoning Template',
                            'language': 'python',
                            'code': 'problem = """\n'
                                    'A bakery sells cupcakes for $3 each and cookies for $2 each.\n'
                                    'Sarah bought 4 cupcakes and 6 cookies, and paid with a $50 bill.\n'
                                    'How much change does she receive?\n'
                                    '"""\n'
                                    '\n'
                                    'cot_prompt = f"""Solve the following math problem step-by-step.\n'
                                    'First write out your deductions inside <thinking> tags.\n'
                                    'Then provide the final dollar amount inside <answer> tags.\n'
                                    '\n'
                                    'Problem:\n'
                                    '{problem}\n'
                                    '"""\n'
                                    '\n'
                                    'print(cot_prompt)',
                            'explanation': 'Illustrates how structured thinking tags encourage reasoning transparency '
                                           'and accurate final deductions.',
                            'output_preview': 'Solve the following math problem step-by-step.\n'
                                              'First write out your deductions inside <thinking> tags.\n'
                                              'Then provide the final dollar amount inside <answer> tags.\n'
                                              '\n'
                                              'Problem:\n'
                                              'A bakery sells cupcakes for $3 each and cookies for $2 each.\n'
                                              'Sarah bought 4 cupcakes and 6 cookies, and paid with a $50 bill.\n'
                                              'How much change does she receive?'},
        'quiz_id': 'quiz-prompt-chain-of-thought-reasoning',
        'summary': 'You understood Chain-of-Thought prompting and why step-by-step scratchpad tokens resolve complex '
                   'reasoning tasks.',
        'next_lesson_slug': 'prompt-ai-agents-tool-use',
        'prev_lesson_slug': 'prompt-foundations-few-shot'},
    {   'slug': 'prompt-ai-agents-tool-use',
        'course_slug': 'prompt-engineering-agents',
        'module_id': 'agent-mod-3',
        'title': 'Building Autonomous AI Agents: Function Calling & ReAct Loops',
        'order': 3,
        'estimated_minutes': 25,
        'difficulty': 'Intermediate',
        'skill_tag': 'ai_agents',
        'learning_objectives': [   'Understand the difference between a static Chatbot and an Autonomous Agent.',
                                   'Learn the ReAct loop: Thought -> Action (Tool Call) -> Observation (Tool Output) '
                                   '-> Final Response.',
                                   'Understand Function Calling: Letting LLMs output structured JSON to invoke APIs '
                                   'and databases.'],
        'theory_sections': [   {   'title': 'From Chatbots to Agents',
                                   'content_markdown': 'A traditional chatbot can only talk.\n'
                                                       '\n'
                                                       'An **AI Agent can take actions in the real world**! It can:\n'
                                                       '* Search the web for current weather or stock prices\n'
                                                       '* Query a SQL database to look up order status\n'
                                                       '* Execute Python code in a sandbox to plot graphs\n'
                                                       '* Send emails and update calendar invites',
                                   'key_takeaway': 'Agents combine reasoning with external tool execution to solve '
                                                   'multi-step problems autonomously.'},
                               {   'title': 'The ReAct (Reason + Act) Loop',
                                   'content_markdown': "How does an agent solve a goal like *'Check tomorrow's weather "
                                                       "in Tokyo and tell me if I need an umbrella'?*\n"
                                                       '\n'
                                                       "1. **Thought**: *'I need to look up Tokyo's weather forecast "
                                                       "for tomorrow.'*\n"
                                                       '2. **Action**: Call tool `get_weather(city="Tokyo", '
                                                       'date="tomorrow")`\n'
                                                       '3. **Observation**: Tool returns `{"rain_chance": 85%, '
                                                       '"condition": "Heavy Rain"}`\n'
                                                       "4. **Thought**: *'Rain chance is 85%, which is very high. I "
                                                       "should recommend an umbrella.'*\n"
                                                       "5. **Final Answer**: *'Yes, bring an umbrella! Tokyo has an "
                                                       "85% chance of heavy rain tomorrow.'*",
                                   'key_takeaway': 'The ReAct loop allows agents to repeatedly think, invoke tools, '
                                                   'inspect outputs, and formulate answers.'}],
        'visual_explainer': {   'type': 'architecture_flow',
                                'title': 'Autonomous Agent ReAct Loop',
                                'subtitle': 'User Goal -> LLM Thought -> Tool Execution -> Observation -> Loop -> '
                                            'Final Answer',
                                'diagram_type': 'agent_loop'},
        'code_example': {   'title': 'Simulating a Minimal ReAct Agent Loop in Python',
                            'language': 'python',
                            'code': 'def mock_calculator_tool(expression: str) -> str:\n'
                                    '    try:\n'
                                    '        return str(eval(expression))\n'
                                    '    except Exception as e:\n'
                                    '        return f"Error: {e}"\n'
                                    '\n'
                                    '# Simulated agent trace\n'
                                    'trace = [\n'
                                    '    {"type": "Thought", "content": "The user wants to know 145 * 38. I will '
                                    'invoke the calculator tool."},\n'
                                    '    {"type": "Action", "tool": "calculator", "args": "145 * 38"},\n'
                                    '    {"type": "Observation", "result": mock_calculator_tool("145 * 38")},\n'
                                    '    {"type": "Thought", "content": "The tool returned 5510. I can now answer the '
                                    'user directly."},\n'
                                    '    {"type": "Final Answer", "content": "145 multiplied by 38 equals 5,510."}\n'
                                    ']\n'
                                    '\n'
                                    'for step in trace:\n'
                                    '    print(f"[{step[\'type\']}]: {step.get(\'content\') or step.get(\'args\') or '
                                    'step.get(\'result\')}")',
                            'explanation': 'Simulates the Thought -> Action -> Observation -> Response cycle of '
                                           'autonomous AI agents.',
                            'output_preview': '[Thought]: The user wants to know 145 * 38. I will invoke the '
                                              'calculator tool.\n'
                                              '[Action]: 145 * 38\n'
                                              '[Observation]: 5510\n'
                                              '[Thought]: The tool returned 5510. I can now answer the user directly.\n'
                                              '[Final Answer]: 145 multiplied by 38 equals 5,510.'},
        'quiz_id': 'quiz-prompt-ai-agents-tool-use',
        'summary': 'You learned how AI agents use function calling and the ReAct loop to interact with tools and '
                   'execute multi-step workflows.',
        'next_lesson_slug': 'web-html-css-box-model',
        'prev_lesson_slug': 'prompt-chain-of-thought-reasoning'},
    {   'slug': 'web-how-the-web-works',
        'course_slug': 'html5-web-architecture',
        'module_id': 'html-mod-1',
        'title': 'How the Web Works: DNS, HTTP/HTTPS & The Client-Server Model',
        'order': 1,
        'estimated_minutes': 15,
        'difficulty': 'Beginner',
        'skill_tag': 'web_foundations',
        'learning_objectives': [   'Understand how a browser converts a URL (like google.com) into an IP address via '
                                   'DNS.',
                                   'Learn the client-server request/response cycle over TCP/IP.',
                                   'Understand HTTP methods (GET, POST, PUT, DELETE) and status codes (200, 301, 404, '
                                   '500).'],
        'theory_sections': [   {   'title': "The Web's Postal System Analogy",
                                   'content_markdown': 'When you type `https://example.com` into your browser:\n'
                                                       "1. **DNS (Phonebook)**: Your browser asks a DNS server, *'What "
                                                       "IP address belongs to example.com?'* -> Answer: "
                                                       '`93.184.216.34`.\n'
                                                       '2. **TCP Handshake (Knocking on the door)**: Browser and '
                                                       'server establish a secure, reliable connection.\n'
                                                       '3. **HTTP Request (Ordering a meal)**: Browser sends a `GET '
                                                       '/index.html HTTP/2` request with headers.\n'
                                                       '4. **HTTP Response (Delivering the meal)**: Server returns '
                                                       '`200 OK` along with the raw HTML string, CSS styles, and JS '
                                                       'bundles.',
                                   'key_takeaway': 'The web is fundamentally a request-response dialogue over HTTP '
                                                   'between client browsers and server machines.'}],
        'visual_explainer': {   'type': 'diagram',
                                'title': 'Client-Server Request-Response Lifecycle',
                                'subtitle': 'Browser -> DNS Lookup -> TCP Handshake -> HTTP GET -> 200 OK Response',
                                'diagram_type': 'client_server_flow'},
        'code_example': {   'title': 'Inspecting HTTP Request and Response Headers',
                            'language': 'http',
                            'code': 'GET /api/v1/profile HTTP/1.1\n'
                                    'Host: api.example.com\n'
                                    'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64)\n'
                                    'Accept: application/json\n'
                                    'Authorization: Bearer eyJhbGciOiJIUzI1NiIsIn...\n'
                                    '\n'
                                    'HTTP/1.1 200 OK\n'
                                    'Content-Type: application/json; charset=utf-8\n'
                                    'Cache-Control: max-age=3600\n'
                                    '\n'
                                    '{\n'
                                    '  "status": "success",\n'
                                    '  "user": { "id": 101, "username": "alex_dev" }\n'
                                    '}',
                            'explanation': 'Demonstrates raw HTTP headers sent by the client and returned by the '
                                           'server.',
                            'output_preview': 'Status: 200 OK | Content-Type: application/json'},
        'quiz_id': 'quiz-web-how-the-web-works',
        'summary': 'You understood DNS resolution, TCP handshakes, and HTTP/HTTPS client-server communication.',
        'next_lesson_slug': 'web-semantic-html5-tags',
        'prev_lesson_slug': 'prompt-ai-agents-tool-use'},
    {   'slug': 'web-semantic-html5-tags',
        'course_slug': 'html5-web-architecture',
        'module_id': 'html-mod-2',
        'title': 'Semantic HTML5 Architecture & Document Structure',
        'order': 2,
        'estimated_minutes': 20,
        'difficulty': 'Beginner',
        'skill_tag': 'html5_semantics',
        'learning_objectives': [   'Understand why semantic tags (<header>, <nav>, <main>, <article>, <aside>, '
                                   '<footer>) beat generic <div> soup.',
                                   'Learn how search engine web crawlers build document outline trees for SEO '
                                   'rankings.',
                                   'Implement accessible landmark elements recognized by screen readers.'],
        'theory_sections': [   {   'title': 'Why Semantic Tags Matter',
                                   'content_markdown': 'A webpage built entirely with `<div>` tags looks like a book '
                                                       'where every single word is printed in the same size without '
                                                       'chapters, headings, or index.\n'
                                                       '\n'
                                                       '* `<header>`: Site banner, logos, primary navigation.\n'
                                                       '* `<main>`: The unique core content of this specific page.\n'
                                                       '* `<article>`: Self-contained piece of content that makes '
                                                       'sense if syndicated on its own (like a blog post or product '
                                                       'card).\n'
                                                       '* `<section>`: Thematic grouping of content with a heading.\n'
                                                       '* `<footer>`: Author copyright, legal links, and secondary '
                                                       'navigation.',
                                   'key_takeaway': 'Semantic HTML describes the meaning of content, making it '
                                                   'indexable by SEO bots and accessible to assistive tech.'}],
        'visual_explainer': {   'type': 'diagram',
                                'title': 'Semantic HTML5 Landmark Hierarchy',
                                'subtitle': '<header> -> <nav> -> <main> [<article>, <section>] -> <aside> -> <footer>',
                                'diagram_type': 'html_landmarks'},
        'code_example': {   'title': 'Clean Semantic HTML5 Layout',
                            'language': 'html',
                            'code': '<!DOCTYPE html>\n'
                                    '<html lang="en">\n'
                                    '<head>\n'
                                    '  <meta charset="UTF-8" />\n'
                                    '  <meta name="viewport" content="width=device-width, initial-scale=1.0" />\n'
                                    '  <title>Developer Portfolio</title>\n'
                                    '</head>\n'
                                    '<body>\n'
                                    '  <header>\n'
                                    '    <nav aria-label="Main navigation">\n'
                                    '      <a href="/">Home</a>\n'
                                    '      <a href="/projects">Projects</a>\n'
                                    '    </nav>\n'
                                    '  </header>\n'
                                    '  <main>\n'
                                    '    <article>\n'
                                    '      <h1>Building Scalable Web Apps</h1>\n'
                                    '      <p>Modern full-stack practices...</p>\n'
                                    '    </article>\n'
                                    '  </main>\n'
                                    '  <footer>\n'
                                    '    <p>&copy; 2026 AI Learning Lab. All rights reserved.</p>\n'
                                    '  </footer>\n'
                                    '</body>\n'
                                    '</html>',
                            'explanation': 'Demonstrates semantic landmarks with proper viewport settings and '
                                           'accessible navigation.',
                            'output_preview': '[Rendered Semantic Web Document with Header, Main, and Footer]'},
        'quiz_id': 'quiz-web-semantic-html5-tags',
        'summary': 'You mastered semantic HTML5 document architecture and SEO landmark structures.',
        'next_lesson_slug': 'web-forms-validation-accessibility',
        'prev_lesson_slug': 'web-how-the-web-works'},
    {   'slug': 'web-forms-validation-accessibility',
        'course_slug': 'html5-web-architecture',
        'module_id': 'html-mod-3',
        'title': 'Interactive Forms, Native Validation & ARIA Accessibility',
        'order': 3,
        'estimated_minutes': 25,
        'difficulty': 'Beginner',
        'skill_tag': 'web_accessibility',
        'learning_objectives': [   'Build accessible forms connecting <label for="id"> with input fields.',
                                   'Use native HTML5 validations: required, minlength, type="email", pattern regex.',
                                   'Apply ARIA attributes (aria-expanded, aria-describedby, role="alert") for screen '
                                   'readers.'],
        'theory_sections': [   {   'title': 'Form Accessibility & UX',
                                   'content_markdown': 'Forms are the primary way users submit data to servers.\n'
                                                       '* Always connect labels to inputs using `<label '
                                                       'for="email-input">` so clicking the label focuses the input.\n'
                                                       '* Native HTML5 validation prevents invalid requests before '
                                                       'hitting JavaScript.\n'
                                                       '* ARIA attributes announce dynamic error messages to visually '
                                                       'impaired users automatically.',
                                   'key_takeaway': 'Accessible forms with explicit labels and native constraints '
                                                   'provide the best user experience and accessibility compliance.'}],
        'visual_explainer': {   'type': 'diagram',
                                'title': 'Accessible Form Interaction Model',
                                'subtitle': 'Label -> Input Focus -> Native Constraint Check -> ARIA Live Error '
                                            'Announcement',
                                'diagram_type': 'form_accessibility'},
        'code_example': {   'title': 'Accessible Registration Form with HTML5 Validation',
                            'language': 'html',
                            'code': '<form action="/api/register" method="POST">\n'
                                    '  <div class="form-group">\n'
                                    '    <label for="username">Username</label>\n'
                                    '    <input \n'
                                    '      type="text" \n'
                                    '      id="username" \n'
                                    '      name="username" \n'
                                    '      required \n'
                                    '      minlength="3" \n'
                                    '      aria-describedby="user-hint" \n'
                                    '    />\n'
                                    '    <small id="user-hint">Must be at least 3 characters.</small>\n'
                                    '  </div>\n'
                                    '  <button type="submit">Create Account</button>\n'
                                    '</form>',
                            'explanation': 'Demonstrates native client-side validation paired with ARIA description '
                                           'attributes.',
                            'output_preview': '[Accessible Input Form with validation feedback]'},
        'quiz_id': 'quiz-web-forms-validation-accessibility',
        'summary': 'You mastered accessible forms, ARIA standards, and native HTML5 input constraints.',
        'next_lesson_slug': 'web-css-box-model-cascade',
        'prev_lesson_slug': 'web-semantic-html5-tags'},
    {   'slug': 'web-css-box-model-cascade',
        'course_slug': 'css3-mastery-responsive-grid',
        'module_id': 'css-mod-1',
        'title': 'The CSS Box Model, Specificity & The Cascade',
        'order': 1,
        'estimated_minutes': 20,
        'difficulty': 'Beginner',
        'skill_tag': 'css_box_model',
        'learning_objectives': [   'Master the 4 layers of the Box Model: Content, Padding, Border, Margin.',
                                   'Understand why `box-sizing: border-box` solves accidental width expansion.',
                                   'Calculate CSS selector specificity: Inline (1000) > IDs (100) > Classes (10) > '
                                   'Tags (1).'],
        'theory_sections': [   {   'title': 'The Box Model Analogy',
                                   'content_markdown': 'Every single element on a web page is a rectangular box:\n'
                                                       '1. **Content**: The photo or text itself.\n'
                                                       '2. **Padding**: Bubble wrap inside the cardboard box '
                                                       'protecting the item.\n'
                                                       '3. **Border**: The cardboard box itself.\n'
                                                       '4. **Margin**: The empty distance between your package and '
                                                       'neighboring packages on the shelf!\n'
                                                       '\n'
                                                       'Using `box-sizing: border-box` ensures padding and borders '
                                                       'stay inside your specified width without breaking responsive '
                                                       'grids.',
                                   'key_takeaway': "Always use border-box so padding doesn't unexpectedly expand "
                                                   'element widths.'}],
        'visual_explainer': {   'type': 'diagram',
                                'title': 'CSS Box Model Layers',
                                'subtitle': 'Margin -> Border -> Padding -> Content',
                                'diagram_type': 'box_model'},
        'code_example': {   'title': 'Universal Box-Sizing Reset',
                            'language': 'css',
                            'code': '/* Universal CSS Reset */\n'
                                    '*,\n'
                                    '*::before,\n'
                                    '*::after {\n'
                                    '  box-sizing: border-box;\n'
                                    '  margin: 0;\n'
                                    '  padding: 0;\n'
                                    '}\n'
                                    '\n'
                                    '.card {\n'
                                    '  width: 300px;\n'
                                    '  padding: 20px;\n'
                                    '  border: 2px solid #3b82f6;\n'
                                    '  margin: 16px;\n'
                                    '  /* Total width remains precisely 300px on screen! */\n'
                                    '}',
                            'explanation': 'Demonstrates why border-box prevents element overflow in responsive '
                                           'layouts.',
                            'output_preview': '[Perfect 300px Width Box with internal padding]'},
        'quiz_id': 'quiz-web-css-box-model-cascade',
        'summary': 'You mastered the CSS Box Model, border-box sizing, and specificity calculations.',
        'next_lesson_slug': 'web-css-flexbox-grid-mastery',
        'prev_lesson_slug': 'web-forms-validation-accessibility'},
    {   'slug': 'web-css-flexbox-grid-mastery',
        'course_slug': 'css3-mastery-responsive-grid',
        'module_id': 'css-mod-2',
        'title': '1D Flexbox & 2D CSS Grid Layout Engineering',
        'order': 2,
        'estimated_minutes': 25,
        'difficulty': 'Beginner',
        'skill_tag': 'css_flexbox_grid',
        'learning_objectives': [   'Master 1D Flexbox: Main axis (justify-content) vs Cross axis (align-items).',
                                   'Master 2D CSS Grid: grid-template-columns with repeat(auto-fit, minmax(280px, '
                                   '1fr)).',
                                   'Combine Flexbox for components and CSS Grid for macro-page layouts.'],
        'theory_sections': [   {   'title': 'When to Use Flexbox vs CSS Grid',
                                   'content_markdown': '* **Flexbox (1D)**: For arranging items in a single direction '
                                                       '(row OR column). Ideal for navbars, pill badges, and form '
                                                       'control rows.\n'
                                                       '* **CSS Grid (2D)**: For arranging items across rows AND '
                                                       'columns simultaneously. Ideal for dashboard widgets, photo '
                                                       'galleries, and responsive product grids without media queries!',
                                   'key_takeaway': 'Use CSS Grid for overall page layouts and Flexbox for '
                                                   'component-level alignment.'}],
        'visual_explainer': {   'type': 'diagram',
                                'title': 'Flexbox vs CSS Grid Axis Models',
                                'subtitle': 'Flexbox (1D: Main/Cross) | CSS Grid (2D: Rows & Columns Matrix)',
                                'diagram_type': 'flex_vs_grid'},
        'code_example': {   'title': 'Zero-Media-Query Responsive Card Grid with CSS Grid',
                            'language': 'css',
                            'code': '.dashboard-grid {\n'
                                    '  display: grid;\n'
                                    '  /* Automatically wraps cards into clean columns based on available width */\n'
                                    '  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));\n'
                                    '  gap: 1.5rem;\n'
                                    '  padding: 1.5rem;\n'
                                    '}\n'
                                    '\n'
                                    '.card {\n'
                                    '  display: flex;\n'
                                    '  flex-direction: column;\n'
                                    '  justify-content: space-between;\n'
                                    '  background: #1e293b;\n'
                                    '  border-radius: 12px;\n'
                                    '  padding: 1rem;\n'
                                    '}',
                            'explanation': 'Creates a completely fluid responsive layout that adapts to any screen '
                                           'size automatically.',
                            'output_preview': '[Responsive Multi-Column Card Grid with auto-fit]'},
        'quiz_id': 'quiz-web-css-flexbox-grid-mastery',
        'summary': 'You mastered 1D Flexbox alignment and responsive 2D CSS Grid templates.',
        'next_lesson_slug': 'web-css-responsive-animations',
        'prev_lesson_slug': 'web-css-box-model-cascade'},
    {   'slug': 'web-css-responsive-animations',
        'course_slug': 'css3-mastery-responsive-grid',
        'module_id': 'css-mod-3',
        'title': 'Responsive Units, Custom Properties & Smooth Animations',
        'order': 3,
        'estimated_minutes': 20,
        'difficulty': 'Beginner',
        'skill_tag': 'css_animations',
        'learning_objectives': [   'Use fluid typography with `clamp(min, preferred, max)`.',
                                   'Manage design system tokens using CSS Custom Properties (`--color-primary`).',
                                   'Create 60fps GPU-accelerated micro-animations using `transform` and `opacity`.'],
        'theory_sections': [   {   'title': '60fps Performance Rules in CSS',
                                   'content_markdown': 'Animating properties like `width`, `height`, or `top` forces '
                                                       'the browser to recalculate layout and repaint pixels across '
                                                       'the entire screen (causing UI lag).\n'
                                                       '\n'
                                                       'Always animate `transform: translate3d()` and `opacity`. These '
                                                       'run directly on the GPU compositor thread without triggering '
                                                       'CPU layout recalculations!',
                                   'key_takeaway': 'Animate only transform and opacity for butter-smooth 60fps '
                                                   'animations.'}],
        'visual_explainer': {   'type': 'diagram',
                                'title': 'Browser Rendering Pipeline',
                                'subtitle': 'JS -> Style Calc -> Layout (Reflow) -> Paint -> Composite (GPU)',
                                'diagram_type': 'rendering_pipeline'},
        'code_example': {   'title': 'Design Tokens & Smooth GPU Hover Effect',
                            'language': 'css',
                            'code': ':root {\n'
                                    '  --primary: #3b82f6;\n'
                                    '  --radius: 8px;\n'
                                    '  --transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1);\n'
                                    '}\n'
                                    '\n'
                                    '.btn-interactive {\n'
                                    '  background: var(--primary);\n'
                                    '  border-radius: var(--radius);\n'
                                    '  transition: transform 0.2s ease, box-shadow 0.2s ease;\n'
                                    '  will-change: transform;\n'
                                    '}\n'
                                    '\n'
                                    '.btn-interactive:hover {\n'
                                    '  transform: translateY(-2px);\n'
                                    '  box-shadow: 0 10px 25px -5px rgba(59, 130, 246, 0.5);\n'
                                    '}',
                            'explanation': 'Leverages CSS variables and hardware-accelerated transform for fluid '
                                           'interactive buttons.',
                            'output_preview': '[Interactive Glowing Button with smooth elevation lift]'},
        'quiz_id': 'quiz-web-css-responsive-animations',
        'summary': 'You mastered CSS custom properties, clamp fluid units, and GPU-accelerated animations.',
        'next_lesson_slug': 'web-js-execution-scope-closures',
        'prev_lesson_slug': 'web-css-flexbox-grid-mastery'},
    {   'slug': 'web-js-execution-scope-closures',
        'course_slug': 'javascript-core-async',
        'module_id': 'js-mod-1',
        'title': 'JavaScript Execution Contexts, Lexical Scope & Closures',
        'order': 1,
        'estimated_minutes': 25,
        'difficulty': 'Intermediate',
        'skill_tag': 'javascript_internals',
        'learning_objectives': [   'Understand the Global Execution Context and Function Execution Contexts on the '
                                   'Call Stack.',
                                   'Learn how Lexical Scope determines variable accessibility.',
                                   'Master Closures: How inner functions retain access to their outer enclosing '
                                   'scope.'],
        'theory_sections': [   {   'title': 'The Backpack Analogy (Closures)',
                                   'content_markdown': 'When a function finishes running, its local variables are '
                                                       'normally destroyed by garbage collection.\n'
                                                       '\n'
                                                       'However, if an inner function is returned, it packs a '
                                                       '**Backpack (Closure)** containing all the variables from its '
                                                       'lexical birth environment. Wherever that inner function '
                                                       'travels in your code, it still has access to the variables '
                                                       'inside its backpack!',
                                   'key_takeaway': "A closure gives you access to an outer function's scope from an "
                                                   'inner function even after the outer function has returned.'}],
        'visual_explainer': {   'type': 'diagram',
                                'title': 'Closure Scope Backpack in Memory',
                                'subtitle': 'Outer Function [count=0] -> Returns Inner Function -> Closure retains '
                                            '[count]',
                                'diagram_type': 'closure_memory'},
        'code_example': {   'title': 'Creating Private Encapsulated State with Closures',
                            'language': 'javascript',
                            'code': 'function createCounter(initialValue = 0) {\n'
                                    '  let count = initialValue; // Private state variable\n'
                                    '\n'
                                    '  return {\n'
                                    '    increment: () => ++count,\n'
                                    '    decrement: () => --count,\n'
                                    '    getValue: () => count\n'
                                    '  };\n'
                                    '}\n'
                                    '\n'
                                    'const counter = createCounter(10);\n'
                                    'console.log(counter.increment()); // 11\n'
                                    'console.log(counter.increment()); // 12\n'
                                    'console.log(counter.getValue());  // 12\n'
                                    "// 'count' cannot be modified directly from outside!",
                            'explanation': 'Demonstrates closure data hiding without using classes.',
                            'output_preview': '11\n12\n12'},
        'quiz_id': 'quiz-web-js-execution-scope-closures',
        'summary': 'You mastered execution contexts, lexical scope chains, and closure memory retention.',
        'next_lesson_slug': 'web-js-event-loop-promises-async',
        'prev_lesson_slug': 'web-css-responsive-animations'},
    {   'slug': 'web-js-event-loop-promises-async',
        'course_slug': 'javascript-core-async',
        'module_id': 'js-mod-2',
        'title': 'The Event Loop, Microtask Queue, Promises & Async/Await',
        'order': 2,
        'estimated_minutes': 25,
        'difficulty': 'Intermediate',
        'skill_tag': 'javascript_async',
        'learning_objectives': [   'Understand the single-threaded Event Loop, Call Stack, Web APIs, and Microtask '
                                   'Queue.',
                                   'Learn why Promise microtasks execute before setTimeout macrotasks.',
                                   'Handle asynchronous network calls with async/await and robust try/catch blocks.'],
        'theory_sections': [   {   'title': 'The Restaurant Kitchen (Event Loop)',
                                   'content_markdown': 'JavaScript has only **one thread (one waiter)**.\n'
                                                       '* If the waiter waits 10 minutes at the kitchen door for steak '
                                                       'to cook (Synchronous network block), no other tables get '
                                                       'water!\n'
                                                       '* Instead, the waiter sends the steak order to the kitchen '
                                                       '(Web API background worker) and serves other customers.\n'
                                                       '* When the steak is cooked, it rings a bell in the **Callback '
                                                       'Queue**, and the waiter delivers it as soon as their hands are '
                                                       'free!\n'
                                                       '\n'
                                                       '**Async/Await** lets you write clean asynchronous code without '
                                                       'blocking the browser UI.',
                                   'key_takeaway': 'Async/await prevents blocking the main thread while fetching data '
                                                   'over the network.'}],
        'visual_explainer': {   'type': 'diagram',
                                'title': 'JavaScript Event Loop Architecture',
                                'subtitle': 'Call Stack -> Web APIs -> Microtask Queue (Promises) -> Macrotask Queue '
                                            '(Timers) -> Event Loop',
                                'diagram_type': 'event_loop'},
        'code_example': {   'title': 'Parallel Network Fetching with Promise.allSettled',
                            'language': 'javascript',
                            'code': 'async function loadDashboardData(userId) {\n'
                                    '  try {\n'
                                    '    const [userRes, metricsRes] = await Promise.all([\n'
                                    '      fetch(`/api/users/${userId}`),\n'
                                    '      fetch(`/api/users/${userId}/metrics`)\n'
                                    '    ]);\n'
                                    '\n'
                                    '    const user = await userRes.json();\n'
                                    '    const metrics = await metricsRes.json();\n'
                                    '    return { user, metrics };\n'
                                    '  } catch (err) {\n'
                                    "    console.error('Network failure:', err.message);\n"
                                    '    throw err;\n'
                                    '  }\n'
                                    '}',
                            'explanation': 'Executes multiple HTTP requests in parallel rather than serial waterfalls.',
                            'output_preview': "{ user: { name: 'Alex' }, metrics: { streak: 14 } }"},
        'quiz_id': 'quiz-web-js-event-loop-promises-async',
        'summary': 'You mastered the JavaScript Event Loop, Promise microtask queues, and parallel async data '
                   'fetching.',
        'next_lesson_slug': 'web-js-dom-events-delegation',
        'prev_lesson_slug': 'web-js-execution-scope-closures'},
    {   'slug': 'web-js-dom-events-delegation',
        'course_slug': 'javascript-core-async',
        'module_id': 'js-mod-3',
        'title': 'High-Performance DOM Traversal & Event Delegation',
        'order': 3,
        'estimated_minutes': 20,
        'difficulty': 'Intermediate',
        'skill_tag': 'dom_manipulation',
        'learning_objectives': [   'Traverse and query the DOM with `querySelector` and `closest()`.',
                                   'Understand Event Bubbling and Event Capturing phases.',
                                   'Implement Event Delegation on parent containers to handle thousands of dynamic '
                                   'child nodes efficiently.'],
        'theory_sections': [   {   'title': 'Event Delegation Pattern',
                                   'content_markdown': 'If you have a table with 1,000 rows, attaching 1,000 separate '
                                                       '`click` listeners consumes massive heap memory.\n'
                                                       '\n'
                                                       'Because events **bubble up** to parent ancestors, you attach '
                                                       '**one single listener** to the `<table>` element. When '
                                                       "clicked, `event.target.closest('tr')` identifies precisely "
                                                       'which row triggered the action!',
                                   'key_takeaway': 'Event delegation attaches a single event handler to a parent to '
                                                   'manage all existing and future children.'}],
        'visual_explainer': {   'type': 'diagram',
                                'title': 'DOM Event Bubbling Propagation',
                                'subtitle': 'Target Element -> Parent Div -> Section -> Body -> Document Window',
                                'diagram_type': 'event_bubbling'},
        'code_example': {   'title': 'Event Delegation with closest() Pattern',
                            'language': 'javascript',
                            'code': "const listContainer = document.querySelector('#todo-list');\n"
                                    '\n'
                                    '// One single listener for all present and future items!\n'
                                    "listContainer.addEventListener('click', (e) => {\n"
                                    "  const deleteBtn = e.target.closest('.delete-btn');\n"
                                    '  if (!deleteBtn) return;\n'
                                    '\n'
                                    "  const item = deleteBtn.closest('.todo-item');\n"
                                    '  item.remove();\n'
                                    '});',
                            'explanation': 'Demonstrates high-performance event delegation managing dynamically '
                                           'appended items.',
                            'output_preview': '[Item removed from DOM on delete click]'},
        'quiz_id': 'quiz-web-js-dom-events-delegation',
        'summary': 'You mastered DOM traversal, event bubbling propagation, and high-performance event delegation.',
        'next_lesson_slug': 'web-react-jsx-vdom-components',
        'prev_lesson_slug': 'web-js-event-loop-promises-async'},
    {   'slug': 'web-react-jsx-vdom-components',
        'course_slug': 'react18-frontend-architecture',
        'module_id': 'react-mod-1',
        'title': 'Declarative JSX, Component Hierarchies & Virtual DOM Diffing',
        'order': 1,
        'estimated_minutes': 25,
        'difficulty': 'Intermediate',
        'skill_tag': 'react_core',
        'learning_objectives': [   'Understand Declarative UI vs Imperative DOM manipulation.',
                                   'Learn how JSX compiles down to `React.createElement()` function calls.',
                                   "Understand React's Reconciliation algorithm (Virtual DOM diffing) and why unique "
                                   '`key` props are mandatory.'],
        'theory_sections': [   {   'title': 'Declarative UI vs Imperative DOM',
                                   'content_markdown': 'In traditional vanilla JS, you manually query elements and '
                                                       'modify innerHTML: '
                                                       "`document.getElementById('btn').style.background = 'blue'` "
                                                       '(Imperative).\n'
                                                       '\n'
                                                       'In **React**, you simply declare what the UI should look like '
                                                       "based on current state: *'If `isLiked` is true, render a red "
                                                       "heart; otherwise render a gray heart.'* React takes care of "
                                                       'surgically updating the actual browser DOM using its '
                                                       'high-speed Virtual DOM reconciliation diff algorithm!',
                                   'key_takeaway': 'React component state drives the UI automatically whenever '
                                                   'variables change.'}],
        'visual_explainer': {   'type': 'diagram',
                                'title': 'React Reconciliation & Virtual DOM Diffing',
                                'subtitle': 'State Change -> Virtual DOM Snapshot -> Diff Tree -> Surgical Real DOM '
                                            'Patch',
                                'diagram_type': 'vdom_diffing'},
        'code_example': {   'title': 'Reusable Component with Typed Props and Keys',
                            'language': 'jsx',
                            'code': 'export function CourseCard({ title, level, xpReward, isCompleted }) {\n'
                                    '  return (\n'
                                    "    <div className={`course-card ${isCompleted ? 'border-green' : "
                                    "'border-slate'}`}>\n"
                                    '      <h3>{title}</h3>\n'
                                    '      <div className="meta-row">\n'
                                    '        <span className="badge">{level}</span>\n'
                                    '        <span className="xp">+{xpReward} XP</span>\n'
                                    '      </div>\n'
                                    '    </div>\n'
                                    '  );\n'
                                    '}',
                            'explanation': 'Demonstrates declarative JSX component composition with dynamic '
                                           'conditional classes.',
                            'output_preview': '[Rendered Course Card Component with Badges]'},
        'quiz_id': 'quiz-web-react-jsx-vdom-components',
        'summary': 'You mastered JSX compilation, Virtual DOM reconciliation, and component composition.',
        'next_lesson_slug': 'web-react-hooks-deep-dive',
        'prev_lesson_slug': 'web-js-dom-events-delegation'},
    {   'slug': 'web-react-hooks-deep-dive',
        'course_slug': 'react18-frontend-architecture',
        'module_id': 'react-mod-2',
        'title': 'React 18 Hooks Deep-Dive: useEffect, useMemo & Custom Hooks',
        'order': 2,
        'estimated_minutes': 25,
        'difficulty': 'Intermediate',
        'skill_tag': 'react_hooks',
        'learning_objectives': [   'Master the `useEffect` lifecycle and cleanup functions (clearing '
                                   'timers/listeners).',
                                   'Optimize expensive calculations and memoize callbacks with `useMemo` and '
                                   '`useCallback`.',
                                   'Extract shared business logic into clean, reusable Custom Hooks (e.g. `useFetch`, '
                                   '`useDebounce`).'],
        'theory_sections': [   {   'title': 'The Rules of Hooks & Dependency Arrays',
                                   'content_markdown': '* **Rule 1**: Only call hooks at the top level (never inside '
                                                       'loops or conditions).\n'
                                                       '* **Rule 2**: Only call hooks from React function components '
                                                       'or custom hooks.\n'
                                                       '* **Dependency Arrays**: If you use a state variable or prop '
                                                       'inside `useEffect` or `useMemo`, it MUST be declared in the '
                                                       'dependency array to prevent stale closure bugs.',
                                   'key_takeaway': 'Custom hooks allow you to isolate stateful logic into reusable '
                                                   'modular functions.'}],
        'visual_explainer': {   'type': 'diagram',
                                'title': 'React Hook Lifecycle & Cleanup',
                                'subtitle': 'Component Mount -> Effect Runs -> Dependency Change -> Cleanup Previous '
                                            '-> Effect Re-runs',
                                'diagram_type': 'hooks_lifecycle'},
        'code_example': {   'title': 'Building a Reusable useDebounce Custom Hook',
                            'language': 'jsx',
                            'code': "import { useState, useEffect } from 'react';\n"
                                    '\n'
                                    'export function useDebounce(value, delayMs = 300) {\n'
                                    '  const [debouncedValue, setDebouncedValue] = useState(value);\n'
                                    '\n'
                                    '  useEffect(() => {\n'
                                    '    const timer = setTimeout(() => setDebouncedValue(value), delayMs);\n'
                                    '    return () => clearTimeout(timer); // Cleanup on rapid keystrokes\n'
                                    '  }, [value, delayMs]);\n'
                                    '\n'
                                    '  return debouncedValue;\n'
                                    '}',
                            'explanation': 'Debounces rapid user typing in search inputs to avoid triggering hundreds '
                                           'of redundant API calls.',
                            'output_preview': '[Debounced Search Query emits after 300ms idle]'},
        'quiz_id': 'quiz-web-react-hooks-deep-dive',
        'summary': 'You mastered useEffect cleanup lifecycles, memoization optimizations, and custom hooks.',
        'next_lesson_slug': 'web-react-state-routing-zustand',
        'prev_lesson_slug': 'web-react-jsx-vdom-components'},
    {   'slug': 'web-react-state-routing-zustand',
        'course_slug': 'react18-frontend-architecture',
        'module_id': 'react-mod-3',
        'title': 'Global State Architecture (Context vs Zustand) & Client Routing',
        'order': 3,
        'estimated_minutes': 25,
        'difficulty': 'Intermediate',
        'skill_tag': 'react_state_management',
        'learning_objectives': [   'Understand Prop Drilling and when to use Global State vs Local State.',
                                   'Compare React Context API vs lightweight atomic stores like Zustand.',
                                   'Implement multi-page client-side routing with React Router 6 and protected route '
                                   'guards.'],
        'theory_sections': [   {   'title': 'State Colocation vs Global Stores',
                                   'content_markdown': "Don't put everything into global state! Keep state as close to "
                                                       'where it is used as possible (**State Colocation**).\n'
                                                       '\n'
                                                       'When multiple non-adjacent components need shared data (like '
                                                       'user auth tokens, dark mode theme, or shopping cart items), '
                                                       'lightweight state managers like **Zustand** provide direct '
                                                       'atomic subscriptions without re-rendering the entire component '
                                                       'tree.',
                                   'key_takeaway': 'Use local state for UI components and atomic Zustand stores for '
                                                   'global application state.'}],
        'visual_explainer': {   'type': 'diagram',
                                'title': 'Prop Drilling vs Atomic Global State Store',
                                'subtitle': 'Parent -> Child -> Child (Drilling) vs Component -> Direct Zustand Store '
                                            'Subscription',
                                'diagram_type': 'state_architecture'},
        'code_example': {   'title': 'Creating an Atomic Auth Store with Zustand',
                            'language': 'javascript',
                            'code': "import { create } from 'zustand';\n"
                                    '\n'
                                    'export const useAuthStore = create((set) => ({\n'
                                    '  user: null,\n'
                                    '  token: null,\n'
                                    '  isAuthenticated: false,\n'
                                    '  login: (userData, authToken) => set({\n'
                                    '    user: userData,\n'
                                    '    token: authToken,\n'
                                    '    isAuthenticated: true\n'
                                    '  }),\n'
                                    '  logout: () => set({ user: null, token: null, isAuthenticated: false })\n'
                                    '}));',
                            'explanation': 'Provides instant global state access with zero boilerplate and minimal '
                                           're-render overhead.',
                            'output_preview': '[Global User Profile & Session Store Active]'},
        'quiz_id': 'quiz-web-react-state-routing-zustand',
        'summary': 'You mastered state colocation, Zustand global stores, and client-side routing.',
        'next_lesson_slug': 'web-nodejs-express-middleware',
        'prev_lesson_slug': 'web-react-hooks-deep-dive'},
    {   'slug': 'web-nodejs-express-middleware',
        'course_slug': 'nodejs-backend-apis',
        'module_id': 'node-mod-1',
        'title': 'Node.js Architecture & Express Middleware Pipelines',
        'order': 1,
        'estimated_minutes': 25,
        'difficulty': 'Intermediate',
        'skill_tag': 'nodejs_express',
        'learning_objectives': [   'Understand the Node.js libuv asynchronous I/O thread pool.',
                                   'Learn how the Express Middleware Pipeline processes requests in sequence using '
                                   '`next()`.',
                                   'Implement centralized error-handling middleware.'],
        'theory_sections': [   {   'title': 'The Onion Middleware Model',
                                   'content_markdown': 'In Express, every incoming HTTP request passes through a '
                                                       'pipeline of middleware functions like layers of an onion:\n'
                                                       '1. **Logger Middleware**: Records `[GET] /api/users`.\n'
                                                       '2. **CORS & JSON Body Parser**: Parses raw body streams into '
                                                       '`req.body`.\n'
                                                       '3. **Auth Guard Middleware**: Verifies JWT bearer token.\n'
                                                       '4. **Route Controller**: Executes database query and sends '
                                                       '`res.json()`.',
                                   'key_takeaway': 'Middleware functions have access to req, res, and next, allowing '
                                                   'modular validation, authentication, and logging.'}],
        'visual_explainer': {   'type': 'diagram',
                                'title': 'Express Middleware Onion Pipeline',
                                'subtitle': 'Request -> [Logger] -> [CORS/Parser] -> [AuthGuard] -> [Controller] -> '
                                            'Response',
                                'diagram_type': 'middleware_pipeline'},
        'code_example': {   'title': 'Express REST API with Modular Middleware',
                            'language': 'javascript',
                            'code': "import express from 'express';\n"
                                    '\n'
                                    'const app = express();\n'
                                    'app.use(express.json());\n'
                                    '\n'
                                    '// Custom Request Timing Middleware\n'
                                    'app.use((req, res, next) => {\n'
                                    '  const start = Date.now();\n'
                                    "  res.on('finish', () => console.log(`${req.method} ${req.url} took ${Date.now() "
                                    '- start}ms`));\n'
                                    '  next();\n'
                                    '});\n'
                                    '\n'
                                    "app.get('/api/health', (req, res) => {\n"
                                    "  res.json({ status: 'ok', uptime: process.uptime() });\n"
                                    '});\n'
                                    '\n'
                                    "app.listen(8080, () => console.log('Server running on port 8080'));",
                            'explanation': 'Demonstrates non-blocking middleware execution and JSON response '
                                           'formatting.',
                            'output_preview': '[GET] /api/health took 2ms | 200 OK'},
        'quiz_id': 'quiz-web-nodejs-express-middleware',
        'summary': 'You mastered the Node.js runtime, Express middleware chaining, and server initialization.',
        'next_lesson_slug': 'web-jwt-auth-security-bcrypt',
        'prev_lesson_slug': 'web-react-state-routing-zustand'},
    {   'slug': 'web-jwt-auth-security-bcrypt',
        'course_slug': 'nodejs-backend-apis',
        'module_id': 'node-mod-2',
        'title': 'JWT Token Authentication, Bcrypt Hashing & REST Security',
        'order': 2,
        'estimated_minutes': 25,
        'difficulty': 'Intermediate',
        'skill_tag': 'web_security',
        'learning_objectives': [   'Hash user passwords with salted Bcrypt algorithms (never store plaintext '
                                   'passwords!).',
                                   'Understand the 3 parts of a JWT: Header, Payload, and Cryptographic Signature.',
                                   'Protect endpoints against XSS and CSRF using HTTP-only secure cookies.'],
        'theory_sections': [   {   'title': 'How JSON Web Tokens Work',
                                   'content_markdown': 'A JWT is a stateless identity passport:\n'
                                                       '* **Header**: Algorithm used (e.g. `HS256`).\n'
                                                       '* **Payload**: Public user claims (`userId: 42, role: '
                                                       '"admin"`).\n'
                                                       '* **Signature**: Hash of Header + Payload signed with your '
                                                       "server's secret key.\n"
                                                       '\n'
                                                       'Because the signature can only be created by the server, any '
                                                       'tampering with the payload invalidates the token instantly '
                                                       'without querying a session database!',
                                   'key_takeaway': 'JWTs allow stateless, scalable authentication verified via '
                                                   'cryptographic signatures.'}],
        'visual_explainer': {   'type': 'diagram',
                                'title': 'JWT Authentication Lifecycle',
                                'subtitle': 'Login -> Password Verified -> Server Signs JWT -> Client Stores Token -> '
                                            'Bearer Auth on API Calls',
                                'diagram_type': 'jwt_auth_flow'},
        'code_example': {   'title': 'Verifying JWT in Express Auth Guard Middleware',
                            'language': 'javascript',
                            'code': "import jwt from 'jsonwebtoken';\n"
                                    '\n'
                                    'export function requireAuth(req, res, next) {\n'
                                    '  const authHeader = req.headers.authorization;\n'
                                    "  if (!authHeader || !authHeader.startsWith('Bearer ')) {\n"
                                    "    return res.status(401).json({ error: 'Unauthorized: Missing token' });\n"
                                    '  }\n'
                                    '\n'
                                    "  const token = authHeader.split(' ')[1];\n"
                                    '  try {\n'
                                    '    const decoded = jwt.verify(token, process.env.JWT_SECRET);\n'
                                    '    req.user = decoded;\n'
                                    '    next();\n'
                                    '  } catch (err) {\n'
                                    "    return res.status(403).json({ error: 'Forbidden: Invalid or expired token' "
                                    '});\n'
                                    '  }\n'
                                    '}',
                            'explanation': 'Guards private API routes by verifying JWT cryptographic authenticity.',
                            'output_preview': "Verified req.user: { userId: 42, role: 'admin' }"},
        'quiz_id': 'quiz-web-jwt-auth-security-bcrypt',
        'summary': 'You mastered salted password hashing, JWT signing, and route protection guards.',
        'next_lesson_slug': 'web-db-mongodb-postgresql-crud',
        'prev_lesson_slug': 'web-nodejs-express-middleware'},
    {   'slug': 'web-db-mongodb-postgresql-crud',
        'course_slug': 'nodejs-backend-apis',
        'module_id': 'node-mod-3',
        'title': 'Database Modeling with MongoDB & PostgreSQL CRUD',
        'order': 3,
        'estimated_minutes': 25,
        'difficulty': 'Intermediate',
        'skill_tag': 'database_crud',
        'learning_objectives': [   'Compare Document Databases (MongoDB) vs Relational Tables (PostgreSQL).',
                                   'Design normalized schemas, foreign keys, and indexes for fast queries.',
                                   'Implement high-performance CRUD queries and prevent SQL injection '
                                   'vulnerabilities.'],
        'theory_sections': [   {   'title': 'SQL vs NoSQL Decision Matrix',
                                   'content_markdown': '* **Relational (PostgreSQL)**: Rigid tabular schema with '
                                                       'strict ACID transactions. Best for financial ledgers, '
                                                       'inventory systems, and complex relational joins.\n'
                                                       '* **Document (MongoDB)**: Flexible JSON-like BSON documents '
                                                       'that can nest arrays and sub-objects. Best for rapid '
                                                       'prototyping, content management, and polymorphic data models.',
                                   'key_takeaway': 'Choose PostgreSQL for structured relational consistency and '
                                                   'MongoDB for flexible nested document schemas.'}],
        'visual_explainer': {   'type': 'diagram',
                                'title': 'Relational Tables vs Document JSON Models',
                                'subtitle': 'PostgreSQL (Foreign Key Joins) vs MongoDB (Embedded BSON Documents)',
                                'diagram_type': 'sql_vs_nosql'},
        'code_example': {   'title': 'Parameterized SQL Query Preventing SQL Injection',
                            'language': 'javascript',
                            'code': "import { pool } from './db.js';\n"
                                    '\n'
                                    'export async function getUserById(userId) {\n'
                                    '  // Parameterized query: $1 prevents SQL injection attacks!\n'
                                    "  const query = 'SELECT id, username, email, created_at FROM users WHERE id = "
                                    "$1';\n"
                                    '  const result = await pool.query(query, [userId]);\n'
                                    '  return result.rows[0];\n'
                                    '}',
                            'explanation': 'Demonstrates safe database querying using parameterized values.',
                            'output_preview': "{ id: 101, username: 'alex_dev', email: 'alex@example.com' }"},
        'quiz_id': 'quiz-web-db-mongodb-postgresql-crud',
        'summary': 'You mastered database schema design, index optimization, and SQL injection prevention.',
        'next_lesson_slug': 'web-nextjs-ssr-ssg-hydration',
        'prev_lesson_slug': 'web-jwt-auth-security-bcrypt'},
    {   'slug': 'web-nextjs-ssr-ssg-hydration',
        'course_slug': 'advanced-fullstack-performance',
        'module_id': 'adv-web-mod-1',
        'title': 'Next.js Architecture: SSR, SSG & Client Hydration',
        'order': 1,
        'estimated_minutes': 30,
        'difficulty': 'Advanced',
        'skill_tag': 'nextjs_ssr',
        'learning_objectives': [   'Understand the trade-offs: Client-Side Rendering (CSR), Static Site Generation '
                                   '(SSG), and Server-Side Rendering (SSR).',
                                   'Learn how Client Hydration attaches event listeners to pre-rendered server HTML.',
                                   'Build full-stack applications with React Server Components (RSC).'],
        'theory_sections': [   {   'title': 'The Hydration Process',
                                   'content_markdown': 'In traditional SPA (CSR), the user sees a blank screen until '
                                                       'the massive JS bundle downloads, parses, and renders.\n'
                                                       '\n'
                                                       'In **SSR / Next.js**:\n'
                                                       '1. Server executes React components and sends a fully-rendered '
                                                       'HTML document immediately (instant visual preview for SEO and '
                                                       'users!).\n'
                                                       '2. The browser downloads the lightweight JavaScript bundle.\n'
                                                       '3. **Hydration**: React walks through the existing DOM and '
                                                       'attaches interactive event listeners seamlessly.',
                                   'key_takeaway': 'SSR sends ready-to-view HTML from the server, which is then '
                                                   'hydrated with React interactive event listeners.'}],
        'visual_explainer': {   'type': 'diagram',
                                'title': 'SSR Server Render & Hydration Timeline',
                                'subtitle': 'Server renders HTML -> Fast First Paint -> JS Bundle Loads -> Hydration '
                                            'completes -> Fully Interactive',
                                'diagram_type': 'hydration_timeline'},
        'code_example': {   'title': 'React Server Component Fetching Data on the Server',
                            'language': 'jsx',
                            'code': '// Next.js Server Component (Zero client-side JS bundle overhead!)\n'
                                    'export default async function LeaderboardPage() {\n'
                                    "  const res = await fetch('https://api.example.com/leaderboard', { next: { "
                                    'revalidate: 60 } });\n'
                                    '  const topLearners = await res.json();\n'
                                    '\n'
                                    '  return (\n'
                                    '    <main className="leaderboard">\n'
                                    '      <h1>Global AI Masterclass Leaderboard</h1>\n'
                                    '      <ul>\n'
                                    '        {topLearners.map(student => (\n'
                                    '          <li key={student.id}>{student.name} — {student.xp} XP</li>\n'
                                    '        ))}\n'
                                    '      </ul>\n'
                                    '    </main>\n'
                                    '  );\n'
                                    '}',
                            'explanation': 'Executes data fetching securely on the server without leaking API keys to '
                                           'the browser.',
                            'output_preview': '[Instantly Rendered Server HTML with Cached Leaderboard Data]'},
        'quiz_id': 'quiz-web-nextjs-ssr-ssg-hydration',
        'summary': 'You mastered Server-Side Rendering, Static Site Generation, and React hydration architecture.',
        'next_lesson_slug': 'web-performance-core-web-vitals',
        'prev_lesson_slug': 'web-db-mongodb-postgresql-crud'},
    {   'slug': 'web-performance-core-web-vitals',
        'course_slug': 'advanced-fullstack-performance',
        'module_id': 'adv-web-mod-2',
        'title': 'Web Performance Optimization & Core Web Vitals',
        'order': 2,
        'estimated_minutes': 25,
        'difficulty': 'Advanced',
        'skill_tag': 'web_performance',
        'learning_objectives': [   'Master Google Core Web Vitals: LCP (Largest Contentful Paint), INP (Interaction to '
                                   'Next Paint), CLS (Cumulative Layout Shift).',
                                   'Optimize bundle sizes with dynamic code-splitting and dynamic `import()`.',
                                   'Implement image responsive srcset, lazy loading, and modern WebP/AVIF '
                                   'compression.'],
        'theory_sections': [   {   'title': 'Diagnosing Core Web Vitals',
                                   'content_markdown': '* **LCP (< 2.5s)**: Measures loading performance of the main '
                                                       'hero image or headline block.\n'
                                                       '* **INP (< 200ms)**: Measures UI responsiveness when a user '
                                                       'clicks a button or taps a menu.\n'
                                                       '* **CLS (< 0.1)**: Measures visual stability (preventing '
                                                       'buttons from jumping around as ads or late images load). '
                                                       'Always declare explicit `width` and `height` attributes on '
                                                       'images!',
                                   'key_takeaway': 'Optimizing Core Web Vitals boosts Google SEO rankings and '
                                                   'drastically cuts user bounce rates.'}],
        'visual_explainer': {   'type': 'diagram',
                                'title': 'Google Core Web Vitals Metrics',
                                'subtitle': 'LCP (Loading < 2.5s) | INP (Interactivity < 200ms) | CLS (Stability < '
                                            '0.1)',
                                'diagram_type': 'core_web_vitals'},
        'code_example': {   'title': 'Dynamic Code-Splitting with React.lazy and Suspense',
                            'language': 'jsx',
                            'code': "import React, { lazy, Suspense } from 'react';\n"
                                    '\n'
                                    '// Heavy 3D / Graph component is downloaded only when navigated to!\n'
                                    "const HeavyAnalyticsGraph = lazy(() => import('./HeavyAnalyticsGraph'));\n"
                                    '\n'
                                    'export function AnalyticsDashboard() {\n'
                                    '  return (\n'
                                    '    <div>\n'
                                    '      <h2>Performance Dashboard</h2>\n'
                                    '      <Suspense fallback={<div className="skeleton">Loading chart '
                                    'modules...</div>}>\n'
                                    '        <HeavyAnalyticsGraph />\n'
                                    '      </Suspense>\n'
                                    '    </div>\n'
                                    '  );\n'
                                    '}',
                            'explanation': 'Drastically reduces initial page bundle size by lazy-loading heavy '
                                           'secondary dependencies.',
                            'output_preview': '[Lazy Module Loaded On Demand]'},
        'quiz_id': 'quiz-web-performance-core-web-vitals',
        'summary': 'You mastered Core Web Vitals, dynamic code splitting, and asset loading optimizations.',
        'next_lesson_slug': 'web-websockets-realtime-redis-caching',
        'prev_lesson_slug': 'web-nextjs-ssr-ssg-hydration'},
    {   'slug': 'web-websockets-realtime-redis-caching',
        'course_slug': 'advanced-fullstack-performance',
        'module_id': 'adv-web-mod-3',
        'title': 'Real-Time WebSockets & Distributed In-Memory Redis Caching',
        'order': 3,
        'estimated_minutes': 30,
        'difficulty': 'Advanced',
        'skill_tag': 'realtime_caching',
        'learning_objectives': [   'Understand full-duplex persistent bidirectional communication with WebSockets.',
                                   'Implement the Cache-Aside pattern with Redis to eliminate repetitive database '
                                   'hits.',
                                   'Handle cache invalidation and Time-To-Live (TTL) expiration strategies.'],
        'theory_sections': [   {   'title': 'HTTP Polling vs WebSockets vs Redis Caching',
                                   'content_markdown': '* **HTTP Polling**: Browser asks the server every 2 seconds '
                                                       "*'Any new messages?'* (Wastes massive bandwidth).\n"
                                                       '* **WebSockets**: A persistent TCP handshake connection '
                                                       'remains open. Whenever an event occurs, server pushes data '
                                                       'instantly to the client with sub-10ms latency!\n'
                                                       '* **Redis**: In-memory key-value data store providing '
                                                       'sub-millisecond query responses, reducing PostgreSQL/MongoDB '
                                                       'load by up to 95%.',
                                   'key_takeaway': 'WebSockets enable instant live streaming and Redis caching '
                                                   'protects primary databases from high-concurrency spikes.'}],
        'visual_explainer': {   'type': 'diagram',
                                'title': 'Real-Time WebSocket & Redis Cache-Aside Flow',
                                'subtitle': 'Client <-> WebSocket Server <-> Redis Cache <-> PostgreSQL Database',
                                'diagram_type': 'websocket_redis_flow'},
        'code_example': {   'title': 'Cache-Aside Pattern with Redis in Node.js',
                            'language': 'javascript',
                            'code': "import { redisClient } from './redis.js';\n"
                                    "import { db } from './postgres.js';\n"
                                    '\n'
                                    'export async function getCachedUserProfile(userId) {\n'
                                    '  const cacheKey = `user:${userId}`;\n'
                                    '  \n'
                                    '  // 1. Check Redis Cache First\n'
                                    '  const cached = await redisClient.get(cacheKey);\n'
                                    '  if (cached) return JSON.parse(cached);\n'
                                    '\n'
                                    '  // 2. Cache Miss: Query Database\n'
                                    "  const user = await db.query('SELECT * FROM users WHERE id = $1', [userId]);\n"
                                    '  \n'
                                    '  // 3. Populate Redis with 1 Hour TTL\n'
                                    '  await redisClient.set(cacheKey, JSON.stringify(user.rows[0]), { EX: 3600 });\n'
                                    '  return user.rows[0];\n'
                                    '}',
                            'explanation': 'Implements the industry-standard Cache-Aside pattern with automatic '
                                           'expiration.',
                            'output_preview': '[Cache HIT: 0.8ms response time]'},
        'quiz_id': 'quiz-web-websockets-realtime-redis-caching',
        'summary': 'You mastered real-time WebSocket communication and Redis distributed in-memory caching.',
        'next_lesson_slug': 'app-viewport-flexbox-layout',
        'prev_lesson_slug': 'web-performance-core-web-vitals'},
    {   'slug': 'app-foundations-native-bridge',
        'course_slug': 'mobile-react-native-foundations',
        'module_id': 'app-mod-1',
        'title': 'Native Bridges & Mobile Primitives: View, Text & Image',
        'order': 1,
        'estimated_minutes': 20,
        'difficulty': 'Beginner',
        'skill_tag': 'mobile_native_bridge',
        'theory_sections': [   {   'title': 'Mobile UI Is Not a Browser Webpage',
                                   'content_markdown': 'In traditional web development, HTML tags like `<div>` and '
                                                       '`<p>` are parsed by browser engines (like Blink or WebKit) '
                                                       'into a DOM tree.\n'
                                                       '\n'
                                                       'In **React Native**, there is no browser DOM. When you write '
                                                       '`<View>`, React Native communicates across the **Native Bridge '
                                                       '(or modern JSI - JavaScript Interface)** to instantiate '
                                                       'genuine native platform views:\n'
                                                       '* On **iOS**: `<View>` creates a native `UIView`.\n'
                                                       '* On **Android**: `<View>` creates a native '
                                                       '`android.view.ViewGroup`.\n'
                                                       '\n'
                                                       'Because your UI is rendered using genuine native platform '
                                                       'widgets, your app achieves buttery smooth 60fps / 120fps '
                                                       'native performance and native accessibility.',
                                   'key_takeaway': 'React Native JSX renders genuine native iOS (UIView) and Android '
                                                   '(ViewGroup) UI components, not browser HTML.'},
                               {   'title': 'Core Mobile Primitives',
                                   'content_markdown': '* **`<View>`**: The fundamental rectangular layout container '
                                                       '(equivalent to `<div>` on web, but defaults to flexbox column '
                                                       'layout).\n'
                                                       '* **`<Text>`**: Must wrap all text strings! In React Native, '
                                                       'plain text strings inside `<View>` will crash the app.\n'
                                                       '* **`<Image>`**: Displays local bundle assets or remote URI '
                                                       'images with caching.\n'
                                                       '* **`<ScrollView>` vs `<FlatList>`**: Use `ScrollView` for '
                                                       'small pages; always use `FlatList` for long lists to enable '
                                                       'lazy view recycling!',
                                   'key_takeaway': 'Always wrap text in <Text> components and use FlatList for '
                                                   'memory-efficient list virtualization.'}],
        'visual_explainer': {   'type': 'architecture_flow',
                                'title': 'React Native Bridge & JSI Architecture',
                                'subtitle': 'JavaScript Thread -> JSI / Bridge -> Native Platform Thread (iOS UIKit / '
                                            'Android Views)',
                                'diagram_type': 'react_native_bridge'},
        'code_example': {   'title': 'Core React Native Primitives & Styling',
                            'language': 'javascript',
                            'code': "import React from 'react';\n"
                                    "import { View, Text, StyleSheet, Image } from 'react-native';\n"
                                    '\n'
                                    'export default function AppProfileCard() {\n'
                                    '  return (\n'
                                    '    <View style={styles.cardContainer}>\n'
                                    '      <Image \n'
                                    '        source={{ uri: '
                                    "'https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=200' }}\n"
                                    '        style={styles.avatar}\n'
                                    '      />\n'
                                    '      <View style={styles.infoWrapper}>\n'
                                    '        <Text style={styles.userName}>Elena Rostova</Text>\n'
                                    '        <Text style={styles.userRole}>Mobile Architect</Text>\n'
                                    '      </View>\n'
                                    '    </View>\n'
                                    '  );\n'
                                    '}\n'
                                    '\n'
                                    'const styles = StyleSheet.create({\n'
                                    '  cardContainer: {\n'
                                    "    flexDirection: 'row',\n"
                                    "    alignItems: 'center',\n"
                                    '    padding: 16,\n'
                                    "    backgroundColor: '#1e293b',\n"
                                    '    borderRadius: 16,\n'
                                    '    borderWidth: 1,\n'
                                    "    borderColor: '#334155',\n"
                                    '  },\n'
                                    '  avatar: {\n'
                                    '    width: 60,\n'
                                    '    height: 60,\n'
                                    '    borderRadius: 30,\n'
                                    '    marginRight: 14,\n'
                                    '  },\n'
                                    '  userName: {\n'
                                    '    fontSize: 18,\n'
                                    "    fontWeight: '700',\n"
                                    "    color: '#f8fafc',\n"
                                    '  },\n'
                                    '  userRole: {\n'
                                    '    fontSize: 14,\n'
                                    "    color: '#94a3b8',\n"
                                    '    marginTop: 2,\n'
                                    '  },\n'
                                    '});',
                            'explanation': 'Demonstrates native primitive composition, StyleSheet creation, and '
                                           'flexbox row alignment.',
                            'output_preview': '[Native Profile Card: Elena Rostova - Mobile Architect]'},
        'quiz_id': 'quiz-app-foundations-native-bridge',
        'summary': 'You learned how React Native uses JSI to render genuine native platform views and mastered core '
                   'mobile primitives.',
        'next_lesson_slug': 'app-viewport-density-safe-area',
        'prev_lesson_slug': 'web-websockets-realtime-redis-caching'},
    {   'slug': 'app-viewport-density-safe-area',
        'course_slug': 'mobile-react-native-foundations',
        'module_id': 'app-mod-2',
        'title': 'Screen Densities, Safe Areas & Dynamic Island Notches',
        'order': 2,
        'estimated_minutes': 20,
        'difficulty': 'Beginner',
        'skill_tag': 'mobile_safe_area',
        'theory_sections': [   {   'title': 'Density-Independent Pixels (dp / pt)',
                                   'content_markdown': 'Smartphones come in vastly different physical sizes and '
                                                       'resolutions, from 320x480 low-density screens to 1440x3120 '
                                                       'ultra-dense OLED displays.\n'
                                                       '\n'
                                                       'If you styled a button to be 50 physical pixels wide:\n'
                                                       '* On an old phone (1x density), 50px is a comfortable '
                                                       'finger-sized button.\n'
                                                       '* On a modern 3x Super Retina OLED phone, 50 physical pixels '
                                                       'would look microscopic (smaller than a pencil tip)!\n'
                                                       '\n'
                                                       'Mobile platforms solve this using **Density-Independent Pixels '
                                                       '(dp in Android, pt in iOS)**. 1 dp/pt automatically scales to '
                                                       '2 physical pixels on a 2x screen and 3 physical pixels on a 3x '
                                                       'screen.',
                                   'key_takeaway': 'React Native numeric units are density-independent points (dp/pt) '
                                                   'that scale across hardware screens.'},
                               {   'title': 'Safe Area Insets & Hardware Notches',
                                   'content_markdown': 'Modern phones have rounded display corners, top sensor notches '
                                                       '/ Dynamic Islands, and bottom gesture home bars.\n'
                                                       '\n'
                                                       'If you render UI at position `(0, 0)`, the clock, battery '
                                                       'icon, and camera notch will physically overlap your title!\n'
                                                       '\n'
                                                       '**`SafeAreaView` (and `react-native-safe-area-context`)** '
                                                       'queries the OS for exact edge insets (top, bottom, left, '
                                                       'right) and dynamically applies padding so your content never '
                                                       'gets cut off.',
                                   'key_takeaway': 'Always wrap root mobile views in SafeAreaProvider and use safe '
                                                   'area insets to avoid hardware cutouts.'}],
        'visual_explainer': {   'type': 'diagram',
                                'title': 'Mobile Viewport Safe Area Boundaries',
                                'subtitle': 'Status Bar & Notch -> Safe Content Area -> Home Indicator Bar',
                                'diagram_type': 'mobile_safe_area'},
        'code_example': {   'title': 'Handling Safe Area Insets with react-native-safe-area-context',
                            'language': 'javascript',
                            'code': "import React from 'react';\n"
                                    "import { View, Text, StyleSheet } from 'react-native';\n"
                                    'import { SafeAreaProvider, useSafeAreaInsets } from '
                                    "'react-native-safe-area-context';\n"
                                    '\n'
                                    'function SafeScreenContent() {\n'
                                    '  const insets = useSafeAreaInsets();\n'
                                    '\n'
                                    '  return (\n'
                                    '    <View style={[\n'
                                    '      styles.container,\n'
                                    '      { paddingTop: insets.top, paddingBottom: insets.bottom }\n'
                                    '    ]}>\n'
                                    '      <View style={styles.header}>\n'
                                    '        <Text style={styles.headerTitle}>AI Learning Lab Mobile</Text>\n'
                                    '      </View>\n'
                                    '      <View style={styles.body}>\n'
                                    '        <Text style={styles.bodyText}>\n'
                                    '          Top Notch Inset: {insets.top}dp | Bottom Bar Inset: {insets.bottom}dp\n'
                                    '        </Text>\n'
                                    '      </View>\n'
                                    '    </View>\n'
                                    '  );\n'
                                    '}\n'
                                    '\n'
                                    'export default function App() {\n'
                                    '  return (\n'
                                    '    <SafeAreaProvider>\n'
                                    '      <SafeScreenContent />\n'
                                    '    </SafeAreaProvider>\n'
                                    '  );\n'
                                    '}\n'
                                    '\n'
                                    'const styles = StyleSheet.create({\n'
                                    "  container: { flex: 1, backgroundColor: '#090d16' },\n"
                                    "  header: { padding: 16, borderBottomWidth: 1, borderColor: '#1e293b' },\n"
                                    "  headerTitle: { fontSize: 20, fontWeight: 'bold', color: '#38bdf8' },\n"
                                    "  body: { padding: 20, flex: 1, justifyContent: 'center', alignItems: 'center' "
                                    '},\n'
                                    "  bodyText: { color: '#94a3b8', fontSize: 14 }\n"
                                    '});',
                            'explanation': 'Uses useSafeAreaInsets hook to calculate exact device hardware boundaries '
                                           'dynamically.',
                            'output_preview': '[Dynamic Island Insets: Top=59dp, Bottom=34dp]'},
        'quiz_id': 'quiz-app-viewport-density-safe-area',
        'summary': 'You mastered density-independent pixels and safe-area hardware notch insets.',
        'next_lesson_slug': 'app-mobile-flexbox-touch-targets',
        'prev_lesson_slug': 'app-foundations-native-bridge'},
    {   'slug': 'app-mobile-flexbox-touch-targets',
        'course_slug': 'mobile-react-native-foundations',
        'module_id': 'app-mod-3',
        'title': 'Mobile Flexbox & Touch Target Ergonomics',
        'order': 3,
        'estimated_minutes': 20,
        'difficulty': 'Beginner',
        'skill_tag': 'mobile_touch_targets',
        'theory_sections': [   {   'title': 'Mobile Flexbox: Column-First Direction',
                                   'content_markdown': 'In standard web CSS, `display: flex` defaults to '
                                                       '`flex-direction: row` (horizontal items).\n'
                                                       '\n'
                                                       'In **React Native**, every `View` is automatically `display: '
                                                       'flex`, but the default is **`flex-direction: column`**!\n'
                                                       '\n'
                                                       'This design reflects mobile screen geometry: smartphones are '
                                                       'vertical portrait screens where content naturally flows '
                                                       'downwards.',
                                   'key_takeaway': 'React Native flexbox defaults to column layout and all dimensions '
                                                   'are unitless numbers.'},
                               {   'title': 'Human Thumb Touch Targets (44x44 dp Rule)',
                                   'content_markdown': 'Unlike desktop mouse pointers that have single-pixel '
                                                       'precision, human thumbs have a contact patch of approximately '
                                                       '7-10mm.\n'
                                                       '\n'
                                                       '* **Apple Human Interface Guidelines (HIG)** require a minimum '
                                                       'touch target size of **44 x 44 pt**.\n'
                                                       '* **Google Material Design** recommends a minimum touch target '
                                                       'of **48 x 48 dp**.\n'
                                                       '\n'
                                                       "If a button is too small or crowded, users experience 'rage "
                                                       "taps' and accidental clicks. Use `hitSlop` in React Native to "
                                                       'expand clickable boundaries without altering visual layout!',
                                   'key_takeaway': 'Ensure interactive buttons have at least 44x44 dp hit areas and '
                                                   'use hitSlop for small icons.'}],
        'visual_explainer': {   'type': 'diagram',
                                'title': 'Touch Target Ergonomics & Hit Slop Expansion',
                                'subtitle': 'Visual Icon (24x24) + HitSlop (+10) = Accessible Thumb Target (44x44)',
                                'diagram_type': 'touch_target'},
        'code_example': {   'title': 'Accessible TouchableOpacity with HitSlop',
                            'language': 'javascript',
                            'code': "import React, { useState } from 'react';\n"
                                    "import { View, Text, TouchableOpacity, StyleSheet } from 'react-native';\n"
                                    '\n'
                                    'export default function AccessibleButtonDemo() {\n'
                                    '  const [count, setCount] = useState(0);\n'
                                    '\n'
                                    '  return (\n'
                                    '    <View style={styles.container}>\n'
                                    '      <Text style={styles.label}>Thumb Taps: {count}</Text>\n'
                                    '      <TouchableOpacity\n'
                                    '        style={styles.primaryButton}\n'
                                    '        activeOpacity={0.7}\n'
                                    '        hitSlop={{ top: 12, bottom: 12, left: 12, right: 12 }}\n'
                                    '        onPress={() => setCount((c) => c + 1)}\n'
                                    '        accessibilityRole="button"\n'
                                    '        accessibilityLabel="Increment counter"\n'
                                    '      >\n'
                                    '        <Text style={styles.buttonText}>+ Tap Target (48dp height)</Text>\n'
                                    '      </TouchableOpacity>\n'
                                    '    </View>\n'
                                    '  );\n'
                                    '}\n'
                                    '\n'
                                    'const styles = StyleSheet.create({\n'
                                    "  container: { padding: 24, alignItems: 'center', backgroundColor: '#0f172a' },\n"
                                    "  label: { fontSize: 18, color: '#f8fafc', marginBottom: 16, fontWeight: '600' "
                                    '},\n'
                                    '  primaryButton: {\n'
                                    '    height: 48,\n'
                                    '    minWidth: 200,\n'
                                    "    backgroundColor: '#ec4899',\n"
                                    '    borderRadius: 24,\n'
                                    "    justifyContent: 'center',\n"
                                    "    alignItems: 'center',\n"
                                    '    paddingHorizontal: 20,\n'
                                    '  },\n'
                                    "  buttonText: { color: '#ffffff', fontWeight: 'bold', fontSize: 16 }\n"
                                    '});',
                            'explanation': 'Implements 48dp minimum button height and hitSlop for comfortable mobile '
                                           'thumb taps.',
                            'output_preview': '[Accessible Mobile Button with 48dp Thumb Area]'},
        'quiz_id': 'quiz-app-mobile-flexbox-touch-targets',
        'summary': 'You mastered mobile flexbox column orientation, touch target accessibility, and hitSlop expansion.',
        'next_lesson_slug': 'app-navigation-stacks-tabs',
        'prev_lesson_slug': 'app-viewport-density-safe-area'},
    {   'slug': 'app-navigation-stacks-tabs',
        'course_slug': 'mobile-navigation-gestures',
        'module_id': 'app-nav-mod-1',
        'title': 'Stack Navigation, Bottom Tab Bars & Deep Links',
        'order': 1,
        'estimated_minutes': 25,
        'difficulty': 'Intermediate',
        'skill_tag': 'mobile_navigation_stacks',
        'theory_sections': [   {   'title': 'Stack Navigation (LIFO Pancake History)',
                                   'content_markdown': 'Mobile navigation differs fundamentally from browser URL '
                                                       'routing.\n'
                                                       '\n'
                                                       'In mobile apps, navigating from a Product List to Product '
                                                       'Details **Pushes** a new screen onto a Last-In-First-Out '
                                                       '(LIFO) stack.\n'
                                                       '* The previous screen remains mounted in memory with its '
                                                       'scroll position intact.\n'
                                                       '* Tapping the Back button or swiping from the left screen edge '
                                                       '**Pops** the top screen off the stack, seamlessly revealing '
                                                       'the previous list.',
                                   'key_takeaway': 'Stack navigators maintain screen state and scroll positions when '
                                                   'pushing and popping views.'},
                               {   'title': 'Bottom Tabs & Deep Linking',
                                   'content_markdown': '**Bottom Tab Navigators** represent the primary top-level hubs '
                                                       'of a mobile app (e.g. Home, Search, Library, Profile).\n'
                                                       '\n'
                                                       '**Deep Linking** allows external links (like '
                                                       '`myapp://course/react-native` or HTTPS Universal Links) to '
                                                       'open your app and immediately navigate deep into a nested '
                                                       'stack screen.',
                                   'key_takeaway': 'Combine bottom tab bars for root navigation with nested stack '
                                                   'navigators for detail drill-downs.'}],
        'visual_explainer': {   'type': 'diagram',
                                'title': 'Nested Navigation Architecture',
                                'subtitle': 'Root Bottom Tabs -> Nested Feature Stacks (Push / Pop)',
                                'diagram_type': 'nav_stack'},
        'code_example': {   'title': 'Configuring React Navigation 6 with Stack and Tabs',
                            'language': 'javascript',
                            'code': "import React from 'react';\n"
                                    "import { createBottomTabNavigator } from '@react-navigation/bottom-tabs';\n"
                                    "import { createNativeStackNavigator } from '@react-navigation/native-stack';\n"
                                    '\n'
                                    'const Tab = createBottomTabNavigator();\n'
                                    'const Stack = createNativeStackNavigator();\n'
                                    '\n'
                                    'function CoursesStackNavigator() {\n'
                                    '  return (\n'
                                    '    <Stack.Navigator screenOptions={{ headerBackTitleVisible: false }}>\n'
                                    '      <Stack.Screen name="CourseList" component={CourseListScreen} options={{ '
                                    "title: 'Courses' }} />\n"
                                    '      <Stack.Screen name="CourseDetail" component={CourseDetailScreen} options={{ '
                                    "title: 'Lesson View' }} />\n"
                                    '    </Stack.Navigator>\n'
                                    '  );\n'
                                    '}\n'
                                    '\n'
                                    'export function RootAppNavigation() {\n'
                                    '  return (\n'
                                    "    <Tab.Navigator screenOptions={{ tabBarActiveTintColor: '#f43f5e' }}>\n"
                                    '      <Tab.Screen name="Learn" component={CoursesStackNavigator} options={{ '
                                    'headerShown: false }} />\n'
                                    '      <Tab.Screen name="Profile" component={ProfileScreen} />\n'
                                    '    </Tab.Navigator>\n'
                                    '  );\n'
                                    '}',
                            'explanation': 'Demonstrates nesting a native stack navigator inside a bottom tab '
                                           'navigator with header options.',
                            'output_preview': '[Root Navigation: Learn Tab (with nested Stack) | Profile Tab]'},
        'quiz_id': 'quiz-app-navigation-stacks-tabs',
        'summary': 'You mastered stack screen lifecycles, bottom tab navigation, and deep linking architectures.',
        'next_lesson_slug': 'app-gestures-pan-swipe-pinch',
        'prev_lesson_slug': 'app-mobile-flexbox-touch-targets'},
    {   'slug': 'app-gestures-pan-swipe-pinch',
        'course_slug': 'mobile-navigation-gestures',
        'module_id': 'app-nav-mod-2',
        'title': 'Continuous Pan Gestures, Swipes & Multi-Touch Pinch',
        'order': 2,
        'estimated_minutes': 25,
        'difficulty': 'Intermediate',
        'skill_tag': 'mobile_gestures',
        'theory_sections': [   {   'title': 'The Native Gesture Engine',
                                   'content_markdown': 'Handling smooth touch gestures in JavaScript can lead to '
                                                       'dropped frames because touch events have to cross the bridge '
                                                       'on every touchmove event.\n'
                                                       '\n'
                                                       '**React Native Gesture Handler (RNGH)** runs gesture '
                                                       'recognition directly on the OS native UI thread (`UIKit` on '
                                                       'iOS and `View` gesture recognizers on Android):\n'
                                                       '* **PanGesture**: Tracks continuous X/Y thumb dragging with '
                                                       'velocity tracking.\n'
                                                       '* **Fling/Swipe**: Recognizes directional flicks.\n'
                                                       '* **PinchGesture**: Tracks two-finger scale transforms for '
                                                       'photo zooming.',
                                   'key_takeaway': 'RNGH runs touch recognition directly on native threads to prevent '
                                                   'lag during fast drags.'}],
        'visual_explainer': {   'type': 'diagram',
                                'title': 'Native UI Thread Gesture Handling Flow',
                                'subtitle': 'Touch Event -> Native Gesture Recognizer -> Direct Transform (0 Bridge '
                                            'Overhead)',
                                'diagram_type': 'gesture_flow'},
        'code_example': {   'title': 'Interactive Pan Gesture with react-native-gesture-handler',
                            'language': 'javascript',
                            'code': "import React from 'react';\n"
                                    "import { View, StyleSheet } from 'react-native';\n"
                                    'import { GestureDetector, Gesture, GestureHandlerRootView } from '
                                    "'react-native-gesture-handler';\n"
                                    'import Animated, { useSharedValue, useAnimatedStyle } from '
                                    "'react-native-reanimated';\n"
                                    '\n'
                                    'export default function SwipeableCard() {\n'
                                    '  const translationX = useSharedValue(0);\n'
                                    '\n'
                                    '  const panGesture = Gesture.Pan()\n'
                                    '    .onUpdate((event) => {\n'
                                    '      translationX.value = event.translationX;\n'
                                    '    })\n'
                                    '    .onEnd(() => {\n'
                                    '      translationX.value = 0; // Return to origin\n'
                                    '    });\n'
                                    '\n'
                                    '  const animatedStyle = useAnimatedStyle(() => ({\n'
                                    '    transform: [{ translateX: translationX.value }],\n'
                                    '  }));\n'
                                    '\n'
                                    '  return (\n'
                                    '    <GestureHandlerRootView style={styles.container}>\n'
                                    '      <GestureDetector gesture={panGesture}>\n'
                                    '        <Animated.View style={[styles.card, animatedStyle]} />\n'
                                    '      </GestureDetector>\n'
                                    '    </GestureHandlerRootView>\n'
                                    '  );\n'
                                    '}\n'
                                    '\n'
                                    'const styles = StyleSheet.create({\n'
                                    "  container: { flex: 1, justifyContent: 'center', alignItems: 'center' },\n"
                                    "  card: { width: 280, height: 160, backgroundColor: '#f43f5e', borderRadius: 20 "
                                    '}\n'
                                    '});',
                            'explanation': 'Binds a native Pan gesture to shared animated transform coordinates.',
                            'output_preview': '[Interactive Drag Card with zero-latency touch response]'},
        'quiz_id': 'quiz-app-gestures-pan-swipe-pinch',
        'summary': 'You mastered native pan gestures, multi-touch pinch recognizers, and velocity tracking.',
        'next_lesson_slug': 'app-reanimated-60fps-physics',
        'prev_lesson_slug': 'app-navigation-stacks-tabs'},
    {   'slug': 'app-reanimated-60fps-physics',
        'course_slug': 'mobile-navigation-gestures',
        'module_id': 'app-nav-mod-3',
        'title': 'Reanimated 3, Worklets & 60fps Spring Physics',
        'order': 3,
        'estimated_minutes': 25,
        'difficulty': 'Intermediate',
        'skill_tag': 'mobile_reanimated',
        'theory_sections': [   {   'title': 'Worklets: Running JavaScript on the UI Thread',
                                   'content_markdown': 'Normally, JavaScript code runs on a single JS thread. If a '
                                                       'complex data calculation blocks the JS thread for 50ms, a '
                                                       'traditional JS animation will stutter.\n'
                                                       '\n'
                                                       '**Reanimated 3 introduces Worklets** — tiny JavaScript '
                                                       'functions compiled to execute synchronously inside the native '
                                                       'UI rendering thread (Hermes runtime on UI thread)!\n'
                                                       '\n'
                                                       'Animations update frame-by-frame on the GPU without any bridge '
                                                       'communication.',
                                   'key_takeaway': 'Worklets execute directly on the UI thread to guarantee 60fps / '
                                                   '120fps fluid animations.'},
                               {   'title': 'Spring Physics vs Cubic Bézier Timing',
                                   'content_markdown': 'Linear or bezier easing often feels robotic. Real physical '
                                                       'objects have mass, friction, and tension.\n'
                                                       '\n'
                                                       "`withSpring` models physical Hooke's Law dynamics:\n"
                                                       '* **Damping**: How quickly the bounce settles.\n'
                                                       '* **Stiffness**: How snappy the spring reacts.\n'
                                                       '* **Mass**: Heaviness of the bouncing object.',
                                   'key_takeaway': 'Use withSpring for organic, snappy mobile micro-interactions that '
                                                   'feel natural.'}],
        'visual_explainer': {   'type': 'diagram',
                                'title': 'Spring Physics Oscillation Curve',
                                'subtitle': 'Displacement -> Overshoot -> Damped Oscillation -> Equilibrium',
                                'diagram_type': 'spring_physics'},
        'code_example': {   'title': 'Smooth 60fps Spring Physics with Reanimated 3',
                            'language': 'javascript',
                            'code': "import React from 'react';\n"
                                    "import { View, Button, StyleSheet } from 'react-native';\n"
                                    'import Animated, { useSharedValue, useAnimatedStyle, withSpring } from '
                                    "'react-native-reanimated';\n"
                                    '\n'
                                    'export default function BouncyModal() {\n'
                                    '  const scale = useSharedValue(0);\n'
                                    '\n'
                                    '  const handleOpen = () => {\n'
                                    '    scale.value = withSpring(1, { damping: 12, stiffness: 100 });\n'
                                    '  };\n'
                                    '\n'
                                    '  const handleClose = () => {\n'
                                    '    scale.value = withSpring(0, { damping: 15, stiffness: 120 });\n'
                                    '  };\n'
                                    '\n'
                                    '  const animatedStyle = useAnimatedStyle(() => ({\n'
                                    '    transform: [{ scale: scale.value }],\n'
                                    '    opacity: scale.value,\n'
                                    '  }));\n'
                                    '\n'
                                    '  return (\n'
                                    '    <View style={styles.container}>\n'
                                    '      <Animated.View style={[styles.modalBox, animatedStyle]} />\n'
                                    '      <View style={styles.buttonRow}>\n'
                                    '        <Button title="Open Spring Modal" onPress={handleOpen} color="#f43f5e" '
                                    '/>\n'
                                    '        <Button title="Close" onPress={handleClose} color="#64748b" />\n'
                                    '      </View>\n'
                                    '    </View>\n'
                                    '  );\n'
                                    '}\n'
                                    '\n'
                                    'const styles = StyleSheet.create({\n'
                                    "  container: { flex: 1, justifyContent: 'center', alignItems: 'center' },\n"
                                    "  modalBox: { width: 220, height: 220, backgroundColor: '#8b5cf6', borderRadius: "
                                    '24, marginBottom: 20 },\n'
                                    "  buttonRow: { flexDirection: 'row', gap: 12 }\n"
                                    '});',
                            'explanation': 'Demonstrates Reanimated 3 shared values with spring physics '
                                           'configurations.',
                            'output_preview': '[Bouncy Modal: Scale 0 -> 1 with snappy spring overshoot]'},
        'quiz_id': 'quiz-app-reanimated-60fps-physics',
        'summary': 'You mastered Reanimated 3 worklets, shared values, and physics-driven spring animations.',
        'next_lesson_slug': 'app-offline-first-mmkv-storage',
        'prev_lesson_slug': 'app-gestures-pan-swipe-pinch'},
    {   'slug': 'app-offline-first-mmkv-storage',
        'course_slug': 'mobile-storage-device-apis',
        'module_id': 'app-api-mod-1',
        'title': 'Offline-First Architecture & MMKV Ultra-Fast Storage',
        'order': 1,
        'estimated_minutes': 25,
        'difficulty': 'Intermediate',
        'skill_tag': 'mobile_mmkv_storage',
        'theory_sections': [   {   'title': 'Why Mobile Apps Must Be Offline-First',
                                   'content_markdown': 'Mobile users constantly pass through subway tunnels, flight '
                                                       'airplane modes, and weak elevator signals.\n'
                                                       '\n'
                                                       'An app that displays an infinite loading spinner or white '
                                                       'screen when offline will be immediately uninstalled.\n'
                                                       '\n'
                                                       '**The Offline-First Rule**:\n'
                                                       '1. **Read from Local Cache First**: Render stored local state '
                                                       'instantly (0ms load time).\n'
                                                       '2. **Fetch in Background**: Make network requests '
                                                       'asynchronously.\n'
                                                       '3. **Optimistically Mutate**: Update the UI immediately when '
                                                       'the user likes or edits an item, then sync the change to the '
                                                       'backend queue.',
                                   'key_takeaway': 'Always render local cache on startup and mutate UI optimistically '
                                                   'before network confirmation.'},
                               {   'title': 'AsyncStorage vs Tencent MMKV',
                                   'content_markdown': '* **AsyncStorage**: Serializes strings across the async bridge '
                                                       'and writes to disk via SQLite/SharedPreferences (~30ms '
                                                       'latency).\n'
                                                       '* **MMKV (Memory-Mapped Key-Value)**: Uses C++ `mmap` to map '
                                                       'memory directly to files. Read and write operations execute in '
                                                       '**sub-millisecond (< 0.1ms) synchronous speeds** directly '
                                                       'through JSI!',
                                   'key_takeaway': 'MMKV provides 30x faster synchronous key-value storage using '
                                                   'memory-mapped C++ files.'}],
        'visual_explainer': {   'type': 'diagram',
                                'title': 'Offline-First Sync Engine Architecture',
                                'subtitle': 'UI <-> MMKV Fast Cache (Instant) <-> Background Sync Worker <-> Cloud API',
                                'diagram_type': 'offline_sync'},
        'code_example': {   'title': 'Synchronous State Caching with react-native-mmkv',
                            'language': 'javascript',
                            'code': "import { MMKV } from 'react-native-mmkv';\n"
                                    '\n'
                                    'export const storage = new MMKV();\n'
                                    '\n'
                                    '// 1. Synchronous ultra-fast writes (0.05ms)\n'
                                    'export function cacheUserProfile(user) {\n'
                                    "  storage.set('user.profile', JSON.stringify(user));\n"
                                    "  storage.set('user.isLoggedIn', true);\n"
                                    "  storage.set('user.theme', 'dark');\n"
                                    '}\n'
                                    '\n'
                                    '// 2. Synchronous reads on app launch (No await required!)\n'
                                    'export function loadCachedUser() {\n'
                                    "  const jsonString = storage.getString('user.profile');\n"
                                    '  if (!jsonString) return null;\n'
                                    '  return JSON.parse(jsonString);\n'
                                    '}\n'
                                    '\n'
                                    "console.log('Synchronous Cached User:', loadCachedUser());",
                            'explanation': 'Illustrates synchronous MMKV reading and writing with zero bridge latency.',
                            'output_preview': "Synchronous Cached User: { name: 'Elena Rostova', tier: 'Pro' }"},
        'quiz_id': 'quiz-app-offline-first-mmkv-storage',
        'summary': 'You mastered offline-first mobile architecture and ultra-fast synchronous MMKV persistence.',
        'next_lesson_slug': 'app-sqlite-local-relational-db',
        'prev_lesson_slug': 'app-reanimated-60fps-physics'},
    {   'slug': 'app-sqlite-local-relational-db',
        'course_slug': 'mobile-storage-device-apis',
        'module_id': 'app-api-mod-2',
        'title': 'Embedded SQLite & Local Relational Queries on Mobile',
        'order': 2,
        'estimated_minutes': 25,
        'difficulty': 'Intermediate',
        'skill_tag': 'mobile_sqlite',
        'theory_sections': [   {   'title': 'When Key-Value Storage Is Not Enough',
                                   'content_markdown': 'If your app stores 10,000 chat messages, song tracks, or '
                                                       'offline catalog items, storing them as a huge JSON string in '
                                                       'MMKV requires parsing a 50MB string into memory every time the '
                                                       'app opens.\n'
                                                       '\n'
                                                       '**SQLite** is an embedded relational C-database running '
                                                       'directly inside iOS and Android:\n'
                                                       '* Supports indexed `SELECT`, `JOIN`, and `WHERE` filtering.\n'
                                                       '* Enables pagination with `LIMIT` and `OFFSET` without loading '
                                                       'the whole table into RAM.\n'
                                                       '* Provides ACID transactions to guarantee data integrity '
                                                       'during unexpected app termination.',
                                   'key_takeaway': 'Use embedded SQLite to index, query, and paginate thousands of '
                                                   'local records efficiently.'}],
        'visual_explainer': {   'type': 'diagram',
                                'title': 'Embedded Mobile SQLite Query Engine',
                                'subtitle': 'Mobile App UI -> SQLite C Engine (Indexed B-Tree) -> Encrypted DB File',
                                'diagram_type': 'sqlite_mobile'},
        'code_example': {   'title': 'Local SQLite Database Setup with expo-sqlite / op-sqlite',
                            'language': 'javascript',
                            'code': "import * as SQLite from 'expo-sqlite';\n"
                                    '\n'
                                    "const db = SQLite.openDatabaseSync('learning_lab.db');\n"
                                    '\n'
                                    '// 1. Initialize schema\n'
                                    'db.execSync(`\n'
                                    '  CREATE TABLE IF NOT EXISTS lessons (\n'
                                    '    id INTEGER PRIMARY KEY AUTOINCREMENT,\n'
                                    '    slug TEXT UNIQUE,\n'
                                    '    title TEXT,\n'
                                    '    is_completed INTEGER DEFAULT 0\n'
                                    '  );\n'
                                    '`);\n'
                                    '\n'
                                    '// 2. Perform insert transaction\n'
                                    "db.runSync('INSERT OR REPLACE INTO lessons (slug, title, is_completed) VALUES (?, "
                                    "?, ?)', [\n"
                                    "  'app-offline-first',\n"
                                    "  'Offline First Architecture',\n"
                                    '  1\n'
                                    ']);\n'
                                    '\n'
                                    '// 3. Fast indexed query\n'
                                    "const completedLessons = db.getAllSync('SELECT * FROM lessons WHERE is_completed "
                                    "= 1');\n"
                                    "console.log('Completed Lessons from Local SQLite:', completedLessons);",
                            'explanation': 'Executes local SQLite table creation, parameterized queries, and record '
                                           'retrieval.',
                            'output_preview': 'Completed Lessons from Local SQLite: [{ id: 1, slug: '
                                              "'app-offline-first', is_completed: 1 }]"},
        'quiz_id': 'quiz-app-sqlite-local-relational-db',
        'summary': 'You mastered embedded mobile SQLite schemas, ACID transactions, and indexed relational queries.',
        'next_lesson_slug': 'app-device-hardware-camera-location',
        'prev_lesson_slug': 'app-offline-first-mmkv-storage'},
    {   'slug': 'app-device-hardware-camera-location',
        'course_slug': 'mobile-storage-device-apis',
        'module_id': 'app-api-mod-3',
        'title': 'Camera, Biometrics (FaceID) & Hardware Permissions',
        'order': 3,
        'estimated_minutes': 25,
        'difficulty': 'Intermediate',
        'skill_tag': 'mobile_native_hardware',
        'theory_sections': [   {   'title': 'OS Runtime Permission Lifecycles',
                                   'content_markdown': 'Mobile operating systems strictly isolate sensitive hardware '
                                                       '(Camera, Microphone, GPS Location, Photo Gallery, Contacts).\n'
                                                       '\n'
                                                       'On iOS and Android:\n'
                                                       '1. You must declare permissions in `Info.plist` (iOS) and '
                                                       '`AndroidManifest.xml` (Android) with a clear human rationale '
                                                       'string.\n'
                                                       '2. You must request **runtime permission** just in time when '
                                                       "the user initiates the action (e.g. tapping 'Take Photo').\n"
                                                       '3. If the user permanently denies permission, you must '
                                                       'gracefully direct them to OS Settings.',
                                   'key_takeaway': 'Request hardware permissions just-in-time and handle denied '
                                                   'permission fallbacks gracefully.'},
                               {   'title': 'Biometric Authentication: FaceID & TouchID',
                                   'content_markdown': 'Using `expo-local-authentication` or '
                                                       '`react-native-biometrics`, apps can authenticate users via '
                                                       'Apple FaceID or Android BiometricPrompt with cryptographic '
                                                       'Secure Enclave protection.',
                                   'key_takeaway': 'Biometric authentication secures local tokens using hardware '
                                                   'Secure Enclave coprocessors.'}],
        'visual_explainer': {   'type': 'diagram',
                                'title': 'Biometric Authentication Security Flow',
                                'subtitle': 'App Prompt -> iOS Secure Enclave (FaceID) -> Cryptographic Token Release',
                                'diagram_type': 'biometric_auth'},
        'code_example': {   'title': 'Authenticating with Apple FaceID / Android Biometrics',
                            'language': 'javascript',
                            'code': "import * as LocalAuthentication from 'expo-local-authentication';\n"
                                    '\n'
                                    'export async function authenticateWithBiometrics() {\n'
                                    '  // 1. Check if hardware sensor is available\n'
                                    '  const hasHardware = await LocalAuthentication.hasHardwareAsync();\n'
                                    '  const isEnrolled = await LocalAuthentication.isEnrolledAsync();\n'
                                    '\n'
                                    '  if (!hasHardware || !isEnrolled) {\n'
                                    "    return { success: false, reason: 'Biometrics unavailable' };\n"
                                    '  }\n'
                                    '\n'
                                    '  // 2. Prompt FaceID / Fingerprint dialog\n'
                                    '  const authResult = await LocalAuthentication.authenticateAsync({\n'
                                    "    promptMessage: 'Unlock AI Learning Lab Secure Vault',\n"
                                    "    fallbackLabel: 'Use Passcode',\n"
                                    '  });\n'
                                    '\n'
                                    '  if (authResult.success) {\n'
                                    "    console.log('User authenticated successfully via FaceID!');\n"
                                    '  }\n'
                                    '  return authResult;\n'
                                    '}',
                            'explanation': 'Prompts native FaceID authentication dialog with hardware enrollment '
                                           'verification.',
                            'output_preview': '[FaceID Prompt: Unlock AI Learning Lab Secure Vault -> Success]'},
        'quiz_id': 'quiz-app-device-hardware-camera-location',
        'summary': 'You mastered OS runtime permissions, camera access, and FaceID biometric authentication.',
        'next_lesson_slug': 'app-flutter-widget-tree-rendering',
        'prev_lesson_slug': 'app-sqlite-local-relational-db'},
    {   'slug': 'app-flutter-widget-tree-rendering',
        'course_slug': 'flutter-dart-engineering',
        'module_id': 'flutter-mod-1',
        'title': 'Flutter Architecture, Impeller Engine & The Widget Tree',
        'order': 1,
        'estimated_minutes': 25,
        'difficulty': 'Intermediate',
        'skill_tag': 'flutter_widget_tree',
        'theory_sections': [   {   'title': "Flutter's Render-Own-Pixels Architecture",
                                   'content_markdown': 'Unlike React Native which wraps native OEM widgets, **Google '
                                                       'Flutter paints every single pixel directly onto a Skia / '
                                                       'Impeller canvas** at 120fps.\n'
                                                       '\n'
                                                       '* **Ahead-Of-Time (AOT) Compiled**: Dart code compiles '
                                                       'directly into ARM64 machine assembly code with no runtime '
                                                       'bridge interpreter.\n'
                                                       '* **Impeller Engine**: Pre-compiles all shaders to eliminate '
                                                       'runtime shader compilation jank on iOS and Android.',
                                   'key_takeaway': 'Flutter compiles directly to native ARM machine code and renders '
                                                   'its own widget pixels via Impeller.'},
                               {   'title': "The 'Everything Is a Widget' Paradigm",
                                   'content_markdown': 'In Flutter, layout, styling, text, animation, and structural '
                                                       'components are all **Widgets**:\n'
                                                       '* `Container`, `Padding`, `Center`: Layout widgets.\n'
                                                       '* `Row`, `Column`, `Stack`: Multi-child alignment widgets.\n'
                                                       '* `StatelessWidget`: Immutable widgets whose configuration '
                                                       'never changes over time.',
                                   'key_takeaway': 'Flutter UI is composed as a declarative tree of immutable widget '
                                                   'nodes.'}],
        'visual_explainer': {   'type': 'diagram',
                                'title': 'Flutter Impeller Rendering Pipeline',
                                'subtitle': 'Dart Code -> Widget Tree -> Render Objects -> Impeller Vulkan/Metal '
                                            'Canvas',
                                'diagram_type': 'flutter_rendering'},
        'code_example': {   'title': 'Clean Flutter StatelessWidget Composition in Dart',
                            'language': 'dart',
                            'code': "import 'package:flutter/material.dart';\n"
                                    '\n'
                                    'class CourseBadgeWidget extends StatelessWidget {\n'
                                    '  final String title;\n'
                                    '  final String level;\n'
                                    '\n'
                                    '  const CourseBadgeWidget({\n'
                                    '    super.key,\n'
                                    '    required this.title,\n'
                                    '    required this.level,\n'
                                    '  });\n'
                                    '\n'
                                    '  @override\n'
                                    '  Widget build(BuildContext context) {\n'
                                    '    return Container(\n'
                                    '      padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 12),\n'
                                    '      decoration: BoxDecoration(\n'
                                    '        color: const Color(0xFF0F172A),\n'
                                    '        borderRadius: BorderRadius.circular(16),\n'
                                    '        border: Border.all(color: const Color(0xFF0284C7), width: 1.5),\n'
                                    '      ),\n'
                                    '      child: Row(\n'
                                    '        mainAxisSize: MainAxisSize.min,\n'
                                    '        children: [\n'
                                    '          const Icon(Icons.bolt, color: Color(0xFF38BDF8)),\n'
                                    '          const SizedBox(width: 8),\n'
                                    '          Text(\n'
                                    "            '$title ($level)',\n"
                                    '            style: const TextStyle(color: Colors.white, fontWeight: '
                                    'FontWeight.bold),\n'
                                    '          ),\n'
                                    '        ],\n'
                                    '      ),\n'
                                    '    );\n'
                                    '  }\n'
                                    '}',
                            'explanation': 'Builds a custom immutable Flutter widget composed of Container, Row, Icon, '
                                           'and Text.',
                            'output_preview': '[Flutter Widget: ⚡ React Native & Mobile (Intermediate)]'},
        'quiz_id': 'quiz-app-flutter-widget-tree-rendering',
        'summary': "You mastered Flutter's Impeller rendering engine, AOT machine compilation, and declarative widget "
                   'trees.',
        'next_lesson_slug': 'app-flutter-stateful-lifecycle',
        'prev_lesson_slug': 'app-device-hardware-camera-location'},
    {   'slug': 'app-flutter-stateful-lifecycle',
        'course_slug': 'flutter-dart-engineering',
        'module_id': 'flutter-mod-2',
        'title': 'StatefulWidget Lifecycles & Reactive setState',
        'order': 2,
        'estimated_minutes': 25,
        'difficulty': 'Intermediate',
        'skill_tag': 'flutter_state_lifecycle',
        'theory_sections': [   {   'title': 'StatefulWidget Lifecycle Stages',
                                   'content_markdown': 'A `StatefulWidget` creates a persistent `State` object that '
                                                       'lives across rebuilds:\n'
                                                       '1. **`initState()`**: Called exactly once when the widget '
                                                       'enters the tree. Used for subscribing to streams, starting '
                                                       'animations, and fetching data.\n'
                                                       '2. **`build(context)`**: Called whenever `setState()` is '
                                                       'invoked to recalculate the widget sub-tree.\n'
                                                       '3. **`didUpdateWidget()`**: Triggered when the parent widget '
                                                       'passes updated configuration props.\n'
                                                       '4. **`dispose()`**: Called when the widget is permanently '
                                                       'removed from the tree. You **must cancel stream subscriptions '
                                                       'and dispose AnimationControllers** to avoid memory leaks!',
                                   'key_takeaway': 'Always clean up controllers and listeners inside dispose() to '
                                                   'prevent memory leaks.'}],
        'visual_explainer': {   'type': 'diagram',
                                'title': 'Flutter StatefulWidget Lifecycle Sequence',
                                'subtitle': 'createState() -> initState() -> build() <-> setState() -> dispose()',
                                'diagram_type': 'flutter_lifecycle'},
        'code_example': {   'title': 'Flutter StatefulWidget with Lifecycle Hooks',
                            'language': 'dart',
                            'code': "import 'package:flutter/material.dart';\n"
                                    '\n'
                                    'class InteractiveCounter extends StatefulWidget {\n'
                                    '  const InteractiveCounter({super.key});\n'
                                    '\n'
                                    '  @override\n'
                                    '  State<InteractiveCounter> createState() => _InteractiveCounterState();\n'
                                    '}\n'
                                    '\n'
                                    'class _InteractiveCounterState extends State<InteractiveCounter> {\n'
                                    '  int _counter = 0;\n'
                                    '\n'
                                    '  @override\n'
                                    '  void initState() {\n'
                                    '    super.initState();\n'
                                    "    print('Counter widget initialized');\n"
                                    '  }\n'
                                    '\n'
                                    '  void _increment() {\n'
                                    '    setState(() {\n'
                                    '      _counter++;\n'
                                    '    });\n'
                                    '  }\n'
                                    '\n'
                                    '  @override\n'
                                    '  void dispose() {\n'
                                    "    print('Counter widget disposed safely');\n"
                                    '    super.dispose();\n'
                                    '  }\n'
                                    '\n'
                                    '  @override\n'
                                    '  Widget build(BuildContext context) {\n'
                                    '    return ElevatedButton(\n'
                                    '      onPressed: _increment,\n'
                                    "      child: Text('Tapped: $_counter times'),\n"
                                    '    );\n'
                                    '  }\n'
                                    '}',
                            'explanation': 'Illustrates initState, setState trigger, build invocation, and dispose '
                                           'cleanup.',
                            'output_preview': '[ElevatedButton: Tapped: 1 times]'},
        'quiz_id': 'quiz-app-flutter-stateful-lifecycle',
        'summary': 'You mastered StatefulWidget lifecycles, setState reactive updates, and memory cleanup with '
                   'dispose.',
        'next_lesson_slug': 'app-flutter-bloc-state-streams',
        'prev_lesson_slug': 'app-flutter-widget-tree-rendering'},
    {   'slug': 'app-flutter-bloc-state-streams',
        'course_slug': 'flutter-dart-engineering',
        'module_id': 'flutter-mod-3',
        'title': 'BLoC Architecture & Reactive Dart Streams',
        'order': 3,
        'estimated_minutes': 25,
        'difficulty': 'Intermediate',
        'skill_tag': 'flutter_bloc_pattern',
        'theory_sections': [   {   'title': 'Business Logic Component (BLoC) Pattern',
                                   'content_markdown': 'In large enterprise Flutter applications, putting business '
                                                       'logic inside UI widget classes makes code hard to test and '
                                                       'maintain.\n'
                                                       '\n'
                                                       '**The BLoC Pattern separates UI from Business Logic '
                                                       'completely**:\n'
                                                       '* **Events**: Dispatched by UI buttons (e.g. '
                                                       '`LoadCoursesEvent`, `FilterTrackEvent`).\n'
                                                       '* **BLoC**: Receives Events, performs async network calls or '
                                                       'computations, and emits States.\n'
                                                       '* **States**: Consumed by `BlocBuilder` widgets to re-render '
                                                       'UI declaratively (`CoursesLoadingState`, `CoursesLoadedState`, '
                                                       '`CoursesErrorState`).',
                                   'key_takeaway': 'BLoC transforms incoming Events into outgoing States using '
                                                   'unidirectional reactive streams.'}],
        'visual_explainer': {   'type': 'diagram',
                                'title': 'Flutter BLoC Unidirectional Event-State Flow',
                                'subtitle': 'UI Widgets -> [Event Sink] -> BLoC Engine -> [State Stream] -> '
                                            'BlocBuilder UI',
                                'diagram_type': 'bloc_flow'},
        'code_example': {   'title': 'Flutter BLoC Implementation in Dart',
                            'language': 'dart',
                            'code': "import 'package:flutter_bloc/flutter_bloc.dart';\n"
                                    '\n'
                                    '// 1. Events\n'
                                    'abstract class CourseEvent {}\n'
                                    'class FetchCoursesEvent extends CourseEvent {}\n'
                                    '\n'
                                    '// 2. States\n'
                                    'abstract class CourseState {}\n'
                                    'class CourseLoading extends CourseState {}\n'
                                    'class CourseLoaded extends CourseState {\n'
                                    '  final List<String> courses;\n'
                                    '  CourseLoaded(this.courses);\n'
                                    '}\n'
                                    '\n'
                                    '// 3. BLoC Handler\n'
                                    'class CourseBloc extends Bloc<CourseEvent, CourseState> {\n'
                                    '  CourseBloc() : super(CourseLoading()) {\n'
                                    '    on<FetchCoursesEvent>((event, emit) async {\n'
                                    '      emit(CourseLoading());\n'
                                    '      // Simulate backend async fetch\n'
                                    '      await Future.delayed(const Duration(milliseconds: 500));\n'
                                    "      emit(CourseLoaded(['React Native Foundations', 'Flutter Architecture', "
                                    "'SQLite APIs']));\n"
                                    '    });\n'
                                    '  }\n'
                                    '}',
                            'explanation': 'Defines typed Events, States, and an Event-to-State emitter handler.',
                            'output_preview': '[CourseBloc emitted CourseLoaded with 3 mobile courses]'},
        'quiz_id': 'quiz-app-flutter-bloc-state-streams',
        'summary': 'You mastered BLoC architecture, unidirectional event streams, and reactive state separation in '
                   'Flutter.',
        'next_lesson_slug': 'app-push-notifications-fcm-apns',
        'prev_lesson_slug': 'app-flutter-stateful-lifecycle'},
    {   'slug': 'app-push-notifications-fcm-apns',
        'course_slug': 'mobile-production-app-stores',
        'module_id': 'app-prod-mod-1',
        'title': 'Push Notifications: FCM, Apple APNs & Device Tokens',
        'order': 1,
        'estimated_minutes': 25,
        'difficulty': 'Advanced',
        'skill_tag': 'mobile_push_notifications',
        'theory_sections': [   {   'title': 'How Remote Push Notifications Work',
                                   'content_markdown': 'Mobile apps cannot keep continuous TCP sockets open 24/7 '
                                                       'because the OS would kill the app to save battery.\n'
                                                       '\n'
                                                       'Instead, Apple and Google operate centralized push servers:\n'
                                                       '* **Apple APNs (Apple Push Notification service)**\n'
                                                       '* **Google FCM (Firebase Cloud Messaging)**\n'
                                                       '\n'
                                                       '**Lifecycle**:\n'
                                                       '1. App boots up and registers with APNs/FCM to receive a '
                                                       'unique **Device Push Token**.\n'
                                                       '2. App sends this token to your backend database.\n'
                                                       '3. When an event occurs (e.g. new message), your backend sends '
                                                       'an HTTP/2 payload to APNs/FCM, which wakes up the physical '
                                                       'device and presents the notification banner!',
                                   'key_takeaway': 'Your backend notifies Apple/Google push servers using unique '
                                                   'device tokens to wake up phones.'}],
        'visual_explainer': {   'type': 'diagram',
                                'title': 'Remote Push Notification Delivery Lifecycle',
                                'subtitle': 'Backend Server -> FCM / APNs Gateway -> Cellular Wakeup -> Device '
                                            'Notification Tray',
                                'diagram_type': 'push_notification_flow'},
        'code_example': {   'title': 'Registering for Push Tokens with Expo Notifications',
                            'language': 'javascript',
                            'code': "import * as Notifications from 'expo-notifications';\n"
                                    "import * as Device from 'expo-device';\n"
                                    '\n'
                                    'export async function registerForPushNotificationsAsync() {\n'
                                    '  if (!Device.isDevice) {\n'
                                    "    console.log('Push notifications require a physical device');\n"
                                    '    return null;\n'
                                    '  }\n'
                                    '\n'
                                    '  const { status: existingStatus } = await Notifications.getPermissionsAsync();\n'
                                    '  let finalStatus = existingStatus;\n'
                                    '\n'
                                    "  if (existingStatus !== 'granted') {\n"
                                    '    const { status } = await Notifications.requestPermissionsAsync();\n'
                                    '    finalStatus = status;\n'
                                    '  }\n'
                                    '\n'
                                    "  if (finalStatus !== 'granted') {\n"
                                    "    console.warn('Failed to get push token permission!');\n"
                                    '    return null;\n'
                                    '  }\n'
                                    '\n'
                                    '  const tokenData = await Notifications.getExpoPushTokenAsync({\n'
                                    "    projectId: 'ai-learning-lab'\n"
                                    '  });\n'
                                    "  console.log('Device Push Token:', tokenData.data);\n"
                                    '  return tokenData.data;\n'
                                    '}',
                            'explanation': 'Prompts for push permission and generates an Expo/APNs device token.',
                            'output_preview': 'Device Push Token: ExponentPushToken[8a9f...b2c1]'},
        'quiz_id': 'quiz-app-push-notifications-fcm-apns',
        'summary': 'You mastered remote push notification architecture, device token registration, and APNs/FCM '
                   'payloads.',
        'next_lesson_slug': 'app-background-tasks-worker-sync',
        'prev_lesson_slug': 'app-flutter-bloc-state-streams'},
    {   'slug': 'app-background-tasks-worker-sync',
        'course_slug': 'mobile-production-app-stores',
        'module_id': 'app-prod-mod-2',
        'title': 'Background Fetch & Periodic Sync Workers',
        'order': 2,
        'estimated_minutes': 25,
        'difficulty': 'Advanced',
        'skill_tag': 'mobile_background_workers',
        'theory_sections': [   {   'title': 'Mobile OS Background Execution Constraints',
                                   'content_markdown': 'When a user swipes away or minimizes your app, the mobile OS '
                                                       'freezes its process within seconds to prevent battery drain.\n'
                                                       '\n'
                                                       'To perform periodic work (like syncing unread messages or '
                                                       'health step counters), you must use OS-managed background '
                                                       'schedulers:\n'
                                                       "* **iOS `BGAppRefreshTask` / `BGProcessingTask`**: Apple's ML "
                                                       'scheduler decides when to wake your app based on battery '
                                                       'level, Wi-Fi connectivity, and user charging habits.\n'
                                                       '* **Android `WorkManager`**: Schedules battery-efficient '
                                                       'background tasks with constraints (e.g. `requiresCharging`, '
                                                       '`requiresUnmeteredNetwork`).',
                                   'key_takeaway': 'Use OS-governed background schedulers (WorkManager / '
                                                   'BGAppRefreshTask) to sync data without draining battery.'}],
        'visual_explainer': {   'type': 'diagram',
                                'title': 'Background Worker Execution Pipeline',
                                'subtitle': 'App Suspended -> OS Scheduler Trigger -> 30s Execution Window -> Save to '
                                            'SQLite',
                                'diagram_type': 'background_worker'},
        'code_example': {   'title': 'Registering Background Fetch Task with expo-task-manager',
                            'language': 'javascript',
                            'code': "import * as TaskManager from 'expo-task-manager';\n"
                                    "import * as BackgroundFetch from 'expo-background-fetch';\n"
                                    '\n'
                                    "const BACKGROUND_SYNC_TASK = 'BACKGROUND_SYNC_LESSONS';\n"
                                    '\n'
                                    '// 1. Define background worker function\n'
                                    'TaskManager.defineTask(BACKGROUND_SYNC_TASK, async () => {\n'
                                    '  try {\n'
                                    "    console.log('[Background Fetch] Synchronizing offline curriculum "
                                    "updates...');\n"
                                    '    // Fetch delta updates and store in local SQLite\n'
                                    '    return BackgroundFetch.BackgroundFetchResult.NewData;\n'
                                    '  } catch (error) {\n'
                                    '    return BackgroundFetch.BackgroundFetchResult.Failed;\n'
                                    '  }\n'
                                    '});\n'
                                    '\n'
                                    '// 2. Register periodic background worker\n'
                                    'export async function initBackgroundSync() {\n'
                                    '  await BackgroundFetch.registerTaskAsync(BACKGROUND_SYNC_TASK, {\n'
                                    '    minimumInterval: 60 * 15, // Run every 15 minutes\n'
                                    '    stopOnTerminate: false,\n'
                                    '    startOnBoot: true,\n'
                                    '  });\n'
                                    '}',
                            'explanation': 'Defines and registers a background periodic synchronization task.',
                            'output_preview': '[Background Fetch Registered: 15-min interval scheduled]'},
        'quiz_id': 'quiz-app-background-tasks-worker-sync',
        'summary': 'You mastered OS background tasks, Android WorkManager constraints, and battery-efficient offline '
                   'synchronization.',
        'next_lesson_slug': 'app-appstore-playstore-deployment',
        'prev_lesson_slug': 'app-push-notifications-fcm-apns'},
    {   'slug': 'app-appstore-playstore-deployment',
        'course_slug': 'mobile-production-app-stores',
        'module_id': 'app-prod-mod-3',
        'title': 'Code Signing, Fastlane & App Store / Play Store Publishing',
        'order': 3,
        'estimated_minutes': 30,
        'difficulty': 'Advanced',
        'skill_tag': 'mobile_app_store_release',
        'theory_sections': [   {   'title': 'Mobile Code Signing & Certificates',
                                   'content_markdown': 'Unlike web servers where you simply deploy code to an IP '
                                                       'address, mobile operating systems require strict cryptographic '
                                                       'code signing:\n'
                                                       '* **iOS**: Requires an Apple Developer Account, Distribution '
                                                       'Certificate (.p12), App ID, and a Provisioning Profile '
                                                       '(.mobileprovision) that signs the compiled IPA binary.\n'
                                                       '* **Android**: Requires an Android Keystore (JKS) private key '
                                                       'that signs Android App Bundles (.aab) with Play App Signing.',
                                   'key_takeaway': 'Code signing certificates prove binary authenticity and prevent '
                                                   'tampering.'},
                               {   'title': 'Automated Mobile CI/CD with Fastlane & EAS',
                                   'content_markdown': 'Manually opening Xcode and Android Studio to archive and '
                                                       'upload binaries takes 45 minutes per release.\n'
                                                       '\n'
                                                       '**Fastlane & Expo Application Services (EAS Build)** automate '
                                                       'the entire release pipeline:\n'
                                                       '* Increment build numbers automatically.\n'
                                                       '* Build production binaries on cloud macOS runners.\n'
                                                       '* Upload directly to Apple TestFlight and Google Play Internal '
                                                       'Testing tracks.',
                                   'key_takeaway': 'Fastlane and EAS automate mobile cloud compilation, code signing, '
                                                   'and App Store releases.'}],
        'visual_explainer': {   'type': 'diagram',
                                'title': 'Mobile Automated CI/CD Release Pipeline',
                                'subtitle': 'Git Tag -> EAS / Fastlane Runner -> Code Signing -> Apple TestFlight / '
                                            'Google Play',
                                'diagram_type': 'mobile_cicd_pipeline'},
        'code_example': {   'title': 'Production EAS Build & Fastlane Configuration (eas.json)',
                            'language': 'json',
                            'code': '{\n'
                                    '  "cli": {\n'
                                    '    "version": ">= 5.0.0"\n'
                                    '  },\n'
                                    '  "build": {\n'
                                    '    "development": {\n'
                                    '      "developmentClient": true,\n'
                                    '      "distribution": "internal"\n'
                                    '    },\n'
                                    '    "preview": {\n'
                                    '      "distribution": "internal"\n'
                                    '    },\n'
                                    '    "production": {\n'
                                    '      "ios": {\n'
                                    '        "simulator": false,\n'
                                    '        "resourceClass": "m1-medium"\n'
                                    '      },\n'
                                    '      "android": {\n'
                                    '        "buildType": "app-bundle"\n'
                                    '      }\n'
                                    '    }\n'
                                    '  },\n'
                                    '  "submit": {\n'
                                    '    "production": {\n'
                                    '      "ios": {\n'
                                    '        "appleId": "developer@ailearninglab.com",\n'
                                    '        "ascAppId": "1694829102"\n'
                                    '      }\n'
                                    '    }\n'
                                    '  }\n'
                                    '}',
                            'explanation': 'Configures cloud production builds and automated App Store submission '
                                           'targets.',
                            'output_preview': '[EAS Production Build: iOS IPA & Android AAB successfully uploaded to '
                                              'Stores]'},
        'quiz_id': 'quiz-app-appstore-playstore-deployment',
        'summary': 'You mastered mobile code signing, provisioning profiles, Fastlane automation, and App Store '
                   'publishing.',
        'next_lesson_slug': 'sys-client-server-scaling',
        'prev_lesson_slug': 'app-background-tasks-worker-sync'},
    {   'slug': 'sys-client-server-scaling',
        'course_slug': 'system-design-foundations',
        'module_id': 'sys-found-mod-1',
        'title': 'Scaling Up vs Scaling Out & Edge CDN Caching',
        'order': 1,
        'estimated_minutes': 25,
        'difficulty': 'Beginner',
        'skill_tag': 'sys_scaling_foundations',
        'theory_sections': [   {   'title': 'Vertical Scaling vs Horizontal Scaling',
                                   'content_markdown': '* **Vertical Scaling (Scale Up)**: Adding more CPU, RAM, and '
                                                       'faster NVMe disks to a single server instance. Simple to '
                                                       'implement (zero code changes), but hits hard physical hardware '
                                                       'limits and introduces a **Single Point of Failure (SPOF)**.\n'
                                                       '* **Horizontal Scaling (Scale Out)**: Adding hundreds of '
                                                       'smaller, cheaper commodity server instances behind a load '
                                                       'balancer. Provides infinite scalability and high availability '
                                                       '(if one machine dies, others handle the traffic).',
                                   'key_takeaway': 'Vertical scaling hits hard hardware limits; horizontal scaling '
                                                   'provides high availability and unbounded scale.'},
                               {   'title': 'Content Delivery Networks (CDNs) & Anycast DNS',
                                   'content_markdown': 'If your main database server is in Virginia (US-East) and a '
                                                       'user requests an image from Tokyo (Japan), round-trip speed of '
                                                       'light latency through trans-Pacific fiber optics is ~160ms.\n'
                                                       '\n'
                                                       'A **CDN (Cloudflare, Fastly, AWS CloudFront)** caches static '
                                                       'HTML, JS, CSS, and media at 300+ Edge Points of Presence '
                                                       '(PoPs) worldwide. Users connect to the geographically closest '
                                                       'Edge server via Anycast DNS in < 10ms!',
                                   'key_takeaway': 'CDNs serve cached static assets from edge points of presence '
                                                   'closest to the user in sub-10ms.'}],
        'visual_explainer': {   'type': 'diagram',
                                'title': 'Global CDN Edge Architecture',
                                'subtitle': 'Global Users -> Anycast DNS -> Nearest Edge PoP (<10ms) -> Origin Server '
                                            '(Cache Miss)',
                                'diagram_type': 'cdn_edge_flow'},
        'code_example': {   'title': 'Configuring Cache-Control Headers for Edge CDNs',
                            'language': 'python',
                            'code': 'from fastapi import FastAPI, Response\n'
                                    '\n'
                                    'app = FastAPI()\n'
                                    '\n'
                                    "@app.get('/api/v1/curriculum/manifest')\n"
                                    'async def get_curriculum_manifest(response: Response):\n'
                                    '    # Tell CDN Edge to cache for 1 hour (3600s), and revalidate in background '
                                    '(stale-while-revalidate)\n'
                                    "    response.headers['Cache-Control'] = 'public, max-age=3600, s-maxage=86400, "
                                    "stale-while-revalidate=600'\n"
                                    "    response.headers['CDN-Cache-Control'] = 'max-age=86400'\n"
                                    '    \n'
                                    '    return {\n'
                                    "        'version': '1.0.4',\n"
                                    "        'tracks': ['AI & ML', 'Web Dev', 'App Dev', 'System Design', 'Git & "
                                    "GitHub'],\n"
                                    "        'total_courses': 24\n"
                                    '    }',
                            'explanation': 'Demonstrates HTTP standard Cache-Control and CDN edge caching response '
                                           'headers.',
                            'output_preview': '[HTTP 200 OK | Cache-Control: public, s-maxage=86400 | CDN Edge Hit: '
                                              '4ms]'},
        'quiz_id': 'quiz-sys-client-server-scaling',
        'summary': 'You mastered vertical vs horizontal scaling trade-offs and edge CDN caching architectures.',
        'next_lesson_slug': 'sys-monolith-to-microservices',
        'prev_lesson_slug': 'app-appstore-playstore-deployment'},
    {   'slug': 'sys-monolith-to-microservices',
        'course_slug': 'system-design-foundations',
        'module_id': 'sys-found-mod-2',
        'title': 'Monoliths to Microservices Architecture & Domain-Driven Design',
        'order': 2,
        'estimated_minutes': 25,
        'difficulty': 'Beginner',
        'skill_tag': 'sys_microservices_architecture',
        'theory_sections': [   {   'title': 'The Monolith vs Microservices Spectrum',
                                   'content_markdown': '* **Monolithic Architecture**: All business logic (auth, '
                                                       'courses, payments, notifications) runs in a single application '
                                                       'process sharing one database. Excellent for small teams and '
                                                       'early MVP stages due to fast deployments and zero network '
                                                       'latency between modules.\n'
                                                       '* **Microservices Architecture**: The system is split into '
                                                       'independent services, each owning its own dedicated database '
                                                       'and communicating over lightweight HTTP/gRPC APIs. Allows 50 '
                                                       'engineering teams to deploy independently without stepping on '
                                                       "each other's code.",
                                   'key_takeaway': 'Start with a well-structured modular monolith, then extract '
                                                   'high-scale bounded contexts into microservices.'}],
        'visual_explainer': {   'type': 'diagram',
                                'title': 'Monolith vs Microservices Architecture Comparison',
                                'subtitle': 'Monolith (Shared DB & Process) vs Microservices (Isolated DB per Service)',
                                'diagram_type': 'monolith_vs_microservices'},
        'code_example': {   'title': 'Defining Microservice Contract with gRPC & Protocol Buffers',
                            'language': 'protobuf',
                            'code': 'syntax = "proto3";\n'
                                    '\n'
                                    'package courses;\n'
                                    '\n'
                                    'service CourseService {\n'
                                    '  rpc GetCourse (CourseRequest) returns (CourseResponse);\n'
                                    '  rpc StreamLessons (StreamRequest) returns (stream LessonChunk);\n'
                                    '}\n'
                                    '\n'
                                    'message CourseRequest {\n'
                                    '  string course_slug = 1;\n'
                                    '  string user_id = 2;\n'
                                    '}\n'
                                    '\n'
                                    'message CourseResponse {\n'
                                    '  string id = 1;\n'
                                    '  string title = 2;\n'
                                    '  string domain = 3;\n'
                                    '  int32 total_lessons = 4;\n'
                                    '}',
                            'explanation': 'Illustrates strongly typed binary RPC communication between distributed '
                                           'microservices.',
                            'output_preview': '[gRPC Proto Compiled: Binary Serialization ~10x faster than JSON]'},
        'quiz_id': 'quiz-sys-monolith-to-microservices',
        'summary': 'You mastered monolithic vs microservices trade-offs and Domain-Driven Design service boundaries.',
        'next_lesson_slug': 'sys-cap-theorem-pacelc',
        'prev_lesson_slug': 'sys-client-server-scaling'},
    {   'slug': 'sys-cap-theorem-pacelc',
        'course_slug': 'system-design-foundations',
        'module_id': 'sys-found-mod-3',
        'title': 'The CAP Theorem & PACELC Distributed Trade-offs',
        'order': 3,
        'estimated_minutes': 25,
        'difficulty': 'Beginner',
        'skill_tag': 'sys_cap_theorem',
        'theory_sections': [   {   'title': "The CAP Theorem: Eric Brewer's Fundamental Law",
                                   'content_markdown': 'In any distributed data store, network cables will '
                                                       'occasionally get cut (Network Partition, **P**).\n'
                                                       '\n'
                                                       'When a partition occurs between Data Center A and Data Center '
                                                       'B, you **must choose between**:\n'
                                                       '1. **Consistency (CP)**: Refuse writes or return error until '
                                                       'the network heals so all users see identical data. (e.g. Bank '
                                                       'Account balances, Google Spanner, MongoDB).\n'
                                                       '2. **Availability (AP)**: Accept writes on both sides and '
                                                       'reconcile later (Eventual Consistency) so no request fails. '
                                                       '(e.g. DNS, Amazon DynamoDB, Apache Cassandra).',
                                   'key_takeaway': 'Under network partitions (P), distributed systems must trade off '
                                                   'Consistency (CP) vs Availability (AP).'},
                               {   'title': 'PACELC Theorem (Normal Operation vs Partitions)',
                                   'content_markdown': '**PACELC** extends CAP to describe normal operations:\n'
                                                       '* If there is a **Partition (P)**, trade off **Availability '
                                                       '(A)** or **Consistency (C)**.\n'
                                                       '* **Else (E)** (normal healthy network), trade off **Latency '
                                                       '(L)** or **Consistency (C)**.\n'
                                                       '\n'
                                                       'For example, MongoDB is **PC/EC** (consistent under partition, '
                                                       'consistent during normal operations at the cost of waiting for '
                                                       'primary write acknowledgments).',
                                   'key_takeaway': 'PACELC accounts for Latency vs Consistency trade-offs during '
                                                   'normal healthy network operation.'}],
        'visual_explainer': {   'type': 'diagram',
                                'title': 'CAP Theorem Venn Diagram & Trade-offs',
                                'subtitle': 'Consistency (CP) vs Availability (AP) vs Network Partitions (P)',
                                'diagram_type': 'cap_theorem'},
        'code_example': {   'title': 'Simulating Quorum Read/Write Consistency in Distributed Systems',
                            'language': 'python',
                            'code': 'def check_quorum_consistency(total_nodes: int, write_quorum: int, read_quorum: '
                                    'int) -> bool:\n'
                                    '    """If W + R > N, strong consistency is mathematically guaranteed (Pigeonhole '
                                    'principle)."""\n'
                                    '    is_strong = (write_quorum + read_quorum) > total_nodes\n'
                                    '    overlap = (write_quorum + read_quorum) - total_nodes\n'
                                    '    return is_strong, overlap\n'
                                    '\n'
                                    'N, W, R = 5, 3, 3\n'
                                    'strong, overlap = check_quorum_consistency(N, W, R)\n'
                                    'print(f"Nodes={N}, W={W}, R={R} -> Strong Consistency: {strong} (Overlapping '
                                    'Nodes: {overlap})")',
                            'explanation': 'Demonstrates Quorum (W + R > N) mathematical proof for distributed strong '
                                           'consistency.',
                            'output_preview': 'Nodes=5, W=3, R=3 -> Strong Consistency: True (Overlapping Nodes: 1)'},
        'quiz_id': 'quiz-sys-cap-theorem-pacelc',
        'summary': 'You mastered the CAP theorem, PACELC latency trade-offs, and quorum consistency formulas.',
        'next_lesson_slug': 'sys-l4-l7-load-balancing',
        'prev_lesson_slug': 'sys-monolith-to-microservices'},
    {   'slug': 'sys-l4-l7-load-balancing',
        'course_slug': 'system-design-loadbalancing-gateways',
        'module_id': 'sys-lb-mod-1',
        'title': 'Layer 4 vs Layer 7 Load Balancing & Algorithms',
        'order': 1,
        'estimated_minutes': 25,
        'difficulty': 'Intermediate',
        'skill_tag': 'sys_load_balancing',
        'theory_sections': [   {   'title': 'Layer 4 vs Layer 7 Load Balancing',
                                   'content_markdown': '* **Layer 4 (Transport / TCP/UDP)**: Routes traffic based only '
                                                       'on IP address and port number (e.g. AWS NLB, HAProxy TCP '
                                                       'mode). It forwards raw TCP packets without inspecting payload '
                                                       'contents. Extremely fast (millions of packets/sec with minimal '
                                                       'CPU overhead).\n'
                                                       '* **Layer 7 (Application / HTTP/HTTPS)**: Decrypts TLS and '
                                                       'inspects HTTP headers, cookies, and URL paths (e.g. Nginx, AWS '
                                                       'ALB, Envoy). Can route `/api/video` to Video Servers and '
                                                       '`/api/auth` to Auth Servers, but consumes more CPU.',
                                   'key_takeaway': 'L4 routes raw TCP packets with ultra-low latency; L7 inspects HTTP '
                                                   'paths, headers, and cookies.'},
                               {   'title': 'Balancing Algorithms',
                                   'content_markdown': '1. **Round Robin**: Cycles evenly through nodes.\n'
                                                       '2. **Least Connections**: Sends requests to the server '
                                                       'currently handling the fewest active connections (best for '
                                                       'long-lived database or WebSocket sessions).\n'
                                                       '3. **IP Hash**: Hashes client IP to ensure session persistence '
                                                       '(sticky sessions).',
                                   'key_takeaway': 'Use Least Connections for uneven workload requests and Round Robin '
                                                   'for uniform stateless APIs.'}],
        'visual_explainer': {   'type': 'diagram',
                                'title': 'Layer 7 HTTP Path-Based Routing Architecture',
                                'subtitle': 'Incoming Request -> L7 Load Balancer -> (/courses -> Node A | /video -> '
                                            'Node B)',
                                'diagram_type': 'l7_load_balancer'},
        'code_example': {   'title': 'Nginx Layer 7 Load Balancing Configuration (nginx.conf)',
                            'language': 'nginx',
                            'code': 'upstream backend_cluster {\n'
                                    '    least_conn; # Load balancing algorithm\n'
                                    '    server 10.0.0.1:8001 weight=3;\n'
                                    '    server 10.0.0.2:8001 weight=2;\n'
                                    '    server 10.0.0.3:8001 backup; # Only used if primary nodes fail\n'
                                    '}\n'
                                    '\n'
                                    'server {\n'
                                    '    listen 80;\n'
                                    '    server_name api.ailearninglab.com;\n'
                                    '\n'
                                    '    location / {\n'
                                    '        proxy_pass http://backend_cluster;\n'
                                    '        proxy_set_header Host $host;\n'
                                    '        proxy_set_header X-Real-IP $remote_addr;\n'
                                    '        proxy_connect_timeout 2s;\n'
                                    '    }\n'
                                    '}',
                            'explanation': 'Configures least_conn load balancing with weighted worker nodes and backup '
                                           'failover.',
                            'output_preview': '[Nginx L7 Reverse Proxy active on port 80]'},
        'quiz_id': 'quiz-sys-l4-l7-load-balancing',
        'summary': 'You mastered L4 vs L7 load balancing mechanisms, weighted routing, and connection algorithms.',
        'next_lesson_slug': 'sys-api-gateways-rate-limiting',
        'prev_lesson_slug': 'sys-cap-theorem-pacelc'},
    {   'slug': 'sys-api-gateways-rate-limiting',
        'course_slug': 'system-design-loadbalancing-gateways',
        'module_id': 'sys-lb-mod-2',
        'title': 'API Gateways & Token Bucket Rate Limiting Algorithms',
        'order': 2,
        'estimated_minutes': 25,
        'difficulty': 'Intermediate',
        'skill_tag': 'sys_api_gateways',
        'theory_sections': [   {   'title': 'The Role of the API Gateway',
                                   'content_markdown': 'Instead of exposing 50 internal microservices directly to the '
                                                       'public internet, an **API Gateway (Kong, AWS API Gateway, '
                                                       'KrakenD)** serves as the single secure entry door:\n'
                                                       '* Centralized Authentication & JWT Verification\n'
                                                       '* SSL/TLS Termination\n'
                                                       '* Distributed Rate Limiting & DDoS Shield\n'
                                                       '* Request transformation and response aggregation.',
                                   'key_takeaway': 'API Gateways centralize security, rate limiting, and routing '
                                                   'before traffic reaches internal services.'},
                               {   'title': 'Token Bucket vs Leaky Bucket Rate Limiting',
                                   'content_markdown': '* **Token Bucket**: Tokens are added to a bucket at a constant '
                                                       'refill rate (e.g. 10 tokens/sec up to capacity of 50). Each '
                                                       'request consumes 1 token. Allows temporary bursts of traffic '
                                                       'while enforcing average rate limits.\n'
                                                       '* **Sliding Window Log**: Stores timestamps in Redis sorted '
                                                       'sets. Highly accurate but consumes high memory.',
                                   'key_takeaway': 'Token Bucket allows controlled bursts while maintaining strict '
                                                   'average request rate limits.'}],
        'visual_explainer': {   'type': 'diagram',
                                'title': 'Token Bucket Rate Limiting Algorithm',
                                'subtitle': 'Refill Rate (+10 tokens/sec) -> Bucket Capacity (50 max) -> Request '
                                            'consumes 1 token',
                                'diagram_type': 'token_bucket'},
        'code_example': {   'title': 'Token Bucket Rate Limiter Implementation in Python',
                            'language': 'python',
                            'code': 'import time\n'
                                    '\n'
                                    'class TokenBucketRateLimiter:\n'
                                    '    def __init__(self, capacity: int, refill_rate_per_sec: float):\n'
                                    '        self.capacity = capacity\n'
                                    '        self.tokens = capacity\n'
                                    '        self.refill_rate = refill_rate_per_sec\n'
                                    '        self.last_refill = time.time()\n'
                                    '\n'
                                    '    def allow_request(self) -> bool:\n'
                                    '        now = time.time()\n'
                                    '        elapsed = now - self.last_refill\n'
                                    '        self.tokens = min(self.capacity, self.tokens + elapsed * '
                                    'self.refill_rate)\n'
                                    '        self.last_refill = now\n'
                                    '\n'
                                    '        if self.tokens >= 1.0:\n'
                                    '            self.tokens -= 1.0\n'
                                    '            return True\n'
                                    '        return False\n'
                                    '\n'
                                    'limiter = TokenBucketRateLimiter(capacity=5, refill_rate_per_sec=2.0)\n'
                                    'for i in range(1, 8):\n'
                                    '    allowed = limiter.allow_request()\n'
                                    '    print(f"Request {i} -> Allowed: {allowed} (Remaining Tokens: '
                                    '{limiter.tokens:.1f})")',
                            'explanation': 'Simulates token bucket consumption, capacity ceiling, and rate refills.',
                            'output_preview': 'Request 1 -> Allowed: True (Remaining Tokens: 4.0)\n'
                                              'Request 2 -> Allowed: True (Remaining Tokens: 3.0)\n'
                                              'Request 6 -> Allowed: False (Remaining Tokens: 0.0)'},
        'quiz_id': 'quiz-sys-api-gateways-rate-limiting',
        'summary': 'You mastered API Gateway security architecture and Token Bucket rate limiting algorithms.',
        'next_lesson_slug': 'sys-circuit-breaker-fault-tolerance',
        'prev_lesson_slug': 'sys-l4-l7-load-balancing'},
    {   'slug': 'sys-circuit-breaker-fault-tolerance',
        'course_slug': 'system-design-loadbalancing-gateways',
        'module_id': 'sys-lb-mod-3',
        'title': 'Circuit Breakers, Bulkheads & Graceful Degradation',
        'order': 3,
        'estimated_minutes': 25,
        'difficulty': 'Intermediate',
        'skill_tag': 'sys_fault_tolerance',
        'theory_sections': [   {   'title': 'Preventing Cascading Microservice Failures',
                                   'content_markdown': 'If Service A calls Service B, and Service B slows down due to '
                                                       "database lockups, Service A's thread pool fills up with "
                                                       'waiting requests. Soon Service A runs out of memory and '
                                                       'crashes, bringing down the entire company!\n'
                                                       '\n'
                                                       '**The Circuit Breaker Pattern (Netflix Hystrix, '
                                                       'Resilience4j)** monitors failure rates:\n'
                                                       '1. **Closed**: Normal operation; calls pass through.\n'
                                                       '2. **Open**: If failure rate exceeds 50%, immediately trip '
                                                       'Open. Fail instantly without calling Service B (returning '
                                                       'fallback data) so Service B can recover.\n'
                                                       '3. **Half-Open**: After a cooldown period, allow a few trial '
                                                       'requests. If they succeed, close the circuit!',
                                   'key_takeaway': 'Circuit Breakers trip open to fail fast and prevent slow '
                                                   'downstream services from crashing the system.'}],
        'visual_explainer': {   'type': 'diagram',
                                'title': 'Circuit Breaker State Machine',
                                'subtitle': 'Closed (Normal) -> [Error Threshold Exceeded] -> Open (Fail Fast) -> '
                                            '[Cooldown] -> Half-Open',
                                'diagram_type': 'circuit_breaker'},
        'code_example': {   'title': 'Circuit Breaker State Machine in Python',
                            'language': 'python',
                            'code': 'import time\n'
                                    '\n'
                                    'class CircuitBreaker:\n'
                                    '    def __init__(self, failure_threshold=3, recovery_time=5.0):\n'
                                    "        self.state = 'CLOSED'\n"
                                    '        self.failure_count = 0\n'
                                    '        self.failure_threshold = failure_threshold\n'
                                    '        self.recovery_time = recovery_time\n'
                                    '        self.last_failure_time = 0\n'
                                    '\n'
                                    '    def call(self, func, fallback_func):\n'
                                    '        now = time.time()\n'
                                    "        if self.state == 'OPEN':\n"
                                    '            if now - self.last_failure_time > self.recovery_time:\n'
                                    "                self.state = 'HALF_OPEN'\n"
                                    "                print('[CIRCUIT] Cooldown expired -> Entering HALF_OPEN test "
                                    "state')\n"
                                    '            else:\n'
                                    "                print('[CIRCUIT] Circuit OPEN -> Fast fallback return')\n"
                                    '                return fallback_func()\n'
                                    '\n'
                                    '        try:\n'
                                    '            result = func()\n'
                                    "            if self.state == 'HALF_OPEN':\n"
                                    "                self.state = 'CLOSED'\n"
                                    '                self.failure_count = 0\n'
                                    '            return result\n'
                                    '        except Exception as e:\n'
                                    '            self.failure_count += 1\n'
                                    '            self.last_failure_time = now\n'
                                    '            if self.failure_count >= self.failure_threshold:\n'
                                    "                self.state = 'OPEN'\n"
                                    "                print(f'[CIRCUIT] Failure threshold reached -> Tripped to "
                                    "OPEN!')\n"
                                    '            return fallback_func()',
                            'explanation': 'Implements Closed, Open, and Half-Open state transitions with fast '
                                           'fallback invocation.',
                            'output_preview': '[CIRCUIT] Failure threshold reached -> Tripped to OPEN!'},
        'quiz_id': 'quiz-sys-circuit-breaker-fault-tolerance',
        'summary': 'You mastered Circuit Breakers, Bulkhead isolation, and graceful degradation strategies.',
        'next_lesson_slug': 'sys-redis-caching-patterns',
        'prev_lesson_slug': 'sys-api-gateways-rate-limiting'},
    {   'slug': 'sys-redis-caching-patterns',
        'course_slug': 'system-design-caching-queues',
        'module_id': 'sys-cache-mod-1',
        'title': 'Redis Caching Patterns & Invalidation Strategies',
        'order': 1,
        'estimated_minutes': 25,
        'difficulty': 'Intermediate',
        'skill_tag': 'sys_redis_caching',
        'theory_sections': [   {   'title': 'Caching Topologies & Latency Hierarchy',
                                   'content_markdown': 'Reading from RAM (Redis) takes **~100 microseconds (0.1ms)**, '
                                                       'whereas querying a disk database (PostgreSQL/MySQL) takes '
                                                       '**10-50 milliseconds** (100x slower).\n'
                                                       '\n'
                                                       '**Common Caching Patterns**:\n'
                                                       '* **Cache-Aside (Lazy Loading)**: App checks cache. If hit, '
                                                       'return. If miss, fetch from DB and write to cache. Most '
                                                       'popular and resilient.\n'
                                                       '* **Write-Through**: Writes go to cache first, which '
                                                       'synchronously writes to DB.\n'
                                                       '* **Write-Behind (Write-Back)**: Writes go to cache, and an '
                                                       'async worker batches writes to DB later (ultra-fast writes, '
                                                       'but risk of data loss on crash).',
                                   'key_takeaway': 'Cache-Aside lazily populates memory while shielding persistent '
                                                   'databases from read traffic.'},
                               {   'title': 'Thundering Herd & Cache Stampede Mitigation',
                                   'content_markdown': 'When a popular cache key expires (e.g. World Cup live score), '
                                                       '10,000 concurrent requests all experience a Cache Miss '
                                                       'simultaneously and hammer the database at the exact same '
                                                       'millisecond!\n'
                                                       '\n'
                                                       '**Solutions**: Distributed Mutex Locks (`SETNX`), '
                                                       'probabilistic early expiration (XFetch), or background refresh '
                                                       'crons.',
                                   'key_takeaway': 'Use distributed locks (SETNX) to prevent thundering herd database '
                                                   'stampedes on cache misses.'}],
        'visual_explainer': {   'type': 'diagram',
                                'title': 'Cache-Aside with Mutex Lock Stampede Protection',
                                'subtitle': 'App Cache Miss -> Acquire Redis SETNX Lock -> Query DB -> Populate Cache '
                                            '-> Release Lock',
                                'diagram_type': 'cache_aside_lock'},
        'code_example': {   'title': 'Cache-Aside with Redis SETNX Stampede Guard in Python',
                            'language': 'python',
                            'code': 'import time\n'
                                    '\n'
                                    "mock_db = {'course:sys-design': {'title': 'Distributed Systems Mastery', "
                                    "'students': 14200}}\n"
                                    'mock_redis = {}\n'
                                    '\n'
                                    'def get_course_cached(slug: str):\n'
                                    '    # 1. Check in-memory Redis cache\n'
                                    '    if slug in mock_redis:\n'
                                    '        print(f"[CACHE HIT] Returning {slug} in 0.2ms")\n'
                                    '        return mock_redis[slug]\n'
                                    '\n'
                                    '    print(f"[CACHE MISS] Querying disk DB for {slug} in 25ms...")\n'
                                    '    data = mock_db.get(slug)\n'
                                    '    if data:\n'
                                    '        mock_redis[slug] = data # Store for future hits\n'
                                    '    return data\n'
                                    '\n'
                                    '# First query is miss, second is instant hit\n'
                                    "get_course_cached('course:sys-design')\n"
                                    "get_course_cached('course:sys-design')",
                            'explanation': 'Illustrates Cache-Aside hit/miss flow and cache population.',
                            'output_preview': '[CACHE MISS] Querying disk DB for course:sys-design in 25ms...\n'
                                              '[CACHE HIT] Returning course:sys-design in 0.2ms'},
        'quiz_id': 'quiz-sys-redis-caching-patterns',
        'summary': 'You mastered Redis caching patterns, eviction algorithms (LRU/LFU), and thundering herd stampede '
                   'protection.',
        'next_lesson_slug': 'sys-message-queues-rabbitmq-kafka',
        'prev_lesson_slug': 'sys-circuit-breaker-fault-tolerance'},
    {   'slug': 'sys-message-queues-rabbitmq-kafka',
        'course_slug': 'system-design-caching-queues',
        'module_id': 'sys-cache-mod-2',
        'title': 'Message Brokers: RabbitMQ vs Apache Kafka',
        'order': 2,
        'estimated_minutes': 25,
        'difficulty': 'Intermediate',
        'skill_tag': 'sys_message_queues',
        'theory_sections': [   {   'title': 'RabbitMQ (AMQP Push) vs Apache Kafka (Append-Only Log)',
                                   'content_markdown': '* **RabbitMQ (Traditional Message Queue)**: Smart broker, dumb '
                                                       'consumer. Messages are placed in a queue and **pushed** to '
                                                       'workers. Once a worker acknowledges receipt (`ack`), the '
                                                       'message is deleted from the queue. Excellent for complex '
                                                       'routing, job queues, and background email tasks.\n'
                                                       '* **Apache Kafka (Distributed Event Streaming)**: Dumb broker, '
                                                       'smart consumer. Kafka stores messages as an **immutable '
                                                       'append-only partitioned commit log on disk**. Messages are NOT '
                                                       'deleted when read. Multiple consumer groups can replay history '
                                                       'from any timestamp offset at gigabytes-per-second throughput!',
                                   'key_takeaway': 'Use RabbitMQ for transient task queues and Kafka for '
                                                   'high-throughput immutable event stream replay.'}],
        'visual_explainer': {   'type': 'diagram',
                                'title': 'Kafka Partitioned Append-Only Commit Log',
                                'subtitle': 'Producer -> Topic (Partition 0, 1, 2) -> Consumer Group (Offset Pointers)',
                                'diagram_type': 'kafka_stream'},
        'code_example': {   'title': 'Publishing and Consuming Events with Python & Kafka/RabbitMQ',
                            'language': 'python',
                            'code': 'import json\n'
                                    '\n'
                                    'class MockKafkaTopic:\n'
                                    '    def __init__(self, name: str):\n'
                                    '        self.name = name\n'
                                    '        self.log = [] # Append-only commit log\n'
                                    '\n'
                                    '    def produce(self, key: str, value: dict):\n'
                                    '        offset = len(self.log)\n'
                                    "        entry = {'offset': offset, 'key': key, 'payload': value}\n"
                                    '        self.log.append(entry)\n'
                                    '        print(f"[PRODUCER] Appended to Topic \'{self.name}\' at Offset '
                                    '#{offset}")\n'
                                    '        return offset\n'
                                    '\n'
                                    '    def consume_from(self, start_offset: int):\n'
                                    '        return self.log[start_offset:]\n'
                                    '\n'
                                    "topic = MockKafkaTopic('user-signups')\n"
                                    "topic.produce('usr_1', {'email': 'rajdeep@learninglab.com', 'tier': 'pro'})\n"
                                    "topic.produce('usr_2', {'email': 'elena@learninglab.com', 'tier': 'enterprise'})\n"
                                    '\n'
                                    'print("Replaying events from offset 0:", topic.consume_from(0))',
                            'explanation': 'Demonstrates append-only log architecture and offset-based consumer '
                                           'replays.',
                            'output_preview': "[PRODUCER] Appended to Topic 'user-signups' at Offset #0\n"
                                              "[PRODUCER] Appended to Topic 'user-signups' at Offset #1"},
        'quiz_id': 'quiz-sys-message-queues-rabbitmq-kafka',
        'summary': 'You mastered AMQP task queues vs Kafka append-only commit logs, partitions, and consumer offsets.',
        'next_lesson_slug': 'sys-event-driven-pubsub',
        'prev_lesson_slug': 'sys-redis-caching-patterns'},
    {   'slug': 'sys-event-driven-pubsub',
        'course_slug': 'system-design-caching-queues',
        'module_id': 'sys-cache-mod-3',
        'title': 'Event-Driven Pub/Sub & Distributed Saga Transactions',
        'order': 3,
        'estimated_minutes': 25,
        'difficulty': 'Intermediate',
        'skill_tag': 'sys_event_driven_sagas',
        'theory_sections': [   {   'title': 'The Problem with 2-Phase Commit (2PC)',
                                   'content_markdown': 'In monolithic apps, database ACID transactions span multiple '
                                                       'tables effortlessly (`BEGIN TRANSACTION ... COMMIT`).\n'
                                                       '\n'
                                                       'In microservices, where Order Service, Payment Service, and '
                                                       'Inventory Service each have separate databases, traditional '
                                                       'Two-Phase Locking (2PC) is too slow and creates distributed '
                                                       'deadlocks.\n'
                                                       '\n'
                                                       '**The Saga Pattern** solves this using a sequence of local '
                                                       'transactions coordinated by events:\n'
                                                       '* If Payment fails, the Saga emits **Compensating '
                                                       'Transactions** (e.g. `RefundPaymentEvent`, '
                                                       '`CancelInventoryHoldEvent`) to undo preceding steps cleanly.',
                                   'key_takeaway': 'Sagas manage distributed data consistency through local '
                                                   'transactions and compensating rollback events.'}],
        'visual_explainer': {   'type': 'diagram',
                                'title': 'Choreography vs Orchestration Saga Flow',
                                'subtitle': 'OrderCreated -> ReserveInventory -> ProcessPayment -> [Failure -> '
                                            'Compensate & Refund]',
                                'diagram_type': 'saga_flow'},
        'code_example': {   'title': 'Distributed Saga Compensating Transaction Handler in Python',
                            'language': 'python',
                            'code': 'def execute_order_saga(order_id: str, payment_succeeds: bool):\n'
                                    '    print(f"1. [Inventory Service] Reserved 1 seat for {order_id}")\n'
                                    '    \n'
                                    '    if not payment_succeeds:\n'
                                    '        print("2. [Payment Service] Payment Declined (Insufficient Funds)!")\n'
                                    '        print("3. [COMPENSATION] Triggering Compensating Event -> Release '
                                    'Inventory Hold")\n'
                                    "        return {'status': 'FAILED', 'reason': 'Payment declined, inventory "
                                    "released'}\n"
                                    '        \n'
                                    '    print("2. [Payment Service] Payment Processed Successfully!")\n'
                                    '    print("3. [Notification Service] Sent receipt email to user.")\n'
                                    "    return {'status': 'COMPLETED'}\n"
                                    '\n'
                                    "print(execute_order_saga('ORD-9021', payment_succeeds=False))",
                            'explanation': 'Illustrates Saga failure handling and compensating rollback execution.',
                            'output_preview': '[COMPENSATION] Triggering Compensating Event -> Release Inventory Hold\n'
                                              "{'status': 'FAILED', 'reason': 'Payment declined, inventory released'}"},
        'quiz_id': 'quiz-sys-event-driven-pubsub',
        'summary': 'You mastered event-driven pub/sub decoupling, idempotency keys, and distributed Saga transactions.',
        'next_lesson_slug': 'sys-db-replication-consensus',
        'prev_lesson_slug': 'sys-message-queues-rabbitmq-kafka'},
    {   'slug': 'sys-db-replication-consensus',
        'course_slug': 'system-design-databases-sharding',
        'module_id': 'sys-db-mod-1',
        'title': 'Leader-Follower Replication, Raft Consensus & Split-Brain',
        'order': 1,
        'estimated_minutes': 30,
        'difficulty': 'Advanced',
        'skill_tag': 'sys_db_consensus',
        'theory_sections': [   {   'title': 'Leader-Follower Replication (Read Scaling)',
                                   'content_markdown': '* **Single Leader (Primary-Replica)**: All write queries '
                                                       '(`INSERT`, `UPDATE`, `DELETE`) go to the Leader. The Leader '
                                                       'replicates write logs asynchronously or synchronously to '
                                                       'multiple Read Replicas (Followers). Read traffic is '
                                                       'distributed across replicas.\n'
                                                       '* **Replication Lag**: With async replication, there is a '
                                                       'small delay (~10ms) before a write appears on followers. If '
                                                       'the user writes data and refreshes immediately, they may see '
                                                       'stale data (Read-Your-Writes consistency issue).',
                                   'key_takeaway': 'Leader-Follower scales read throughput, but async replication '
                                                   'introduces replication lag.'},
                               {   'title': 'Raft Consensus & Split-Brain Prevention',
                                   'content_markdown': 'If the Leader database crashes or the network partitions, the '
                                                       'remaining nodes must elect a new Leader using the **Raft '
                                                       'Consensus Algorithm**.\n'
                                                       '\n'
                                                       'To prevent **Split-Brain** (where two isolated groups both '
                                                       'elect themselves as the Leader and accept conflicting writes), '
                                                       'elections require a **Majority Quorum (> 50% of total '
                                                       'nodes)**. An odd number of nodes (3, 5, or 7) is always '
                                                       'recommended!',
                                   'key_takeaway': 'Raft consensus uses majority quorums (> 50%) to elect leaders and '
                                                   'prevent split-brain write corruption.'}],
        'visual_explainer': {   'type': 'diagram',
                                'title': 'Raft Consensus Leader Election & Quorum',
                                'subtitle': 'Heartbeat Timeout -> Candidate RequestVote -> Majority Quorum Grant (3 of '
                                            '5) -> New Leader',
                                'diagram_type': 'raft_consensus'},
        'code_example': {   'title': 'Simulating Raft Majority Quorum Election in Python',
                            'language': 'python',
                            'code': 'class RaftClusterNode:\n'
                                    '    def __init__(self, node_id: int, total_nodes: int):\n'
                                    '        self.node_id = node_id\n'
                                    '        self.total_nodes = total_nodes\n'
                                    '        self.majority_needed = (total_nodes // 2) + 1\n'
                                    '\n'
                                    '    def request_votes(self, available_nodes: list) -> bool:\n'
                                    '        votes = len(available_nodes)\n'
                                    '        elected = votes >= self.majority_needed\n'
                                    '        print(f"Node #{self.node_id} received {votes}/{self.total_nodes} votes '
                                    '(Needed: {self.majority_needed}) -> Elected Leader: {elected}")\n'
                                    '        return elected\n'
                                    '\n'
                                    'cluster = RaftClusterNode(node_id=1, total_nodes=5)\n'
                                    'cluster.request_votes([1, 2, 3]) # 3 votes out of 5 -> Majority won!',
                            'explanation': 'Illustrates majority voting calculation in a 5-node distributed Raft '
                                           'cluster.',
                            'output_preview': 'Node #1 received 3/5 votes (Needed: 3) -> Elected Leader: True'},
        'quiz_id': 'quiz-sys-db-replication-consensus',
        'summary': 'You mastered database replication topologies, replication lag, and Raft consensus leader '
                   'elections.',
        'next_lesson_slug': 'sys-consistent-hashing-sharding',
        'prev_lesson_slug': 'sys-event-driven-pubsub'},
    {   'slug': 'sys-consistent-hashing-sharding',
        'course_slug': 'system-design-databases-sharding',
        'module_id': 'sys-db-mod-2',
        'title': 'Database Sharding & Consistent Hashing Rings',
        'order': 2,
        'estimated_minutes': 30,
        'difficulty': 'Advanced',
        'skill_tag': 'sys_db_sharding',
        'theory_sections': [   {   'title': 'Why Simple Modulo Sharding Fails',
                                   'content_markdown': 'If you shard a database using `shard_id = user_id % 4` across '
                                                       '4 servers, everything works until you add a 5th server!\n'
                                                       '\n'
                                                       'Changing the formula to `user_id % 5` causes **nearly 80% of '
                                                       'all existing keys to map to new servers**, requiring a '
                                                       'massive, downtime-inducing data migration.\n'
                                                       '\n'
                                                       '**Consistent Hashing** maps both Servers and Keys to a '
                                                       'circular 360-degree hash ring (0 to $2^{32}-1$). When a new '
                                                       'server node is added, only $1/N$ fraction of keys need to '
                                                       'move!',
                                   'key_takeaway': 'Consistent hashing minimizes data remapping to only k/N keys when '
                                                   'adding or removing database nodes.'}],
        'visual_explainer': {   'type': 'diagram',
                                'title': 'Consistent Hashing Ring with Virtual Nodes',
                                'subtitle': 'Hash Ring (0 - 2^32) -> Virtual Nodes (A1, B1, A2, B2) -> Clockwise Key '
                                            'Lookup',
                                'diagram_type': 'consistent_hashing'},
        'code_example': {   'title': 'Consistent Hashing Ring Implementation in Python',
                            'language': 'python',
                            'code': 'import hashlib\n'
                                    'import bisect\n'
                                    '\n'
                                    'class ConsistentHashRing:\n'
                                    '    def __init__(self, nodes=None, replicas=3):\n'
                                    '        self.replicas = replicas\n'
                                    '        self.ring = []\n'
                                    '        self.node_map = {}\n'
                                    '        for node in (nodes or []):\n'
                                    '            self.add_node(node)\n'
                                    '\n'
                                    '    def _hash(self, key: str) -> int:\n'
                                    '        return int(hashlib.md5(key.encode()).hexdigest(), 16)\n'
                                    '\n'
                                    '    def add_node(self, node: str):\n'
                                    '        for i in range(self.replicas):\n'
                                    '            h = self._hash(f"{node}#vnode_{i}")\n'
                                    '            bisect.insort(self.ring, h)\n'
                                    '            self.node_map[h] = node\n'
                                    '\n'
                                    '    def get_node(self, key: str) -> str:\n'
                                    '        if not self.ring: return None\n'
                                    '        h = self._hash(key)\n'
                                    '        idx = bisect.bisect_right(self.ring, h)\n'
                                    '        if idx == len(self.ring): idx = 0 # Wrap around ring\n'
                                    '        return self.node_map[self.ring[idx]]\n'
                                    '\n'
                                    "ring = ConsistentHashRing(['DB-Node-A', 'DB-Node-B', 'DB-Node-C'])\n"
                                    "for user in ['usr_42', 'usr_99', 'usr_104']:\n"
                                    '    print(f"User \'{user}\' routed to -> {ring.get_node(user)}")',
                            'explanation': 'Implements a consistent hashing ring with virtual nodes and binary search '
                                           'ring lookups.',
                            'output_preview': "User 'usr_42' routed to -> DB-Node-B\n"
                                              "User 'usr_99' routed to -> DB-Node-A\n"
                                              "User 'usr_104' routed to -> DB-Node-C"},
        'quiz_id': 'quiz-sys-consistent-hashing-sharding',
        'summary': 'You mastered horizontal database sharding, partition keys, and virtual nodes on consistent hash '
                   'rings.',
        'next_lesson_slug': 'sys-nosql-timeseries-search',
        'prev_lesson_slug': 'sys-db-replication-consensus'},
    {   'slug': 'sys-nosql-timeseries-search',
        'course_slug': 'system-design-databases-sharding',
        'module_id': 'sys-db-mod-3',
        'title': 'NoSQL Types, Time-Series & Inverted Search Indexes',
        'order': 3,
        'estimated_minutes': 30,
        'difficulty': 'Advanced',
        'skill_tag': 'sys_nosql_search',
        'theory_sections': [   {   'title': 'Matching the Right Database to the Right Workload',
                                   'content_markdown': 'Modern architectures use **Polyglot Persistence** (using '
                                                       'different specialized databases for different tasks):\n'
                                                       '* **Document / Key-Value (MongoDB, DynamoDB)**: Flexible '
                                                       'schema, horizontal scaling for user profiles and carts.\n'
                                                       '* **Columnar / Time-Series (InfluxDB, ClickHouse)**: Appending '
                                                       'millions of sensor readings or server metrics per second with '
                                                       'fast range queries.\n'
                                                       '* **Search Engines (Elasticsearch, Meilisearch)**: Uses '
                                                       '**Inverted Indexes** (mapping words to document IDs) to '
                                                       'perform full-text fuzzy searches in milliseconds.',
                                   'key_takeaway': 'Use polyglot persistence to match data structures to specialized '
                                                   'database storage engines.'}],
        'visual_explainer': {   'type': 'diagram',
                                'title': 'Inverted Index Full-Text Search Architecture',
                                'subtitle': 'Tokenized Terms -> Postings List (Doc IDs, Positions) -> Sub-Millisecond '
                                            'Search',
                                'diagram_type': 'inverted_index'},
        'code_example': {   'title': 'Building an Inverted Search Index in Python',
                            'language': 'python',
                            'code': 'from collections import defaultdict\n'
                                    '\n'
                                    'class InvertedIndex:\n'
                                    '    def __init__(self):\n'
                                    '        self.index = defaultdict(set)\n'
                                    '\n'
                                    '    def index_document(self, doc_id: str, text: str):\n'
                                    '        for word in text.lower().split():\n'
                                    '            self.index[word].add(doc_id)\n'
                                    '\n'
                                    '    def search(self, query: str):\n'
                                    '        words = query.lower().split()\n'
                                    '        matching_sets = [self.index.get(w, set()) for w in words]\n'
                                    '        return set.intersection(*matching_sets) if matching_sets else set()\n'
                                    '\n'
                                    'idx = InvertedIndex()\n'
                                    "idx.index_document('doc_1', 'React Native and Flutter mobile app development')\n"
                                    "idx.index_document('doc_2', 'Distributed systems system design and Redis "
                                    "caching')\n"
                                    "idx.index_document('doc_3', 'Flutter widgets and mobile performance')\n"
                                    '\n'
                                    'print("Search \'mobile flutter\':", idx.search(\'mobile flutter\'))',
                            'explanation': 'Illustrates how Elasticsearch tokenizes text into inverted index postings '
                                           'lists.',
                            'output_preview': "Search 'mobile flutter': {'doc_1', 'doc_3'}"},
        'quiz_id': 'quiz-sys-nosql-timeseries-search',
        'summary': 'You mastered NoSQL paradigms, LSM trees, time-series storage, and Elasticsearch inverted indexing.',
        'next_lesson_slug': 'git-internals-blobs-trees-commits',
        'prev_lesson_slug': 'sys-consistent-hashing-sharding'},
    {   'slug': 'git-internals-blobs-trees-commits',
        'course_slug': 'git-core-internals',
        'module_id': 'git-core-mod-1',
        'title': 'Git Object Storage: Blobs, Trees & The Immutable Commit DAG',
        'order': 1,
        'estimated_minutes': 20,
        'difficulty': 'Beginner',
        'skill_tag': 'git_internals_dag',
        'theory_sections': [   {   'title': 'Git Is an Object Database, Not a Delta Tracker',
                                   'content_markdown': 'Many developers imagine Git stores file differences (diff '
                                                       'lines) like an incremental patch file.\n'
                                                       '\n'
                                                       'In reality, **Git is a content-addressable key-value object '
                                                       'store** in `.git/objects/`:\n'
                                                       '* **Blob (Binary Large Object)**: Stores pure file content '
                                                       'compressed with zlib. Keyed by SHA-1 hash.\n'
                                                       '* **Tree Object**: Represents a directory folder. Maps '
                                                       'filenames and permissions to child Blob or Tree SHA hashes.\n'
                                                       '* **Commit Object**: Stores author, committer, timestamp, '
                                                       'message, parent commit SHA, and root Tree SHA.\n'
                                                       '\n'
                                                       'Because commit parent pointers only point backwards, Git forms '
                                                       'an **Immutable Directed Acyclic Graph (DAG)**!',
                                   'key_takeaway': 'Git stores full immutable snapshots in a DAG of Blobs, Trees, and '
                                                   'Commits addressed by cryptographic SHA hashes.'}],
        'visual_explainer': {   'type': 'diagram',
                                'title': 'Git Object Database Architecture',
                                'subtitle': 'Commit SHA -> Root Tree SHA -> Sub-Trees & Blobs (SHA-1 / SHA-256)',
                                'diagram_type': 'git_dag'},
        'code_example': {   'title': 'Creating a Real Git Blob Object with Python & SHA-1',
                            'language': 'python',
                            'code': 'import hashlib\n'
                                    'import zlib\n'
                                    '\n'
                                    'def create_git_blob_object(content: str) -> tuple:\n'
                                    "    raw_bytes = content.encode('utf-8')\n"
                                    "    # Git Header: 'blob <size>\\0'\n"
                                    '    header = f"blob {len(raw_bytes)}\\0".encode(\'utf-8\')\n'
                                    '    store = header + raw_bytes\n'
                                    '    sha1_hash = hashlib.sha1(store).hexdigest()\n'
                                    '    compressed_data = zlib.compress(store)\n'
                                    '    return sha1_hash, compressed_data\n'
                                    '\n'
                                    'code = "console.log(\'AI Learning Lab Mobile & Web\');"\n'
                                    'sha, comp = create_git_blob_object(code)\n'
                                    'print(f"Git Blob SHA-1: {sha}")\n'
                                    'print(f"Object File Path: .git/objects/{sha[:2]}/{sha[2:]}")',
                            'explanation': 'Calculates the exact SHA-1 key and zlib storage format used by Git '
                                           'internally.',
                            'output_preview': 'Git Blob SHA-1: b886a8e63080e74f3ffca93cf938ef57c0a6b99e\n'
                                              'Object File Path: '
                                              '.git/objects/b8/86a8e63080e74f3ffca93cf938ef57c0a6b99e'},
        'quiz_id': 'quiz-git-internals-blobs-trees-commits',
        'summary': 'You mastered Git object database storage, Blobs, Trees, and immutable Commit DAG graphs.',
        'next_lesson_slug': 'git-staging-working-tree-index',
        'prev_lesson_slug': 'sys-nosql-timeseries-search'},
    {   'slug': 'git-staging-working-tree-index',
        'course_slug': 'git-core-internals',
        'module_id': 'git-core-mod-2',
        'title': 'The 3 Trees: Working Directory, Staging Index & Repository',
        'order': 2,
        'estimated_minutes': 20,
        'difficulty': 'Beginner',
        'skill_tag': 'git_three_trees',
        'theory_sections': [   {   'title': 'The Three Arenas of Git',
                                   'content_markdown': 'To understand `git add`, `git commit`, and `git checkout`, you '
                                                       "must visualize Git's 3 distinct trees:\n"
                                                       '1. **Working Directory**: The actual sandbox files on your '
                                                       'filesystem where you edit code in VS Code.\n'
                                                       '2. **Staging Index (`.git/index`)**: A binary cache that '
                                                       'prepares the exact snapshot that will be written into the next '
                                                       'commit. `git add` copies files from your working tree into the '
                                                       'index.\n'
                                                       '3. **Git Repository (HEAD Commit)**: The permanent history of '
                                                       'committed snapshots.',
                                   'key_takeaway': 'The Staging Index is your preview draft canvas before permanently '
                                                   'committing a snapshot to repository history.'}],
        'visual_explainer': {   'type': 'diagram',
                                'title': 'The 3 Trees of Git Workflow',
                                'subtitle': 'Working Directory --(git add)--> Staging Index --(git commit)--> Git Repo '
                                            '(HEAD)',
                                'diagram_type': 'git_three_trees'},
        'code_example': {   'title': 'Inspecting Staging Area Status and Diffs',
                            'language': 'bash',
                            'code': '# 1. Inspect differences between Working Directory and Index\n'
                                    'git diff\n'
                                    '\n'
                                    '# 2. Inspect differences between Staging Index and HEAD commit\n'
                                    'git diff --staged\n'
                                    '\n'
                                    '# 3. View binary index entries\n'
                                    'git ls-files --stage',
                            'explanation': 'Compares changes across the 3 trees to verify staged snapshot content.',
                            'output_preview': '100644 b886a8e63080e74f3ffca93cf938ef57c0a6b99e 0  src/App.jsx'},
        'quiz_id': 'quiz-git-staging-working-tree-index',
        'summary': 'You mastered the 3 trees of Git: Working directory, binary staging index, and permanent repository '
                   'commits.',
        'next_lesson_slug': 'git-head-branches-tags',
        'prev_lesson_slug': 'git-internals-blobs-trees-commits'},
    {   'slug': 'git-head-branches-tags',
        'course_slug': 'git-core-internals',
        'module_id': 'git-core-mod-3',
        'title': 'The HEAD Pointer, Branch References & Detached HEAD',
        'order': 3,
        'estimated_minutes': 20,
        'difficulty': 'Beginner',
        'skill_tag': 'git_head_pointers',
        'theory_sections': [   {   'title': 'Branches Are Just 41-Byte Text Files',
                                   'content_markdown': 'In Git, a branch is **not a heavy copy of your codebase**.\n'
                                                       '\n'
                                                       'A branch is literally a simple 41-byte text file in '
                                                       '`.git/refs/heads/main` containing a 40-character commit SHA '
                                                       'string and a newline!\n'
                                                       '\n'
                                                       '**The `HEAD` Pointer**:\n'
                                                       '* `.git/HEAD` points to your current branch reference (e.g. '
                                                       '`ref: refs/heads/main`).\n'
                                                       '* When you create a new commit, Git updates the branch file to '
                                                       'point to the new commit SHA and advances `HEAD`.',
                                   'key_takeaway': 'Branches are lightweight 41-byte text pointers that advance '
                                                   'automatically with every new commit.'},
                               {   'title': 'Detached HEAD State Demystified',
                                   'content_markdown': 'If you run `git checkout <commit_sha>` instead of checking out '
                                                       'a branch name, `HEAD` points directly to a commit hash rather '
                                                       'than a branch reference.\n'
                                                       '\n'
                                                       'Any commits made in this state are **detached** (unnamed) and '
                                                       'will be lost when you switch branches unless you create a new '
                                                       'branch pointer (`git checkout -b new-branch`)!',
                                   'key_takeaway': 'A detached HEAD points directly to a commit hash; create a branch '
                                                   'to preserve detached work.'}],
        'visual_explainer': {   'type': 'diagram',
                                'title': 'HEAD Pointer & Branch References',
                                'subtitle': 'HEAD -> refs/heads/main -> Commit C3 (f7a2) -> Parent C2 -> Parent C1',
                                'diagram_type': 'git_head_branch'},
        'code_example': {   'title': 'Inspecting HEAD and Branch Reference Pointers in Terminal',
                            'language': 'bash',
                            'code': '# 1. Inspect what HEAD is currently pointing to\n'
                                    'cat .git/HEAD\n'
                                    '# Output: ref: refs/heads/main\n'
                                    '\n'
                                    "# 2. Inspect the commit SHA that 'main' points to\n"
                                    'cat .git/refs/heads/main\n'
                                    '# Output: 9f41a8e2bc7041f92e34081c7f42817d91e602ab',
                            'explanation': 'Reveals that Git branches and HEAD are plain text pointer files.',
                            'output_preview': 'ref: refs/heads/main\n9f41a8e2bc7041f92e34081c7f42817d91e602ab'},
        'quiz_id': 'quiz-git-head-branches-tags',
        'summary': 'You mastered Git branch references, HEAD pointer mechanics, and navigating detached HEAD states.',
        'next_lesson_slug': 'git-branching-merge-strategies',
        'prev_lesson_slug': 'git-staging-working-tree-index'},
    {   'slug': 'git-branching-merge-strategies',
        'course_slug': 'git-branching-rebase-workflow',
        'module_id': 'git-branch-mod-1',
        'title': 'Fast-Forward Merges vs 3-Way Merge Commits',
        'order': 1,
        'estimated_minutes': 25,
        'difficulty': 'Intermediate',
        'skill_tag': 'git_merge_strategies',
        'theory_sections': [   {   'title': 'Fast-Forward Merge',
                                   'content_markdown': 'If the `main` branch has not received any new commits since '
                                                       'your feature branch branched off, merging is '
                                                       '**Fast-Forward**:\n'
                                                       '* Git simply moves the `main` branch pointer forward to the '
                                                       'tip of your feature branch.\n'
                                                       '* No new merge commit is created; the history remains a '
                                                       'straight linear line.',
                                   'key_takeaway': 'Fast-Forward merges simply move the target branch pointer forward '
                                                   'without creating a new commit.'},
                               {   'title': '3-Way Merge Commit (Diamond Graph)',
                                   'content_markdown': 'If `main` has advanced with new commits while you worked on '
                                                       'your feature, Git performs a **3-Way Merge** using:\n'
                                                       '1. Common Ancestor Commit\n'
                                                       '2. Tip of `main` branch\n'
                                                       '3. Tip of `feature` branch\n'
                                                       '\n'
                                                       'Git combines both trees into a new **Merge Commit** with **two '
                                                       'parent pointers**.',
                                   'key_takeaway': '3-Way merges create a merge commit with two parents to join '
                                                   'diverging branch histories.'}],
        'visual_explainer': {   'type': 'diagram',
                                'title': 'Fast-Forward vs 3-Way Merge Commits',
                                'subtitle': 'Fast-Forward (Linear Pointer Advance) vs 3-Way Merge (2 Parents Diamond '
                                            'Graph)',
                                'diagram_type': 'merge_vs_rebase'},
        'code_example': {   'title': 'Executing Fast-Forward and Non-Fast-Forward Merges',
                            'language': 'bash',
                            'code': '# 1. Fast-forward merge (default when linear)\n'
                                    'git checkout main\n'
                                    'git merge feature/auth\n'
                                    '\n'
                                    '# 2. Force a merge commit even if fast-forward is possible (--no-ff)\n'
                                    'git merge --no-ff feature/payments -m "merge: incorporate payments module"',
                            'explanation': 'Demonstrates fast-forward merges and explicit merge commit creation with '
                                           '--no-ff.',
                            'output_preview': 'Updating 9f41a8e..c8d201f\n'
                                              'Fast-forward\n'
                                              ' src/auth.js | 42 ++++++++++++++++++++++++++++++++++++++++++\n'
                                              ' 1 file changed, 42 insertions(+)'},
        'quiz_id': 'quiz-git-branching-merge-strategies',
        'summary': 'You mastered fast-forward pointer movement and 3-way merge commits with common ancestors.',
        'next_lesson_slug': 'git-interactive-rebase-squash',
        'prev_lesson_slug': 'git-head-branches-tags'},
    {   'slug': 'git-interactive-rebase-squash',
        'course_slug': 'git-branching-rebase-workflow',
        'module_id': 'git-branch-mod-2',
        'title': 'Interactive Rebase (`git rebase -i`): Squashing & Rewording',
        'order': 2,
        'estimated_minutes': 25,
        'difficulty': 'Intermediate',
        'skill_tag': 'git_interactive_rebase',
        'theory_sections': [   {   'title': "Commit Hygiene: Never Open a PR with 'WIP' Commits",
                                   'content_markdown': "During development, you might make 12 messy commits: `'fix "
                                                       "typo'`, `'wip test'`, `'oops'`, `'test again'`.\n"
                                                       '\n'
                                                       'Submitting this clutter makes peer code reviews miserable and '
                                                       'pollutes git blame.\n'
                                                       '\n'
                                                       '**`git rebase -i HEAD~4` (Interactive Rebase)** gives you a '
                                                       'text editor menu to rewrite history before pushing:\n'
                                                       '* **`pick`**: Keep commit as is.\n'
                                                       '* **`squash` (s)**: Melt this commit into the previous '
                                                       'commit.\n'
                                                       '* **`reword` (r)**: Edit the commit message to follow '
                                                       'Conventional Commits.\n'
                                                       '* **`drop` (d)**: Delete accidental debug commits completely!',
                                   'key_takeaway': 'Use interactive rebase to squash messy WIP commits into clean, '
                                                   'logical semantic changesets.'}],
        'visual_explainer': {   'type': 'diagram',
                                'title': 'Interactive Rebase Squashing Workflow',
                                'subtitle': "4 WIP Commits -> git rebase -i -> 1 Clean Atomic 'feat: add dark mode' "
                                            'Commit',
                                'diagram_type': 'git_rebase_squash'},
        'code_example': {   'title': 'Interactive Rebase Command Sheet (git rebase -i HEAD~3)',
                            'language': 'bash',
                            'code': '# In the rebase todo list editor:\n'
                                    'pick a1b2c3d feat(mobile): add course navigation stack\n'
                                    'squash e4f5g6h fix typo in stack header\n'
                                    'squash j7k8l9m adjust tab icon padding\n'
                                    '\n'
                                    "# Saves as 1 clean atomic commit: 'feat(mobile): add course navigation stack'",
                            'explanation': 'Squashes 3 fragmented commits into one pristine commit with clean message.',
                            'output_preview': '[detached HEAD 4a2b91c] feat(mobile): add course navigation stack\n'
                                              ' 3 files changed, 120 insertions(+)'},
        'quiz_id': 'quiz-git-interactive-rebase-squash',
        'summary': 'You mastered interactive rebasing, commit squashing, rewording, and commit history hygiene.',
        'next_lesson_slug': 'git-merge-conflicts-cherrypick',
        'prev_lesson_slug': 'git-branching-merge-strategies'},
    {   'slug': 'git-merge-conflicts-cherrypick',
        'course_slug': 'git-branching-rebase-workflow',
        'module_id': 'git-branch-mod-3',
        'title': 'Conflict Resolution, `git cherry-pick` & Time Travel with Reflog',
        'order': 3,
        'estimated_minutes': 25,
        'difficulty': 'Intermediate',
        'skill_tag': 'git_conflicts_reflog',
        'theory_sections': [   {   'title': 'Understanding Merge Conflict Markers',
                                   'content_markdown': 'When two developers modify the exact same line in a file, Git '
                                                       'cannot guess which version is correct and pauses with conflict '
                                                       'markers:\n'
                                                       '```\n'
                                                       '<<<<<<< HEAD (Current change on main)\n'
                                                       "const API_URL = 'https://api.v2.learninglab.com';\n"
                                                       '=======\n'
                                                       "const API_URL = 'https://api.staging.learninglab.com';\n"
                                                       '>>>>>>> feature/auth (Incoming change)\n'
                                                       '```\n'
                                                       'To resolve, simply delete the conflict marker lines and choose '
                                                       'the intended code, then `git add` and `git commit`.',
                                   'key_takeaway': 'Merge conflicts occur when the same lines are edited concurrently; '
                                                   'resolve manually and commit.'},
                               {   'title': 'Emergency Time Travel with `git reflog`',
                                   'content_markdown': 'Even if you accidentally run `git branch -D` or botch a '
                                                       'rebase, **Git rarely deletes commit objects immediately**.\n'
                                                       '\n'
                                                       '`git reflog` records every movement of `HEAD` for the last 90 '
                                                       'days. You can find the lost commit hash and restore your '
                                                       'branch instantly with `git checkout -b recovered-branch '
                                                       'HEAD@{3}`!',
                                   'key_takeaway': 'git reflog is your safety net to recover deleted branches or '
                                                   'aborted rebases.'}],
        'visual_explainer': {   'type': 'diagram',
                                'title': 'Git Reflog History Journal',
                                'subtitle': 'HEAD@{0} -> HEAD@{1} (rebase checkout) -> HEAD@{2} (commit: feature save) '
                                            '-> Restore Point',
                                'diagram_type': 'git_reflog'},
        'code_example': {   'title': 'Recovering a Lost Branch Using git reflog',
                            'language': 'bash',
                            'code': '# 1. View local reference history log\n'
                                    'git reflog -n 5\n'
                                    '\n'
                                    '# Output:\n'
                                    '# 90a21b4 (HEAD -> main) HEAD@{0}: checkout: moving from feature to main\n'
                                    '# f4e3d21 HEAD@{1}: commit: important work on mobile UI\n'
                                    '\n'
                                    '# 2. Re-create deleted branch from reflog snapshot!\n'
                                    'git checkout -b feature/mobile-restored f4e3d21',
                            'explanation': 'Recovers an accidentally deleted commit branch using local reflog '
                                           'tracking.',
                            'output_preview': "Switched to a new branch 'feature/mobile-restored' pointing to f4e3d21"},
        'quiz_id': 'quiz-git-merge-conflicts-cherrypick',
        'summary': 'You mastered merge conflict resolution, git cherry-pick, and recovering lost commits with git '
                   'reflog.',
        'next_lesson_slug': 'git-github-prs-code-reviews',
        'prev_lesson_slug': 'git-interactive-rebase-squash'},
    {   'slug': 'git-github-prs-code-reviews',
        'course_slug': 'github-team-cicd-actions',
        'module_id': 'git-team-mod-1',
        'title': 'Pull Requests, Code Reviews & Semantic Versioning (SemVer)',
        'order': 1,
        'estimated_minutes': 25,
        'difficulty': 'Intermediate',
        'skill_tag': 'github_pr_workflow',
        'theory_sections': [   {   'title': 'The GitHub Pull Request Lifecycle',
                                   'content_markdown': 'In professional engineering organizations, code is never '
                                                       'committed directly to `main`.\n'
                                                       '\n'
                                                       '**The PR Lifecycle**:\n'
                                                       '1. Engineer pushes feature branch to GitHub and opens a **Pull '
                                                       'Request**.\n'
                                                       '2. Automated CI checks run tests, linting, and build steps.\n'
                                                       '3. Teammates review code, leave inline comments, and suggest '
                                                       'modifications.\n'
                                                       '4. Once approvals (LGTM) and status checks pass, the PR is '
                                                       'merged via Squash & Merge.',
                                   'key_takeaway': 'Pull Requests provide peer code reviews and automated quality gate '
                                                   'checks before merging.'},
                               {   'title': 'Semantic Versioning (SemVer 2.0.0)',
                                   'content_markdown': 'Software releases follow **`MAJOR.MINOR.PATCH`** (e.g. '
                                                       '`v1.0.4`):\n'
                                                       '* **PATCH (`+0.0.1`)**: Backwards-compatible bug fixes.\n'
                                                       '* **MINOR (`+0.1.0`)**: Backwards-compatible new features.\n'
                                                       '* **MAJOR (`+1.0.0`)**: Breaking API changes that require user '
                                                       'modifications.',
                                   'key_takeaway': 'Use SemVer to communicate API stability and breaking changes to '
                                                   'consumers.'}],
        'visual_explainer': {   'type': 'diagram',
                                'title': 'GitHub Pull Request & Branch Protection Flow',
                                'subtitle': 'Feature Branch -> Pull Request -> Automated CI Tests -> 2 Peer Approvals '
                                            '-> Merge to Main',
                                'diagram_type': 'github_pr_flow'},
        'code_example': {   'title': 'Conventional Commit Messages for Automated Changelogs',
                            'language': 'bash',
                            'code': '# Semantic commit prefixes for automated release tagging\n'
                                    'git commit -m "feat(curriculum): add 5 comprehensive App Dev courses"\n'
                                    'git commit -m "fix(routing): resolve algorithm laboratory redirection path"\n'
                                    'git commit -m "chore(release): bump version to v1.0.4"',
                            'explanation': 'Demonstrates Conventional Commit conventions used by semantic release '
                                           'bots.',
                            'output_preview': '[main 3f91a20] feat(curriculum): add 5 comprehensive App Dev courses'},
        'quiz_id': 'quiz-git-github-prs-code-reviews',
        'summary': 'You mastered GitHub PR workflows, code review etiquette, branch protection rules, and SemVer '
                   'versioning.',
        'next_lesson_slug': 'git-actions-cicd-automation',
        'prev_lesson_slug': 'git-merge-conflicts-cherrypick'},
    {   'slug': 'git-actions-cicd-automation',
        'course_slug': 'github-team-cicd-actions',
        'module_id': 'git-team-mod-2',
        'title': 'Automated GitHub Actions CI/CD Workflows & Matrix Testing',
        'order': 2,
        'estimated_minutes': 25,
        'difficulty': 'Intermediate',
        'skill_tag': 'github_actions_cicd',
        'theory_sections': [   {   'title': 'GitHub Actions Architecture',
                                   'content_markdown': 'GitHub Actions runs automated workflows inside isolated '
                                                       'ephemeral cloud virtual machines (Ubuntu, macOS, Windows):\n'
                                                       '* **Events**: Triggering webhooks (e.g. `on: push`, `on: '
                                                       'pull_request`, `on: release`).\n'
                                                       '* **Jobs**: A series of steps running on a specific `runs-on` '
                                                       'VM.\n'
                                                       '* **Matrix Strategy**: Runs your test suite across multiple '
                                                       'OSs and runtime versions concurrently (e.g. Python 3.11, 3.12, '
                                                       '3.13 and Node 18, 20, 22) in parallel!',
                                   'key_takeaway': 'GitHub Actions workflows execute automated multi-version matrix '
                                                   'tests on every push.'}],
        'visual_explainer': {   'type': 'diagram',
                                'title': 'GitHub Actions CI Pipeline Architecture',
                                'subtitle': 'git push -> Webhook -> GitHub Runner VM -> Checkout -> Install -> Test '
                                            'Matrix -> Pass/Fail',
                                'diagram_type': 'cicd_pipeline'},
        'code_example': {   'title': 'Full CI/CD Pipeline Workflow (.github/workflows/ci.yml)',
                            'language': 'yaml',
                            'code': 'name: CI Pipeline\n'
                                    'on:\n'
                                    '  push:\n'
                                    '    branches: [main]\n'
                                    '  pull_request:\n'
                                    '    branches: [main]\n'
                                    '\n'
                                    'jobs:\n'
                                    '  test-backend:\n'
                                    '    runs-on: ubuntu-latest\n'
                                    '    steps:\n'
                                    '      - uses: actions/checkout@v4\n'
                                    '      - uses: actions/setup-python@v5\n'
                                    '        with:\n'
                                    "          python-version: '3.13'\n"
                                    '      - name: Install Dependencies & Run Pytest\n'
                                    '        run: |\n'
                                    '          cd apps/backend\n'
                                    '          pip install -r requirements.txt\n'
                                    '          pytest tests/ -v\n'
                                    '\n'
                                    '  build-desktop:\n'
                                    '    runs-on: ubuntu-latest\n'
                                    '    steps:\n'
                                    '      - uses: actions/checkout@v4\n'
                                    '      - uses: actions/setup-node@v4\n'
                                    '        with:\n'
                                    '          node-version: 20\n'
                                    '      - name: Build Vite & Tauri Bundle\n'
                                    '        run: |\n'
                                    '          cd apps/desktop\n'
                                    '          npm ci\n'
                                    '          npm run build',
                            'explanation': 'Defines a complete parallel backend pytest and desktop build validation '
                                           'workflow.',
                            'output_preview': '[GitHub Actions: 2 Jobs Succeeded in 45s]'},
        'quiz_id': 'quiz-git-actions-cicd-automation',
        'summary': 'You mastered GitHub Actions YAML workflows, runner environments, event triggers, and parallel '
                   'matrix jobs.',
        'next_lesson_slug': 'git-releases-tag-publishing',
        'prev_lesson_slug': 'git-github-prs-code-reviews'},
    {   'slug': 'git-releases-tag-publishing',
        'course_slug': 'github-team-cicd-actions',
        'module_id': 'git-team-mod-3',
        'title': 'Automated Release Tagging, Changelogs & Artifact Publishing',
        'order': 3,
        'estimated_minutes': 25,
        'difficulty': 'Intermediate',
        'skill_tag': 'github_releases_publishing',
        'theory_sections': [   {   'title': 'Git Annotated Tags vs GitHub Releases',
                                   'content_markdown': "* **Annotated Git Tag (`git tag -a v1.0.4 -m '...'`)**: An "
                                                       'immutable cryptographic tag object in Git storing the tagger, '
                                                       'date, message, and target commit SHA.\n'
                                                       '* **GitHub Release**: A user-facing release webpage tied to a '
                                                       'Git tag that includes markdown changelog release notes and '
                                                       'downloadable binary installer assets (.exe, .dmg, .apk, .ipa).',
                                   'key_takeaway': 'Annotated Git tags mark release milestones, and GitHub Releases '
                                                   'distribute compiled binary artifacts.'},
                               {   'title': 'Automating Binary Releases with GitHub Actions',
                                   'content_markdown': "By configuring `on: push: tags: ['v*.*.*']`, pushing a version "
                                                       'tag automatically triggers GitHub Actions to compile Tauri '
                                                       'desktop executables and attach them directly to the GitHub '
                                                       'Release download page.',
                                   'key_takeaway': 'Pushing a semantic Git tag triggers CI/CD to build and publish '
                                                   'installer binaries automatically.'}],
        'visual_explainer': {   'type': 'diagram',
                                'title': 'Automated Release Publishing Workflow',
                                'subtitle': 'git push origin v1.0.4 -> Tag Trigger -> Tauri Cross-Compile -> GitHub '
                                            'Release Assets',
                                'diagram_type': 'release_tag_pipeline'},
        'code_example': {   'title': 'Creating and Pushing Annotated Git Release Tags',
                            'language': 'bash',
                            'code': '# 1. Create annotated release tag with changelog message\n'
                                    'git tag -a v1.0.4 -m "Release v1.0.4: Complete App Development & System Design '
                                    'Tracks"\n'
                                    '\n'
                                    '# 2. Push tag to GitHub remote\n'
                                    'git push origin v1.0.4\n'
                                    '\n'
                                    '# 3. View tag signature details\n'
                                    'git show v1.0.4',
                            'explanation': 'Creates and pushes an immutable annotated release tag to trigger GitHub '
                                           'Release pipelines.',
                            'output_preview': '[Pushed Git Tag v1.0.4 -> Triggered GitHub Release Workflow]'},
        'quiz_id': 'quiz-git-releases-tag-publishing',
        'summary': 'You mastered annotated Git tags, automated changelog generation, and GitHub Release asset '
                   'distribution.',
        'next_lesson_slug': None,
        'prev_lesson_slug': 'git-actions-cicd-automation'}]

QUIZZES_DATA = [   {   'id': 'quiz-py-intro-variables',
        'lesson_slug': 'py-intro-variables',
        'title': 'Python References & Object Mutability Quiz',
        'passing_score': 70,
        'questions': [   {   'id': 'q1',
                             'type': 'multiple_choice',
                             'question': 'What happens in memory when executing: `a = [1, 2]`; `b = a`; `b.append(3)`?',
                             'options': [   'b gets a new independent copy of the list; a remains [1, 2]',
                                            'Both a and b point to the exact same list object on the heap; a is now '
                                            '[1, 2, 3]',
                                            'Python throws a ReferenceError',
                                            'b is appended but a is set to None'],
                             'correct_answer': 1,
                             'points': 10,
                             'skill_tag': 'python_basics',
                             'explanation': 'Lists are mutable objects in Python. The assignment `b = a` copies the '
                                            'reference (memory address), not the underlying list. Modifying `b` '
                                            'modifies the same heap allocation that `a` references.',
                             'hint': 'Remember that Python variables are references (pointers) to objects in memory.'},
                         {   'id': 'q2',
                             'type': 'true_false',
                             'question': 'In Python, numbers (integers, floats) and strings are immutable (cannot be '
                                         'altered in-place).',
                             'options': ['True', 'False'],
                             'correct_answer': 0,
                             'points': 10,
                             'skill_tag': 'python_basics',
                             'explanation': 'True. Numeric types (int, float) and strings are immutable. Any '
                                            'modification (like `x += 1`) creates a brand new number object rather '
                                            'than modifying the existing memory block in-place.'}]},
    {   'id': 'quiz-py-data-structures-comprehensions',
        'lesson_slug': 'py-data-structures-comprehensions',
        'title': 'Python Data Structures & Comprehensions Quiz',
        'passing_score': 70,
        'questions': [   {   'id': 'q1',
                             'type': 'multiple_choice',
                             'question': 'What is the output of the list comprehension: `[x**2 for x in [1, 2, 3, 4] '
                                         'if x % 2 == 0]`?',
                             'options': ['[1, 9]', '[4, 16]', '[1, 4, 9, 16]', '[2, 4]'],
                             'correct_answer': 1,
                             'points': 10,
                             'skill_tag': 'python_basics',
                             'explanation': 'The condition `if x % 2 == 0` filters only even numbers (2 and 4). The '
                                            'expression `x**2` squares them, producing [4, 16].',
                             'hint': 'Filter even numbers first, then square each.'}]},
    {   'id': 'quiz-py-numpy-arrays-broadcasting',
        'lesson_slug': 'py-numpy-arrays-broadcasting',
        'title': 'NumPy Broadcasting & Tensor Shapes Quiz',
        'passing_score': 70,
        'questions': [   {   'id': 'q1',
                             'type': 'multiple_choice',
                             'question': 'Which of the following array shape pairs CANNOT be broadcast together under '
                                         'NumPy rules?',
                             'options': [   '(4, 3) and (3,)',
                                            '(5, 1, 4) and (1, 3, 4)',
                                            '(3, 4) and (3, 1)',
                                            '(4, 3) and (4,)'],
                             'correct_answer': 3,
                             'points': 10,
                             'skill_tag': 'numpy_basics',
                             'explanation': 'Broadcasting aligns trailing (rightmost) dimensions. For `(4, 3)` and '
                                            '`(4,)`, the trailing dimensions are `3` and `4`. Since neither is equal '
                                            'nor 1, NumPy raises a ValueError.',
                             'hint': 'Compare trailing dimensions from right to left. They must be equal or one of '
                                     'them must be 1.'}]},
    {   'id': 'quiz-py-numpy-matrix-operations',
        'lesson_slug': 'py-numpy-matrix-operations',
        'title': 'NumPy Matrix Operations Quiz',
        'passing_score': 70,
        'questions': [   {   'id': 'q1',
                             'type': 'multiple_choice',
                             'question': 'If matrix A has shape (5, 8) and matrix B has shape (8, 3), what is the '
                                         'shape of the matrix product A @ B?',
                             'options': ['(5, 3)', '(8, 8)', '(5, 8)', '(8, 3)'],
                             'correct_answer': 0,
                             'points': 10,
                             'skill_tag': 'numpy_basics',
                             'explanation': 'In matrix multiplication (M, K) @ (K, N), the inner dimension K=8 matches '
                                            'and cancels, leaving shape (M, N) = (5, 3).',
                             'hint': 'Outer dimensions define the resulting output shape.'}]},
    {   'id': 'quiz-py-pandas-dataframes-cleaning',
        'lesson_slug': 'py-pandas-dataframes-cleaning',
        'title': 'Pandas Data Cleaning & Preprocessing Quiz',
        'passing_score': 70,
        'questions': [   {   'id': 'q1',
                             'type': 'multiple_choice',
                             'question': 'Why is it usually preferable to impute missing numeric values with the '
                                         'column median rather than the column mean?',
                             'options': [   'Median takes less memory to store',
                                            'Median is robust to extreme outliers and skewed data distributions',
                                            'Mean is only defined for integer values',
                                            'Pandas cannot compute the mean of a column'],
                             'correct_answer': 1,
                             'points': 10,
                             'skill_tag': 'data_preprocessing',
                             'explanation': 'The median represents the exact 50th percentile and is not pulled by '
                                            'massive outliers (like a $10M salary entry), making it safer for '
                                            'real-world imputation.',
                             'hint': 'Think about how one billionaire skews the average income of a small town.'}]},
    {   'id': 'quiz-math-vectors-dot-products',
        'lesson_slug': 'math-vectors-dot-products',
        'title': 'Vectors & Dot Products Quiz',
        'passing_score': 70,
        'questions': [   {   'id': 'q1',
                             'type': 'multiple_choice',
                             'question': 'If two non-zero vectors u and v have a dot product u · v = 0, what does this '
                                         'indicate geometrically?',
                             'options': [   'They point in exactly the same direction',
                                            'They are orthogonal (perpendicular / 90 degrees apart with 0 similarity)',
                                            'One of the vectors has length zero',
                                            'They point in opposite directions (180 degrees)'],
                             'correct_answer': 1,
                             'points': 10,
                             'skill_tag': 'linear_algebra',
                             'explanation': 'When the dot product between two non-zero vectors is 0, cos(theta) = 0, '
                                            'meaning the angle between them is 90 degrees (orthogonal / independent).',
                             'hint': 'Recall that a dot product of 0 means 90 degree angle.'}]},
    {   'id': 'quiz-math-matrix-multiplication',
        'lesson_slug': 'math-matrix-multiplication',
        'title': 'Matrix Multiplication & Transformations Quiz',
        'passing_score': 70,
        'questions': [   {   'id': 'q1',
                             'type': 'multiple_choice',
                             'question': 'What is the primary geometric effect of multiplying a 2D data vector by a '
                                         '2x2 identity matrix [[1, 0], [0, 1]]?',
                             'options': [   'The vector is rotated 180 degrees',
                                            'The vector remains completely unchanged in position and length',
                                            "The vector's coordinates are doubled",
                                            'The vector collapses to the origin (0, 0)'],
                             'correct_answer': 1,
                             'points': 10,
                             'skill_tag': 'linear_algebra',
                             'explanation': 'The identity matrix is the matrix equivalent of the number 1. Multiplying '
                                            'any vector by the identity matrix leaves it unchanged.',
                             'hint': 'Identity matrix acts like multiplying by 1.'}]},
    {   'id': 'quiz-math-derivatives-gradients',
        'lesson_slug': 'math-derivatives-gradients',
        'title': 'Derivatives & Gradients Quiz',
        'passing_score': 70,
        'questions': [   {   'id': 'q1',
                             'type': 'multiple_choice',
                             'question': 'In Gradient Descent optimization, in which direction do we update model '
                                         'weights to reduce prediction error?',
                             'options': [   'In the direction of the gradient (+∇L) to go uphill',
                                            'In the opposite direction of the gradient (-∇L) to go downhill toward '
                                            'lowest error',
                                            'At a random 90-degree angle to the gradient',
                                            'Weights are never updated using the gradient'],
                             'correct_answer': 1,
                             'points': 10,
                             'skill_tag': 'calculus',
                             'explanation': 'The gradient vector points in the direction of steepest increase '
                                            '(uphill). Therefore, taking steps in the negative gradient direction '
                                            '(-∇L) takes us downhill toward minimum loss.',
                             'hint': 'We want to decrease error, so we move opposite to the steepest uphill '
                                     'direction.'}]},
    {   'id': 'quiz-math-chain-rule-backprop-math',
        'lesson_slug': 'math-chain-rule-backprop-math',
        'title': 'The Chain Rule Quiz',
        'passing_score': 70,
        'questions': [   {   'id': 'q1',
                             'type': 'multiple_choice',
                             'question': 'If y = g(u) and u = h(x), what is the Chain Rule formula for dy/dx?',
                             'options': ['(dy/du) + (du/dx)', '(dy/du) * (du/dx)', '(dy/du) / (du/dx)', 'dy - dx'],
                             'correct_answer': 1,
                             'points': 10,
                             'skill_tag': 'calculus',
                             'explanation': 'The Chain Rule states that the derivative of a composite function is the '
                                            'product of the intermediate derivatives: dy/dx = (dy/du) * (du/dx).',
                             'hint': 'Think of multiplying connected gears.'}]},
    {   'id': 'quiz-math-probability-bayes-theorem',
        'lesson_slug': 'math-probability-bayes-theorem',
        'title': "Probability & Bayes' Theorem Quiz",
        'passing_score': 70,
        'questions': [   {   'id': 'q1',
                             'type': 'multiple_choice',
                             'question': "In Bayes' Theorem P(A|B) = [P(B|A) * P(A)] / P(B), what is P(A) called?",
                             'options': [   'The Likelihood',
                                            'The Prior Probability (initial baseline belief before observing evidence '
                                            'B)',
                                            'The Posterior Probability',
                                            'The Marginal Variance'],
                             'correct_answer': 1,
                             'points': 10,
                             'skill_tag': 'probability',
                             'explanation': 'P(A) is the Prior Probability—our existing belief about A before any new '
                                            'evidence B is observed.',
                             'hint': 'It comes *prior* to observing new clues.'}]},
    {   'id': 'quiz-ml-linear-regression-ols',
        'lesson_slug': 'ml-linear-regression-ols',
        'title': 'Linear Regression & Loss Functions Quiz',
        'passing_score': 70,
        'questions': [   {   'id': 'q1',
                             'type': 'multiple_choice',
                             'question': 'In the linear regression equation y_hat = w · x + b, what does parameter b '
                                         'represent?',
                             'options': [   'The slope (rate of change per unit of x)',
                                            'The bias / y-intercept (the baseline prediction when input feature x is '
                                            '0)',
                                            'The total number of training rows',
                                            'The learning rate'],
                             'correct_answer': 1,
                             'points': 10,
                             'skill_tag': 'regression',
                             'explanation': 'Parameter b is the bias (or intercept). It shifts the line up or down so '
                                            'the model can make predictions when all input features x are zero.',
                             'hint': 'Think of y = mx + b where b is the y-intercept.'}]},
    {   'id': 'quiz-ml-gradient-descent-intuition',
        'lesson_slug': 'ml-gradient-descent-intuition',
        'title': 'Gradient Descent Mechanics Quiz',
        'passing_score': 70,
        'questions': [   {   'id': 'q1',
                             'type': 'multiple_choice',
                             'question': 'What happens when training a neural network with an excessively large '
                                         'learning rate (e.g. alpha = 100.0)?',
                             'options': [   'The model learns instantaneously on step 1',
                                            'The parameters overshoot the valley floor and loss diverges to infinity / '
                                            'NaN',
                                            'The model parameters freeze and make zero progress',
                                            'Memory usage doubles'],
                             'correct_answer': 1,
                             'points': 10,
                             'skill_tag': 'optimization',
                             'explanation': 'An excessively large learning rate causes huge leaps that bounce out of '
                                            'the loss valley, causing numerical overflow and divergent loss.',
                             'hint': 'Think of jumping so hard you fly off the mountain.'}]},
    {   'id': 'quiz-ml-logistic-regression-classification',
        'lesson_slug': 'ml-logistic-regression-classification',
        'title': 'Logistic Regression & Sigmoid Quiz',
        'passing_score': 70,
        'questions': [   {   'id': 'q1',
                             'type': 'multiple_choice',
                             'question': 'What is the output range of the standard Sigmoid activation function '
                                         'sigma(z)?',
                             'options': [   '[-1.0, 1.0]',
                                            '(0.0, 1.0) strictly between 0 and 1',
                                            '[0.0, infinity)',
                                            '(-infinity, +infinity)'],
                             'correct_answer': 1,
                             'points': 10,
                             'skill_tag': 'classification',
                             'explanation': 'Sigmoid squashes any real number from negative to positive infinity into '
                                            'a strict probability interval (0.0, 1.0).',
                             'hint': 'Probabilities must always be between 0% and 100%.'}]},
    {   'id': 'quiz-ml-decision-trees-entropy',
        'lesson_slug': 'ml-decision-trees-entropy',
        'title': 'Decision Trees & Entropy Quiz',
        'passing_score': 70,
        'questions': [   {   'id': 'q1',
                             'type': 'multiple_choice',
                             'question': 'If a subset of data at a tree leaf contains 100 samples and all 100 belong '
                                         "to the 'Spam' class, what is the Shannon Entropy of this node?",
                             'options': ['1.0', '0.0 (Completely Pure)', '0.5', '100.0'],
                             'correct_answer': 1,
                             'points': 10,
                             'skill_tag': 'decision_trees',
                             'explanation': 'When all items belong to a single class, there is zero uncertainty or '
                                            'disorder. Entropy is 0.0.',
                             'hint': 'Pure sets have zero disorder.'}]},
    {   'id': 'quiz-ml-kmeans-clustering-algorithm',
        'lesson_slug': 'ml-kmeans-clustering-algorithm',
        'title': 'K-Means Clustering Quiz',
        'passing_score': 70,
        'questions': [   {   'id': 'q1',
                             'type': 'multiple_choice',
                             'question': 'Is K-Means an example of Supervised or Unsupervised learning?',
                             'options': [   'Supervised (requires target labels y)',
                                            'Unsupervised (finds clusters in unlabeled data X)',
                                            'Reinforcement Learning',
                                            'Rule-based Expert System'],
                             'correct_answer': 1,
                             'points': 10,
                             'skill_tag': 'clustering',
                             'explanation': 'K-Means is an unsupervised algorithm because it groups raw data points '
                                            'based on geometric distance without requiring pre-existing ground truth '
                                            'labels.',
                             'hint': 'Clustering discovers patterns on its own without teacher labels.'}]},
    {   'id': 'quiz-dl-perceptron-forward-prop',
        'lesson_slug': 'dl-perceptron-forward-prop',
        'title': 'Artificial Neurons & Activations Quiz',
        'passing_score': 70,
        'questions': [   {   'id': 'q1',
                             'type': 'multiple_choice',
                             'question': 'What is the primary mathematical reason for using non-linear activation '
                                         'functions (like ReLU) in deep neural networks?',
                             'options': [   'To speed up matrix multiplication hardware',
                                            'To prevent multiple linear layers from collapsing into a single simple '
                                            'linear model, enabling complex pattern recognition',
                                            'To convert all numbers to integers',
                                            "To eliminate all negative numbers from the computer's memory"],
                             'correct_answer': 1,
                             'points': 10,
                             'skill_tag': 'neural_networks',
                             'explanation': 'Without non-linear activations, stacking 100 neural layers is '
                                            'mathematically equivalent to a single linear layer (W2 * W1 * x = '
                                            'W_combined * x). Non-linear activations allow networks to learn curved, '
                                            'complex boundaries.',
                             'hint': 'Without non-linearities, linear layers simply multiply into another straight '
                                     'line.'}]},
    {   'id': 'quiz-dl-activation-functions',
        'lesson_slug': 'dl-activation-functions',
        'title': 'Activation Functions Quiz',
        'passing_score': 70,
        'questions': [   {   'id': 'q1',
                             'type': 'multiple_choice',
                             'question': 'What is the output of ReLU(z) when z = -4.5?',
                             'options': ['-4.5', '0.0', '4.5', '1.0'],
                             'correct_answer': 1,
                             'points': 10,
                             'skill_tag': 'neural_networks',
                             'explanation': 'ReLU(z) = max(0, z). For any negative number, ReLU outputs 0.0.',
                             'hint': 'ReLU zeroes out all negative numbers.'}]},
    {   'id': 'quiz-dl-backpropagation-calculus',
        'lesson_slug': 'dl-backpropagation-calculus',
        'title': 'Backpropagation Quiz',
        'passing_score': 70,
        'questions': [   {   'id': 'q1',
                             'type': 'multiple_choice',
                             'question': 'During neural network training, in what order do information and gradients '
                                         'travel?',
                             'options': [   'Inputs travel forward to produce loss; error gradients travel backwards '
                                            'to update weights',
                                            'Gradients travel forward; inputs travel backwards',
                                            'Both travel forward simultaneously',
                                            'Weights update before the forward pass executes'],
                             'correct_answer': 0,
                             'points': 10,
                             'skill_tag': 'backpropagation',
                             'explanation': 'Inputs pass forward through layers to compute the output prediction and '
                                            'loss. The backward pass then propagates gradients from loss back through '
                                            'weights.',
                             'hint': 'Think of forward prediction followed by backward feedback.'}]},
    {   'id': 'quiz-dl-cnn-convolution-pooling',
        'lesson_slug': 'dl-cnn-convolution-pooling',
        'title': 'Convolutional Neural Networks (CNNs) Quiz',
        'passing_score': 70,
        'questions': [   {   'id': 'q1',
                             'type': 'multiple_choice',
                             'question': 'What is the primary function of Max Pooling layers in a CNN?',
                             'options': [   'To add more color channels to the image',
                                            'To reduce spatial dimensions (downsampling) while preserving the most '
                                            'prominent features',
                                            'To generate new images',
                                            'To compute cross-entropy loss'],
                             'correct_answer': 1,
                             'points': 10,
                             'skill_tag': 'computer_vision',
                             'explanation': 'Max Pooling downsamples feature maps by picking the highest activation in '
                                            'each small window, reducing computational load and providing spatial '
                                            'shift invariance.',
                             'hint': 'Max pooling shrinks the size while keeping the highest values.'}]},
    {   'id': 'quiz-genai-tokenization-embeddings',
        'lesson_slug': 'genai-tokenization-embeddings',
        'title': 'Tokenization & Embeddings Quiz',
        'passing_score': 70,
        'questions': [   {   'id': 'q1',
                             'type': 'multiple_choice',
                             'question': 'What is an embedding vector in modern Natural Language Processing?',
                             'options': [   'A file path on the hard drive',
                                            'A dense list of floating-point numbers where geometric proximity '
                                            'represents semantic meaning',
                                            'A single binary true/false flag',
                                            'An encrypted password hash'],
                             'correct_answer': 1,
                             'points': 10,
                             'skill_tag': 'nlp_embeddings',
                             'explanation': 'An embedding maps words, sentences, or images into a continuous '
                                            'multidimensional vector space where similar concepts cluster together '
                                            'geometrically.',
                             'hint': 'Think of coordinates on a high-dimensional concept map.'}]},
    {   'id': 'quiz-genai-self-attention-transformers',
        'lesson_slug': 'genai-self-attention-transformers',
        'title': 'Self-Attention & Transformers Quiz',
        'passing_score': 70,
        'questions': [   {   'id': 'q1',
                             'type': 'multiple_choice',
                             'question': 'In the Transformer attention equation Softmax(Q·Kᵀ / √d_k) · V, why do we '
                                         'divide the dot products by √d_k?',
                             'options': [   'To convert the matrix into text characters',
                                            'To scale dot product magnitudes and prevent vanishing gradients during '
                                            'Softmax backpropagation',
                                            'To remove punctuation marks from sentences',
                                            'To calculate the total number of words in the vocabulary'],
                             'correct_answer': 1,
                             'points': 10,
                             'skill_tag': 'transformers',
                             'explanation': 'In high dimensions d_k, dot products grow large in magnitude, which would '
                                            'push the Softmax function into flat regions with tiny gradients. Dividing '
                                            'by √d_k stabilizes variance to 1.0.',
                             'hint': 'Dividing by √d_k keeps numbers within a well-behaved range for Softmax.'}]},
    {   'id': 'quiz-genai-rag-architecture-pipeline',
        'lesson_slug': 'genai-rag-architecture-pipeline',
        'title': 'RAG Architecture Quiz',
        'passing_score': 70,
        'questions': [   {   'id': 'q1',
                             'type': 'multiple_choice',
                             'question': 'What is the primary benefit of Retrieval-Augmented Generation (RAG) over '
                                         "relying solely on a model's pre-trained weights?",
                             'options': [   'RAG makes the model run without using any electricity',
                                            'RAG grounds the model in up-to-date, verifiable external documents to '
                                            'reduce hallucinations',
                                            'RAG translates all text to Latin',
                                            'RAG removes the need for tokenizers'],
                             'correct_answer': 1,
                             'points': 10,
                             'skill_tag': 'rag_systems',
                             'explanation': 'RAG injects relevant text snippets from private databases directly into '
                                            'the prompt, giving the model current factual context and eliminating '
                                            'hallucinations.',
                             'hint': 'Think of an open-book exam where the model can read exact reference excerpts.'}]},
    {   'id': 'quiz-prompt-foundations-few-shot',
        'lesson_slug': 'prompt-foundations-few-shot',
        'title': 'Prompt Foundations & Few-Shot Quiz',
        'passing_score': 70,
        'questions': [   {   'id': 'q1',
                             'type': 'multiple_choice',
                             'question': 'What is Few-Shot Prompting?',
                             'options': [   'Running the model only a few times a day to save API costs',
                                            'Providing 2-3 input and expected output examples inside the prompt to '
                                            'demonstrate the target format',
                                            "Limiting the model's vocabulary to 100 words",
                                            'Fine-tuning model weights with backpropagation'],
                             'correct_answer': 1,
                             'points': 10,
                             'skill_tag': 'prompt_engineering',
                             'explanation': 'Few-shot prompting provides concrete examples of the task directly in the '
                                            "prompt context, guiding the model's format and style without updating "
                                            'model weights.',
                             'hint': 'Think of showing examples before asking the student to solve a problem.'}]},
    {   'id': 'quiz-prompt-chain-of-thought-reasoning',
        'lesson_slug': 'prompt-chain-of-thought-reasoning',
        'title': 'Chain-of-Thought Reasoning Quiz',
        'passing_score': 70,
        'questions': [   {   'id': 'q1',
                             'type': 'multiple_choice',
                             'question': "Why does adding 'Think step-by-step before answering' improve LLM accuracy "
                                         'on complex reasoning tasks?',
                             'options': [   "It doubles the computer's CPU clock speed",
                                            'It forces the model to generate intermediate reasoning tokens that act as '
                                            'a working memory scratchpad',
                                            'It automatically searches Google in the background',
                                            'It bypasses all safety filters'],
                             'correct_answer': 1,
                             'points': 10,
                             'skill_tag': 'prompt_engineering',
                             'explanation': 'LLMs predict token by token. Generating intermediate reasoning steps '
                                            'gives the model computational tokens to work out math and logic before '
                                            'emitting the final conclusion.',
                             'hint': 'It provides a scratchpad for step-by-step thinking.'}]},
    {   'id': 'quiz-prompt-ai-agents-tool-use',
        'lesson_slug': 'prompt-ai-agents-tool-use',
        'title': 'AI Autonomous Agents & ReAct Quiz',
        'passing_score': 70,
        'questions': [   {   'id': 'q1',
                             'type': 'multiple_choice',
                             'question': 'What are the core steps of the ReAct (Reason + Act) agent loop?',
                             'options': [   'Thought -> Action (Tool Call) -> Observation (Tool Output) -> Repeat / '
                                            'Answer',
                                            'Compile -> Link -> Execute -> Crash',
                                            'Download -> Extract -> Install -> Reboot',
                                            'Prompt -> Output -> Exit'],
                             'correct_answer': 0,
                             'points': 10,
                             'skill_tag': 'ai_agents',
                             'explanation': 'ReAct stands for Reason + Act: The agent reasons about its current state, '
                                            'calls an external tool, observes the result, and loops until the goal is '
                                            'achieved.',
                             'hint': 'Reason, Act, Observe, Repeat.'}]},
    {   'id': 'quiz-web-how-the-web-works',
        'lesson_slug': 'web-how-the-web-works',
        'title': 'Web Architecture & HTTP Protocols Quiz',
        'passing_score': 70,
        'questions': [   {   'id': 'q1',
                             'type': 'multiple_choice',
                             'question': 'What is the primary role of DNS (Domain Name System) on the web?',
                             'options': [   'Translates human-readable domain names (like example.com) into machine IP '
                                            'addresses (like 93.184.216.34)',
                                            'Encrypts database passwords',
                                            'Renders HTML in the browser canvas',
                                            'Compiles TypeScript into JavaScript'],
                             'correct_answer': 0,
                             'points': 10,
                             'skill_tag': 'web_foundations',
                             'explanation': 'DNS acts as the phonebook of the internet, resolving domain names into '
                                            'numerical IP addresses.',
                             'hint': 'Think of an internet phonebook.'}]},
    {   'id': 'quiz-web-semantic-html5-tags',
        'lesson_slug': 'web-semantic-html5-tags',
        'title': 'Semantic HTML5 Architecture Quiz',
        'passing_score': 70,
        'questions': [   {   'id': 'q1',
                             'type': 'multiple_choice',
                             'question': 'Which HTML5 tag represents self-contained content that can be syndicated '
                                         'independently (such as a blog post or tweet card)?',
                             'options': ['<article>', '<div>', '<span>', '<header>'],
                             'correct_answer': 0,
                             'points': 10,
                             'skill_tag': 'html5_semantics',
                             'explanation': '<article> is used for self-contained, standalone content suitable for '
                                            'syndication or RSS readers.',
                             'hint': 'Think of a newspaper article.'}]},
    {   'id': 'quiz-web-forms-validation-accessibility',
        'lesson_slug': 'web-forms-validation-accessibility',
        'title': 'Forms & ARIA Accessibility Quiz',
        'passing_score': 70,
        'questions': [   {   'id': 'q1',
                             'type': 'multiple_choice',
                             'question': 'Why is associating a <label for="id"> with an <input id="id"> critical for '
                                         'web accessibility?',
                             'options': [   'It allows screen readers to announce the field name when focused and '
                                            'expands the clickable target area',
                                            'It speeds up network bandwidth',
                                            'It automatically submits the form to the backend',
                                            'It disables browser cookies'],
                             'correct_answer': 0,
                             'points': 10,
                             'skill_tag': 'web_accessibility',
                             'explanation': 'Explicit label associations enable assistive technology to read inputs '
                                            'aloud and allow users to click the text label to focus the input.',
                             'hint': 'It aids screen readers and expands tap targets.'}]},
    {   'id': 'quiz-web-css-box-model-cascade',
        'lesson_slug': 'web-css-box-model-cascade',
        'title': 'CSS Box Model & Specificity Quiz',
        'passing_score': 70,
        'questions': [   {   'id': 'q1',
                             'type': 'multiple_choice',
                             'question': 'When using `box-sizing: border-box` in CSS, what is included inside the '
                                         "element's declared width?",
                             'options': [   'Content only (padding and border add extra width)',
                                            'Content, Padding, and Border (padding and border do NOT expand total '
                                            'width)',
                                            'Margin and Padding only',
                                            'Border and Margin only'],
                             'correct_answer': 1,
                             'points': 10,
                             'skill_tag': 'css_box_model',
                             'explanation': 'With border-box, the declared width absorbs padding and border, '
                                            'eliminating unexpected overflow.',
                             'hint': 'Border-box absorbs padding inside the box.'}]},
    {   'id': 'quiz-web-css-flexbox-grid-mastery',
        'lesson_slug': 'web-css-flexbox-grid-mastery',
        'title': 'Flexbox & CSS Grid Mastery Quiz',
        'passing_score': 70,
        'questions': [   {   'id': 'q1',
                             'type': 'multiple_choice',
                             'question': 'What is the key architectural difference between CSS Flexbox and CSS Grid?',
                             'options': [   'Flexbox is designed for 1-dimensional layouts (row OR column), while CSS '
                                            'Grid is designed for 2-dimensional layouts (rows AND columns '
                                            'simultaneously)',
                                            'Flexbox only works in dark mode',
                                            'CSS Grid cannot use padding',
                                            'Flexbox requires JavaScript'],
                             'correct_answer': 0,
                             'points': 10,
                             'skill_tag': 'css_flexbox_grid',
                             'explanation': 'Flexbox handles 1D linear alignment, whereas CSS Grid controls '
                                            'simultaneous 2D row/column matrices.',
                             'hint': '1D vs 2D layout models.'}]},
    {   'id': 'quiz-web-css-responsive-animations',
        'lesson_slug': 'web-css-responsive-animations',
        'title': 'Responsive Units & 60fps Animations Quiz',
        'passing_score': 70,
        'questions': [   {   'id': 'q1',
                             'type': 'multiple_choice',
                             'question': 'Which CSS properties run directly on the GPU compositor thread without '
                                         'triggering expensive CPU layout recalculations?',
                             'options': [   '`transform` and `opacity`',
                                            '`width` and `height`',
                                            '`margin-top` and `left`',
                                            '`font-size` and `border-width`'],
                             'correct_answer': 0,
                             'points': 10,
                             'skill_tag': 'css_animations',
                             'explanation': 'Transform and opacity bypass the layout/paint steps and execute on the '
                                            'GPU compositor for 60fps animations.',
                             'hint': 'Transform and opacity are hardware accelerated.'}]},
    {   'id': 'quiz-web-js-execution-scope-closures',
        'lesson_slug': 'web-js-execution-scope-closures',
        'title': 'JavaScript Closures & Execution Scope Quiz',
        'passing_score': 70,
        'questions': [   {   'id': 'q1',
                             'type': 'multiple_choice',
                             'question': 'What is a closure in JavaScript?',
                             'options': [   'A function bundled together with references to its lexical environment, '
                                            'allowing it to remember outer variables even after the outer function has '
                                            'returned',
                                            'A syntax error when missing a closing bracket',
                                            'A way to terminate an infinite loop',
                                            'A method to close browser tabs'],
                             'correct_answer': 0,
                             'points': 10,
                             'skill_tag': 'javascript_internals',
                             'explanation': 'Closures allow inner functions to retain access to enclosing outer scope '
                                            'variables across memory lifetimes.',
                             'hint': 'Think of the backpack analogy retaining outer variables.'}]},
    {   'id': 'quiz-web-js-event-loop-promises-async',
        'lesson_slug': 'web-js-event-loop-promises-async',
        'title': 'Event Loop & Async Promises Quiz',
        'passing_score': 70,
        'questions': [   {   'id': 'q1',
                             'type': 'multiple_choice',
                             'question': 'In the JavaScript event loop, which queue has higher priority and executes '
                                         'first when the call stack clears?',
                             'options': [   'Microtask Queue (Promise callbacks, queueMicrotask)',
                                            'Macrotask Queue (setTimeout, setInterval)',
                                            'Render Queue',
                                            'Garbage Collector'],
                             'correct_answer': 0,
                             'points': 10,
                             'skill_tag': 'javascript_async',
                             'explanation': 'Microtasks (resolved Promise handlers) are drained completely before the '
                                            'next macrotask (timer) is executed.',
                             'hint': 'Microtasks run before macrotasks.'}]},
    {   'id': 'quiz-web-js-dom-events-delegation',
        'lesson_slug': 'web-js-dom-events-delegation',
        'title': 'DOM Traversal & Event Delegation Quiz',
        'passing_score': 70,
        'questions': [   {   'id': 'q1',
                             'type': 'multiple_choice',
                             'question': 'Why is Event Delegation more performant than attaching individual listeners '
                                         'to 1,000 table rows?',
                             'options': [   'It leverages event bubbling to handle all child clicks from a single '
                                            'parent listener, saving heap memory and automatically supporting new rows',
                                            'It bypasses the JavaScript single thread',
                                            'It forces hardware GPU acceleration',
                                            'It compiles JavaScript into C++'],
                             'correct_answer': 0,
                             'points': 10,
                             'skill_tag': 'dom_manipulation',
                             'explanation': 'Attaching one parent listener catches bubbled events from any child, '
                                            'dramatically cutting memory usage.',
                             'hint': 'One parent listener handles all children via event bubbling.'}]},
    {   'id': 'quiz-web-react-jsx-vdom-components',
        'lesson_slug': 'web-react-jsx-vdom-components',
        'title': 'React 18 JSX & Virtual DOM Diffing Quiz',
        'passing_score': 70,
        'questions': [   {   'id': 'q1',
                             'type': 'multiple_choice',
                             'question': 'Why does React require a unique `key` prop when rendering dynamic arrays of '
                                         'elements?',
                             'options': [   'It helps the Virtual DOM diffing algorithm uniquely track which items '
                                            'were added, removed, or reordered without re-rendering the whole list',
                                            'It is used for database indexing',
                                            'It encrypts array contents',
                                            'It determines CSS z-index'],
                             'correct_answer': 0,
                             'points': 10,
                             'skill_tag': 'react_core',
                             'explanation': 'Keys give React stable element identities to perform optimal '
                                            'minimum-mutation diffs during list reconciliation.',
                             'hint': 'Keys identify items across list re-renders.'}]},
    {   'id': 'quiz-web-react-hooks-deep-dive',
        'lesson_slug': 'web-react-hooks-deep-dive',
        'title': 'React 18 Hooks & Memoization Quiz',
        'passing_score': 70,
        'questions': [   {   'id': 'q1',
                             'type': 'multiple_choice',
                             'question': 'What is the primary purpose of `useCallback` in React?',
                             'options': [   'Memoizes a function definition between renders so child components '
                                            "receiving it as a prop don't re-render unnecessarily",
                                            'Calls an API endpoint in the background',
                                            'Creates a timer loop',
                                            'Renders JSX to HTML strings'],
                             'correct_answer': 0,
                             'points': 10,
                             'skill_tag': 'react_hooks',
                             'explanation': 'useCallback caches function instances between re-renders to maintain '
                                            'referential equality for memoized children.',
                             'hint': 'It preserves function identity across re-renders.'}]},
    {   'id': 'quiz-web-react-state-routing-zustand',
        'lesson_slug': 'web-react-state-routing-zustand',
        'title': 'Global State & Client Routing Quiz',
        'passing_score': 70,
        'questions': [   {   'id': 'q1',
                             'type': 'multiple_choice',
                             'question': 'What advantage does Zustand offer over standard React Context API for global '
                                         'application state?',
                             'options': [   'Components can subscribe to atomic state slices without re-rendering when '
                                            'unrelated state properties change',
                                            'It requires a Redux boilerplate boilerplate reducer',
                                            'It only works on mobile devices',
                                            'It stores data in cookies only'],
                             'correct_answer': 0,
                             'points': 10,
                             'skill_tag': 'react_state_management',
                             'explanation': 'Zustand provides selective atomic subscriptions, eliminating the '
                                            'full-tree re-render issues of wide Context providers.',
                             'hint': 'Selective atomic subscriptions prevent redundant re-renders.'}]},
    {   'id': 'quiz-web-nodejs-express-middleware',
        'lesson_slug': 'web-nodejs-express-middleware',
        'title': 'Node.js & Express Middleware Quiz',
        'passing_score': 70,
        'questions': [   {   'id': 'q1',
                             'type': 'multiple_choice',
                             'question': 'What happens if an Express middleware does not call `next()` or send a '
                                         'response with `res.json()`?',
                             'options': [   'The client HTTP request will hang indefinitely until timing out',
                                            'The server will immediately crash and reboot',
                                            'The database will automatically rollback',
                                            'The request will jump to the next route automatically'],
                             'correct_answer': 0,
                             'points': 10,
                             'skill_tag': 'nodejs_express',
                             'explanation': 'Express middleware must either call next() to advance the pipeline or '
                                            'terminate the request by sending a response.',
                             'hint': 'The pipeline stops and the request hangs.'}]},
    {   'id': 'quiz-web-jwt-auth-security-bcrypt',
        'lesson_slug': 'web-jwt-auth-security-bcrypt',
        'title': 'JWT Auth & Web Security Quiz',
        'passing_score': 70,
        'questions': [   {   'id': 'q1',
                             'type': 'multiple_choice',
                             'question': 'Why is storing JWT auth tokens in `httpOnly` secure cookies safer than '
                                         'localStorage?',
                             'options': [   '`httpOnly` cookies cannot be accessed by JavaScript, protecting them from '
                                            'Cross-Site Scripting (XSS) token theft',
                                            'Cookies are stored in RAM only',
                                            'localStorage is limited to 10 bytes',
                                            'Cookies bypass CORS rules'],
                             'correct_answer': 0,
                             'points': 10,
                             'skill_tag': 'web_security',
                             'explanation': 'httpOnly cookies shield sensitive session credentials from malicious '
                                            'scripts injected via XSS vulnerabilities.',
                             'hint': 'JavaScript cannot read httpOnly cookies.'}]},
    {   'id': 'quiz-web-db-mongodb-postgresql-crud',
        'lesson_slug': 'web-db-mongodb-postgresql-crud',
        'title': 'Databases & CRUD Optimization Quiz',
        'passing_score': 70,
        'questions': [   {   'id': 'q1',
                             'type': 'multiple_choice',
                             'question': 'Why should database queries always use parameterized values (e.g. `SELECT * '
                                         'FROM users WHERE id = $1`) instead of string concatenation?',
                             'options': [   'To completely prevent SQL injection attacks by treating user input '
                                            'strictly as literal data rather than executable code',
                                            'To make queries run on the client GPU',
                                            'To format the output as JSON automatically',
                                            'To compress the database on disk'],
                             'correct_answer': 0,
                             'points': 10,
                             'skill_tag': 'database_crud',
                             'explanation': 'Parameterized queries separate SQL structure from user input, making SQL '
                                            'injection impossible.',
                             'hint': 'It treats input strictly as data, preventing SQL injection.'}]},
    {   'id': 'quiz-web-nextjs-ssr-ssg-hydration',
        'lesson_slug': 'web-nextjs-ssr-ssg-hydration',
        'title': 'Next.js SSR & Hydration Quiz',
        'passing_score': 70,
        'questions': [   {   'id': 'q1',
                             'type': 'multiple_choice',
                             'question': "What is 'Client Hydration' in Server-Side Rendered (SSR) React applications?",
                             'options': [   'The process where client-side JavaScript attaches event listeners to '
                                            'pre-rendered server HTML to make it interactive',
                                            'Downloading water reminder notifications',
                                            'Cleaning up unmounted component memory',
                                            'Compressing image assets into WebP'],
                             'correct_answer': 0,
                             'points': 10,
                             'skill_tag': 'nextjs_ssr',
                             'explanation': 'Hydration brings static server-rendered HTML alive by attaching React '
                                            'state and event handlers in the browser.',
                             'hint': 'Attaching event handlers to server HTML.'}]},
    {   'id': 'quiz-web-performance-core-web-vitals',
        'lesson_slug': 'web-performance-core-web-vitals',
        'title': 'Core Web Vitals & Performance Quiz',
        'passing_score': 70,
        'questions': [   {   'id': 'q1',
                             'type': 'multiple_choice',
                             'question': 'How do you prevent Cumulative Layout Shift (CLS) when loading responsive '
                                         'images?',
                             'options': [   'Always set explicit `width` and `height` aspect-ratio attributes on '
                                            '`<img>` tags so the browser reserves layout space before download',
                                            'Use PNG instead of JPEG',
                                            'Load all images on startup',
                                            'Remove CSS styles'],
                             'correct_answer': 0,
                             'points': 10,
                             'skill_tag': 'web_performance',
                             'explanation': 'Explicit width/height attributes allow the browser layout engine to '
                                            'allocate space immediately, preventing jumpy shifts.',
                             'hint': 'Reserve space with explicit width and height attributes.'}]},
    {   'id': 'quiz-web-websockets-realtime-redis-caching',
        'lesson_slug': 'web-websockets-realtime-redis-caching',
        'title': 'Real-Time WebSockets & Redis Caching Quiz',
        'passing_score': 70,
        'questions': [   {   'id': 'q1',
                             'type': 'multiple_choice',
                             'question': 'In the Cache-Aside pattern with Redis, what happens when a requested item is '
                                         'NOT found in the cache (Cache Miss)?',
                             'options': [   'The application queries the primary database, returns data to the user, '
                                            'and writes the result into Redis with a TTL for future requests',
                                            'The server throws a 500 error',
                                            'The client disconnects',
                                            'Redis clears all memory'],
                             'correct_answer': 0,
                             'points': 10,
                             'skill_tag': 'realtime_caching',
                             'explanation': 'On a cache miss, data is read from the primary database and cached in '
                                            'Redis with a TTL to accelerate future reads.',
                             'hint': 'Read from DB and populate Redis with a TTL.'}]},
    {   'id': 'quiz-app-foundations-native-bridge',
        'lesson_slug': 'app-foundations-native-bridge',
        'title': 'React Native Bridge & Primitives Quiz',
        'passing_score': 70,
        'questions': [   {   'id': 'q1',
                             'type': 'multiple_choice',
                             'question': "What does React Native's `<View>` component render under the hood on iOS and "
                                         'Android devices?',
                             'options': [   'A browser <div> element inside a hidden WebView',
                                            'Genuine native platform views: `UIView` on iOS and `ViewGroup` on Android',
                                            'A canvas bitmap image',
                                            'An HTML iframe'],
                             'correct_answer': 1,
                             'points': 10,
                             'skill_tag': 'mobile_native_bridge',
                             'explanation': 'React Native communicates across the bridge / JSI to instantiate genuine '
                                            'native platform views (`UIView` on iOS and `ViewGroup` on Android), '
                                            'giving true native performance and platform feel.',
                             'hint': 'Think about what makes React Native apps look and feel native instead of '
                                     'web-based.'},
                         {   'id': 'q2',
                             'type': 'true_false',
                             'question': 'In React Native, plain text strings can be placed directly inside a `<View>` '
                                         'without wrapping them in a `<Text>` component.',
                             'options': ['True', 'False'],
                             'correct_answer': 1,
                             'points': 10,
                             'skill_tag': 'mobile_native_bridge',
                             'explanation': 'False. In React Native, all raw text strings must be wrapped in a '
                                            '`<Text>` component, otherwise React Native will throw a runtime error.'}]},
    {   'id': 'quiz-app-viewport-density-safe-area',
        'lesson_slug': 'app-viewport-density-safe-area',
        'title': 'Screen Densities & Safe Areas Quiz',
        'passing_score': 70,
        'questions': [   {   'id': 'q1',
                             'type': 'multiple_choice',
                             'question': 'Why do mobile operating systems use Density-Independent Pixels (dp / pt) '
                                         'instead of physical screen pixels?',
                             'options': [   'To ensure UI buttons and text maintain the exact same physical finger '
                                            'size across screens of different pixel densities (1x, 2x, 3x)',
                                            'To make the screen brighter',
                                            'To save cellular data',
                                            'Because physical pixels do not exist on phones'],
                             'correct_answer': 0,
                             'points': 10,
                             'skill_tag': 'mobile_safe_area',
                             'explanation': 'Density-independent points scale automatically so a 48pt button remains a '
                                            'comfortable finger-tap size on high-DPI Super Retina screens.',
                             'hint': 'Consider what happens if a button had fixed 50 physical pixels on a 4K phone '
                                     'display.'}]},
    {   'id': 'quiz-app-mobile-flexbox-touch-targets',
        'lesson_slug': 'app-mobile-flexbox-touch-targets',
        'title': 'Mobile Flexbox & Touch Targets Quiz',
        'passing_score': 70,
        'questions': [   {   'id': 'q1',
                             'type': 'multiple_choice',
                             'question': 'What is the default `flexDirection` of `<View>` components in React Native, '
                                         'and what is the minimum recommended touch target size in Apple HIG / '
                                         'Material Design?',
                             'options': [   '`row` and 20x20 pt',
                                            '`column` and 44x44 to 48x48 dp',
                                            '`grid` and 100x100 dp',
                                            '`inline` and 10x10 pt'],
                             'correct_answer': 1,
                             'points': 10,
                             'skill_tag': 'mobile_touch_targets',
                             'explanation': 'React Native defaults to `column` layout for vertical portrait screens, '
                                            'and human touch accessibility guidelines require a minimum 44x44 pt '
                                            '(Apple) or 48x48 dp (Google) touch target.',
                             'hint': 'Phones are portrait-oriented and human thumbs need at least 44-48dp.'}]},
    {   'id': 'quiz-app-navigation-stacks-tabs',
        'lesson_slug': 'app-navigation-stacks-tabs',
        'title': 'Mobile Navigation Stacks & Tabs Quiz',
        'passing_score': 70,
        'questions': [   {   'id': 'q1',
                             'type': 'multiple_choice',
                             'question': 'What happens to the previous screen when a user navigates to a new details '
                                         'screen using a React Navigation Stack Navigator?',
                             'options': [   'It is completely unmounted and destroyed from memory',
                                            'It remains mounted underneath in the LIFO stack with its scroll position '
                                            'and state preserved',
                                            'It is saved to local storage and reloaded on back',
                                            'The browser refreshes'],
                             'correct_answer': 1,
                             'points': 10,
                             'skill_tag': 'mobile_navigation_stacks',
                             'explanation': 'Stack navigators push new screens on top of the stack while keeping '
                                            'previous screens alive in memory, ensuring instant back navigation with '
                                            'preserved scroll state.',
                             'hint': 'Think of the pancake stack analogy.'}]},
    {   'id': 'quiz-app-gestures-pan-swipe-pinch',
        'lesson_slug': 'app-gestures-pan-swipe-pinch',
        'title': 'Mobile Gestures & Pan Handling Quiz',
        'passing_score': 70,
        'questions': [   {   'id': 'q1',
                             'type': 'multiple_choice',
                             'question': 'Why does React Native Gesture Handler (RNGH) run gesture recognition on the '
                                         'native OS UI thread instead of the JS thread?',
                             'options': [   'To avoid frame drops and lag when continuous drag/pan touch events occur, '
                                            'even if the JS thread is busy',
                                            'Because JavaScript does not have math operations',
                                            'To reduce battery consumption by turning off the GPU',
                                            'To prevent users from swiping'],
                             'correct_answer': 0,
                             'points': 10,
                             'skill_tag': 'mobile_gestures',
                             'explanation': 'Running gesture recognizers directly on native threads eliminates bridge '
                                            'traffic during rapid touch gestures, guaranteeing smooth 60fps tracking.',
                             'hint': 'Zero bridge latency during continuous touch movement.'}]},
    {   'id': 'quiz-app-reanimated-60fps-physics',
        'lesson_slug': 'app-reanimated-60fps-physics',
        'title': 'Reanimated 3 & Spring Physics Quiz',
        'passing_score': 70,
        'questions': [   {   'id': 'q1',
                             'type': 'multiple_choice',
                             'question': "What is a 'Worklet' in React Native Reanimated 3?",
                             'options': [   'A background thread that mines cryptocurrency',
                                            'A tiny JavaScript function compiled to run synchronously on the native UI '
                                            'rendering thread',
                                            'An HTML worker iframe',
                                            'A CSS stylesheet'],
                             'correct_answer': 1,
                             'points': 10,
                             'skill_tag': 'mobile_reanimated',
                             'explanation': 'Worklets are JavaScript functions executed directly inside the UI thread '
                                            'runtime to drive 60fps/120fps physics animations without crossing the '
                                            'bridge.',
                             'hint': 'Functions running on the native UI thread.'}]},
    {   'id': 'quiz-app-offline-first-mmkv-storage',
        'lesson_slug': 'app-offline-first-mmkv-storage',
        'title': 'Offline-First Storage & MMKV Quiz',
        'passing_score': 70,
        'questions': [   {   'id': 'q1',
                             'type': 'multiple_choice',
                             'question': 'Why is Tencent MMKV significantly faster than traditional AsyncStorage in '
                                         'React Native?',
                             'options': [   'MMKV uses C++ memory-mapped files (mmap) to read and write synchronously '
                                            'via JSI in <0.1ms without bridge serialization',
                                            'MMKV compresses files with zip',
                                            'MMKV deletes data automatically',
                                            'MMKV only runs on desktop'],
                             'correct_answer': 0,
                             'points': 10,
                             'skill_tag': 'mobile_mmkv_storage',
                             'explanation': 'MMKV uses memory mapping (mmap) and JSI to perform sub-millisecond '
                                            'synchronous reads and writes without JSON bridge serialization.',
                             'hint': 'C++ memory mapping directly to RAM.'}]},
    {   'id': 'quiz-app-sqlite-local-relational-db',
        'lesson_slug': 'app-sqlite-local-relational-db',
        'title': 'Mobile Embedded SQLite Quiz',
        'passing_score': 70,
        'questions': [   {   'id': 'q1',
                             'type': 'multiple_choice',
                             'question': 'When is an embedded SQLite database preferred over simple key-value storage '
                                         '(like MMKV or AsyncStorage) on mobile?',
                             'options': [   'When managing thousands of structured records that require indexed '
                                            'filtering, SQL JOINs, pagination, and ACID transactions',
                                            'Only when the app is connected to high-speed 5G internet',
                                            'When storing a single boolean user setting',
                                            'To store user passwords in plain text'],
                             'correct_answer': 0,
                             'points': 10,
                             'skill_tag': 'mobile_sqlite',
                             'explanation': 'SQLite allows querying, indexing, and paginating thousands of local '
                                            'records without loading giant JSON blobs into device RAM.',
                             'hint': 'Think of large structured datasets requiring indexed queries.'}]},
    {   'id': 'quiz-app-device-hardware-camera-location',
        'lesson_slug': 'app-device-hardware-camera-location',
        'title': 'Mobile Hardware & Biometrics Quiz',
        'passing_score': 70,
        'questions': [   {   'id': 'q1',
                             'type': 'multiple_choice',
                             'question': 'Where should biometric authentication (Apple FaceID / TouchID) cryptographic '
                                         'keys be stored on mobile hardware?',
                             'options': [   'Inside a public text file in the documents directory',
                                            'Inside the hardware Secure Enclave / Android KeyStore coprocessor',
                                            'In local browser cookies',
                                            'On the camera sensor'],
                             'correct_answer': 1,
                             'points': 10,
                             'skill_tag': 'mobile_native_hardware',
                             'explanation': 'The hardware Secure Enclave isolated chip securely verifies biometric '
                                            'matches and unlocks encryption keys without exposing raw biometric scans '
                                            'to the app.',
                             'hint': 'Hardware isolated security chip.'}]},
    {   'id': 'quiz-app-flutter-widget-tree-rendering',
        'lesson_slug': 'app-flutter-widget-tree-rendering',
        'title': 'Flutter Impeller & Widget Tree Quiz',
        'passing_score': 70,
        'questions': [   {   'id': 'q1',
                             'type': 'multiple_choice',
                             'question': "How does Google Flutter's rendering architecture differ from React Native?",
                             'options': [   'Flutter paints every single pixel directly onto a Skia/Impeller canvas '
                                            'via AOT-compiled ARM machine code rather than wrapping OEM platform '
                                            'widgets',
                                            'Flutter uses HTML5 iframes',
                                            'Flutter runs inside a Node.js server',
                                            'Flutter cannot run on iOS'],
                             'correct_answer': 0,
                             'points': 10,
                             'skill_tag': 'flutter_widget_tree',
                             'explanation': 'Flutter renders its own widgets directly to the GPU via Impeller, '
                                            'compiling Dart code Ahead-Of-Time (AOT) to native machine code.',
                             'hint': 'Direct pixel painting with Impeller rendering engine.'}]},
    {   'id': 'quiz-app-flutter-stateful-lifecycle',
        'lesson_slug': 'app-flutter-stateful-lifecycle',
        'title': 'Flutter StatefulWidget Lifecycle Quiz',
        'passing_score': 70,
        'questions': [   {   'id': 'q1',
                             'type': 'multiple_choice',
                             'question': 'Which lifecycle method in a Flutter State class is called when the widget is '
                                         'permanently removed from the widget tree and must be used to cancel streams?',
                             'options': ['`initState()`', '`dispose()`', '`build()`', '`setState()`'],
                             'correct_answer': 1,
                             'points': 10,
                             'skill_tag': 'flutter_state_lifecycle',
                             'explanation': '`dispose()` is invoked upon widget destruction to close controllers, '
                                            'cancel timer intervals, and release stream subscriptions.',
                             'hint': 'The cleanup hook to prevent memory leaks.'}]},
    {   'id': 'quiz-app-flutter-bloc-state-streams',
        'lesson_slug': 'app-flutter-bloc-state-streams',
        'title': 'Flutter BLoC Pattern Quiz',
        'passing_score': 70,
        'questions': [   {   'id': 'q1',
                             'type': 'multiple_choice',
                             'question': 'In the Flutter BLoC pattern, what are the two core reactive primitives '
                                         'flowing into and out of the BLoC engine?',
                             'options': [   'Incoming Events from the UI -> Outgoing States to the UI via Dart Streams',
                                            'HTML -> CSS',
                                            'SQL queries -> CSV exports',
                                            'Getters -> Setters'],
                             'correct_answer': 0,
                             'points': 10,
                             'skill_tag': 'flutter_bloc_pattern',
                             'explanation': 'The BLoC pattern transforms incoming Events (e.g. `FetchCourses`) into '
                                            'outgoing States (e.g. `CoursesLoaded`) using unidirectional async '
                                            'streams.',
                             'hint': 'Unidirectional flow from Events to States.'}]},
    {   'id': 'quiz-app-push-notifications-fcm-apns',
        'lesson_slug': 'app-push-notifications-fcm-apns',
        'title': 'Remote Push Notifications Quiz',
        'passing_score': 70,
        'questions': [   {   'id': 'q1',
                             'type': 'multiple_choice',
                             'question': 'How does a backend server deliver a push notification to a specific physical '
                                         'smartphone when the app is completely closed?',
                             'options': [   "By sending an HTTP/2 payload to Apple APNs or Google FCM using the user's "
                                            'unique Device Push Token',
                                            "By making an HTTP request directly to the phone's cellular IP address",
                                            'By sending an SMS text message',
                                            'By broadcasting to all phones in the country'],
                             'correct_answer': 0,
                             'points': 10,
                             'skill_tag': 'mobile_push_notifications',
                             'explanation': 'APNs (Apple) and FCM (Google) maintain a single low-power persistent '
                                            'connection to devices, delivering backend payloads directed at registered '
                                            'device tokens.',
                             'hint': 'Apple APNs and Google FCM central gateways.'}]},
    {   'id': 'quiz-app-background-tasks-worker-sync',
        'lesson_slug': 'app-background-tasks-worker-sync',
        'title': 'Background Sync Workers Quiz',
        'passing_score': 70,
        'questions': [   {   'id': 'q1',
                             'type': 'multiple_choice',
                             'question': 'Why do mobile operating systems enforce strict time limits (e.g. 30 seconds) '
                                         'on background fetch workers?',
                             'options': [   'To prevent rogue apps from draining battery, overheating the device, and '
                                            'burning cellular data in the background',
                                            'Because cellular towers turn off at night',
                                            'Because RAM is cleared every minute',
                                            'To slow down competitor apps'],
                             'correct_answer': 0,
                             'points': 10,
                             'skill_tag': 'mobile_background_workers',
                             'explanation': 'Battery preservation is paramount for mobile OSs; background tasks must '
                                            'execute quickly and yield CPU resources back to the scheduler.',
                             'hint': 'Battery life and thermal protection.'}]},
    {   'id': 'quiz-app-appstore-playstore-deployment',
        'lesson_slug': 'app-appstore-playstore-deployment',
        'title': 'Mobile App Store Release Quiz',
        'passing_score': 70,
        'questions': [   {   'id': 'q1',
                             'type': 'multiple_choice',
                             'question': 'What is the purpose of iOS Provisioning Profiles and Android Keystore '
                                         'certificates during app deployment?',
                             'options': [   'To cryptographically sign the compiled application binary, proving '
                                            'authenticity and preventing tampering',
                                            'To compress images into WebP',
                                            'To translate JavaScript to HTML',
                                            "To format the user's device"],
                             'correct_answer': 0,
                             'points': 10,
                             'skill_tag': 'mobile_app_store_release',
                             'explanation': 'Code signing certificates guarantee that the binary originates from an '
                                            'authorized developer and has not been corrupted or tampered with.',
                             'hint': 'Cryptographic proof of developer identity and binary integrity.'}]},
    {   'id': 'quiz-sys-client-server-scaling',
        'lesson_slug': 'sys-client-server-scaling',
        'title': 'Scaling Up vs Scaling Out Quiz',
        'passing_score': 70,
        'questions': [   {   'id': 'q1',
                             'type': 'multiple_choice',
                             'question': 'What is the primary advantage of Horizontal Scaling (Scale Out) over '
                                         'Vertical Scaling (Scale Up)?',
                             'options': [   'Horizontal scaling avoids single points of failure (SPOF) and provides '
                                            'virtually unbounded scale by adding commodity servers',
                                            'Horizontal scaling never requires load balancers',
                                            'Horizontal scaling reduces server count to 1',
                                            'Vertical scaling is always cheaper'],
                             'correct_answer': 0,
                             'points': 10,
                             'skill_tag': 'sys_scaling_foundations',
                             'explanation': 'Horizontal scaling distributes traffic across many redundant nodes, '
                                            'eliminating single points of failure and allowing dynamic autoscaling.',
                             'hint': 'Adding more machines eliminates single points of failure.'}]},
    {   'id': 'quiz-sys-monolith-to-microservices',
        'lesson_slug': 'sys-monolith-to-microservices',
        'title': 'Microservices Architecture Quiz',
        'passing_score': 70,
        'questions': [   {   'id': 'q1',
                             'type': 'multiple_choice',
                             'question': 'What is a core architectural rule of microservices regarding database '
                                         'persistence?',
                             'options': [   'All 50 microservices must share a single monolithic PostgreSQL database '
                                            'table',
                                            'Each microservice should own its own private database and communicate '
                                            'with other services only via APIs or events',
                                            'Microservices cannot use databases',
                                            'Databases must be restarted on every request'],
                             'correct_answer': 1,
                             'points': 10,
                             'skill_tag': 'sys_microservices_architecture',
                             'explanation': 'Database-per-Service ensures loose coupling, independent schema '
                                            'migrations, and fault isolation between teams.',
                             'hint': 'Database-per-service pattern.'}]},
    {   'id': 'quiz-sys-cap-theorem-pacelc',
        'lesson_slug': 'sys-cap-theorem-pacelc',
        'title': 'CAP Theorem & PACELC Quiz',
        'passing_score': 70,
        'questions': [   {   'id': 'q1',
                             'type': 'multiple_choice',
                             'question': 'According to the CAP theorem, what trade-off must a distributed system make '
                                         'when a network partition (P) occurs?',
                             'options': [   'Between Consistency (CP) and Availability (AP)',
                                            'Between CPU speed and RAM size',
                                            'Between IPv4 and IPv6',
                                            'Between JSON and XML'],
                             'correct_answer': 0,
                             'points': 10,
                             'skill_tag': 'sys_cap_theorem',
                             'explanation': 'When network cables fail (Partition P), a system must either reject '
                                            'writes to guarantee Consistency (CP) or accept writes on both sides '
                                            'risking inconsistency for Availability (AP).',
                             'hint': 'Consistency vs Availability under network partition.'}]},
    {   'id': 'quiz-sys-l4-l7-load-balancing',
        'lesson_slug': 'sys-l4-l7-load-balancing',
        'title': 'L4 vs L7 Load Balancing Quiz',
        'passing_score': 70,
        'questions': [   {   'id': 'q1',
                             'type': 'multiple_choice',
                             'question': 'Which layer of load balancing can inspect HTTP request paths (e.g. '
                                         '`/api/videos` vs `/api/auth`) to route traffic to specialized server pools?',
                             'options': [   'Layer 4 (Transport / TCP)',
                                            'Layer 7 (Application / HTTP)',
                                            'Layer 2 (Data Link / MAC)',
                                            'Layer 1 (Physical / Copper)'],
                             'correct_answer': 1,
                             'points': 10,
                             'skill_tag': 'sys_load_balancing',
                             'explanation': 'Layer 7 load balancers inspect application payload headers, cookies, and '
                                            'HTTP URI paths to perform intelligent path-based routing.',
                             'hint': 'Application layer (HTTP).'}]},
    {   'id': 'quiz-sys-api-gateways-rate-limiting',
        'lesson_slug': 'sys-api-gateways-rate-limiting',
        'title': 'Rate Limiting Algorithms Quiz',
        'passing_score': 70,
        'questions': [   {   'id': 'q1',
                             'type': 'multiple_choice',
                             'question': 'Why is the Token Bucket algorithm widely preferred for API rate limiting?',
                             'options': [   'It allows temporary bursts of traffic up to the bucket capacity while '
                                            'strictly enforcing the average request refill rate',
                                            'It blocks all requests forever after 1 minute',
                                            'It requires no memory',
                                            'It increases network latency'],
                             'correct_answer': 0,
                             'points': 10,
                             'skill_tag': 'sys_api_gateways',
                             'explanation': 'Token bucket permits legitimate short bursts of traffic (e.g. page '
                                            'loading 5 parallel assets) without violating steady-state average rate '
                                            'limits.',
                             'hint': 'Allows burst capacity up to limit.'}]},
    {   'id': 'quiz-sys-circuit-breaker-fault-tolerance',
        'lesson_slug': 'sys-circuit-breaker-fault-tolerance',
        'title': 'Circuit Breakers & Fault Tolerance Quiz',
        'passing_score': 70,
        'questions': [   {   'id': 'q1',
                             'type': 'multiple_choice',
                             'question': "What is the primary benefit of tripping a Circuit Breaker to the 'OPEN' "
                                         'state when a downstream service is failing?',
                             'options': [   'It fails fast immediately with fallback data, preventing upstream server '
                                            'thread starvation and allowing the downstream service to recover',
                                            'It restarts all computers in the data center',
                                            'It deletes the database',
                                            'It makes the network faster'],
                             'correct_answer': 0,
                             'points': 10,
                             'skill_tag': 'sys_fault_tolerance',
                             'explanation': 'Tripping open prevents cascading failures by rejecting requests '
                                            'instantly, shielding struggling services from crashing under '
                                            'backpressure.',
                             'hint': 'Fail fast and prevent thread pool starvation.'}]},
    {   'id': 'quiz-sys-redis-caching-patterns',
        'lesson_slug': 'sys-redis-caching-patterns',
        'title': 'Redis Caching Strategies Quiz',
        'passing_score': 70,
        'questions': [   {   'id': 'q1',
                             'type': 'multiple_choice',
                             'question': 'In the Cache-Aside (Lazy Loading) pattern, what happens when a Cache Miss '
                                         'occurs?',
                             'options': [   'The application queries the database, returns the result to the user, and '
                                            'writes the data into the cache for future requests',
                                            'The application throws a 500 error',
                                            'The database is wiped',
                                            'The cache is deleted'],
                             'correct_answer': 0,
                             'points': 10,
                             'skill_tag': 'sys_redis_caching',
                             'explanation': 'Cache-Aside queries persistent storage on miss and lazily stores the '
                                            'fetched data into the cache key for sub-millisecond future hits.',
                             'hint': 'Fetch from DB and populate cache.'}]},
    {   'id': 'quiz-sys-message-queues-rabbitmq-kafka',
        'lesson_slug': 'sys-message-queues-rabbitmq-kafka',
        'title': 'RabbitMQ vs Kafka Quiz',
        'passing_score': 70,
        'questions': [   {   'id': 'q1',
                             'type': 'multiple_choice',
                             'question': 'What is a major fundamental architectural difference between RabbitMQ and '
                                         'Apache Kafka?',
                             'options': [   'RabbitMQ deletes messages upon consumer acknowledgment, while Kafka '
                                            'stores events in an immutable append-only commit log that can be replayed '
                                            'from any offset',
                                            'RabbitMQ only runs in browsers',
                                            'Kafka does not use disks',
                                            'Kafka is written in CSS'],
                             'correct_answer': 0,
                             'points': 10,
                             'skill_tag': 'sys_message_queues',
                             'explanation': 'Kafka retains immutable log partitions for days or months, allowing new '
                                            'consumer groups to replay history from arbitrary offset positions.',
                             'hint': 'Immutable commit log replay vs transient task queue.'}]},
    {   'id': 'quiz-sys-event-driven-pubsub',
        'lesson_slug': 'sys-event-driven-pubsub',
        'title': 'Event-Driven & Sagas Quiz',
        'passing_score': 70,
        'questions': [   {   'id': 'q1',
                             'type': 'multiple_choice',
                             'question': 'In a distributed Saga transaction across microservices, what action is taken '
                                         'if a step fails midway (e.g. payment failure)?',
                             'options': [   'The Saga emits Compensating Transactions (rollback events) to undo the '
                                            'effects of previous successful steps',
                                            'The entire database cluster is formatted',
                                            'All microservices are stopped',
                                            'Nothing happens'],
                             'correct_answer': 0,
                             'points': 10,
                             'skill_tag': 'sys_event_driven_sagas',
                             'explanation': 'Compensating transactions execute reverse business operations (like '
                                            'releasing reserved inventory holds or refunding balances) to maintain '
                                            'eventual consistency.',
                             'hint': 'Compensating transactions roll back distributed steps.'}]},
    {   'id': 'quiz-sys-db-replication-consensus',
        'lesson_slug': 'sys-db-replication-consensus',
        'title': 'Database Replication & Raft Quiz',
        'passing_score': 70,
        'questions': [   {   'id': 'q1',
                             'type': 'multiple_choice',
                             'question': 'Why does the Raft Consensus leader election algorithm require a strict '
                                         'Majority Quorum (> 50% of nodes)?',
                             'options': [   'To mathematically prevent Split-Brain (ensuring two isolated network '
                                            'partitions cannot both elect leaders simultaneously)',
                                            'To reduce electricity costs',
                                            'Because even numbers cannot vote in computers',
                                            'To make database queries faster'],
                             'correct_answer': 0,
                             'points': 10,
                             'skill_tag': 'sys_db_consensus',
                             'explanation': 'A majority quorum (> N/2) guarantees that only one partition can have '
                                            'enough votes to elect a leader, preventing duplicate leaders from '
                                            'accepting conflicting writes.',
                             'hint': 'Majority quorum prevents split-brain duplicate leaders.'}]},
    {   'id': 'quiz-sys-consistent-hashing-sharding',
        'lesson_slug': 'sys-consistent-hashing-sharding',
        'title': 'Consistent Hashing & Sharding Quiz',
        'passing_score': 70,
        'questions': [   {   'id': 'q1',
                             'type': 'multiple_choice',
                             'question': 'When a new database server node is added to a Consistent Hashing ring with N '
                                         'existing nodes, what fraction of keys must be migrated?',
                             'options': [   'Nearly 100% of all keys in the entire database',
                                            'Only approximately 1/N of total keys (only keys belonging to the new '
                                            "node's partition segment)",
                                            'Zero keys',
                                            'All primary keys'],
                             'correct_answer': 1,
                             'points': 10,
                             'skill_tag': 'sys_db_sharding',
                             'explanation': 'Consistent hashing ensures that adding or removing a node only impacts '
                                            'adjacent segments on the ring (~k/N keys), preventing cluster-wide rehash '
                                            'storms.',
                             'hint': 'Only a fraction (1/N) of keys move.'}]},
    {   'id': 'quiz-sys-nosql-timeseries-search',
        'lesson_slug': 'sys-nosql-timeseries-search',
        'title': 'Inverted Indexes & Search Engines Quiz',
        'passing_score': 70,
        'questions': [   {   'id': 'q1',
                             'type': 'multiple_choice',
                             'question': 'How does an Inverted Index in Elasticsearch enable sub-millisecond full-text '
                                         'keyword searches across millions of documents?',
                             'options': [   'By scanning all documents line-by-line using a regex loop',
                                            'By mapping unique tokenized words to a postings list of matching document '
                                            'IDs and positions',
                                            'By copying all text into browser memory',
                                            'By sorting documents by creation date'],
                             'correct_answer': 1,
                             'points': 10,
                             'skill_tag': 'sys_nosql_search',
                             'explanation': 'An inverted index operates like the index at the back of a textbook: it '
                                            'maps words to exact document ID lists for immediate O(1) set intersection '
                                            'lookups.',
                             'hint': 'Mapping words to lists of document IDs.'}]},
    {   'id': 'quiz-git-internals-blobs-trees-commits',
        'lesson_slug': 'git-internals-blobs-trees-commits',
        'title': 'Git Object Storage & DAG Quiz',
        'passing_score': 70,
        'questions': [   {   'id': 'q1',
                             'type': 'multiple_choice',
                             'question': 'What are the 3 fundamental object types stored inside the `.git/objects/` '
                                         'directory?',
                             'options': [   'Blobs (file content), Trees (directories), and Commits (snapshots)',
                                            'HTML, CSS, and JavaScript',
                                            'Branches, Remotes, and Hooks',
                                            'Zips, TARs, and Gzips'],
                             'correct_answer': 0,
                             'points': 10,
                             'skill_tag': 'git_internals_dag',
                             'explanation': 'Git stores file contents in Blobs, directory structures in Trees, and '
                                            'snapshot metadata/parents in Commits, all addressed by SHA hashes.',
                             'hint': 'Blobs, Trees, and Commits.'}]},
    {   'id': 'quiz-git-staging-working-tree-index',
        'lesson_slug': 'git-staging-working-tree-index',
        'title': 'The 3 Trees of Git Quiz',
        'passing_score': 70,
        'questions': [   {   'id': 'q1',
                             'type': 'multiple_choice',
                             'question': 'What command copies modified files from the Working Directory into the '
                                         'Staging Index in preparation for the next commit?',
                             'options': ['`git commit`', '`git add`', '`git push`', '`git clone`'],
                             'correct_answer': 1,
                             'points': 10,
                             'skill_tag': 'git_three_trees',
                             'explanation': '`git add` stages changes into the binary `.git/index` cache, forming the '
                                            'exact snapshot that `git commit` will permanently record.',
                             'hint': 'git add stages files.'}]},
    {   'id': 'quiz-git-head-branches-tags',
        'lesson_slug': 'git-head-branches-tags',
        'title': 'HEAD Pointer & Branch References Quiz',
        'passing_score': 70,
        'questions': [   {   'id': 'q1',
                             'type': 'multiple_choice',
                             'question': 'What is a Git branch under the hood inside the `.git` directory?',
                             'options': [   'A 500MB zip file containing the entire project history',
                                            'A simple 41-byte text file containing a 40-character commit SHA hash and '
                                            'a newline',
                                            'A database table in SQLite',
                                            'A remote server connection'],
                             'correct_answer': 1,
                             'points': 10,
                             'skill_tag': 'git_head_pointers',
                             'explanation': 'Git branches are lightweight movable pointers referencing commit hashes '
                                            'stored in `.git/refs/heads/`.',
                             'hint': 'A lightweight 41-byte text pointer file.'}]},
    {   'id': 'quiz-git-branching-merge-strategies',
        'lesson_slug': 'git-branching-merge-strategies',
        'title': 'Fast-Forward vs 3-Way Merges Quiz',
        'passing_score': 70,
        'questions': [   {   'id': 'q1',
                             'type': 'multiple_choice',
                             'question': 'When does Git perform a Fast-Forward merge instead of creating a 3-way merge '
                                         'commit?',
                             'options': [   'When the target branch (`main`) has not advanced with any new commits '
                                            'since the feature branch was created',
                                            'Only when merging across different computers',
                                            'When there are merge conflicts',
                                            'Whenever `--no-ff` is passed'],
                             'correct_answer': 0,
                             'points': 10,
                             'skill_tag': 'git_merge_strategies',
                             'explanation': 'If history has not diverged, Git simply moves the target branch pointer '
                                            'forward to the feature branch commit without creating a merge commit.',
                             'hint': 'When the base branch has no intervening commits.'}]},
    {   'id': 'quiz-git-interactive-rebase-squash',
        'lesson_slug': 'git-interactive-rebase-squash',
        'title': 'Interactive Rebase & Squashing Quiz',
        'passing_score': 70,
        'questions': [   {   'id': 'q1',
                             'type': 'multiple_choice',
                             'question': 'What action does the `squash` (or `s`) command perform during an interactive '
                                         'rebase (`git rebase -i`)?',
                             'options': [   'Melts the selected commit into the previous commit, combining their diffs '
                                            'and prompting to edit the combined commit message',
                                            'Deletes all files in the working directory',
                                            'Pushes the commit to GitHub immediately',
                                            'Creates a detached HEAD'],
                             'correct_answer': 0,
                             'points': 10,
                             'skill_tag': 'git_interactive_rebase',
                             'explanation': 'Squashing combines multiple WIP commits into a single clean atomic commit '
                                            'with a cohesive message.',
                             'hint': 'Melts commit into previous commit.'}]},
    {   'id': 'quiz-git-merge-conflicts-cherrypick',
        'lesson_slug': 'git-merge-conflicts-cherrypick',
        'title': 'Conflict Resolution & Git Reflog Quiz',
        'passing_score': 70,
        'questions': [   {   'id': 'q1',
                             'type': 'multiple_choice',
                             'question': 'If you accidentally delete a branch using `git branch -D`, how can you '
                                         'recover the lost commits within 90 days?',
                             'options': [   'Run `git reflog` to find the lost commit SHA and recreate the branch '
                                            'pointer with `git checkout -b recovered <SHA>`',
                                            'Re-install Git',
                                            'Lost commits cannot ever be recovered in Git',
                                            'Check the browser download folder'],
                             'correct_answer': 0,
                             'points': 10,
                             'skill_tag': 'git_conflicts_reflog',
                             'explanation': '`git reflog` records all local HEAD movements, allowing recovery of '
                                            'unreachable commits before garbage collection.',
                             'hint': 'git reflog logs every local HEAD pointer change.'}]},
    {   'id': 'quiz-git-github-prs-code-reviews',
        'lesson_slug': 'git-github-prs-code-reviews',
        'title': 'Pull Requests & SemVer Quiz',
        'passing_score': 70,
        'questions': [   {   'id': 'q1',
                             'type': 'multiple_choice',
                             'question': 'Under Semantic Versioning (SemVer 2.0.0), what does a MAJOR version bump '
                                         '(e.g. `1.4.0` -> `2.0.0`) signify?',
                             'options': [   'Incompatible breaking API changes that require code updates from '
                                            'consumers',
                                            'Small backwards-compatible bug fixes',
                                            'Only aesthetic CSS color updates',
                                            'A weekly scheduled update'],
                             'correct_answer': 0,
                             'points': 10,
                             'skill_tag': 'github_pr_workflow',
                             'explanation': 'MAJOR version increments indicate breaking changes, MINOR indicates '
                                            'backwards-compatible features, and PATCH indicates backwards-compatible '
                                            'bug fixes.',
                             'hint': 'Breaking API changes.'}]},
    {   'id': 'quiz-git-actions-cicd-automation',
        'lesson_slug': 'git-actions-cicd-automation',
        'title': 'GitHub Actions CI/CD Quiz',
        'passing_score': 70,
        'questions': [   {   'id': 'q1',
                             'type': 'multiple_choice',
                             'question': 'What is the primary role of automated GitHub Actions CI workflows in '
                                         'software teams?',
                             'options': [   'To automatically execute unit test suites, type checking, and build '
                                            'validations on every push and pull request before merging',
                                            'To replace human programmers',
                                            'To generate random passwords',
                                            'To format developer hard drives'],
                             'correct_answer': 0,
                             'points': 10,
                             'skill_tag': 'github_actions_cicd',
                             'explanation': 'GitHub Actions enforces automated quality gates, running test suites in '
                                            'cloud runners to ensure broken code never enters production.',
                             'hint': 'Automated testing and verification on every pull request.'}]},
    {   'id': 'quiz-git-releases-tag-publishing',
        'lesson_slug': 'git-releases-tag-publishing',
        'title': 'Release Tags & Artifacts Quiz',
        'passing_score': 70,
        'questions': [   {   'id': 'q1',
                             'type': 'multiple_choice',
                             'question': 'How can pushing a Git tag (e.g. `git push origin v1.0.4`) automate '
                                         'application delivery?',
                             'options': [   'By triggering a GitHub Actions release workflow that compiles release '
                                            'binaries and publishes them as downloadable GitHub Release assets',
                                            'By turning off the repository',
                                            'By deleting older commits',
                                            'By sending SMS messages to all users'],
                             'correct_answer': 0,
                             'points': 10,
                             'skill_tag': 'github_releases_publishing',
                             'explanation': 'Tag-triggered CI workflows compile production binaries (Tauri '
                                            'executables, IPAs, AABs) and attach them directly to GitHub Releases.',
                             'hint': 'Automated release build and artifact attachment.'}]}]

SKILLS_DATA = [   {   'id': 'skill-python-basics',
        'name': 'Python & NumPy Computing',
        'category': 'Programming',
        'description': 'Object reference models, mutability, vectorization, and broadcasting.',
        'icon': 'Code2',
        'tier': 1,
        'prerequisites': [],
        'mastery_threshold': 70,
        'matching_lessons': [   'py-intro-variables',
                                'py-data-structures-comprehensions',
                                'py-numpy-arrays-broadcasting',
                                'py-numpy-matrix-operations']},
    {   'id': 'skill-data-preprocessing',
        'name': 'Data Preprocessing & Pandas',
        'category': 'Data Science',
        'description': 'Tabular manipulation, missing value imputation, and feature engineering.',
        'icon': 'Database',
        'tier': 1,
        'prerequisites': ['skill-python-basics'],
        'mastery_threshold': 70,
        'matching_lessons': ['py-pandas-dataframes-cleaning']},
    {   'id': 'skill-linear-algebra',
        'name': 'Linear Algebra & Vectors',
        'category': 'Mathematics',
        'description': 'Vector dot products, geometric cosine similarity, and matrix transformations.',
        'icon': 'Binary',
        'tier': 1,
        'prerequisites': ['skill-python-basics'],
        'mastery_threshold': 70,
        'matching_lessons': ['math-vectors-dot-products', 'math-matrix-multiplication']},
    {   'id': 'skill-calculus',
        'name': 'Calculus & Optimization',
        'category': 'Mathematics',
        'description': 'Derivatives, partial slopes, gradient vectors, and the Chain Rule.',
        'icon': 'TrendingUp',
        'tier': 2,
        'prerequisites': ['skill-linear-algebra'],
        'mastery_threshold': 70,
        'matching_lessons': ['math-derivatives-gradients', 'math-chain-rule-backprop-math']},
    {   'id': 'skill-probability',
        'name': 'Probability & Bayes',
        'category': 'Mathematics',
        'description': 'Bayes Theorem, prior/posterior probabilities, and likelihood estimation.',
        'icon': 'Dice5',
        'tier': 2,
        'prerequisites': ['skill-linear-algebra'],
        'mastery_threshold': 70,
        'matching_lessons': ['math-probability-bayes-theorem']},
    {   'id': 'skill-regression',
        'name': 'Classical Machine Learning',
        'category': 'Machine Learning',
        'description': 'Linear regression, loss surfaces, MSE, and gradient descent optimization.',
        'icon': 'Cpu',
        'tier': 2,
        'prerequisites': ['skill-calculus'],
        'mastery_threshold': 70,
        'matching_lessons': ['ml-linear-regression-ols', 'ml-gradient-descent-intuition']},
    {   'id': 'skill-classification',
        'name': 'Classification & Trees',
        'category': 'Machine Learning',
        'description': 'Logistic regression, Sigmoid curves, Decision Trees, and Entropy.',
        'icon': 'GitFork',
        'tier': 2,
        'prerequisites': ['skill-regression'],
        'mastery_threshold': 70,
        'matching_lessons': [   'ml-logistic-regression-classification',
                                'ml-decision-trees-entropy',
                                'ml-kmeans-clustering-algorithm']},
    {   'id': 'skill-neural-networks',
        'name': 'Deep Neural Networks',
        'category': 'Deep Learning',
        'description': 'Multi-layer perceptron forward prop, ReLU activations, and Backpropagation.',
        'icon': 'Network',
        'tier': 3,
        'prerequisites': ['skill-regression'],
        'mastery_threshold': 70,
        'matching_lessons': ['dl-perceptron-forward-prop', 'dl-activation-functions', 'dl-backpropagation-calculus']},
    {   'id': 'skill-computer-vision',
        'name': 'Computer Vision & CNNs',
        'category': 'Deep Learning',
        'description': '2D convolution filters, feature map hierarchies, and Max Pooling.',
        'icon': 'Eye',
        'tier': 3,
        'prerequisites': ['skill-neural-networks'],
        'mastery_threshold': 70,
        'matching_lessons': ['dl-cnn-convolution-pooling']},
    {   'id': 'skill-transformers',
        'name': 'Transformers & Generative AI',
        'category': 'Generative AI',
        'description': 'Query/Key/Value self-attention, token contextualization, and RAG pipelines.',
        'icon': 'Sparkles',
        'tier': 4,
        'prerequisites': ['skill-neural-networks'],
        'mastery_threshold': 70,
        'matching_lessons': [   'genai-tokenization-embeddings',
                                'genai-self-attention-transformers',
                                'genai-rag-architecture-pipeline']},
    {   'id': 'skill-prompt-engineering',
        'name': 'Prompt Engineering & Agents',
        'category': 'Practical AI',
        'description': 'Few-shot prompting, Chain of Thought, tool usage, and autonomous ReAct agents.',
        'icon': 'Bot',
        'tier': 4,
        'prerequisites': ['skill-python-basics'],
        'mastery_threshold': 70,
        'matching_lessons': [   'prompt-foundations-few-shot',
                                'prompt-chain-of-thought-reasoning',
                                'prompt-ai-agents-tool-use']},
    {   'id': 'skill-web-foundations',
        'name': 'Web Architecture & HTML5',
        'category': 'Web Development',
        'description': 'DNS, HTTP/HTTPS protocols, semantic landmarks, and accessible form validations.',
        'icon': 'Globe',
        'tier': 1,
        'prerequisites': [],
        'mastery_threshold': 70,
        'matching_lessons': ['web-how-the-web-works', 'web-semantic-html5-tags', 'web-forms-validation-accessibility']},
    {   'id': 'skill-css-mastery',
        'name': 'CSS3 Box Model & Grid',
        'category': 'Web Development',
        'description': 'Box model, specificity, 1D flexbox, 2D CSS grid templates, and 60fps animations.',
        'icon': 'Layers',
        'tier': 1,
        'prerequisites': ['skill-web-foundations'],
        'mastery_threshold': 70,
        'matching_lessons': [   'web-css-box-model-cascade',
                                'web-css-flexbox-grid-mastery',
                                'web-css-responsive-animations']},
    {   'id': 'skill-javascript-core',
        'name': 'JavaScript Engine & Async',
        'category': 'Web Development',
        'description': 'Execution contexts, closures, event loop microtasks, promises, and DOM delegation.',
        'icon': 'Code2',
        'tier': 2,
        'prerequisites': ['skill-css-mastery'],
        'mastery_threshold': 70,
        'matching_lessons': [   'web-js-execution-scope-closures',
                                'web-js-event-loop-promises-async',
                                'web-js-dom-events-delegation']},
    {   'id': 'skill-react-engineering',
        'name': 'React 18 & State Architecture',
        'category': 'Web Development',
        'description': 'Declarative Virtual DOM rendering, useState, useEffect, custom hooks, and Zustand.',
        'icon': 'Cpu',
        'tier': 2,
        'prerequisites': ['skill-javascript-core'],
        'mastery_threshold': 70,
        'matching_lessons': [   'web-react-jsx-vdom-components',
                                'web-react-hooks-deep-dive',
                                'web-react-state-routing-zustand']},
    {   'id': 'skill-nodejs-backend',
        'name': 'Node.js & Database Engineering',
        'category': 'Web Development',
        'description': 'Express middleware pipelines, JWT auth, MongoDB and PostgreSQL CRUD optimization.',
        'icon': 'Server',
        'tier': 3,
        'prerequisites': ['skill-javascript-core'],
        'mastery_threshold': 70,
        'matching_lessons': [   'web-nodejs-express-middleware',
                                'web-jwt-auth-security-bcrypt',
                                'web-db-mongodb-postgresql-crud']},
    {   'id': 'skill-advanced-fullstack',
        'name': 'SSR, Next.js & Performance',
        'category': 'Web Development',
        'description': 'Server components, hydration, Core Web Vitals, WebSockets, and Redis in-memory caching.',
        'icon': 'Zap',
        'tier': 4,
        'prerequisites': ['skill-react-engineering', 'skill-nodejs-backend'],
        'mastery_threshold': 70,
        'matching_lessons': [   'web-nextjs-ssr-ssg-hydration',
                                'web-performance-core-web-vitals',
                                'web-websockets-realtime-redis-caching']},
    {   'id': 'skill-mobile-ui-primitives',
        'name': 'Native Bridges & Primitives',
        'category': 'App Development',
        'description': 'React Native JSI bridge, native viewports, density-independent pixels, and touch targets.',
        'icon': 'Smartphone',
        'tier': 1,
        'prerequisites': [],
        'mastery_threshold': 70,
        'matching_lessons': [   'app-foundations-native-bridge',
                                'app-viewport-density-safe-area',
                                'app-mobile-flexbox-touch-targets']},
    {   'id': 'skill-mobile-navigation-gestures',
        'name': 'Navigation & Reanimated 3',
        'category': 'App Development',
        'description': 'Stack & tab navigators, continuous pan gestures, worklets, and spring physics.',
        'icon': 'Layers',
        'tier': 2,
        'prerequisites': ['skill-mobile-ui-primitives'],
        'mastery_threshold': 70,
        'matching_lessons': [   'app-navigation-stacks-tabs',
                                'app-gestures-pan-swipe-pinch',
                                'app-reanimated-60fps-physics']},
    {   'id': 'skill-mobile-storage-hardware',
        'name': 'MMKV, SQLite & Hardware',
        'category': 'App Development',
        'description': 'Offline-first sync, MMKV caching, embedded SQLite, FaceID biometrics, and camera permissions.',
        'icon': 'HardDrive',
        'tier': 3,
        'prerequisites': ['skill-mobile-navigation-gestures'],
        'mastery_threshold': 70,
        'matching_lessons': [   'app-offline-first-mmkv-storage',
                                'app-sqlite-local-relational-db',
                                'app-device-hardware-camera-location']},
    {   'id': 'skill-flutter-dart-engineering',
        'name': 'Flutter & BLoC Architecture',
        'category': 'App Development',
        'description': 'Dart language, Impeller rendering engine, StatefulWidget lifecycles, and BLoC reactive '
                       'streams.',
        'icon': 'Smartphone',
        'tier': 3,
        'prerequisites': ['skill-mobile-ui-primitives'],
        'mastery_threshold': 70,
        'matching_lessons': [   'app-flutter-widget-tree-rendering',
                                'app-flutter-stateful-lifecycle',
                                'app-flutter-bloc-state-streams']},
    {   'id': 'skill-mobile-production-deploy',
        'name': 'Push, Sync & App Store Release',
        'category': 'App Development',
        'description': 'APNs/FCM push notifications, background tasks, code signing certificates, and Fastlane / EAS '
                       'deployment.',
        'icon': 'Zap',
        'tier': 4,
        'prerequisites': ['skill-mobile-storage-hardware', 'skill-flutter-dart-engineering'],
        'mastery_threshold': 70,
        'matching_lessons': [   'app-push-notifications-fcm-apns',
                                'app-background-tasks-worker-sync',
                                'app-appstore-playstore-deployment']},
    {   'id': 'skill-system-foundations',
        'name': 'Distributed Foundations & CAP',
        'category': 'System Design',
        'description': 'Scaling up vs out, CDNs, monolith to microservices trade-offs, and CAP/PACELC theorems.',
        'icon': 'Layers',
        'tier': 1,
        'prerequisites': [],
        'mastery_threshold': 70,
        'matching_lessons': ['sys-client-server-scaling', 'sys-monolith-to-microservices', 'sys-cap-theorem-pacelc']},
    {   'id': 'skill-system-lb-gateways',
        'name': 'Load Balancing & Circuit Breakers',
        'category': 'System Design',
        'description': 'L4 vs L7 load balancing, API gateways, Token Bucket rate limiting, and Circuit Breaker '
                       'isolation.',
        'icon': 'Server',
        'tier': 2,
        'prerequisites': ['skill-system-foundations'],
        'mastery_threshold': 70,
        'matching_lessons': [   'sys-l4-l7-load-balancing',
                                'sys-api-gateways-rate-limiting',
                                'sys-circuit-breaker-fault-tolerance']},
    {   'id': 'skill-system-caching-queues',
        'name': 'Redis, Kafka & Saga Transactions',
        'category': 'System Design',
        'description': 'Cache-Aside pattern, thundering herd protection, RabbitMQ queues, Kafka logs, and Sagas.',
        'icon': 'Cpu',
        'tier': 3,
        'prerequisites': ['skill-system-foundations'],
        'mastery_threshold': 70,
        'matching_lessons': [   'sys-redis-caching-patterns',
                                'sys-message-queues-rabbitmq-kafka',
                                'sys-event-driven-pubsub']},
    {   'id': 'skill-system-sharding-consensus',
        'name': 'DB Sharding & Raft Consensus',
        'category': 'System Design',
        'description': 'Leader-follower replication, Raft majority elections, consistent hashing rings, and '
                       'Elasticsearch inverted indexes.',
        'icon': 'Database',
        'tier': 4,
        'prerequisites': ['skill-system-caching-queues'],
        'mastery_threshold': 70,
        'matching_lessons': [   'sys-db-replication-consensus',
                                'sys-consistent-hashing-sharding',
                                'sys-nosql-timeseries-search']},
    {   'id': 'skill-git-internals-dag',
        'name': 'Git Object Database & DAG',
        'category': 'Git & GitHub',
        'description': 'Blobs, trees, commit objects, 3 trees (Working, Index, Repo), and HEAD reference mechanics.',
        'icon': 'GitCommit',
        'tier': 1,
        'prerequisites': [],
        'mastery_threshold': 70,
        'matching_lessons': [   'git-internals-blobs-trees-commits',
                                'git-staging-working-tree-index',
                                'git-head-branches-tags']},
    {   'id': 'skill-git-rebase-workflows',
        'name': 'Rebase, Squashing & Reflog',
        'category': 'Git & GitHub',
        'description': 'Fast-forward vs 3-way merges, interactive rebasing (`git rebase -i`), squashing, and git '
                       'reflog time travel.',
        'icon': 'GitBranch',
        'tier': 2,
        'prerequisites': ['skill-git-internals-dag'],
        'mastery_threshold': 70,
        'matching_lessons': [   'git-branching-merge-strategies',
                                'git-interactive-rebase-squash',
                                'git-merge-conflicts-cherrypick']},
    {   'id': 'skill-github-cicd-releases',
        'name': 'Pull Requests & GitHub Actions',
        'category': 'Git & GitHub',
        'description': 'Pull Request code reviews, branch protections, automated CI/CD YAML workflows, and release '
                       'tagging.',
        'icon': 'GitPullRequest',
        'tier': 3,
        'prerequisites': ['skill-git-rebase-workflows'],
        'mastery_threshold': 70,
        'matching_lessons': [   'git-github-prs-code-reviews',
                                'git-actions-cicd-automation',
                                'git-releases-tag-publishing']}]

# Extend with comprehensive DSA and Cyber Security curriculum tracks
from app.seed.dsa_cyber_seed_data import (
    DSA_CYBER_COURSES,
    DSA_CYBER_LESSONS,
    DSA_CYBER_QUIZZES,
    DSA_CYBER_SKILLS
)

COURSES_DATA.extend(DSA_CYBER_COURSES)
LESSONS_DATA.extend(DSA_CYBER_LESSONS)
QUIZZES_DATA.extend(DSA_CYBER_QUIZZES)
SKILLS_DATA.extend(DSA_CYBER_SKILLS)
