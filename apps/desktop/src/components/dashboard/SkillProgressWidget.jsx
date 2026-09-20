import React from 'react';
import { useNavigate } from 'react-router-dom';
import { ChevronRight, Sparkles } from 'lucide-react';
import ProgressBar from '../common/ProgressBar';

export default function SkillProgressWidget({ skills = [] }) {
  const navigate = useNavigate();

  const getSkillColor = (category) => {
    switch (category) {
      case 'Programming': return '#3b82f6';
      case 'Mathematics': return '#8b5cf6';
      case 'Machine Learning': return '#10b981';
      case 'Deep Learning': return '#f59e0b';
      case 'Generative AI': return '#ec4899';
      default: return 'var(--accent-primary)';
    }
  };

  return (
    <div className="card">
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: 18 }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
          <Sparkles size={18} style={{ color: 'var(--accent-primary)' }} />
          <h3 style={{ fontSize: '1.05rem' }}>Skill Mastery Graph</h3>
        </div>
        <button
          onClick={() => navigate('/skills')}
          className="btn btn-ghost btn-sm"
          style={{ display: 'flex', alignItems: 'center', gap: 4, fontSize: '0.8rem' }}
        >
          <span>Full Tree</span>
          <ChevronRight size={14} />
        </button>
      </div>

      <div style={{ display: 'flex', flexDirection: 'column', gap: 16 }}>
        {skills.map((skill) => {
          const color = getSkillColor(skill.category);
          return (
            <div key={skill.skill_id}>
              <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: 6 }}>
                <div>
                  <span style={{ fontSize: '0.85rem', fontWeight: 600 }}>{skill.name}</span>
                  <span style={{ fontSize: '0.72rem', color: 'var(--text-muted)', marginLeft: 8 }}>({skill.level_label})</span>
                </div>
                <span style={{ fontSize: '0.825rem', fontWeight: 700, color: color }}>
                  {skill.percentage}%
                </span>
              </div>
              <ProgressBar
                percentage={skill.percentage}
                color={color}
                height={6}
              />
            </div>
          );
        })}
      </div>
    </div>
  );
}
