import React, { useState } from 'react';
import { Award, CheckCircle2, Zap } from 'lucide-react';

export default function DailyChallengeCard({ challenge }) {
  const [selectedOption, setSelectedOption] = useState(null);
  const [submitted, setSubmitted] = useState(false);
  const [isCorrect, setIsCorrect] = useState(false);

  if (!challenge) return null;

  const handleSubmit = (idx) => {
    setSelectedOption(idx);
    setSubmitted(true);
    // Option 0 is "(3, 2)" for shape rule
    const correct = idx === 0;
    setIsCorrect(correct);
  };

  return (
    <div
      className="card"
      style={{
        background: 'linear-gradient(145deg, rgba(245, 158, 11, 0.08) 0%, var(--bg-card) 100%)',
        border: '1px solid rgba(245, 158, 11, 0.25)',
      }}
    >
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: 12 }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: 6 }}>
          <Zap size={18} style={{ color: '#fbbf24', fill: '#fbbf24' }} />
          <h3 style={{ fontSize: '1rem', color: '#fbbf24' }}>Daily AI Challenge</h3>
        </div>
        <span className="badge badge-amber">+{challenge.points} XP</span>
      </div>

      <h4 style={{ fontSize: '0.95rem', fontWeight: 600, marginBottom: 8 }}>{challenge.title}</h4>
      <p style={{ fontSize: '0.85rem', color: 'var(--text-secondary)', marginBottom: 16 }}>
        {challenge.description}
      </p>

      {/* Options */}
      <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: 8, marginBottom: 14 }}>
        {challenge.options?.map((opt, idx) => {
          let btnClass = 'quiz-option-card';
          if (submitted) {
            if (idx === 0) btnClass += ' correct';
            else if (idx === selectedOption) btnClass += ' incorrect';
          } else if (selectedOption === idx) {
            btnClass += ' selected';
          }

          return (
            <div
              key={idx}
              className={btnClass}
              onClick={() => !submitted && handleSubmit(idx)}
              style={{ padding: '10px 14px', margin: 0, fontSize: '0.85rem' }}
            >
              <span>{opt}</span>
            </div>
          );
        })}
      </div>

      {submitted && (
        <div style={{
          padding: '10px 14px',
          borderRadius: 'var(--radius-md)',
          background: isCorrect ? 'rgba(16, 185, 129, 0.15)' : 'rgba(239, 68, 68, 0.15)',
          border: `1px solid ${isCorrect ? 'rgba(16, 185, 129, 0.3)' : 'rgba(239, 68, 68, 0.3)'}`,
          fontSize: '0.825rem',
          color: isCorrect ? '#34d399' : '#f87171',
          display: 'flex',
          alignItems: 'center',
          gap: 8
        }}>
          <CheckCircle2 size={16} />
          <span>
            {isCorrect
              ? `Correct! (3, 4) @ (4, 2) produces matrix of shape (3, 2). +${challenge.points} XP earned!`
              : 'Incorrect. Remember: (M, K) @ (K, N) produces shape (M, N). The inner dimensions match (4) and outer dimensions form (3, 2).'}
          </span>
        </div>
      )}
    </div>
  );
}
