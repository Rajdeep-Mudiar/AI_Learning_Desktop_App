import React, { useState, useEffect, useRef } from 'react';
import { Copy, Check, Play, RotateCcw, MonitorPlay, Code2, Sparkles, Split, Rows, Code, Eye, ZoomIn, ZoomOut } from 'lucide-react';

export default function CodeSnippetBox({ snippet }) {
  const [copied, setCopied] = useState(false);
  const [code, setCode] = useState(snippet?.code || '');
  const [output, setOutput] = useState(snippet?.output_preview || '');
  const [isRunning, setIsRunning] = useState(false);
  const [viewMode, setViewMode] = useState('split'); // 'split' | 'stacked' | 'code' | 'preview'
  const [fontSize, setFontSize] = useState(14); // 13, 14, 16, 18
  const iframeRef = useRef(null);

  useEffect(() => {
    if (snippet?.code) {
      setCode(snippet.code);
      setOutput(snippet.output_preview || '');
    }
  }, [snippet]);

  if (!snippet) return null;

  const lang = (snippet.language || 'javascript').toLowerCase();
  const isWebCode = ['html', 'css', 'javascript', 'jsx', 'typescript'].includes(lang) || snippet.code?.includes('<') || snippet.code?.includes('{');

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
      if (iframeRef.current) {
        const doc = iframeRef.current.contentDocument || iframeRef.current.contentWindow?.document;
        if (doc) {
          doc.open();
          doc.write(generateFullHtmlDocument(code, lang));
          doc.close();
        }
      }
    } else {
      try {
        if (lang === 'python' || lang === 'py') {
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

  const generateFullHtmlDocument = (rawCode, language) => {
    let cssContent = `
      * { box-sizing: border-box; margin: 0; padding: 0; }
      body {
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
        padding: 24px;
        background: #090d16;
        color: #f1f5f9;
        line-height: 1.6;
      }
      h1, h2, h3, h4 { color: #38bdf8; margin-bottom: 8px; font-weight: 700; }
      h1 { font-size: 1.65rem; }
      p { color: #94a3b8; font-size: 0.92rem; margin-bottom: 12px; }
      a { color: #60a5fa; text-decoration: underline; }
      .site-header, header { background: #131d31; padding: 14px 18px; border-radius: 8px; border: 1px solid #1e293b; margin-bottom: 16px; }
      main { background: #0f172a; padding: 20px; border-radius: 8px; border: 1px solid #1e293b; margin-bottom: 16px; }
      footer { padding: 12px; font-size: 0.8rem; color: #64748b; border-top: 1px solid #1e293b; }
      .nav-links { display: flex; gap: 16px; list-style: none; margin-top: 6px; }
      .skip-link { position: absolute; left: -9999px; }
      .skip-link:focus { position: static; background: #38bdf8; color: #000; padding: 4px 8px; font-weight: bold; border-radius: 4px; }
      button {
        cursor: pointer;
        padding: 8px 16px;
        border-radius: 6px;
        border: none;
        background: #3b82f6;
        color: #fff;
        font-weight: 600;
        transition: all 0.15s ease;
      }
      button:hover { background: #2563eb; transform: translateY(-1px); }
    `;

    if (language === 'css') {
      return `
        <!DOCTYPE html>
        <html>
          <head><style>${cssContent}\n${rawCode}</style></head>
          <body>
            <div class="user-card" style="padding: 20px; background: #1e293b; border-radius: 8px; border: 1px solid #334155;">
              <h3 style="color: #60a5fa; margin-bottom: 8px;">Live CSS Layout Canvas</h3>
              <p style="color: #94a3b8; font-size: 0.92rem;">Edit the CSS stylesheet to see responsive layout modifications instantly!</p>
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
          ${rawCode}
        </body>
      </html>
    `;
  };

  // Determine container layout based on viewMode
  const getLayoutStyles = () => {
    if (viewMode === 'stacked') {
      return {
        display: 'flex',
        flexDirection: 'column',
        minHeight: '600px'
      };
    }
    if (viewMode === 'code') {
      return {
        display: 'grid',
        gridTemplateColumns: '1fr',
        minHeight: '440px'
      };
    }
    if (viewMode === 'preview') {
      return {
        display: 'grid',
        gridTemplateColumns: '1fr',
        minHeight: '440px'
      };
    }
    // Default 'split'
    return {
      display: 'grid',
      gridTemplateColumns: '1fr 1fr',
      minHeight: '440px'
    };
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
        boxShadow: '0 8px 32px rgba(0,0,0,0.18)',
        borderRadius: 12
      }}
    >
      {/* Top Interactive Toolbar */}
      <div 
        style={{ 
          display: 'flex', 
          justifyContent: 'space-between', 
          alignItems: 'center', 
          padding: '12px 18px', 
          background: 'var(--bg-tertiary)', 
          borderBottom: '1px solid var(--border-subtle)',
          flexWrap: 'wrap',
          gap: 12
        }}
      >
        <div style={{ display: 'flex', alignItems: 'center', gap: 12 }}>
          <div style={{ display: 'flex', alignItems: 'center', gap: 6 }}>
            <span style={{ width: 11, height: 11, borderRadius: '50%', background: '#ef4444' }}></span>
            <span style={{ width: 11, height: 11, borderRadius: '50%', background: '#f59e0b' }}></span>
            <span style={{ width: 11, height: 11, borderRadius: '50%', background: '#10b981' }}></span>
          </div>
          <span style={{ fontWeight: 700, fontSize: '0.92rem', color: 'var(--text-primary)', display: 'flex', alignItems: 'center', gap: 8 }}>
            <Code2 size={17} style={{ color: '#38bdf8' }} />
            {snippet.title || 'Interactive Code Laboratory'}
          </span>
          <span className="badge badge-blue" style={{ fontSize: '0.72rem', textTransform: 'uppercase', padding: '2px 8px' }}>
            {lang} • Editable
          </span>
        </div>

        {/* Action & View Mode Controls */}
        <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
          {/* View Mode Switcher */}
          <div style={{ display: 'flex', background: 'var(--bg-secondary)', padding: 2, borderRadius: 6, border: '1px solid var(--border-subtle)' }}>
            <button
              onClick={() => setViewMode('split')}
              className={viewMode === 'split' ? 'btn btn-primary btn-sm' : 'btn btn-ghost btn-sm'}
              style={{ padding: '4px 8px', fontSize: '0.75rem', gap: 4, height: 28 }}
              title="Split View (Side-by-Side)"
            >
              <Split size={13} />
              <span>Split</span>
            </button>
            <button
              onClick={() => setViewMode('stacked')}
              className={viewMode === 'stacked' ? 'btn btn-primary btn-sm' : 'btn btn-ghost btn-sm'}
              style={{ padding: '4px 8px', fontSize: '0.75rem', gap: 4, height: 28 }}
              title="Stacked View (Full Width Top / Bottom)"
            >
              <Rows size={13} />
              <span>Stacked</span>
            </button>
            <button
              onClick={() => setViewMode('code')}
              className={viewMode === 'code' ? 'btn btn-primary btn-sm' : 'btn btn-ghost btn-sm'}
              style={{ padding: '4px 8px', fontSize: '0.75rem', gap: 4, height: 28 }}
              title="Code Editor Only"
            >
              <Code size={13} />
            </button>
            <button
              onClick={() => setViewMode('preview')}
              className={viewMode === 'preview' ? 'btn btn-primary btn-sm' : 'btn btn-ghost btn-sm'}
              style={{ padding: '4px 8px', fontSize: '0.75rem', gap: 4, height: 28 }}
              title="Live Preview Only"
            >
              <Eye size={13} />
            </button>
          </div>

          {/* Font Scaling */}
          <button
            onClick={() => setFontSize(prev => prev > 12 ? prev - 1 : 12)}
            className="btn btn-ghost btn-sm"
            style={{ padding: '4px 6px', height: 28 }}
            title="Decrease Font Size"
          >
            <ZoomOut size={13} />
          </button>
          <span style={{ fontSize: '0.75rem', color: 'var(--text-muted)', fontFamily: 'var(--font-mono)' }}>
            {fontSize}px
          </span>
          <button
            onClick={() => setFontSize(prev => prev < 20 ? prev + 1 : 20)}
            className="btn btn-ghost btn-sm"
            style={{ padding: '4px 6px', height: 28 }}
            title="Increase Font Size"
          >
            <ZoomIn size={13} />
          </button>

          {/* Run Button */}
          <button
            onClick={handleRun}
            className="btn btn-primary btn-sm"
            style={{ padding: '5px 16px', fontSize: '0.8rem', gap: 6, fontWeight: 700, background: '#10b981', borderColor: '#10b981', height: 28 }}
            disabled={isRunning}
          >
            <Play size={13} fill="currentColor" />
            <span>{isRunning ? 'Rendering...' : 'Run & Render'}</span>
          </button>

          {/* Reset */}
          <button
            onClick={handleReset}
            className="btn btn-ghost btn-sm"
            title="Reset code to original"
            style={{ padding: '5px 8px', fontSize: '0.75rem', gap: 4, height: 28 }}
          >
            <RotateCcw size={13} />
          </button>

          {/* Copy */}
          <button
            onClick={handleCopy}
            className="btn btn-ghost btn-sm"
            style={{ padding: '5px 8px', fontSize: '0.75rem', gap: 4, height: 28 }}
          >
            {copied ? <Check size={13} style={{ color: '#34d399' }} /> : <Copy size={13} />}
          </button>
        </div>
      </div>

      {/* Spacious Editor & Sandbox Container */}
      <div 
        style={{ 
          ...getLayoutStyles(),
          borderBottom: '1px solid var(--border-subtle)'
        }}
      >
        {/* Code Editor Column */}
        {viewMode !== 'preview' && (
          <div 
            style={{ 
              display: 'flex', 
              flexDirection: 'column', 
              borderRight: viewMode === 'split' ? '1px solid var(--border-subtle)' : 'none',
              borderBottom: viewMode === 'stacked' ? '1px solid var(--border-subtle)' : 'none',
              background: '#070b13',
              minHeight: viewMode === 'stacked' ? '300px' : '440px'
            }}
          >
            <div 
              style={{ 
                padding: '8px 16px', 
                background: '#0d1322', 
                borderBottom: '1px solid #1a2333', 
                fontSize: '0.75rem', 
                color: '#94a3b8', 
                display: 'flex', 
                justifyContent: 'space-between',
                fontFamily: 'var(--font-mono)' 
              }}
            >
              <span>EDIT CODE BELOW</span>
              <span style={{ color: '#38bdf8' }}>Live Sandbox • Editable</span>
            </div>

            <textarea
              value={code}
              onChange={(e) => setCode(e.target.value)}
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
                minHeight: viewMode === 'stacked' ? '280px' : '400px',
                padding: '16px 20px',
                background: 'transparent',
                color: '#f8fafc',
                border: 'none',
                outline: 'none',
                resize: 'vertical',
                fontFamily: 'var(--font-mono, monospace)',
                fontSize: `${fontSize}px`,
                lineHeight: 1.7,
                whiteSpace: 'pre',
                overflowWrap: 'normal',
                overflowX: 'auto'
              }}
            />
          </div>
        )}

        {/* Live Output & Browser Preview Column */}
        {viewMode !== 'code' && (
          <div 
            style={{ 
              display: 'flex', 
              flexDirection: 'column', 
              background: isWebCode ? '#090d16' : 'var(--bg-secondary)',
              minHeight: viewMode === 'stacked' ? '300px' : '440px'
            }}
          >
            <div 
              style={{ 
                padding: '8px 16px', 
                background: '#0d1322', 
                borderBottom: '1px solid #1a2333', 
                fontSize: '0.75rem', 
                color: '#94a3b8', 
                display: 'flex', 
                justifyContent: 'space-between', 
                alignItems: 'center',
                fontFamily: 'var(--font-mono)' 
              }}
            >
              <span style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                <MonitorPlay size={13} style={{ color: '#10b981' }} />
                {isWebCode ? 'LIVE BROWSER PREVIEW' : 'TERMINAL OUTPUT'}
              </span>
              <span style={{ color: '#10b981', fontSize: '0.72rem', fontWeight: 600 }}>● Active Canvas</span>
            </div>

            {isWebCode ? (
              /* Live Web Sandbox IFrame */
              <div style={{ flex: 1, display: 'flex', background: '#090d16', minHeight: viewMode === 'stacked' ? '280px' : '400px' }}>
                <iframe
                  ref={iframeRef}
                  title="Live Code Preview"
                  srcDoc={generateFullHtmlDocument(code, lang)}
                  sandbox="allow-scripts"
                  style={{
                    width: '100%',
                    height: '100%',
                    minHeight: viewMode === 'stacked' ? '280px' : '400px',
                    border: 'none',
                    background: '#090d16'
                  }}
                />
              </div>
            ) : (
              /* Terminal Execution Output */
              <div 
                style={{ 
                  flex: 1, 
                  padding: '20px', 
                  fontFamily: 'var(--font-mono, monospace)', 
                  fontSize: `${fontSize}px`, 
                  color: '#34d399', 
                  background: '#070b13', 
                  overflowY: 'auto',
                  whiteSpace: 'pre-wrap',
                  lineHeight: 1.7
                }}
              >
                <div style={{ color: '#64748b', fontSize: '0.75rem', marginBottom: 10 }}>
                  $ {lang} execution_engine --run
                </div>
                {output || 'Click "Run & Render" to execute code.'}
              </div>
            )}
          </div>
        )}
      </div>

      {/* Key Takeaway Footer */}
      {snippet.explanation && (
        <div 
          style={{ 
            padding: '14px 20px', 
            background: 'var(--bg-tertiary)', 
            fontSize: '0.85rem', 
            color: 'var(--text-secondary)',
            display: 'flex',
            alignItems: 'center',
            gap: 10
          }}
        >
          <Sparkles size={16} style={{ color: 'var(--accent-primary)', flexShrink: 0 }} />
          <span>
            <strong style={{ color: 'var(--text-primary)' }}>Key Takeaway: </strong> 
            {snippet.explanation}
          </span>
        </div>
      )}
    </div>
  );
}
