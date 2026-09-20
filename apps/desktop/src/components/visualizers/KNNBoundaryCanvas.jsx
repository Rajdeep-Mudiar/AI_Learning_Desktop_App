import React, { useState, useEffect, useRef } from 'react';
import { Sliders, RotateCcw, Plus, Sparkles } from 'lucide-react';

export default function KNNBoundaryCanvas() {
  const [points, setPoints] = useState([
    // Class 0: Blue (Top-Left)
    { x: 30, y: 40, label: 0 },
    { x: 50, y: 60, label: 0 },
    { x: 40, y: 90, label: 0 },
    { x: 70, y: 50, label: 0 },
    // Class 1: Red (Bottom-Right)
    { x: 140, y: 150, label: 1 },
    { x: 160, y: 130, label: 1 },
    { x: 170, y: 170, label: 1 },
    { x: 130, y: 180, label: 1 },
    // Class 2: Emerald (Top-Right)
    { x: 150, y: 40, label: 2 },
    { x: 170, y: 60, label: 2 },
    { x: 130, y: 70, label: 2 },
  ]);

  const [k, setK] = useState(3);
  const [metric, setMetric] = useState('euclidean');
  const [activeClass, setActiveClass] = useState(0); // For clicking to add points
  const [mouseQuery, setMouseQuery] = useState(null);

  const canvasWidth = 220;
  const canvasHeight = 220;
  const stepSize = 8; // Grid resolution

  const getDistance = (x1, y1, x2, y2) => {
    if (metric === 'manhattan') {
      return Math.abs(x1 - x2) + Math.abs(y1 - y2);
    }
    return Math.hypot(x1 - x2, y1 - y2);
  };

  const predictKNN = (x, y) => {
    if (points.length === 0) return 0;
    const distances = points.map((p) => ({
      dist: getDistance(x, y, p.x, p.y),
      label: p.label,
    }));
    distances.sort((a, b) => a.dist - b.dist);
    const kNearest = distances.slice(0, Math.min(k, distances.length));

    // Majority vote
    const counts = {};
    kNearest.forEach((n) => {
      counts[n.label] = (counts[n.label] || 0) + 1;
    });

    let bestLabel = 0;
    let maxCount = -1;
    Object.entries(counts).forEach(([lbl, cnt]) => {
      if (cnt > maxCount) {
        maxCount = cnt;
        bestLabel = parseInt(lbl);
      }
    });
    return bestLabel;
  };

  const classColors = ['#3b82f6', '#ef4444', '#10b981'];
  const bgShades = [
    'rgba(59, 130, 246, 0.18)',
    'rgba(239, 68, 68, 0.18)',
    'rgba(16, 185, 129, 0.18)',
  ];

  // Canvas click to add point
  const handleCanvasClick = (e) => {
    const rect = e.currentTarget.getBoundingClientRect();
    const x = ((e.clientX - rect.left) / rect.width) * canvasWidth;
    const y = ((e.clientY - rect.top) / rect.height) * canvasHeight;
    setPoints((prev) => [...prev, { x, y, label: activeClass }]);
  };

  const handleMouseMove = (e) => {
    const rect = e.currentTarget.getBoundingClientRect();
    const x = ((e.clientX - rect.left) / rect.width) * canvasWidth;
    const y = ((e.clientY - rect.top) / rect.height) * canvasHeight;
    const pred = predictKNN(x, y);
    setMouseQuery({ x, y, pred });
  };

  return (
    <div className="card" style={{ padding: 24 }}>
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: 18 }}>
        <div>
          <h2 style={{ fontSize: '1.25rem', marginBottom: 4 }}>K-Nearest Neighbors & Decision Boundary Shading</h2>
          <p style={{ fontSize: '0.85rem', color: 'var(--text-secondary)' }}>
            Click anywhere on the canvas to place new training samples and observe dynamic boundary shifts.
          </p>
        </div>

        <button onClick={() => setPoints([])} className="btn btn-secondary btn-sm">
          <RotateCcw size={14} /> Clear Canvas
        </button>
      </div>

      <div style={{ display: 'grid', gridTemplateColumns: '1.2fr 1fr', gap: 20, marginBottom: 20 }}>
        {/* Interactive 2D Grid Canvas */}
        <div
          onClick={handleCanvasClick}
          onMouseMove={handleMouseMove}
          onMouseLeave={() => setMouseQuery(null)}
          style={{
            background: '#070a13',
            borderRadius: 'var(--radius-md)',
            border: '1px solid var(--border-subtle)',
            overflow: 'hidden',
            cursor: 'crosshair',
            position: 'relative',
            height: '340px'
          }}
        >
          <svg width="100%" height="100%" viewBox={`0 0 ${canvasWidth} ${canvasHeight}`} style={{ display: 'block' }}>
            {/* Grid Shading */}
            {Array.from({ length: Math.ceil(canvasWidth / stepSize) }).map((_, i) =>
              Array.from({ length: Math.ceil(canvasHeight / stepSize) }).map((_, j) => {
                const gx = i * stepSize;
                const gy = j * stepSize;
                const label = predictKNN(gx + stepSize / 2, gy + stepSize / 2);
                return (
                  <rect
                    key={`${i}-${j}`}
                    x={gx}
                    y={gy}
                    width={stepSize}
                    height={stepSize}
                    fill={bgShades[label]}
                  />
                );
              })
            )}

            {/* Training Sample Points */}
            {points.map((pt, i) => (
              <circle
                key={i}
                cx={pt.x}
                cy={pt.y}
                r="5"
                fill={classColors[pt.label]}
                stroke="#ffffff"
                strokeWidth="1.5"
              />
            ))}

            {/* Hover Cursor Query Circle */}
            {mouseQuery && (
              <g>
                <circle
                  cx={mouseQuery.x}
                  cy={mouseQuery.y}
                  r="7"
                  fill="none"
                  stroke="#fbbf24"
                  strokeWidth="2"
                  strokeDasharray="3 2"
                />
                <circle
                  cx={mouseQuery.x}
                  cy={mouseQuery.y}
                  r="3"
                  fill={classColors[mouseQuery.pred]}
                />
              </g>
            )}
          </svg>
        </div>

        {/* Controls & Class Picker */}
        <div style={{ display: 'flex', flexDirection: 'column', gap: 14 }}>
          {/* Active class placing */}
          <div style={{ background: 'var(--bg-secondary)', padding: 14, borderRadius: 'var(--radius-md)', border: '1px solid var(--border-subtle)' }}>
            <div style={{ fontSize: '0.75rem', color: 'var(--text-muted)', marginBottom: 8, fontWeight: 700 }}>
              Class to Add on Click
            </div>
            <div style={{ display: 'flex', gap: 8 }}>
              {['Class 0 (Blue)', 'Class 1 (Red)', 'Class 2 (Green)'].map((name, idx) => (
                <button
                  key={idx}
                  onClick={() => setActiveClass(idx)}
                  className={activeClass === idx ? 'btn btn-primary btn-sm' : 'btn btn-secondary btn-sm'}
                  style={{
                    flex: 1,
                    fontSize: '0.75rem',
                    background: activeClass === idx ? classColors[idx] : 'var(--bg-tertiary)',
                    borderColor: classColors[idx],
                  }}
                >
                  {name}
                </button>
              ))}
            </div>
          </div>

          {/* Hyperparameters */}
          <div style={{ background: 'var(--bg-secondary)', padding: 16, borderRadius: 'var(--radius-md)', border: '1px solid var(--border-subtle)', display: 'flex', flexDirection: 'column', gap: 14 }}>
            <div>
              <div style={{ display: 'flex', justifyContent: 'space-between', fontSize: '0.825rem', marginBottom: 6 }}>
                <span>Neighbors (K): <b>{k}</b></span>
                <span style={{ color: 'var(--text-muted)' }}>{k % 2 === 0 ? '⚠️ Even K (Tie risks)' : 'Odd K (Stable)'}</span>
              </div>
              <input
                type="range"
                min="1"
                max="15"
                step="1"
                value={k}
                onChange={(e) => setK(parseInt(e.target.value))}
                style={{ width: '100%' }}
              />
            </div>

            <div>
              <label className="form-label">Distance Metric</label>
              <div style={{ display: 'flex', gap: 8 }}>
                <button
                  onClick={() => setMetric('euclidean')}
                  className={metric === 'euclidean' ? 'btn btn-primary btn-sm' : 'btn btn-secondary btn-sm'}
                  style={{ flex: 1 }}
                >
                  Euclidean (L2)
                </button>
                <button
                  onClick={() => setMetric('manhattan')}
                  className={metric === 'manhattan' ? 'btn btn-primary btn-sm' : 'btn btn-secondary btn-sm'}
                  style={{ flex: 1 }}
                >
                  Manhattan (L1)
                </button>
              </div>
            </div>

            {mouseQuery && (
              <div style={{ fontSize: '0.8rem', color: 'var(--text-secondary)', padding: '8px 12px', background: 'var(--bg-tertiary)', borderRadius: 6 }}>
                Pointer Location: ({Math.round(mouseQuery.x)}, {Math.round(mouseQuery.y)}) → Predicted: <b style={{ color: classColors[mouseQuery.pred] }}>Class {mouseQuery.pred}</b>
              </div>
            )}
          </div>
        </div>
      </div>
    </div>
  );
}
