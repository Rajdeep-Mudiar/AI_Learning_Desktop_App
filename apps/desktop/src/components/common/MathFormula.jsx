import React from 'react';
import { HelpCircle } from 'lucide-react';

/**
 * Converts common LaTeX and math strings into readable, clean Unicode mathematical formatting.
 */
export function formatMathString(rawStr) {
  if (!rawStr) return '';
  let s = String(rawStr);

  // 1. First remove LaTeX grouping / delimiters
  s = s.replace(/\\left\(/g, '(');
  s = s.replace(/\\right\)/g, ')');
  s = s.replace(/\\left\[/g, '[');
  s = s.replace(/\\right\]/g, ']');
  s = s.replace(/\\left\\\{/g, '{');
  s = s.replace(/\\right\\\}/g, '}');

  // 2. Text and styling commands
  s = s.replace(/\\text\{([^}]+)\}/g, '$1');
  s = s.replace(/\\mathbf\{([^}]+)\}/g, '$1');
  s = s.replace(/\\mathbb\{R\}\^\{([^}]+)\}/g, 'ℝ^$1');
  s = s.replace(/\\mathbb\{R\}/g, 'ℝ');
  s = s.replace(/\\mathrm\{([^}]+)\}/g, '$1');

  // 3. Fractions, roots, and sums
  s = s.replace(/\\frac\{([^}]+)\}\{([^}]+)\}/g, '$1 / $2');
  s = s.replace(/\\sqrt\{([^}]+)\}/g, '√($1)');
  s = s.replace(/\\sqrt/g, '√');
  s = s.replace(/\\sum_\{([^}]+)\}\^\{([^}]+)\}/g, 'Σ($1 to $2)');
  s = s.replace(/\\sum/g, 'Σ');
  s = s.replace(/\\prod/g, 'Π');

  // 4. Greek letters
  s = s.replace(/\\sigma/g, 'σ');
  s = s.replace(/\\alpha/g, 'α');
  s = s.replace(/\\beta/g, 'β');
  s = s.replace(/\\gamma/g, 'γ');
  s = s.replace(/\\theta/g, 'θ');
  s = s.replace(/\\eta/g, 'η');
  s = s.replace(/\\lambda/g, 'λ');
  s = s.replace(/\\Delta/g, 'Δ');
  s = s.replace(/\\nabla/g, '∇');

  // 5. Operators & Relations with word boundaries
  s = s.replace(/\\cdot/g, ' · ');
  s = s.replace(/\\times/g, ' × ');
  s = s.replace(/\\approx/g, ' ≈ ');
  s = s.replace(/\\leq?\b/g, ' ≤ ');
  s = s.replace(/\\geq?\b/g, ' ≥ ');
  s = s.replace(/\\neq/g, ' ≠ ');
  s = s.replace(/\\in\b/g, ' ∈ ');
  s = s.replace(/\\partial/g, '∂');
  s = s.replace(/\\top/g, 'ᵀ');

  // 6. Subscripts & Superscripts
  s = s.replace(/\^T\b/g, 'ᵀ');
  s = s.replace(/\^\{T\}/g, 'ᵀ');
  s = s.replace(/\^2\b/g, '²');
  s = s.replace(/\^3\b/g, '³');
  s = s.replace(/\_i\b/g, 'ᵢ');
  s = s.replace(/\_j\b/g, 'ⱼ');
  s = s.replace(/\_k\b/g, 'ₖ');
  s = s.replace(/\_n\b/g, 'ₙ');
  s = s.replace(/\_0\b/g, '₀');
  s = s.replace(/\_1\b/g, '₁');
  s = s.replace(/\_2\b/g, '₂');

  // 7. Common Math Functions
  s = s.replace(/\\max/g, 'max');
  s = s.replace(/\\min/g, 'min');
  s = s.replace(/\\log/g, 'log');
  s = s.replace(/\\exp/g, 'exp');
  s = s.replace(/\\tanh/g, 'tanh');
  s = s.replace(/\\softmax/gi, 'Softmax');

  // 8. Clean up extra backslashes, math dollar signs, and redundant spaces
  s = s.replace(/\\/g, '');
  s = s.replace(/\$/g, '');
  s = s.replace(/\s+/g, ' ');

  return s.trim();
}

/**
 * MathFormula - A card displaying a mathematical formula with crystal-clear readability,
 * syntax highlighting, and an intuitive breakdown of what each variable represents.
 */
export default function MathFormula({
  formula,
  title = 'Mathematical Formula',
  breakdown = null,
  simpleExplanation = null,
  example = null,
}) {
  const formattedFormula = formatMathString(formula);

  return (
    <div
      className="card"
      style={{
        padding: '20px',
        margin: '16px 0',
        background: 'linear-gradient(135deg, rgba(99, 102, 241, 0.06) 0%, var(--bg-card) 100%)',
        border: '1px solid var(--border-highlight)',
        borderRadius: 'var(--radius-lg)',
        boxShadow: 'var(--shadow-sm)',
      }}
    >
      {/* Formula Title Header */}
      {title && (
        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '12px' }}>
          <span style={{ fontSize: '0.75rem', textTransform: 'uppercase', fontWeight: 700, color: 'var(--color-primary-400)', letterSpacing: '0.04em' }}>
            📐 {title}
          </span>
          <span style={{ fontSize: '0.7rem', color: 'var(--color-text-muted)', background: 'var(--color-surface-elevated)', padding: '2px 8px', borderRadius: 'var(--radius-full)' }}>
            Plain Math
          </span>
        </div>
      )}

      {/* High-Contrast Formula Display */}
      <div
        style={{
          padding: '16px 20px',
          background: 'var(--canvas-bg)',
          border: '1px solid var(--border-highlight)',
          borderRadius: 'var(--radius-md)',
          textAlign: 'center',
          fontFamily: 'var(--font-mono)',
          fontSize: '1.15rem',
          fontWeight: 600,
          color: 'var(--accent-primary)',
          letterSpacing: '0.04em',
          overflowX: 'auto',
          margin: '4px 0 14px 0',
          boxShadow: 'var(--shadow-xs)',
        }}
      >
        {formattedFormula}
      </div>

      {/* Simple Plain-English Explanation */}
      {simpleExplanation && (
        <div style={{ marginBottom: '12px', fontSize: '0.85rem', color: 'var(--color-text-main)', lineHeight: 1.6 }}>
          <strong>💡 In Simple Words:</strong> {simpleExplanation}
        </div>
      )}

      {/* Variable-by-Variable Breakdown Box */}
      {breakdown && Object.keys(breakdown).length > 0 && (
        <div style={{ background: 'var(--color-surface-elevated)', borderRadius: 'var(--radius-sm)', padding: '12px 16px', border: '1px solid var(--color-border)', marginBottom: '8px' }}>
          <div style={{ fontSize: '0.75rem', fontWeight: 700, color: 'var(--color-text-muted)', textTransform: 'uppercase', marginBottom: '8px' }}>
            What each part means:
          </div>
          <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(200px, 1fr))', gap: '8px' }}>
            {Object.entries(breakdown).map(([sym, desc]) => (
              <div key={sym} style={{ display: 'flex', alignItems: 'baseline', gap: '8px', fontSize: '0.8rem' }}>
                <span style={{ fontFamily: 'var(--font-mono)', fontWeight: 700, color: '#34d399', background: 'rgba(52, 211, 153, 0.1)', padding: '1px 6px', borderRadius: '4px' }}>
                  {formatMathString(sym)}
                </span>
                <span style={{ color: 'var(--color-text-secondary)' }}>{desc}</span>
              </div>
            ))}
          </div>
        </div>
      )}

      {/* Step-by-Step Numerical Example */}
      {example && (
        <div style={{ marginTop: '8px', padding: '10px 14px', background: 'rgba(56, 189, 248, 0.08)', borderRadius: 'var(--radius-sm)', borderLeft: '3px solid #38bdf8', fontSize: '0.825rem', color: 'var(--color-text-main)' }}>
          <strong>🔢 Example Calculation:</strong> {example}
        </div>
      )}
    </div>
  );
}
