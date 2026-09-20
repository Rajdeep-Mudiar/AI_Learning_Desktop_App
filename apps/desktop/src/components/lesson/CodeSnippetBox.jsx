import React, { useState, useEffect, useRef } from 'react';
import { Copy, Check, Terminal, Play, RotateCcw, MonitorPlay, Code2, Sparkles, Maximize2, Split } from 'lucide-react';

export default function CodeSnippetBox({ snippet }) {
  const [copied, setCopied] = useState(false);
  const [code, setCode] = useState(snippet?.code || '');
  const [output, setOutput] = useState(snippet?.output_preview || '');
  const [isRunning, setIsRunning] = useState(false);
  const [activeView, setActiveView] = useState('split'); // 'split' | 'code' | 'preview'
  const iframeRef = useRef(null);

  useEffect(() => {
    if (snippet?.code) {
      setCode(snippet.code);
      setOutput(snippet.output_preview || '');
    }
  }, [snippet]);

  if (!snippet) return null;

  const lang = (snippet.language || 'javascript').toLowerCase();
  const isWebCode = ['html', 'css', 'javascript', 'jsx', 'typescript'].includes(lang) || snippet.code?.includes('<div') || snippet.code?.includes('<style>');

  const handleCopy = () => {
    navigator.clipboard.writeText(code);
    setCopied(true);
    setTimeout(() => setCopied(false), 2000);
  };

  const handleReset = () => {
    setCode(snippet.code);
    setOutput(snippet.output_preview || '');
  };

  const handleRun = () => {
    setIsRunning(true);

    if (isWebCode) {
      // Re-trigger iframe reload with updated HTML/CSS
      if (iframeRef.current) {
        const doc = iframeRef.current.contentDocument || iframeRef.current.contentWindow?.document;
        if (doc) {
          doc.open();
          doc.write(generateFullHtmlDocument(code, lang));
          doc.close();
        }
      }
    } else {
      // Simulate backend / python execution
      try {
        if (lang === 'python' || lang === 'py') {
          // Check for print statements or return lines
          const printMatches = code.match(/print\((.*?)\)/g);
          if (printMatches && printMatches.length > 0) {
            const outputs = printMatches.map(p => {
              const inside = p.replace(/^print\(/, '').replace(/\)$/, '').trim();
              return inside.replace(/^['"]/, '').replace(/['"]$/, '');
            });
            setOutput(outputs.join('\n'));
          } else {
            setOutput('>>> Process finished with exit code 0\nResult: Execution successful');
          }
        } else {
          setOutput(`Executed successfully (${lang}):\n${snippet.output_preview || 'Output generated.'}`);
        }
      } catch (e) {
        setOutput(`Execution error: ${e.message}`);
      }
    }

    setTimeout(() => setIsRunning(false), 300);
  };

  // Generate clean isolated HTML document for live iframe sandbox
  const generateFullHtmlDocument = (rawCode, language) => {
    let htmlContent = rawCode;
    let cssContent = `
      * { box-sizing: border-box; margin: 0; padding: 0; }
      body {
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
        padding: 20px;
        background: #0f172a;
        color: #f8fafc;
        display: flex;
        flex-direction: column;
        gap: 16px;
      }
      button {
        cursor: pointer;
        padding: 8px 16px;
        border-radius: 6px;
        border: none;
        background: #3b82f6;
        color: #fff;
        font-weight: 600;
        transition: transform 0.15s ease, background 0.15s ease;
      }
      button:hover {
        background: #2563eb;
        transform: translateY(-1px);
      }
    `;

    if (language === 'css') {
      return `
        <!DOCTYPE html>
        <html>
          <head><style>${cssContent}\n${rawCode}</style></head>
          <body>
            <div class="user-card" style="padding: 16px; background: #1e293b; border-radius: 8px;">
              <h3 style="color: #60a5fa; margin-bottom: 8px;">Live CSS Preview Box</h3>
              <p style="color: #94a3b8; font-size: 0.9rem;">Edit the CSS on the left to see live layout changes instantly!</p>
              <button class="btn-interactive" style="margin-top: 12px;">Interactive Button</button>
            </div>
          </body>
        </html>
      `;
    }

    return `
      <!DOCTYPE html>
      <html>
        <head>
          <meta charset="utf-8" />
          <meta name="viewport" content="width=device-width, initial-scale=1" />
          <style>${cssContent}</style>
        </head>
        <body>
          ${htmlContent}
        </body>
      </html>
    `;
  };

  return (
    <div 
      className="card" 
      style={{ 
        marginBottom: 28, 
        padding: 0, 
        overflow: 'hidden', 
        border: '1px solid var(--border-subtle)',
        background: 'var(--bg-secondary)',
        boxShadow: '0 4px 24px rgba(0,0,0,0.12)'
      }}
    >
      {/* Top Interactive Toolbar */}
      <div 
        style={{ 
          display: 'flex', 
          justifyContent: 'space-between', 
          alignItems: 'center', 
          padding: '10px 16px', 
          background: 'var(--bg-tertiary)', 
          borderBottom: '1px solid var(--border-subtle)' 
        }}
      >
        <div style={{ display: 'flex', alignItems: 'center', gap: 10 }}>
          <div style={{ display: 'flex', alignItems: 'center', gap: 6 }}>
            <span style={{ width: 10, height: 10, borderRadius: '50%', background: '#ef4444' }}></span>
            <span style={{ width: 10, height: 10, borderRadius: '50%', background: '#f59e0b' }}></span>
            <span style={{ width: 10, height: 10, borderRadius: '50%', background: '#10b981' }}></span>
          </div>
          <span style={{ fontWeight: 700, fontSize: '0.88rem', color: 'var(--text-primary)', display: 'flex', alignItems: 'center', gap: 6 }}>
            <Code2 size={15} style={{ color: '#38bdf8' }} />
            {snippet.title || 'Interactive Live Code Laboratory'}
          </span>
          <span className="badge badge-blue" style={{ fontSize: '0.7rem', textTransform: 'uppercase' }}>
            {lang} • Editable
          </span>
        </div>

        {/* Action Controls */}
        <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
          <button
            onClick={handleRun}
            className="btn btn-primary btn-sm"
            style={{ padding: '5px 14px', fontSize: '0.78rem', gap: 6, fontWeight: 700, background: '#10b981', borderColor: '#10b981' }}
            disabled={isRunning}
          >
            <Play size={13} fill="currentColor" />
            <span>{isRunning ? 'Running...' : 'Run & Render'}</span>
          </button>

          <button
            onClick={handleReset}
            className="btn btn-ghost btn-sm"
            title="Reset code to original"
            style={{ padding: '5px 8px', fontSize: '0.75rem', gap: 4 }}
          >
            <RotateCcw size={13} />
            <span>Reset</span>
          </button>

          <button
            onClick={handleCopy}
            className="btn btn-ghost btn-sm"
            style={{ padding: '5px 8px', fontSize: '0.75rem', gap: 4 }}
          >
            {copied ? <Check size={13} style={{ color: '#34d399' }} /> : <Copy size={13} />}
            <span>{copied ? 'Copied' : 'Copy'}</span>
          </button>
        </div>
      </div>

      {/* W3Schools-like Responsive Split Editor and Live Preview Window */}
      <div 
        style={{ 
          display: 'grid', 
          gridTemplateColumns: '1fr 1fr', 
          minHeight: '290px',
          borderBottom: '1px solid var(--border-subtle)'
        }}
      >
        {/* Left Column: Interactive Editable Code Input */}
        <div 
          style={{ 
            display: 'flex', 
            flexDirection: 'column', 
            borderRight: '1px solid var(--border-subtle)',
            background: 'var(--color-neutral-900, #0b1120)'
          }}
        >
          <div 
            style={{ 
              padding: '6px 14px', 
              background: '#0f172a', 
              borderBottom: '1px solid #1e293b', 
              fontSize: '0.72rem', 
              color: '#94a3b8', 
              display: 'flex', 
              justifyContent: 'space-between',
              fontFamily: 'var(--font-mono)' 
            }}
          >
            <span>EDIT CODE BELOW</span>
            <span style={{ color: '#38bdf8' }}>Live Sandbox</span>
          </div>

          <textarea
            value={code}
            onChange={(e) => {
              setCode(e.target.value);
            }}
            onKeyDown={(e) => {
              if (e.key === 'Tab') {
                e.preventDefault();
                const start = e.target.selectionStart;
                const end = e.target.selectionEnd;
                setCode(code.substring(0, start) + '  ' + code.substring(end));
                setTimeout(() => {
                  e.target.selectionStart = e.target.selectionEnd = start + 2;
                }, 0);
              }
            }}
            spellCheck="false"
            style={{
              flex: 1,
              width: '100%',
              minHeight: '260px',
              padding: '14px',
              background: 'transparent',
              color: '#f8fafc',
              border: 'none',
              outline: 'none',
              resize: 'vertical',
              fontFamily: 'var(--font-mono, monospace)',
              fontSize: '0.85rem',
              lineHeight: 1.6,
              whiteSpace: 'pre',
              overflowWrap: 'normal',
              overflowX: 'auto'
            }}
          />
        </div>

        {/* Right Column: Live Output & Browser / Terminal Preview */}
        <div 
          style={{ 
            display: 'flex', 
            flexDirection: 'column', 
            background: isWebCode ? '#0f172a' : 'var(--bg-secondary)'
          }}
        >
          <div 
            style={{ 
              padding: '6px 14px', 
              background: '#0f172a', 
              borderBottom: '1px solid #1e293b', 
              fontSize: '0.72rem', 
              color: '#94a3b8', 
              display: 'flex', 
              justifyContent: 'space-between',
              alignItems: 'center',
              fontFamily: 'var(--font-mono)' 
            }}
          >
            <span style={{ display: 'flex', alignItems: 'center', gap: 6 }}>
              <MonitorPlay size={12} style={{ color: '#10b981' }} />
              {isWebCode ? 'LIVE BROWSER PREVIEW' : 'TERMINAL OUTPUT'}
            </span>
            <span style={{ color: '#10b981', fontSize: '0.7rem', fontWeight: 600 }}>● Active</span>
          </div>

          {isWebCode ? (
            /* Live Web Sandbox IFrame */
            <div style={{ flex: 1, display: 'flex', background: '#0f172a', minHeight: '240px' }}>
              <iframe
                ref={iframeRef}
                title="Live Code Preview"
                srcDoc={generateFullHtmlDocument(code, lang)}
                sandbox="allow-scripts"
                style={{
                  width: '100%',
                  height: '100%',
                  minHeight: '240px',
                  border: 'none',
                  background: '#0f172a'
                }}
              />
            </div>
          ) : (
            /* Terminal Execution Output */
            <div 
              style={{ 
                flex: 1, 
                padding: '16px', 
                fontFamily: 'var(--font-mono, monospace)', 
                fontSize: '0.85rem', 
                color: '#34d399', 
                background: '#0b1120', 
                overflowY: 'auto',
                whiteSpace: 'pre-wrap',
                lineHeight: 1.6
              }}
            >
              <div style={{ color: '#64748b', fontSize: '0.72rem', marginBottom: 8 }}>
                $ python script.py
              </div>
              {output || 'Click "Run & Render" to execute code.'}
            </div>
          )}
        </div>
      </div>

      {/* Key Takeaway Footer */}
      {snippet.explanation && (
        <div 
          style={{ 
            padding: '12px 18px', 
            background: 'var(--bg-tertiary)', 
            fontSize: '0.825rem', 
            color: 'var(--text-secondary)',
            display: 'flex',
            alignItems: 'center',
            gap: 8
          }}
        >
          <Sparkles size={14} style={{ color: 'var(--accent-primary)', flexShrink: 0 }} />
          <span>
            <strong style={{ color: 'var(--text-primary)' }}>Key Takeaway: </strong> 
            {snippet.explanation}
          </span>
        </div>
      )}
    </div>
  );
}
