import React from 'react';
import { Terminal, Trash2, Clock, CheckCircle2, AlertCircle, Copy, Check } from 'lucide-react';

export default function OutputTerminal({ result, onClear }) {
  const [copied, setCopied] = React.useState(false);

  const handleCopy = () => {
    if (!result) return;
    const text = result.stdout || result.stderr || '';
    navigator.clipboard.writeText(text);
    setCopied(true);
    setTimeout(() => setCopied(false), 2000);
  };

  return (
    <div style={{
      height: '100%',
      display: 'flex',
      flexDirection: 'column',
      background: '#040711',
      border: '1px solid var(--border-subtle)',
      borderRadius: 'var(--radius-md)',
      overflow: 'hidden'
    }}>
      {/* Terminal Header */}
      <div style={{
        display: 'flex',
        justifyContent: 'space-between',
        alignItems: 'center',
        padding: '8px 14px',
        background: '#080d1a',
        borderBottom: '1px solid var(--border-subtle)',
        fontSize: '0.8rem',
        color: 'var(--text-muted)'
      }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
          <Terminal size={14} style={{ color: '#38bdf8' }} />
          <span style={{ fontWeight: 600, color: 'var(--text-primary)' }}>Terminal Console</span>
          {result && (
            <span style={{
              fontSize: '0.72rem',
              display: 'flex',
              alignItems: 'center',
              gap: 4,
              color: result.status === 'success' ? '#34d399' : result.status === 'timeout' ? '#fbbf24' : '#f87171'
            }}>
              {result.status === 'success' ? <CheckCircle2 size={12} /> : <AlertCircle size={12} />}
              {result.status.toUpperCase()} ({result.duration_ms} ms)
            </span>
          )}
        </div>

        <div style={{ display: 'flex', gap: 6 }}>
          <button
            onClick={handleCopy}
            className="btn btn-ghost btn-sm"
            style={{ padding: '2px 8px', fontSize: '0.75rem', gap: 4 }}
            title="Copy Output"
          >
            {copied ? <Check size={12} style={{ color: '#34d399' }} /> : <Copy size={12} />}
            <span>{copied ? 'Copied' : 'Copy'}</span>
          </button>
          <button
            onClick={onClear}
            className="btn btn-ghost btn-sm"
            style={{ padding: '2px 8px', fontSize: '0.75rem', gap: 4 }}
            title="Clear Console"
          >
            <Trash2 size={12} />
            <span>Clear</span>
          </button>
        </div>
      </div>

      {/* Terminal Stream Viewport */}
      <div style={{
        flex: 1,
        padding: '14px',
        overflowY: 'auto',
        fontFamily: 'var(--font-mono)',
        fontSize: '0.85rem',
        lineHeight: 1.5,
        color: '#e2e8f0'
      }}>
        {!result && (
          <div style={{ color: 'var(--text-muted)', fontStyle: 'italic' }}>
            Ready to execute. Click "Run Code (Ctrl+Enter)" above to see terminal output.
          </div>
        )}

        {result && (
          <div>
            {result.stdout && (
              <pre style={{ margin: 0, whiteSpace: 'pre-wrap', color: '#38bdf8' }}>
                {result.stdout}
              </pre>
            )}

            {result.stderr && (
              <pre style={{ margin: '8px 0 0 0', whiteSpace: 'pre-wrap', color: '#f87171' }}>
                {result.stderr}
              </pre>
            )}
          </div>
        )}
      </div>
    </div>
  );
}
