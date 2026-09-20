import React, { useState } from 'react';
import { Copy, Check, Terminal, Play } from 'lucide-react';

export default function CodeSnippetBox({ snippet }) {
  const [copied, setCopied] = useState(false);

  if (!snippet) return null;

  const handleCopy = () => {
    navigator.clipboard.writeText(snippet.code);
    setCopied(true);
    setTimeout(() => setCopied(false), 2000);
  };

  return (
    <div className="code-container">
      <div className="code-header">
        <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
          <Terminal size={14} style={{ color: '#38bdf8' }} />
          <span style={{ fontWeight: 600, color: 'var(--text-primary)' }}>{snippet.title || 'Python Implementation'}</span>
        </div>
        <button
          onClick={handleCopy}
          className="btn btn-ghost btn-sm"
          style={{ padding: '4px 8px', fontSize: '0.75rem', gap: 4 }}
        >
          {copied ? <Check size={14} style={{ color: '#34d399' }} /> : <Copy size={14} />}
          <span>{copied ? 'Copied!' : 'Copy Code'}</span>
        </button>
      </div>

      <pre className="code-body">
        <code>{snippet.code}</code>
      </pre>

      {snippet.output_preview && (
        <div className="output-preview-box">
          <div style={{ fontSize: '0.7rem', color: 'var(--text-muted)', textTransform: 'uppercase', marginBottom: 4, letterSpacing: '0.05em' }}>
            Terminal Output Preview:
          </div>
          <pre style={{ margin: 0, whiteSpace: 'pre-wrap' }}>{snippet.output_preview}</pre>
        </div>
      )}

      {snippet.explanation && (
        <div style={{ padding: '12px 16px', background: 'var(--bg-tertiary)', fontSize: '0.825rem', color: 'var(--text-secondary)', borderTop: '1px solid var(--border-subtle)' }}>
          <b>Key Takeaway:</b> {snippet.explanation}
        </div>
      )}
    </div>
  );
}
