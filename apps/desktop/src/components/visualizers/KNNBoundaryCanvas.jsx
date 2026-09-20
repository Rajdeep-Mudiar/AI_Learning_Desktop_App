import React, { useState, useEffect, useRef } from 'react';
import { Sliders, RotateCcw, Plus, Sparkles, Maximize2, Minimize2, Trash2, MousePointer } from 'lucide-react';

export default function KNNBoundaryCanvas() {
  const [points, setPoints] = useState([
    // Class 0: Blue (Top-Left)
    { x: 30, y: 40, label: 0 },
    { x: 50, y: 60, label: 0 },
    { x: 40, y: 90, label: 0 },
    { x: 70, y: 50, label: 0 },
    { x: 60, y: 80, label: 0 },
    // Class 1: Red (Bottom-Right)
    { x: 140, y: 150, label: 1 },
    { x: 160, y: 130, label: 1 },
    { x: 170, y: 170, label: 1 },
    { x: 130, y: 180, label: 1 },
    { x: 150, y: 190, label: 1 },
    // Class 2: Emerald (Top-Right)
    { x: 150, y: 40, label: 2 },
    { x: 170, y: 60, label: 2 },
    { x: 130, y: 70, label: 2 },
    { x: 160, y: 90, label: 2 },
    { x: 180, y: 45, label: 2 },
  ]);

  const [k, setK] = useState(3);
  const [metric, setMetric] = useState('euclidean');
  const [activeClass, setActiveClass] = useState(0);
  const [mouseQuery, setMouseQuery] = useState(null);
  const [isFullscreen, setIsFullscreen] = useState(false);
  const [manualX, setManualX] = useState('100');
  const [manualY, setManualY] = useState('100');

  const canvasWidth = isFullscreen ? 360 : 260;
  const canvasHeight = isFullscreen ? 360 : 260;
  const stepSize = isFullscreen ? 10 : 8;

  useEffect(() => {
    const handleKeyDown = (e) => {
      if (e.key === 'Escape' && isFullscreen) setIsFullscreen(false);
    };
    window.addEventListener('keydown', handleKeyDown);
    return () => window.removeEventListener('keydown', handleKeyDown);
  }, [isFullscreen]);

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
    'rgba(59, 130, 246, 0.22)',
    'rgba(239, 68, 68, 0.22)',
    'rgba(16, 185, 129, 0.22)',
  ];

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

  const handleManualAdd = (e) => {
    e?.preventDefault();
    const x = parseFloat(manualX);
    const y = parseFloat(manualY);
    if (!isNaN(x) && !isNaN(y)) {
      setPoints((prev) => [...prev, { x, y, label: activeClass }]);
    }
  };

  const handleLoadPreset = (type) => {
    const newPts = [];
    if (type === 'blobs') {
      const centers = [
        { cx: 50, cy: 60, lbl: 0 },
        { cx: 180, cy: 190, lbl: 1 },
        { cx: 180, cy: 60, lbl: 2 },
      ];
      centers.forEach((c) => {
        for (let i = 0; i < 10; i++) {
          newPts.push({
            x: Math.max(10, Math.min(canvasWidth - 10, c.cx + (Math.random() - 0.5) * 50)),
            y: Math.max(10, Math.min(canvasHeight - 10, c.cy + (Math.random() - 0.5) * 50)),
            label: c.lbl
          });
        }
      });
    } else if (type === 'concentric') {
      // Inner circle class 0, outer ring class 1
      for (let i = 0; i < 16; i++) {
        const ang = (i / 16) * Math.PI * 2;
        newPts.push({
          x: canvasWidth / 2 + Math.cos(ang) * (Math.random() * 30),
          y: canvasHeight / 2 + Math.sin(ang) * (Math.random() * 30),
          label: 0
        });
      }
      for (let i = 0; i < 24; i++) {
        const ang = (i / 24) * Math.PI * 2;
        const rad = 65 + Math.random() * 25;
        newPts.push({
          x: canvasWidth / 2 + Math.cos(ang) * rad,
          y: canvasHeight / 2 + Math.sin(ang) * rad,
          label: 1
        });
      }
    } else if (type === 'dense') {
      for (let i = 0; i < 45; i++) {
        const lbl = i % 3;
        const cx = lbl === 0 ? 60 : (lbl === 1 ? 200 : 130);
        const cy = lbl === 0 ? 80 : (lbl === 1 ? 190 : 60);
        newPts.push({
          x: Math.max(10, Math.min(canvasWidth - 10, cx + (Math.random() - 0.5) * 60)),
          y: Math.max(10, Math.min(canvasHeight - 10, cy + (Math.random() - 0.5) * 60)),
          label: lbl
        });
      }
    }
    setPoints(newPts);
  };

  return (
    <div className={`card ${isFullscreen ? 'simulation-fullscreen-overlay' : ''}`} style={{ padding: isFullscreen ? 32 : 24 }}>
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', marginBottom: 18, flexWrap: 'wrap', gap: 12 }}>
        <div>
          <div style={{ display: 'flex', alignItems: 'center', gap: 10, marginBottom: 4 }}>
            <h2 style={{ fontSize: isFullscreen ? '1.5rem' : '1.25rem' }}>
              K-Nearest Neighbors & Decision Boundary Shading
            </h2>
            {isFullscreen && <span className="badge badge-purple">Fullscreen View</span>}
          </div>
          <p style={{ fontSize: '0.85rem', color: 'var(--text-secondary)' }}>
            Click anywhere on the canvas to place new training samples and observe dynamic boundary shifts in real time.
          </p>
        </div>

        <div style={{ display: 'flex', gap: 8, alignItems: 'center' }}>
          <button 
            onClick={() => setIsFullscreen(!isFullscreen)} 
            className="btn btn-secondary btn-sm"
            title={isFullscreen ? 'Exit Fullscreen (Esc)' : 'Expand to Fullscreen'}
          >
            {isFullscreen ? <Minimize2 size={15} /> : <Maximize2 size={15} />}
            <span>{isFullscreen ? 'Exit Fullscreen' : 'Full Screen'}</span>
          </button>
          <button onClick={() => setPoints([])} className="btn btn-secondary btn-sm">
            <RotateCcw size={14} /> Clear Canvas
          </button>
        </div>
      </div>

      {/* Presets & Manual Addition Bar */}
      <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', background: 'var(--bg-secondary)', padding: '10px 16px', borderRadius: 'var(--radius-md)', border: '1px solid var(--border-subtle)', marginBottom: 16, flexWrap: 'wrap', gap: 12 }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: 6, flexWrap: 'wrap' }}>
          <span style={{ fontSize: '0.75rem', fontWeight: 700, color: 'var(--text-muted)', textTransform: 'uppercase' }}>
            Presets:
          </span>
          <button onClick={() => handleLoadPreset('blobs')} className="btn btn-ghost btn-sm" style={{ border: '1px solid var(--border-subtle)' }}>
            3 Blobs (30 pts)
          </button>
          <button onClick={() => handleLoadPreset('concentric')} className="btn btn-ghost btn-sm" style={{ border: '1px solid var(--border-subtle)' }}>
            Concentric Rings (40 pts)
          </button>
          <button onClick={() => handleLoadPreset('dense')} className="btn btn-ghost btn-sm" style={{ border: '1px solid var(--border-subtle)' }}>
            Dense Scatter (45 pts)
          </button>
        </div>

        <form onSubmit={handleManualAdd} style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
          <span style={{ fontSize: '0.75rem', color: 'var(--text-secondary)' }}>Add Manual Point:</span>
          <input 
            type="number" 
            min="5" 
            max={canvasWidth} 
            value={manualX} 
            onChange={(e) => setManualX(e.target.value)} 
            className="form-input" 
            style={{ width: 60, padding: '4px 8px', fontSize: '0.8rem' }}
          />
          <input 
            type="number" 
            min="5" 
            max={canvasHeight} 
            value={manualY} 
            onChange={(e) => setManualY(e.target.value)} 
            className="form-input" 
            style={{ width: 60, padding: '4px 8px', fontSize: '0.8rem' }}
          />
          <button type="submit" className="btn btn-secondary btn-sm" style={{ padding: '5px 10px' }}>
            <Plus size={14} /> Add
          </button>
        </form>
      </div>

      <div style={{ display: 'grid', gridTemplateColumns: isFullscreen ? '1.4fr 1fr' : '1.2fr 1fr', gap: 20, marginBottom: 20 }}>
        {/* Interactive 2D Grid Canvas */}
        <div
          className="simulation-canvas-container"
          onClick={handleCanvasClick}
          onMouseMove={handleMouseMove}
          onMouseLeave={() => setMouseQuery(null)}
          style={{
            cursor: 'crosshair',
            height: isFullscreen ? '480px' : '360px',
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center',
          }}
        >
          <svg width="100%" height="100%" viewBox={`0 0 ${canvasWidth} ${canvasHeight}`} style={{ display: 'block', borderRadius: 8, overflow: 'hidden' }}>
            {/* Grid Decision Shading */}
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
              <g key={i}>
                <circle
                  cx={pt.x}
                  cy={pt.y}
                  r="5.5"
                  fill={classColors[pt.label]}
                  stroke="#ffffff"
                  strokeWidth="2"
                />
              </g>
            ))}

            {/* Hover Cursor Query Circle */}
            {mouseQuery && (
              <g>
                <circle
                  cx={mouseQuery.x}
                  cy={mouseQuery.y}
                  r="9"
                  fill="none"
                  stroke="#fbbf24"
                  strokeWidth="2"
                  strokeDasharray="3 2"
                />
                <circle
                  cx={mouseQuery.x}
                  cy={mouseQuery.y}
                  r="4"
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
              Class to Add on Click / Input ({points.length} samples total)
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
                    color: activeClass === idx ? '#ffffff' : 'var(--text-primary)'
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
                max="19"
                step="1"
                value={k}
                onChange={(e) => setK(parseInt(e.target.value))}
                style={{ width: '100%' }}
              />
            </div>

            <div>
              <label className="form-label" style={{ fontSize: '0.8rem' }}>Distance Metric</label>
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
              <div style={{ fontSize: '0.8rem', color: 'var(--text-secondary)', padding: '10px 14px', background: 'var(--bg-tertiary)', borderRadius: 8, border: '1px solid var(--border-subtle)' }}>
                Pointer Location: ({Math.round(mouseQuery.x)}, {Math.round(mouseQuery.y)}) → Predicted: <b style={{ color: classColors[mouseQuery.pred] }}>Class {mouseQuery.pred}</b>
              </div>
            )}
          </div>
        </div>
      </div>
    </div>
  );
}
