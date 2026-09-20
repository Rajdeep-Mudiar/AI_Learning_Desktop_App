import React, { useState, useEffect } from 'react';
import { AlertTriangle, Lightbulb, CheckCircle2, XCircle, Code2, Award, Terminal, HelpCircle } from 'lucide-react';
import { simulationService } from '../services/simulationService';
import LoadingSpinner from '../components/common/LoadingSpinner';
import Badge from '../components/common/Badge';

export default function BreakTheModelPage() {
  const [scenarios, setScenarios] = useState([]);
  const [activeScenarioId, setActiveScenarioId] = useState(null);
  const [scenarioDetail, setScenarioDetail] = useState(null);
  const [loading, setLoading] = useState(true);
  const [loadingDetail, setLoadingDetail] = useState(false);
  const [selectedOption, setSelectedOption] = useState(null);
  const [submitting, setSubmitting] = useState(false);
  const [evaluationResult, setEvaluationResult] = useState(null);
  const [unlockedHintsCount, setUnlockedHintsCount] = useState(0);

  useEffect(() => {
    async function loadScenarios() {
      try {
        setLoading(true);
        const list = await simulationService.listDiagnosticScenarios();
        setScenarios(list);
        if (list.length > 0) {
          setActiveScenarioId(list[0].id);
        }
      } catch (err) {
        console.error('Failed to list scenarios:', err);
      } finally {
        setLoading(false);
      }
    }
    loadScenarios();
  }, []);

  useEffect(() => {
    async function loadDetail() {
      if (!activeScenarioId) return;
      try {
        setLoadingDetail(true);
        const data = await simulationService.getDiagnosticScenario(activeScenarioId);
        setScenarioDetail(data);
        setSelectedOption(null);
        setEvaluationResult(null);
        setUnlockedHintsCount(0);
      } catch (err) {
        console.error('Failed to load scenario detail:', err);
      } finally {
        setLoadingDetail(false);
      }
    }
    loadDetail();
  }, [activeScenarioId]);

  const handleSubmitDiagnosis = async () => {
    if (selectedOption === null || !activeScenarioId) return;
    try {
      setSubmitting(true);
      const res = await simulationService.submitDiagnosis(activeScenarioId, selectedOption);
      setEvaluationResult(res);
    } catch (err) {
      console.error('Submission failed:', err);
    } finally {
      setSubmitting(false);
    }
  };

  const handleUnlockHint = () => {
    if (scenarioDetail && unlockedHintsCount < scenarioDetail.hints.length) {
      setUnlockedHintsCount((prev) => prev + 1);
    }
  };

  if (loading) return <LoadingSpinner message="Loading Break the Model scenarios..." />;

  return (
    <div className="animate-fade-in" style={{ maxWidth: '1000px' }}>
      <div style={{ marginBottom: 24 }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: 8, marginBottom: 4 }}>
          <span className="badge badge-amber">Diagnostic Challenge Sandbox</span>
        </div>
        <h1 style={{ fontSize: '1.75rem', marginBottom: 6 }}>"Break the Model" Lab</h1>
        <p style={{ color: 'var(--text-secondary)', fontSize: '0.925rem' }}>
          Inspect broken ML pipelines, debug metrics disparities, and isolate critical modeling flaws.
        </p>
      </div>

      {/* Scenario Tabs */}
      <div style={{ display: 'flex', gap: 8, overflowX: 'auto', paddingBottom: 12, marginBottom: 24 }}>
        {scenarios.map((scen) => {
          const isActive = scen.id === activeScenarioId;
          return (
            <button
              key={scen.id}
              onClick={() => setActiveScenarioId(scen.id)}
              className={isActive ? 'btn btn-primary' : 'btn btn-secondary'}
              style={{ padding: '9px 16px', borderRadius: 999, fontSize: '0.85rem' }}
            >
              <AlertTriangle size={15} />
              <span>{scen.title}</span>
            </button>
          );
        })}
      </div>

      {loadingDetail || !scenarioDetail ? (
        <LoadingSpinner message="Loading scenario inspection..." />
      ) : (
        <div style={{ display: 'flex', flexDirection: 'column', gap: 24 }}>
          {/* Overview & Symptoms */}
          <div className="card" style={{ borderLeft: '4px solid #f59e0b' }}>
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', marginBottom: 12 }}>
              <div>
                <div style={{ display: 'flex', alignItems: 'center', gap: 8, marginBottom: 4 }}>
                  <Badge variant="amber">{scenarioDetail.category}</Badge>
                  <span style={{ fontSize: '0.75rem', color: 'var(--text-muted)' }}>• Difficulty: {scenarioDetail.difficulty}</span>
                </div>
                <h2 style={{ fontSize: '1.3rem' }}>{scenarioDetail.title}</h2>
              </div>
              <span className="badge badge-gray">+{scenarioDetail.xp_reward} XP</span>
            </div>

            <p style={{ fontSize: '0.9rem', color: 'var(--text-secondary)', lineHeight: 1.6, marginBottom: 16 }}>
              {scenarioDetail.description}
            </p>

            {/* Observed Symptoms */}
            <div style={{ background: 'var(--bg-secondary)', padding: 14, borderRadius: 'var(--radius-md)' }}>
              <div style={{ fontSize: '0.75rem', fontWeight: 700, color: '#fbbf24', textTransform: 'uppercase', marginBottom: 6 }}>
                Reported Pipeline Symptoms:
              </div>
              <ul style={{ paddingLeft: 18, display: 'flex', flexDirection: 'column', gap: 4, fontSize: '0.825rem', color: 'var(--text-primary)' }}>
                {scenarioDetail.symptoms?.map((sym, idx) => (
                  <li key={idx}>{sym}</li>
                ))}
              </ul>
            </div>
          </div>

          {/* Code Inspection & Metrics */}
          <div style={{ display: 'grid', gridTemplateColumns: '1.4fr 1fr', gap: 20 }}>
            {/* Code Box */}
            <div className="code-container" style={{ margin: 0 }}>
              <div className="code-header">
                <div style={{ display: 'flex', alignItems: 'center', gap: 6 }}>
                  <Code2 size={14} style={{ color: '#38bdf8' }} />
                  <span style={{ fontWeight: 600 }}>pipeline_inspect.py</span>
                </div>
              </div>
              <pre className="code-body" style={{ maxHeight: '280px', overflowY: 'auto' }}>
                <code>{scenarioDetail.code_snippet}</code>
              </pre>
            </div>

            {/* Telemetry Metrics Log */}
            <div className="card" style={{ background: 'var(--bg-secondary)' }}>
              <div style={{ fontSize: '0.75rem', fontWeight: 700, color: 'var(--text-muted)', textTransform: 'uppercase', marginBottom: 12 }}>
                Model Telemetry Log
              </div>
              <div style={{ display: 'flex', flexDirection: 'column', gap: 8 }}>
                {Object.entries(scenarioDetail.metrics_log || {}).map(([key, val]) => (
                  <div key={key} style={{ display: 'flex', justifyContent: 'space-between', fontSize: '0.825rem', padding: '6px 0', borderBottom: '1px solid var(--border-subtle)' }}>
                    <span style={{ color: 'var(--text-muted)' }}>{key}:</span>
                    <b style={{ color: 'var(--text-primary)' }}>{val}</b>
                  </div>
                ))}
              </div>

              {/* Progressive Hints Unlock */}
              <div style={{ marginTop: 20 }}>
                {unlockedHintsCount < scenarioDetail.hints?.length && (
                  <button onClick={handleUnlockHint} className="btn btn-secondary btn-sm" style={{ width: '100%' }}>
                    <Lightbulb size={14} style={{ color: '#fbbf24' }} />
                    <span>Unlock Hint ({unlockedHintsCount + 1}/{scenarioDetail.hints.length})</span>
                  </button>
                )}

                {scenarioDetail.hints?.slice(0, unlockedHintsCount).map((hint, idx) => (
                  <div key={idx} style={{ marginTop: 8, padding: 10, borderRadius: 6, background: 'rgba(245, 158, 11, 0.1)', border: '1px solid rgba(245, 158, 11, 0.25)', fontSize: '0.8rem', color: '#fbbf24' }}>
                    {hint}
                  </div>
                ))}
              </div>
            </div>
          </div>

          {/* Diagnostic Diagnosis Choices */}
          <div className="card" style={{ borderTop: '4px solid var(--accent-primary)' }}>
            <h3 style={{ fontSize: '1.05rem', marginBottom: 14 }}>Select Root Cause Diagnosis:</h3>

            <div style={{ display: 'flex', flexDirection: 'column', gap: 8, marginBottom: 20 }}>
              {scenarioDetail.options?.map((opt, idx) => {
                const isSelected = selectedOption === idx;
                let optClass = 'quiz-option-card';
                if (evaluationResult) {
                  if (evaluationResult.is_correct && isSelected) optClass += ' correct';
                  else if (!evaluationResult.is_correct && isSelected) optClass += ' incorrect';
                } else if (isSelected) {
                  optClass += ' selected';
                }

                return (
                  <div
                    key={idx}
                    className={optClass}
                    onClick={() => !evaluationResult && setSelectedOption(idx)}
                    style={{ margin: 0 }}
                  >
                    <span style={{ fontSize: '0.875rem' }}>{opt}</span>
                  </div>
                );
              })}
            </div>

            {/* Evaluation result */}
            {evaluationResult && (
              <div style={{
                padding: 16,
                borderRadius: 'var(--radius-md)',
                background: evaluationResult.is_correct ? 'rgba(16, 185, 129, 0.08)' : 'rgba(239, 68, 68, 0.08)',
                borderLeft: `4px solid ${evaluationResult.is_correct ? '#10b981' : '#ef4444'}`,
                marginBottom: 20
              }}>
                <div style={{ display: 'flex', alignItems: 'center', gap: 8, fontWeight: 700, color: evaluationResult.is_correct ? '#34d399' : '#f87171', marginBottom: 6 }}>
                  {evaluationResult.is_correct ? <CheckCircle2 size={18} /> : <XCircle size={18} />}
                  <span>{evaluationResult.is_correct ? `Diagnosis Confirmed! (+${evaluationResult.points_earned} XP)` : 'Incorrect Diagnosis'}</span>
                </div>
                <p style={{ fontSize: '0.85rem', color: 'var(--text-primary)', marginBottom: 12 }}>
                  {evaluationResult.explanation}
                </p>

                <div style={{ fontSize: '0.75rem', fontWeight: 700, color: '#38bdf8', textTransform: 'uppercase', marginBottom: 4 }}>
                  Verified Production Fix:
                </div>
                <pre style={{ background: '#070a13', padding: 12, borderRadius: 6, fontSize: '0.8rem', color: '#38bdf8', overflowX: 'auto', margin: 0 }}>
                  <code>{evaluationResult.fix_code_snippet}</code>
                </pre>
              </div>
            )}

            {!evaluationResult && (
              <button
                onClick={handleSubmitDiagnosis}
                className="btn btn-primary"
                disabled={submitting || selectedOption === null}
                style={{ width: '100%', maxWidth: '240px' }}
              >
                {submitting ? 'Verifying Diagnosis...' : 'Submit Diagnosis'}
              </button>
            )}
          </div>
        </div>
      )}
    </div>
  );
}
