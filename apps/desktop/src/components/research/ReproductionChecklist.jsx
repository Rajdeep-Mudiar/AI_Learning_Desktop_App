import React, { useState } from 'react';
import { CheckCircle2, Circle, Copy, Check, Code } from 'lucide-react';

export default function ReproductionChecklist({ steps = [], onToggleStep }) {
  const [copiedIdx, setCopiedIdx] = useState(null);

  const handleCopy = (code, idx) => {
    navigator.clipboard.writeText(code);
    setCopiedIdx(idx);
    setTimeout(() => setCopiedIdx(null), 2000);
  };

  return (
    <div style={{ display: 'flex', flexDirection: 'column', gap: 'var(--space-md)' }}>
      {steps.map((step, idx) => (
        <div
          key={step.step_number}
          className="card"
          style={{
            padding: 'var(--space-lg)',
            display: 'flex',
            flexDirection: 'column',
            gap: 'var(--space-md)',
            background: 'var(--color-surface)',
            borderLeft: step.is_completed ? '4px solid #10b981' : '4px solid var(--color-border)',
          }}
        >
          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start' }}>
            <div style={{ display: 'flex', alignItems: 'center', gap: '10px' }}>
              <button
                onClick={() => onToggleStep(step.step_number)}
                style={{ background: 'none', border: 'none', cursor: 'pointer', padding: 0 }}
              >
                {step.is_completed ? (
                  <CheckCircle2 size={20} color="#10b981" />
                ) : (
                  <Circle size={20} color="var(--color-text-muted)" />
                )}
              </button>
              <div>
                <span style={{ fontSize: '10px', textTransform: 'uppercase', color: 'var(--color-primary-400)', fontWeight: 700 }}>
                  Reproduction Step {step.step_number}
                </span>
                <h4 style={{ margin: 0, fontSize: 'var(--font-md)', color: 'var(--color-text-main)' }}>
                  {step.title}
                </h4>
              </div>
            </div>

            <button
              onClick={() => onToggleStep(step.step_number)}
              className={step.is_completed ? 'btn btn-secondary' : 'btn btn-primary'}
              style={{ padding: '4px 10px', fontSize: '11px' }}
            >
              {step.is_completed ? 'Completed ✓' : 'Mark Done'}
            </button>
          </div>

          <p style={{ margin: 0, fontSize: 'var(--font-xs)', color: 'var(--color-text-muted)', lineHeight: 1.5 }}>
            {step.description}
          </p>

          {/* Code block */}
          {step.executable_code && (
            <div>
              <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '4px' }}>
                <span style={{ fontSize: '11px', color: 'var(--color-text-muted)', display: 'flex', alignItems: 'center', gap: '4px' }}>
                  <Code size={12} /> Reference PyTorch Implementation
                </span>
                <button
                  onClick={() => handleCopy(step.executable_code, idx)}
                  style={{ background: 'none', border: 'none', color: 'var(--color-primary-400)', fontSize: '11px', cursor: 'pointer', display: 'flex', alignItems: 'center', gap: '4px' }}
                >
                  {copiedIdx === idx ? <Check size={12} /> : <Copy size={12} />}
                  <span>{copiedIdx === idx ? 'Copied' : 'Copy Code'}</span>
                </button>
              </div>
              <pre
                style={{
                  padding: 'var(--space-md)',
                  background: '#0d1117',
                  color: '#e6edf3',
                  borderRadius: 'var(--radius-md)',
                  fontFamily: 'var(--font-mono)',
                  fontSize: '11px',
                  overflowX: 'auto',
                  margin: 0,
                }}
              >
                {step.executable_code}
              </pre>
            </div>
          )}

          <div style={{ background: 'var(--color-surface-elevated)', padding: '6px 10px', borderRadius: 'var(--radius-sm)', fontSize: '11px', color: 'var(--color-text-main)' }}>
            <strong>Expected Verification Outcome:</strong> {step.expected_outcome}
          </div>
        </div>
      ))}
    </div>
  );
}
