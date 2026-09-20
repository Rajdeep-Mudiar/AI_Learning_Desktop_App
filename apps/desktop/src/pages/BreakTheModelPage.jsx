import React, { useState, useEffect, useMemo } from 'react';
import {
  AlertTriangle,
  Lightbulb,
  CheckCircle2,
  XCircle,
  Code2,
  Copy,
  Check,
  Search,
  Filter,
  Layers,
  Sparkles,
  RefreshCw,
  Maximize2,
  Minimize2
} from 'lucide-react';
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

  // Filters state
  const [searchQuery, setSearchQuery] = useState('');
  const [selectedCategory, setSelectedCategory] = useState('All');
  const [selectedDifficulty, setSelectedDifficulty] = useState('All');
  const [copiedCode, setCopiedCode] = useState(false);
  const [isExpandedCode, setIsExpandedCode] = useState(false);

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

  // Compute available categories dynamically
  const categories = useMemo(() => {
    const cats = new Set(scenarios.map((s) => s.category).filter(Boolean));
    return ['All', ...Array.from(cats)];
  }, [scenarios]);

  // Compute filtered scenarios
  const filteredScenarios = useMemo(() => {
    return scenarios.filter((scen) => {
      const matchesCat = selectedCategory === 'All' || scen.category === selectedCategory;
      const matchesDiff = selectedDifficulty === 'All' || scen.difficulty === selectedDifficulty;
      const q = searchQuery.toLowerCase().trim();
      const matchesQuery =
        !q ||
        scen.title.toLowerCase().includes(q) ||
        scen.description.toLowerCase().includes(q) ||
        scen.category.toLowerCase().includes(q) ||
        (scen.symptoms && scen.symptoms.some((s) => s.toLowerCase().includes(q)));

      return matchesCat && matchesDiff && matchesQuery;
    });
  }, [scenarios, selectedCategory, selectedDifficulty, searchQuery]);

  // If active scenario is not in filtered list, set it to the first visible one
  useEffect(() => {
    if (filteredScenarios.length > 0) {
      const exists = filteredScenarios.some((s) => s.id === activeScenarioId);
      if (!exists) {
        setActiveScenarioId(filteredScenarios[0].id);
      }
    }
  }, [filteredScenarios, activeScenarioId]);

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

  const handleCopyCode = (text) => {
    if (!text) return;
    navigator.clipboard.writeText(text);
    setCopiedCode(true);
    setTimeout(() => setCopiedCode(false), 2000);
  };

  if (loading) return <LoadingSpinner message="Loading Break the Model challenges..." />;

  return (
    <div className="animate-fade-in" style={{ maxWidth: '1080px', margin: '0 auto' }}>
      {/* Header */}
      <div style={{ marginBottom: 20 }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: 8, marginBottom: 6 }}>
          <span className="badge badge-amber" style={{ display: 'inline-flex', alignItems: 'center', gap: 5 }}>
            <AlertTriangle size={13} />
            Diagnostic Laboratory
          </span>
          <span className="badge badge-blue">
            {scenarios.length} Interactive Cases
          </span>
        </div>
        <h1 style={{ fontSize: '1.85rem', fontWeight: 800, marginBottom: 6, letterSpacing: '-0.02em' }}>
          "Break the Model" Lab
        </h1>
        <p style={{ color: 'var(--text-secondary)', fontSize: '0.925rem', maxWidth: '780px' }}>
          Inspect broken ML pipelines, analyze telemetry and metric disparities, study full production scripts, and isolate critical root-cause bugs.
        </p>
      </div>

      {/* Filter & Search Bar Controls */}
      <div
        className="card"
        style={{
          marginBottom: 20,
          padding: '16px 20px',
          background: 'var(--bg-secondary)',
          border: '1px solid var(--border-subtle)',
          borderRadius: 'var(--radius-lg)'
        }}
      >
        <div style={{ display: 'flex', flexWrap: 'wrap', gap: 14, alignItems: 'center', justifyContent: 'space-between' }}>
          {/* Search Input */}
          <div style={{ position: 'relative', flex: '1 1 240px', minWidth: '220px' }}>
            <Search
              size={16}
              style={{ position: 'absolute', left: 12, top: '50%', transform: 'translateY(-50%)', color: 'var(--text-muted)' }}
            />
            <input
              type="text"
              placeholder="Search challenges, symptoms, keywords..."
              value={searchQuery}
              onChange={(e) => setSearchQuery(e.target.value)}
              className="input-field"
              style={{ paddingLeft: 36, width: '100%', fontSize: '0.875rem' }}
            />
          </div>

          {/* Difficulty Filter */}
          <div style={{ display: 'flex', alignItems: 'center', gap: 6 }}>
            <span style={{ fontSize: '0.8rem', color: 'var(--text-muted)', fontWeight: 600 }}>Difficulty:</span>
            {['All', 'Beginner', 'Intermediate', 'Advanced'].map((diff) => {
              const active = selectedDifficulty === diff;
              return (
                <button
                  key={diff}
                  onClick={() => setSelectedDifficulty(diff)}
                  className={active ? 'btn btn-primary btn-sm' : 'btn btn-secondary btn-sm'}
                  style={{
                    padding: '4px 10px',
                    fontSize: '0.775rem',
                    borderRadius: 999,
                    height: '28px'
                  }}
                >
                  {diff}
                </button>
              );
            })}
          </div>
        </div>

        {/* Category Filter Chips */}
        <div style={{ marginTop: 14, paddingTop: 12, borderTop: '1px solid var(--border-subtle)', display: 'flex', alignItems: 'center', gap: 8, flexWrap: 'wrap' }}>
          <span style={{ fontSize: '0.8rem', color: 'var(--text-muted)', fontWeight: 600, display: 'flex', alignItems: 'center', gap: 4 }}>
            <Filter size={13} />
            Category:
          </span>
          {categories.map((cat) => {
            const active = selectedCategory === cat;
            return (
              <button
                key={cat}
                onClick={() => setSelectedCategory(cat)}
                style={{
                  padding: '4px 12px',
                  borderRadius: 999,
                  fontSize: '0.775rem',
                  fontWeight: active ? 600 : 400,
                  border: active ? '1px solid var(--accent-primary)' : '1px solid var(--border-subtle)',
                  background: active ? 'var(--accent-primary)' : 'var(--bg-tertiary)',
                  color: active ? '#ffffff' : 'var(--text-secondary)',
                  cursor: 'pointer',
                  transition: 'all 0.15s ease'
                }}
              >
                {cat}
              </button>
            );
          })}
          <span style={{ marginLeft: 'auto', fontSize: '0.775rem', color: 'var(--text-muted)' }}>
            Showing <b>{filteredScenarios.length}</b> of {scenarios.length}
          </span>
        </div>
      </div>

      {/* Scenario Selection Tabs */}
      {filteredScenarios.length === 0 ? (
        <div className="card" style={{ textAlign: 'center', padding: '36px 20px', color: 'var(--text-muted)' }}>
          <AlertTriangle size={32} style={{ color: '#f59e0b', margin: '0 auto 12px' }} />
          <h3 style={{ fontSize: '1.1rem', color: 'var(--text-primary)', marginBottom: 6 }}>No Scenarios Match Your Filter</h3>
          <p style={{ fontSize: '0.875rem', marginBottom: 16 }}>Try resetting search keywords or selecting "All" categories.</p>
          <button
            onClick={() => {
              setSearchQuery('');
              setSelectedCategory('All');
              setSelectedDifficulty('All');
            }}
            className="btn btn-secondary btn-sm"
          >
            <RefreshCw size={14} />
            <span>Reset Filters</span>
          </button>
        </div>
      ) : (
        <div style={{ display: 'flex', gap: 8, overflowX: 'auto', paddingBottom: 12, marginBottom: 20 }}>
          {filteredScenarios.map((scen) => {
            const isActive = scen.id === activeScenarioId;
            return (
              <button
                key={scen.id}
                onClick={() => setActiveScenarioId(scen.id)}
                className={isActive ? 'btn btn-primary' : 'btn btn-secondary'}
                style={{
                  padding: '8px 16px',
                  borderRadius: 999,
                  fontSize: '0.825rem',
                  whiteSpace: 'nowrap',
                  display: 'flex',
                  alignItems: 'center',
                  gap: 7
                }}
              >
                <AlertTriangle size={14} style={{ color: isActive ? '#ffffff' : '#f59e0b' }} />
                <span>{scen.title}</span>
                <span
                  style={{
                    fontSize: '0.675rem',
                    padding: '2px 6px',
                    borderRadius: 4,
                    background: isActive ? 'rgba(255,255,255,0.2)' : 'rgba(255,255,255,0.06)'
                  }}
                >
                  {scen.difficulty}
                </span>
              </button>
            );
          })}
        </div>
      )}

      {/* Active Scenario Details */}
      {loadingDetail || !scenarioDetail ? (
        filteredScenarios.length > 0 && <LoadingSpinner message="Loading scenario pipeline..." />
      ) : (
        <div style={{ display: 'flex', flexDirection: 'column', gap: 20 }}>
          {/* Overview & Symptoms */}
          <div className="card" style={{ borderLeft: '4px solid #f59e0b', background: 'var(--bg-secondary)' }}>
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', marginBottom: 12, flexWrap: 'wrap', gap: 8 }}>
              <div>
                <div style={{ display: 'flex', alignItems: 'center', gap: 8, marginBottom: 6 }}>
                  <Badge variant="amber">{scenarioDetail.category}</Badge>
                  <span className="badge badge-gray" style={{ fontSize: '0.75rem' }}>
                    Difficulty: {scenarioDetail.difficulty}
                  </span>
                </div>
                <h2 style={{ fontSize: '1.35rem', fontWeight: 700 }}>{scenarioDetail.title}</h2>
              </div>
              <span className="badge badge-amber" style={{ fontSize: '0.85rem', fontWeight: 700, padding: '6px 12px' }}>
                +{scenarioDetail.xp_reward} XP
              </span>
            </div>

            <p style={{ fontSize: '0.925rem', color: 'var(--text-secondary)', lineHeight: 1.6, marginBottom: 16 }}>
              {scenarioDetail.description}
            </p>

            {/* Observed Symptoms */}
            <div style={{ background: 'var(--bg-tertiary)', padding: 14, borderRadius: 'var(--radius-md)', border: '1px solid var(--border-subtle)' }}>
              <div style={{ fontSize: '0.75rem', fontWeight: 700, color: '#fbbf24', textTransform: 'uppercase', marginBottom: 8, letterSpacing: '0.04em' }}>
                Reported Pipeline Symptoms & Telemetry Anomalies:
              </div>
              <ul style={{ paddingLeft: 18, display: 'flex', flexDirection: 'column', gap: 5, fontSize: '0.85rem', color: 'var(--text-primary)', margin: 0 }}>
                {scenarioDetail.symptoms?.map((sym, idx) => (
                  <li key={idx} style={{ lineHeight: 1.4 }}>{sym}</li>
                ))}
              </ul>
            </div>
          </div>

          {/* Code Inspection & Metrics */}
          <div style={{ display: 'grid', gridTemplateColumns: isExpandedCode ? '1fr' : '1.5fr 1fr', gap: 20 }}>
            {/* Full Code Box */}
            <div className="code-container" style={{ margin: 0, display: 'flex', flexDirection: 'column' }}>
              <div className="code-header" style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', padding: '10px 14px' }}>
                <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                  <Code2 size={15} style={{ color: '#38bdf8' }} />
                  <span style={{ fontWeight: 600, fontSize: '0.85rem' }}>pipeline_inspect.py</span>
                  <span style={{ fontSize: '0.725rem', color: 'var(--text-muted)' }}>(Full Standalone Code)</span>
                </div>
                <div style={{ display: 'flex', alignItems: 'center', gap: 6 }}>
                  <button
                    onClick={() => handleCopyCode(scenarioDetail.code_snippet)}
                    className="btn btn-secondary btn-sm"
                    style={{ padding: '3px 8px', fontSize: '0.75rem', height: '26px' }}
                    title="Copy full Python script"
                  >
                    {copiedCode ? <Check size={13} style={{ color: '#34d399' }} /> : <Copy size={13} />}
                    <span>{copiedCode ? 'Copied!' : 'Copy Code'}</span>
                  </button>
                  <button
                    onClick={() => setIsExpandedCode(!isExpandedCode)}
                    className="btn btn-secondary btn-sm"
                    style={{ padding: '3px 8px', fontSize: '0.75rem', height: '26px' }}
                    title={isExpandedCode ? 'Standard width' : 'Expand full width'}
                  >
                    {isExpandedCode ? <Minimize2 size={13} /> : <Maximize2 size={13} />}
                  </button>
                </div>
              </div>

              {/* Code lines */}
              <div
                style={{
                  background: '#090d16',
                  padding: '12px 0',
                  maxHeight: isExpandedCode ? '520px' : '380px',
                  overflowY: 'auto',
                  fontFamily: 'Consolas, Monaco, "Courier New", monospace',
                  fontSize: '0.825rem',
                  lineHeight: '1.5'
                }}
              >
                {scenarioDetail.code_snippet?.split('\n').map((line, idx) => {
                  const isComment = line.trim().startsWith('#');
                  const isBugHighlight = line.includes('BUG');
                  return (
                    <div
                      key={idx}
                      style={{
                        display: 'flex',
                        padding: '1px 12px',
                        background: isBugHighlight ? 'rgba(239, 68, 68, 0.12)' : 'transparent',
                        borderLeft: isBugHighlight ? '3px solid #ef4444' : '3px solid transparent'
                      }}
                    >
                      <span style={{ width: '32px', color: '#475569', textAlign: 'right', marginRight: '14px', userSelect: 'none', fontSize: '0.75rem' }}>
                        {idx + 1}
                      </span>
                      <span
                        style={{
                          color: isBugHighlight ? '#fca5a5' : isComment ? '#64748b' : '#e2e8f0',
                          whiteSpace: 'pre',
                          wordBreak: 'break-all'
                        }}
                      >
                        {line}
                      </span>
                    </div>
                  );
                })}
              </div>
            </div>

            {/* Telemetry Metrics Log & Progressive Hints */}
            <div style={{ display: 'flex', flexDirection: 'column', gap: 16 }}>
              {/* Telemetry Log */}
              <div className="card" style={{ background: 'var(--bg-secondary)', margin: 0 }}>
                <div style={{ fontSize: '0.75rem', fontWeight: 700, color: 'var(--text-muted)', textTransform: 'uppercase', marginBottom: 10, letterSpacing: '0.04em' }}>
                  Model Telemetry Log
                </div>
                <div style={{ display: 'flex', flexDirection: 'column', gap: 6 }}>
                  {Object.entries(scenarioDetail.metrics_log || {}).map(([key, val]) => (
                    <div
                      key={key}
                      style={{
                        display: 'flex',
                        justifyContent: 'space-between',
                        fontSize: '0.825rem',
                        padding: '6px 0',
                        borderBottom: '1px solid var(--border-subtle)'
                      }}
                    >
                      <span style={{ color: 'var(--text-muted)' }}>{key}:</span>
                      <b style={{ color: 'var(--text-primary)', fontFamily: 'monospace' }}>{val}</b>
                    </div>
                  ))}
                </div>
              </div>

              {/* Progressive Hints Unlock Card */}
              <div className="card" style={{ background: 'var(--bg-secondary)', margin: 0 }}>
                <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: 10 }}>
                  <div style={{ fontSize: '0.75rem', fontWeight: 700, color: '#fbbf24', textTransform: 'uppercase', display: 'flex', alignItems: 'center', gap: 5 }}>
                    <Lightbulb size={13} />
                    Diagnostic Hints
                  </div>
                  <span style={{ fontSize: '0.75rem', color: 'var(--text-muted)' }}>
                    {unlockedHintsCount} / {scenarioDetail.hints?.length || 0} unlocked
                  </span>
                </div>

                {unlockedHintsCount < (scenarioDetail.hints?.length || 0) && (
                  <button onClick={handleUnlockHint} className="btn btn-secondary btn-sm" style={{ width: '100%', marginBottom: 10 }}>
                    <Lightbulb size={14} style={{ color: '#fbbf24' }} />
                    <span>Unlock Next Hint ({unlockedHintsCount + 1}/{scenarioDetail.hints.length})</span>
                  </button>
                )}

                <div style={{ display: 'flex', flexDirection: 'column', gap: 8 }}>
                  {scenarioDetail.hints?.slice(0, unlockedHintsCount).map((hint, idx) => (
                    <div
                      key={idx}
                      style={{
                        padding: 10,
                        borderRadius: 6,
                        background: 'rgba(245, 158, 11, 0.08)',
                        border: '1px solid rgba(245, 158, 11, 0.2)',
                        fontSize: '0.8rem',
                        color: '#fbbf24',
                        lineHeight: 1.4
                      }}
                    >
                      <b>Hint {idx + 1}:</b> {hint}
                    </div>
                  ))}
                  {unlockedHintsCount === 0 && (
                    <p style={{ fontSize: '0.785rem', color: 'var(--text-muted)', margin: 0, fontStyle: 'italic' }}>
                      Stuck? Click "Unlock Next Hint" above to reveal progressive diagnostic clues without penalty.
                    </p>
                  )}
                </div>
              </div>
            </div>
          </div>

          {/* Diagnostic Diagnosis Selection Card */}
          <div className="card" style={{ borderTop: '4px solid var(--accent-primary)', background: 'var(--bg-secondary)' }}>
            <h3 style={{ fontSize: '1.1rem', fontWeight: 700, marginBottom: 14, display: 'flex', alignItems: 'center', gap: 8 }}>
              <Sparkles size={16} style={{ color: 'var(--accent-primary)' }} />
              Select Root Cause Diagnosis:
            </h3>

            <div style={{ display: 'flex', flexDirection: 'column', gap: 10, marginBottom: 20 }}>
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
                    style={{ margin: 0, padding: '14px 16px' }}
                  >
                    <div style={{ display: 'flex', alignItems: 'flex-start', gap: 10 }}>
                      <span
                        style={{
                          display: 'inline-flex',
                          alignItems: 'center',
                          justifyContent: 'center',
                          width: 22,
                          height: 22,
                          borderRadius: '50%',
                          background: isSelected ? 'var(--accent-primary)' : 'var(--bg-tertiary)',
                          color: isSelected ? '#ffffff' : 'var(--text-muted)',
                          fontSize: '0.75rem',
                          fontWeight: 700,
                          flexShrink: 0
                        }}
                      >
                        {String.fromCharCode(65 + idx)}
                      </span>
                      <span style={{ fontSize: '0.875rem', lineHeight: 1.45 }}>{opt}</span>
                    </div>
                  </div>
                );
              })}
            </div>

            {/* Evaluation Result Feedback */}
            {evaluationResult && (
              <div
                style={{
                  padding: 18,
                  borderRadius: 'var(--radius-md)',
                  background: evaluationResult.is_correct ? 'rgba(16, 185, 129, 0.08)' : 'rgba(239, 68, 68, 0.08)',
                  borderLeft: `4px solid ${evaluationResult.is_correct ? '#10b981' : '#ef4444'}`,
                  marginBottom: 20
                }}
              >
                <div style={{ display: 'flex', alignItems: 'center', gap: 8, fontWeight: 700, color: evaluationResult.is_correct ? '#34d399' : '#f87171', marginBottom: 8, fontSize: '1rem' }}>
                  {evaluationResult.is_correct ? <CheckCircle2 size={20} /> : <XCircle size={20} />}
                  <span>{evaluationResult.is_correct ? `Diagnosis Confirmed! (+${evaluationResult.points_earned} XP)` : 'Incorrect Root Cause'}</span>
                </div>
                <p style={{ fontSize: '0.875rem', color: 'var(--text-primary)', marginBottom: 14, lineHeight: 1.5 }}>
                  {evaluationResult.explanation}
                </p>

                <div style={{ fontSize: '0.75rem', fontWeight: 700, color: '#38bdf8', textTransform: 'uppercase', marginBottom: 6, letterSpacing: '0.04em' }}>
                  Verified Production Fix:
                </div>
                <pre style={{ background: '#070a13', padding: 14, borderRadius: 8, fontSize: '0.825rem', color: '#38bdf8', overflowX: 'auto', margin: 0, border: '1px solid rgba(56, 189, 248, 0.2)' }}>
                  <code>{evaluationResult.fix_code_snippet}</code>
                </pre>
              </div>
            )}

            {!evaluationResult ? (
              <button
                onClick={handleSubmitDiagnosis}
                className="btn btn-primary"
                disabled={submitting || selectedOption === null}
                style={{ width: '100%', maxWidth: '240px', padding: '10px 20px', fontSize: '0.9rem' }}
              >
                {submitting ? 'Verifying Diagnosis...' : 'Submit Diagnosis'}
              </button>
            ) : (
              <button
                onClick={() => {
                  setSelectedOption(null);
                  setEvaluationResult(null);
                  setUnlockedHintsCount(0);
                }}
                className="btn btn-secondary"
                style={{ width: '100%', maxWidth: '200px' }}
              >
                <RefreshCw size={14} />
                <span>Retry Challenge</span>
              </button>
            )}
          </div>
        </div>
      )}
    </div>
  );
}
