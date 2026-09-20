import React from 'react';
import { Eye, HelpCircle, Layers, Sparkles } from 'lucide-react';
import { formatMathString } from '../common/MathFormula';

export default function EquationExplainerCard({ equation }) {
  const formattedLatex = formatMathString(equation.equation_latex);

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
        boxShadow: 'var(--shadow-sm)',
      }}
    >
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
        <h4 style={{ margin: 0, fontSize: 'var(--font-sm)', color: 'var(--color-text-main)', fontWeight: 700 }}>
          {equation.equation_name}
        </h4>
        <span style={{ fontSize: '10px', color: 'var(--color-primary-400)', textTransform: 'uppercase', fontWeight: 700, background: 'rgba(99, 102, 241, 0.12)', padding: '2px 8px', borderRadius: 'var(--radius-full)' }}>
          Mathematical Formulation
        </span>
      </div>

      {/* Formula Display Box */}
      <div
        style={{
          padding: '16px 20px',
          background: '#070a13',
          borderRadius: 'var(--radius-md)',
          border: '1px solid rgba(99, 102, 241, 0.25)',
          fontFamily: 'var(--font-mono)',
          fontSize: '1.05rem',
          fontWeight: 600,
          textAlign: 'center',
          color: '#38bdf8',
          letterSpacing: '0.03em',
          overflowX: 'auto',
          boxShadow: 'inset 0 2px 8px rgba(0, 0, 0, 0.4)',
        }}
      >
        {formattedLatex}
      </div>

      {/* Plain English Meaning */}
      <div style={{ display: 'flex', flexDirection: 'column', gap: '4px', background: 'var(--color-surface-elevated)', padding: '12px 14px', borderRadius: 'var(--radius-sm)', border: '1px solid var(--color-border)' }}>
        <span style={{ fontSize: '11px', color: '#10b981', fontWeight: 700, display: 'flex', alignItems: 'center', gap: '5px', textTransform: 'uppercase', letterSpacing: '0.04em' }}>
          <Eye size={13} color="#10b981" /> Plain-English Intuition (What it means):
        </span>
        <p style={{ margin: 0, fontSize: 'var(--font-xs)', color: 'var(--color-text-main)', lineHeight: 1.6 }}>
          {equation.plain_english_meaning}
        </p>
      </div>

      {/* Geometric Interpretation */}
      <div style={{ display: 'flex', flexDirection: 'column', gap: '4px', background: 'var(--color-surface-elevated)', padding: '12px 14px', borderRadius: 'var(--radius-sm)', border: '1px solid var(--color-border)' }}>
        <span style={{ fontSize: '11px', color: '#fbbf24', fontWeight: 700, display: 'flex', alignItems: 'center', gap: '5px', textTransform: 'uppercase', letterSpacing: '0.04em' }}>
          <HelpCircle size={13} color="#fbbf24" /> Visual & Geometric Concept:
        </span>
        <p style={{ margin: 0, fontSize: 'var(--font-xs)', color: 'var(--color-text-secondary)', lineHeight: 1.6 }}>
          {equation.geometric_intuition}
        </p>
      </div>

      {/* Tensor Dimensionality */}
      <div style={{ background: 'rgba(0,0,0,0.25)', padding: '8px 12px', borderRadius: 'var(--radius-sm)', fontSize: '11px', color: 'var(--color-text-muted)', borderLeft: '3px solid var(--color-primary-400)' }}>
        <strong style={{ color: 'var(--color-text-main)' }}>Tensor Dimensions:</strong> {equation.dimension_notes}
      </div>
    </div>
  );
}
