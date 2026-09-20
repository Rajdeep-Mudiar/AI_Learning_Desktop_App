import React, { useState } from 'react';

export default function TransformerAttentionVisualizer({
  data,
  sentence,
  onSentenceChange,
  numHeads,
  onNumHeadsChange,
  onCompute,
  loading,
}) {
  const [selectedHeadIdx, setSelectedHeadIdx] = useState(0); // 0 = Average, 1..N = specific head
  const [hoveredTokenIdx, setHoveredTokenIdx] = useState(null);

  if (!data) return null;

  const { tokens = [], heads = [], average_attention = [], formula_explanation = '' } = data;
  const numTokens = tokens.length;

  // Determine active matrix to display
  let activeMatrix = average_attention;
  if (selectedHeadIdx > 0 && heads[selectedHeadIdx - 1]) {
    activeMatrix = heads[selectedHeadIdx - 1].attention_weights;
  }

  const PRESET_SENTENCES = [
    "The transformer model calculates attention weights across tokens",
    "The animal did not cross the street because it was tired",
    "Self attention enables parallel processing of contextual sequences",
    "Antigravity neural network visualizer deep learning laboratory",
  ];

  return (
    <div style={{ display: 'flex', flexDirection: 'column', gap: 'var(--space-lg)' }}>
      {/* Input & Config Card */}
      <div className="card" style={{ padding: 'var(--space-md)', display: 'flex', flexDirection: 'column', gap: 'var(--space-md)' }}>
        <div style={{ display: 'flex', gap: 'var(--space-md)', alignItems: 'center' }}>
          <div style={{ flex: 1 }}>
            <label style={{ fontSize: '11px', color: 'var(--color-text-muted)', display: 'block', marginBottom: '2px' }}>
              Input Sentence for Tokenization & Self-Attention
            </label>
            <input
              type="text"
              className="input"
              value={sentence}
              onChange={(e) => onSentenceChange(e.target.value)}
              placeholder="Enter sentence..."
              style={{ width: '100%' }}
            />
          </div>
          <div>
            <label style={{ fontSize: '11px', color: 'var(--color-text-muted)', display: 'block', marginBottom: '2px' }}>
              Attention Heads
            </label>
            <select
              className="input"
              value={numHeads}
              onChange={(e) => onNumHeadsChange(parseInt(e.target.value))}
              style={{ fontSize: 'var(--font-xs)' }}
            >
              <option value={2}>2 Heads</option>
              <option value={4}>4 Heads</option>
              <option value={8}>8 Heads</option>
            </select>
          </div>
          <button
            onClick={onCompute}
            disabled={loading}
            className="btn btn-primary"
            style={{ marginTop: '16px', padding: '8px 16px', fontSize: 'var(--font-xs)', fontWeight: 700 }}
          >
            {loading ? 'Computing...' : '⚡ Compute Attention'}
          </button>
        </div>

        {/* Preset sentence chips */}
        <div style={{ display: 'flex', gap: 'var(--space-xs)', flexWrap: 'wrap', alignItems: 'center' }}>
          <span style={{ fontSize: '11px', color: 'var(--color-text-muted)' }}>Presets:</span>
          {PRESET_SENTENCES.map((preset, idx) => (
            <button
              key={idx}
              onClick={() => {
                onSentenceChange(preset);
              }}
              style={{
                background: 'var(--color-surface-elevated)',
                border: '1px solid var(--color-border)',
                borderRadius: 'var(--radius-full)',
                padding: '2px 10px',
                fontSize: '11px',
                color: 'var(--color-text-main)',
                cursor: 'pointer',
              }}
            >
              {preset.slice(0, 32)}...
            </button>
          ))}
        </div>
      </div>

      {/* Head Selection Tabs */}
      <div style={{ display: 'flex', gap: 'var(--space-xs)', borderBottom: '1px solid var(--color-border)', paddingBottom: 'var(--space-xs)' }}>
        <button
          onClick={() => setSelectedHeadIdx(0)}
          style={{
            background: selectedHeadIdx === 0 ? 'rgba(99, 102, 241, 0.15)' : 'none',
            border: selectedHeadIdx === 0 ? '1px solid var(--color-primary-400)' : '1px solid transparent',
            color: selectedHeadIdx === 0 ? 'var(--color-primary-400)' : 'var(--color-text-muted)',
            borderRadius: 'var(--radius-sm)',
            padding: '4px 12px',
            fontSize: 'var(--font-xs)',
            fontWeight: selectedHeadIdx === 0 ? 700 : 500,
            cursor: 'pointer',
          }}
        >
          🌐 Multi-Head Average
        </button>
        {heads.map((h) => (
          <button
            key={h.head_idx}
            onClick={() => setSelectedHeadIdx(h.head_idx)}
            style={{
              background: selectedHeadIdx === h.head_idx ? 'rgba(99, 102, 241, 0.15)' : 'none',
              border: selectedHeadIdx === h.head_idx ? '1px solid var(--color-primary-400)' : '1px solid transparent',
              color: selectedHeadIdx === h.head_idx ? 'var(--color-primary-400)' : 'var(--color-text-muted)',
              borderRadius: 'var(--radius-sm)',
              padding: '4px 12px',
              fontSize: 'var(--font-xs)',
              fontWeight: selectedHeadIdx === h.head_idx ? 700 : 500,
              cursor: 'pointer',
            }}
          >
            Head #{h.head_idx}
          </button>
        ))}
      </div>

      {/* Main Attention Matrix Visualizer */}
      <div style={{ display: 'grid', gridTemplateColumns: '1fr 340px', gap: 'var(--space-lg)', alignItems: 'start' }}>
        
        {/* NxN Heatmap Matrix */}
        <div className="card" style={{ padding: 'var(--space-lg)', overflowX: 'auto' }}>
          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: 'var(--space-sm)' }}>
            <h4 style={{ margin: 0, fontSize: 'var(--font-sm)', color: 'var(--color-text-main)' }}>
              Self-Attention Weight Matrix A = Softmax(Q Kᵀ / √dₖ)
            </h4>
            <span style={{ fontSize: '11px', color: 'var(--color-text-muted)' }}>
              Rows: Query Tokens (Q) • Cols: Key Tokens (K)
            </span>
          </div>

          <table style={{ borderCollapse: 'collapse', textAlign: 'center', fontSize: '11px', minWidth: `${numTokens * 40 + 80}px` }}>
            <thead>
              <tr>
                <th style={{ padding: '6px', borderBottom: '1px solid var(--color-border)', textAlign: 'right' }}>Q \ K</th>
                {tokens.map((tok, idx) => (
                  <th
                    key={idx}
                    style={{
                      padding: '6px 8px',
                      borderBottom: '1px solid var(--color-border)',
                      color: hoveredTokenIdx === idx ? '#f59e0b' : 'var(--color-primary-400)',
                      fontWeight: 600,
                      maxWidth: '70px',
                      overflow: 'hidden',
                      textOverflow: 'ellipsis',
                      whiteSpace: 'nowrap',
                    }}
                    title={tok}
                  >
                    {tok}
                  </th>
                ))}
              </tr>
            </thead>
            <tbody>
              {activeMatrix.map((row, rIdx) => (
                <tr key={rIdx}>
                  <td
                    style={{
                      padding: '6px 10px',
                      fontWeight: 600,
                      textAlign: 'right',
                      borderRight: '1px solid var(--color-border)',
                      color: hoveredTokenIdx === rIdx ? '#f59e0b' : 'var(--color-text-main)',
                      maxWidth: '80px',
                      overflow: 'hidden',
                      textOverflow: 'ellipsis',
                      whiteSpace: 'nowrap',
                    }}
                    title={tokens[rIdx]}
                  >
                    {tokens[rIdx]}
                  </td>
                  {row.map((weight, cIdx) => {
                    const isDiagonal = rIdx === cIdx;
                    const isHoveredRow = hoveredTokenIdx === rIdx;
                    const isHoveredCol = hoveredTokenIdx === cIdx;
                    
                    // Heatmap color intensity
                    const bg = `rgba(99, 102, 241, ${Math.max(0.04, weight * 0.9)})`;
                    const textColor = weight > 0.4 ? '#ffffff' : 'var(--color-text-main)';

                    return (
                      <td
                        key={cIdx}
                        onMouseEnter={() => setHoveredTokenIdx(rIdx)}
                        onMouseLeave={() => setHoveredTokenIdx(null)}
                        title={`Query: "${tokens[rIdx]}" attends to Key: "${tokens[cIdx]}" with weight ${weight}`}
                        style={{
                          padding: '8px 4px',
                          background: bg,
                          color: textColor,
                          fontWeight: isDiagonal ? 700 : 500,
                          border: isHoveredRow && isHoveredCol ? '1.5px solid #f59e0b' : '1px solid var(--color-border)',
                          cursor: 'default',
                        }}
                      >
                        {weight.toFixed(2)}
                      </td>
                    );
                  })}
                </tr>
              ))}
            </tbody>
          </table>
        </div>

        {/* Token-to-Token Attention Flow Inspector */}
        <div className="card" style={{ padding: 'var(--space-md)', display: 'flex', flexDirection: 'column', gap: 'var(--space-md)' }}>
          <h4 style={{ margin: 0, fontSize: 'var(--font-sm)', color: 'var(--color-text-main)' }}>
            Contextual Attention Breakdown
          </h4>

          {hoveredTokenIdx !== null && activeMatrix[hoveredTokenIdx] ? (
            <div style={{ display: 'flex', flexDirection: 'column', gap: 'var(--space-sm)' }}>
              <div style={{ fontSize: 'var(--font-xs)', color: 'var(--color-text-muted)' }}>
                Top Attended Keys for query <strong>"{tokens[hoveredTokenIdx]}"</strong>:
              </div>
              {tokens.map((tok, idx) => {
                const w = activeMatrix[hoveredTokenIdx][idx] || 0;
                return (
                  <div key={idx} style={{ display: 'flex', alignItems: 'center', gap: 'var(--space-xs)', fontSize: '11px' }}>
                    <span style={{ minWidth: '70px', overflow: 'hidden', textOverflow: 'ellipsis', whiteSpace: 'nowrap' }}>
                      ➜ {tok}
                    </span>
                    <div style={{ flex: 1, height: '6px', background: 'var(--color-surface-elevated)', borderRadius: 'var(--radius-full)', overflow: 'hidden' }}>
                      <div
                        style={{
                          height: '100%',
                          width: `${Math.round(w * 100)}%`,
                          background: 'var(--color-primary-400)',
                          borderRadius: 'var(--radius-full)',
                        }}
                      />
                    </div>
                    <span style={{ minWidth: '32px', textAlign: 'right', fontFamily: 'var(--font-mono)' }}>
                      {(w * 100).toFixed(0)}%
                    </span>
                  </div>
                );
              })}
            </div>
          ) : (
            <div style={{ padding: 'var(--space-lg)', textAlign: 'center', color: 'var(--color-text-muted)', fontSize: 'var(--font-xs)' }}>
              Hover over any token in the matrix to inspect its full attention distribution arc.
            </div>
          )}

          <div style={{ padding: 'var(--space-sm)', background: 'var(--color-surface-elevated)', borderRadius: 'var(--radius-sm)', fontSize: '11px', color: 'var(--color-text-muted)' }}>
            {formula_explanation}
          </div>
        </div>
      </div>
    </div>
  );
}
