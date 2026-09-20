import React, { useState } from 'react';

export default function CNNKernelVisualizer({
  data,
  selectedKernel,
  onKernelChange,
  poolingType,
  onPoolingChange,
  stride,
  onStrideChange,
}) {
  const [hoveredCell, setHoveredCell] = useState({ r: 4, c: 4 }); // coordinate in feature map

  if (!data) return null;

  const { kernel = [], input_matrix = [], feature_map = [], pooled_map = [], formula_explanation = '' } = data;

  const kSize = kernel.length || 3;
  const inRows = input_matrix.length || 14;
  const inCols = input_matrix[0]?.length || 14;
  const fRows = feature_map.length || 12;
  const fCols = feature_map[0]?.length || 12;

  // Compute active receptive field patch in input matrix
  const patchR = (hoveredCell.r || 0) * stride;
  const patchC = (hoveredCell.c || 0) * stride;

  // Extract values in active receptive field
  const receptiveFieldPatch = [];
  let dotProductSum = 0;
  for (let kr = 0; kr < kSize; kr++) {
    const rowVals = [];
    for (let kc = 0; kc < kSize; kc++) {
      const ir = patchR + kr;
      const ic = patchC + kc;
      const inVal = ir < inRows && ic < inCols ? input_matrix[ir][ic] : 0;
      const kVal = kernel[kr][kc] || 0;
      dotProductSum += inVal * kVal;
      rowVals.push({ inVal, kVal, prod: inVal * kVal });
    }
    receptiveFieldPatch.push(rowVals);
  }
  const reluOut = Math.max(0, dotProductSum);

  return (
    <div style={{ display: 'flex', flexDirection: 'column', gap: 'var(--space-lg)' }}>
      {/* Controls toolbar */}
      <div className="card" style={{ padding: 'var(--space-md)', display: 'flex', gap: 'var(--space-lg)', flexWrap: 'wrap', alignItems: 'center' }}>
        <div>
          <label style={{ fontSize: '11px', color: 'var(--color-text-muted)', display: 'block', marginBottom: '2px' }}>Kernel Filter</label>
          <select className="input" value={selectedKernel} onChange={(e) => onKernelChange(e.target.value)} style={{ fontSize: 'var(--font-xs)', minWidth: '160px' }}>
            <option value="sobel_horizontal">Sobel Horizontal (dI/dy)</option>
            <option value="sobel_vertical">Sobel Vertical (dI/dx)</option>
            <option value="edge_detect">Laplacian Edge Detection</option>
            <option value="sharpen">Sharpening Filter</option>
            <option value="gaussian_blur">Gaussian Blur (Smoothing)</option>
            <option value="ridge">Ridge Detection</option>
          </select>
        </div>

        <div>
          <label style={{ fontSize: '11px', color: 'var(--color-text-muted)', display: 'block', marginBottom: '2px' }}>Downsampling Pooling</label>
          <select className="input" value={poolingType} onChange={(e) => onPoolingChange(e.target.value)} style={{ fontSize: 'var(--font-xs)' }}>
            <option value="max">2x2 Max Pooling</option>
            <option value="average">2x2 Average Pooling</option>
            <option value="none">None (Raw Feature Map)</option>
          </select>
        </div>

        <div>
          <label style={{ fontSize: '11px', color: 'var(--color-text-muted)', display: 'block', marginBottom: '2px' }}>Stride</label>
          <select className="input" value={stride} onChange={(e) => onStrideChange(parseInt(e.target.value))} style={{ fontSize: 'var(--font-xs)' }}>
            <option value={1}>Stride = 1</option>
            <option value={2}>Stride = 2</option>
          </select>
        </div>

        <div style={{ flex: 1, fontSize: '11px', color: 'var(--color-text-muted)', borderLeft: '1px solid var(--color-border)', paddingLeft: 'var(--space-md)' }}>
          {formula_explanation}
        </div>
      </div>

      {/* Grid Flow: Input Image -> Kernel -> Output Feature Map -> Pooling Map */}
      <div style={{ display: 'grid', gridTemplateColumns: 'auto auto auto auto', gap: 'var(--space-lg)', alignItems: 'center', overflowX: 'auto', padding: 'var(--space-xs)' }}>
        
        {/* 1. Input Image Matrix */}
        <div className="card" style={{ padding: 'var(--space-md)', textAlign: 'center' }}>
          <h4 style={{ margin: '0 0 var(--space-xs) 0', fontSize: 'var(--font-xs)', color: 'var(--color-text-main)' }}>
            Input Image (14×14)
          </h4>
          <div style={{ display: 'inline-grid', gridTemplateColumns: `repeat(${inCols}, 16px)`, gap: '1px', background: 'var(--color-border)', padding: '1px', borderRadius: 'var(--radius-sm)' }}>
            {input_matrix.map((row, r) =>
              row.map((val, c) => {
                const inPatch = r >= patchR && r < patchR + kSize && c >= patchC && c < patchC + kSize;
                const bg = `rgba(255, 255, 255, ${val * 0.9 + 0.05})`;
                return (
                  <div
                    key={`in-${r}-${c}`}
                    style={{
                      width: '16px',
                      height: '16px',
                      background: bg,
                      border: inPatch ? '1.5px solid #f59e0b' : 'none',
                      boxSizing: 'border-box',
                    }}
                    title={`Pixel (${r}, ${c}): ${val}`}
                  />
                );
              })
            )}
          </div>
        </div>

        <div style={{ fontSize: 'var(--font-lg)', color: 'var(--color-primary-400)', fontWeight: 800 }}>✖</div>

        {/* 2. 3x3 Kernel Matrix */}
        <div className="card" style={{ padding: 'var(--space-md)', textAlign: 'center' }}>
          <h4 style={{ margin: '0 0 var(--space-xs) 0', fontSize: 'var(--font-xs)', color: 'var(--color-text-main)' }}>
            Kernel Filter (3×3)
          </h4>
          <div style={{ display: 'inline-grid', gridTemplateColumns: `repeat(${kSize}, 32px)`, gap: '2px', background: 'var(--color-border)', padding: '2px', borderRadius: 'var(--radius-sm)' }}>
            {kernel.map((row, r) =>
              row.map((val, c) => {
                const isPos = val > 0;
                const bg = isPos ? `rgba(16, 185, 129, ${Math.min(0.8, Math.abs(val) * 0.25 + 0.2)})` : val < 0 ? `rgba(239, 68, 68, ${Math.min(0.8, Math.abs(val) * 0.25 + 0.2)})` : 'var(--color-surface)';
                return (
                  <div
                    key={`k-${r}-${c}`}
                    style={{
                      width: '32px',
                      height: '32px',
                      background: bg,
                      display: 'flex',
                      alignItems: 'center',
                      justifyContent: 'center',
                      fontSize: '11px',
                      fontWeight: 700,
                      color: '#ffffff',
                    }}
                  >
                    {val}
                  </div>
                );
              })
            )}
          </div>
        </div>

        <div style={{ fontSize: 'var(--font-lg)', color: 'var(--color-primary-400)', fontWeight: 800 }}>➜</div>

        {/* 3. Output Feature Map Matrix */}
        <div className="card" style={{ padding: 'var(--space-md)', textAlign: 'center' }}>
          <h4 style={{ margin: '0 0 var(--space-xs) 0', fontSize: 'var(--font-xs)', color: 'var(--color-text-main)' }}>
            Feature Map ({fRows}×{fCols})
          </h4>
          <div style={{ display: 'inline-grid', gridTemplateColumns: `repeat(${fCols}, 18px)`, gap: '1px', background: 'var(--color-border)', padding: '1px', borderRadius: 'var(--radius-sm)' }}>
            {feature_map.map((row, r) =>
              row.map((val, c) => {
                const isHovered = hoveredCell.r === r && hoveredCell.c === c;
                // Max feature map intensity
                const bg = `rgba(99, 102, 241, ${Math.min(0.95, val * 0.5 + 0.05)})`;
                return (
                  <div
                    key={`fm-${r}-${c}`}
                    onMouseEnter={() => setHoveredCell({ r, c })}
                    style={{
                      width: '18px',
                      height: '18px',
                      background: isHovered ? '#f59e0b' : bg,
                      border: isHovered ? '2px solid #ffffff' : 'none',
                      cursor: 'pointer',
                      boxSizing: 'border-box',
                    }}
                    title={`Feature Map (${r}, ${c}): ${val}`}
                  />
                );
              })
            )}
          </div>
        </div>

        {/* 4. Downsampled Pooled Map (if selected) */}
        {pooled_map && (
          <>
            <div style={{ fontSize: 'var(--font-lg)', color: 'var(--color-primary-400)', fontWeight: 800 }}>➜</div>
            <div className="card" style={{ padding: 'var(--space-md)', textAlign: 'center' }}>
              <h4 style={{ margin: '0 0 var(--space-xs) 0', fontSize: 'var(--font-xs)', color: 'var(--color-text-main)' }}>
                {poolingType.toUpperCase()} Pooled ({pooled_map.length}×{pooled_map[0]?.length})
              </h4>
              <div style={{ display: 'inline-grid', gridTemplateColumns: `repeat(${pooled_map[0]?.length}, 26px)`, gap: '2px', background: 'var(--color-border)', padding: '2px', borderRadius: 'var(--radius-sm)' }}>
                {pooled_map.map((row, r) =>
                  row.map((val, c) => {
                    const bg = `rgba(16, 185, 129, ${Math.min(0.9, val * 0.4 + 0.1)})`;
                    return (
                      <div
                        key={`pm-${r}-${c}`}
                        style={{
                          width: '26px',
                          height: '26px',
                          background: bg,
                          display: 'flex',
                          alignItems: 'center',
                          justifyContent: 'center',
                          fontSize: '10px',
                          fontWeight: 700,
                          color: '#ffffff',
                        }}
                        title={`Pooled (${r}, ${c}): ${val}`}
                      >
                        {val.toFixed(1)}
                      </div>
                    );
                  })
                )}
              </div>
            </div>
          </>
        )}
      </div>

      {/* Math inspector callout for the currently hovered patch */}
      <div className="card" style={{ padding: 'var(--space-md)', background: 'var(--color-surface-elevated)', borderLeft: '4px solid var(--color-primary-400)' }}>
        <h4 style={{ margin: '0 0 var(--space-xs) 0', fontSize: 'var(--font-sm)', color: 'var(--color-text-main)' }}>
          Mathematical Dot Product Inspector at Feature Map ({hoveredCell.r}, {hoveredCell.c})
        </h4>
        <div style={{ fontSize: 'var(--font-xs)', fontFamily: 'var(--font-mono)', color: 'var(--color-text-muted)' }}>
          <span>z = Σ (I_patch ⊙ K) = <strong>{dotProductSum.toFixed(3)}</strong></span>
          &nbsp;➜&nbsp;
          <span>a = ReLU(z) = <strong>{reluOut.toFixed(3)}</strong></span>
        </div>
      </div>
    </div>
  );
}
