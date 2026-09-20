import React from 'react';
import { useNavigate } from 'react-router-dom';
import { Layers, Sparkles, BookOpen, ArrowRight, Code, ShieldCheck } from 'lucide-react';

export default function FeatureTeaserPage({ title, phase, description, roadmapItems = [] }) {
  const navigate = useNavigate();

  return (
    <div className="animate-fade-in" style={{ maxWidth: '800px', margin: '40px auto' }}>
      <div className="card" style={{ padding: 36, textAlign: 'center', borderTop: '4px solid var(--accent-primary)' }}>
        <div style={{
          width: 56,
          height: 56,
          borderRadius: 16,
          background: 'rgba(99, 102, 241, 0.12)',
          color: 'var(--accent-primary)',
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
          margin: '0 auto 16px auto'
        }}>
          <Sparkles size={28} />
        </div>

        <span className="badge badge-purple" style={{ marginBottom: 12 }}>
          {phase} Feature
        </span>

        <h1 style={{ fontSize: '1.75rem', marginBottom: 12 }}>{title}</h1>
        <p style={{ fontSize: '0.95rem', color: 'var(--text-secondary)', lineHeight: 1.6, maxWidth: '580px', margin: '0 auto 28px auto' }}>
          {description}
        </p>

        {roadmapItems.length > 0 && (
          <div style={{ textAlign: 'left', background: 'var(--bg-secondary)', padding: 20, borderRadius: 'var(--radius-md)', marginBottom: 28 }}>
            <h4 style={{ fontSize: '0.9rem', marginBottom: 10, color: 'var(--text-primary)' }}>Phase Specifications & Architecture:</h4>
            <ul style={{ paddingLeft: 20, display: 'flex', flexDirection: 'column', gap: 6, fontSize: '0.85rem', color: 'var(--text-secondary)' }}>
              {roadmapItems.map((item, idx) => (
                <li key={idx}>{item}</li>
              ))}
            </ul>
          </div>
        )}

        <div style={{ display: 'flex', justifyContent: 'center', gap: 12 }}>
          <button onClick={() => navigate('/learn')} className="btn btn-primary">
            <BookOpen size={16} /> Explore Active Curriculum
          </button>
          <button onClick={() => navigate('/dashboard')} className="btn btn-secondary">
            Return to Dashboard
          </button>
        </div>
      </div>
    </div>
  );
}
