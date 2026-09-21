import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { Eye, Sliders, RefreshCw, ExternalLink, Sparkles, Layers, Play, CheckCircle2, Globe, Cpu, GitBranch, Smartphone, Server, Binary, ShieldCheck, Lock } from 'lucide-react';

export default function VisualExplainerCard({ visual, domain }) {
  const navigate = useNavigate();
  if (!visual) return null;

  // Linear Regression simulation state
  const [slope, setSlope] = useState(1.8);
  const [intercept, setIntercept] = useState(2.4);

  // CSS Box Model simulation state
  const [paddingSize, setPaddingSize] = useState(20);
  const [borderSize, setBorderSize] = useState(4);
  const [marginSize, setMarginSize] = useState(16);
  const [boxSizing, setBoxSizing] = useState('border-box');

  // Flex vs Grid simulation state
  const [layoutMode, setLayoutMode] = useState('flex'); // 'flex' | 'grid'
  const [flexDirection, setFlexDirection] = useState('row');

  // Event Loop simulation step
  const [eventLoopStep, setEventLoopStep] = useState(0);

  // Determine intelligent lab destination & title strictly by domain first
  const getLabDestination = () => {
    const dom = (domain || '').toLowerCase();
    const type = (visual.diagram_type || '').toLowerCase();
    const title = (visual.title || '').toLowerCase();

    if (dom === 'dsa' || dom.startsWith('dsa-') || dom.includes('dsa')) {
      return { path: '/dsa-lab', label: 'Open DSA Lab', icon: Binary };
    }
    if (dom === 'cybersecurity' || dom.startsWith('cyber') || dom.includes('security')) {
      return { path: '/cyber-lab', label: 'Open Cyber Security Lab', icon: ShieldCheck };
    }
    if (dom === 'web-dev' || dom.startsWith('web-') || dom.includes('html') || dom.includes('css') || dom.includes('react') || dom.includes('javascript') || dom.includes('nodejs')) {
      return { path: '/web-lab', label: 'Open Web Dev Lab', icon: Globe };
    }
    if (dom === 'github' || dom.startsWith('git-') || dom.includes('git')) {
      return { path: '/git-lab', label: 'Open Git & GitHub Lab', icon: GitBranch };
    }
    if (dom === 'app-dev' || dom.startsWith('app-') || dom.includes('flutter') || dom.includes('mobile')) {
      return { path: '/app-lab', label: 'Open Mobile App Lab', icon: Smartphone };
    }
    if (dom === 'system-design' || dom.startsWith('system-') || dom.startsWith('sys-') || dom.includes('system')) {
      return { path: '/system-design-lab', label: 'Open System Design Lab', icon: Server };
    }
    if (dom === 'ai-ml' || dom.startsWith('ai') || dom.startsWith('aiml-') || dom.includes('deep-learning') || dom.includes('math') || dom.includes('python')) {
      if (type.includes('cnn') || type.includes('transformer') || type.includes('neural') || title.includes('deep learning')) {
        return { path: '/deep-learning', label: 'Open Deep Learning Lab', icon: Cpu };
      }
      return { path: '/algorithms', label: 'Open AI & ML Lab', icon: Cpu };
    }

    return { path: '/algorithms', label: 'Open Interactive Lab', icon: Eye };
  };

  const targetLab = getLabDestination();
  const LabIcon = targetLab.icon;

  // Render specific interactive diagram based on diagram_type
  const renderInteractiveDiagram = () => {
    switch (visual.diagram_type) {
      case 'box_model':
        return (
          <div style={{ display: 'flex', flexDirection: 'column', gap: 16 }}>
            {/* Interactive Visual Box Model Renderer */}
            <div style={{ background: '#0b1120', borderRadius: 12, padding: 20, border: '1px solid #1e293b', display: 'flex', justifyContent: 'center', alignItems: 'center' }}>
              <div 
                style={{ 
                  margin: `${marginSize}px`,
                  border: `${borderSize}px solid #3b82f6`,
                  padding: `${paddingSize}px`,
                  background: 'rgba(59, 130, 246, 0.15)',
                  borderRadius: 8,
                  boxSizing: boxSizing,
                  width: '260px',
                  textAlign: 'center',
                  transition: 'all 0.2s ease',
                  boxShadow: '0 8px 30px rgba(0,0,0,0.4)'
                }}
              >
                <div style={{ padding: 12, background: '#1e293b', borderRadius: 6, border: '1px dashed #60a5fa' }}>
                  <div style={{ fontWeight: 700, color: '#60a5fa', fontSize: '0.85rem' }}>Content Box (260px)</div>
                  <div style={{ fontSize: '0.72rem', color: '#94a3b8', marginTop: 4 }}>
                    Padding: {paddingSize}px | Border: {borderSize}px | Margin: {marginSize}px
                  </div>
                </div>
              </div>
            </div>

            {/* Interactive Sliders */}
            <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr 1fr 1fr', gap: 12, background: 'var(--bg-secondary)', padding: 14, borderRadius: 8 }}>
              <div>
                <label style={{ fontSize: '0.75rem', fontWeight: 600, display: 'block', marginBottom: 4 }}>
                  Padding: <b>{paddingSize}px</b>
                </label>
                <input
                  type="range"
                  min="4"
                  max="40"
                  value={paddingSize}
                  onChange={(e) => setPaddingSize(parseInt(e.target.value))}
                  style={{ width: '100%' }}
                />
              </div>

              <div>
                <label style={{ fontSize: '0.75rem', fontWeight: 600, display: 'block', marginBottom: 4 }}>
                  Border: <b>{borderSize}px</b>
                </label>
                <input
                  type="range"
                  min="1"
                  max="12"
                  value={borderSize}
                  onChange={(e) => setBorderSize(parseInt(e.target.value))}
                  style={{ width: '100%' }}
                />
              </div>

              <div>
                <label style={{ fontSize: '0.75rem', fontWeight: 600, display: 'block', marginBottom: 4 }}>
                  Margin: <b>{marginSize}px</b>
                </label>
                <input
                  type="range"
                  min="0"
                  max="30"
                  value={marginSize}
                  onChange={(e) => setMarginSize(parseInt(e.target.value))}
                  style={{ width: '100%' }}
                />
              </div>

              <div>
                <label style={{ fontSize: '0.75rem', fontWeight: 600, display: 'block', marginBottom: 4 }}>
                  Box-Sizing:
                </label>
                <button
                  onClick={() => setBoxSizing(boxSizing === 'border-box' ? 'content-box' : 'border-box')}
                  className="btn btn-secondary btn-sm"
                  style={{ width: '100%', fontSize: '0.75rem' }}
                >
                  {boxSizing}
                </button>
              </div>
            </div>
          </div>
        );

      case 'flex_vs_grid':
        return (
          <div style={{ display: 'flex', flexDirection: 'column', gap: 14 }}>
            <div style={{ display: 'flex', gap: 8, alignItems: 'center' }}>
              <button
                onClick={() => setLayoutMode('flex')}
                className={layoutMode === 'flex' ? 'btn btn-primary btn-sm' : 'btn btn-secondary btn-sm'}
              >
                1D Flexbox Mode
              </button>
              <button
                onClick={() => setLayoutMode('grid')}
                className={layoutMode === 'grid' ? 'btn btn-primary btn-sm' : 'btn btn-secondary btn-sm'}
              >
                2D CSS Grid Mode
              </button>
              {layoutMode === 'flex' && (
                <button
                  onClick={() => setFlexDirection(flexDirection === 'row' ? 'column' : 'row')}
                  className="btn btn-ghost btn-sm"
                  style={{ fontSize: '0.78rem' }}
                >
                  Direction: {flexDirection}
                </button>
              )}
            </div>

            <div 
              style={{ 
                background: '#0b1120', 
                borderRadius: 8, 
                padding: 16, 
                border: '1px solid #1e293b',
                display: layoutMode === 'flex' ? 'flex' : 'grid',
                flexDirection: flexDirection,
                gridTemplateColumns: 'repeat(auto-fit, minmax(80px, 1fr))',
                gap: 10,
                minHeight: '130px'
              }}
            >
              {[1, 2, 3, 4].map(num => (
                <div 
                  key={num} 
                  style={{ 
                    padding: '16px 12px', 
                    background: 'rgba(59, 130, 246, 0.2)', 
                    border: '1px solid #3b82f6', 
                    borderRadius: 6,
                    color: '#60a5fa',
                    fontWeight: 700,
                    textAlign: 'center',
                    fontSize: '0.85rem'
                  }}
                >
                  Item {num}
                </div>
              ))}
            </div>
          </div>
        );

      case 'event_loop':
        const eventSteps = [
          { title: 'Call Stack runs console.log("Start")', stack: ['console.log("Start")'], webApi: [], micro: [], macro: [] },
          { title: 'setTimeout registered with Web API timer', stack: [], webApi: ['Timer (1000ms)'], micro: [], macro: [] },
          { title: 'Promise.resolve() placed in Microtask Queue', stack: [], webApi: ['Timer (1000ms)'], micro: ['Promise.then()'], macro: [] },
          { title: 'Call Stack runs console.log("End")', stack: ['console.log("End")'], webApi: ['Timer (1000ms)'], micro: ['Promise.then()'], macro: [] },
          { title: 'Event loop executes Microtasks (Promise) first!', stack: ['Promise Callback'], webApi: ['Timer (1000ms)'], micro: [], macro: [] },
          { title: 'Timer expires and macrotask runs last', stack: ['setTimeout Callback'], webApi: [], micro: [], macro: [] }
        ];
        const cur = eventSteps[eventLoopStep];

        return (
          <div style={{ display: 'flex', flexDirection: 'column', gap: 12 }}>
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
              <span style={{ fontSize: '0.82rem', fontWeight: 600, color: '#38bdf8' }}>
                Step {eventLoopStep + 1} of {eventSteps.length}: {cur.title}
              </span>
              <button
                onClick={() => setEventLoopStep((prev) => (prev + 1) % eventSteps.length)}
                className="btn btn-primary btn-sm"
                style={{ padding: '4px 12px', fontSize: '0.75rem', gap: 4 }}
              >
                <Play size={12} fill="currentColor" /> Next Event Step
              </button>
            </div>

            <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr 1fr', gap: 10 }}>
              <div style={{ background: '#0b1120', padding: 12, borderRadius: 6, border: '1px solid #1e293b' }}>
                <div style={{ fontSize: '0.7rem', color: '#94a3b8', fontWeight: 700, marginBottom: 6 }}>CALL STACK</div>
                <div style={{ fontSize: '0.78rem', color: '#f8fafc', minHeight: 40, fontFamily: 'var(--font-mono)' }}>
                  {cur.stack.join(', ') || '(empty)'}
                </div>
              </div>

              <div style={{ background: '#0b1120', padding: 12, borderRadius: 6, border: '1px solid #1e293b' }}>
                <div style={{ fontSize: '0.7rem', color: '#a78bfa', fontWeight: 700, marginBottom: 6 }}>MICROTASK QUEUE</div>
                <div style={{ fontSize: '0.78rem', color: '#c084fc', minHeight: 40, fontFamily: 'var(--font-mono)' }}>
                  {cur.micro.join(', ') || '(empty)'}
                </div>
              </div>

              <div style={{ background: '#0b1120', padding: 12, borderRadius: 6, border: '1px solid #1e293b' }}>
                <div style={{ fontSize: '0.7rem', color: '#34d399', fontWeight: 700, marginBottom: 6 }}>WEB APIS / TIMERS</div>
                <div style={{ fontSize: '0.78rem', color: '#6ee7b7', minHeight: 40, fontFamily: 'var(--font-mono)' }}>
                  {cur.webApi.join(', ') || '(empty)'}
                </div>
              </div>
            </div>
          </div>
        );

      case 'linear_regression':
        // Generate scatter points and best-fit line SVG
        const points = [
          { x: 40, y: 190 },
          { x: 80, y: 160 },
          { x: 120, y: 145 },
          { x: 160, y: 110 },
          { x: 200, y: 90 },
          { x: 240, y: 65 },
          { x: 280, y: 40 },
        ];
        const lineY1 = 220 - (slope * 20 + intercept * 15);
        const lineY2 = 220 - (slope * 120 + intercept * 15);

        return (
          <div style={{ display: 'flex', flexDirection: 'column', gap: 16 }}>
            <div style={{ background: 'var(--canvas-bg)', borderRadius: 8, padding: 16, border: '1px solid var(--border-subtle)', display: 'flex', justifyContent: 'center' }}>
              <svg width="340" height="220" viewBox="0 0 340 220">
                <line x1="30" y1="20" x2="30" y2="200" stroke="var(--canvas-grid)" strokeWidth="1" />
                <line x1="30" y1="200" x2="320" y2="200" stroke="var(--canvas-grid)" strokeWidth="1" />
                
                {points.map((pt, i) => {
                  const fitY = 220 - (slope * (pt.x * 0.4) + intercept * 15);
                  return (
                    <line
                      key={`res-${i}`}
                      x1={pt.x}
                      y1={pt.y}
                      x2={pt.x}
                      y2={fitY}
                      stroke="var(--accent-danger)"
                      strokeWidth="1.5"
                      strokeDasharray="2 2"
                    />
                  );
                })}

                <line
                  x1="30"
                  y1={lineY1}
                  x2="310"
                  y2={lineY2}
                  stroke="var(--canvas-line)"
                  strokeWidth="3"
                />

                {points.map((pt, i) => (
                  <circle key={i} cx={pt.x} cy={pt.y} r="5" fill="var(--canvas-point)" stroke="var(--canvas-point-stroke)" strokeWidth="1" />
                ))}

                <text x="35" y="25" fill="var(--canvas-text)" fontSize="10">Target Y (Housing Price)</text>
                <text x="240" y="195" fill="var(--canvas-text)" fontSize="10">Feature X (SqFt)</text>
              </svg>
            </div>

            <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: 16 }}>
              <div>
                <div style={{ display: 'flex', justifyContent: 'space-between', fontSize: '0.8rem', marginBottom: 4 }}>
                  <span>Weight / Slope (w): <b>{slope}</b></span>
                </div>
                <input
                  type="range"
                  min="0.5"
                  max="3.0"
                  step="0.1"
                  value={slope}
                  onChange={(e) => setSlope(parseFloat(e.target.value))}
                  style={{ width: '100%' }}
                />
              </div>

              <div>
                <div style={{ display: 'flex', justifyContent: 'space-between', fontSize: '0.8rem', marginBottom: 4 }}>
                  <span>Bias / Intercept (b): <b>{intercept}</b></span>
                </div>
                <input
                  type="range"
                  min="0.0"
                  max="5.0"
                  step="0.2"
                  value={intercept}
                  onChange={(e) => setIntercept(parseFloat(e.target.value))}
                  style={{ width: '100%' }}
                />
              </div>
            </div>
          </div>
        );

      case 'neural_net':
        return (
          <div style={{ background: 'var(--canvas-bg)', borderRadius: 8, padding: 16, border: '1px solid var(--border-subtle)', display: 'flex', justifyContent: 'center' }}>
            <svg width="360" height="200" viewBox="0 0 360 200">
              {[40, 100, 160].map((y1, i) =>
                [30, 75, 125, 170].map((y2, j) => (
                  <line key={`c1-${i}-${j}`} x1="60" y1={y1} x2="180" y2={y2} stroke="rgba(99, 102, 241, 0.25)" strokeWidth="1.5" />
                ))
              )}
              {[30, 75, 125, 170].map((y1, i) =>
                [65, 135].map((y2, j) => (
                  <line key={`c2-${i}-${j}`} x1="180" y1={y1} x2="300" y2={y2} stroke="rgba(56, 189, 248, 0.3)" strokeWidth="1.5" />
                ))
              )}

              {[40, 100, 160].map((y, i) => (
                <g key={`l1-${i}`}>
                  <circle cx="60" cy={y} r="14" fill="var(--bg-tertiary)" stroke="var(--accent-primary)" strokeWidth="2" />
                  <text x="60" y={y + 4} fill="var(--text-primary)" fontSize="10" textAnchor="middle" fontWeight="bold">x{i+1}</text>
                </g>
              ))}

              {[30, 75, 125, 170].map((y, i) => (
                <g key={`l2-${i}`}>
                  <circle cx="180" cy={y} r="14" fill="var(--bg-tertiary)" stroke="var(--accent-purple)" strokeWidth="2" />
                  <text x="180" y={y + 4} fill="var(--accent-purple)" fontSize="10" textAnchor="middle" fontWeight="bold">h{i+1}</text>
                </g>
              ))}

              {[65, 135].map((y, i) => (
                <g key={`l3-${i}`}>
                  <circle cx="300" cy={y} r="15" fill="var(--bg-tertiary)" stroke="var(--accent-secondary)" strokeWidth="2" />
                  <text x="300" y={y + 4} fill="var(--accent-secondary)" fontSize="10" textAnchor="middle" fontWeight="bold">y{i+1}</text>
                </g>
              ))}

              <text x="60" y="195" fill="var(--canvas-subtext)" fontSize="10" textAnchor="middle">Input (3)</text>
              <text x="180" y="195" fill="var(--canvas-subtext)" fontSize="10" textAnchor="middle">Dense Layer (4 ReLU)</text>
              <text x="300" y="195" fill="var(--canvas-subtext)" fontSize="10" textAnchor="middle">Output (2 Softmax)</text>
            </svg>
          </div>
        );

      case 'attention_matrix':
        return (
          <div style={{ background: 'var(--canvas-bg)', borderRadius: 8, padding: 16, border: '1px solid var(--border-subtle)', display: 'flex', flexDirection: 'column', alignItems: 'center' }}>
            <div style={{ fontSize: '0.8rem', color: 'var(--text-muted)', marginBottom: 12 }}>
              Attention Weights Heatmap: <b>Softmax(QKᵀ / √dₖ)</b>
            </div>
            <div style={{ display: 'grid', gridTemplateColumns: 'auto repeat(3, 70px)', gap: 4, alignItems: 'center' }}>
              <div />
              <div style={{ textAlign: 'center', fontSize: '0.75rem', fontWeight: 600, color: 'var(--accent-secondary)' }}>"The"</div>
              <div style={{ textAlign: 'center', fontSize: '0.75rem', fontWeight: 600, color: 'var(--accent-secondary)' }}>"animal"</div>
              <div style={{ textAlign: 'center', fontSize: '0.75rem', fontWeight: 600, color: 'var(--accent-secondary)' }}>"tired"</div>

              <div style={{ fontSize: '0.75rem', fontWeight: 600, color: 'var(--accent-purple)', paddingRight: 6 }}>"The"</div>
              <div style={{ background: 'rgba(99, 102, 241, 0.2)', padding: 12, textAlign: 'center', borderRadius: 4, fontSize: '0.8rem', color: 'var(--text-primary)' }}>0.25</div>
              <div style={{ background: 'rgba(99, 102, 241, 0.4)', padding: 12, textAlign: 'center', borderRadius: 4, fontSize: '0.8rem', color: 'var(--text-primary)' }}>0.55</div>
              <div style={{ background: 'rgba(99, 102, 241, 0.15)', padding: 12, textAlign: 'center', borderRadius: 4, fontSize: '0.8rem', color: 'var(--text-primary)' }}>0.20</div>

              <div style={{ fontSize: '0.75rem', fontWeight: 600, color: 'var(--accent-purple)', paddingRight: 6 }}>"it"</div>
              <div style={{ background: 'rgba(99, 102, 241, 0.1)', padding: 12, textAlign: 'center', borderRadius: 4, fontSize: '0.8rem', color: 'var(--text-primary)' }}>0.08</div>
              <div style={{ background: 'var(--accent-primary)', padding: 12, textAlign: 'center', borderRadius: 4, fontSize: '0.8rem', fontWeight: 'bold', color: '#ffffff' }}>0.78</div>
              <div style={{ background: 'rgba(99, 102, 241, 0.15)', padding: 12, textAlign: 'center', borderRadius: 4, fontSize: '0.8rem', color: 'var(--text-primary)' }}>0.14</div>

              <div style={{ fontSize: '0.75rem', fontWeight: 600, color: 'var(--accent-purple)', paddingRight: 6 }}>"tired"</div>
              <div style={{ background: 'rgba(99, 102, 241, 0.1)', padding: 12, textAlign: 'center', borderRadius: 4, fontSize: '0.8rem', color: 'var(--text-primary)' }}>0.10</div>
              <div style={{ background: 'rgba(99, 102, 241, 0.3)', padding: 12, textAlign: 'center', borderRadius: 4, fontSize: '0.8rem', color: 'var(--text-primary)' }}>0.40</div>
              <div style={{ background: 'rgba(99, 102, 241, 0.45)', padding: 12, textAlign: 'center', borderRadius: 4, fontSize: '0.8rem', color: 'var(--text-primary)' }}>0.50</div>
            </div>
            <p style={{ fontSize: '0.75rem', color: 'var(--text-muted)', marginTop: 12 }}>
              Notice how <b>"it"</b> attends predominantly (0.78 weight) to <b>"animal"</b> across the sequence.
            </p>
          </div>
        );

      case 'two_pointers_array':
        return (
          <div style={{ background: '#0b1120', padding: 18, borderRadius: 10, border: '1px solid #1e293b' }}>
            <div style={{ fontSize: '0.8rem', color: '#94a3b8', marginBottom: 12 }}>Two Pointers Array Search: <b>L (Left)</b> & <b>R (Right)</b> Inward Convergence</div>
            <div style={{ display: 'flex', justifyContent: 'center', gap: 10 }}>
              {[2, 7, 11, 15, 22].map((num, i) => (
                <div key={i} style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', gap: 6 }}>
                  <span style={{ fontSize: '0.7rem', fontWeight: 700, color: i === 0 ? '#38bdf8' : i === 4 ? '#f43f5e' : 'transparent' }}>
                    {i === 0 ? 'LEFT' : i === 4 ? 'RIGHT' : '-'}
                  </span>
                  <div style={{ width: 44, height: 44, borderRadius: 8, background: i === 0 ? 'rgba(56, 189, 248, 0.2)' : i === 4 ? 'rgba(244, 63, 94, 0.2)' : '#1e293b', border: i === 0 ? '2px solid #38bdf8' : i === 4 ? '2px solid #f43f5e' : '1px solid #334155', display: 'flex', alignItems: 'center', justifyContent: 'center', color: '#fff', fontWeight: 700 }}>
                    {num}
                  </div>
                  <span style={{ fontSize: '0.68rem', color: '#64748b' }}>[{i}]</span>
                </div>
              ))}
            </div>
            <div style={{ marginTop: 12, textAlign: 'center', fontSize: '0.78rem', color: '#34d399' }}>
              arr[0] (2) + arr[4] (22) = 24. If target is 18, decrement Right pointer to reduce sum!
            </div>
          </div>
        );

      case 'bst_tree_traversal':
        return (
          <div style={{ background: '#0b1120', padding: 16, borderRadius: 10, border: '1px solid #1e293b', textAlign: 'center' }}>
            <div style={{ fontSize: '0.8rem', color: '#94a3b8', marginBottom: 10 }}>Binary Search Tree Property: <code>Left &lt; Root &lt; Right</code></div>
            <svg width="280" height="120" viewBox="0 0 280 120" style={{ margin: '0 auto' }}>
              <line x1="140" y1="20" x2="80" y2="60" stroke="#334155" strokeWidth="2" />
              <line x1="140" y1="20" x2="200" y2="60" stroke="#334155" strokeWidth="2" />
              <circle cx="140" cy="20" r="16" fill="#1e293b" stroke="#f43f5e" strokeWidth="2" />
              <text x="140" y="24" fill="#fff" fontSize="11" fontWeight="bold" textAnchor="middle">50</text>

              <circle cx="80" cy="60" r="14" fill="#1e293b" stroke="#38bdf8" strokeWidth="2" />
              <text x="80" y="64" fill="#fff" fontSize="10" fontWeight="bold" textAnchor="middle">30</text>

              <circle cx="200" cy="60" r="14" fill="#1e293b" stroke="#10b981" strokeWidth="2" />
              <text x="200" y="64" fill="#fff" fontSize="10" fontWeight="bold" textAnchor="middle">70</text>
            </svg>
            <div style={{ fontSize: '0.75rem', color: '#a5b4fc', marginTop: 4 }}>Inorder Traversal: 30 → 50 → 70 (Always naturally sorted)</div>
          </div>
        );

      case 'rsa_crypto_flow':
        return (
          <div style={{ background: '#0b1120', padding: 16, borderRadius: 10, border: '1px solid #1e293b' }}>
            <div style={{ fontSize: '0.8rem', color: '#94a3b8', marginBottom: 10 }}>Asymmetric Cryptography: Public Key Encrypts, Private Key Decrypts</div>
            <div style={{ display: 'grid', gridTemplateColumns: '1fr auto 1fr auto 1fr', alignItems: 'center', gap: 8, textAlign: 'center' }}>
              <div style={{ background: '#1e293b', padding: 8, borderRadius: 6, fontSize: '0.75rem', color: '#f8fafc' }}>Plaintext "Hello"</div>
              <span style={{ color: '#14b8a6' }}>🔒 + (Pub Key) →</span>
              <div style={{ background: 'rgba(20, 184, 166, 0.2)', border: '1px dashed #14b8a6', padding: 8, borderRadius: 6, fontSize: '0.72rem', color: '#2dd4bf', fontFamily: 'var(--font-mono)' }}>0x8a92f...</div>
              <span style={{ color: '#f43f5e' }}>🔑 + (Priv Key) →</span>
              <div style={{ background: '#1e293b', padding: 8, borderRadius: 6, fontSize: '0.75rem', color: '#34d399' }}>Decrypted "Hello"</div>
            </div>
          </div>
        );

      case 'sql_injection_defense':
        return (
          <div style={{ background: '#0b1120', padding: 16, borderRadius: 10, border: '1px solid #1e293b' }}>
            <div style={{ fontSize: '0.8rem', color: '#94a3b8', marginBottom: 10 }}>SQL Injection Defense: Prepared Statements vs Vulnerable Concatenation</div>
            <div style={{ display: 'flex', flexDirection: 'column', gap: 8 }}>
              <div style={{ background: 'rgba(244, 63, 94, 0.15)', border: '1px solid #f43f5e', padding: 8, borderRadius: 6, fontSize: '0.75rem', color: '#fca5a5', fontFamily: 'var(--font-mono)' }}>
                ✖ Vulnerable: "SELECT * FROM users WHERE user = '" + input + "'"
              </div>
              <div style={{ background: 'rgba(16, 185, 129, 0.15)', border: '1px solid #10b981', padding: 8, borderRadius: 6, fontSize: '0.75rem', color: '#86efac', fontFamily: 'var(--font-mono)' }}>
                ✔ Defended: "SELECT * FROM users WHERE user = ?" [Bind param: input]
              </div>
            </div>
          </div>
        );

      case 'html_aria_landmarks':
      case 'dom_tree_accessibility':
        return (
          <div style={{ background: '#0b1120', padding: 18, borderRadius: 10, border: '1px solid #1e293b' }}>
            <div style={{ fontSize: '0.8rem', color: '#94a3b8', marginBottom: 12 }}>Semantic HTML5 Landmarks &amp; Accessibility (AOM) Hierarchy</div>
            <div style={{ display: 'flex', flexDirection: 'column', gap: 8, maxWidth: '520px', margin: '0 auto' }}>
              <div style={{ padding: '8px 14px', background: 'rgba(56, 189, 248, 0.15)', border: '1px solid #38bdf8', borderRadius: 6, display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                <span style={{ fontFamily: 'var(--font-mono)', color: '#38bdf8', fontSize: '0.82rem', fontWeight: 700 }}>&lt;header role="banner"&gt;</span>
                <span style={{ fontSize: '0.72rem', color: '#94a3b8' }}>Global Branding &amp; Top Nav</span>
              </div>
              <div style={{ padding: '8px 14px', background: 'rgba(168, 85, 247, 0.15)', border: '1px solid #a855f7', borderRadius: 6, display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginLeft: 16 }}>
                <span style={{ fontFamily: 'var(--font-mono)', color: '#c084fc', fontSize: '0.82rem', fontWeight: 700 }}>&lt;nav aria-label="Main Navigation"&gt;</span>
                <span style={{ fontSize: '0.72rem', color: '#94a3b8' }}>Accessible Link List</span>
              </div>
              <div style={{ padding: '12px 14px', background: 'rgba(16, 185, 129, 0.15)', border: '1px solid #10b981', borderRadius: 6, display: 'flex', flexDirection: 'column', gap: 6 }}>
                <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                  <span style={{ fontFamily: 'var(--font-mono)', color: '#34d399', fontSize: '0.82rem', fontWeight: 700 }}>&lt;main id="content" role="main"&gt;</span>
                  <span style={{ fontSize: '0.72rem', color: '#6ee7b7' }}>Primary Unique Document Body</span>
                </div>
                <div style={{ padding: '6px 12px', background: 'rgba(16, 185, 129, 0.2)', border: '1px dashed #10b981', borderRadius: 4, marginLeft: 16, display: 'flex', justifyContent: 'space-between' }}>
                  <span style={{ fontFamily: 'var(--font-mono)', color: '#a7f3d0', fontSize: '0.78rem' }}>&lt;article aria-labelledby="post-title"&gt;</span>
                  <span style={{ fontSize: '0.7rem', color: '#cbd5e1' }}>Self-contained Article</span>
                </div>
              </div>
              <div style={{ padding: '8px 14px', background: 'rgba(245, 158, 11, 0.15)', border: '1px solid #f59e0b', borderRadius: 6, display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                <span style={{ fontFamily: 'var(--font-mono)', color: '#fbbf24', fontSize: '0.82rem', fontWeight: 700 }}>&lt;footer role="contentinfo"&gt;</span>
                <span style={{ fontSize: '0.72rem', color: '#94a3b8' }}>Copyright, Legal &amp; Secondary Links</span>
              </div>
            </div>
            <div style={{ marginTop: 12, textAlign: 'center', fontSize: '0.75rem', color: '#38bdf8' }}>
              Screen readers allow blind users to jump directly between these landmark zones via rotor key commands!
            </div>
          </div>
        );

      case 'git_three_trees':
        return (
          <div style={{ background: '#0b1120', padding: 18, borderRadius: 10, border: '1px solid #1e293b' }}>
            <div style={{ fontSize: '0.8rem', color: '#94a3b8', marginBottom: 12 }}>The 3 Git States / Trees Workflow</div>
            <div style={{ display: 'grid', gridTemplateColumns: '1fr auto 1fr auto 1fr', gap: 8, alignItems: 'center', textAlign: 'center' }}>
              <div style={{ background: '#1e293b', border: '1px solid #475569', padding: 12, borderRadius: 8 }}>
                <div style={{ fontWeight: 700, color: '#f43f5e', fontSize: '0.8rem' }}>Working Directory</div>
                <div style={{ fontSize: '0.7rem', color: '#94a3b8', marginTop: 4 }}>Untracked / Modified</div>
              </div>
              <span style={{ color: '#f59e0b', fontWeight: 700, fontSize: '0.75rem' }}>git add →</span>
              <div style={{ background: 'rgba(245, 158, 11, 0.15)', border: '1px solid #f59e0b', padding: 12, borderRadius: 8 }}>
                <div style={{ fontWeight: 700, color: '#fbbf24', fontSize: '0.8rem' }}>Staging Index</div>
                <div style={{ fontSize: '0.7rem', color: '#fde68a', marginTop: 4 }}>Prepared Snapshot</div>
              </div>
              <span style={{ color: '#10b981', fontWeight: 700, fontSize: '0.75rem' }}>git commit →</span>
              <div style={{ background: 'rgba(16, 185, 129, 0.15)', border: '1px solid #10b981', padding: 12, borderRadius: 8 }}>
                <div style={{ fontWeight: 700, color: '#34d399', fontSize: '0.8rem' }}>Git Repository (HEAD)</div>
                <div style={{ fontSize: '0.7rem', color: '#a7f3d0', marginTop: 4 }}>Immutable Commit SHA</div>
              </div>
            </div>
          </div>
        );

      case 'flutter_widget_tree':
        return (
          <div style={{ background: '#0b1120', padding: 18, borderRadius: 10, border: '1px solid #1e293b' }}>
            <div style={{ fontSize: '0.8rem', color: '#94a3b8', marginBottom: 12 }}>Flutter Reactive Three-Tree Hierarchy</div>
            <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr 1fr', gap: 10, textAlign: 'center' }}>
              <div style={{ background: 'rgba(59, 130, 246, 0.15)', border: '1px solid #3b82f6', padding: 12, borderRadius: 8 }}>
                <div style={{ fontWeight: 700, color: '#60a5fa', fontSize: '0.8rem' }}>Widget Tree</div>
                <div style={{ fontSize: '0.7rem', color: '#93c5fd', marginTop: 4 }}>Immutable Configurations (Container, Text)</div>
              </div>
              <div style={{ background: 'rgba(168, 85, 247, 0.15)', border: '1px solid #a855f7', padding: 12, borderRadius: 8 }}>
                <div style={{ fontWeight: 700, color: '#c084fc', fontSize: '0.8rem' }}>Element Tree</div>
                <div style={{ fontSize: '0.7rem', color: '#e9d5ff', marginTop: 4 }}>Persistent State &amp; Lifecycle Bridge</div>
              </div>
              <div style={{ background: 'rgba(16, 185, 129, 0.15)', border: '1px solid #10b981', padding: 12, borderRadius: 8 }}>
                <div style={{ fontWeight: 700, color: '#34d399', fontSize: '0.8rem' }}>RenderObject Tree</div>
                <div style={{ fontSize: '0.7rem', color: '#a7f3d0', marginTop: 4 }}>Sizing, Layout &amp; GPU Painting</div>
              </div>
            </div>
          </div>
        );

      case 'consistent_hashing_ring':
        return (
          <div style={{ background: '#0b1120', padding: 18, borderRadius: 10, border: '1px solid #1e293b', textAlign: 'center' }}>
            <div style={{ fontSize: '0.8rem', color: '#94a3b8', marginBottom: 10 }}>Distributed Consistent Hashing Ring (0 to 2³²-1)</div>
            <div style={{ display: 'flex', justifyContent: 'center', gap: 16, alignItems: 'center' }}>
              <div style={{ padding: 10, background: '#1e293b', border: '2px solid #38bdf8', borderRadius: 8, color: '#38bdf8', fontWeight: 700, fontSize: '0.75rem' }}>Node A (Tokens: 0, 1000)</div>
              <span style={{ color: '#94a3b8' }}>↻</span>
              <div style={{ padding: 10, background: '#1e293b', border: '2px solid #a855f7', borderRadius: 8, color: '#c084fc', fontWeight: 700, fontSize: '0.75rem' }}>Node B (Tokens: 2000, 3000)</div>
              <span style={{ color: '#94a3b8' }}>↻</span>
              <div style={{ padding: 10, background: '#1e293b', border: '2px solid #10b981', borderRadius: 8, color: '#34d399', fontWeight: 700, fontSize: '0.75rem' }}>Node C (Tokens: 4000, 5000)</div>
            </div>
            <div style={{ fontSize: '0.72rem', color: '#64748b', marginTop: 8 }}>Keys hash to coordinates and walk clockwise to the nearest node, minimizing cache invalidation when nodes join or fail.</div>
          </div>
        );

      case 'jwt_signature_verify':
        return (
          <div style={{ background: '#0b1120', padding: 16, borderRadius: 10, border: '1px solid #1e293b' }}>
            <div style={{ fontSize: '0.8rem', color: '#94a3b8', marginBottom: 10 }}>JSON Web Token (JWT) Cryptographic Anatomy</div>
            <div style={{ display: 'flex', gap: 6, fontFamily: 'var(--font-mono)', fontSize: '0.75rem', justifyContent: 'center', flexWrap: 'wrap' }}>
              <span style={{ background: 'rgba(244, 63, 94, 0.2)', color: '#f43f5e', padding: '4px 8px', borderRadius: 4, border: '1px solid #f43f5e' }}>eyJhbGciOiJIUzI1NiJ9 (Header)</span>
              <span style={{ color: '#fff' }}>.</span>
              <span style={{ background: 'rgba(168, 85, 247, 0.2)', color: '#c084fc', padding: '4px 8px', borderRadius: 4, border: '1px solid #a855f7' }}>eyJzdWIiOiIxMjM0NTY3ODkwIn0 (Payload)</span>
              <span style={{ color: '#fff' }}>.</span>
              <span style={{ background: 'rgba(16, 185, 129, 0.2)', color: '#34d399', padding: '4px 8px', borderRadius: 4, border: '1px solid #10b981' }}>SflKxwRJSMeKKF2QT4f... (Signature)</span>
            </div>
          </div>
        );
    }
  };

  return (
    <div className="card" style={{ marginBottom: 24, borderLeft: '4px solid var(--accent-secondary)' }}>
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: 14 }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
          <Eye size={18} style={{ color: 'var(--accent-secondary)' }} />
          <div>
            <h3 style={{ fontSize: '1rem', color: 'var(--text-primary)' }}>{visual.title}</h3>
            {visual.subtitle && <p style={{ fontSize: '0.8rem', color: 'var(--text-muted)' }}>{visual.subtitle}</p>}
          </div>
        </div>

        <button
          onClick={() => navigate(targetLab.path)}
          className="btn btn-ghost btn-sm"
          style={{ gap: 6, color: 'var(--accent-primary)', fontSize: '0.78rem', fontWeight: 600 }}
        >
          <LabIcon size={14} />
          <span>{targetLab.label}</span>
          <ExternalLink size={12} />
        </button>
      </div>

      {renderInteractiveDiagram()}
    </div>
  );
}
