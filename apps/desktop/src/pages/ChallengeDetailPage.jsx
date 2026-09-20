import React, { useState, useEffect } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import { ArrowLeft, Play, Lightbulb, CheckCircle2, XCircle, Award, Code2, Lock } from 'lucide-react';
import { challengeService } from '../services/challengeService';
import MonacoCodeEditor from '../components/playground/MonacoCodeEditor';
import LoadingSpinner from '../components/common/LoadingSpinner';
import Badge from '../components/common/Badge';

export default function ChallengeDetailPage() {
  const { challengeId } = useParams();
  const navigate = useNavigate();
  const [challenge, setChallenge] = useState(null);
  const [code, setCode] = useState('');
  const [loading, setLoading] = useState(true);
  const [submitting, setSubmitting] = useState(false);
  const [gradingResult, setGradingResult] = useState(null);
  const [unlockedHintsCount, setUnlockedHintsCount] = useState(0);

  useEffect(() => {
    async function loadDetail() {
      try {
        setLoading(true);
        const data = await challengeService.getChallenge(challengeId);
        setChallenge(data);
        setCode(data.starter_code);
        setGradingResult(null);
        setUnlockedHintsCount(0);
      } catch (err) {
        console.error('Failed to load challenge:', err);
      } finally {
        setLoading(false);
      }
    }
    loadDetail();
  }, [challengeId]);

  const handleSubmit = async () => {
    try {
      setSubmitting(true);
      const res = await challengeService.submitChallenge(challengeId, code);
      setGradingResult(res);
    } catch (err) {
      console.error('Grading error:', err);
    } finally {
      setSubmitting(false);
    }
  };

  const handleUnlockHint = () => {
    if (challenge && unlockedHintsCount < challenge.hints.length) {
      setUnlockedHintsCount((prev) => prev + 1);
    }
  };

  if (loading) return <LoadingSpinner message="Loading challenge workspace..." />;
  if (!challenge) return <div className="card">Challenge not found.</div>;

  return (
    <div className="animate-fade-in" style={{ height: 'calc(100vh - 120px)', display: 'flex', flexDirection: 'column' }}>
      {/* Top Header */}
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: 14, flexShrink: 0 }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: 12 }}>
          <button
            onClick={() => navigate('/challenges')}
            className="btn btn-ghost btn-sm"
            style={{ padding: '4px 8px' }}
          >
            <ArrowLeft size={16} /> Challenges
          </button>
          <div style={{ borderLeft: '1px solid var(--border-subtle)', paddingLeft: 12 }}>
            <h1 style={{ fontSize: '1.35rem' }}>{challenge.title}</h1>
          </div>
        </div>

        <div style={{ display: 'flex', alignItems: 'center', gap: 12 }}>
          <span className="badge badge-amber">+{challenge.xp_reward} XP</span>
          <button
            onClick={handleSubmit}
            className="btn btn-primary"
            disabled={submitting}
            style={{ padding: '8px 20px', gap: 8 }}
          >
            <Play size={16} fill="currentColor" />
            <span>{submitting ? 'Autograding...' : 'Submit & Autograde'}</span>
          </button>
        </div>
      </div>

      {/* Split Workspace: Problem Statement & Hints on Left, Monaco & Test Results on Right */}
      <div style={{ flex: 1, display: 'grid', gridTemplateColumns: '1fr 1.3fr', gap: 16, minHeight: 0 }}>
        {/* Left Column: Problem & Hints */}
        <div style={{ display: 'flex', flexDirection: 'column', gap: 14, overflowY: 'auto', paddingRight: 4 }}>
          {/* Problem Statement */}
          <div className="card" style={{ padding: 20 }}>
            <div style={{ display: 'flex', alignItems: 'center', gap: 8, marginBottom: 8 }}>
              <Badge variant="blue">{challenge.category}</Badge>
              <span style={{ fontSize: '0.75rem', color: 'var(--text-muted)' }}>Difficulty: {challenge.difficulty}</span>
            </div>
            <h3 style={{ fontSize: '1.05rem', marginBottom: 12 }}>Problem Statement</h3>
            <div style={{ fontSize: '0.875rem', lineHeight: 1.6, color: 'var(--text-secondary)', whiteSpace: 'pre-line' }}>
              {challenge.problem_statement}
            </div>
          </div>

          {/* Progressive Hints Drawer */}
          <div className="card" style={{ padding: 18 }}>
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: 10 }}>
              <div style={{ display: 'flex', alignItems: 'center', gap: 6 }}>
                <Lightbulb size={16} style={{ color: '#fbbf24' }} />
                <h4 style={{ fontSize: '0.9rem' }}>Progressive Hints</h4>
              </div>
              <span style={{ fontSize: '0.75rem', color: 'var(--text-muted)' }}>
                {unlockedHintsCount}/{challenge.hints.length} Unlocked
              </span>
            </div>

            {unlockedHintsCount < challenge.hints.length && (
              <button onClick={handleUnlockHint} className="btn btn-secondary btn-sm" style={{ width: '100%', marginBottom: 8 }}>
                <Lightbulb size={13} style={{ color: '#fbbf24' }} />
                <span>Unlock Next Hint ({unlockedHintsCount + 1})</span>
              </button>
            )}

            <div style={{ display: 'flex', flexDirection: 'column', gap: 8 }}>
              {challenge.hints.slice(0, unlockedHintsCount).map((hint, idx) => (
                <div
                  key={idx}
                  style={{
                    padding: '10px 12px',
                    borderRadius: 6,
                    background: 'rgba(245, 158, 11, 0.1)',
                    border: '1px solid rgba(245, 158, 11, 0.25)',
                    fontSize: '0.8rem',
                    color: '#fbbf24'
                  }}
                >
                  {hint}
                </div>
              ))}
            </div>
          </div>
        </div>

        {/* Right Column: Code Editor & Autograder Test Suite */}
        <div style={{ display: 'flex', flexDirection: 'column', gap: 14, minHeight: 0 }}>
          {/* Monaco Editor */}
          <div className="card" style={{ flex: 1, padding: 0, overflow: 'hidden', minHeight: '260px' }}>
            <MonacoCodeEditor
              code={code}
              onChange={(newCode) => setCode(newCode)}
              language="python"
            />
          </div>

          {/* Autograder Test Suite Results */}
          {gradingResult && (
            <div className="card" style={{ padding: 18, maxHeight: '240px', overflowY: 'auto' }}>
              <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: 12 }}>
                <div style={{ display: 'flex', alignItems: 'center', gap: 8, fontWeight: 700, color: gradingResult.all_passed ? '#34d399' : '#f87171' }}>
                  {gradingResult.all_passed ? <CheckCircle2 size={18} /> : <XCircle size={18} />}
                  <span>{gradingResult.all_passed ? 'ALL TEST CASES PASSED!' : 'SOME TESTS FAILED'}</span>
                  <span style={{ fontSize: '0.8rem', color: 'var(--text-muted)' }}>
                    ({gradingResult.passed_count}/{gradingResult.total_count} Passed • {gradingResult.execution_duration_ms} ms)
                  </span>
                </div>
                {gradingResult.all_passed && <span className="badge badge-green">+{gradingResult.xp_earned} XP</span>}
              </div>

              <div style={{ display: 'flex', flexDirection: 'column', gap: 6 }}>
                {gradingResult.test_results.map((t, idx) => (
                  <div
                    key={idx}
                    style={{
                      padding: '8px 12px',
                      borderRadius: 6,
                      background: 'var(--bg-secondary)',
                      borderLeft: `3px solid ${t.passed ? '#10b981' : '#ef4444'}`,
                      fontSize: '0.8rem',
                      display: 'flex',
                      justifyContent: 'space-between',
                      alignItems: 'center'
                    }}
                  >
                    <div>
                      <span style={{ fontWeight: 600, color: 'var(--text-primary)' }}>{t.description}</span>
                      {t.error_message && (
                        <div style={{ color: '#f87171', marginTop: 2, fontFamily: 'var(--font-mono)' }}>
                          {t.error_message}
                        </div>
                      )}
                      {!t.passed && t.expected_output && (
                        <div style={{ color: 'var(--text-muted)', marginTop: 2 }}>
                          Expected: <code>{t.expected_output}</code> | Got: <code>{t.actual_output}</code>
                        </div>
                      )}
                    </div>
                    <span style={{ fontWeight: 700, color: t.passed ? '#34d399' : '#f87171' }}>
                      {t.passed ? 'PASSED' : 'FAILED'}
                    </span>
                  </div>
                ))}
              </div>
            </div>
          )}
        </div>
      </div>
    </div>
  );
}
