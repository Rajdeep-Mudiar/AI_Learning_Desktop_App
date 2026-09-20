import React from 'react';
import SkillTreeGraph from '../components/skill/SkillTreeGraph';

export default function SkillTreePage() {
  return (
    <div className="animate-fade-in">
      <div style={{ marginBottom: 28 }}>
        <h1 style={{ fontSize: '1.75rem', marginBottom: 6 }}>AI Skill Knowledge Graph</h1>
        <p style={{ color: 'var(--text-secondary)', fontSize: '0.925rem' }}>
          Real-time dynamic visualization of your conceptual and practical mastery across all AI disciplines.
        </p>
      </div>

      <SkillTreeGraph />
    </div>
  );
}
