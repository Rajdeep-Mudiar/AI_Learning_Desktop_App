import React from 'react';
import { Paperclip, Code, AlertCircle, BookOpen } from 'lucide-react';

export default function TutorContextSelector({ context, onContextChange, lessons = [] }) {
  const [isOpen, setIsOpen] = React.useState(false);

  const hasActiveContext =
    context.current_lesson_title || context.active_code || context.active_error || context.recent_quiz_mistake;

  return (
    <div style={{ position: 'relative' }}>
      <button
        type="button"
        onClick={() => setIsOpen(!isOpen)}
        style={{
          display: 'flex',
          alignItems: 'center',
          gap: '6px',
          padding: '6px 12px',
          borderRadius: 'var(--radius-full)',
          background: hasActiveContext ? 'rgba(99, 102, 241, 0.15)' : 'var(--color-surface-elevated)',
          border: hasActiveContext ? '1px solid var(--color-primary-400)' : '1px solid var(--color-border)',
          color: hasActiveContext ? 'var(--color-primary-400)' : 'var(--color-text-muted)',
          fontSize: '11px',
          fontWeight: 600,
          cursor: 'pointer',
        }}
      >
        <Paperclip size={13} />
        <span>
          {hasActiveContext
            ? `Context Attached (${context.current_lesson_title ? context.current_lesson_title.slice(0, 18) + '...' : 'Custom'})`
            : 'Attach Learning Context'}
        </span>
      </button>

      {isOpen && (
        <div
          style={{
            position: 'absolute',
            bottom: '100%',
            left: 0,
            marginBottom: '8px',
            width: '320px',
            background: 'var(--color-surface)',
            border: '1px solid var(--color-border)',
            borderRadius: 'var(--radius-lg)',
            boxShadow: 'var(--shadow-lg)',
            padding: 'var(--space-md)',
            zIndex: 100,
            display: 'flex',
            flexDirection: 'column',
            gap: 'var(--space-sm)',
          }}
        >
          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
            <h4 style={{ margin: 0, fontSize: 'var(--font-xs)', color: 'var(--color-text-main)' }}>
              Grounding Context
            </h4>
            <button
              onClick={() => {
                onContextChange({
                  current_lesson_title: null,
                  current_lesson_slug: null,
                  active_code: null,
                  active_error: null,
                  recent_quiz_mistake: null,
                });
                setIsOpen(false);
              }}
              style={{ background: 'none', border: 'none', color: '#ef4444', fontSize: '10px', cursor: 'pointer' }}
            >
              Clear
            </button>
          </div>

          {/* Lesson Attachment */}
          <div>
            <label style={{ fontSize: '10px', color: 'var(--color-text-muted)', display: 'flex', alignItems: 'center', gap: '4px', marginBottom: '2px' }}>
              <BookOpen size={11} /> Attached Lesson
            </label>
            <select
              className="input"
              value={context.current_lesson_title || ''}
              onChange={(e) =>
                onContextChange({
                  ...context,
                  current_lesson_title: e.target.value || null,
                })
              }
              style={{ fontSize: '11px', padding: '4px 8px' }}
            >
              <option value="">None (General AI Query)</option>
              <option value="Scaled Dot-Product Attention">Scaled Dot-Product Attention</option>
              <option value="Linear Regression & Normal Equation">Linear Regression & Normal Equation</option>
              <option value="Decision Trees & Gini Impurity">Decision Trees & Gini Impurity</option>
              <option value="Convolutional Neural Networks (CNN)">Convolutional Neural Networks (CNN)</option>
              <option value="K-Means Clustering & Centroid Shift">K-Means Clustering & Centroid Shift</option>
            </select>
          </div>

          {/* Active Code Snippet */}
          <div>
            <label style={{ fontSize: '10px', color: 'var(--color-text-muted)', display: 'flex', alignItems: 'center', gap: '4px', marginBottom: '2px' }}>
              <Code size={11} /> Active Code Snippet
            </label>
            <textarea
              className="input"
              rows={3}
              placeholder="Paste code to review..."
              value={context.active_code || ''}
              onChange={(e) => onContextChange({ ...context, active_code: e.target.value || null })}
              style={{ fontFamily: 'var(--font-mono)', fontSize: '10px' }}
            />
          </div>

          {/* Active Error */}
          <div>
            <label style={{ fontSize: '10px', color: 'var(--color-text-muted)', display: 'flex', alignItems: 'center', gap: '4px', marginBottom: '2px' }}>
              <AlertCircle size={11} /> Error / Exception Traceback
            </label>
            <input
              type="text"
              className="input"
              placeholder="e.g. ValueError: shapes (3, 2) and (3, 2) not aligned"
              value={context.active_error || ''}
              onChange={(e) => onContextChange({ ...context, active_error: e.target.value || null })}
              style={{ fontSize: '10px', padding: '4px 8px' }}
            />
          </div>

          <button
            type="button"
            onClick={() => setIsOpen(false)}
            className="btn btn-primary"
            style={{ padding: '4px 8px', fontSize: '11px', alignSelf: 'flex-end' }}
          >
            Apply Context
          </button>
        </div>
      )}
    </div>
  );
}
