import React, { useState, useEffect, useRef } from 'react';
import { 
  Play, Pause, RotateCcw, StepForward, Sliders, Sparkles, 
  TrendingUp, Maximize2, Minimize2, Plus, Trash2, Table, 
  MousePointer, HelpCircle, Layers, ShieldAlert 
} from 'lucide-react';
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

  // Advanced features
  const [isFullscreen, setIsFullscreen] = useState(false);
  const [showDataTable, setShowDataTable] = useState(false);
  const [manualX, setManualX] = useState('5.5');
  const [manualY, setManualY] = useState('9.0');
  const [mouseCoord, setMouseCoord] = useState(null);
  const [pointCountPreset, setPointCountPreset] = useState(20);
  const [noiseLevel, setNoiseLevel] = useState(1.2);

  const isPlayingRef = useRef(isPlaying);
  isPlayingRef.current = isPlaying;
  const svgRef = useRef(null);

  // Keyboard shortcut for Fullscreen exit
  useEffect(() => {
    const handleKeyDown = (e) => {
      if (e.key === 'Escape' && isFullscreen) {
        setIsFullscreen(false);
      }
    };
    window.addEventListener('keydown', handleKeyDown);
    return () => window.removeEventListener('keydown', handleKeyDown);
  }, [isFullscreen]);

  // Compute initial metrics
  useEffect(() => {
    computeMetrics(weight, bias, points);
  }, [points]);

  // Generate synthetic dataset with customizable density & noise
  const handleGenerateData = (count = pointCountPreset, noise = noiseLevel, presetType = 'linear') => {
    const newPts = [];
    if (presetType === 'linear') {
      const trueW = 1.6;
      const trueB = 2.0;
      for (let i = 0; i < count; i++) {
        const xVal = parseFloat((1 + (i / Math.max(1, count - 1)) * 9).toFixed(2));
        const noiseVal = (Math.random() - 0.5) * 2 * noise;
        const yVal = Math.max(0.5, Math.min(19.5, parseFloat((trueW * xVal + trueB + noiseVal).toFixed(2))));
        newPts.push({ x: xVal, y: yVal });
      }
    } else if (presetType === 'outliers') {
      const trueW = 1.4;
      const trueB = 3.0;
      for (let i = 0; i < count; i++) {
        const xVal = parseFloat((1 + (i / Math.max(1, count - 1)) * 9).toFixed(2));
        let noiseVal = (Math.random() - 0.5) * 1.5;
        // Inject 3 severe outliers
        if (i === Math.floor(count * 0.3)) noiseVal += 7.0;
        if (i === Math.floor(count * 0.7)) noiseVal -= 6.0;
        if (i === Math.floor(count * 0.9)) noiseVal += 6.5;
        const yVal = Math.max(0.5, Math.min(19.5, parseFloat((trueW * xVal + trueB + noiseVal).toFixed(2))));
        newPts.push({ x: xVal, y: yVal });
      }
    } else if (presetType === 'steep') {
      const trueW = 2.2;
      const trueB = 0.5;
      for (let i = 0; i < count; i++) {
        const xVal = parseFloat((0.8 + (i / Math.max(1, count - 1)) * 7.5).toFixed(2));
        const noiseVal = (Math.random() - 0.5) * 1.8;
        const yVal = Math.max(0.5, Math.min(19.5, parseFloat((trueW * xVal + trueB + noiseVal).toFixed(2))));
        newPts.push({ x: xVal, y: yVal });
      }
    } else if (presetType === 'flat') {
      const trueW = 0.1;
      const trueB = 10.0;
      for (let i = 0; i < count; i++) {
        const xVal = parseFloat((1 + (i / Math.max(1, count - 1)) * 9).toFixed(2));
        const noiseVal = (Math.random() - 0.5) * 2.5;
        const yVal = Math.max(0.5, Math.min(19.5, parseFloat((trueW * xVal + trueB + noiseVal).toFixed(2))));
        newPts.push({ x: xVal, y: yVal });
      }
    }
    setPoints(newPts);
    handleReset(newPts);
  };

  const handleReset = (currentPts = points) => {
    setIsPlaying(false);
    setWeight(0.0);
    setBias(0.0);
    setEpoch(0);
    setLossHistory([]);
    computeMetrics(0.0, 0.0, currentPts);
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
    if (currentPts.length === 0) return;
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
      setLossHistory((prev) => [...prev.slice(-40), res.mse_loss]);
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
      }, 70);
    }
    return () => clearInterval(timer);
  }, [isPlaying, weight, bias, points, learningRate]);

  // Canvas coordinate math
  const svgWidth = isFullscreen ? 800 : 540;
  const svgHeight = isFullscreen ? 420 : 320;
  const padding = 45;

  const maxX = 11;
  const maxY = 20;

  const scaleX = (val) => padding + (val / maxX) * (svgWidth - padding * 2);
  const scaleY = (val) => svgHeight - padding - (val / maxY) * (svgHeight - padding * 2);

  const unscaleX = (pixelX) => {
    const raw = ((pixelX - padding) / (svgWidth - padding * 2)) * maxX;
    return Math.max(0.2, Math.min(maxX, parseFloat(raw.toFixed(2))));
  };

  const unscaleY = (pixelY) => {
    const raw = ((svgHeight - padding - pixelY) / (svgHeight - padding * 2)) * maxY;
    return Math.max(0.2, Math.min(maxY, parseFloat(raw.toFixed(2))));
  };

  // SVG Line endpoints
  const lineX1 = scaleX(0);
  const lineY1 = scaleY(weight * 0 + bias);
  const lineX2 = scaleX(maxX);
  const lineY2 = scaleY(weight * maxX + bias);

  // Canvas Click to add point directly
  const handleCanvasClick = (e) => {
    if (!svgRef.current) return;
    const rect = svgRef.current.getBoundingClientRect();
    const clickX = ((e.clientX - rect.left) / rect.width) * svgWidth;
    const clickY = ((e.clientY - rect.top) / rect.height) * svgHeight;

    if (clickX >= padding - 10 && clickX <= svgWidth - padding + 10 &&
        clickY >= padding - 10 && clickY <= svgHeight - padding + 10) {
      const x = unscaleX(clickX);
      const y = unscaleY(clickY);
      setPoints((prev) => [...prev, { x, y }]);
    }
  };

  const handleCanvasMouseMove = (e) => {
    if (!svgRef.current) return;
    const rect = svgRef.current.getBoundingClientRect();
    const curX = ((e.clientX - rect.left) / rect.width) * svgWidth;
    const curY = ((e.clientY - rect.top) / rect.height) * svgHeight;

    if (curX >= padding && curX <= svgWidth - padding &&
        curY >= padding && curY <= svgHeight - padding) {
      setMouseCoord({
        x: unscaleX(curX),
        y: unscaleY(curY),
        pixelX: curX,
        pixelY: curY
      });
    } else {
      setMouseCoord(null);
    }
  };

  const handleAddManualPoint = (e) => {
    e?.preventDefault();
    const x = parseFloat(manualX);
    const y = parseFloat(manualY);
    if (!isNaN(x) && !isNaN(y)) {
      setPoints((prev) => [...prev, { x, y }]);
      setManualX((prev) => (Math.min(10, parseFloat(prev) + 1)).toFixed(1));
    }
  };

  const handleRemovePoint = (index) => {
    setPoints((prev) => prev.filter((_, idx) => idx !== index));
  };

  const handleClearAll = () => {
    setPoints([]);
    handleReset([]);
  };

  return (
    <div className={`card ${isFullscreen ? 'simulation-fullscreen-overlay' : ''}`} style={{ padding: isFullscreen ? 32 : 24 }}>
      {/* Header with Title & Fullscreen Toggle */}
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', marginBottom: 18, flexWrap: 'wrap', gap: 12 }}>
        <div>
          <div style={{ display: 'flex', alignItems: 'center', gap: 10, marginBottom: 4 }}>
            <h2 style={{ fontSize: isFullscreen ? '1.5rem' : '1.25rem' }}>
              Interactive Linear Regression & Gradient Descent
            </h2>
            {isFullscreen && (
              <span className="badge badge-purple">
                Fullscreen Simulation Mode
              </span>
            )}
          </div>
          <p style={{ fontSize: '0.85rem', color: 'var(--text-secondary)' }}>
            Click anywhere inside the coordinate plane to plot custom datapoints, adjust parameters, and watch the regression line converge.
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
          <button onClick={() => handleGenerateData(pointCountPreset, noiseLevel, 'linear')} className="btn btn-secondary btn-sm">
            <Sparkles size={14} /> Reset Points
          </button>
          <button onClick={() => handleReset()} className="btn btn-secondary btn-sm">
            <RotateCcw size={14} /> Zero Weights
          </button>
        </div>
      </div>

      {/* Dataset Presets & Manual Point Addition Bar */}
      <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', background: 'var(--bg-secondary)', padding: '10px 16px', borderRadius: 'var(--radius-md)', border: '1px solid var(--border-subtle)', marginBottom: 16, flexWrap: 'wrap', gap: 12 }}>
        {/* Preset Buttons */}
        <div style={{ display: 'flex', alignItems: 'center', gap: 6, flexWrap: 'wrap' }}>
          <span style={{ fontSize: '0.75rem', fontWeight: 700, color: 'var(--text-muted)', textTransform: 'uppercase', marginRight: 4 }}>
            Presets:
          </span>
          <button onClick={() => handleGenerateData(8, 1.0, 'linear')} className="btn btn-ghost btn-sm" style={{ border: '1px solid var(--border-subtle)' }}>
            8 Standard
          </button>
          <button onClick={() => handleGenerateData(30, 1.2, 'linear')} className="btn btn-ghost btn-sm" style={{ border: '1px solid var(--border-subtle)' }}>
            30 Dense Cloud
          </button>
          <button onClick={() => handleGenerateData(16, 1.5, 'outliers')} className="btn btn-ghost btn-sm" style={{ border: '1px solid var(--border-subtle)' }}>
            <ShieldAlert size={12} color="var(--accent-warning)" /> Outliers
          </button>
          <button onClick={() => handleGenerateData(15, 1.0, 'steep')} className="btn btn-ghost btn-sm" style={{ border: '1px solid var(--border-subtle)' }}>
            Steep Slope
          </button>
        </div>

        {/* Manual Point Input */}
        <form onSubmit={handleAddManualPoint} style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
          <span style={{ fontSize: '0.78rem', color: 'var(--text-secondary)' }}>Add Point:</span>
          <div style={{ display: 'flex', alignItems: 'center', gap: 4 }}>
            <span style={{ fontSize: '0.75rem', color: 'var(--text-muted)' }}>X:</span>
            <input 
              type="number" 
              step="0.1" 
              min="0" 
              max="11" 
              value={manualX} 
              onChange={(e) => setManualX(e.target.value)}
              className="form-input"
              style={{ width: 64, padding: '4px 8px', fontSize: '0.8rem' }}
            />
          </div>
          <div style={{ display: 'flex', alignItems: 'center', gap: 4 }}>
            <span style={{ fontSize: '0.75rem', color: 'var(--text-muted)' }}>Y:</span>
            <input 
              type="number" 
              step="0.1" 
              min="0" 
              max="20" 
              value={manualY} 
              onChange={(e) => setManualY(e.target.value)}
              className="form-input"
              style={{ width: 64, padding: '4px 8px', fontSize: '0.8rem' }}
            />
          </div>
          <button type="submit" className="btn btn-secondary btn-sm" style={{ padding: '5px 10px' }}>
            <Plus size={14} /> Add
          </button>
          <button 
            type="button" 
            onClick={() => setShowDataTable(!showDataTable)} 
            className={`btn btn-sm ${showDataTable ? 'btn-primary' : 'btn-secondary'}`}
            style={{ padding: '5px 10px' }}
          >
            <Table size={14} /> Points ({points.length})
          </button>
        </form>
      </div>

      {/* Main Simulation Viewport */}
      <div style={{ display: 'grid', gridTemplateColumns: isFullscreen ? '1.8fr 1fr' : '1.4fr 1fr', gap: 20, marginBottom: 20 }}>
        {/* Interactive SVG Plot Canvas */}
        <div 
          className="simulation-canvas-container" 
          style={{ cursor: 'crosshair', userSelect: 'none' }}
        >
          <svg 
            ref={svgRef}
            width="100%" 
            height={svgHeight} 
            viewBox={`0 0 ${svgWidth} ${svgHeight}`}
            onClick={handleCanvasClick}
            onMouseMove={handleCanvasMouseMove}
            onMouseLeave={() => setMouseCoord(null)}
          >
            {/* Grid background lines */}
            {[2, 4, 6, 8, 10].map((val) => (
              <line key={`gx-${val}`} x1={scaleX(val)} y1={padding} x2={scaleX(val)} y2={svgHeight - padding} stroke="var(--canvas-grid)" strokeDasharray="3 3" strokeWidth="1" />
            ))}
            {[5, 10, 15].map((val) => (
              <line key={`gy-${val}`} x1={padding} y1={scaleY(val)} x2={svgWidth - padding} y2={scaleY(val)} stroke="var(--canvas-grid)" strokeDasharray="3 3" strokeWidth="1" />
            ))}

            {/* Axes */}
            <line x1={padding} y1={svgHeight - padding} x2={svgWidth - padding} y2={svgHeight - padding} stroke="var(--canvas-axis)" strokeWidth="1.5" />
            <line x1={padding} y1={padding} x2={padding} y2={svgHeight - padding} stroke="var(--canvas-axis)" strokeWidth="1.5" />

            {/* Residual error lines */}
            {points.map((pt, i) => {
              const predY = weight * pt.x + bias;
              return (
                <line
                  key={`res-${i}`}
                  x1={scaleX(pt.x)}
                  y1={scaleY(pt.y)}
                  x2={scaleX(pt.x)}
                  y2={scaleY(predY)}
                  stroke="var(--accent-danger)"
                  strokeWidth="1.5"
                  strokeDasharray="2 2"
                />
              );
            })}

            {/* Fitted Regression Line */}
            <line
              x1={lineX1}
              y1={lineY1}
              x2={lineX2}
              y2={lineY2}
              stroke="var(--canvas-line)"
              strokeWidth="3.5"
              strokeLinecap="round"
            />

            {/* Data Points */}
            {points.map((pt, i) => (
              <g key={i} style={{ cursor: 'pointer' }} onClick={(e) => { e.stopPropagation(); handleRemovePoint(i); }}>
                <circle
                  cx={scaleX(pt.x)}
                  cy={scaleY(pt.y)}
                  r="6.5"
                  fill="var(--canvas-point)"
                  stroke="var(--canvas-point-stroke)"
                  strokeWidth="2"
                />
                <title>{`Point #${i + 1}: (X=${pt.x}, Y=${pt.y})\nClick to delete point`}</title>
              </g>
            ))}

            {/* Live Hover Crosshair Indicator */}
            {mouseCoord && (
              <g pointerEvents="none">
                <line x1={mouseCoord.pixelX} y1={padding} x2={mouseCoord.pixelX} y2={svgHeight - padding} stroke="var(--canvas-crosshair)" strokeDasharray="2 2" />
                <line x1={padding} y1={mouseCoord.pixelY} x2={svgWidth - padding} y2={mouseCoord.pixelY} stroke="var(--canvas-crosshair)" strokeDasharray="2 2" />
                <circle cx={mouseCoord.pixelX} cy={mouseCoord.pixelY} r="4" fill="var(--accent-primary)" />
                <rect x={Math.min(svgWidth - 110, mouseCoord.pixelX + 10)} y={Math.max(10, mouseCoord.pixelY - 24)} width="95" height="20" rx="4" fill="var(--bg-card)" stroke="var(--border-strong)" />
                <text x={Math.min(svgWidth - 110, mouseCoord.pixelX + 10) + 48} y={Math.max(10, mouseCoord.pixelY - 24) + 14} fill="var(--text-primary)" fontSize="10" fontWeight="600" textAnchor="middle">
                  {`(${mouseCoord.x}, ${mouseCoord.y})`}
                </text>
              </g>
            )}

            {/* Axis labels & tick marks */}
            {[0, 2, 4, 6, 8, 10].map((val) => (
              <text key={`tx-${val}`} x={scaleX(val)} y={svgHeight - padding + 16} fill="var(--canvas-subtext)" fontSize="10" textAnchor="middle">{val}</text>
            ))}
            {[0, 5, 10, 15, 20].map((val) => (
              <text key={`ty-${val}`} x={padding - 10} y={scaleY(val) + 3} fill="var(--canvas-subtext)" fontSize="10" textAnchor="end">{val}</text>
            ))}

            <text x={svgWidth / 2} y={svgHeight - 6} fill="var(--canvas-text)" fontSize="11" fontWeight="600" textAnchor="middle">Feature X</text>
            <text x={12} y={svgHeight / 2} fill="var(--canvas-text)" fontSize="11" fontWeight="600" textAnchor="middle" transform={`rotate(-90 12, ${svgHeight / 2})`}>Target Y</text>
          </svg>

          {/* Click to add helper watermark */}
          <div style={{ position: 'absolute', bottom: 12, right: 16, fontSize: '0.72rem', color: 'var(--text-muted)', display: 'flex', alignItems: 'center', gap: 4, pointerEvents: 'none' }}>
            <MousePointer size={12} /> Click canvas to add datapoint
          </div>
        </div>

        {/* Real-time Telemetry & Convergence */}
        <div style={{ display: 'flex', flexDirection: 'column', gap: 14 }}>
          <div style={{ background: 'var(--bg-secondary)', padding: 16, borderRadius: 'var(--radius-md)', border: '1px solid var(--border-subtle)' }}>
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: 12 }}>
              <span style={{ fontSize: '0.75rem', color: 'var(--text-muted)', textTransform: 'uppercase', fontWeight: 700 }}>
                Live Model Telemetry (Epoch {epoch})
              </span>
              <span className="badge badge-blue">{points.length} Points Loaded</span>
            </div>

            <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: 12 }}>
              <div style={{ background: 'var(--bg-tertiary)', padding: 10, borderRadius: 'var(--radius-sm)', border: '1px solid var(--border-subtle)' }}>
                <span style={{ fontSize: '0.72rem', color: 'var(--text-muted)' }}>MSE Loss (Mean Sq Error)</span>
                <div style={{ fontSize: '1.3rem', fontWeight: 800, color: 'var(--accent-danger)' }}>{mse}</div>
              </div>
              <div style={{ background: 'var(--bg-tertiary)', padding: 10, borderRadius: 'var(--radius-sm)', border: '1px solid var(--border-subtle)' }}>
                <span style={{ fontSize: '0.72rem', color: 'var(--text-muted)' }}>Weight Slope (w)</span>
                <div style={{ fontSize: '1.3rem', fontWeight: 800, color: 'var(--accent-primary)' }}>{weight}</div>
              </div>
              <div style={{ background: 'var(--bg-tertiary)', padding: 10, borderRadius: 'var(--radius-sm)', border: '1px solid var(--border-subtle)' }}>
                <span style={{ fontSize: '0.72rem', color: 'var(--text-muted)' }}>Bias Intercept (b)</span>
                <div style={{ fontSize: '1.15rem', fontWeight: 700, color: 'var(--accent-secondary)' }}>{bias}</div>
              </div>
              <div style={{ background: 'var(--bg-tertiary)', padding: 10, borderRadius: 'var(--radius-sm)', border: '1px solid var(--border-subtle)' }}>
                <span style={{ fontSize: '0.72rem', color: 'var(--text-muted)' }}>Gradient ∂L/∂w</span>
                <div style={{ fontSize: '1.15rem', fontWeight: 700, color: 'var(--accent-warning)' }}>{gradientW}</div>
              </div>
            </div>
          </div>

          {/* Loss Curve Mini Sparkline */}
          <div style={{ background: 'var(--bg-secondary)', padding: 14, borderRadius: 'var(--radius-md)', border: '1px solid var(--border-subtle)' }}>
            <div style={{ display: 'flex', justifyContent: 'space-between', marginBottom: 8 }}>
              <span style={{ fontSize: '0.75rem', color: 'var(--text-muted)', fontWeight: 600 }}>Loss Convergence Curve</span>
              <span style={{ fontSize: '0.72rem', color: 'var(--text-secondary)' }}>{lossHistory.length} Steps</span>
            </div>
            <div style={{ height: 48, display: 'flex', alignItems: 'flex-end', gap: 2, background: 'var(--bg-tertiary)', padding: '6px 8px', borderRadius: 'var(--radius-sm)' }}>
              {lossHistory.length === 0 ? (
                <div style={{ width: '100%', height: '100%', display: 'flex', alignItems: 'center', justifyContent: 'center', fontSize: '0.75rem', color: 'var(--text-muted)' }}>
                  Click "Train" to begin optimization
                </div>
              ) : (
                lossHistory.map((val, idx) => {
                  const maxL = Math.max(...lossHistory, 1);
                  const h = Math.max(4, (val / maxL) * 36);
                  return (
                    <div
                      key={idx}
                      title={`Step ${idx + 1}: Loss ${val}`}
                      style={{
                        flex: 1,
                        height: `${h}px`,
                        background: 'linear-gradient(180deg, var(--accent-primary-light) 0%, var(--accent-primary) 100%)',
                        borderRadius: 2
                      }}
                    />
                  );
                })
              )}
            </div>
          </div>

          {/* Dataset Density & Noise Generator */}
          <div style={{ background: 'var(--bg-secondary)', padding: 12, borderRadius: 'var(--radius-md)', border: '1px solid var(--border-subtle)' }}>
            <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', marginBottom: 6 }}>
              <span style={{ fontSize: '0.75rem', color: 'var(--text-secondary)', fontWeight: 600 }}>Batch Points Generator</span>
              <span style={{ fontSize: '0.75rem', fontWeight: 700 }}>{pointCountPreset} Points · ±{noiseLevel} Noise</span>
            </div>
            <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: 12 }}>
              <div>
                <input 
                  type="range" 
                  min="5" 
                  max="60" 
                  step="5" 
                  value={pointCountPreset} 
                  onChange={(e) => setPointCountPreset(parseInt(e.target.value))}
                  style={{ width: '100%' }}
                />
              </div>
              <div>
                <input 
                  type="range" 
                  min="0.2" 
                  max="4.0" 
                  step="0.2" 
                  value={noiseLevel} 
                  onChange={(e) => setNoiseLevel(parseFloat(e.target.value))}
                  style={{ width: '100%' }}
                />
              </div>
            </div>
          </div>
        </div>
      </div>

      {/* Points Data Table (Collapsible) */}
      {showDataTable && (
        <div style={{ marginBottom: 20 }} className="animate-fade-in">
          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: 8 }}>
            <span style={{ fontSize: '0.85rem', fontWeight: 700 }}>Active Datapoints Table ({points.length} samples)</span>
            <button onClick={handleClearAll} className="btn btn-ghost btn-sm" style={{ color: 'var(--accent-danger)' }}>
              <Trash2 size={13} /> Clear All Points
            </button>
          </div>
          <div className="datapoints-table-container">
            <table className="datapoints-table">
              <thead>
                <tr>
                  <th>#</th>
                  <th>Feature (X)</th>
                  <th>Target (Y)</th>
                  <th>Model Prediction (ŷ)</th>
                  <th>Residual Error (ŷ - Y)</th>
                  <th>Squared Error (ŷ - Y)²</th>
                  <th style={{ textAlign: 'right' }}>Action</th>
                </tr>
              </thead>
              <tbody>
                {points.length === 0 ? (
                  <tr>
                    <td colSpan="7" style={{ textAlign: 'center', padding: '16px', color: 'var(--text-muted)' }}>
                      No datapoints loaded. Click on the canvas or use the "Add Point" form above!
                    </td>
                  </tr>
                ) : (
                  points.map((pt, i) => {
                    const pred = parseFloat((weight * pt.x + bias).toFixed(2));
                    const res = parseFloat((pred - pt.y).toFixed(2));
                    const sq = parseFloat((res ** 2).toFixed(2));
                    return (
                      <tr key={i}>
                        <td style={{ color: 'var(--text-muted)' }}>{i + 1}</td>
                        <td style={{ fontWeight: 600 }}>{pt.x}</td>
                        <td style={{ fontWeight: 600 }}>{pt.y}</td>
                        <td style={{ color: 'var(--accent-primary-light)' }}>{pred}</td>
                        <td style={{ color: res > 0 ? 'var(--accent-warning)' : 'var(--accent-secondary)' }}>{res > 0 ? `+${res}` : res}</td>
                        <td style={{ color: 'var(--accent-danger)' }}>{sq}</td>
                        <td style={{ textAlign: 'right' }}>
                          <button 
                            onClick={() => handleRemovePoint(i)} 
                            className="btn btn-ghost btn-sm"
                            style={{ padding: '2px 6px', color: 'var(--text-muted)' }}
                            title="Delete this point"
                          >
                            <Trash2 size={13} />
                          </button>
                        </td>
                      </tr>
                    );
                  })
                )}
              </tbody>
            </table>
          </div>
        </div>
      )}

      {/* Control Sliders & Playback */}
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', background: 'var(--bg-secondary)', padding: 16, borderRadius: 'var(--radius-md)', border: '1px solid var(--border-subtle)', flexWrap: 'wrap', gap: 16 }}>
        {/* Playback Buttons */}
        <div style={{ display: 'flex', gap: 8 }}>
          <button
            onClick={() => setIsPlaying(!isPlaying)}
            className="btn btn-primary"
            style={{ padding: '8px 20px' }}
          >
            {isPlaying ? <Pause size={16} /> : <Play size={16} />}
            <span>{isPlaying ? 'Pause Training' : 'Train (Gradient Descent)'}</span>
          </button>

          <button onClick={() => stepOptimizer()} className="btn btn-secondary" disabled={isPlaying}>
            <StepForward size={16} /> Step 1 Epoch
          </button>
        </div>

        {/* Hyperparameter Controls */}
        <div style={{ display: 'flex', alignItems: 'center', gap: 24, flexWrap: 'wrap' }}>
          <div style={{ display: 'flex', alignItems: 'center', gap: 10 }}>
            <span style={{ fontSize: '0.825rem', color: 'var(--text-secondary)' }}>Learning Rate (α):</span>
            <input
              type="range"
              min="0.005"
              max="0.1"
              step="0.005"
              value={learningRate}
              onChange={(e) => setLearningRate(parseFloat(e.target.value))}
              style={{ width: 120 }}
            />
            <span style={{ fontSize: '0.825rem', fontWeight: 700, minWidth: 36, color: 'var(--accent-primary-light)' }}>{learningRate}</span>
          </div>

          <div style={{ display: 'flex', alignItems: 'center', gap: 10 }}>
            <span style={{ fontSize: '0.825rem', color: 'var(--text-secondary)' }}>Manual Weight (w):</span>
            <input
              type="range"
              min="-2.0"
              max="4.0"
              step="0.05"
              value={weight}
              onChange={(e) => {
                const w = parseFloat(e.target.value);
                setWeight(w);
                computeMetrics(w, bias, points);
              }}
              style={{ width: 100 }}
            />
            <span style={{ fontSize: '0.825rem', fontWeight: 700, minWidth: 36 }}>{weight}</span>
          </div>
        </div>
      </div>
    </div>
  );
}
