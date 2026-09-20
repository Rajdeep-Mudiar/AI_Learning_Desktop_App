import React, { useState } from 'react';

export default function ROCCurveChart({ data }) {
  const [hoveredPoint, setHoveredPoint] = useState(null);

  if (!data || !data.points || !data.points.length) {
    return (
      <div style={{ padding: 'var(--space-md)', textAlign: 'center', color: 'var(--color-text-muted)', fontSize: 'var(--font-xs)' }}>
        ROC Curve only available for binary classification tasks.
      </div>
    );
  }

  const { points, auc } = data;
  const size = 260;
  const padding = 35;
  const plotWidth = size - padding * 2;
  const plotHeight = size - padding * 2;

  // Convert (fpr, tpr) in [0, 1] to SVG coordinates
  const toSvgX = (fpr) => padding + fpr * plotWidth;
  const toSvgY = (tpr) => padding + (1 - tpr) * plotHeight;

  // Generate SVG path for the curve
  let pathD = '';
  points.forEach((pt, idx) => {
    const x = toSvgX(pt.fpr);
    const y = toSvgY(pt.tpr);
    if (idx === 0) {
      pathD += `M ${x} ${y}`;
    } else {
      pathD += ` L ${x} ${y}`;
    }
  });

  // Closed path for area under curve fill
  const areaD = `${pathD} L ${toSvgX(1)} ${toSvgY(0)} L ${toSvgX(0)} ${toSvgY(0)} Z`;

  return (
    <div style={{ display: 'flex', flexDirection: 'column', gap: 'var(--space-xs)', alignItems: 'center' }}>
      <div style={{ display: 'flex', justifyContent: 'space-between', width: '100%', alignItems: 'center' }}>
        <h4 style={{ margin: 0, fontSize: 'var(--font-sm)', fontWeight: 600, color: 'var(--color-text-main)' }}>
          ROC Curve
        </h4>
        <span
          style={{
            padding: '2px 8px',
            borderRadius: 'var(--radius-full)',
            background: 'rgba(99, 102, 241, 0.15)',
            color: 'var(--color-primary-400)',
            fontSize: 'var(--font-xs)',
            fontWeight: 700,
          }}
        >
          AUC: {auc}
        </span>
      </div>

      <div style={{ position: 'relative' }}>
        <svg width={size} height={size} style={{ background: 'var(--color-surface)', borderRadius: 'var(--radius-md)', border: '1px solid var(--color-border)' }}>
          {/* Grid lines */}
          <line x1={toSvgX(0)} y1={toSvgY(0.5)} x2={toSvgX(1)} y2={toSvgY(0.5)} stroke="rgba(255,255,255,0.06)" strokeDasharray="3 3" />
          <line x1={toSvgX(0.5)} y1={toSvgY(0)} x2={toSvgX(0.5)} y2={toSvgY(1)} stroke="rgba(255,255,255,0.06)" strokeDasharray="3 3" />

          {/* Random chance 45-degree diagonal */}
          <line
            x1={toSvgX(0)}
            y1={toSvgY(0)}
            x2={toSvgX(1)}
            y2={toSvgY(1)}
            stroke="var(--color-text-muted)"
            strokeDasharray="4 4"
            strokeWidth="1.5"
          />

          {/* Area Under Curve */}
          <path d={areaD} fill="rgba(99, 102, 241, 0.12)" />

          {/* ROC Curve Path */}
          <path d={pathD} fill="none" stroke="var(--color-primary-400)" strokeWidth="2.5" strokeLinecap="round" strokeLinejoin="round" />

          {/* Points */}
          {points.map((pt, idx) => (
            <circle
              key={idx}
              cx={toSvgX(pt.fpr)}
              cy={toSvgY(pt.tpr)}
              r={hoveredPoint === pt ? 5 : 3}
              fill="var(--color-primary-400)"
              stroke="#ffffff"
              strokeWidth="1"
              style={{ cursor: 'pointer', transition: 'r 0.15s ease' }}
              onMouseEnter={() => setHoveredPoint(pt)}
              onMouseLeave={() => setHoveredPoint(null)}
            />
          ))}

          {/* Axes */}
          <line x1={toSvgX(0)} y1={toSvgY(0)} x2={toSvgX(1)} y2={toSvgY(0)} stroke="var(--color-border)" strokeWidth="1.5" />
          <line x1={toSvgX(0)} y1={toSvgY(0)} x2={toSvgX(0)} y2={toSvgY(1)} stroke="var(--color-border)" strokeWidth="1.5" />

          {/* Ticks & Labels */}
          <text x={toSvgX(0)} y={size - 10} fill="var(--color-text-muted)" fontSize="10" textAnchor="middle">0.0</text>
          <text x={toSvgX(0.5)} y={size - 10} fill="var(--color-text-muted)" fontSize="10" textAnchor="middle">0.5</text>
          <text x={toSvgX(1)} y={size - 10} fill="var(--color-text-muted)" fontSize="10" textAnchor="middle">1.0</text>

          <text x={12} y={toSvgY(0) + 3} fill="var(--color-text-muted)" fontSize="10" textAnchor="end">0.0</text>
          <text x={12} y={toSvgY(0.5) + 3} fill="var(--color-text-muted)" fontSize="10" textAnchor="end">0.5</text>
          <text x={12} y={toSvgY(1) + 3} fill="var(--color-text-muted)" fontSize="10" textAnchor="end">1.0</text>
        </svg>

        {hoveredPoint && (
          <div
            style={{
              position: 'absolute',
              top: '10px',
              right: '10px',
              background: 'var(--color-surface-elevated)',
              border: '1px solid var(--color-border)',
              borderRadius: 'var(--radius-sm)',
              padding: '4px 8px',
              fontSize: '11px',
              color: 'var(--color-text-main)',
              pointerEvents: 'none',
              boxShadow: 'var(--shadow-sm)',
            }}
          >
            <div><strong>FPR:</strong> {hoveredPoint.fpr}</div>
            <div><strong>TPR:</strong> {hoveredPoint.tpr}</div>
          </div>
        )}
      </div>
      <div style={{ display: 'flex', justifyContent: 'space-between', width: '100%', fontSize: '11px', color: 'var(--color-text-muted)' }}>
        <span>False Positive Rate (FPR)</span>
        <span>True Positive Rate (TPR)</span>
      </div>
    </div>
  );
}
