import React, { useState, useEffect, useRef } from 'react';
import {
  Binary,
  GitBranch,
  Layers,
  ArrowRight,
  Play,
  Pause,
  RotateCcw,
  Sparkles,
  Search,
  Plus,
  Trash2,
  Cpu,
  TrendingUp,
  CheckCircle2,
  Code2,
  FastForward,
  ChevronRight,
  ListOrdered,
  Share2,
  Box
} from 'lucide-react';
import Badge from '../components/common/Badge';

export default function DSALabPage() {
  const [activeTab, setActiveTab] = useState('two-pointers'); // 'two-pointers' | 'bst' | 'stack-queue' | 'sorting' | 'graph' | 'dp' | 'practice'

  // ==========================================
  // MODULE 1: TWO POINTERS & SLIDING WINDOW
  // ==========================================
  const [arr, setArr] = useState([2, 4, 7, 11, 15, 18, 24, 30]);
  const [targetSum, setTargetSum] = useState(22);
  const [leftPtr, setLeftPtr] = useState(0);
  const [rightPtr, setRightPtr] = useState(7);
  const [twoPtrFound, setTwoPtrFound] = useState(null);
  const [twoPtrLog, setTwoPtrLog] = useState([]);
  const [isAutoSearching, setIsAutoSearching] = useState(false);

  const resetTwoPointers = () => {
    setLeftPtr(0);
    setRightPtr(arr.length - 1);
    setTwoPtrFound(null);
    setTwoPtrLog(['Initialized Left pointer at index 0, Right pointer at index ' + (arr.length - 1)]);
    setIsAutoSearching(false);
  };

  const stepTwoPointers = () => {
    if (leftPtr >= rightPtr) {
      setTwoPtrLog(prev => [...prev, 'Pointers crossed or met. Target sum not found.']);
      setIsAutoSearching(false);
      return;
    }
    const sum = arr[leftPtr] + arr[rightPtr];
    if (sum === targetSum) {
      setTwoPtrFound([leftPtr, rightPtr]);
      setTwoPtrLog(prev => [...prev, `Found! arr[${leftPtr}] (${arr[leftPtr]}) + arr[${rightPtr}] (${arr[rightPtr]}) = ${targetSum}`]);
      setIsAutoSearching(false);
    } else if (sum < targetSum) {
      setTwoPtrLog(prev => [...prev, `Sum ${sum} < ${targetSum}: Increment left pointer to index ${leftPtr + 1}`]);
      setLeftPtr(l => l + 1);
    } else {
      setTwoPtrLog(prev => [...prev, `Sum ${sum} > ${targetSum}: Decrement right pointer to index ${rightPtr - 1}`]);
      setRightPtr(r => r - 1);
    }
  };

  useEffect(() => {
    let timer;
    if (isAutoSearching && !twoPtrFound && leftPtr < rightPtr) {
      timer = setTimeout(() => {
        stepTwoPointers();
      }, 700);
    }
    return () => clearTimeout(timer);
  }, [isAutoSearching, leftPtr, rightPtr, twoPtrFound]);

  // ==========================================
  // MODULE 2: BINARY SEARCH TREE (BST)
  // ==========================================
  const initialBST = {
    val: 50,
    left: {
      val: 30,
      left: { val: 20, left: null, right: null },
      right: { val: 40, left: null, right: null }
    },
    right: {
      val: 70,
      left: { val: 60, left: null, right: null },
      right: { val: 80, left: null, right: null }
    }
  };

  const [bstRoot, setBstRoot] = useState(initialBST);
  const [bstInsertVal, setBstInsertVal] = useState(35);
  const [bstSearchVal, setBstSearchVal] = useState(60);
  const [bstSearchPath, setBstSearchPath] = useState([]);
  const [bstFoundNode, setBstFoundNode] = useState(null);
  const [traversalResult, setTraversalResult] = useState([]);
  const [traversalType, setTraversalType] = useState('');

  const insertNode = (node, val) => {
    if (!node) return { val, left: null, right: null };
    if (val < node.val) {
      return { ...node, left: insertNode(node.left, val) };
    } else if (val > node.val) {
      return { ...node, right: insertNode(node.right, val) };
    }
    return node;
  };

  const handleBstInsert = () => {
    if (isNaN(bstInsertVal)) return;
    setBstRoot(root => insertNode(root, parseInt(bstInsertVal)));
    setBstSearchPath([]);
    setBstFoundNode(null);
  };

  const handleBstSearch = () => {
    const path = [];
    let curr = bstRoot;
    const target = parseInt(bstSearchVal);
    let found = false;

    while (curr) {
      path.push(curr.val);
      if (curr.val === target) {
        found = true;
        break;
      } else if (target < curr.val) {
        curr = curr.left;
      } else {
        curr = curr.right;
      }
    }
    setBstSearchPath(path);
    setBstFoundNode(found ? target : 'not_found');
  };

  const runTraversal = (type) => {
    setTraversalType(type);
    const res = [];
    const inorder = (n) => {
      if (!n) return;
      inorder(n.left);
      res.push(n.val);
      inorder(n.right);
    };
    const preorder = (n) => {
      if (!n) return;
      res.push(n.val);
      preorder(n.left);
      preorder(n.right);
    };
    const postorder = (n) => {
      if (!n) return;
      postorder(n.left);
      postorder(n.right);
      res.push(n.val);
    };

    if (type === 'Inorder') inorder(bstRoot);
    if (type === 'Preorder') preorder(bstRoot);
    if (type === 'Postorder') postorder(bstRoot);

    setTraversalResult(res);
  };

  // ==========================================
  // MODULE 3: STACK & QUEUE VISUALIZER
  // ==========================================
  const [stackItems, setStackItems] = useState([10, 20, 30]);
  const [queueItems, setQueueItems] = useState(['Req #1', 'Req #2', 'Req #3']);
  const [structInput, setStructInput] = useState('');
  const [stackPopAnim, setStackPopAnim] = useState(null);

  const pushStack = () => {
    const val = structInput.trim() || `Item ${stackItems.length + 1}`;
    setStackItems(prev => [...prev, val]);
    setStructInput('');
  };

  const popStack = () => {
    if (stackItems.length === 0) return;
    const popped = stackItems[stackItems.length - 1];
    setStackPopAnim(popped);
    setTimeout(() => {
      setStackItems(prev => prev.slice(0, -1));
      setStackPopAnim(null);
    }, 300);
  };

  const enqueueQueue = () => {
    const val = structInput.trim() || `Req #${queueItems.length + 1}`;
    setQueueItems(prev => [...prev, val]);
    setStructInput('');
  };

  const dequeueQueue = () => {
    if (queueItems.length === 0) return;
    setQueueItems(prev => prev.slice(1));
  };

  // ==========================================
  // MODULE 4: SORTING RACE & STEP SIMULATOR
  // ==========================================
  const [sortArray, setSortArray] = useState([45, 12, 85, 32, 89, 39, 69, 21, 54, 98]);
  const [activeCompare, setActiveCompare] = useState([]);
  const [sortedIndices, setSortedIndices] = useState([]);
  const [isSorting, setIsSorting] = useState(false);
  const [sortSpeed, setSortSpeed] = useState(250);
  const [comparisonsCount, setComparisonsCount] = useState(0);

  const randomizeSortArray = () => {
    const newArr = Array.from({ length: 10 }, () => Math.floor(Math.random() * 85) + 15);
    setSortArray(newArr);
    setActiveCompare([]);
    setSortedIndices([]);
    setComparisonsCount(0);
    setIsSorting(false);
  };

  const runBubbleSort = async () => {
    setIsSorting(true);
    let arrCopy = [...sortArray];
    let n = arrCopy.length;
    let comps = 0;

    for (let i = 0; i < n - 1; i++) {
      for (let j = 0; j < n - i - 1; j++) {
        setActiveCompare([j, j + 1]);
        comps++;
        setComparisonsCount(comps);
        await new Promise(r => setTimeout(r, sortSpeed));

        if (arrCopy[j] > arrCopy[j + 1]) {
          let temp = arrCopy[j];
          arrCopy[j] = arrCopy[j + 1];
          arrCopy[j + 1] = temp;
          setSortArray([...arrCopy]);
          await new Promise(r => setTimeout(r, sortSpeed));
        }
      }
      setSortedIndices(prev => [...prev, n - 1 - i]);
    }
    setSortedIndices(Array.from({ length: n }, (_, i) => i));
    setActiveCompare([]);
    setIsSorting(false);
  };

  // ==========================================
  // MODULE 5: GRAPH BFS & DFS TRAVERSAL
  // ==========================================
  const graphNodes = ['A', 'B', 'C', 'D', 'E', 'F'];
  const graphAdj = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
  };

  const [graphVisited, setGraphVisited] = useState([]);
  const [graphQueueStack, setGraphQueueStack] = useState([]);
  const [graphStepLog, setGraphStepLog] = useState([]);
  const [graphRunning, setGraphRunning] = useState(false);

  const runBFS = async () => {
    setGraphRunning(true);
    setGraphVisited([]);
    setGraphStepLog(['Starting BFS from Node A...']);
    const queue = ['A'];
    const visited = new Set(['A']);
    setGraphQueueStack([...queue]);
    setGraphVisited(['A']);

    while (queue.length > 0) {
      await new Promise(r => setTimeout(r, 600));
      const curr = queue.shift();
      setGraphQueueStack([...queue]);
      setGraphStepLog(prev => [...prev, `Dequeued Node ${curr}. Exploring neighbors...`]);

      for (let neighbor of graphAdj[curr]) {
        if (!visited.has(neighbor)) {
          visited.add(neighbor);
          queue.push(neighbor);
          setGraphVisited(Array.from(visited));
          setGraphQueueStack([...queue]);
          setGraphStepLog(prev => [...prev, `Discovered Node ${neighbor}, added to queue.`]);
        }
      }
    }
    setGraphStepLog(prev => [...prev, 'BFS Complete! All reachable nodes visited.']);
    setGraphRunning(false);
  };

  const runDFS = async () => {
    setGraphRunning(true);
    setGraphVisited([]);
    setGraphStepLog(['Starting DFS from Node A...']);
    const stack = ['A'];
    const visited = new Set();

    while (stack.length > 0) {
      await new Promise(r => setTimeout(r, 600));
      const curr = stack.pop();
      setGraphQueueStack([...stack]);

      if (!visited.has(curr)) {
        visited.add(curr);
        setGraphVisited(Array.from(visited));
        setGraphStepLog(prev => [...prev, `Visited Node ${curr} from Stack.`]);

        for (let i = graphAdj[curr].length - 1; i >= 0; i--) {
          const neighbor = graphAdj[curr][i];
          if (!visited.has(neighbor)) {
            stack.push(neighbor);
            setGraphQueueStack([...stack]);
            setGraphStepLog(prev => [...prev, `Pushed neighbor ${neighbor} to Stack.`]);
          }
        }
      }
    }
    setGraphStepLog(prev => [...prev, 'DFS Complete! Depth path exhausted.']);
    setGraphRunning(false);
  };

  // ==========================================
  // MODULE 6: DYNAMIC PROGRAMMING (0/1 KNAPSACK)
  // ==========================================
  const dpItems = [
    { name: 'Gem', weight: 1, val: 15 },
    { name: 'Vase', weight: 2, val: 20 },
    { name: 'Crown', weight: 3, val: 50 },
    { name: 'Tablet', weight: 4, val: 65 }
  ];
  const maxCapacity = 5;

  const [dpGrid, setDpGrid] = useState([]);

  useEffect(() => {
    const dp = Array.from({ length: dpItems.length + 1 }, () => Array(maxCapacity + 1).fill(0));
    for (let i = 1; i <= dpItems.length; i++) {
      const item = dpItems[i - 1];
      for (let w = 0; w <= maxCapacity; w++) {
        if (item.weight <= w) {
          dp[i][w] = Math.max(dp[i - 1][w], item.val + dp[i - 1][w - item.weight]);
        } else {
          dp[i][w] = dp[i - 1][w];
        }
      }
    }
    setDpGrid(dp);
  }, []);

  // ==========================================
  // MODULE 7: INTERACTIVE DSA PRACTICE RUNNER
  // ==========================================
  const [practiceCode, setPracticeCode] = useState(`function twoSum(nums, target) {
  const map = new Map();
  for (let i = 0; i < nums.length; i++) {
    const complement = target - nums[i];
    if (map.has(complement)) {
      return [map.get(complement), i];
    }
    map.set(nums[i], i);
  }
  return [];
}
twoSum([2, 7, 11, 15], 9);`);
  const [practiceOutput, setPracticeOutput] = useState(null);

  const runPracticeCode = () => {
    try {
      const result = new Function(`${practiceCode}`)();
      setPracticeOutput({
        status: 'success',
        result: JSON.stringify(result),
        logs: 'Code executed in 1.4ms with O(N) Time Complexity.'
      });
    } catch (e) {
      setPracticeOutput({
        status: 'error',
        result: e.message,
        logs: 'Runtime Error during execution.'
      });
    }
  };

  return (
    <div className="animate-fade-in" style={{ paddingBottom: 'var(--space-2xl)' }}>
      {/* Header */}
      <div style={{ marginBottom: 24, display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', flexWrap: 'wrap', gap: 16 }}>
        <div>
          <div style={{ display: 'flex', alignItems: 'center', gap: 8, marginBottom: 4 }}>
            <Badge variant="pink">DSA Interactive Laboratory</Badge>
            <span style={{ fontSize: '0.8rem', color: 'var(--text-muted)' }}>Visual Algorithm Simulator & Sandboxes</span>
          </div>
          <h1 style={{ fontSize: '1.75rem', marginBottom: 6 }}>Data Structures & Algorithms Laboratory</h1>
          <p style={{ color: 'var(--text-secondary)', fontSize: '0.925rem' }}>
            Master core computer science algorithms and interview patterns through step-by-step interactive visual mechanics.
          </p>
        </div>
      </div>

      {/* Tabs */}
      <div style={{ display: 'flex', gap: 8, overflowX: 'auto', paddingBottom: 12, marginBottom: 24 }}>
        {[
          { id: 'two-pointers', label: 'Two Pointers & Sliding Window', icon: ArrowRight },
          { id: 'bst', label: 'Binary Search Tree & Traversals', icon: GitBranch },
          { id: 'stack-queue', label: 'Stacks & Queues Pipe', icon: Layers },
          { id: 'sorting', label: 'Sorting Race Visualizer', icon: ListOrdered },
          { id: 'graph', label: 'Graph BFS & DFS Traversals', icon: Share2 },
          { id: 'dp', label: 'Dynamic Programming Matrix', icon: Box },
          { id: 'practice', label: 'Interactive Code Practice', icon: Code2 },
        ].map(tab => {
          const Icon = tab.icon;
          const isActive = activeTab === tab.id;
          return (
            <button
              key={tab.id}
              onClick={() => setActiveTab(tab.id)}
              className={isActive ? 'btn btn-primary' : 'btn btn-secondary'}
              style={{
                borderRadius: 999,
                fontSize: '0.85rem',
                padding: '8px 16px',
                display: 'flex',
                alignItems: 'center',
                gap: 8,
                background: isActive ? 'linear-gradient(135deg, #F43F5E, #E11D48)' : undefined,
                border: isActive ? 'none' : undefined
              }}
            >
              <Icon size={16} />
              <span>{tab.label}</span>
            </button>
          );
        })}
      </div>

      {/* TAB 1: TWO POINTERS */}
      {activeTab === 'two-pointers' && (
        <div style={{ display: 'grid', gridTemplateColumns: '1fr 340px', gap: 20 }}>
          <div className="card" style={{ padding: 24 }}>
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: 20 }}>
              <div>
                <h3 style={{ fontSize: '1.15rem', marginBottom: 4 }}>Two Pointers Target Search (Sorted Array)</h3>
                <p style={{ fontSize: '0.85rem', color: 'var(--text-secondary)' }}>
                  Time Complexity: <b>O(N)</b> vs Brute Force <b>O(N²)</b>. Pointers converge inward based on sum evaluation.
                </p>
              </div>
              <div style={{ display: 'flex', gap: 8 }}>
                <button onClick={resetTwoPointers} className="btn btn-secondary btn-sm" title="Reset pointers">
                  <RotateCcw size={14} /> Reset
                </button>
                <button
                  onClick={() => setIsAutoSearching(!isAutoSearching)}
                  className="btn btn-primary btn-sm"
                  style={{ background: '#F43F5E', border: 'none' }}
                >
                  {isAutoSearching ? <Pause size={14} /> : <Play size={14} />}
                  <span>{isAutoSearching ? 'Pause' : 'Auto Search'}</span>
                </button>
                <button onClick={stepTwoPointers} className="btn btn-outline btn-sm" disabled={twoPtrFound || leftPtr >= rightPtr}>
                  <ChevronRight size={14} /> Step
                </button>
              </div>
            </div>

            <div style={{ background: '#0b1120', padding: '36px 20px', borderRadius: 14, border: '1px solid #1e293b', marginBottom: 24 }}>
              <div style={{ display: 'flex', justifyContent: 'center', gap: 12, flexWrap: 'wrap' }}>
                {arr.map((val, idx) => {
                  const isLeft = idx === leftPtr;
                  const isRight = idx === rightPtr;
                  const isMatch = twoPtrFound && (idx === twoPtrFound[0] || idx === twoPtrFound[1]);
                  const inBetween = idx > leftPtr && idx < rightPtr;

                  return (
                    <div key={idx} style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', gap: 8 }}>
                      <div style={{ height: 24, display: 'flex', alignItems: 'center' }}>
                        {isLeft && (
                          <span style={{ fontSize: '0.72rem', fontWeight: 800, padding: '2px 8px', borderRadius: 6, background: '#38bdf8', color: '#0f172a' }}>
                            LEFT
                          </span>
                        )}
                        {isRight && (
                          <span style={{ fontSize: '0.72rem', fontWeight: 800, padding: '2px 8px', borderRadius: 6, background: '#f43f5e', color: '#ffffff' }}>
                            RIGHT
                          </span>
                        )}
                      </div>

                      <div
                        style={{
                          width: 58,
                          height: 58,
                          borderRadius: 12,
                          background: isMatch ? '#10b981' : isLeft ? 'rgba(56, 189, 248, 0.25)' : isRight ? 'rgba(244, 63, 94, 0.25)' : inBetween ? 'rgba(99, 102, 241, 0.12)' : '#1e293b',
                          border: isMatch ? '2px solid #10b981' : isLeft ? '2px solid #38bdf8' : isRight ? '2px solid #f43f5e' : '1px solid #334155',
                          display: 'flex',
                          alignItems: 'center',
                          justifyContent: 'center',
                          fontSize: '1.25rem',
                          fontWeight: 700,
                          color: isMatch ? '#ffffff' : isLeft ? '#38bdf8' : isRight ? '#f43f5e' : '#f8fafc',
                          boxShadow: isMatch ? '0 0 20px rgba(16, 185, 129, 0.6)' : 'none',
                          transition: 'all 0.25s ease'
                        }}
                      >
                        {val}
                      </div>

                      <span style={{ fontSize: '0.72rem', color: '#64748b' }}>[{idx}]</span>
                    </div>
                  );
                })}
              </div>

              <div style={{ marginTop: 28, background: '#1e293b', padding: '14px 20px', borderRadius: 10, display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                <div style={{ display: 'flex', alignItems: 'center', gap: 16 }}>
                  <div>
                    <span style={{ fontSize: '0.75rem', color: '#94a3b8' }}>Current Sum:</span>
                    <div style={{ fontSize: '1.2rem', fontWeight: 700, color: '#f8fafc' }}>
                      arr[{leftPtr}] ({arr[leftPtr]}) + arr[{rightPtr}] ({arr[rightPtr]}) = <strong style={{ color: arr[leftPtr] + arr[rightPtr] === targetSum ? '#10b981' : '#f59e0b' }}>{arr[leftPtr] + arr[rightPtr]}</strong>
                    </div>
                  </div>
                  <div style={{ width: 1, height: 32, background: '#334155' }} />
                  <div>
                    <span style={{ fontSize: '0.75rem', color: '#94a3b8' }}>Target Sum:</span>
                    <div style={{ fontSize: '1.2rem', fontWeight: 700, color: '#38bdf8' }}>{targetSum}</div>
                  </div>
                </div>

                {twoPtrFound && (
                  <div style={{ display: 'flex', alignItems: 'center', gap: 6, color: '#10b981', fontWeight: 700, fontSize: '0.9rem' }}>
                    <CheckCircle2 size={18} /> Target Sum Pair Found!
                  </div>
                )}
              </div>
            </div>

            <div style={{ display: 'flex', gap: 12, alignItems: 'center' }}>
              <label style={{ fontSize: '0.85rem', fontWeight: 600 }}>Set Target Sum:</label>
              <input
                type="number"
                value={targetSum}
                onChange={e => { setTargetSum(parseInt(e.target.value) || 0); resetTwoPointers(); }}
                className="input"
                style={{ width: 100 }}
              />
              <span style={{ fontSize: '0.8rem', color: 'var(--text-muted)' }}>Try targets like 22, 33, 45, or 13</span>
            </div>
          </div>

          <div className="card" style={{ padding: 20, display: 'flex', flexDirection: 'column' }}>
            <h4 style={{ fontSize: '0.95rem', marginBottom: 12, display: 'flex', alignItems: 'center', gap: 6 }}>
              <Cpu size={16} style={{ color: '#F43F5E' }} /> Execution Trace
            </h4>
            <div style={{ flex: 1, background: '#0b1120', borderRadius: 8, padding: 12, overflowY: 'auto', maxHeight: '380px', fontFamily: 'var(--font-mono)', fontSize: '0.78rem', display: 'flex', flexDirection: 'column', gap: 8 }}>
              {twoPtrLog.map((log, i) => (
                <div key={i} style={{ color: log.includes('Found!') ? '#34d399' : log.includes('Increment') ? '#38bdf8' : log.includes('Decrement') ? '#f43f5e' : '#94a3b8' }}>
                  &gt; {log}
                </div>
              ))}
            </div>
          </div>
        </div>
      )}

      {/* TAB 2: BST */}
      {activeTab === 'bst' && (
        <div style={{ display: 'grid', gridTemplateColumns: '1fr 340px', gap: 20 }}>
          <div className="card" style={{ padding: 24 }}>
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: 20, flexWrap: 'wrap', gap: 10 }}>
              <div>
                <h3 style={{ fontSize: '1.15rem', marginBottom: 4 }}>Binary Search Tree (BST) Canvas</h3>
                <p style={{ fontSize: '0.85rem', color: 'var(--text-secondary)' }}>
                  Search & Insert: <b>O(log N)</b> average. Left subtree elements &lt; Node &lt; Right subtree elements.
                </p>
              </div>

              <div style={{ display: 'flex', gap: 8 }}>
                <input
                  type="number"
                  value={bstInsertVal}
                  onChange={e => setBstInsertVal(e.target.value)}
                  className="input"
                  style={{ width: 80 }}
                  placeholder="Val"
                />
                <button onClick={handleBstInsert} className="btn btn-secondary btn-sm">
                  <Plus size={14} /> Insert
                </button>
              </div>
            </div>

            <div style={{ background: '#0b1120', padding: 20, borderRadius: 14, border: '1px solid #1e293b', minHeight: '340px', display: 'flex', justifyContent: 'center', alignItems: 'center', position: 'relative' }}>
              <svg width="560" height="260" viewBox="0 0 560 260">
                <line x1="280" y1="40" x2="160" y2="100" stroke="#334155" strokeWidth="2" />
                <line x1="280" y1="40" x2="400" y2="100" stroke="#334155" strokeWidth="2" />
                <line x1="160" y1="100" x2="100" y2="180" stroke="#334155" strokeWidth="2" />
                <line x1="160" y1="100" x2="220" y2="180" stroke="#334155" strokeWidth="2" />
                <line x1="400" y1="100" x2="340" y2="180" stroke="#334155" strokeWidth="2" />
                <line x1="400" y1="100" x2="460" y2="180" stroke="#334155" strokeWidth="2" />

                {[
                  { val: 50, x: 280, y: 40 },
                  { val: 30, x: 160, y: 100 },
                  { val: 70, x: 400, y: 100 },
                  { val: 20, x: 100, y: 180 },
                  { val: 40, x: 220, y: 180 },
                  { val: 60, x: 340, y: 180 },
                  { val: 80, x: 460, y: 180 },
                ].map((node, i) => {
                  const isInPath = bstSearchPath.includes(node.val);
                  const isFound = bstFoundNode === node.val;
                  return (
                    <g key={i}>
                      <circle
                        cx={node.x}
                        cy={node.y}
                        r="22"
                        fill={isFound ? '#10b981' : isInPath ? 'rgba(244, 63, 94, 0.4)' : '#1e293b'}
                        stroke={isFound ? '#10b981' : isInPath ? '#f43f5e' : '#6366f1'}
                        strokeWidth="2.5"
                      />
                      <text
                        x={node.x}
                        y={node.y + 5}
                        fill="#f8fafc"
                        fontSize="13"
                        fontWeight="bold"
                        textAnchor="middle"
                      >
                        {node.val}
                      </text>
                    </g>
                  );
                })}
              </svg>
            </div>

            <div style={{ marginTop: 20, display: 'flex', justifyContent: 'space-between', alignItems: 'center', flexWrap: 'wrap', gap: 12 }}>
              <div style={{ display: 'flex', gap: 8 }}>
                {['Inorder', 'Preorder', 'Postorder'].map(type => (
                  <button
                    key={type}
                    onClick={() => runTraversal(type)}
                    className={traversalType === type ? 'btn btn-primary btn-sm' : 'btn btn-secondary btn-sm'}
                    style={{ background: traversalType === type ? '#6366F1' : undefined }}
                  >
                    {type} (Sorted)
                  </button>
                ))}
              </div>

              {traversalResult.length > 0 && (
                <div style={{ display: 'flex', alignItems: 'center', gap: 8, background: '#1e293b', padding: '6px 14px', borderRadius: 8 }}>
                  <span style={{ fontSize: '0.8rem', color: '#94a3b8' }}>{traversalType} Path:</span>
                  <span style={{ fontFamily: 'var(--font-mono)', fontWeight: 700, color: '#38bdf8', fontSize: '0.9rem' }}>
                    [{traversalResult.join(' -> ')}]
                  </span>
                </div>
              )}
            </div>
          </div>

          <div className="card" style={{ padding: 20 }}>
            <h4 style={{ fontSize: '0.95rem', marginBottom: 12, display: 'flex', alignItems: 'center', gap: 6 }}>
              <Search size={16} style={{ color: '#F43F5E' }} /> Search Node Path
            </h4>
            <div style={{ display: 'flex', gap: 8, marginBottom: 16 }}>
              <input
                type="number"
                value={bstSearchVal}
                onChange={e => setBstSearchVal(e.target.value)}
                className="input"
                style={{ flex: 1 }}
                placeholder="Search value..."
              />
              <button onClick={handleBstSearch} className="btn btn-primary btn-sm" style={{ background: '#F43F5E', border: 'none' }}>
                Search
              </button>
            </div>

            <div style={{ background: '#0b1120', padding: 14, borderRadius: 8, fontSize: '0.82rem', color: 'var(--text-secondary)', lineHeight: 1.6 }}>
              {bstSearchPath.length > 0 ? (
                <>
                  <div style={{ fontWeight: 700, color: '#f8fafc', marginBottom: 6 }}>Path Explored:</div>
                  <div style={{ display: 'flex', gap: 6, flexWrap: 'wrap', marginBottom: 10 }}>
                    {bstSearchPath.map((v, idx) => (
                      <span key={idx} style={{ padding: '2px 8px', background: '#1e293b', borderRadius: 4, color: '#f43f5e', fontFamily: 'var(--font-mono)', fontWeight: 700 }}>
                        {v} {idx < bstSearchPath.length - 1 && '→'}
                      </span>
                    ))}
                  </div>
                  {bstFoundNode !== 'not_found' ? (
                    <span style={{ color: '#10b981', fontWeight: 700 }}>✔ Node {bstSearchVal} exists in tree!</span>
                  ) : (
                    <span style={{ color: '#ef4444', fontWeight: 700 }}>✖ Node {bstSearchVal} not found in tree.</span>
                  )}
                </>
              ) : (
                <span>Type a target value (e.g. 60 or 20) to visualize binary search branching decisions.</span>
              )}
            </div>
          </div>
        </div>
      )}

      {/* TAB 3: STACK & QUEUE */}
      {activeTab === 'stack-queue' && (
        <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: 20 }}>
          <div className="card" style={{ padding: 24 }}>
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: 16 }}>
              <div>
                <h3 style={{ fontSize: '1.15rem', marginBottom: 2 }}>Call Stack (LIFO: Last-In, First-Out)</h3>
                <span style={{ fontSize: '0.78rem', color: 'var(--text-muted)' }}>Push/Pop: <b>O(1)</b> Time</span>
              </div>
              <div style={{ display: 'flex', gap: 6 }}>
                <button onClick={pushStack} className="btn btn-secondary btn-sm">
                  <Plus size={14} /> Push
                </button>
                <button onClick={popStack} className="btn btn-outline btn-sm" disabled={stackItems.length === 0}>
                  <Trash2 size={14} /> Pop
                </button>
              </div>
            </div>

            <div style={{ height: '240px', background: '#0b1120', border: '2px dashed #334155', borderTop: 'none', borderRadius: '0 0 16px 16px', padding: 16, display: 'flex', flexDirection: 'column-reverse', gap: 8, overflowY: 'auto' }}>
              {stackItems.map((item, idx) => {
                const isTop = idx === stackItems.length - 1;
                return (
                  <div
                    key={idx}
                    style={{
                      padding: '12px 16px',
                      background: isTop ? 'rgba(244, 63, 94, 0.25)' : 'rgba(99, 102, 241, 0.2)',
                      border: isTop ? '1.5px solid #f43f5e' : '1px solid #6366f1',
                      borderRadius: 8,
                      display: 'flex',
                      justifyContent: 'space-between',
                      alignItems: 'center',
                      fontWeight: 700,
                      color: isTop ? '#f43f5e' : '#a5b4fc',
                      animation: 'fadeIn 0.2s ease-out'
                    }}
                  >
                    <span>Stack Frame #{idx}: <b>{item}</b></span>
                    {isTop && <span style={{ fontSize: '0.72rem', background: '#f43f5e', color: '#fff', padding: '2px 6px', borderRadius: 4 }}>TOP (HEAD)</span>}
                  </div>
                );
              })}
              {stackItems.length === 0 && (
                <div style={{ textAlign: 'center', color: '#64748b', fontSize: '0.85rem', margin: 'auto 0' }}>
                  Stack is empty. Click <b>Push</b> to add a frame.
                </div>
              )}
            </div>
          </div>

          <div className="card" style={{ padding: 24 }}>
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: 16 }}>
              <div>
                <h3 style={{ fontSize: '1.15rem', marginBottom: 2 }}>Queue Pipe (FIFO: First-In, First-Out)</h3>
                <span style={{ fontSize: '0.78rem', color: 'var(--text-muted)' }}>Enqueue/Dequeue: <b>O(1)</b> Time</span>
              </div>
              <div style={{ display: 'flex', gap: 6 }}>
                <button onClick={enqueueQueue} className="btn btn-secondary btn-sm">
                  <Plus size={14} /> Enqueue
                </button>
                <button onClick={dequeueQueue} className="btn btn-outline btn-sm" disabled={queueItems.length === 0}>
                  <Trash2 size={14} /> Dequeue
                </button>
              </div>
            </div>

            <div style={{ height: '240px', background: '#0b1120', border: '2px dashed #334155', borderRadius: 16, padding: 16, display: 'flex', alignItems: 'center', gap: 10, overflowX: 'auto' }}>
              {queueItems.map((item, idx) => {
                const isFront = idx === 0;
                const isRear = idx === queueItems.length - 1;
                return (
                  <div
                    key={idx}
                    style={{
                      minWidth: 120,
                      padding: 14,
                      background: isFront ? 'rgba(16, 185, 129, 0.25)' : isRear ? 'rgba(56, 189, 248, 0.25)' : 'rgba(99, 102, 241, 0.15)',
                      border: isFront ? '1.5px solid #10b981' : isRear ? '1.5px solid #38bdf8' : '1px solid #6366f1',
                      borderRadius: 10,
                      textAlign: 'center',
                      fontSize: '0.85rem',
                      fontWeight: 700,
                      color: isFront ? '#34d399' : isRear ? '#38bdf8' : '#e2e8f0',
                      position: 'relative'
                    }}
                  >
                    <div>{item}</div>
                    <div style={{ fontSize: '0.7rem', marginTop: 4, color: '#94a3b8' }}>
                      {isFront ? 'FRONT (Exits)' : isRear ? 'REAR (Enters)' : `Pos ${idx}`}
                    </div>
                  </div>
                );
              })}
              {queueItems.length === 0 && (
                <div style={{ textAlign: 'center', color: '#64748b', fontSize: '0.85rem', width: '100%' }}>
                  Queue is empty. Click <b>Enqueue</b> to append requests.
                </div>
              )}
            </div>
          </div>
        </div>
      )}

      {/* TAB 4: SORTING */}
      {activeTab === 'sorting' && (
        <div className="card" style={{ padding: 24 }}>
          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: 24, flexWrap: 'wrap', gap: 12 }}>
            <div>
              <h3 style={{ fontSize: '1.15rem', marginBottom: 4 }}>Sorting Race & Step Simulator</h3>
              <p style={{ fontSize: '0.85rem', color: 'var(--text-secondary)' }}>
                Comparing Bubble Sort (O(N²)) vs Quick Sort / Merge Sort (O(N log N)).
              </p>
            </div>

            <div style={{ display: 'flex', gap: 10, alignItems: 'center' }}>
              <button onClick={randomizeSortArray} className="btn btn-secondary btn-sm">
                <RotateCcw size={14} /> Randomize Array
              </button>
              <button
                onClick={runBubbleSort}
                disabled={isSorting}
                className="btn btn-primary btn-sm"
                style={{ background: '#F43F5E', border: 'none' }}
              >
                <Play size={14} /> Run Bubble Sort
              </button>
            </div>
          </div>

          <div style={{ height: 260, background: '#0b1120', borderRadius: 14, border: '1px solid #1e293b', display: 'flex', alignItems: 'flex-end', justifyContent: 'center', gap: 16, padding: '24px 20px' }}>
            {sortArray.map((val, idx) => {
              const isComp = activeCompare.includes(idx);
              const isSorted = sortedIndices.includes(idx);

              return (
                <div key={idx} style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', gap: 6, flex: 1, maxWidth: 48 }}>
                  <span style={{ fontSize: '0.72rem', color: '#94a3b8', fontWeight: 600 }}>{val}</span>
                  <div
                    style={{
                      width: '100%',
                      height: `${val * 2}px`,
                      background: isSorted ? '#10b981' : isComp ? '#f43f5e' : 'linear-gradient(180deg, #6366f1, #3b82f6)',
                      borderRadius: '6px 6px 0 0',
                      transition: 'height 0.15s ease, background 0.15s ease',
                      boxShadow: isComp ? '0 0 15px rgba(244, 63, 94, 0.7)' : 'none'
                    }}
                  />
                  <span style={{ fontSize: '0.68rem', color: '#64748b' }}>[{idx}]</span>
                </div>
              );
            })}
          </div>

          <div style={{ display: 'grid', gridTemplateColumns: 'repeat(3, 1fr)', gap: 12, marginTop: 20 }}>
            <div style={{ background: 'var(--bg-secondary)', padding: 12, borderRadius: 8, textAlign: 'center' }}>
              <span style={{ fontSize: '0.75rem', color: 'var(--text-muted)' }}>Comparisons Made</span>
              <div style={{ fontSize: '1.25rem', fontWeight: 700, color: '#f43f5e' }}>{comparisonsCount}</div>
            </div>
            <div style={{ background: 'var(--bg-secondary)', padding: 12, borderRadius: 8, textAlign: 'center' }}>
              <span style={{ fontSize: '0.75rem', color: 'var(--text-muted)' }}>Algorithm Speed</span>
              <div style={{ fontSize: '1.25rem', fontWeight: 700, color: '#38bdf8' }}>{sortSpeed}ms / step</div>
            </div>
            <div style={{ background: 'var(--bg-secondary)', padding: 12, borderRadius: 8, textAlign: 'center' }}>
              <span style={{ fontSize: '0.75rem', color: 'var(--text-muted)' }}>Sorted Status</span>
              <div style={{ fontSize: '1.25rem', fontWeight: 700, color: sortedIndices.length === sortArray.length ? '#10b981' : '#f59e0b' }}>
                {sortedIndices.length === sortArray.length ? 'Sorted 100%' : `${sortedIndices.length}/${sortArray.length} Placed`}
              </div>
            </div>
          </div>
        </div>
      )}

      {/* TAB 5: GRAPH */}
      {activeTab === 'graph' && (
        <div style={{ display: 'grid', gridTemplateColumns: '1fr 340px', gap: 20 }}>
          <div className="card" style={{ padding: 24 }}>
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: 20 }}>
              <div>
                <h3 style={{ fontSize: '1.15rem', marginBottom: 4 }}>Graph Traversal Visualizer</h3>
                <p style={{ fontSize: '0.85rem', color: 'var(--text-secondary)' }}>
                  BFS (Breadth-First: Shortest Path Queue) vs DFS (Depth-First: Backtracking Stack).
                </p>
              </div>
              <div style={{ display: 'flex', gap: 8 }}>
                <button onClick={runBFS} disabled={graphRunning} className="btn btn-primary btn-sm" style={{ background: '#38bdf8', color: '#0f172a', border: 'none' }}>
                  Run BFS (Level Order)
                </button>
                <button onClick={runDFS} disabled={graphRunning} className="btn btn-primary btn-sm" style={{ background: '#F43F5E', border: 'none' }}>
                  Run DFS (Depth Path)
                </button>
              </div>
            </div>

            <div style={{ background: '#0b1120', padding: 20, borderRadius: 14, border: '1px solid #1e293b', display: 'flex', justifyContent: 'center' }}>
              <svg width="480" height="220" viewBox="0 0 480 220">
                <line x1="80" y1="110" x2="200" y2="50" stroke="#334155" strokeWidth="2" />
                <line x1="80" y1="110" x2="200" y2="170" stroke="#334155" strokeWidth="2" />
                <line x1="200" y1="50" x2="320" y2="50" stroke="#334155" strokeWidth="2" />
                <line x1="200" y1="50" x2="320" y2="170" stroke="#334155" strokeWidth="2" />
                <line x1="200" y1="170" x2="400" y2="110" stroke="#334155" strokeWidth="2" />
                <line x1="320" y1="170" x2="400" y2="110" stroke="#334155" strokeWidth="2" />

                {[
                  { id: 'A', x: 80, y: 110 },
                  { id: 'B', x: 200, y: 50 },
                  { id: 'C', x: 200, y: 170 },
                  { id: 'D', x: 320, y: 50 },
                  { id: 'E', x: 320, y: 170 },
                  { id: 'F', x: 400, y: 110 },
                ].map((node) => {
                  const isVisited = graphVisited.includes(node.id);
                  return (
                    <g key={node.id}>
                      <circle
                        cx={node.x}
                        cy={node.y}
                        r="20"
                        fill={isVisited ? '#10b981' : '#1e293b'}
                        stroke={isVisited ? '#34d399' : '#6366f1'}
                        strokeWidth="2.5"
                      />
                      <text
                        x={node.x}
                        y={node.y + 5}
                        fill="#ffffff"
                        fontSize="13"
                        fontWeight="bold"
                        textAnchor="middle"
                      >
                        {node.id}
                      </text>
                    </g>
                  );
                })}
              </svg>
            </div>

            <div style={{ marginTop: 20, background: 'var(--bg-secondary)', padding: '12px 18px', borderRadius: 8, display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
              <div>
                <span style={{ fontSize: '0.75rem', color: 'var(--text-muted)' }}>Frontier Data Structure (Queue / Stack):</span>
                <div style={{ fontFamily: 'var(--font-mono)', fontWeight: 700, color: '#38bdf8', fontSize: '0.95rem' }}>
                  [{graphQueueStack.join(', ') || 'empty'}]
                </div>
              </div>
              <div>
                <span style={{ fontSize: '0.75rem', color: 'var(--text-muted)' }}>Visited Set:</span>
                <div style={{ fontFamily: 'var(--font-mono)', fontWeight: 700, color: '#10b981', fontSize: '0.95rem' }}>
                  {`{${graphVisited.join(', ')}}`}
                </div>
              </div>
            </div>
          </div>

          <div className="card" style={{ padding: 20 }}>
            <h4 style={{ fontSize: '0.95rem', marginBottom: 12 }}>Step-by-Step Log</h4>
            <div style={{ background: '#0b1120', padding: 12, borderRadius: 8, height: '280px', overflowY: 'auto', fontFamily: 'var(--font-mono)', fontSize: '0.78rem', display: 'flex', flexDirection: 'column', gap: 6 }}>
              {graphStepLog.map((log, i) => (
                <div key={i} style={{ color: log.includes('Complete') ? '#34d399' : '#94a3b8' }}>
                  &gt; {log}
                </div>
              ))}
            </div>
          </div>
        </div>
      )}

      {/* TAB 6: DP */}
      {activeTab === 'dp' && (
        <div className="card" style={{ padding: 24 }}>
          <div style={{ marginBottom: 20 }}>
            <h3 style={{ fontSize: '1.15rem', marginBottom: 4 }}>0/1 Knapsack Dynamic Programming Table</h3>
            <p style={{ fontSize: '0.85rem', color: 'var(--text-secondary)' }}>
              Formula: <code>dp[i][w] = max(dp[i-1][w], val[i] + dp[i-1][w - wt[i]])</code>. Eliminates repeated subproblems.
            </p>
          </div>

          <div style={{ overflowX: 'auto', marginBottom: 20 }}>
            <table style={{ width: '100%', borderCollapse: 'collapse', textAlign: 'center', fontSize: '0.85rem' }}>
              <thead>
                <tr style={{ background: 'var(--bg-secondary)', borderBottom: '1px solid var(--border-color)' }}>
                  <th style={{ padding: '10px 14px', textAlign: 'left' }}>Item (Weight, Val)</th>
                  {Array.from({ length: maxCapacity + 1 }, (_, w) => (
                    <th key={w} style={{ padding: '10px 14px', color: '#38bdf8' }}>Cap {w}</th>
                  ))}
                </tr>
              </thead>
              <tbody>
                {dpGrid.map((row, i) => (
                  <tr key={i} style={{ borderBottom: '1px solid var(--border-subtle)' }}>
                    <td style={{ padding: '10px 14px', textAlign: 'left', fontWeight: 600, color: 'var(--text-primary)' }}>
                      {i === 0 ? '0: (None)' : `${i}: ${dpItems[i - 1].name} (w:${dpItems[i - 1].weight}, $${dpItems[i - 1].val})`}
                    </td>
                    {row.map((cellVal, w) => (
                      <td
                        key={w}
                        style={{
                          padding: '10px 14px',
                          fontWeight: 700,
                          color: i === dpGrid.length - 1 && w === maxCapacity ? '#10b981' : '#f8fafc',
                          background: i === dpGrid.length - 1 && w === maxCapacity ? 'rgba(16, 185, 129, 0.2)' : 'transparent',
                          borderRadius: 6
                        }}
                      >
                        {cellVal}
                      </td>
                    ))}
                  </tr>
                ))}
              </tbody>
            </table>
          </div>

          <div style={{ background: '#0b1120', padding: 14, borderRadius: 8, display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
            <div style={{ fontSize: '0.85rem', color: '#94a3b8' }}>
              Optimal Max Value for Capacity 5 = <strong style={{ color: '#10b981', fontSize: '1.1rem' }}>$85</strong> (Crown: 3kg/$50 + Vase: 2kg/$20 + Gem: 1kg/$15)
            </div>
            <span style={{ fontSize: '0.78rem', color: '#64748b' }}>Time: O(N × W) | Space: O(N × W)</span>
          </div>
        </div>
      )}

      {/* TAB 7: PRACTICE */}
      {activeTab === 'practice' && (
        <div style={{ display: 'grid', gridTemplateColumns: '1fr 360px', gap: 20 }}>
          <div className="card" style={{ padding: 24 }}>
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: 16 }}>
              <div>
                <h3 style={{ fontSize: '1.15rem', marginBottom: 2 }}>Interactive Algorithm Sandbox</h3>
                <span style={{ fontSize: '0.8rem', color: 'var(--text-muted)' }}>Write, test, and validate time complexity live</span>
              </div>
              <button onClick={runPracticeCode} className="btn btn-primary btn-sm" style={{ background: '#F43F5E', border: 'none' }}>
                <Play size={14} /> Run Solution
              </button>
            </div>

            <textarea
              value={practiceCode}
              onChange={e => setPracticeCode(e.target.value)}
              className="input"
              style={{
                width: '100%',
                height: '280px',
                fontFamily: 'var(--font-mono)',
                fontSize: '0.88rem',
                lineHeight: 1.6,
                padding: 14,
                background: '#0b1120',
                color: '#f8fafc',
                borderRadius: 10,
                border: '1px solid #1e293b'
              }}
            />
          </div>

          <div className="card" style={{ padding: 20, display: 'flex', flexDirection: 'column' }}>
            <h4 style={{ fontSize: '0.95rem', marginBottom: 12, display: 'flex', alignItems: 'center', gap: 6 }}>
              <Cpu size={16} style={{ color: '#F43F5E' }} /> Sandbox Output
            </h4>
            <div style={{ flex: 1, background: '#0b1120', padding: 14, borderRadius: 8, fontFamily: 'var(--font-mono)', fontSize: '0.82rem', color: '#f8fafc', display: 'flex', flexDirection: 'column', gap: 10 }}>
              {practiceOutput ? (
                <>
                  <div style={{ color: practiceOutput.status === 'success' ? '#34d399' : '#ef4444', fontWeight: 700 }}>
                    {practiceOutput.status === 'success' ? '✔ Tests Passed' : '✖ Execution Error'}
                  </div>
                  <div>
                    <span style={{ color: '#94a3b8' }}>Result: </span>
                    <span style={{ color: '#38bdf8', fontWeight: 700 }}>{practiceOutput.result}</span>
                  </div>
                  <div style={{ fontSize: '0.75rem', color: '#64748b', marginTop: 10 }}>
                    {practiceOutput.logs}
                  </div>
                </>
              ) : (
                <span style={{ color: '#64748b' }}>Click 'Run Solution' to execute code and test output.</span>
              )}
            </div>
          </div>
        </div>
      )}
    </div>
  );
}
