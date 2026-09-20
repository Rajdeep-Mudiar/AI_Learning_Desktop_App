import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { Eye, Sliders, RefreshCw, ExternalLink, Sparkles } from 'lucide-react';

export default function VisualExplainerCard({ visual }) {
  const navigate = useNavigate();
  if (!visual) return null;

  // Interactive controls for Linear Regression simulation
  const [slope, setSlope] = useState(1.8);
  const [intercept, setIntercept] = useState(2.4);

  // Render specific interactive diagram based on diagram_type
  const renderInteractiveDiagram = () => {
    switch (visual.diagram_type) {
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
            <div style={{ background: '#070a13', borderRadius: 8, padding: 16, border: '1px solid var(--border-subtle)', display: 'flex', justifyContent: 'center' }}>
              <svg width="340" height="220" viewBox="0 0 340 220">
                {/* Grid Lines */}
                <line x1="30" y1="20" x2="30" y2="200" stroke="#1e293b" strokeWidth="1" />
                <line x1="30" y1="200" x2="320" y2="200" stroke="#1e293b" strokeWidth="1" />
                
                {/* Residual Lines */}
                {points.map((pt, i) => {
                  const fitY = 220 - (slope * (pt.x * 0.4) + intercept * 15);
                  return (
                    <line
                      key={`res-${i}`}
                      x1={pt.x}
                      y1={pt.y}
                      x2={pt.x}
                      y2={fitY}
                      stroke="#ef4444"
                      strokeWidth="1.5"
                      strokeDasharray="2 2"
                    />
                  );
                })}

                {/* Regression Line */}
                <line
                  x1="30"
                  y1={lineY1}
                  x2="310"
                  y2={lineY2}
                  stroke="#6366f1"
                  strokeWidth="3"
                />

                {/* Data Points */}
                {points.map((pt, i) => (
                  <circle key={i} cx={pt.x} cy={pt.y} r="5" fill="#38bdf8" />
                ))}

                {/* Labels */}
                <text x="35" y="25" fill="#64748b" fontSize="10">Target Y (Housing Price)</text>
                <text x="240" y="195" fill="#64748b" fontSize="10">Feature X (SqFt)</text>
              </svg>
            </div>

            {/* Interactive Sliders */}
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
          <div style={{ background: '#070a13', borderRadius: 8, padding: 16, border: '1px solid var(--border-subtle)', display: 'flex', justifyContent: 'center' }}>
            <svg width="360" height="200" viewBox="0 0 360 200">
              {/* Connections Layer 1 -> Layer 2 */}
              {[40, 100, 160].map((y1, i) =>
                [30, 75, 125, 170].map((y2, j) => (
                  <line key={`c1-${i}-${j}`} x1="60" y1={y1} x2="180" y2={y2} stroke="rgba(99, 102, 241, 0.25)" strokeWidth="1.5" />
                ))
              )}
              {/* Connections Layer 2 -> Output */}
              {[30, 75, 125, 170].map((y1, i) =>
                [65, 135].map((y2, j) => (
                  <line key={`c2-${i}-${j}`} x1="180" y1={y1} x2="300" y2={y2} stroke="rgba(56, 189, 248, 0.3)" strokeWidth="1.5" />
                ))
              )}

              {/* Layer 1 Nodes (Inputs) */}
              {[40, 100, 160].map((y, i) => (
                <g key={`l1-${i}`}>
                  <circle cx="60" cy={y} r="14" fill="#1e293b" stroke="#6366f1" strokeWidth="2" />
                  <text x="60" y={y + 4} fill="#f8fafc" fontSize="10" textAnchor="middle" fontWeight="bold">x{i+1}</text>
                </g>
              ))}

              {/* Layer 2 Nodes (Hidden ReLU) */}
              {[30, 75, 125, 170].map((y, i) => (
                <g key={`l2-${i}`}>
                  <circle cx="180" cy={y} r="14" fill="#1e1b4b" stroke="#8b5cf6" strokeWidth="2" />
                  <text x="180" y={y + 4} fill="#c084fc" fontSize="10" textAnchor="middle" fontWeight="bold">h{i+1}</text>
                </g>
              ))}

              {/* Layer 3 Nodes (Output Softmax) */}
              {[65, 135].map((y, i) => (
                <g key={`l3-${i}`}>
                  <circle cx="300" cy={y} r="15" fill="#082f49" stroke="#38bdf8" strokeWidth="2" />
                  <text x="300" y={y + 4} fill="#7dd3fc" fontSize="10" textAnchor="middle" fontWeight="bold">y{i+1}</text>
                </g>
              ))}

              <text x="60" y="195" fill="#64748b" fontSize="10" textAnchor="middle">Input (3)</text>
              <text x="180" y="195" fill="#64748b" fontSize="10" textAnchor="middle">Dense Layer (4 ReLU)</text>
              <text x="300" y="195" fill="#64748b" fontSize="10" textAnchor="middle">Output (2 Softmax)</text>
            </svg>
          </div>
        );

      case 'attention_matrix':
        return (
          <div style={{ background: '#070a13', borderRadius: 8, padding: 16, border: '1px solid var(--border-subtle)', display: 'flex', flexDirection: 'column', alignItems: 'center' }}>
            <div style={{ fontSize: '0.8rem', color: 'var(--text-muted)', marginBottom: 12 }}>
              Attention Weights Heatmap: <b>Softmax(QKᵀ / √dₖ)</b>
            </div>
            <div style={{ display: 'grid', gridTemplateColumns: 'auto repeat(3, 70px)', gap: 4, alignItems: 'center' }}>
              <div />
              <div style={{ textAlign: 'center', fontSize: '0.75rem', fontWeight: 600, color: '#38bdf8' }}>"The"</div>
              <div style={{ textAlign: 'center', fontSize: '0.75rem', fontWeight: 600, color: '#38bdf8' }}>"animal"</div>
              <div style={{ textAlign: 'center', fontSize: '0.75rem', fontWeight: 600, color: '#38bdf8' }}>"tired"</div>

              <div style={{ fontSize: '0.75rem', fontWeight: 600, color: '#a855f7', paddingRight: 6 }}>"The"</div>
              <div style={{ background: 'rgba(99, 102, 241, 0.4)', padding: 12, textAlign: 'center', borderRadius: 4, fontSize: '0.8rem' }}>0.25</div>
              <div style={{ background: 'rgba(99, 102, 241, 0.5)', padding: 12, textAlign: 'center', borderRadius: 4, fontSize: '0.8rem' }}>0.55</div>
              <div style={{ background: 'rgba(99, 102, 241, 0.2)', padding: 12, textAlign: 'center', borderRadius: 4, fontSize: '0.8rem' }}>0.20</div>

              <div style={{ fontSize: '0.75rem', fontWeight: 600, color: '#a855f7', paddingRight: 6 }}>"it"</div>
              <div style={{ background: 'rgba(99, 102, 241, 0.1)', padding: 12, textAlign: 'center', borderRadius: 4, fontSize: '0.8rem' }}>0.08</div>
              <div style={{ background: 'rgba(99, 102, 241, 0.9)', padding: 12, textAlign: 'center', borderRadius: 4, fontSize: '0.8rem', fontWeight: 'bold', color: '#ffffff' }}>0.78</div>
              <div style={{ background: 'rgba(99, 102, 241, 0.15)', padding: 12, textAlign: 'center', borderRadius: 4, fontSize: '0.8rem' }}>0.14</div>

              <div style={{ fontSize: '0.75rem', fontWeight: 600, color: '#a855f7', paddingRight: 6 }}>"tired"</div>
              <div style={{ background: 'rgba(99, 102, 241, 0.1)', padding: 12, textAlign: 'center', borderRadius: 4, fontSize: '0.8rem' }}>0.10</div>
              <div style={{ background: 'rgba(99, 102, 241, 0.4)', padding: 12, textAlign: 'center', borderRadius: 4, fontSize: '0.8rem' }}>0.40</div>
              <div style={{ background: 'rgba(99, 102, 241, 0.6)', padding: 12, textAlign: 'center', borderRadius: 4, fontSize: '0.8rem' }}>0.50</div>
            </div>
            <p style={{ fontSize: '0.75rem', color: 'var(--text-muted)', marginTop: 12 }}>
              Notice how <b>"it"</b> attends predominantly (0.78 weight) to <b>"animal"</b> across the sequence.
            </p>
          </div>
        );

      default:
        return (
          <div style={{ background: '#070a13', borderRadius: 8, padding: 24, border: '1px solid var(--border-subtle)', textAlign: 'center' }}>
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
          onClick={() => navigate('/algorithms')}
          className="btn btn-ghost btn-sm"
          style={{ gap: 4, color: 'var(--accent-primary)', fontSize: '0.78rem' }}
        >
          <ExternalLink size={14} /> Full Algorithm Lab
        </button>
      </div>

      {renderInteractiveDiagram()}
    </div>
  );
}
