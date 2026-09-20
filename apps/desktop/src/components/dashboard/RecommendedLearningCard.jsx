import React from 'react';
import { useNavigate } from 'react-router-dom';
import { Compass, ArrowRight, BookOpen } from 'lucide-react';
import Badge from '../common/Badge';

export default function RecommendedLearningCard({ recommendations = [] }) {
  const navigate = useNavigate();

  return (
    <div className="card">
      <div style={{ display: 'flex', alignItems: 'center', gap: 8, marginBottom: 16 }}>
        <Compass size={18} style={{ color: 'var(--accent-secondary)' }} />
        <h3 style={{ fontSize: '1.05rem' }}>Personalized Recommendations</h3>
      </div>

      <div style={{ display: 'flex', flexDirection: 'column', gap: 12 }}>
        {recommendations.map((item, idx) => (
          <div
            key={idx}
            onClick={() => navigate(`/lessons/${item.lesson_slug}`)}
            style={{
              padding: '14px',
              borderRadius: 'var(--radius-md)',
              background: 'var(--bg-tertiary)',
              border: '1px solid var(--border-subtle)',
              cursor: 'pointer',
              display: 'flex',
              justifyContent: 'space-between',
              alignItems: 'center',
              transition: 'all var(--transition-fast)'
            }}
            className="card-hoverable"
          >
            <div>
              <div style={{ display: 'flex', alignItems: 'center', gap: 8, marginBottom: 4 }}>
                <Badge variant="blue">{item.course_title}</Badge>
                <span style={{ fontSize: '0.75rem', color: 'var(--text-muted)' }}>• {item.estimated_minutes} min</span>
              </div>
              <h4 style={{ fontSize: '0.9rem', color: 'var(--text-primary)', marginBottom: 4 }}>{item.lesson_title}</h4>
              <p style={{ fontSize: '0.78rem', color: 'var(--text-secondary)' }}>{item.reason}</p>
            </div>
            <ArrowRight size={16} style={{ color: 'var(--text-muted)', flexShrink: 0 }} />
          </div>
        ))}
      </div>
    </div>
  );
}
