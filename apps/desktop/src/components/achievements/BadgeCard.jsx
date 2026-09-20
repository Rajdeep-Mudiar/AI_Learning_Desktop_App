import React from 'react';
import { Lock, CheckCircle2 } from 'lucide-react';

export default function BadgeCard({ badge }) {
  const tierColors = {
    Bronze: '#cd7f32',
    Silver: '#94a3b8',
    Gold: '#f59e0b',
    Diamond: '#38bdf8',
  };

  const borderCol = tierColors[badge.tier] || '#6366f1';

  return (
    <div
      className="card"
      style={{
        padding: 'var(--space-md)',
        display: 'flex',
        flexDirection: 'column',
        gap: 'var(--space-sm)',
        borderLeft: `4px solid ${borderCol}`,
        opacity: badge.is_unlocked ? 1 : 0.65,
        position: 'relative',
        transition: 'transform 0.15s ease',
      }}
    >
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start' }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
          <span style={{ fontSize: '24px' }}>{badge.icon}</span>
          <div>
            <h4 style={{ margin: 0, fontSize: 'var(--font-sm)', color: 'var(--color-text-main)' }}>
              {badge.title}
            </h4>
            <span style={{ fontSize: '10px', color: borderCol, fontWeight: 700, textTransform: 'uppercase' }}>
              {badge.tier} Tier • +{badge.xp_reward} XP
            </span>
          </div>
        </div>

        {badge.is_unlocked ? (
          <CheckCircle2 size={16} color="#10b981" />
        ) : (
          <Lock size={16} color="var(--color-text-muted)" />
        )}
      </div>

      <p style={{ margin: 0, fontSize: 'var(--font-xs)', color: 'var(--color-text-muted)', lineHeight: 1.4 }}>
        {badge.description}
      </p>

      {!badge.is_unlocked && badge.progress_percentage !== undefined && (
        <div>
          <div style={{ display: 'flex', justifyContent: 'space-between', fontSize: '10px', color: 'var(--color-text-muted)', marginBottom: '2px' }}>
            <span>Progress</span>
            <span>{badge.progress_percentage}%</span>
          </div>
          <div style={{ height: '4px', background: 'var(--color-surface-elevated)', borderRadius: 'var(--radius-full)', overflow: 'hidden' }}>
            <div style={{ height: '100%', width: `${badge.progress_percentage}%`, background: borderCol, borderRadius: 'var(--radius-full)' }} />
          </div>
        </div>
      )}

      {badge.is_unlocked && badge.unlocked_at && (
        <div style={{ fontSize: '10px', color: 'var(--color-text-muted)', marginTop: 'auto' }}>
          Unlocked on {new Date(badge.unlocked_at).toLocaleDateString()}
        </div>
      )}
    </div>
  );
}
