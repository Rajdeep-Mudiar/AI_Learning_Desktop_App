import React, { useState, useEffect } from 'react';
import { hackathonService } from '../services/hackathonService';
import { Flame, Clock, Award, Play, Trophy, CheckCircle2 } from 'lucide-react';

export default function HackathonsPage() {
  const [hackathons, setHackathons] = useState([]);
  const [loading, setLoading] = useState(true);
  const [submitting, setSubmitting] = useState(false);
  const [modelCode, setModelCode] = useState('');
  const [modelName, setModelName] = useState('My Tuned GradientBooster');
  const [submissionSuccess, setSubmissionSuccess] = useState(false);

  useEffect(() => {
    loadHackathons();
  }, []);

  const loadHackathons = async () => {
    try {
      setLoading(true);
      const data = await hackathonService.getHackathons();
      setHackathons(data);
      if (data.length > 0 && data[0].starter_code) {
        setModelCode(data[0].starter_code);
      }
    } catch (err) {
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  const handleSubmit = async (challengeId) => {
    try {
      setSubmitting(true);
      setSubmissionSuccess(false);
      await hackathonService.submitEntry({
        challenge_id: challengeId,
        code: modelCode,
        model_name: modelName,
      });
      setSubmissionSuccess(true);
      await loadHackathons();
    } catch (err) {
      console.error(err);
    } finally {
      setSubmitting(false);
    }
  };

  if (loading) {
    return (
      <div className="container" style={{ padding: 'var(--space-2xl)', textAlign: 'center', color: 'var(--color-text-muted)' }}>
        Loading active hackathon sprints...
      </div>
    );
  }

  const activeChallenge = hackathons[0];

  return (
    <div className="container" style={{ paddingBottom: 'var(--space-2xl)' }}>
      {/* Header */}
      <div style={{ marginBottom: 'var(--space-xl)' }}>
        <h1 style={{ fontSize: 'var(--font-2xl)', fontWeight: 800, margin: '0 0 var(--space-xs) 0', color: 'var(--color-text-main)', display: 'flex', alignItems: 'center', gap: '8px' }}>
          <Flame size={24} color="#ef4444" /> AI Hackathons & Timed Competitions
        </h1>
        <p style={{ margin: 0, color: 'var(--color-text-muted)', fontSize: 'var(--font-sm)' }}>
          Timed competitive sprints with private holdout test datasets, target SLA thresholds, and live leaderboards.
        </p>
      </div>

      {activeChallenge && (
        <div style={{ display: 'grid', gridTemplateColumns: '1fr 380px', gap: 'var(--space-xl)', alignItems: 'start' }}>
          {/* Left Column: Challenge & Submission */}
          <div style={{ display: 'flex', flexDirection: 'column', gap: 'var(--space-lg)' }}>
            <div className="card" style={{ padding: 'var(--space-xl)', display: 'flex', flexDirection: 'column', gap: 'var(--space-md)' }}>
              <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                <span style={{ fontSize: '10px', textTransform: 'uppercase', color: '#ef4444', fontWeight: 700, padding: '2px 8px', borderRadius: 'var(--radius-full)', background: 'rgba(239, 68, 68, 0.12)' }}>
                  Active Sprint • {activeChallenge.time_limit_minutes} Mins
                </span>
                <span style={{ fontSize: 'var(--font-xs)', color: 'var(--color-text-muted)', display: 'flex', alignItems: 'center', gap: '4px' }}>
                  <Clock size={13} /> Time Remaining: 38:42
                </span>
              </div>

              <h2 style={{ margin: 0, fontSize: 'var(--font-lg)', color: 'var(--color-text-main)' }}>
                {activeChallenge.title}
              </h2>

              <p style={{ margin: 0, fontSize: 'var(--font-xs)', color: 'var(--color-text-muted)', lineHeight: 1.5 }}>
                {activeChallenge.description}
              </p>

              <div style={{ background: 'var(--color-surface-elevated)', padding: 'var(--space-md)', borderRadius: 'var(--radius-md)', display: 'flex', justifyContent: 'space-between', fontSize: 'var(--font-xs)' }}>
                <div>
                  <div style={{ color: 'var(--color-text-muted)', fontSize: '10px' }}>Evaluation Metric</div>
                  <strong style={{ color: 'var(--color-primary-400)' }}>{activeChallenge.metric_name}</strong>
                </div>
                <div>
                  <div style={{ color: 'var(--color-text-muted)', fontSize: '10px' }}>Target Benchmark</div>
                  <strong style={{ color: '#10b981' }}>{activeChallenge.target_benchmark}</strong>
                </div>
                <div>
                  <div style={{ color: 'var(--color-text-muted)', fontSize: '10px' }}>Dataset</div>
                  <strong>{activeChallenge.dataset_info}</strong>
                </div>
              </div>

              {/* Code Submission */}
              <div style={{ display: 'flex', flexDirection: 'column', gap: 'var(--space-sm)', marginTop: 'var(--space-sm)' }}>
                <div style={{ display: 'flex', gap: 'var(--space-md)' }}>
                  <div style={{ flex: 1 }}>
                    <label style={{ display: 'block', fontSize: '11px', color: 'var(--color-text-muted)', marginBottom: '2px' }}>Model Name</label>
                    <input
                      type="text"
                      className="input"
                      value={modelName}
                      onChange={(e) => setModelName(e.target.value)}
                      style={{ fontSize: 'var(--font-xs)' }}
                    />
                  </div>
                </div>

                <div>
                  <label style={{ display: 'block', fontSize: '11px', color: 'var(--color-text-muted)', marginBottom: '2px' }}>Estimator Code</label>
                  <textarea
                    className="input"
                    rows={8}
                    value={modelCode}
                    onChange={(e) => setModelCode(e.target.value)}
                    style={{ fontFamily: 'var(--font-mono)', fontSize: '11px' }}
                  />
                </div>

                {submissionSuccess && (
                  <div style={{ padding: 'var(--space-sm)', background: 'rgba(16, 185, 129, 0.1)', border: '1px solid #10b981', color: '#10b981', borderRadius: 'var(--radius-sm)', fontSize: 'var(--font-xs)' }}>
                    ✓ Submission evaluated and posted to live leaderboard!
                  </div>
                )}

                <button
                  onClick={() => handleSubmit(activeChallenge.id)}
                  disabled={submitting}
                  className="btn btn-primary"
                  style={{ alignSelf: 'flex-end', display: 'flex', alignItems: 'center', gap: '6px', padding: '10px 18px' }}
                >
                  <Play size={14} />
                  <span>{submitting ? 'Benchmarking on Private Test Set...' : 'Submit to Leaderboard'}</span>
                </button>
              </div>
            </div>
          </div>

          {/* Right Column: Live Leaderboard */}
          <div className="card" style={{ padding: 'var(--space-lg)', display: 'flex', flexDirection: 'column', gap: 'var(--space-md)' }}>
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
              <div style={{ display: 'flex', alignItems: 'center', gap: '6px' }}>
                <Trophy size={18} color="#f59e0b" />
                <h3 style={{ margin: 0, fontSize: 'var(--font-sm)', color: 'var(--color-text-main)' }}>
                  Live Leaderboard
                </h3>
              </div>
              <span style={{ fontSize: '10px', color: '#10b981', fontWeight: 700 }}>● Live</span>
            </div>

            <table style={{ width: '100%', borderCollapse: 'collapse', textAlign: 'left', fontSize: 'var(--font-xs)' }}>
              <thead>
                <tr style={{ background: 'var(--color-surface-elevated)', borderBottom: '1px solid var(--color-border)' }}>
                  <th style={{ padding: '8px' }}>#</th>
                  <th style={{ padding: '8px' }}>User</th>
                  <th style={{ padding: '8px' }}>Score</th>
                  <th style={{ padding: '8px' }}>Latency</th>
                </tr>
              </thead>
              <tbody>
                {activeChallenge.leaderboard.map((entry) => {
                  const isTop1 = entry.rank === 1;
                  const isUser = entry.username.includes('You');

                  return (
                    <tr
                      key={entry.rank}
                      style={{
                        borderBottom: '1px solid var(--color-border)',
                        background: isUser ? 'rgba(99, 102, 241, 0.1)' : isTop1 ? 'rgba(245, 158, 11, 0.08)' : 'transparent',
                      }}
                    >
                      <td style={{ padding: '8px', fontWeight: 700, color: isTop1 ? '#f59e0b' : 'inherit' }}>
                        {isTop1 ? '🥇' : entry.rank}
                      </td>
                      <td style={{ padding: '8px', fontWeight: isUser ? 700 : 500 }}>
                        {entry.username}
                        <div style={{ fontSize: '9px', color: 'var(--color-text-muted)' }}>{entry.model_name}</div>
                      </td>
                      <td style={{ padding: '8px', fontWeight: 700, color: '#10b981' }}>
                        {entry.score.toFixed(3)}
                      </td>
                      <td style={{ padding: '8px', color: 'var(--color-text-muted)' }}>
                        {entry.latency_ms}ms
                      </td>
                    </tr>
                  );
                })}
              </tbody>
            </table>
          </div>
        </div>
      )}
    </div>
  );
}
