import React, { useState, useEffect } from 'react';
import { Play, StepForward, RotateCcw, Sparkles, Activity } from 'lucide-react';
import { simulationService } from '../../services/simulationService';

export default function KMeansCanvas() {
  const [points, setPoints] = useState([
    // Cluster 1 (Top-Left)
    { x: 30, y: 40 }, { x: 45, y: 55 }, { x: 35, y: 70 }, { x: 60, y: 45 }, { x: 50, y: 80 },
    // Cluster 2 (Bottom-Left)
    { x: 40, y: 150 }, { x: 55, y: 165 }, { x: 35, y: 180 }, { x: 65, y: 145 }, { x: 50, y: 175 },
    // Cluster 3 (Right)
    { x: 150, y: 90 }, { x: 165, y: 110 }, { x: 175, y: 85 }, { x: 140, y: 120 }, { x: 160, y: 135 },
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

  const clusterColors = ['#3b82f6', '#ef4444', '#10b981', '#f59e0b', '#a855f7'];

  const handleGeneratePoints = () => {
    const newPts = [];
    const centers = [
      { cx: 45, cy: 50 },
      { cx: 50, cy: 160 },
      { cx: 160, cy: 100 },
    ];
    centers.forEach((c) => {
      for (let i = 0; i < 8; i++) {
        newPts.push({
          x: Math.max(10, Math.min(190, c.cx + (Math.random() - 0.5) * 45)),
          y: Math.max(10, Math.min(190, c.cy + (Math.random() - 0.5) * 45)),
        });
      }
    });
    setPoints(newPts);
    handleReset(newPts);
  };

  const handleReset = (currentPts = points) => {
    setIsPlaying(false);
    setIteration(0);
    setConverged(false);
    setAssignments([]);
    // Random centroids
    const initialC = [];
    for (let i = 0; i < k; i++) {
      initialC.push({
        x: Math.round(30 + Math.random() * 140),
        y: Math.round(30 + Math.random() * 140),
      });
    }
    setCentroids(initialC);
  };

  const stepIteration = async () => {
    if (converged) return;
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

  useEffect(() => {
    let timer;
    if (isPlaying && !converged) {
      timer = setInterval(async () => {
        await stepIteration();
      }, 500);
    }
    return () => clearInterval(timer);
  }, [isPlaying, converged, points, centroids]);

  return (
    <div className="card" style={{ padding: 24 }}>
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: 18 }}>
        <div>
          <h2 style={{ fontSize: '1.25rem', marginBottom: 4 }}>K-Means Clustering & Centroid Dynamics</h2>
          <p style={{ fontSize: '0.85rem', color: 'var(--text-secondary)' }}>
            Watch centroids dynamically move to the center of mass of their assigned cluster points.
          </p>
        </div>

        <div style={{ display: 'flex', gap: 8 }}>
          <button onClick={handleGeneratePoints} className="btn btn-secondary btn-sm">
            <Sparkles size={14} /> New Blobs
          </button>
          <button onClick={() => handleReset()} className="btn btn-secondary btn-sm">
            <RotateCcw size={14} /> Reset
          </button>
        </div>
      </div>

      <div style={{ display: 'grid', gridTemplateColumns: '1.4fr 1fr', gap: 20, marginBottom: 20 }}>
        {/* SVG Cluster Plot */}
        <div style={{ background: '#070a13', borderRadius: 'var(--radius-md)', padding: 12, border: '1px solid var(--border-subtle)', height: '340px' }}>
          <svg width="100%" height="100%" viewBox="0 0 200 200">
            {/* Voronoi / Connection lines from point to assigned centroid */}
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
                    strokeWidth="0.8"
                    strokeOpacity="0.3"
                  />
                );
              }
              return null;
            })}

            {/* Points */}
            {points.map((pt, i) => {
              const cIdx = assignments[i];
              const ptColor = cIdx !== undefined ? clusterColors[cIdx] : '#94a3b8';
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
        </div>

        {/* Telemetry & Controls */}
        <div style={{ display: 'flex', flexDirection: 'column', gap: 14 }}>
          <div style={{ background: 'var(--bg-secondary)', padding: 16, borderRadius: 'var(--radius-md)', border: '1px solid var(--border-subtle)' }}>
            <div style={{ fontSize: '0.75rem', color: 'var(--text-muted)', textTransform: 'uppercase', marginBottom: 8, fontWeight: 700 }}>
              Iteration {iteration} {converged && <span style={{ color: '#34d399', marginLeft: 6 }}>• CONVERGED</span>}
            </div>

            <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: 10 }}>
              <div>
                <span style={{ fontSize: '0.75rem', color: 'var(--text-muted)' }}>Inertia (WCSS)</span>
                <div style={{ fontSize: '1.3rem', fontWeight: 800, color: '#f43f5e' }}>{inertia}</div>
              </div>
              <div>
                <span style={{ fontSize: '0.75rem', color: 'var(--text-muted)' }}>Clusters (K)</span>
                <div style={{ fontSize: '1.3rem', fontWeight: 800, color: '#6366f1' }}>{k}</div>
              </div>
            </div>
          </div>

          <div style={{ display: 'flex', gap: 8 }}>
            <button
              onClick={() => setIsPlaying(!isPlaying)}
              className="btn btn-primary"
              disabled={converged}
              style={{ flex: 1 }}
            >
              {isPlaying ? 'Pause' : 'Animate to Convergence'}
            </button>
            <button
              onClick={stepIteration}
              className="btn btn-secondary"
              disabled={converged || isPlaying}
            >
              <StepForward size={16} /> Step
            </button>
          </div>
        </div>
      </div>
    </div>
  );
}
