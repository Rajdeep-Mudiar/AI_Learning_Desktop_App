import React, { useState, useEffect, useRef } from 'react';
import { Sliders, Sparkles, RotateCcw, Maximize2, Minimize2, Plus, MousePointer } from 'lucide-react';
import { simulationService } from '../../services/simulationService';
import ProgressBar from '../common/ProgressBar';

export default function PCACanvas() {
  const [spreadAngle, setSpreadAngle] = useState(35);
  const [pointCount, setPointCount] = useState(35);
  const [points, setPoints] = useState([]);
  const [pcaResult, setPcaResult] = useState(null);
  const [showProjection, setShowProjection] = useState(true);
  const [isFullscreen, setIsFullscreen] = useState(false);
  const [manualX, setManualX] = useState('100');
  const [manualY, setManualY] = useState('100');

  const svgRef = useRef(null);

  useEffect(() => {
    const handleKeyDown = (e) => {
      if (e.key === 'Escape' && isFullscreen) setIsFullscreen(false);
    };
    window.addEventListener('keydown', handleKeyDown);
    return () => window.removeEventListener('keydown', handleKeyDown);
  }, [isFullscreen]);

  // Generate correlated 2D Gaussian dataset
  const generateCloud = (angleDeg = spreadAngle, count = pointCount) => {
    const rad = (angleDeg * Math.PI) / 180;
    const cosA = Math.cos(rad);
    const sinA = Math.sin(rad);

    const newPts = [];
    for (let i = 0; i < count; i++) {
      const u = (Math.random() - 0.5) * 75;
      const v = (Math.random() - 0.5) * 20;
      const x = 100 + (u * cosA - v * sinA);
      const y = 100 + (u * sinA + v * cosA);
      newPts.push({ x: parseFloat(x.toFixed(2)), y: parseFloat(y.toFixed(2)) });
    }
    setPoints(newPts);
  };

  useEffect(() => {
    generateCloud(spreadAngle, pointCount);
  }, [spreadAngle, pointCount]);

  useEffect(() => {
    async function runPCA() {
      if (points.length < 2) return;
      try {
        const res = await simulationService.computePCA(points);
        setPcaResult(res);
      } catch (err) {
        console.error('PCA computation failed:', err);
      }
    }
    runPCA();
  }, [points]);

  const handleCanvasClick = (e) => {
    if (!svgRef.current) return;
    const rect = svgRef.current.getBoundingClientRect();
    const x = parseFloat((((e.clientX - rect.left) / rect.width) * 200).toFixed(2));
    const y = parseFloat((((e.clientY - rect.top) / rect.height) * 200).toFixed(2));
    setPoints((prev) => [...prev, { x, y }]);
  };

  const handleManualAdd = (e) => {
    e?.preventDefault();
    const x = parseFloat(manualX);
    const y = parseFloat(manualY);
    if (!isNaN(x) && !isNaN(y)) {
      setPoints((prev) => [...prev, { x, y }]);
    }
  };

  const mean = pcaResult?.mean || { x: 100, y: 100 };
  const v1 = pcaResult?.components?.[0] || { x: 1, y: 0 };
  const v2 = pcaResult?.components?.[1] || { x: 0, y: 1 };
  const pc1VarRatio = pcaResult ? Math.round(pcaResult.explained_variance_ratio[0] * 100) : 85;

  return (
    <div className={`card ${isFullscreen ? 'simulation-fullscreen-overlay' : ''}`} style={{ padding: isFullscreen ? 32 : 24 }}>
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', marginBottom: 18, flexWrap: 'wrap', gap: 12 }}>
        <div>
          <div style={{ display: 'flex', alignItems: 'center', gap: 10, marginBottom: 4 }}>
            <h2 style={{ fontSize: isFullscreen ? '1.5rem' : '1.25rem' }}>
              Principal Component Analysis (PCA) & Subspace Projection
            </h2>
            {isFullscreen && <span className="badge badge-purple">Fullscreen View</span>}
          </div>
          <p style={{ fontSize: '0.85rem', color: 'var(--text-secondary)' }}>
            Inspect orthogonal eigenvectors and dimensionality reduction onto the direction of maximal variance.
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
          <button onClick={() => generateCloud(spreadAngle, pointCount)} className="btn btn-secondary btn-sm">
            <Sparkles size={14} /> New Point Cloud
          </button>
          <button onClick={() => setPoints([])} className="btn btn-secondary btn-sm">
            <RotateCcw size={14} /> Clear Points
          </button>
        </div>
      </div>

      {/* Manual Input & Point Density Bar */}
      <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', background: 'var(--bg-secondary)', padding: '10px 16px', borderRadius: 'var(--radius-md)', border: '1px solid var(--border-subtle)', marginBottom: 16, flexWrap: 'wrap', gap: 12 }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: 10 }}>
          <span style={{ fontSize: '0.75rem', fontWeight: 700, color: 'var(--text-muted)', textTransform: 'uppercase' }}>
            Density:
          </span>
          <input 
            type="range" 
            min="10" 
            max="100" 
            step="5" 
            value={pointCount} 
            onChange={(e) => setPointCount(parseInt(e.target.value))} 
            style={{ width: 120 }}
          />
          <span style={{ fontSize: '0.8rem', fontWeight: 700 }}>{pointCount} Points</span>
        </div>

        <form onSubmit={handleManualAdd} style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
          <span style={{ fontSize: '0.75rem', color: 'var(--text-secondary)' }}>Add Point:</span>
          <input 
            type="number" 
            min="5" 
            max="195" 
            value={manualX} 
            onChange={(e) => setManualX(e.target.value)} 
            className="form-input" 
            style={{ width: 60, padding: '4px 8px', fontSize: '0.8rem' }}
          />
          <input 
            type="number" 
            min="5" 
            max="195" 
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

      <div style={{ display: 'grid', gridTemplateColumns: isFullscreen ? '1.5fr 1fr' : '1.3fr 1fr', gap: 20, marginBottom: 20 }}>
        {/* SVG PCA Plot */}
        <div 
          className="simulation-canvas-container" 
          style={{ height: isFullscreen ? '450px' : '340px', position: 'relative', cursor: 'crosshair' }}
        >
          <svg 
            ref={svgRef}
            width="100%" 
            height="100%" 
            viewBox="0 0 200 200" 
            onClick={handleCanvasClick}
            style={{ display: 'block', borderRadius: 8 }}
          >
            {/* Grid */}
            <line x1="100" y1="10" x2="100" y2="190" stroke="var(--canvas-grid)" strokeDasharray="3 3" strokeWidth="1" />
            <line x1="10" y1="100" x2="190" y2="100" stroke="var(--canvas-grid)" strokeDasharray="3 3" strokeWidth="1" />

            {/* Projection dashed lines */}
            {showProjection && pcaResult?.projected_points?.map((proj, i) => {
              const orig = points[i];
              if (!orig) return null;
              return (
                <line
                  key={`proj-line-${i}`}
                  x1={orig.x}
                  y1={orig.y}
                  x2={proj.x}
                  y2={proj.y}
                  stroke="#fbbf24"
                  strokeWidth="0.9"
                  strokeDasharray="2 2"
                  strokeOpacity="0.45"
                />
              );
            })}

            {/* Projected Points onto PC1 */}
            {showProjection && pcaResult?.projected_points?.map((proj, i) => (
              <circle
                key={`proj-pt-${i}`}
                cx={proj.x}
                cy={proj.y}
                r="3"
                fill="#fbbf24"
              />
            ))}

            {/* Original 2D points */}
            {points.map((pt, i) => (
              <circle
                key={`orig-${i}`}
                cx={pt.x}
                cy={pt.y}
                r="4.5"
                fill="var(--canvas-point)"
                stroke="var(--canvas-point-stroke)"
                strokeWidth="1.2"
              />
            ))}

            {/* PC1 Eigenvector Arrow */}
            <line
              x1={mean.x - v1.x * 65}
              y1={mean.y - v1.y * 65}
              x2={mean.x + v1.x * 65}
              y2={mean.y + v1.y * 65}
              stroke="var(--accent-primary)"
              strokeWidth="3"
            />

            {/* PC2 Eigenvector Arrow */}
            <line
              x1={mean.x - v2.x * 30}
              y1={mean.y - v2.y * 30}
              x2={mean.x + v2.x * 30}
              y2={mean.y + v2.y * 30}
              stroke="var(--accent-pink)"
              strokeWidth="2.2"
            />

            {/* Mean Center */}
            <circle cx={mean.x} cy={mean.y} r="5" fill="#ffffff" stroke="var(--accent-primary)" strokeWidth="2.5" />
          </svg>

          <div style={{ position: 'absolute', bottom: 12, right: 16, fontSize: '0.72rem', color: 'var(--text-muted)', display: 'flex', alignItems: 'center', gap: 4, pointerEvents: 'none' }}>
            <MousePointer size={12} /> Click canvas to add datapoint
          </div>
        </div>

        {/* Variance Explained & Controls */}
        <div style={{ display: 'flex', flexDirection: 'column', gap: 14 }}>
          {/* Variance Breakdown Card */}
          <div style={{ background: 'var(--bg-secondary)', padding: 16, borderRadius: 'var(--radius-md)', border: '1px solid var(--border-subtle)' }}>
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: 12 }}>
              <span style={{ fontSize: '0.75rem', color: 'var(--text-muted)', textTransform: 'uppercase', fontWeight: 700 }}>
                Explained Variance Ratio
              </span>
              <span className="badge badge-purple">{points.length} Points</span>
            </div>

            <div style={{ marginBottom: 12 }}>
              <div style={{ display: 'flex', justifyContent: 'space-between', fontSize: '0.85rem', marginBottom: 4 }}>
                <span style={{ color: 'var(--accent-primary)', fontWeight: 600 }}>PC1 (Principal Axis)</span>
                <b>{pc1VarRatio}%</b>
              </div>
              <ProgressBar percentage={pc1VarRatio} color="var(--accent-primary)" height={8} />
            </div>

            <div>
              <div style={{ display: 'flex', justifyContent: 'space-between', fontSize: '0.85rem', marginBottom: 4 }}>
                <span style={{ color: 'var(--accent-pink)', fontWeight: 600 }}>PC2 (Orthogonal Axis)</span>
                <b>{100 - pc1VarRatio}%</b>
              </div>
              <ProgressBar percentage={100 - pc1VarRatio} color="var(--accent-pink)" height={8} />
            </div>
          </div>

          {/* Cloud Rotation Angle Slider */}
          <div style={{ background: 'var(--bg-secondary)', padding: 16, borderRadius: 'var(--radius-md)', border: '1px solid var(--border-subtle)', display: 'flex', flexDirection: 'column', gap: 12 }}>
            <div>
              <div style={{ display: 'flex', justifyContent: 'space-between', fontSize: '0.825rem', marginBottom: 6 }}>
                <span>Data Distribution Angle: <b>{spreadAngle}°</b></span>
              </div>
              <input
                type="range"
                min="0"
                max="180"
                step="5"
                value={spreadAngle}
                onChange={(e) => setSpreadAngle(parseInt(e.target.value))}
                style={{ width: '100%' }}
              />
            </div>

            <div style={{ display: 'flex', alignItems: 'center', gap: 8, marginTop: 4 }}>
              <input
                type="checkbox"
                id="showProj"
                checked={showProjection}
                onChange={(e) => setShowProjection(e.target.checked)}
              />
              <label htmlFor="showProj" style={{ fontSize: '0.85rem', color: 'var(--text-secondary)', cursor: 'pointer' }}>
                Show 1D Subspace Projections (Yellow)
              </label>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
