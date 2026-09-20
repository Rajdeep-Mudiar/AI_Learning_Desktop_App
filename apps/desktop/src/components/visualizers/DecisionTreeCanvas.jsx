import React, { useState, useEffect } from 'react';
import { GitBranch, Sliders, Layers, Sparkles, Maximize2, Minimize2 } from 'lucide-react';

export default function DecisionTreeCanvas() {
  const [maxDepth, setMaxDepth] = useState(2);
  const [criterion, setCriterion] = useState('gini');
  const [featureSplitVal, setFeatureSplitVal] = useState(4.5);
  const [totalA, setTotalA] = useState(50);
  const [totalB, setTotalB] = useState(50);
  const [isFullscreen, setIsFullscreen] = useState(false);

  useEffect(() => {
    const handleKeyDown = (e) => {
      if (e.key === 'Escape' && isFullscreen) setIsFullscreen(false);
    };
    window.addEventListener('keydown', handleKeyDown);
    return () => window.removeEventListener('keydown', handleKeyDown);
  }, [isFullscreen]);

  const totalN = totalA + totalB;

  // Split calculations based on featureSplitVal (range 1.0 to 9.0)
  const leftA = Math.round(Math.min(totalA, Math.max(0, (featureSplitVal / 10) * (totalA * 1.6))));
  const leftB = Math.round(Math.min(totalB, Math.max(0, (featureSplitVal / 10) * (totalB * 0.4))));
  const leftN = Math.max(1, leftA + leftB);

  const rightA = totalA - leftA;
  const rightB = totalB - leftB;
  const rightN = Math.max(1, rightA + rightB);

  // Compute Impurity Functions
  const computeImpurity = (countA, countB) => {
    const total = countA + countB;
    if (total === 0) return 0.0;
    const pA = countA / total;
    const pB = countB / total;

    if (criterion === 'gini') {
      return parseFloat((1.0 - (pA ** 2 + pB ** 2)).toFixed(3));
    } else {
      const eA = pA > 0 ? pA * Math.log2(pA) : 0;
      const eB = pB > 0 ? pB * Math.log2(pB) : 0;
      return parseFloat((- (eA + eB)).toFixed(3));
    }
  };

  const parentImpurity = computeImpurity(totalA, totalB);
  const leftImpurity = computeImpurity(leftA, leftB);
  const rightImpurity = computeImpurity(rightA, rightB);

  // Information Gain
  const infoGain = parseFloat((
    parentImpurity - ((leftN / totalN) * leftImpurity + (rightN / totalN) * rightImpurity)
  ).toFixed(3));

  return (
    <div className={`card ${isFullscreen ? 'simulation-fullscreen-overlay' : ''}`} style={{ padding: isFullscreen ? 32 : 24 }}>
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', marginBottom: 18, flexWrap: 'wrap', gap: 12 }}>
        <div>
          <div style={{ display: 'flex', alignItems: 'center', gap: 10, marginBottom: 4 }}>
            <h2 style={{ fontSize: isFullscreen ? '1.5rem' : '1.25rem' }}>
              Decision Tree Split & Information Gain Visualizer
            </h2>
            {isFullscreen && <span className="badge badge-purple">Fullscreen View</span>}
          </div>
          <p style={{ fontSize: '0.85rem', color: 'var(--text-secondary)' }}>
            Adjust the feature split threshold to observe how Information Gain and Gini Impurity dynamically change.
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
          <button onClick={() => { setTotalA(50); setTotalB(50); setFeatureSplitVal(4.5); }} className="btn btn-secondary btn-sm">
            Reset Distribution
          </button>
        </div>
      </div>

      <div style={{ display: 'grid', gridTemplateColumns: isFullscreen ? '1.5fr 1fr' : '1.4fr 1fr', gap: 20, marginBottom: 20 }}>
        {/* Tree Graph Visualization */}
        <div 
          className="simulation-canvas-container" 
          style={{ padding: 24, display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center', minHeight: isFullscreen ? '420px' : '340px' }}
        >
          {/* Root Node */}
          <div style={{
            background: 'var(--bg-tertiary)',
            border: '2px solid var(--accent-primary)',
            borderRadius: 'var(--radius-md)',
            padding: '12px 20px',
            textAlign: 'center',
            minWidth: '220px',
            boxShadow: 'var(--shadow-md)'
          }}>
            <div style={{ fontSize: '0.9rem', fontWeight: 700, color: 'var(--text-primary)', marginBottom: 4 }}>
              Feature X ≤ {featureSplitVal}
            </div>
            <div style={{ fontSize: '0.75rem', color: 'var(--text-muted)' }}>
              {criterion === 'gini' ? 'Gini Impurity' : 'Entropy'}: <b>{parentImpurity}</b>
            </div>
            <div style={{ fontSize: '0.725rem', color: 'var(--text-secondary)', marginTop: 2 }}>
              Total Samples: {totalN} [Red: {totalA}, Blue: {totalB}]
            </div>
          </div>

          {/* Connecting Lines */}
          <svg width="340" height="70" viewBox="0 0 340 70">
            <line x1="170" y1="0" x2="85" y2="65" stroke="var(--canvas-grid)" strokeWidth="2.5" />
            <line x1="170" y1="0" x2="255" y2="65" stroke="var(--canvas-grid)" strokeWidth="2.5" />
            <rect x="75" y="24" width="40" height="20" rx="4" fill="var(--bg-card)" stroke="var(--border-subtle)" />
            <text x="95" y="38" fill="var(--accent-success)" fontSize="11" fontWeight="bold" textAnchor="middle">True</text>
            <rect x="225" y="24" width="45" height="20" rx="4" fill="var(--bg-card)" stroke="var(--border-subtle)" />
            <text x="247" y="38" fill="var(--accent-danger)" fontSize="11" fontWeight="bold" textAnchor="middle">False</text>
          </svg>

          {/* Child Nodes */}
          <div style={{ display: 'flex', gap: 36 }}>
            {/* Left Leaf */}
            <div style={{
              background: 'var(--bg-tertiary)',
              border: `2px solid ${leftA >= leftB ? '#ef4444' : '#3b82f6'}`,
              borderRadius: 'var(--radius-md)',
              padding: '12px 16px',
              textAlign: 'center',
              minWidth: '140px',
              boxShadow: 'var(--shadow-sm)'
            }}>
              <div style={{ fontSize: '0.825rem', fontWeight: 700, color: leftA >= leftB ? '#ef4444' : '#3b82f6' }}>
                Majority: {leftA >= leftB ? 'Class Red' : 'Class Blue'}
              </div>
              <div style={{ fontSize: '0.75rem', color: 'var(--text-muted)', marginTop: 2 }}>
                {criterion === 'gini' ? 'Gini' : 'Entropy'}: <b>{leftImpurity}</b>
              </div>
              <div style={{ fontSize: '0.72rem', color: 'var(--text-secondary)', marginTop: 2 }}>
                [{leftA} Red, {leftB} Blue] (N={leftN})
              </div>
            </div>

            {/* Right Leaf */}
            <div style={{
              background: 'var(--bg-tertiary)',
              border: `2px solid ${rightA >= rightB ? '#ef4444' : '#3b82f6'}`,
              borderRadius: 'var(--radius-md)',
              padding: '12px 16px',
              textAlign: 'center',
              minWidth: '140px',
              boxShadow: 'var(--shadow-sm)'
            }}>
              <div style={{ fontSize: '0.825rem', fontWeight: 700, color: rightA >= rightB ? '#ef4444' : '#3b82f6' }}>
                Majority: {rightA >= rightB ? 'Class Red' : 'Class Blue'}
              </div>
              <div style={{ fontSize: '0.75rem', color: 'var(--text-muted)', marginTop: 2 }}>
                {criterion === 'gini' ? 'Gini' : 'Entropy'}: <b>{rightImpurity}</b>
              </div>
              <div style={{ fontSize: '0.72rem', color: 'var(--text-secondary)', marginTop: 2 }}>
                [{rightA} Red, {rightB} Blue] (N={rightN})
              </div>
            </div>
          </div>
        </div>

        {/* Mathematical Formulas & Controls */}
        <div style={{ display: 'flex', flexDirection: 'column', gap: 14 }}>
          {/* Information Gain Metric */}
          <div style={{ background: 'var(--bg-secondary)', padding: 16, borderRadius: 'var(--radius-md)', border: '1px solid var(--border-subtle)' }}>
            <div style={{ fontSize: '0.75rem', color: 'var(--text-muted)', textTransform: 'uppercase', marginBottom: 4, fontWeight: 700 }}>
              Information Gain (IG)
            </div>
            <div style={{ fontSize: '1.8rem', fontWeight: 800, color: 'var(--accent-success)' }}>
              +{infoGain}
            </div>
            <p style={{ fontSize: '0.75rem', color: 'var(--text-secondary)', marginTop: 4 }}>
              Higher Information Gain represents a purer partitioning between target classes.
            </p>
          </div>

          {/* Split Slider */}
          <div style={{ background: 'var(--bg-secondary)', padding: 16, borderRadius: 'var(--radius-md)', border: '1px solid var(--border-subtle)', display: 'flex', flexDirection: 'column', gap: 14 }}>
            <div>
              <div style={{ display: 'flex', justifyContent: 'space-between', fontSize: '0.825rem', marginBottom: 6 }}>
                <span>Split Threshold (X ≤ θ): <b>{featureSplitVal}</b></span>
              </div>
              <input
                type="range"
                min="1.0"
                max="9.0"
                step="0.1"
                value={featureSplitVal}
                onChange={(e) => setFeatureSplitVal(parseFloat(e.target.value))}
                style={{ width: '100%' }}
              />
            </div>

            <div>
              <label className="form-label" style={{ fontSize: '0.8rem' }}>Split Criterion</label>
              <div style={{ display: 'flex', gap: 8 }}>
                <button
                  onClick={() => setCriterion('gini')}
                  className={criterion === 'gini' ? 'btn btn-primary btn-sm' : 'btn btn-secondary btn-sm'}
                  style={{ flex: 1 }}
                >
                  Gini Impurity
                </button>
                <button
                  onClick={() => setCriterion('entropy')}
                  className={criterion === 'entropy' ? 'btn btn-primary btn-sm' : 'btn btn-secondary btn-sm'}
                  style={{ flex: 1 }}
                >
                  Shannon Entropy
                </button>
              </div>
            </div>

            <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: 10 }}>
              <div>
                <span style={{ fontSize: '0.72rem', color: 'var(--text-muted)' }}>Class A Samples</span>
                <input 
                  type="number" 
                  min="10" 
                  max="100" 
                  value={totalA} 
                  onChange={(e) => setTotalA(parseInt(e.target.value) || 10)}
                  className="form-input" 
                  style={{ padding: '4px 8px', fontSize: '0.8rem', marginTop: 4 }}
                />
              </div>
              <div>
                <span style={{ fontSize: '0.72rem', color: 'var(--text-muted)' }}>Class B Samples</span>
                <input 
                  type="number" 
                  min="10" 
                  max="100" 
                  value={totalB} 
                  onChange={(e) => setTotalB(parseInt(e.target.value) || 10)}
                  className="form-input" 
                  style={{ padding: '4px 8px', fontSize: '0.8rem', marginTop: 4 }}
                />
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
