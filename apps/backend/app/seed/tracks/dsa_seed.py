"""
DSA (Data Structures & Algorithms) Comprehensive Curriculum Track
Levels 1 - 5 covering:
- Level 1: Foundations (Complexity, Arrays, Strings, Matrix, Prefix Sum, Sliding Window, Two Pointers, Hashing, Recursion)
- Level 2: Core Data Structures (Linked Lists, Stack, Queue, Deque, Hash Table, Heap/Priority Queue)
- Level 3: Trees (Binary Tree, Traversals, BST, AVL Tree, Heap, Trie, Segment Tree, Fenwick Tree)
- Level 4: Graphs (Representation, BFS, DFS, Cycle Detection, Topo Sort, Shortest Path Dijkstra/Bellman-Ford/Floyd-Warshall, MST, DSU, SCC)
- Level 5: Algorithms & Advanced (Binary Search, Divide & Conquer, Greedy, Backtracking, DP 1D/2D/Tree/Digit/Bitmask, Bit Manipulation, String KMP/Z, Network Flow)
"""

COURSES_DATA = [
    {
        "id": "course-dsa-lvl1",
        "title": "DSA Level 1: Algorithmic Foundations & Array Patterns",
        "slug": "dsa-level-1-foundations",
        "domain": "dsa",
        "color": "#F43F5E",
        "icon": "Binary",
        "is_published": True,
        "skills_taught": ['Big-O Notation', 'Data Structures', 'Algorithmic Patterns', 'Optimization'],
        "description": "Master asymptotic Big-O analysis, memory layout, and fundamental array & string algorithmic patterns including Sliding Window and Two Pointers.",
        "category": "Arrays & Strings",
        "level": "beginner",
        "estimated_hours": 14,
        "thumbnail_url": "/assets/courses/dsa-foundations.png",
        "modules": [
            {
                "id": "mod-dsa-1-1",
                "title": "Module 1: Time, Space & Asymptotic Complexity",
                "description": "Formal definitions of Big-O, Omega, Theta, and practical amortized analysis.",
                "order": 1,
                "lesson_ids": ["dsa-asymptotic-complexity", "dsa-arrays-strings-memory"]
            },
            {
                "id": "mod-dsa-1-2",
                "title": "Module 2: Two Pointers & Prefix Sum Techniques",
                "description": "In-place array manipulation, convergent pointers, and O(1) range queries.",
                "order": 2,
                "lesson_ids": ["dsa-two-pointers-prefix-sum", "dsa-sliding-window-patterns"]
            },
            {
                "id": "mod-dsa-1-3",
                "title": "Module 3: Hashing & Matrix Algorithms",
                "description": "Hash collision resolution, 2D matrix traversals, and spiral algorithms.",
                "order": 3,
                "lesson_ids": ["dsa-hashing-lookup-tables", "dsa-matrix-transformations"]
            },
            {
                "id": "mod-dsa-1-4",
                "title": "Module 4: Recursion Mechanics & Call Stacks",
                "description": "Stack frame memory execution, recurrence relations, and base case formulation.",
                "order": 4,
                "lesson_ids": ["dsa-recursion-stack-mechanics", "dsa-recursion-divide-foundations"]
            }
        ]
    },
    {
        "id": "course-dsa-lvl2",
        "title": "DSA Level 2: Core Linear & Node Data Structures",
        "slug": "dsa-level-2-core-structures",
        "domain": "dsa",
        "color": "#F43F5E",
        "icon": "Binary",
        "is_published": True,
        "skills_taught": ['Big-O Notation', 'Data Structures', 'Algorithmic Patterns', 'Optimization'],
        "description": "Deep dive into pointer-based node structures: Singly/Doubly/Circular Linked Lists, Stacks, Queues, Deques, and Heaps.",
        "category": "Linked Lists & Stacks",
        "level": "intermediate",
        "estimated_hours": 16,
        "thumbnail_url": "/assets/courses/dsa-structures.png",
        "modules": [
            {
                "id": "mod-dsa-2-1",
                "title": "Module 1: Linked List Architectures",
                "description": "Singly, Doubly, and Circular Linked Lists with fast-slow pointer cycle detection.",
                "order": 1,
                "lesson_ids": ["dsa-linked-list-fundamentals", "dsa-doubly-circular-lists"]
            },
            {
                "id": "mod-dsa-2-2",
                "title": "Module 2: Stacks & Monotonic Stack Patterns",
                "description": "LIFO memory structures, parenthetical parsing, and next greater element monotonic stacks.",
                "order": 2,
                "lesson_ids": ["dsa-stacks-monotonic-patterns", "dsa-queues-deques-buffers"]
            },
            {
                "id": "mod-dsa-2-3",
                "title": "Module 3: Priority Queues & Binary Heaps",
                "description": "Min/Max Binary Heaps, array representation, and heapify in O(N) time.",
                "order": 3,
                "lesson_ids": ["dsa-binary-heaps-priority-queues", "dsa-hash-maps-sets-internals"]
            },
            {
                "id": "mod-dsa-2-4",
                "title": "Module 4: Practical Structural Design",
                "description": "Designing LRU/LFU caches and composite data structures with O(1) constraints.",
                "order": 4,
                "lesson_ids": ["dsa-composite-lru-design", "dsa-linear-structures-review"]
            }
        ]
    },
    {
        "id": "course-dsa-lvl3",
        "title": "DSA Level 3: Trees, BSTs & Advanced Tree Structures",
        "slug": "dsa-level-3-trees",
        "domain": "dsa",
        "color": "#F43F5E",
        "icon": "Binary",
        "is_published": True,
        "skills_taught": ['Big-O Notation', 'Data Structures', 'Algorithmic Patterns', 'Optimization'],
        "description": "Comprehensive tree architectures from Binary Trees and Traversals to AVL Self-Balancing, Tries, Segment Trees, and Fenwick Trees.",
        "category": "Trees & Graphs",
        "level": "advanced",
        "estimated_hours": 20,
        "thumbnail_url": "/assets/courses/dsa-trees.png",
        "modules": [
            {
                "id": "mod-dsa-3-1",
                "title": "Module 1: Binary Trees & Tree Traversals",
                "description": "In-order, Pre-order, Post-order, and Level-order BFS traversals with stack/queue implementations.",
                "order": 1,
                "lesson_ids": ["dsa-binary-tree-traversals", "dsa-bst-operations-validation"]
            },
            {
                "id": "mod-dsa-3-2",
                "title": "Module 2: Self-Balancing Trees & Tries",
                "description": "AVL tree rotations (LL, RR, LR, RL) and Prefix Tree / Trie string lookups.",
                "order": 2,
                "lesson_ids": ["dsa-avl-trees-rotations", "dsa-trie-prefix-trees"]
            },
            {
                "id": "mod-dsa-3-3",
                "title": "Module 3: Range Query Trees",
                "description": "Segment Trees for range minimum/sum queries with Lazy Propagation and Fenwick Trees (BIT).",
                "order": 3,
                "lesson_ids": ["dsa-segment-trees-lazy", "dsa-fenwick-binary-indexed-trees"]
            },
            {
                "id": "mod-dsa-3-4",
                "title": "Module 4: Tree Decomposition & Heavy-Light",
                "description": "Euler tour traversals, Lowest Common Ancestor (LCA) binary lifting, and HLD basics.",
                "order": 4,
                "lesson_ids": ["dsa-lca-binary-lifting", "dsa-tree-dp-foundations"]
            }
        ]
    },
    {
        "id": "course-dsa-lvl4",
        "title": "DSA Level 4: Graph Algorithms & Network Topology",
        "slug": "dsa-level-4-graphs",
        "domain": "dsa",
        "color": "#F43F5E",
        "icon": "Binary",
        "is_published": True,
        "skills_taught": ['Big-O Notation', 'Data Structures', 'Algorithmic Patterns', 'Optimization'],
        "description": "Master graph theory: BFS, DFS, Cycle Detection, Topological Sorting, Dijkstra, Bellman-Ford, Floyd-Warshall, Prim, Kruskal, DSU, and SCC.",
        "category": "Trees & Graphs",
        "level": "advanced",
        "estimated_hours": 22,
        "thumbnail_url": "/assets/courses/dsa-graphs.png",
        "modules": [
            {
                "id": "mod-dsa-4-1",
                "title": "Module 1: Graph Representation & Search",
                "description": "Adjacency matrices vs lists, BFS wave propagation, and DFS component discovery.",
                "order": 1,
                "lesson_ids": ["dsa-graph-representations-bfs-dfs", "dsa-cycle-detection-topological-sort"]
            },
            {
                "id": "mod-dsa-4-2",
                "title": "Module 2: Shortest Path Algorithms",
                "description": "Single-source Dijkstra with Priority Queue, Bellman-Ford with negative cycles, and Floyd-Warshall all-pairs.",
                "order": 2,
                "lesson_ids": ["dsa-dijkstra-shortest-path", "dsa-bellman-ford-floyd-warshall"]
            },
            {
                "id": "mod-dsa-4-3",
                "title": "Module 3: Minimum Spanning Trees & DSU",
                "description": "Disjoint Set Union (DSU) with path compression, Kruskal's greedy edges, and Prim's cut property.",
                "order": 3,
                "lesson_ids": ["dsa-dsu-kruskal-prim", "dsa-bipartite-graph-matching"]
            },
            {
                "id": "mod-dsa-4-4",
                "title": "Module 4: Connectivity & Advanced Graphs",
                "description": "Tarjan's strongly connected components (SCC), bridges, and articulation points.",
                "order": 4,
                "lesson_ids": ["dsa-scc-tarjan-bridges", "dsa-network-flow-max-cut"]
            }
        ]
    },
    {
        "id": "course-dsa-lvl5",
        "title": "DSA Level 5: Algorithmic Paradigms & Advanced Dynamic Programming",
        "slug": "dsa-level-5-algorithms-dp",
        "domain": "dsa",
        "color": "#F43F5E",
        "icon": "Binary",
        "is_published": True,
        "skills_taught": ['Big-O Notation', 'Data Structures', 'Algorithmic Patterns', 'Optimization'],
        "description": "Advanced problem solving: Divide & Conquer, Backtracking, 1D/2D DP, Tree DP, Digit DP, Bitmask DP, String Algorithms (KMP, Z), and Computational Geometry.",
        "category": "Dynamic Programming",
        "level": "expert",
        "estimated_hours": 26,
        "thumbnail_url": "/assets/courses/dsa-dp.png",
        "modules": [
            {
                "id": "mod-dsa-5-1",
                "title": "Module 1: Divide & Conquer and Greedy",
                "description": "Merge Sort, Quick Sort, Binary Search on Answer, and Greedy choice property.",
                "order": 1,
                "lesson_ids": ["dsa-binary-search-on-answer", "dsa-greedy-interval-scheduling"]
            },
            {
                "id": "mod-dsa-5-2",
                "title": "Module 2: Classical & Multi-Dimensional DP",
                "description": "0/1 Knapsack, Unbounded Knapsack, Longest Common Subsequence (LCS), and Matrix Chain Multiplication.",
                "order": 2,
                "lesson_ids": ["dsa-dp-knapsack-variants", "dsa-dp-lcs-lis-grid"]
            },
            {
                "id": "mod-dsa-5-3",
                "title": "Module 3: Advanced DP Patterns",
                "description": "Bitmask DP for Traveling Salesperson, Digit DP for numeric ranges, and Tree DP sub-tree memoization.",
                "order": 3,
                "lesson_ids": ["dsa-bitmask-dp-tsp", "dsa-digit-dp-numeric-ranges"]
            },
            {
                "id": "mod-dsa-5-4",
                "title": "Module 4: String Algorithms & Geometry",
                "description": "Knuth-Morris-Pratt (KMP) prefix function, Z-algorithm, Rolling Hash, and Convex Hull Graham Scan.",
                "order": 4,
                "lesson_ids": ["dsa-kmp-z-algorithm-strings", "dsa-computational-geometry-convex-hull"]
            }
        ]
    }
]

LESSONS_DATA = [
    {
        "id": "dsa-asymptotic-complexity",
        "title": "Asymptotic Analysis: Big-O, Omega, and Theta Bounds",
        "slug": "dsa-asymptotic-complexity",
        "domain": "dsa",
        "color": "#F43F5E",
        "icon": "Binary",
        "is_published": True,
        "skills_taught": ['Big-O Notation', 'Data Structures', 'Algorithmic Patterns', 'Optimization'],
        "course_id": "course-dsa-lvl1",
        "order": 1,
        "xp_reward": 50,
        "visual_diagram_type": "two_pointers_array",
        "content": """# Asymptotic Complexity & Efficiency Analysis

In computer science, algorithm efficiency is evaluated mathematically with respect to input size $N$.

### Formal Mathematical Definitions

1. **Big-O Notation ($O$) — Asymptotic Upper Bound**:
   $$f(N) = O(g(N)) \\iff \\exists c > 0, N_0 > 0 \\text{ s.t. } \\forall N \\ge N_0, 0 \\le f(N) \\le c \\cdot g(N)$$
   Represents the guaranteed worst-case execution boundary.

2. **Big-Omega Notation ($\\Omega$) — Asymptotic Lower Bound**:
   $$f(N) = \\Omega(g(N)) \\iff \\exists c > 0, N_0 > 0 \\text{ s.t. } \\forall N \\ge N_0, 0 \\le c \\cdot g(N) \\le f(N)$$

3. **Big-Theta Notation ($\\Theta$) — Asymptotically Tight Bound**:
   $$f(N) = \\Theta(g(N)) \\iff f(N) = O(g(N)) \\text{ and } f(N) = \\Omega(g(N))$$

### Standard Complexity Hierarchy
$$O(1) < O(\\log N) < O(N) < O(N \\log N) < O(N^2) < O(2^N) < O(N!)$$

```python
def find_max(arr: list[int]) -> int:
    # Time Complexity: O(N) linear scan
    # Space Complexity: O(1) auxiliary variables
    max_val = arr[0]
    for x in arr:
        if x > max_val:
            max_val = x
    return max_val
```
"""
    },
    {
        "id": "dsa-arrays-strings-memory",
        "title": "Contiguous Memory Layouts & String Immobility",
        "slug": "dsa-arrays-strings-memory",
        "domain": "dsa",
        "color": "#F43F5E",
        "icon": "Binary",
        "is_published": True,
        "skills_taught": ['Big-O Notation', 'Data Structures', 'Algorithmic Patterns', 'Optimization'],
        "course_id": "course-dsa-lvl1",
        "order": 2,
        "xp_reward": 50,
        "visual_diagram_type": "two_pointers_array",
        "content": """# Contiguous Memory & Dynamic Array Amortization

Arrays allocate sequential memory addresses, allowing $O(1)$ random access through pointer arithmetic:
$$\\text{Address}(A[i]) = \\text{BaseAddress} + i \\times \\text{SizeOfElement}$$

### Geometric Doubling & Amortized $O(1)$ Append
When dynamic arrays (e.g. `std::vector`, Python `list`) exceed capacity $C$, they allocate a new block of size $2C$ and copy $N$ elements.
$$\\text{Total Operations for } N \\text{ appends} = N + (1 + 2 + 4 + \\dots + N) = N + 2N = 3N \\implies O(1) \\text{ amortized time}.$$
"""
    },
    {
        "id": "dsa-two-pointers-prefix-sum",
        "title": "Two Pointers Strategy & Prefix Sum Arrays",
        "slug": "dsa-two-pointers-prefix-sum",
        "domain": "dsa",
        "color": "#F43F5E",
        "icon": "Binary",
        "is_published": True,
        "skills_taught": ['Big-O Notation', 'Data Structures', 'Algorithmic Patterns', 'Optimization'],
        "course_id": "course-dsa-lvl1",
        "order": 3,
        "xp_reward": 60,
        "visual_diagram_type": "two_pointers_array",
        "content": """# Two Pointers & Prefix Sum Optimization

### 1. Two Pointers Convergent Pattern
Solves Two Sum on sorted arrays in $O(N)$ time and $O(1)$ space:
```python
def two_sum_sorted(nums: list[int], target: int) -> tuple[int, int]:
    left, right = 0, len(nums) - 1
    while left < right:
        s = nums[left] + nums[right]
        if s == target:
            return left, right
        elif s < target:
            left += 1
        else:
            right -= 1
    return -1, -1
```

### 2. Prefix Sum Range Queries
Prefix array $P[i] = \\sum_{j=0}^{i-1} A[j]$ allows $O(1)$ range sum queries:
$$\\sum_{k=L}^{R} A[k] = P[R+1] - P[L]$$
"""
    },
    {
        "id": "dsa-sliding-window-patterns",
        "title": "Sliding Window: Fixed & Dynamic Windows",
        "slug": "dsa-sliding-window-patterns",
        "domain": "dsa",
        "color": "#F43F5E",
        "icon": "Binary",
        "is_published": True,
        "skills_taught": ['Big-O Notation', 'Data Structures', 'Algorithmic Patterns', 'Optimization'],
        "course_id": "course-dsa-lvl1",
        "order": 4,
        "xp_reward": 60,
        "visual_diagram_type": "two_pointers_array",
        "content": """# Sliding Window Subarray Patterns

Maintains a continuous contiguous window $[L, R]$ across an array without recomputing overlapping states.

```python
def max_subarray_sum_k(nums: list[int], k: int) -> int:
    window_sum = sum(nums[:k])
    max_sum = window_sum
    for i in range(k, len(nums)):
        window_sum += nums[i] - nums[i - k]  # Slide window
        max_sum = max(max_sum, window_sum)
    return max_sum
```
"""
    },
    {
        "id": "dsa-hashing-lookup-tables",
        "title": "Hash Tables, Collisions & Constant Time Lookup",
        "slug": "dsa-hashing-lookup-tables",
        "domain": "dsa",
        "color": "#F43F5E",
        "icon": "Binary",
        "is_published": True,
        "skills_taught": ['Big-O Notation', 'Data Structures', 'Algorithmic Patterns', 'Optimization'],
        "course_id": "course-dsa-lvl1",
        "order": 5,
        "xp_reward": 50,
        "visual_diagram_type": "two_pointers_array",
        "content": """# Hash Tables & Amortized O(1) Sets

A Hash Table maps keys to bucket indices using a hash function $h(k) \\pmod M$.

### Collision Resolution Strategies
1. **Separate Chaining**: Each bucket contains a linked list or red-black tree.
2. **Open Addressing**: Linear probing $h(k, i) = (h(k) + i) \\pmod M$ or quadratic probing.
"""
    },
    {
        "id": "dsa-matrix-transformations",
        "title": "2D Matrices, Spiral Walks & In-Place Rotations",
        "slug": "dsa-matrix-transformations",
        "domain": "dsa",
        "color": "#F43F5E",
        "icon": "Binary",
        "is_published": True,
        "skills_taught": ['Big-O Notation', 'Data Structures', 'Algorithmic Patterns', 'Optimization'],
        "course_id": "course-dsa-lvl1",
        "order": 6,
        "xp_reward": 50,
        "visual_diagram_type": "two_pointers_array",
        "content": """# 2D Matrix Traversal & Transpositions

Matrix $M \\in \\mathbb{R}^{R \\times C}$ is indexed row-major in contiguous memory: $\\text{index}(r, c) = r \\times C + c$.

### 90-Degree Clockwise Rotation In-Place:
1. Transpose matrix: swap $M[r][c]$ with $M[c][r]$.
2. Reverse every row horizontally.
"""
    },
    {
        "id": "dsa-recursion-stack-mechanics",
        "title": "Recursion Call Stack & Master Theorem",
        "slug": "dsa-recursion-stack-mechanics",
        "domain": "dsa",
        "color": "#F43F5E",
        "icon": "Binary",
        "is_published": True,
        "skills_taught": ['Big-O Notation', 'Data Structures', 'Algorithmic Patterns', 'Optimization'],
        "course_id": "course-dsa-lvl1",
        "order": 7,
        "xp_reward": 60,
        "visual_diagram_type": "two_pointers_array",
        "content": """# Recursion Stack Frames & Master Theorem

### The Master Theorem for Divide & Conquer:
$$T(N) = a T(N/b) + O(N^d)$$
1. If $d < \\log_b a \\implies T(N) = O(N^{\\log_b a})$
2. If $d = \\log_b a \\implies T(N) = O(N^d \\log N)$
3. If $d > \\log_b a \\implies T(N) = O(N^d)$
"""
    },
    {
        "id": "dsa-recursion-divide-foundations",
        "title": "Divide & Conquer: Binary Search Foundations",
        "slug": "dsa-recursion-divide-foundations",
        "domain": "dsa",
        "color": "#F43F5E",
        "icon": "Binary",
        "is_published": True,
        "skills_taught": ['Big-O Notation', 'Data Structures', 'Algorithmic Patterns', 'Optimization'],
        "course_id": "course-dsa-lvl1",
        "order": 8,
        "xp_reward": 60,
        "visual_diagram_type": "two_pointers_array",
        "content": """# Binary Search: Invariant Guarantees

Binary search halves the search space at each iteration, yielding $O(\\log N)$ time.
```python
def binary_search(arr: list[int], target: int) -> int:
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = low + (high - low) // 2  # Prevents integer overflow
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1
```
"""
    },
    {
        "id": "dsa-linked-list-fundamentals",
        "title": "Singly Linked Lists & Fast-Slow Pointers",
        "slug": "dsa-linked-list-fundamentals",
        "domain": "dsa",
        "color": "#F43F5E",
        "icon": "Binary",
        "is_published": True,
        "skills_taught": ['Big-O Notation', 'Data Structures', 'Algorithmic Patterns', 'Optimization'],
        "course_id": "course-dsa-lvl2",
        "order": 1,
        "xp_reward": 60,
        "visual_diagram_type": "two_pointers_array",
        "content": """# Singly Linked Lists & Cycle Detection

A Linked List consists of dynamic memory nodes connected via pointer references.

### Floyd's Tortoise & Hare Cycle Algorithm
- Slow pointer advances 1 step ($s = s.next$).
- Fast pointer advances 2 steps ($f = f.next.next$).
- If they meet, a cycle exists. The start of the cycle is found by resetting one pointer to head and advancing both 1 step simultaneously.
"""
    },
    {
        "id": "dsa-doubly-circular-lists",
        "title": "Doubly Linked Lists & Sentinel Nodes",
        "slug": "dsa-doubly-circular-lists",
        "domain": "dsa",
        "color": "#F43F5E",
        "icon": "Binary",
        "is_published": True,
        "skills_taught": ['Big-O Notation', 'Data Structures', 'Algorithmic Patterns', 'Optimization'],
        "course_id": "course-dsa-lvl2",
        "order": 2,
        "xp_reward": 60,
        "visual_diagram_type": "two_pointers_array",
        "content": """# Doubly Linked Lists & Constant Time Node Deletion

Each node contains `prev`, `next`, and `val`. Sentinel dummy head and tail nodes eliminate null checks at boundaries.
"""
    },
    {
        "id": "dsa-stacks-monotonic-patterns",
        "title": "Stacks & The Monotonic Stack Pattern",
        "slug": "dsa-stacks-monotonic-patterns",
        "domain": "dsa",
        "color": "#F43F5E",
        "icon": "Binary",
        "is_published": True,
        "skills_taught": ['Big-O Notation', 'Data Structures', 'Algorithmic Patterns', 'Optimization'],
        "course_id": "course-dsa-lvl2",
        "order": 3,
        "xp_reward": 70,
        "visual_diagram_type": "two_pointers_array",
        "content": """# Monotonic Stack for Next Greater Element

A Monotonic Stack maintains elements in strictly increasing or decreasing order in $O(N)$ amortized time.
```python
def next_greater_elements(nums: list[int]) -> list[int]:
    n = len(nums)
    res = [-1] * n
    stack = []  # Store indices
    for i in range(n):
        while stack and nums[i] > nums[stack[-1]]:
            idx = stack.pop()
            res[idx] = nums[i]
        stack.append(i)
    return res
```
"""
    },
    {
        "id": "dsa-queues-deques-buffers",
        "title": "Queues, Circular Buffers & Monotonic Deques",
        "slug": "dsa-queues-deques-buffers",
        "domain": "dsa",
        "color": "#F43F5E",
        "icon": "Binary",
        "is_published": True,
        "skills_taught": ['Big-O Notation', 'Data Structures', 'Algorithmic Patterns', 'Optimization'],
        "course_id": "course-dsa-lvl2",
        "order": 4,
        "xp_reward": 60,
        "visual_diagram_type": "two_pointers_array",
        "content": """# Queues, Ring Buffers & Sliding Window Maximum

A Double-Ended Queue (Deque) supports $O(1)$ push/pop at both ends. Monotonic deques solve Sliding Window Maximum in $O(N)$ time.
"""
    },
    {
        "id": "dsa-binary-heaps-priority-queues",
        "title": "Binary Heaps & Bottom-Up Heapify in O(N)",
        "slug": "dsa-binary-heaps-priority-queues",
        "domain": "dsa",
        "color": "#F43F5E",
        "icon": "Binary",
        "is_published": True,
        "skills_taught": ['Big-O Notation', 'Data Structures', 'Algorithmic Patterns', 'Optimization'],
        "course_id": "course-dsa-lvl2",
        "order": 5,
        "xp_reward": 70,
        "visual_diagram_type": "bst_tree_traversal",
        "content": """# Binary Heaps & Priority Queues

Complete binary tree represented as an array where parent at index $i$ has children at $2i+1$ and $2i+2$.
- **Insertion**: $O(\\log N)$ sift-up.
- **Extraction**: $O(\\log N)$ sift-down.
- **Build Heap**: $O(N)$ linear time via bottom-up sift-down.
"""
    },
    {
        "id": "dsa-hash-maps-sets-internals",
        "title": "Hash Table Internals & Robin Hood Hashing",
        "slug": "dsa-hash-maps-sets-internals",
        "domain": "dsa",
        "color": "#F43F5E",
        "icon": "Binary",
        "is_published": True,
        "skills_taught": ['Big-O Notation', 'Data Structures', 'Algorithmic Patterns', 'Optimization'],
        "course_id": "course-dsa-lvl2",
        "order": 6,
        "xp_reward": 60,
        "visual_diagram_type": "two_pointers_array",
        "content": """# Robin Hood Hashing & Load Factors

Robin Hood hashing equalizes displacement distance so probe variance is minimized, preventing long search chains.
"""
    },
    {
        "id": "dsa-composite-lru-design",
        "title": "Composite Structures: O(1) LRU Cache Design",
        "slug": "dsa-composite-lru-design",
        "domain": "dsa",
        "color": "#F43F5E",
        "icon": "Binary",
        "is_published": True,
        "skills_taught": ['Big-O Notation', 'Data Structures', 'Algorithmic Patterns', 'Optimization'],
        "course_id": "course-dsa-lvl2",
        "order": 7,
        "xp_reward": 75,
        "visual_diagram_type": "two_pointers_array",
        "content": """# Designing an O(1) LRU Cache

Combines a **Hash Map** ($O(1)$ lookup) with a **Doubly Linked List** ($O(1)$ removal and insertion at head).
"""
    },
    {
        "id": "dsa-linear-structures-review",
        "title": "Linear Structures Diagnostic Review",
        "slug": "dsa-linear-structures-review",
        "domain": "dsa",
        "color": "#F43F5E",
        "icon": "Binary",
        "is_published": True,
        "skills_taught": ['Big-O Notation', 'Data Structures', 'Algorithmic Patterns', 'Optimization'],
        "course_id": "course-dsa-lvl2",
        "order": 8,
        "xp_reward": 50,
        "visual_diagram_type": "two_pointers_array",
        "content": """# Linear Structures Summary & Tradeoff Matrix

| Structure | Access | Search | Insert | Delete |
| :--- | :--- | :--- | :--- | :--- |
| **Array** | $O(1)$ | $O(N)$ | $O(N)$ | $O(N)$ |
| **Linked List** | $O(N)$ | $O(N)$ | $O(1)$ | $O(1)$ |
| **Stack / Queue** | $O(1)$ top | $O(N)$ | $O(1)$ | $O(1)$ |
| **Binary Heap** | $O(1)$ peek | $O(N)$ | $O(\\log N)$ | $O(\\log N)$ |
"""
    },
    {
        "id": "dsa-binary-tree-traversals",
        "title": "Binary Tree Traversals: Recursive & Iterative",
        "slug": "dsa-binary-tree-traversals",
        "domain": "dsa",
        "color": "#F43F5E",
        "icon": "Binary",
        "is_published": True,
        "skills_taught": ['Big-O Notation', 'Data Structures', 'Algorithmic Patterns', 'Optimization'],
        "course_id": "course-dsa-lvl3",
        "order": 1,
        "xp_reward": 70,
        "visual_diagram_type": "bst_tree_traversal",
        "content": """# Tree Traversals & Depth-First Mechanics

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# In-order Traversal (Left -> Root -> Right)
def inorder(root: TreeNode | None) -> list[int]:
    res, stack, curr = [], [], root
    while curr or stack:
        while curr:
            stack.append(curr)
            curr = curr.left
        curr = stack.pop()
        res.append(curr.val)
        curr = curr.right
    return res
```
"""
    },
    {
        "id": "dsa-bst-operations-validation",
        "title": "BST Invariant, Search, Insertion & Validation",
        "slug": "dsa-bst-operations-validation",
        "domain": "dsa",
        "color": "#F43F5E",
        "icon": "Binary",
        "is_published": True,
        "skills_taught": ['Big-O Notation', 'Data Structures', 'Algorithmic Patterns', 'Optimization'],
        "course_id": "course-dsa-lvl3",
        "order": 2,
        "xp_reward": 70,
        "visual_diagram_type": "bst_tree_traversal",
        "content": """# Binary Search Tree Validation

A binary tree is a valid BST if and only if for every node $X$, all left descendants $< X.val <$ all right descendants.
Validating in $O(N)$ time with range bounds $(\\text{low}, \\text{high})$:
```python
def is_valid_bst(root: TreeNode | None, low=float('-inf'), high=float('inf')) -> bool:
    if not root:
        return True
    if not (low < root.val < high):
        return False
    return is_valid_bst(root.left, low, root.val) and is_valid_bst(root.right, root.val, high)
```
"""
    },
    {
        "id": "dsa-avl-trees-rotations",
        "title": "AVL Trees & Self-Balancing Rotations",
        "slug": "dsa-avl-trees-rotations",
        "domain": "dsa",
        "color": "#F43F5E",
        "icon": "Binary",
        "is_published": True,
        "skills_taught": ['Big-O Notation', 'Data Structures', 'Algorithmic Patterns', 'Optimization'],
        "course_id": "course-dsa-lvl3",
        "order": 3,
        "xp_reward": 80,
        "visual_diagram_type": "bst_tree_traversal",
        "content": """# AVL Self-Balancing Tree Rotations

Balance factor $\\text{BF}(N) = \\text{height}(\\text{left}) - \\text{height}(\\text{right}) \\in \\{-1, 0, 1\\}$.
Rotations:
- **Left Rotation (LL)**
- **Right Rotation (RR)**
- **Left-Right Rotation (LR)**
- **Right-Left Rotation (RL)**
"""
    },
    {
        "id": "dsa-trie-prefix-trees",
        "title": "Tries (Prefix Trees) & Autocomplete Engines",
        "slug": "dsa-trie-prefix-trees",
        "domain": "dsa",
        "color": "#F43F5E",
        "icon": "Binary",
        "is_published": True,
        "skills_taught": ['Big-O Notation', 'Data Structures', 'Algorithmic Patterns', 'Optimization'],
        "course_id": "course-dsa-lvl3",
        "order": 4,
        "xp_reward": 75,
        "visual_diagram_type": "bst_tree_traversal",
        "content": """# Trie Prefix Tree Implementation

```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True
```
"""
    },
    {
        "id": "dsa-segment-trees-lazy",
        "title": "Segment Trees & Lazy Propagation",
        "slug": "dsa-segment-trees-lazy",
        "domain": "dsa",
        "color": "#F43F5E",
        "icon": "Binary",
        "is_published": True,
        "skills_taught": ['Big-O Notation', 'Data Structures', 'Algorithmic Patterns', 'Optimization'],
        "course_id": "course-dsa-lvl3",
        "order": 5,
        "xp_reward": 85,
        "visual_diagram_type": "bst_tree_traversal",
        "content": """# Segment Trees for Range Queries in O(log N)

A Segment Tree builds an array tree where node $i$ stores the aggregate (sum, min, gcd) of range $[L, R]$.
Lazy propagation defers child updates to achieve $O(\\log N)$ range update time.
"""
    },
    {
        "id": "dsa-fenwick-binary-indexed-trees",
        "title": "Fenwick Trees (Binary Indexed Trees - BIT)",
        "slug": "dsa-fenwick-binary-indexed-trees",
        "domain": "dsa",
        "color": "#F43F5E",
        "icon": "Binary",
        "is_published": True,
        "skills_taught": ['Big-O Notation', 'Data Structures', 'Algorithmic Patterns', 'Optimization'],
        "course_id": "course-dsa-lvl3",
        "order": 6,
        "xp_reward": 80,
        "visual_diagram_type": "bst_tree_traversal",
        "content": """# Binary Indexed Tree (BIT) Mechanics

Uses lowest set bit `i & (-i)` to update and query prefix sums in $O(\\log N)$ with zero tree pointer overhead.
"""
    },
    {
        "id": "dsa-lca-binary-lifting",
        "title": "Lowest Common Ancestor (LCA) via Binary Lifting",
        "slug": "dsa-lca-binary-lifting",
        "domain": "dsa",
        "color": "#F43F5E",
        "icon": "Binary",
        "is_published": True,
        "skills_taught": ['Big-O Notation', 'Data Structures', 'Algorithmic Patterns', 'Optimization'],
        "course_id": "course-dsa-lvl3",
        "order": 7,
        "xp_reward": 85,
        "visual_diagram_type": "bst_tree_traversal",
        "content": """# Binary Lifting for O(log N) LCA

Precomputes $2^k$-th parent table `up[node][k]` to jump up the tree in logarithmic steps.
"""
    },
    {
        "id": "dsa-tree-dp-foundations",
        "title": "Tree Dynamic Programming Patterns",
        "slug": "dsa-tree-dp-foundations",
        "domain": "dsa",
        "color": "#F43F5E",
        "icon": "Binary",
        "is_published": True,
        "skills_taught": ['Big-O Notation', 'Data Structures', 'Algorithmic Patterns', 'Optimization'],
        "course_id": "course-dsa-lvl3",
        "order": 8,
        "xp_reward": 85,
        "visual_diagram_type": "bst_tree_traversal",
        "content": """# Tree DP: Subtree Aggregation & Re-Rooting

Solves tree diameter, maximum independent set on trees, and re-rooting technique in $O(N)$ time.
"""
    },
    {
        "id": "dsa-graph-representations-bfs-dfs",
        "title": "Graph Representations: Adjacency List, BFS & DFS",
        "slug": "dsa-graph-representations-bfs-dfs",
        "domain": "dsa",
        "color": "#F43F5E",
        "icon": "Binary",
        "is_published": True,
        "skills_taught": ['Big-O Notation', 'Data Structures', 'Algorithmic Patterns', 'Optimization'],
        "course_id": "course-dsa-lvl4",
        "order": 1,
        "xp_reward": 75,
        "visual_diagram_type": "two_pointers_array",
        "content": """# Graph Traversals: BFS & DFS

```python
from collections import deque

def bfs(graph: dict[int, list[int]], start: int) -> list[int]:
    visited = {start}
    queue = deque([start])
    order = []
    while queue:
        u = queue.popleft()
        order.append(u)
        for v in graph.get(u, []):
            if v not in visited:
                visited.add(v)
                queue.append(v)
    return order
```
"""
    },
    {
        "id": "dsa-cycle-detection-topological-sort",
        "title": "Cycle Detection & Kahn's Topological Sort",
        "slug": "dsa-cycle-detection-topological-sort",
        "domain": "dsa",
        "color": "#F43F5E",
        "icon": "Binary",
        "is_published": True,
        "skills_taught": ['Big-O Notation', 'Data Structures', 'Algorithmic Patterns', 'Optimization'],
        "course_id": "course-dsa-lvl4",
        "order": 2,
        "xp_reward": 80,
        "visual_diagram_type": "two_pointers_array",
        "content": """# Kahn's Algorithm (In-Degree Topological Sort)

For a Directed Acyclic Graph (DAG), Kahn's algorithm iteratively removes vertices with in-degree 0:
```python
def topological_sort(n: int, edges: list[tuple[int, int]]) -> list[int]:
    adj = {i: [] for i in range(n)}
    in_degree = [0] * n
    for u, v in edges:
        adj[u].append(v)
        in_degree[v] += 1
    
    queue = deque([i for i in range(n) if in_degree[i] == 0])
    order = []
    while queue:
        u = queue.popleft()
        order.append(u)
        for v in adj[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)
    return order if len(order) == n else []
```
"""
    },
    {
        "id": "dsa-dijkstra-shortest-path",
        "title": "Dijkstra's Single-Source Shortest Path",
        "slug": "dsa-dijkstra-shortest-path",
        "domain": "dsa",
        "color": "#F43F5E",
        "icon": "Binary",
        "is_published": True,
        "skills_taught": ['Big-O Notation', 'Data Structures', 'Algorithmic Patterns', 'Optimization'],
        "course_id": "course-dsa-lvl4",
        "order": 3,
        "xp_reward": 85,
        "visual_diagram_type": "two_pointers_array",
        "content": """# Dijkstra's Algorithm in O((V + E) log V)

Finds the shortest path from a source node to all other nodes in a weighted graph with non-negative edge weights.
"""
    },
    {
        "id": "dsa-bellman-ford-floyd-warshall",
        "title": "Bellman-Ford & Floyd-Warshall Algorithms",
        "slug": "dsa-bellman-ford-floyd-warshall",
        "domain": "dsa",
        "color": "#F43F5E",
        "icon": "Binary",
        "is_published": True,
        "skills_taught": ['Big-O Notation', 'Data Structures', 'Algorithmic Patterns', 'Optimization'],
        "course_id": "course-dsa-lvl4",
        "order": 4,
        "xp_reward": 85,
        "visual_diagram_type": "two_pointers_array",
        "content": """# Shortest Paths with Negative Weights

- **Bellman-Ford**: $O(V \\cdot E)$ time, detects negative weight cycles.
- **Floyd-Warshall**: $O(V^3)$ all-pairs shortest paths via dynamic programming:
  $$D[i][j] = \\min(D[i][j], D[i][k] + D[k][j])$$
"""
    },
    {
        "id": "dsa-dsu-kruskal-prim",
        "title": "Disjoint Set Union (DSU) & MST (Kruskal / Prim)",
        "slug": "dsa-dsu-kruskal-prim",
        "domain": "dsa",
        "color": "#F43F5E",
        "icon": "Binary",
        "is_published": True,
        "skills_taught": ['Big-O Notation', 'Data Structures', 'Algorithmic Patterns', 'Optimization'],
        "course_id": "course-dsa-lvl4",
        "order": 5,
        "xp_reward": 85,
        "visual_diagram_type": "two_pointers_array",
        "content": """# Disjoint Set Union (Union-Find) & Kruskal's MST

DSU with Path Compression and Union by Rank achieves $\\alpha(N)$ nearly constant time:
```python
class DSU:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]

    def union(self, x: int, y: int) -> bool:
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return False
        if self.rank[rx] < self.rank[ry]:
            rx, ry = ry, rx
        self.parent[ry] = rx
        if self.rank[rx] == self.rank[ry]:
            self.rank[rx] += 1
        return True
```
"""
    },
    {
        "id": "dsa-bipartite-graph-matching",
        "title": "Bipartite Graph Verification & 2-Coloring",
        "slug": "dsa-bipartite-graph-matching",
        "domain": "dsa",
        "color": "#F43F5E",
        "icon": "Binary",
        "is_published": True,
        "skills_taught": ['Big-O Notation', 'Data Structures', 'Algorithmic Patterns', 'Optimization'],
        "course_id": "course-dsa-lvl4",
        "order": 6,
        "xp_reward": 80,
        "visual_diagram_type": "two_pointers_array",
        "content": """# Bipartite Graph 2-Coloring

A graph is bipartite if and only if it contains no odd-length cycles.
"""
    },
    {
        "id": "dsa-scc-tarjan-bridges",
        "title": "Tarjan's SCC, Bridges & Articulation Points",
        "slug": "dsa-scc-tarjan-bridges",
        "domain": "dsa",
        "color": "#F43F5E",
        "icon": "Binary",
        "is_published": True,
        "skills_taught": ['Big-O Notation', 'Data Structures', 'Algorithmic Patterns', 'Optimization'],
        "course_id": "course-dsa-lvl4",
        "order": 7,
        "xp_reward": 90,
        "visual_diagram_type": "two_pointers_array",
        "content": """# Tarjan's Algorithm for Bridges & Critical Connections

Uses DFS discovery time `tin[u]` and low-link value `low[u]`.
An edge $(u, v)$ is a **Bridge** if and only if `low[v] > tin[u]`.
"""
    },
    {
        "id": "dsa-network-flow-max-cut",
        "title": "Max-Flow Min-Cut: Edmonds-Karp & Dinic",
        "slug": "dsa-network-flow-max-cut",
        "domain": "dsa",
        "color": "#F43F5E",
        "icon": "Binary",
        "is_published": True,
        "skills_taught": ['Big-O Notation', 'Data Structures', 'Algorithmic Patterns', 'Optimization'],
        "course_id": "course-dsa-lvl4",
        "order": 8,
        "xp_reward": 95,
        "visual_diagram_type": "two_pointers_array",
        "content": """# Ford-Fulkerson & Dinic's Algorithm

The **Max-Flow Min-Cut Theorem** proves the maximum flow through a network equals the minimum capacity cut separating source $S$ from sink $T$.
"""
    },
    {
        "id": "dsa-binary-search-on-answer",
        "title": "Binary Search on Monotonic Answer Spaces",
        "slug": "dsa-binary-search-on-answer",
        "domain": "dsa",
        "color": "#F43F5E",
        "icon": "Binary",
        "is_published": True,
        "skills_taught": ['Big-O Notation', 'Data Structures', 'Algorithmic Patterns', 'Optimization'],
        "course_id": "course-dsa-lvl5",
        "order": 1,
        "xp_reward": 85,
        "visual_diagram_type": "two_pointers_array",
        "content": """# Binary Search on Monotonic Predicates

When a feasibility function $f(x) \\in \\{\\text{False}, \\text{True}\\}$ is monotonic, we binary search over the answer space in $O(\\log(\\text{Range}) \\times \\text{CheckTime})$.
"""
    },
    {
        "id": "dsa-greedy-interval-scheduling",
        "title": "Greedy Strategies & Interval Scheduling",
        "slug": "dsa-greedy-interval-scheduling",
        "domain": "dsa",
        "color": "#F43F5E",
        "icon": "Binary",
        "is_published": True,
        "skills_taught": ['Big-O Notation', 'Data Structures', 'Algorithmic Patterns', 'Optimization'],
        "course_id": "course-dsa-lvl5",
        "order": 2,
        "xp_reward": 80,
        "visual_diagram_type": "two_pointers_array",
        "content": """# Interval Scheduling Maximization

Sorting intervals by earliest end time yields optimal non-overlapping interval selection.
"""
    },
    {
        "id": "dsa-dp-knapsack-variants",
        "title": "0/1 Knapsack, Unbounded Knapsack & Space Compression",
        "slug": "dsa-dp-knapsack-variants",
        "domain": "dsa",
        "color": "#F43F5E",
        "icon": "Binary",
        "is_published": True,
        "skills_taught": ['Big-O Notation', 'Data Structures', 'Algorithmic Patterns', 'Optimization'],
        "course_id": "course-dsa-lvl5",
        "order": 3,
        "xp_reward": 90,
        "visual_diagram_type": "two_pointers_array",
        "content": """# Dynamic Programming: Knapsack Mastery

### 0/1 Knapsack Recurrence:
$$\\text{dp}[w] = \\max(\\text{dp}[w], \\,\\text{val}[i] + \\text{dp}[w - \\text{wt}[i]])$$
Iterating capacity $w$ backwards from $W \\to \\text{wt}[i]$ allows 1D space optimization $O(W)$.
"""
    },
    {
        "id": "dsa-dp-lcs-lis-grid",
        "title": "LCS, LIS with Patience Sorting & Edit Distance",
        "slug": "dsa-dp-lcs-lis-grid",
        "domain": "dsa",
        "color": "#F43F5E",
        "icon": "Binary",
        "is_published": True,
        "skills_taught": ['Big-O Notation', 'Data Structures', 'Algorithmic Patterns', 'Optimization'],
        "course_id": "course-dsa-lvl5",
        "order": 4,
        "xp_reward": 90,
        "visual_diagram_type": "two_pointers_array",
        "content": """# Longest Increasing Subsequence in O(N log N)

Patience sorting maintains the smallest tail of all increasing subsequences of length $L$, updated via binary search.
"""
    },
    {
        "id": "dsa-bitmask-dp-tsp",
        "title": "Bitmask DP & Traveling Salesperson Problem",
        "slug": "dsa-bitmask-dp-tsp",
        "domain": "dsa",
        "color": "#F43F5E",
        "icon": "Binary",
        "is_published": True,
        "skills_taught": ['Big-O Notation', 'Data Structures', 'Algorithmic Patterns', 'Optimization'],
        "course_id": "course-dsa-lvl5",
        "order": 5,
        "xp_reward": 95,
        "visual_diagram_type": "two_pointers_array",
        "content": """# Bitmask DP: State Representation in O(2^N * N^2)

Represents visited node sets as binary integers `mask & (1 << u)` to solve TSP in exponential time instead of $O(N!)$ factorial.
"""
    },
    {
        "id": "dsa-digit-dp-numeric-ranges",
        "title": "Digit DP for Range Constrained Numbers",
        "slug": "dsa-digit-dp-numeric-ranges",
        "domain": "dsa",
        "color": "#F43F5E",
        "icon": "Binary",
        "is_published": True,
        "skills_taught": ['Big-O Notation', 'Data Structures', 'Algorithmic Patterns', 'Optimization'],
        "course_id": "course-dsa-lvl5",
        "order": 6,
        "xp_reward": 95,
        "visual_diagram_type": "two_pointers_array",
        "content": """# Digit DP: Counting Numbers with Properties in [L, R]

State tuple `dp(index, is_tight, is_leading_zero, mask)`.
"""
    },
    {
        "id": "dsa-kmp-z-algorithm-strings",
        "title": "KMP Pattern Matching & The Z-Algorithm",
        "slug": "dsa-kmp-z-algorithm-strings",
        "domain": "dsa",
        "color": "#F43F5E",
        "icon": "Binary",
        "is_published": True,
        "skills_taught": ['Big-O Notation', 'Data Structures', 'Algorithmic Patterns', 'Optimization'],
        "course_id": "course-dsa-lvl5",
        "order": 7,
        "xp_reward": 95,
        "visual_diagram_type": "two_pointers_array",
        "content": """# Knuth-Morris-Pratt (KMP) in O(N + M)

Constructs the Longest Proper Prefix which is also Suffix (LPS) array to avoid backtracking on mismatch.
"""
    },
    {
        "id": "dsa-computational-geometry-convex-hull",
        "title": "Computational Geometry: Graham Scan Convex Hull",
        "slug": "dsa-computational-geometry-convex-hull",
        "domain": "dsa",
        "color": "#F43F5E",
        "icon": "Binary",
        "is_published": True,
        "skills_taught": ['Big-O Notation', 'Data Structures', 'Algorithmic Patterns', 'Optimization'],
        "course_id": "course-dsa-lvl5",
        "order": 8,
        "xp_reward": 100,
        "visual_diagram_type": "two_pointers_array",
        "content": """# Graham Scan & Cross Product Orientation

The 2D cross product $(p_2.x - p_1.x)(p_3.y - p_1.y) - (p_2.y - p_1.y)(p_3.x - p_1.x)$ determines counter-clockwise vs clockwise turns in $O(N \\log N)$ time.
"""
    }
]

QUIZZES_DATA = [
    {
        "id": "quiz-dsa-lvl1",
        "lesson_id": "dsa-asymptotic-complexity",
        "title": "Asymptotic Complexity & Array Patterns Diagnostic",
        "passing_score": 80,
        "questions": [
            {
                "id": "q-dsa-1-1",
                "question": "What is the amortized time complexity of appending an element to a dynamic array?",
                "options": ["O(N)", "O(1)", "O(log N)", "O(N^2)"],
                "correct_option_index": 1,
                "explanation": "Dynamic arrays double capacity geometrically when full. Over N insertions, total resize copying is 2N, giving O(1) amortized append time."
            },
            {
                "id": "q-dsa-1-2",
                "question": "Why does Two Pointers reduce the complexity of Two Sum on a sorted array from O(N^2) to O(N)?",
                "options": [
                    "It computes the Cartesian product",
                    "Each pointer moves monotonically, visiting each element at most once",
                    "It hashes elements to O(1) buckets",
                    "It sorts the array in O(1)"
                ],
                "correct_option_index": 1,
                "explanation": "Because the array is sorted, comparing sum against target allows discarding one whole search branch monotonically."
            }
        ]
    }
]

SKILLS_DATA = [
    {
        "id": "skill-dsa-foundations",
        "name": "DSA Foundations & Array Mastery",
        "category": "Arrays & Strings",
        "level": 1,
        "unlocked": True,
        "progress": 0.0,
        "prerequisites": [],
        "description": "Master asymptotic Big-O bounds, Sliding Window, and Two Pointers."
    },
    {
        "id": "skill-dsa-trees-graphs",
        "name": "Trees, BSTs & Graph Algorithms",
        "category": "Trees & Graphs",
        "level": 2,
        "unlocked": True,
        "progress": 0.0,
        "prerequisites": ["skill-dsa-foundations"],
        "description": "Master BST traversals, Dijkstra, DSU, Segment Trees, and Tarjan's SCC."
    },
    {
        "id": "skill-dsa-advanced-dp",
        "name": "Advanced Dynamic Programming & Paradigms",
        "category": "Dynamic Programming",
        "level": 3,
        "unlocked": True,
        "progress": 0.0,
        "prerequisites": ["skill-dsa-trees-graphs"],
        "description": "Master Knapsack variants, Bitmask DP, Tree DP, KMP, and Computational Geometry."
    }
]
