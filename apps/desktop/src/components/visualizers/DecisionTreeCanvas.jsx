import React, { useState } from 'react';
import { GitBranch, Sliders, Layers, Sparkles } from 'lucide-react';

export default function DecisionTreeCanvas() {
  const [maxDepth, setMaxDepth] = useState(2);
  const [criterion, setCriterion] = useState('gini'); // 'gini' or 'entropy'
  const [featureSplitVal, setFeatureSplitVal] = useState(4.5);

  // Total samples: 50 Class A (Red), 50 Class B (Blue)
  const totalA = 50;
  const totalB = 50;
  const totalN = totalA + totalB;

  // Split calculations based on featureSplitVal (range 1.0 to 9.0)
  const leftA = Math.round(Math.min(50, Math.max(0, (featureSplitVal / 10) * 80)));
  const leftB = Math.round(Math.min(50, Math.max(0, (featureSplitVal / 10) * 20)));
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
      // Gini = 1 - (pA^2 + pB^2)
      return parseFloat((1.0 - (pA ** 2 + pB ** 2)).toFixed(3));
    } else {
      // Entropy = - pA log2(pA) - pB log2(pB)
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
    <div className="card" style={{ padding: 24 }}>
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: 18 }}>
        <div>
          <h2 style={{ fontSize: '1.25rem', marginBottom: 4 }}>Decision Tree Split & Information Gain Visualizer</h2>
          <p style={{ fontSize: '0.85rem', color: 'var(--text-secondary)' }}>
            Adjust the feature split threshold to see how Information Gain and Gini Impurity dynamically change.
          </p>
        </div>
      </div>

      <div style={{ display: 'grid', gridTemplateColumns: '1.4fr 1fr', gap: 20, marginBottom: 20 }}>
        {/* Interactive Tree Graph Visualization */}
        <div style={{ background: '#070a13', borderRadius: 'var(--radius-md)', padding: 20, border: '1px solid var(--border-subtle)', display: 'flex', flexDirection: 'column', alignItems: 'center', minHeight: '340px' }}>
          {/* Root Node */}
          <div style={{
            background: 'var(--bg-tertiary)',
            border: '2px solid var(--accent-primary)',
            borderRadius: 'var(--radius-md)',
            padding: '12px 18px',
            textAlign: 'center',
            minWidth: '200px',
            boxShadow: '0 4px 12px rgba(99, 102, 241, 0.25)'
          }}>
            <div style={{ fontSize: '0.85rem', fontWeight: 700, color: 'var(--text-primary)', marginBottom: 4 }}>
              Feature X ≤ {featureSplitVal}
            </div>
            <div style={{ fontSize: '0.75rem', color: 'var(--text-muted)' }}>
              {criterion === 'gini' ? 'Gini' : 'Entropy'}: <b>{parentImpurity}</b>
            </div>
            <div style={{ fontSize: '0.725rem', color: 'var(--text-secondary)', marginTop: 2 }}>
              Samples: {totalN} [Red: {totalA}, Blue: {totalB}]
            </div>
          </div>

          {/* SVG Split Connecting Lines */}
          <svg width="320" height="60" viewBox="0 0 320 60">
            <line x1="160" y1="0" x2="80" y2="55" stroke="var(--border-subtle)" strokeWidth="2" />
            <line x1="160" y1="0" x2="240" y2="55" stroke="var(--border-subtle)" strokeWidth="2" />
            <text x="95" y="24" fill="#34d399" fontSize="10" fontWeight="bold">True</text>
            <text x="210" y="24" fill="#f87171" fontSize="10" fontWeight="bold">False</text>
          </svg>

          {/* Child Nodes (Depth 1) */}
          <div style={{ display: 'flex', gap: 40 }}>
            {/* Left Leaf */}
            <div style={{
              background: leftA >= leftB ? 'rgba(239, 68, 68, 0.15)' : 'rgba(59, 130, 246, 0.15)',
              border: `1.5px solid ${leftA >= leftB ? '#ef4444' : '#3b82f6'}`,
              borderRadius: 'var(--radius-md)',
              padding: '10px 14px',
              textAlign: 'center',
              minWidth: '130px'
            }}>
              <div style={{ fontSize: '0.78rem', fontWeight: 700, color: leftA >= leftB ? '#f87171' : '#60a5fa' }}>
                Class: {leftA >= leftB ? 'Red' : 'Blue'}
              </div>
              <div style={{ fontSize: '0.72rem', color: 'var(--text-muted)' }}>
                {criterion === 'gini' ? 'Gini' : 'Entropy'}: <b>{leftImpurity}</b>
              </div>
              <div style={{ fontSize: '0.7rem', color: 'var(--text-secondary)' }}>
                [{leftA}, {leftB}] (N={leftN})
              </div>
            </div>

            {/* Right Leaf */}
            <div style={{
              background: rightA >= rightB ? 'rgba(239, 68, 68, 0.15)' : 'rgba(59, 130, 246, 0.15)',
              border: `1.5px solid ${rightA >= rightB ? '#ef4444' : '#3b82f6'}`,
              borderRadius: 'var(--radius-md)',
              padding: '10px 14px',
              textAlign: 'center',
              minWidth: '130px'
            }}>
              <div style={{ fontSize: '0.78rem', fontWeight: 700, color: rightA >= rightB ? '#f87171' : '#60a5fa' }}>
                Class: {rightA >= rightB ? 'Red' : 'Blue'}
              </div>
              <div style={{ fontSize: '0.72rem', color: 'var(--text-muted)' }}>
                {criterion === 'gini' ? 'Gini' : 'Entropy'}: <b>{rightImpurity}</b>
              </div>
              <div style={{ fontSize: '0.7rem', color: 'var(--text-secondary)' }}>
                [{rightA}, {rightB}] (N={rightN})
              </div>
            </div>
          </div>
        </div>

        {/* Mathematical Formulas & Controls */}
        <div style={{ display: 'flex', flexDirection: 'column', gap: 14 }}>
          {/* Information Gain Metric */}
          <div style={{ background: 'var(--bg-secondary)', padding: 16, borderRadius: 'var(--radius-md)', border: '1px solid var(--border-subtle)' }}>
            <div style={{ fontSize: '0.75rem', color: 'var(--text-muted)', textTransform: 'uppercase', marginBottom: 4 }}>
              Information Gain (IG)
            </div>
            <div style={{ fontSize: '1.6rem', fontWeight: 800, color: '#34d399' }}>
              +{infoGain}
            </div>
            <p style={{ fontSize: '0.75rem', color: 'var(--text-secondary)', marginTop: 4 }}>
              Higher Information Gain represents a cleaner separation between classes.
            </p>
          </div>

          {/* Controls */}
          <div style={{ background: 'var(--bg-secondary)', padding: 16, borderRadius: 'var(--radius-md)', border: '1px solid var(--border-subtle)', display: 'flex', flexDirection: 'column', gap: 14 }}>
            <div>
              <div style={{ display: 'flex', justifyContent: 'space-between', fontSize: '0.825rem', marginBottom: 6 }}>
                <span>Feature Split Threshold (X ≤ v): <b>{featureSplitVal}</b></span>
              </div>
              <input
                type="range"
                min="1.0"
                max="9.0"
                step="0.5"
                value={featureSplitVal}
                onChange={(e) => setFeatureSplitVal(parseFloat(e.target.value))}
                style={{ width: '100%' }}
              />
            </div>

            <div>
              <label className="form-label">Impurity Criterion</label>
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
          </div>
        </div>
      </div>
    </div>
  );
}
