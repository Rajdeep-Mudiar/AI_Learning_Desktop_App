import React, { useState, useRef, useEffect } from 'react';

export default function NeuralNetworkGraphCanvas({ simulationData }) {
  const [hoveredNode, setHoveredNode] = useState(null);
  const [hoveredEdge, setHoveredEdge] = useState(null);
  const decisionCanvasRef = useRef(null);

  const {
    layers = [2, 4, 1],
    weights = [],
    loss_history = [],
    accuracy_history = [],
    final_accuracy = 0,
    sample_forward = [],
    decision_boundary,
    data_points = [],
  } = simulationData || {};

  // Render 2D Decision Boundary on Canvas
  useEffect(() => {
    if (!decisionCanvasRef.current || !decision_boundary || !decision_boundary.grid_z) return;
    const canvas = decisionCanvasRef.current;
    const ctx = canvas.getContext('2d');
    const width = canvas.width;
    const height = canvas.height;

    ctx.clearRect(0, 0, width, height);

    const gridZ = decision_boundary.grid_z;
    const rows = gridZ.length;
    const cols = gridZ[0].length;
    const cellW = width / cols;
    const cellH = height / rows;

    // Draw contour cells
    for (let r = 0; r < rows; r++) {
      for (let c = 0; c < cols; c++) {
        const prob = gridZ[rows - 1 - r][c]; // flip Y for Cartesian
        // Interpolate color: Blue (Class 0) to Orange/Red (Class 1)
        const alpha = Math.abs(prob - 0.5) * 1.5;
        if (prob >= 0.5) {
          ctx.fillStyle = `rgba(245, 158, 11, ${Math.min(0.65, Math.max(0.1, alpha))})`;
        } else {
          ctx.fillStyle = `rgba(59, 130, 246, ${Math.min(0.65, Math.max(0.1, alpha))})`;
        }
        ctx.fillRect(c * cellW, r * cellH, cellW + 0.5, cellH + 0.5);
      }
    }

    // Draw Decision Boundary Line (prob approx 0.5)
    ctx.strokeStyle = 'rgba(255, 255, 255, 0.4)';
    ctx.lineWidth = 1;
    ctx.strokeRect(0, 0, width, height);

    // Draw Data Points
    data_points.forEach((pt) => {
      // Map [-1.5, 1.5] to [0, width]
      const px = ((pt.x + 1.5) / 3.0) * width;
      const py = height - ((pt.y + 1.5) / 3.0) * height;

      ctx.beginPath();
      ctx.arc(px, py, 4, 0, Math.PI * 2);
      ctx.fillStyle = pt.label === 1 ? '#f59e0b' : '#3b82f6';
      ctx.fill();
      ctx.strokeStyle = '#ffffff';
      ctx.lineWidth = 1.2;
      ctx.stroke();
    });
  }, [decision_boundary, data_points]);

  // SVG Graph Layout geometry
  const svgWidth = 480;
  const svgHeight = 280;
  const numLayers = layers.length;
  const colSpacing = (svgWidth - 80) / (numLayers - 1);

  // Compute (x, y) coordinates for every node in every layer
  const nodePositions = layers.map((nodeCount, layerIdx) => {
    const x = 40 + layerIdx * colSpacing;
    const rowSpacing = svgHeight / (nodeCount + 1);
    const nodes = [];
    for (let nodeIdx = 0; nodeIdx < nodeCount; nodeIdx++) {
      const y = (nodeIdx + 1) * rowSpacing;
      nodes.push({ x, y, layerIdx, nodeIdx });
    }
    return nodes;
  });

  return (
    <div style={{ display: 'grid', gridTemplateColumns: '1fr 280px', gap: 'var(--space-lg)', alignItems: 'start' }}>
      {/* Left: Interactive SVG Architecture Graph */}
      <div className="card" style={{ padding: 'var(--space-md)', background: 'var(--color-surface)', position: 'relative' }}>
        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: 'var(--space-xs)' }}>
          <div>
            <h4 style={{ margin: 0, fontSize: 'var(--font-sm)', color: 'var(--color-text-main)' }}>
              Forward Activation & Gradient Computation Graph
            </h4>
            <span style={{ fontSize: '11px', color: 'var(--color-text-muted)' }}>
              Architecture: {layers.join(' → ')} • Accuracy: {(final_accuracy * 100).toFixed(1)}%
            </span>
          </div>
          <div style={{ display: 'flex', gap: '8px', fontSize: '10px', color: 'var(--color-text-muted)' }}>
            <span style={{ color: '#10b981' }}>● +Weight</span>
            <span style={{ color: '#ef4444' }}>● -Weight</span>
          </div>
        </div>

        <svg width="100%" height={svgHeight} viewBox={`0 0 ${svgWidth} ${svgHeight}`} style={{ overflow: 'visible' }}>
          {/* Connecting Edges */}
          {weights.map((lw, lIdx) => {
            const currentLayerNodes = nodePositions[lIdx];
            const nextLayerNodes = nodePositions[lIdx + 1];
            if (!currentLayerNodes || !nextLayerNodes) return null;

            return lw.weights.map((row, srcIdx) =>
              row.map((wVal, dstIdx) => {
                const srcNode = currentLayerNodes[srcIdx];
                const dstNode = nextLayerNodes[dstIdx];
                if (!srcNode || !dstNode) return null;

                const isPos = wVal >= 0;
                const strokeColor = isPos ? 'rgba(16, 185, 129, 0.75)' : 'rgba(239, 68, 68, 0.75)';
                const strokeWidth = Math.min(4, Math.max(0.8, Math.abs(wVal) * 1.5));
                const isHovered = hoveredEdge && hoveredEdge.l === lIdx && hoveredEdge.s === srcIdx && hoveredEdge.d === dstIdx;

                return (
                  <line
                    key={`w-${lIdx}-${srcIdx}-${dstIdx}`}
                    x1={srcNode.x}
                    y1={srcNode.y}
                    x2={dstNode.x}
                    y2={dstNode.y}
                    stroke={isHovered ? '#ffffff' : strokeColor}
                    strokeWidth={isHovered ? strokeWidth + 2 : strokeWidth}
                    strokeOpacity={isHovered ? 1 : 0.6}
                    style={{ cursor: 'pointer', transition: 'stroke-width 0.15s ease' }}
                    onMouseEnter={() => setHoveredEdge({ l: lIdx, s: srcIdx, d: dstIdx, val: wVal })}
                    onMouseLeave={() => setHoveredEdge(null)}
                  />
                );
              })
            );
          })}

          {/* Layer Nodes */}
          {nodePositions.map((layerNodes, lIdx) =>
            layerNodes.map((node, nIdx) => {
              const isInput = lIdx === 0;
              const isOutput = lIdx === layers.length - 1;
              const isHovered = hoveredNode && hoveredNode.l === lIdx && hoveredNode.n === nIdx;

              // Extract activation for this node from sample probe if available
              let nodeActivation = null;
              if (isInput) {
                nodeActivation = nIdx === 0 ? 0.5 : 0.5;
              } else if (sample_forward[lIdx - 1]) {
                nodeActivation = sample_forward[lIdx - 1].post_activations[nIdx];
              }

              return (
                <g key={`n-${lIdx}-${nIdx}`} style={{ cursor: 'pointer' }}>
                  <circle
                    cx={node.x}
                    cy={node.y}
                    r={isHovered ? 15 : 12}
                    fill={isInput ? '#3b82f6' : isOutput ? '#f59e0b' : '#6366f1'}
                    stroke="#ffffff"
                    strokeWidth={isHovered ? 2.5 : 1.5}
                    onMouseEnter={() =>
                      setHoveredNode({
                        l: lIdx,
                        n: nIdx,
                        act: nodeActivation,
                        bias: weights[lIdx - 1]?.biases[nIdx],
                      })
                    }
                    onMouseLeave={() => setHoveredNode(null)}
                  />
                  <text
                    x={node.x}
                    y={node.y + 3}
                    fill="#ffffff"
                    fontSize="9"
                    fontWeight="700"
                    textAnchor="middle"
                    pointerEvents="none"
                  >
                    {isInput ? `x${nIdx + 1}` : isOutput ? 'ŷ' : `h${nIdx + 1}`}
                  </text>
                </g>
              );
            })
          )}

          {/* Layer Labels */}
          {layers.map((_, lIdx) => {
            const x = 40 + lIdx * colSpacing;
            const label = lIdx === 0 ? 'Input' : lIdx === layers.length - 1 ? 'Output' : `Hidden ${lIdx}`;
            return (
              <text key={`lbl-${lIdx}`} x={x} y={svgHeight - 6} fill="var(--color-text-muted)" fontSize="10" textAnchor="middle">
                {label}
              </text>
            );
          })}
        </svg>

        {/* Hover Inspection Tooltip */}
        {(hoveredNode || hoveredEdge) && (
          <div
            style={{
              position: 'absolute',
              bottom: '12px',
              left: '12px',
              background: 'var(--color-surface-elevated)',
              border: '1px solid var(--color-border)',
              borderRadius: 'var(--radius-sm)',
              padding: '6px 12px',
              fontSize: '11px',
              boxShadow: 'var(--shadow-md)',
            }}
          >
            {hoveredNode && (
              <div>
                <strong>Neuron L{hoveredNode.l}[{hoveredNode.n}]:</strong> Activation $a = {hoveredNode.act ?? 'N/A'}$
                {hoveredNode.bias !== undefined && ` • Bias $b = ${hoveredNode.bias}$`}
              </div>
            )}
            {hoveredEdge && (
              <div>
                <strong>Synapse Weight:</strong> $w = {hoveredEdge.val}$ (Layer {hoveredEdge.l} → {hoveredEdge.l + 1})
              </div>
            )}
          </div>
        )}
      </div>

      {/* Right: 2D Decision Boundary & Convergence Curves */}
      <div style={{ display: 'flex', flexDirection: 'column', gap: 'var(--space-md)' }}>
        <div className="card" style={{ padding: 'var(--space-md)', textAlign: 'center' }}>
          <h4 style={{ margin: '0 0 var(--space-xs) 0', fontSize: 'var(--font-xs)', color: 'var(--color-text-main)' }}>
            2D Decision Boundary Contour
          </h4>
          <canvas
            ref={decisionCanvasRef}
            width={240}
            height={200}
            style={{ borderRadius: 'var(--radius-md)', border: '1px solid var(--color-border)', width: '100%', height: 'auto' }}
          />
          <div style={{ display: 'flex', justifyContent: 'space-between', fontSize: '10px', color: 'var(--color-text-muted)', marginTop: '4px' }}>
            <span>● Class 0 (Blue)</span>
            <span>● Class 1 (Amber)</span>
          </div>
        </div>

        {/* Loss Convergence mini-chart */}
        <div className="card" style={{ padding: 'var(--space-sm) var(--space-md)' }}>
          <div style={{ display: 'flex', justifyContent: 'space-between', fontSize: '11px', marginBottom: '4px' }}>
            <span>BCE Loss Curve</span>
            <strong>{loss_history[loss_history.length - 1] ?? '0.00'}</strong>
          </div>
          <div style={{ display: 'flex', alignItems: 'flex-end', height: '36px', gap: '2px', background: 'var(--color-surface-elevated)', padding: '2px', borderRadius: 'var(--radius-sm)' }}>
            {loss_history.map((lVal, idx) => {
              const maxL = Math.max(...loss_history, 1.0);
              const barH = Math.max(3, (lVal / maxL) * 32);
              return (
                <div
                  key={idx}
                  title={`Epoch ${idx * 3}: Loss ${lVal}`}
                  style={{
                    flex: 1,
                    height: `${barH}px`,
                    background: 'var(--color-primary-400)',
                    borderRadius: '1px',
                  }}
                />
              );
            })}
          </div>
        </div>
      </div>
    </div>
  );
}
