import React, { useState, useEffect } from 'react';
import Editor from '@monaco-editor/react';
import {
  Globe,
  Play,
  RotateCcw,
  Sparkles,
  Layout,
  Code2,
  Eye,
  Maximize2,
  CheckCircle2,
  Layers,
  Palette
} from 'lucide-react';
import Badge from '../components/common/Badge';

const WEB_TEMPLATES = {
  'counter-app': {
    title: 'Interactive Counter & State',
    html: `<div class="card">\n  <h2>⚡ Interactive Counter</h2>\n  <p>Practice DOM manipulation and event listeners.</p>\n  <div class="counter-display" id="count">0</div>\n  <div class="button-group">\n    <button id="dec" class="btn btn-secondary">- Decrement</button>\n    <button id="reset" class="btn btn-outline">Reset</button>\n    <button id="inc" class="btn btn-primary">+ Increment</button>\n  </div>\n</div>`,
    css: `body {\n  font-family: system-ui, -apple-system, sans-serif;\n  background: #0f172a;\n  color: #f8fafc;\n  display: flex;\n  justify-content: center;\n  align-items: center;\n  min-height: 90vh;\n  margin: 0;\n}\n.card {\n  background: #1e293b;\n  padding: 2.5rem;\n  border-radius: 1.25rem;\n  box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.5);\n  text-align: center;\n  max-width: 400px;\n  border: 1px solid #334155;\n}\nh2 { margin-top: 0; color: #38bdf8; }\np { color: #94a3b8; font-size: 0.95rem; }\n.counter-display {\n  font-size: 4rem;\n  font-weight: 800;\n  margin: 1.5rem 0;\n  color: #38bdf8;\n  font-variant-numeric: tabular-nums;\n}\n.button-group {\n  display: flex;\n  gap: 0.75rem;\n  justify-content: center;\n}\n.btn {\n  padding: 0.6rem 1.2rem;\n  border-radius: 0.5rem;\n  border: none;\n  font-weight: 600;\n  cursor: pointer;\n  transition: transform 0.1s, opacity 0.2s;\n}\n.btn:active { transform: scale(0.95); }\n.btn-primary { background: #38bdf8; color: #0f172a; }\n.btn-secondary { background: #e2e8f0; color: #0f172a; }\n.btn-outline { background: transparent; border: 1px solid #475569; color: #cbd5e1; }`,
    js: `let count = 0;\nconst display = document.getElementById('count');\n\ndocument.getElementById('inc').addEventListener('click', () => {\n  count++;\n  updateDisplay();\n});\n\ndocument.getElementById('dec').addEventListener('click', () => {\n  count--;\n  updateDisplay();\n});\n\ndocument.getElementById('reset').addEventListener('click', () => {\n  count = 0;\n  updateDisplay();\n});\n\nfunction updateDisplay() {\n  display.textContent = count;\n  display.style.color = count > 0 ? '#38bdf8' : count < 0 ? '#f43f5e' : '#f8fafc';\n}`
  },
  'flexbox-grid': {
    title: 'CSS Flexbox & Responsive Layout',
    html: `<div class="container">\n  <header class="header">\n    <div class="logo">🚀 WebLab</div>\n    <nav class="nav">\n      <a href="#">Home</a>\n      <a href="#">Courses</a>\n      <a href="#">Labs</a>\n    </nav>\n  </header>\n\n  <main class="grid">\n    <div class="grid-item"><h3>Frontend</h3><p>React 18 & Vite</p></div>\n    <div class="grid-item"><h3>Backend</h3><p>FastAPI & Node</p></div>\n    <div class="grid-item"><h3>Database</h3><p>Async MongoDB</p></div>\n  </main>\n</div>`,
    css: `body {\n  font-family: system-ui, sans-serif;\n  background: #090d16;\n  color: #fff;\n  margin: 0;\n  padding: 1.5rem;\n}\n.container { max-width: 700px; margin: 0 auto; }\n.header {\n  display: flex;\n  justify-content: space-between;\n  align-items: center;\n  padding: 1rem 1.5rem;\n  background: #131b2e;\n  border-radius: 12px;\n  border: 1px solid #1e293b;\n}\n.logo { font-weight: 800; font-size: 1.2rem; color: #38bdf8; }\n.nav { display: flex; gap: 1rem; }\n.nav a { color: #94a3b8; text-decoration: none; font-size: 0.9rem; }\n.nav a:hover { color: #38bdf8; }\n.grid {\n  display: grid;\n  grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));\n  gap: 1rem;\n  margin-top: 1.5rem;\n}\n.grid-item {\n  background: #1e293b;\n  padding: 1.5rem;\n  border-radius: 12px;\n  border: 1px solid #334155;\n  transition: transform 0.2s;\n}\n.grid-item:hover { transform: translateY(-4px); border-color: #38bdf8; }\nh3 { margin-top: 0; color: #38bdf8; }\np { color: #94a3b8; margin-bottom: 0; }`,
    js: `console.log('Flexbox & Grid layout initialized!');`
  }
};

export default function WebDevLabPage() {
  const [activeTab, setActiveTab] = useState('html');
  const [selectedTemplate, setSelectedTemplate] = useState('counter-app');
  const [htmlCode, setHtmlCode] = useState(WEB_TEMPLATES['counter-app'].html);
  const [cssCode, setCssCode] = useState(WEB_TEMPLATES['counter-app'].css);
  const [jsCode, setJsCode] = useState(WEB_TEMPLATES['counter-app'].js);
  const [previewSrcDoc, setPreviewSrcDoc] = useState('');

  // Update preview when code changes
  useEffect(() => {
    const combined = `
      <!DOCTYPE html>
      <html>
        <head>
          <style>${cssCode}</style>
        </head>
        <body>
          ${htmlCode}
          <script>
            try {
              ${jsCode}
            } catch (err) {
              console.error(err);
            }
          </script>
        </body>
      </html>
    `;
    setPreviewSrcDoc(combined);
  }, [htmlCode, cssCode, jsCode]);

  const loadTemplate = (key) => {
    setSelectedTemplate(key);
    setHtmlCode(WEB_TEMPLATES[key].html);
    setCssCode(WEB_TEMPLATES[key].css);
    setJsCode(WEB_TEMPLATES[key].js);
  };

  return (
    <div className="animate-fade-in" style={{ paddingBottom: 40 }}>
      {/* Header */}
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', flexWrap: 'wrap', gap: 16, marginBottom: 24 }}>
        <div>
          <div style={{ display: 'flex', alignItems: 'center', gap: 10, marginBottom: 6 }}>
            <Badge variant="blue"><Globe size={14} /> Web Engineering Lab</Badge>
            <span style={{ fontSize: '0.85rem', color: 'var(--text-muted)' }}>Live Full-Stack Sandbox</span>
          </div>
          <h1 style={{ fontSize: '1.85rem', fontWeight: 800 }}>Interactive Web Sandbox & Live Preview</h1>
          <p style={{ color: 'var(--text-secondary)', fontSize: '0.95rem' }}>
            Write HTML, CSS, and modern JavaScript with real-time hot-reloading in an isolated sandboxed iframe.
          </p>
        </div>

        {/* Template selector */}
        <div style={{ display: 'flex', gap: 8, alignItems: 'center' }}>
          <span style={{ fontSize: '0.85rem', color: 'var(--text-muted)' }}>Preset:</span>
          {Object.entries(WEB_TEMPLATES).map(([key, item]) => (
            <button
              key={key}
              onClick={() => loadTemplate(key)}
              className={`btn btn-sm ${selectedTemplate === key ? 'btn-primary' : 'btn-ghost'}`}
              style={{ borderRadius: 16 }}
            >
              {item.title}
            </button>
          ))}
        </div>
      </div>

      {/* Main Split Grid: Editor (Left) & Live Preview (Right) */}
      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(420px, 1fr))', gap: 20 }}>
        {/* Editor Panel */}
        <div className="card" style={{ padding: 0, overflow: 'hidden', display: 'flex', flexDirection: 'column', height: '620px' }}>
          {/* Tab Bar */}
          <div style={{ display: 'flex', background: 'var(--bg-tertiary)', borderBottom: '1px solid var(--border-color)', padding: '4px 8px' }}>
            <button
              onClick={() => setActiveTab('html')}
              className={`btn btn-sm ${activeTab === 'html' ? 'btn-primary' : 'btn-ghost'}`}
              style={{ borderRadius: 6, gap: 6 }}
            >
              <Code2 size={14} /> index.html
            </button>
            <button
              onClick={() => setActiveTab('css')}
              className={`btn btn-sm ${activeTab === 'css' ? 'btn-primary' : 'btn-ghost'}`}
              style={{ borderRadius: 6, gap: 6 }}
            >
              <Palette size={14} /> style.css
            </button>
            <button
              onClick={() => setActiveTab('js')}
              className={`btn btn-sm ${activeTab === 'js' ? 'btn-primary' : 'btn-ghost'}`}
              style={{ borderRadius: 6, gap: 6 }}
            >
              <Sparkles size={14} /> app.js
            </button>
          </div>

          {/* Monaco Editor */}
          <div style={{ flex: 1 }}>
            {activeTab === 'html' && (
              <Editor
                height="100%"
                language="html"
                theme="vs-dark"
                value={htmlCode}
                onChange={(val) => setHtmlCode(val || '')}
                options={{ minimap: { enabled: false }, fontSize: 13, wordWrap: 'on' }}
              />
            )}
            {activeTab === 'css' && (
              <Editor
                height="100%"
                language="css"
                theme="vs-dark"
                value={cssCode}
                onChange={(val) => setCssCode(val || '')}
                options={{ minimap: { enabled: false }, fontSize: 13, wordWrap: 'on' }}
              />
            )}
            {activeTab === 'js' && (
              <Editor
                height="100%"
                language="javascript"
                theme="vs-dark"
                value={jsCode}
                onChange={(val) => setJsCode(val || '')}
                options={{ minimap: { enabled: false }, fontSize: 13, wordWrap: 'on' }}
              />
            )}
          </div>
        </div>

        {/* Live Preview Panel */}
        <div className="card" style={{ padding: 0, overflow: 'hidden', display: 'flex', flexDirection: 'column', height: '620px' }}>
          {/* Header Bar */}
          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', background: 'var(--bg-tertiary)', borderBottom: '1px solid var(--border-color)', padding: '8px 16px' }}>
            <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
              <span style={{ width: 10, height: 10, borderRadius: '50%', background: '#10b981' }} />
              <span style={{ fontSize: '0.85rem', fontWeight: 600, color: 'var(--text-secondary)' }}>Live Browser Sandbox</span>
            </div>
            <span style={{ fontSize: '0.75rem', color: 'var(--text-muted)' }}>localhost:3000</span>
          </div>

          {/* Iframe View */}
          <iframe
            title="Web Sandbox Live Preview"
            srcDoc={previewSrcDoc}
            style={{ width: '100%', height: '100%', border: 'none', background: '#ffffff' }}
            sandbox="allow-scripts"
          />
        </div>
      </div>
    </div>
  );
}
