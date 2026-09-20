import React from 'react';

export default function ProgressBar({ percentage = 0, color = 'var(--accent-primary)', height = 8, showLabel = false, labelText = '' }) {
  const clamped = Math.min(100, Math.max(0, percentage));
  return (
    <div className="progress-bar-container">
      {showLabel && (
        <div style={{ display: 'flex', justifyContent: 'space-between', fontSize: '0.75rem', fontWeight: 600, color: 'var(--text-secondary)' }}>
          <span>{labelText}</span>
          <span>{clamped}%</span>
        </div>
      )}
      <div className="progress-bar-track" style={{ height: `${height}px` }}>
        <div
          className="progress-bar-fill"
          style={{
            width: `${clamped}%`,
            background: color,
          }}
        />
      </div>
    </div>
  );
}
