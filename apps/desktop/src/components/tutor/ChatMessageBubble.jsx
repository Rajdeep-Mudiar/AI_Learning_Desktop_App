import React from 'react';
import { Bot, User, Copy, Check } from 'lucide-react';

export default function ChatMessageBubble({ message, onFollowupClick }) {
  const [copied, setCopied] = React.useState(false);

  const isUser = message.role === 'user';

  const handleCopy = () => {
    navigator.clipboard.writeText(message.content);
    setCopied(true);
    setTimeout(() => setCopied(false), 2000);
  };

  // Simple clean markdown parser for code blocks and bold text
  const renderFormattedContent = (content) => {
    const parts = content.split(/(```[\s\S]*?```)/g);

    return parts.map((part, idx) => {
      if (part.startsWith('```')) {
        const lines = part.slice(3, -3).trim().split('\n');
        const lang = lines[0].trim();
        const codeText = lang.length < 15 ? lines.slice(1).join('\n') : lines.join('\n');

        return (
          <div
            key={idx}
            style={{
              margin: 'var(--space-sm) 0',
              background: '#0d1117',
              borderRadius: 'var(--radius-md)',
              border: '1px solid var(--color-border)',
              overflow: 'hidden',
              fontFamily: 'var(--font-mono)',
              fontSize: '12px',
            }}
          >
            <div style={{ display: 'flex', justifyContent: 'space-between', padding: '4px 12px', background: 'rgba(255,255,255,0.05)', fontSize: '11px', color: 'var(--color-text-muted)' }}>
              <span>{lang || 'code'}</span>
              <button
                onClick={() => navigator.clipboard.writeText(codeText)}
                style={{ background: 'none', border: 'none', color: 'var(--color-text-muted)', cursor: 'pointer', fontSize: '11px' }}
              >
                Copy
              </button>
            </div>
            <pre style={{ padding: '10px 12px', margin: 0, overflowX: 'auto', color: '#e6edf3' }}>
              {codeText}
            </pre>
          </div>
        );
      }

      // Format headers, bolding, and bullet lists
      const lines = part.split('\n');
      return (
        <div key={idx} style={{ lineHeight: 1.6 }}>
          {lines.map((line, lIdx) => {
            if (line.startsWith('### ')) {
              return <h4 key={lIdx} style={{ margin: '8px 0 4px', fontSize: 'var(--font-sm)', color: 'var(--color-text-main)' }}>{line.slice(4)}</h4>;
            }
            if (line.startsWith('## ')) {
              return <h3 key={lIdx} style={{ margin: '10px 0 4px', fontSize: 'var(--font-md)', color: 'var(--color-text-main)' }}>{line.slice(3)}</h3>;
            }
            if (line.startsWith('# ')) {
              return <h2 key={lIdx} style={{ margin: '12px 0 6px', fontSize: 'var(--font-lg)', color: 'var(--color-text-main)' }}>{line.slice(2)}</h2>;
            }
            if (line.startsWith('- ') || line.startsWith('* ')) {
              return <div key={lIdx} style={{ paddingLeft: '12px', margin: '2px 0' }}>• {line.slice(2)}</div>;
            }
            if (/^\d+\.\s/.test(line)) {
              return <div key={lIdx} style={{ paddingLeft: '12px', margin: '2px 0' }}>{line}</div>;
            }
            if (!line.trim()) {
              return <div key={lIdx} style={{ height: '6px' }} />;
            }
            return <p key={lIdx} style={{ margin: '4px 0' }}>{line}</p>;
          })}
        </div>
      );
    });
  };

  return (
    <div
      style={{
        display: 'flex',
        gap: 'var(--space-sm)',
        alignItems: 'flex-start',
        alignSelf: isUser ? 'flex-end' : 'flex-start',
        maxWidth: isUser ? '80%' : '88%',
        marginBottom: 'var(--space-md)',
      }}
    >
      {!isUser && (
        <div
          style={{
            width: 32,
            height: 32,
            borderRadius: 'var(--radius-full)',
            background: 'linear-gradient(135deg, #6366f1, #38bdf8)',
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center',
            color: '#ffffff',
            flexShrink: 0,
            marginTop: '2px',
          }}
        >
          <Bot size={18} />
        </div>
      )}

      <div style={{ display: 'flex', flexDirection: 'column', gap: '4px', flex: 1 }}>
        <div
          style={{
            background: isUser ? 'var(--color-primary-600)' : 'var(--color-surface)',
            color: isUser ? '#ffffff' : 'var(--color-text-main)',
            border: isUser ? 'none' : '1px solid var(--color-border)',
            borderRadius: isUser ? '16px 16px 4px 16px' : '16px 16px 16px 4px',
            padding: 'var(--space-md) var(--space-lg)',
            boxShadow: 'var(--shadow-sm)',
            fontSize: 'var(--font-sm)',
            position: 'relative',
          }}
        >
          {renderFormattedContent(message.content)}

          {/* Copy button */}
          <button
            onClick={handleCopy}
            title="Copy message"
            style={{
              position: 'absolute',
              top: '8px',
              right: '8px',
              background: 'none',
              border: 'none',
              color: isUser ? 'rgba(255,255,255,0.7)' : 'var(--color-text-muted)',
              cursor: 'pointer',
              padding: '2px',
            }}
          >
            {copied ? <Check size={14} /> : <Copy size={14} />}
          </button>
        </div>

        {/* Assistant Metadata & Suggested Follow-ups */}
        {!isUser && message.metadata && (
          <div style={{ display: 'flex', flexDirection: 'column', gap: '6px', paddingLeft: '4px' }}>
            <div style={{ display: 'flex', gap: '8px', fontSize: '10px', color: 'var(--color-text-muted)' }}>
              <span>Provider: <strong>{message.metadata.provider_used}</strong></span>
              <span>•</span>
              <span>Model: <strong>{message.metadata.model_used}</strong></span>
              <span>•</span>
              <span style={{ textTransform: 'capitalize' }}>Mode: <strong>{message.metadata.mode_used?.replace('_', ' ')}</strong></span>
            </div>

            {/* Referenced concepts */}
            {message.metadata.referenced_concepts?.length > 0 && (
              <div style={{ display: 'flex', gap: '4px', flexWrap: 'wrap', alignItems: 'center' }}>
                <span style={{ fontSize: '10px', color: 'var(--color-text-muted)' }}>Concepts:</span>
                {message.metadata.referenced_concepts.map((concept, i) => (
                  <span
                    key={i}
                    style={{
                      fontSize: '10px',
                      padding: '1px 6px',
                      borderRadius: 'var(--radius-full)',
                      background: 'rgba(99, 102, 241, 0.12)',
                      color: 'var(--color-primary-400)',
                      fontWeight: 600,
                    }}
                  >
                    {concept}
                  </span>
                ))}
              </div>
            )}

            {/* Suggested Followups */}
            {message.metadata.suggested_followups?.length > 0 && (
              <div style={{ display: 'flex', gap: '6px', flexWrap: 'wrap', marginTop: '4px' }}>
                {message.metadata.suggested_followups.map((fu, idx) => (
                  <button
                    key={idx}
                    onClick={() => onFollowupClick(fu)}
                    style={{
                      background: 'var(--color-surface-elevated)',
                      border: '1px solid var(--color-border)',
                      borderRadius: 'var(--radius-full)',
                      padding: '3px 10px',
                      fontSize: '11px',
                      color: 'var(--color-text-main)',
                      cursor: 'pointer',
                      transition: 'all 0.15s ease',
                      textAlign: 'left',
                    }}
                  >
                    💬 {fu}
                  </button>
                ))}
              </div>
            )}
          </div>
        )}
      </div>

      {isUser && (
        <div
          style={{
            width: 32,
            height: 32,
            borderRadius: 'var(--radius-full)',
            background: 'var(--color-surface-elevated)',
            border: '1px solid var(--color-border)',
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center',
            color: 'var(--color-text-main)',
            flexShrink: 0,
            marginTop: '2px',
          }}
        >
          <User size={18} />
        </div>
      )}
    </div>
  );
}
