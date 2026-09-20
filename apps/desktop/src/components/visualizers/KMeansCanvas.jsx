import React, { useState, useEffect, useRef } from 'react';
import { Play, Pause, StepForward, RotateCcw, Sparkles, Activity, Maximize2, Minimize2, Plus, MousePointer } from 'lucide-react';
import { simulationService } from '../../services/simulationService';

export default function KMeansCanvas() {
  const [points, setPoints] = useState([
    // Cluster 1 (Top-Left)
    { x: 30, y: 40 }, { x: 45, y: 55 }, { x: 35, y: 70 }, { x: 60, y: 45 }, { x: 50, y: 80 }, { x: 40, y: 60 },
    // Cluster 2 (Bottom-Left)
    { x: 40, y: 150 }, { x: 55, y: 165 }, { x: 35, y: 180 }, { x: 65, y: 145 }, { x: 50, y: 175 }, { x: 60, y: 160 },
    // Cluster 3 (Right)
    { x: 150, y: 90 }, { x: 165, y: 110 }, { x: 175, y: 85 }, { x: 140, y: 120 }, { x: 160, y: 135 }, { x: 150, y: 115 },
  ]);

  const [k, setK] = useState(3);
  const [centroids, setCentroids] = useState([
    { x: 20, y: 30 },
    { x: 100, y: 100 },
    { x: 180, y: 170 },
  ]);

  const [assignments, setAssignments] = useState([]);
  const [iteration, setIteration] = useState(0);
  const [inertia, setInertia] = useState(0.0);
  const [converged, setConverged] = useState(false);
  const [isPlaying, setIsPlaying] = useState(false);
  const [isFullscreen, setIsFullscreen] = useState(false);
  const [manualX, setManualX] = useState('100');
  const [manualY, setManualY] = useState('100');

  const svgRef = useRef(null);
  const clusterColors = ['#3b82f6', '#ef4444', '#10b981', '#f59e0b', '#a855f7'];

  useEffect(() => {
    const handleKeyDown = (e) => {
      if (e.key === 'Escape' && isFullscreen) setIsFullscreen(false);
    };
    window.addEventListener('keydown', handleKeyDown);
    return () => window.removeEventListener('keydown', handleKeyDown);
  }, [isFullscreen]);

  const handleGeneratePoints = (type = '3blobs') => {
    const newPts = [];
    if (type === '3blobs') {
      const centers = [
        { cx: 45, cy: 50 },
        { cx: 50, cy: 160 },
        { cx: 160, cy: 100 },
      ];
      centers.forEach((c) => {
        for (let i = 0; i < 10; i++) {
          newPts.push({
            x: Math.round(Math.max(10, Math.min(190, c.cx + (Math.random() - 0.5) * 45))),
            y: Math.round(Math.max(10, Math.min(190, c.cy + (Math.random() - 0.5) * 45))),
          });
        }
      });
    } else if (type === '4blobs') {
      const centers = [
        { cx: 45, cy: 45 },
        { cx: 155, cy: 45 },
        { cx: 45, cy: 155 },
        { cx: 155, cy: 155 },
      ];
      centers.forEach((c) => {
        for (let i = 0; i < 12; i++) {
          newPts.push({
            x: Math.round(Math.max(10, Math.min(190, c.cx + (Math.random() - 0.5) * 40))),
            y: Math.round(Math.max(10, Math.min(190, c.cy + (Math.random() - 0.5) * 40))),
          });
        }
      });
    } else if (type === 'scatter') {
      for (let i = 0; i < 50; i++) {
        newPts.push({
          x: Math.round(15 + Math.random() * 170),
          y: Math.round(15 + Math.random() * 170),
        });
      }
    }
    setPoints(newPts);
    handleReset(newPts);
  };

  const handleReset = (currentPts = points, currentK = k) => {
    setIsPlaying(false);
    setIteration(0);
    setConverged(false);
    setAssignments([]);
    const initialC = [];
    for (let i = 0; i < currentK; i++) {
      initialC.push({
        x: Math.round(30 + Math.random() * 140),
        y: Math.round(30 + Math.random() * 140),
      });
    }
    setCentroids(initialC);
  };

  const handleKChange = (newK) => {
    setK(newK);
    handleReset(points, newK);
  };

  const stepIteration = async () => {
    if (converged || points.length === 0) return;
    try {
      const res = await simulationService.stepKMeans(points, centroids);
      setAssignments(res.assignments);
      setCentroids(res.new_centroids);
      setInertia(res.inertia);
      setConverged(res.converged);
      setIteration((prev) => prev + 1);
      if (res.converged) {
        setIsPlaying(false);
      }
    } catch (err) {
      console.error('KMeans error:', err);
      setIsPlaying(false);
    }
  };

  const handleCanvasClick = (e) => {
    if (!svgRef.current) return;
    const rect = svgRef.current.getBoundingClientRect();
    const x = Math.round(((e.clientX - rect.left) / rect.width) * 200);
    const y = Math.round(((e.clientY - rect.top) / rect.height) * 200);
    if (x >= 5 && x <= 195 && y >= 5 && y <= 195) {
      setPoints((prev) => [...prev, { x, y }]);
      setConverged(false);
    }
  };

  const handleManualAdd = (e) => {
    e?.preventDefault();
    const x = parseFloat(manualX);
    const y = parseFloat(manualY);
    if (!isNaN(x) && !isNaN(y)) {
      setPoints((prev) => [...prev, { x, y }]);
      setConverged(false);
    }
  };

  useEffect(() => {
    let timer;
    if (isPlaying && !converged) {
      timer = setInterval(async () => {
        await stepIteration();
      }, 450);
    }
    return () => clearInterval(timer);
  }, [isPlaying, converged, points, centroids]);

  return (
    <div className={`card ${isFullscreen ? 'simulation-fullscreen-overlay' : ''}`} style={{ padding: isFullscreen ? 32 : 24 }}>
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', marginBottom: 18, flexWrap: 'wrap', gap: 12 }}>
        <div>
          <div style={{ display: 'flex', alignItems: 'center', gap: 10, marginBottom: 4 }}>
            <h2 style={{ fontSize: isFullscreen ? '1.5rem' : '1.25rem' }}>
              K-Means Clustering & Centroid Dynamics
            </h2>
            {isFullscreen && <span className="badge badge-purple">Fullscreen View</span>}
          </div>
          <p style={{ fontSize: '0.85rem', color: 'var(--text-secondary)' }}>
            Click anywhere inside the 2D plane to place custom points and watch centroids iteratively track cluster centers of mass.
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
          <button onClick={() => handleGeneratePoints('3blobs')} className="btn btn-secondary btn-sm">
            <Sparkles size={14} /> New Blobs
          </button>
          <button onClick={() => handleReset()} className="btn btn-secondary btn-sm">
            <RotateCcw size={14} /> Random Centroids
          </button>
        </div>
      </div>

      {/* Presets and Manual Addition Bar */}
      <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', background: 'var(--bg-secondary)', padding: '10px 16px', borderRadius: 'var(--radius-md)', border: '1px solid var(--border-subtle)', marginBottom: 16, flexWrap: 'wrap', gap: 12 }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: 6, flexWrap: 'wrap' }}>
          <span style={{ fontSize: '0.75rem', fontWeight: 700, color: 'var(--text-muted)', textTransform: 'uppercase' }}>
            Presets:
          </span>
          <button onClick={() => handleGeneratePoints('3blobs')} className="btn btn-ghost btn-sm" style={{ border: '1px solid var(--border-subtle)' }}>
            3 Blobs (30 pts)
          </button>
          <button onClick={() => handleGeneratePoints('4blobs')} className="btn btn-ghost btn-sm" style={{ border: '1px solid var(--border-subtle)' }}>
            4 Dense (48 pts)
          </button>
          <button onClick={() => handleGeneratePoints('scatter')} className="btn btn-ghost btn-sm" style={{ border: '1px solid var(--border-subtle)' }}>
            Uniform Scatter (50 pts)
          </button>
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
        {/* SVG Cluster Plot */}
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
            {/* Grid Lines */}
            <line x1="50" y1="0" x2="50" y2="200" stroke="var(--canvas-grid)" strokeDasharray="3 3" strokeWidth="0.8" />
            <line x1="100" y1="0" x2="100" y2="200" stroke="var(--canvas-grid)" strokeDasharray="3 3" strokeWidth="0.8" />
            <line x1="150" y1="0" x2="150" y2="200" stroke="var(--canvas-grid)" strokeDasharray="3 3" strokeWidth="0.8" />
            <line x1="0" y1="50" x2="200" y2="50" stroke="var(--canvas-grid)" strokeDasharray="3 3" strokeWidth="0.8" />
            <line x1="0" y1="100" x2="200" y2="100" stroke="var(--canvas-grid)" strokeDasharray="3 3" strokeWidth="0.8" />
            <line x1="0" y1="150" x2="200" y2="150" stroke="var(--canvas-grid)" strokeDasharray="3 3" strokeWidth="0.8" />

            {/* Connection lines from point to assigned centroid */}
            {points.map((pt, i) => {
              const cIdx = assignments[i];
              if (cIdx !== undefined && centroids[cIdx]) {
                const c = centroids[cIdx];
                return (
                  <line
                    key={`conn-${i}`}
                    x1={pt.x}
                    y1={pt.y}
                    x2={c.x}
                    y2={c.y}
                    stroke={clusterColors[cIdx]}
                    strokeWidth="1"
                    strokeOpacity="0.35"
                  />
                );
              }
              return null;
            })}

            {/* Points */}
            {points.map((pt, i) => {
              const cIdx = assignments[i];
              const ptColor = cIdx !== undefined ? clusterColors[cIdx] : 'var(--canvas-point)';
              return (
                <circle
                  key={`pt-${i}`}
                  cx={pt.x}
                  cy={pt.y}
                  r="4.5"
                  fill={ptColor}
                  stroke="#ffffff"
                  strokeWidth="1"
                />
              );
            })}

            {/* Centroids */}
            {centroids.map((c, i) => (
              <g key={`c-${i}`}>
                <circle
                  cx={c.x}
                  cy={c.y}
                  r="9"
                  fill={clusterColors[i]}
                  stroke="#ffffff"
                  strokeWidth="2.5"
                />
                <line x1={c.x - 5} y1={c.y} x2={c.x + 5} y2={c.y} stroke="#ffffff" strokeWidth="2" />
                <line x1={c.x} y1={c.y - 5} x2={c.x} y2={c.y + 5} stroke="#ffffff" strokeWidth="2" />
              </g>
            ))}
          </svg>

          <div style={{ position: 'absolute', bottom: 12, right: 16, fontSize: '0.72rem', color: 'var(--text-muted)', display: 'flex', alignItems: 'center', gap: 4, pointerEvents: 'none' }}>
            <MousePointer size={12} /> Click canvas to place point
          </div>
        </div>

        {/* Telemetry & Controls */}
        <div style={{ display: 'flex', flexDirection: 'column', gap: 14 }}>
          <div style={{ background: 'var(--bg-secondary)', padding: 16, borderRadius: 'var(--radius-md)', border: '1px solid var(--border-subtle)' }}>
            <div style={{ fontSize: '0.75rem', color: 'var(--text-muted)', textTransform: 'uppercase', marginBottom: 8, fontWeight: 700 }}>
              Iteration {iteration} {converged && <span style={{ color: 'var(--accent-success)', marginLeft: 6 }}>• CONVERGED</span>}
            </div>

            <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: 10 }}>
              <div style={{ background: 'var(--bg-tertiary)', padding: 10, borderRadius: 'var(--radius-sm)', border: '1px solid var(--border-subtle)' }}>
                <span style={{ fontSize: '0.72rem', color: 'var(--text-muted)' }}>Inertia (WCSS Loss)</span>
                <div style={{ fontSize: '1.3rem', fontWeight: 800, color: 'var(--accent-danger)' }}>{inertia}</div>
              </div>
              <div style={{ background: 'var(--bg-tertiary)', padding: 10, borderRadius: 'var(--radius-sm)', border: '1px solid var(--border-subtle)' }}>
                <span style={{ fontSize: '0.72rem', color: 'var(--text-muted)' }}>Datapoints Loaded</span>
                <div style={{ fontSize: '1.3rem', fontWeight: 800, color: 'var(--accent-primary)' }}>{points.length}</div>
              </div>
            </div>
          </div>

          <div style={{ background: 'var(--bg-secondary)', padding: 14, borderRadius: 'var(--radius-md)', border: '1px solid var(--border-subtle)' }}>
            <div style={{ display: 'flex', justifyContent: 'space-between', fontSize: '0.8rem', marginBottom: 8 }}>
              <span>Cluster Count (K): <b>{k}</b></span>
            </div>
            <div style={{ display: 'flex', gap: 6 }}>
              {[2, 3, 4, 5].map((val) => (
                <button
                  key={val}
                  onClick={() => handleKChange(val)}
                  className={k === val ? 'btn btn-primary btn-sm' : 'btn btn-secondary btn-sm'}
                  style={{ flex: 1 }}
                >
                  K = {val}
                </button>
              ))}
            </div>
          </div>

          <div style={{ display: 'flex', gap: 8 }}>
            <button
              onClick={() => setIsPlaying(!isPlaying)}
              className="btn btn-primary"
              disabled={converged}
              style={{ flex: 1, padding: '10px' }}
            >
              {isPlaying ? 'Pause' : 'Animate to Convergence'}
            </button>
            <button
              onClick={stepIteration}
              className="btn btn-secondary"
              disabled={converged || isPlaying}
              style={{ padding: '10px 18px' }}
            >
              <StepForward size={16} /> Step
            </button>
          </div>
        </div>
      </div>
    </div>
  );
}
