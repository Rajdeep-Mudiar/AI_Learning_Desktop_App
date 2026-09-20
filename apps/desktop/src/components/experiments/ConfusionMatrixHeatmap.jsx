import React from 'react';

export default function ConfusionMatrixHeatmap({ data }) {
  if (!data || !data.matrix || !data.matrix.length) {
    return (
      <div style={{ padding: 'var(--space-md)', textAlign: 'center', color: 'var(--color-text-muted)' }}>
        No confusion matrix data available.
      </div>
    );
  }

  const { labels, matrix } = data;
  const numClasses = labels.length;

  // Compute maximum cell value for heat intensity normalization
  let maxVal = 1;
  let totalSamples = 0;
  for (let r = 0; r < numClasses; r++) {
    for (let c = 0; c < numClasses; c++) {
      const val = matrix[r][c] || 0;
      if (val > maxVal) maxVal = val;
      totalSamples += val;
    }
  }

  return (
    <div style={{ display: 'flex', flexDirection: 'column', gap: 'var(--space-md)' }}>
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
        <div>
          <h4 style={{ margin: 0, fontSize: 'var(--font-sm)', fontWeight: 600, color: 'var(--color-text-main)' }}>
            Confusion Matrix
          </h4>
          <span style={{ fontSize: 'var(--font-xs)', color: 'var(--color-text-muted)' }}>
            Total Test Samples: {totalSamples}
          </span>
        </div>
        <div style={{ display: 'flex', alignItems: 'center', gap: 'var(--space-xs)', fontSize: 'var(--font-xs)', color: 'var(--color-text-muted)' }}>
          <span>Low</span>
          <div style={{ width: '40px', height: '10px', borderRadius: 'var(--radius-full)', background: 'linear-gradient(to right, rgba(99, 102, 241, 0.1), rgba(99, 102, 241, 0.9))' }} />
          <span>High</span>
        </div>
      </div>

      <div style={{ overflowX: 'auto', padding: 'var(--space-xs)' }}>
        <table style={{ borderCollapse: 'collapse', width: '100%', minWidth: '320px', textAlign: 'center' }}>
          <thead>
            <tr>
              <th style={{ padding: '6px', fontSize: 'var(--font-xs)', color: 'var(--color-text-muted)', borderBottom: '1px solid var(--color-border)' }}>
                True \ Pred
              </th>
              {labels.map((lbl, idx) => (
                <th key={idx} style={{ padding: '6px', fontSize: 'var(--font-xs)', color: 'var(--color-primary-400)', fontWeight: 600, borderBottom: '1px solid var(--color-border)' }}>
                  {lbl}
                </th>
              ))}
            </tr>
          </thead>
          <tbody>
            {matrix.map((row, rIdx) => {
              const rowTotal = row.reduce((a, b) => a + b, 0);
              return (
                <tr key={rIdx}>
                  <td style={{ padding: '6px', fontSize: 'var(--font-xs)', fontWeight: 600, color: 'var(--color-text-main)', borderRight: '1px solid var(--color-border)', textAlign: 'right', paddingRight: '12px' }}>
                    {labels[rIdx]}
                  </td>
                  {row.map((val, cIdx) => {
                    const isDiagonal = rIdx === cIdx;
                    const ratio = maxVal > 0 ? val / maxVal : 0;
                    const bg = isDiagonal
                      ? `rgba(16, 185, 129, ${Math.max(0.12, ratio * 0.85)})`
                      : ratio > 0
                      ? `rgba(239, 68, 68, ${Math.max(0.1, ratio * 0.7)})`
                      : 'rgba(255, 255, 255, 0.02)';
                    
                    const textColor = ratio > 0.4 ? '#ffffff' : 'var(--color-text-main)';

                    return (
                      <td
                        key={cIdx}
                        title={`True: ${labels[rIdx]}, Pred: ${labels[cIdx]} (${val} samples)`}
                        style={{
                          padding: '10px 6px',
                          background: bg,
                          color: textColor,
                          fontWeight: isDiagonal ? 700 : 500,
                          fontSize: 'var(--font-sm)',
                          border: '1px solid var(--color-border)',
                          borderRadius: 'var(--radius-sm)',
                          transition: 'transform 0.15s ease',
                          cursor: 'default',
                        }}
                      >
                        {val}
                        <div style={{ fontSize: '10px', opacity: 0.75, fontWeight: 400 }}>
                          {rowTotal > 0 ? `${Math.round((val / rowTotal) * 100)}%` : '0%'}
                        </div>
                      </td>
                    );
                  })}
                </tr>
              );
            })}
          </tbody>
        </table>
      </div>
    </div>
  );
}
