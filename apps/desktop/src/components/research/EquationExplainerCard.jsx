import React from 'react';
import { Eye, HelpCircle, Layers } from 'lucide-react';

export default function EquationExplainerCard({ equation }) {
  return (
    <div
      className="card"
      style={{
        padding: 'var(--space-lg)',
        display: 'flex',
        flexDirection: 'column',
        gap: 'var(--space-md)',
        background: 'var(--color-surface)',
        borderLeft: '4px solid var(--color-primary-400)',
      }}
    >
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
        <h4 style={{ margin: 0, fontSize: 'var(--font-sm)', color: 'var(--color-text-main)' }}>
          {equation.equation_name}
        </h4>
        <span style={{ fontSize: '10px', color: 'var(--color-primary-400)', textTransform: 'uppercase', fontWeight: 700 }}>
          Core Mathematical Formulation
        </span>
      </div>

      {/* Formula Display Box */}
      <div
        style={{
          padding: 'var(--space-md)',
          background: 'var(--color-surface-elevated)',
          borderRadius: 'var(--radius-md)',
          border: '1px solid var(--color-border)',
          fontFamily: 'var(--font-mono)',
          fontSize: 'var(--font-sm)',
          textAlign: 'center',
          color: '#38bdf8',
          overflowX: 'auto',
        }}
      >
        {equation.equation_latex}
      </div>

      {/* Plain English Meaning */}
      <div style={{ display: 'flex', flexDirection: 'column', gap: '2px' }}>
        <span style={{ fontSize: '11px', color: 'var(--color-text-muted)', fontWeight: 600, display: 'flex', alignItems: 'center', gap: '4px' }}>
          <Eye size={12} color="#10b981" /> Plain-English Intuition:
        </span>
        <p style={{ margin: 0, fontSize: 'var(--font-xs)', color: 'var(--color-text-main)', lineHeight: 1.5 }}>
          {equation.plain_english_meaning}
        </p>
      </div>

      {/* Geometric Interpretation */}
      <div style={{ display: 'flex', flexDirection: 'column', gap: '2px' }}>
        <span style={{ fontSize: '11px', color: 'var(--color-text-muted)', fontWeight: 600, display: 'flex', alignItems: 'center', gap: '4px' }}>
          <HelpCircle size={12} color="#f59e0b" /> Geometric / Vector Mechanics:
        </span>
        <p style={{ margin: 0, fontSize: 'var(--font-xs)', color: 'var(--color-text-muted)', lineHeight: 1.5 }}>
          {equation.geometric_intuition}
        </p>
      </div>

      {/* Tensor Dimensionality */}
      <div style={{ background: 'rgba(0,0,0,0.2)', padding: '6px 10px', borderRadius: 'var(--radius-sm)', fontSize: '11px', color: 'var(--color-text-muted)' }}>
        <strong>Tensor Dimensions:</strong> {equation.dimension_notes}
      </div>
    </div>
  );
}
