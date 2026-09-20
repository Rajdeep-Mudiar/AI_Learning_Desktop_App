import React, { useState, useEffect, useRef } from 'react';
import { Play, Pause, RotateCcw, StepForward, Sliders, Sparkles, TrendingUp } from 'lucide-react';
import { simulationService } from '../../services/simulationService';

export default function LinearRegressionCanvas() {
  const [points, setPoints] = useState([
    { x: 1.0, y: 2.2 },
    { x: 2.0, y: 3.8 },
    { x: 3.0, y: 4.9 },
    { x: 4.0, y: 7.1 },
    { x: 5.0, y: 8.5 },
    { x: 6.0, y: 10.2 },
    { x: 7.0, y: 12.4 },
    { x: 8.0, y: 13.9 },
  ]);

  const [weight, setWeight] = useState(0.0);
  const [bias, setBias] = useState(0.0);
  const [learningRate, setLearningRate] = useState(0.03);
  const [epoch, setEpoch] = useState(0);
  const [mse, setMse] = useState(0.0);
  const [gradientW, setGradientW] = useState(0.0);
  const [gradientB, setGradientB] = useState(0.0);
  const [isPlaying, setIsPlaying] = useState(false);
  const [lossHistory, setLossHistory] = useState([]);

  const isPlayingRef = useRef(isPlaying);
  isPlayingRef.current = isPlaying;

  // Generate synthetic dataset
  const handleGenerateData = (noiseLevel = 1.0) => {
    const newPts = [];
    const trueW = 1.6;
    const trueB = 2.0;
    for (let x = 1; x <= 10; x++) {
      const noise = (Math.random() - 0.5) * 2 * noiseLevel;
      newPts.push({ x, y: parseFloat((trueW * x + trueB + noise).toFixed(2)) });
    }
    setPoints(newPts);
    handleReset();
  };

  const handleReset = () => {
    setIsPlaying(false);
    setWeight(0.0);
    setBias(0.0);
    setEpoch(0);
    setLossHistory([]);
    computeMetrics(0.0, 0.0, points);
  };

  const computeMetrics = (w, b, pts) => {
    const N = pts.length || 1;
    let totalSq = 0;
    pts.forEach((p) => {
      const pred = w * p.x + b;
      totalSq += (pred - p.y) ** 2;
    });
    setMse(parseFloat((totalSq / N).toFixed(4)));
  };

  const stepOptimizer = async (currentW = weight, currentB = bias, currentPts = points) => {
    try {
      const res = await simulationService.stepLinearRegression(
        currentPts,
        currentW,
        currentB,
        learningRate
      );
      setWeight(res.new_weight);
      setBias(res.new_bias);
      setMse(res.mse_loss);
      setGradientW(res.gradient_w);
      setGradientB(res.gradient_b);
      setEpoch((prev) => prev + 1);
      setLossHistory((prev) => [...prev.slice(-30), res.mse_loss]);
      return { w: res.new_weight, b: res.new_bias };
    } catch (err) {
      console.error('Step error:', err);
      setIsPlaying(false);
    }
  };

  // Animation Loop
  useEffect(() => {
    let timer;
    if (isPlaying) {
      timer = setInterval(async () => {
        if (!isPlayingRef.current) return;
        await stepOptimizer();
      }, 80);
    }
    return () => clearInterval(timer);
  }, [isPlaying, weight, bias, points, learningRate]);

  // Canvas dimensions
  const svgWidth = 500;
  const svgHeight = 320;
  const padding = 40;

  const scaleX = (val) => padding + (val / 11) * (svgWidth - padding * 2);
  const scaleY = (val) => svgHeight - padding - (val / 20) * (svgHeight - padding * 2);

  // SVG Line endpoints (x=0 to x=10)
  const lineX1 = scaleX(0);
  const lineY1 = scaleY(weight * 0 + bias);
  const lineX2 = scaleX(10);
  const lineY2 = scaleY(weight * 10 + bias);

  return (
    <div className="card" style={{ padding: 24 }}>
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: 18 }}>
        <div>
          <h2 style={{ fontSize: '1.25rem', marginBottom: 4 }}>Interactive Linear Regression & Gradient Descent</h2>
          <p style={{ fontSize: '0.85rem', color: 'var(--text-secondary)' }}>
            Watch the optimizer navigate the loss surface to find optimal parameter weights $\mathbf{w}$ and bias $b$.
          </p>
        </div>

        <div style={{ display: 'flex', gap: 8 }}>
          <button onClick={() => handleGenerateData(1.2)} className="btn btn-secondary btn-sm">
            <Sparkles size={14} /> New Dataset
          </button>
          <button onClick={handleReset} className="btn btn-secondary btn-sm">
            <RotateCcw size={14} /> Reset
          </button>
        </div>
      </div>

      {/* Main Simulation Viewport */}
      <div style={{ display: 'grid', gridTemplateColumns: '1.4fr 1fr', gap: 20, marginBottom: 20 }}>
        {/* SVG Plot Canvas */}
        <div style={{ background: '#070a13', borderRadius: 'var(--radius-md)', padding: 12, border: '1px solid var(--border-subtle)', position: 'relative' }}>
          <svg width="100%" height={svgHeight} viewBox={`0 0 ${svgWidth} ${svgHeight}`}>
            {/* Grid & Axes */}
            <line x1={padding} y1={svgHeight - padding} x2={svgWidth - padding} y2={svgHeight - padding} stroke="#1e293b" strokeWidth="1.5" />
            <line x1={padding} y1={padding} x2={padding} y2={svgHeight - padding} stroke="#1e293b" strokeWidth="1.5" />

            {/* Grid lines */}
            {[5, 10, 15].map((val) => (
              <line key={val} x1={padding} y1={scaleY(val)} x2={svgWidth - padding} y2={scaleY(val)} stroke="#1e293b" strokeDasharray="3 3" />
            ))}

            {/* Residual Lines */}
            {points.map((pt, i) => {
              const predY = weight * pt.x + bias;
              return (
                <line
                  key={`res-${i}`}
                  x1={scaleX(pt.x)}
                  y1={scaleY(pt.y)}
                  x2={scaleX(pt.x)}
                  y2={scaleY(predY)}
                  stroke="#ef4444"
                  strokeWidth="1.5"
                  strokeDasharray="2 2"
                />
              );
            })}

            {/* Regression Line */}
            <line
              x1={lineX1}
              y1={lineY1}
              x2={lineX2}
              y2={lineY2}
              stroke="#6366f1"
              strokeWidth="3.5"
              strokeLinecap="round"
            />

            {/* Data Points */}
            {points.map((pt, i) => (
              <circle
                key={i}
                cx={scaleX(pt.x)}
                cy={scaleY(pt.y)}
                r="6"
                fill="#38bdf8"
                stroke="#0284c7"
                strokeWidth="1.5"
              />
            ))}

            {/* Axis labels */}
            <text x={svgWidth / 2} y={svgHeight - 10} fill="#64748b" fontSize="11" textAnchor="middle">Feature X</text>
            <text x={15} y={svgHeight / 2} fill="#64748b" fontSize="11" textAnchor="middle" transform={`rotate(-90 15, ${svgHeight / 2})`}>Target Y</text>
          </svg>
        </div>

        {/* Real-time Math & Metrics telemetry */}
        <div style={{ display: 'flex', flexDirection: 'column', gap: 14 }}>
          <div style={{ background: 'var(--bg-secondary)', padding: 16, borderRadius: 'var(--radius-md)', border: '1px solid var(--border-subtle)' }}>
            <div style={{ fontSize: '0.75rem', color: 'var(--text-muted)', textTransform: 'uppercase', marginBottom: 8, fontWeight: 700 }}>
              Live Telemetry (Epoch {epoch})
            </div>

            <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: 10 }}>
              <div>
                <span style={{ fontSize: '0.75rem', color: 'var(--text-muted)' }}>MSE Loss</span>
                <div style={{ fontSize: '1.25rem', fontWeight: 800, color: '#f43f5e' }}>{mse}</div>
              </div>
              <div>
                <span style={{ fontSize: '0.75rem', color: 'var(--text-muted)' }}>Weight (w)</span>
                <div style={{ fontSize: '1.25rem', fontWeight: 800, color: '#6366f1' }}>{weight}</div>
              </div>
              <div>
                <span style={{ fontSize: '0.75rem', color: 'var(--text-muted)' }}>Bias (b)</span>
                <div style={{ fontSize: '1.1rem', fontWeight: 700, color: '#38bdf8' }}>{bias}</div>
              </div>
              <div>
                <span style={{ fontSize: '0.75rem', color: 'var(--text-muted)' }}>Gradient ∂L/∂w</span>
                <div style={{ fontSize: '1.1rem', fontWeight: 700, color: '#fbbf24' }}>{gradientW}</div>
              </div>
            </div>
          </div>

          {/* Loss Curve Mini Sparkline */}
          <div style={{ background: 'var(--bg-secondary)', padding: 14, borderRadius: 'var(--radius-md)', border: '1px solid var(--border-subtle)' }}>
            <div style={{ fontSize: '0.75rem', color: 'var(--text-muted)', marginBottom: 6 }}>Loss Convergence History</div>
            <div style={{ height: 40, display: 'flex', alignItems: 'flex-end', gap: 3 }}>
              {lossHistory.map((val, idx) => {
                const maxL = Math.max(...lossHistory, 1);
                const h = Math.max(4, (val / maxL) * 36);
                return (
                  <div
                    key={idx}
                    style={{
                      flex: 1,
                      height: `${h}px`,
                      background: 'rgba(99, 102, 241, 0.6)',
                      borderRadius: 2
                    }}
                  />
                );
              })}
            </div>
          </div>
        </div>
      </div>

      {/* Control Sliders & Playback */}
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', background: 'var(--bg-secondary)', padding: 16, borderRadius: 'var(--radius-md)', border: '1px solid var(--border-subtle)', flexWrap: 'wrap', gap: 16 }}>
        {/* Playback Buttons */}
        <div style={{ display: 'flex', gap: 8 }}>
          <button
            onClick={() => setIsPlaying(!isPlaying)}
            className="btn btn-primary"
            style={{ padding: '8px 18px' }}
          >
            {isPlaying ? <Pause size={16} /> : <Play size={16} />}
            <span>{isPlaying ? 'Pause Training' : 'Train (Animate)'}</span>
          </button>

          <button onClick={() => stepOptimizer()} className="btn btn-secondary" disabled={isPlaying}>
            <StepForward size={16} /> Step
          </button>
        </div>

        {/* Hyperparameter Controls */}
        <div style={{ display: 'flex', alignItems: 'center', gap: 20 }}>
          <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
            <span style={{ fontSize: '0.8rem', color: 'var(--text-secondary)' }}>Learning Rate (α):</span>
            <input
              type="range"
              min="0.005"
              max="0.1"
              step="0.005"
              value={learningRate}
              onChange={(e) => setLearningRate(parseFloat(e.target.value))}
              style={{ width: 100 }}
            />
            <span style={{ fontSize: '0.8rem', fontWeight: 700, minWidth: 36 }}>{learningRate}</span>
          </div>
        </div>
      </div>
    </div>
  );
}
