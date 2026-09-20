import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { Eye, Sliders, RefreshCw, ExternalLink, Sparkles, Layers, Play, CheckCircle2, Globe, Cpu, GitBranch, Smartphone, Server } from 'lucide-react';

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

  // Determine intelligent lab destination & title
  const getLabDestination = () => {
    const type = (visual.diagram_type || '').toLowerCase();
    const title = (visual.title || '').toLowerCase();
    const dom = (domain || '').toLowerCase();

    if (dom === 'web-dev' || type.includes('box_model') || type.includes('html') || type.includes('flex') || type.includes('grid') || type.includes('event_loop') || type.includes('vdom') || type.includes('middleware') || type.includes('jwt') || type.includes('hydration') || title.includes('web') || title.includes('css') || title.includes('html') || title.includes('react') || title.includes('dom') || title.includes('next.js')) {
      return { path: '/web-lab', label: 'Open Web Dev Lab', icon: Globe };
    }
    if (dom === 'github' || type.includes('git') || type.includes('commit') || type.includes('dag') || title.includes('git') || title.includes('github') || title.includes('rebase')) {
      return { path: '/git-lab', label: 'Open Git & GitHub Lab', icon: GitBranch };
    }
    if (dom === 'app-dev' || type.includes('mobile') || type.includes('viewport') || type.includes('safe_area') || title.includes('mobile') || title.includes('flutter') || title.includes('react native')) {
      return { path: '/app-lab', label: 'Open Mobile App Lab', icon: Smartphone };
    }
    if (dom === 'system-design' || type.includes('microservice') || type.includes('caching') || type.includes('sharding') || type.includes('system') || title.includes('system design') || title.includes('load balancer') || title.includes('redis')) {
      return { path: '/system-design-lab', label: 'Open System Design Lab', icon: Server };
    }
    if (type.includes('cnn') || type.includes('transformer') || type.includes('backprop') || type.includes('activation') || type.includes('neural') || title.includes('deep learning') || title.includes('neural')) {
      return { path: '/deep-learning', label: 'Open Deep Learning Lab', icon: Cpu };
    }
    return { path: '/algorithms', label: 'Open Machine Learning Lab', icon: Eye };
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

      default:
        return (
          <div style={{ background: 'var(--canvas-bg)', borderRadius: 8, padding: 24, border: '1px solid var(--border-subtle)', textAlign: 'center' }}>
            <Eye size={32} style={{ color: 'var(--accent-primary)', marginBottom: 8 }} />
            <p style={{ fontSize: '0.85rem', color: 'var(--text-secondary)' }}>
              Interactive Visual Simulation: <b>{visual.title}</b>
            </p>
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
