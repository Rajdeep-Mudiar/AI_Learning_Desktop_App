import React, { useState, useEffect } from 'react';
import { Sliders, Sparkles, RotateCcw } from 'lucide-react';
import { simulationService } from '../../services/simulationService';
import ProgressBar from '../common/ProgressBar';

export default function PCACanvas() {
  const [spreadAngle, setSpreadAngle] = useState(35); // degrees
  const [points, setPoints] = useState([]);
  const [pcaResult, setPcaResult] = useState(null);
  const [showProjection, setShowProjection] = useState(true);

  // Generate correlated 2D Gaussian dataset
  const generateCloud = (angleDeg = spreadAngle) => {
    const rad = (angleDeg * Math.PI) / 180;
    const cosA = Math.cos(rad);
    const sinA = Math.sin(rad);

    const newPts = [];
    for (let i = 0; i < 30; i++) {
      // Major axis variance 40, minor axis variance 10
      const u = (Math.random() - 0.5) * 70;
      const v = (Math.random() - 0.5) * 18;
      const x = 100 + (u * cosA - v * sinA);
      const y = 100 + (u * sinA + v * cosA);
      newPts.push({ x: parseFloat(x.toFixed(2)), y: parseFloat(y.toFixed(2)) });
    }
    setPoints(newPts);
  };

  useEffect(() => {
    generateCloud(spreadAngle);
  }, [spreadAngle]);

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

  const mean = pcaResult?.mean || { x: 100, y: 100 };
  const v1 = pcaResult?.components?.[0] || { x: 1, y: 0 };
  const v2 = pcaResult?.components?.[1] || { x: 0, y: 1 };
  const pc1VarRatio = pcaResult ? Math.round(pcaResult.explained_variance_ratio[0] * 100) : 85;

  return (
    <div className="card" style={{ padding: 24 }}>
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: 18 }}>
        <div>
          <h2 style={{ fontSize: '1.25rem', marginBottom: 4 }}>Principal Component Analysis (PCA) & Subspace Projection</h2>
          <p style={{ fontSize: '0.85rem', color: 'var(--text-secondary)' }}>
            Inspect orthogonal eigenvectors and dimensionality reduction onto the direction of maximal variance.
          </p>
        </div>

        <button onClick={() => generateCloud(spreadAngle)} className="btn btn-secondary btn-sm">
          <Sparkles size={14} /> New Point Cloud
        </button>
      </div>

      <div style={{ display: 'grid', gridTemplateColumns: '1.4fr 1fr', gap: 20, marginBottom: 20 }}>
        {/* SVG PCA Plot */}
        <div style={{ background: '#070a13', borderRadius: 'var(--radius-md)', padding: 12, border: '1px solid var(--border-subtle)', height: '340px' }}>
          <svg width="100%" height="100%" viewBox="0 0 200 200">
            {/* Grid */}
            <line x1="100" y1="10" x2="100" y2="190" stroke="#1e293b" strokeDasharray="3 3" />
            <line x1="10" y1="100" x2="190" y2="100" stroke="#1e293b" strokeDasharray="3 3" />

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
                  strokeWidth="0.8"
                  strokeDasharray="2 2"
                  strokeOpacity="0.4"
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
                fill="#38bdf8"
                stroke="#0284c7"
                strokeWidth="1"
              />
            ))}

            {/* PC1 Eigenvector Arrow */}
            <line
              x1={mean.x - v1.x * 55}
              y1={mean.y - v1.y * 55}
              x2={mean.x + v1.x * 55}
              y2={mean.y + v1.y * 55}
              stroke="#6366f1"
              strokeWidth="2.5"
            />

            {/* PC2 Eigenvector Arrow */}
            <line
              x1={mean.x - v2.x * 25}
              y1={mean.y - v2.y * 25}
              x2={mean.x + v2.x * 25}
              y2={mean.y + v2.y * 25}
              stroke="#ec4899"
              strokeWidth="2"
            />

            {/* Mean Center */}
            <circle cx={mean.x} cy={mean.y} r="5" fill="#ffffff" stroke="#6366f1" strokeWidth="2" />
          </svg>
        </div>

        {/* Variance Explained & Controls */}
        <div style={{ display: 'flex', flexDirection: 'column', gap: 14 }}>
          {/* Variance Breakdown Card */}
          <div style={{ background: 'var(--bg-secondary)', padding: 16, borderRadius: 'var(--radius-md)', border: '1px solid var(--border-subtle)' }}>
            <div style={{ fontSize: '0.75rem', color: 'var(--text-muted)', textTransform: 'uppercase', marginBottom: 8, fontWeight: 700 }}>
              Explained Variance Ratio
            </div>

            <div style={{ marginBottom: 12 }}>
              <div style={{ display: 'flex', justifyContent: 'space-between', fontSize: '0.85rem', marginBottom: 4 }}>
                <span style={{ color: '#6366f1', fontWeight: 600 }}>PC1 (Principal Direction)</span>
                <b>{pc1VarRatio}%</b>
              </div>
              <ProgressBar percentage={pc1VarRatio} color="#6366f1" height={8} />
            </div>

            <div>
              <div style={{ display: 'flex', justifyContent: 'space-between', fontSize: '0.85rem', marginBottom: 4 }}>
                <span style={{ color: '#ec4899', fontWeight: 600 }}>PC2 (Orthogonal Axis)</span>
                <b>{100 - pc1VarRatio}%</b>
              </div>
              <ProgressBar percentage={100 - pc1VarRatio} color="#ec4899" height={8} />
            </div>
          </div>

          {/* Cloud Rotation Angle Slider */}
          <div style={{ background: 'var(--bg-secondary)', padding: 16, borderRadius: 'var(--radius-md)', border: '1px solid var(--border-subtle)', display: 'flex', flexDirection: 'column', gap: 12 }}>
            <div>
              <div style={{ display: 'flex', justifyContent: 'space-between', fontSize: '0.825rem', marginBottom: 6 }}>
                <span>Data Correlation Angle: <b>{spreadAngle}°</b></span>
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

            <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
              <input
                type="checkbox"
                id="showProj"
                checked={showProjection}
                onChange={(e) => setShowProjection(e.target.checked)}
              />
              <label htmlFor="showProj" style={{ fontSize: '0.85rem', color: 'var(--text-secondary)', cursor: 'pointer' }}>
                Show 1D Orthogonal Projections (Yellow)
              </label>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
