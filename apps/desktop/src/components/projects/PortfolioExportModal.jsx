import React, { useState } from 'react';
import { Copy, Check, Download, FileText } from 'lucide-react';

export default function PortfolioExportModal({ exportData, onClose }) {
  const [copiedReadme, setCopiedReadme] = useState(false);
  const [copiedBullets, setCopiedBullets] = useState(false);

  if (!exportData) return null;

  const handleCopyReadme = () => {
    navigator.clipboard.writeText(exportData.markdown_readme);
    setCopiedReadme(true);
    setTimeout(() => setCopiedReadme(false), 2000);
  };

  const handleCopyBullets = () => {
    navigator.clipboard.writeText(exportData.resume_bullet_points.join('\n• '));
    setCopiedBullets(true);
    setTimeout(() => setCopiedBullets(false), 2000);
  };

  const handleDownloadReadme = () => {
    const blob = new Blob([exportData.markdown_readme], { type: 'text/markdown' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = `README-${exportData.project_id}.md`;
    a.click();
    URL.revokeObjectURL(url);
  };

  return (
    <div
      style={{
        position: 'fixed',
        top: 0,
        left: 0,
        right: 0,
        bottom: 0,
        backgroundColor: 'rgba(0, 0, 0, 0.75)',
        backdropFilter: 'blur(6px)',
        zIndex: 9999,
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'center',
        padding: 'var(--space-md)',
      }}
      onClick={onClose}
    >
      <div
        style={{
          background: 'var(--color-surface)',
          border: '1px solid var(--color-border)',
          borderRadius: 'var(--radius-lg)',
          width: '100%',
          maxWidth: '850px',
          padding: 'var(--space-xl)',
          boxShadow: 'var(--shadow-xl)',
          display: 'flex',
          flexDirection: 'column',
          gap: 'var(--space-lg)',
          maxHeight: '90vh',
          overflowY: 'auto',
        }}
        onClick={(e) => e.stopPropagation()}
      >
        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', borderBottom: '1px solid var(--color-border)', paddingBottom: 'var(--space-sm)' }}>
          <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
            <FileText size={20} color="var(--color-primary-400)" />
            <h3 style={{ margin: 0, fontSize: 'var(--font-lg)', color: 'var(--color-text-main)' }}>
              Production Portfolio & GitHub README Exporter
            </h3>
          </div>
          <button
            onClick={onClose}
            className="btn btn-secondary"
            style={{ padding: '4px 10px', fontSize: 'var(--font-xs)' }}
          >
            ✕
          </button>
        </div>

        {/* Resume Bullet Points */}
        <div className="card" style={{ padding: 'var(--space-md)', background: 'var(--color-surface-elevated)' }}>
          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: 'var(--space-xs)' }}>
            <h4 style={{ margin: 0, fontSize: 'var(--font-xs)', color: 'var(--color-primary-400)', textTransform: 'uppercase' }}>
              Tailored Resume Bullet Points
            </h4>
            <button
              onClick={handleCopyBullets}
              className="btn btn-secondary"
              style={{ padding: '2px 8px', fontSize: '11px', display: 'flex', alignItems: 'center', gap: '4px' }}
            >
              {copiedBullets ? <Check size={12} /> : <Copy size={12} />}
              <span>{copiedBullets ? 'Copied' : 'Copy Bullets'}</span>
            </button>
          </div>
          <ul style={{ margin: 0, paddingLeft: '18px', fontSize: 'var(--font-xs)', color: 'var(--color-text-main)', lineHeight: 1.6 }}>
            {exportData.resume_bullet_points.map((pt, idx) => (
              <li key={idx}>{pt}</li>
            ))}
          </ul>
        </div>

        {/* GitHub README Preview & Download */}
        <div style={{ display: 'flex', flexDirection: 'column', gap: 'var(--space-xs)' }}>
          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
            <h4 style={{ margin: 0, fontSize: 'var(--font-sm)', color: 'var(--color-text-main)' }}>
              Generated GitHub README.md Preview
            </h4>
            <div style={{ display: 'flex', gap: 'var(--space-xs)' }}>
              <button
                onClick={handleCopyReadme}
                className="btn btn-secondary"
                style={{ padding: '4px 10px', fontSize: '11px', display: 'flex', alignItems: 'center', gap: '4px' }}
              >
                {copiedReadme ? <Check size={12} /> : <Copy size={12} />}
                <span>{copiedReadme ? 'Copied' : 'Copy Markdown'}</span>
              </button>
              <button
                onClick={handleDownloadReadme}
                className="btn btn-primary"
                style={{ padding: '4px 12px', fontSize: '11px', display: 'flex', alignItems: 'center', gap: '4px' }}
              >
                <Download size={12} />
                <span>Download README.md</span>
              </button>
            </div>
          </div>

          <pre
            style={{
              padding: 'var(--space-md)',
              background: '#0d1117',
              color: '#e6edf3',
              borderRadius: 'var(--radius-md)',
              border: '1px solid var(--color-border)',
              fontFamily: 'var(--font-mono)',
              fontSize: '11px',
              overflowX: 'auto',
              maxHeight: '340px',
            }}
          >
            {exportData.markdown_readme}
          </pre>
        </div>
      </div>
    </div>
  );
}
