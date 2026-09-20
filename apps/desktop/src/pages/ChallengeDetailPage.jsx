import React, { useState, useEffect, useRef } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import { 
  ArrowLeft, Play, Lightbulb, CheckCircle2, XCircle, Award, Code2, Lock, 
  Terminal as TerminalIcon, GitBranch, GitCommit, GitPullRequest, RotateCcw, 
  Sparkles, Check, ChevronRight, HelpCircle, ShieldAlert, Cpu
} from 'lucide-react';
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

  // Terminal & Git Challenge State
  const [activeStepIdx, setActiveStepIdx] = useState(0);
  const [completedSteps, setCompletedSteps] = useState([]);
  const [terminalInput, setTerminalInput] = useState('');
  const [terminalHistory, setTerminalHistory] = useState([]);
  const [historyPointer, setHistoryPointer] = useState(-1);
  const [commandLog, setCommandLog] = useState([
    { type: 'system', text: '⚡ Interactive Git & GitHub Challenge Terminal Ready.' },
    { type: 'info', text: 'Read the situational mission on the left, then enter the appropriate command below.' }
  ]);
  const [isChallengeCompleted, setIsChallengeCompleted] = useState(false);
  const [activeBranch, setActiveBranch] = useState('main');
  const terminalEndRef = useRef(null);

  useEffect(() => {
    async function loadDetail() {
      try {
        setLoading(true);
        const data = await challengeService.getChallenge(challengeId);
        setChallenge(data);
        setCode(data.starter_code || '');
        setGradingResult(null);
        setUnlockedHintsCount(0);
        setActiveStepIdx(0);
        setCompletedSteps([]);
        setIsChallengeCompleted(false);

        // Set initial branch based on challenge
        if (data.id === 'git-fast-forward') setActiveBranch('main');
        else if (data.id === 'git-merge-base') setActiveBranch('feature/analytics');
        else if (data.id === 'github-pr-conflict-detector') setActiveBranch('feature/search-filters');
        else setActiveBranch('main');

        setCommandLog([
          { type: 'system', text: `⚡ Interactive Git & GitHub Challenge Terminal: [${data.title}]` },
          { type: 'info', text: 'Read the situational mission on the left, then type your Git/GitHub command below.' }
        ]);
      } catch (err) {
        console.error('Failed to load challenge:', err);
      } finally {
        setLoading(false);
      }
    }
    loadDetail();
  }, [challengeId]);

  useEffect(() => {
    terminalEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [commandLog]);

  const isGitChallenge = challenge?.challenge_type === 'git-terminal' || challenge?.domain === 'github';
  const scenarios = challenge?.scenarios || [];
  const currentScenario = scenarios[activeStepIdx] || null;

  const handleSubmitPython = async () => {
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
    const totalHints = isGitChallenge ? scenarios.length : (challenge?.hints?.length || 0);
    if (challenge && unlockedHintsCount < totalHints) {
      setUnlockedHintsCount((prev) => prev + 1);
    }
  };

  const handleTerminalKeyDown = (e) => {
    if (e.key === 'ArrowUp') {
      e.preventDefault();
      if (terminalHistory.length > 0) {
        const nextPtr = historyPointer === -1 ? terminalHistory.length - 1 : Math.max(0, historyPointer - 1);
        setHistoryPointer(nextPtr);
        setTerminalInput(terminalHistory[nextPtr]);
      }
    } else if (e.key === 'ArrowDown') {
      e.preventDefault();
      if (terminalHistory.length > 0 && historyPointer !== -1) {
        const nextPtr = historyPointer + 1;
        if (nextPtr >= terminalHistory.length) {
          setHistoryPointer(-1);
          setTerminalInput('');
        } else {
          setHistoryPointer(nextPtr);
          setTerminalInput(terminalHistory[nextPtr]);
        }
      }
    } else if (e.key === 'Enter') {
      e.preventDefault();
      executeTerminalCommand(terminalInput);
    }
  };

  const executeTerminalCommand = async (rawCmd) => {
    const cmd = rawCmd.trim();
    if (!cmd) return;

    setTerminalHistory((prev) => [...prev, cmd]);
    setHistoryPointer(-1);
    setTerminalInput('');

    // Append user command line
    const newLog = [...commandLog, { type: 'prompt', text: `(repo: ${activeBranch}) $ ${cmd}` }];

    if (cmd === 'clear') {
      setCommandLog([{ type: 'system', text: '⚡ Terminal cleared. Continue your mission below.' }]);
      return;
    }

    if (!currentScenario) {
      newLog.push({ type: 'output', text: 'All mission steps completed! Great work.' });
      setCommandLog(newLog);
      return;
    }

    // Check if command matches accepted patterns for the current active step
    const patterns = currentScenario.accepted_patterns || [];
    let isMatch = false;

    for (const pattern of patterns) {
      try {
        const regex = new RegExp(pattern, 'i');
        if (regex.test(cmd)) {
          isMatch = true;
          break;
        }
      } catch {
        if (cmd.toLowerCase() === pattern.toLowerCase()) {
          isMatch = true;
          break;
        }
      }
    }

    if (isMatch) {
      // Dynamic branch tracking on checkout/switch
      if (cmd.includes('checkout -b') || cmd.includes('switch -c')) {
        const parts = cmd.split(/\s+/);
        const branchName = parts[parts.length - 1];
        if (branchName) setActiveBranch(branchName);
      } else if (cmd.includes('checkout') || cmd.includes('switch')) {
        const parts = cmd.split(/\s+/);
        const branchName = parts[parts.length - 1];
        if (branchName && !branchName.startsWith('-')) setActiveBranch(branchName);
      }

      // Success output
      newLog.push({ 
        type: 'success', 
        text: `✔ [STEP ${currentScenario.step} SUCCESS]: ${currentScenario.success_message}` 
      });

      const nextCompleted = [...completedSteps, currentScenario.step];
      setCompletedSteps(nextCompleted);

      if (activeStepIdx + 1 < scenarios.length) {
        const nextIdx = activeStepIdx + 1;
        setActiveStepIdx(nextIdx);
        newLog.push({ 
          type: 'info', 
          text: `🎯 NEXT MISSION (Step ${scenarios[nextIdx].step}/${scenarios.length}): ${scenarios[nextIdx].title}` 
        });
      } else {
        // All steps completed
        setIsChallengeCompleted(true);
        newLog.push({ 
          type: 'celebration', 
          text: `🎉 CONGRATULATIONS! You completed all ${scenarios.length} situational steps for "${challenge.title}"!` 
        });
        newLog.push({
          type: 'system',
          text: `🏆 +${challenge.xp_reward} XP added to your Git & GitHub Mastery profile.`
        });

        // Trigger auto-grade submission for completion credit
        try {
          await challengeService.submitChallenge(challengeId, '# git challenge completed via situational terminal');
        } catch (e) {
          console.warn('Backend completion sync:', e);
        }
      }
    } else {
      // Provide intelligent real-world Git simulation feedback
      let simulatedResponse = '';
      if (cmd.startsWith('git status')) {
        simulatedResponse = `On branch ${activeBranch}\nChanges to be committed: (review scenario requirements)\nUse "git help" for more info.`;
      } else if (cmd.startsWith('git log')) {
        simulatedResponse = `* 4f82a91 (HEAD -> ${activeBranch}) Current situational head\n* 1a2b3c4 Initial commit`;
      } else if (cmd.startsWith('git branch')) {
        simulatedResponse = `* ${activeBranch}\n  main\n  feature/auth`;
      } else if (cmd.startsWith('gh pr list')) {
        simulatedResponse = `Showing 3 open pull requests in owner/repository:\n#42  Add token validation  feature/auth  OPEN`;
      } else {
        simulatedResponse = `Command executed: "${cmd}". However, this did not satisfy Step ${currentScenario.step}: "${currentScenario.title}". Check instructions or hint!`;
      }
      newLog.push({ type: 'warning', text: simulatedResponse });
    }

    setCommandLog(newLog);
  };

  const resetInteractiveChallenge = () => {
    setActiveStepIdx(0);
    setCompletedSteps([]);
    setIsChallengeCompleted(false);
    setActiveBranch('main');
    setCommandLog([
      { type: 'system', text: `🔄 Challenge reset to Step 1.` },
      { type: 'info', text: 'Read the situational mission on the left, then enter your command below.' }
    ]);
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
          <div style={{ borderLeft: '1px solid var(--border-subtle)', paddingLeft: 12, display: 'flex', alignItems: 'center', gap: 10 }}>
            <h1 style={{ fontSize: '1.35rem', margin: 0 }}>{challenge.title}</h1>
            <Badge variant={challenge.domain === 'github' ? 'blue' : 'purple'}>{challenge.category}</Badge>
            <span style={{ fontSize: '0.75rem', color: 'var(--text-muted)' }}>Difficulty: {challenge.difficulty}</span>
          </div>
        </div>

        <div style={{ display: 'flex', alignItems: 'center', gap: 12 }}>
          <span className="badge badge-amber">+{challenge.xp_reward} XP</span>
          {isGitChallenge ? (
            <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
              <button 
                onClick={resetInteractiveChallenge} 
                className="btn btn-ghost btn-sm"
                title="Reset Challenge"
                style={{ gap: 6 }}
              >
                <RotateCcw size={14} /> Reset
              </button>
              {isChallengeCompleted ? (
                <div style={{ display: 'flex', alignItems: 'center', gap: 6, background: '#10b98120', color: '#10b981', padding: '6px 14px', borderRadius: 8, fontWeight: 700, border: '1px solid #10b98150' }}>
                  <CheckCircle2 size={16} /> Completed (+{challenge.xp_reward} XP)
                </div>
              ) : (
                <div style={{ display: 'flex', alignItems: 'center', gap: 6, background: 'var(--bg-secondary)', padding: '6px 12px', borderRadius: 8, fontSize: '0.85rem', color: 'var(--text-secondary)' }}>
                  <TerminalIcon size={14} />
                  <span>Step {activeStepIdx + 1} of {scenarios.length}</span>
                </div>
              )}
            </div>
          ) : (
            <button
              onClick={handleSubmitPython}
              className="btn btn-primary"
              disabled={submitting}
              style={{ padding: '8px 20px', gap: 8 }}
            >
              <Play size={16} fill="currentColor" />
              <span>{submitting ? 'Autograding...' : 'Submit & Autograde'}</span>
            </button>
          )}
        </div>
      </div>

      {/* Workspace Area */}
      {isGitChallenge ? (
        /* Git & GitHub Situational Interactive Workspace */
        <div style={{ flex: 1, display: 'grid', gridTemplateColumns: '1.1fr 1.3fr', gap: 16, minHeight: 0 }}>
          {/* Left Column: Situational Mission, Step Road-map & Live Visualization */}
          <div style={{ display: 'flex', flexDirection: 'column', gap: 14, overflowY: 'auto', paddingRight: 4 }}>
            
            {/* Situational Context Card */}
            <div className="card" style={{ padding: 18, borderLeft: '4px solid #3b82f6' }}>
              <div style={{ display: 'flex', alignItems: 'center', gap: 8, marginBottom: 8 }}>
                <span style={{ fontSize: '0.8rem', textTransform: 'uppercase', fontWeight: 800, color: '#3b82f6', letterSpacing: 0.5 }}>
                  Real-World Scenario
                </span>
              </div>
              <div style={{ fontSize: '0.88rem', lineHeight: 1.6, color: 'var(--text-secondary)', whiteSpace: 'pre-line' }}>
                {challenge.problem_statement}
              </div>
            </div>

            {/* Multi-Step Mission Roadmap */}
            <div className="card" style={{ padding: 18 }}>
              <h3 style={{ fontSize: '0.95rem', marginBottom: 12, display: 'flex', alignItems: 'center', gap: 8 }}>
                <GitBranch size={16} style={{ color: '#6366f1' }} />
                <span>Mission Objectives Checklist ({completedSteps.length}/{scenarios.length})</span>
              </h3>

              <div style={{ display: 'flex', flexDirection: 'column', gap: 10 }}>
                {scenarios.map((sc, idx) => {
                  const isDone = completedSteps.includes(sc.step);
                  const isCurrent = activeStepIdx === idx && !isDone;
                  const isLocked = !isDone && !isCurrent;

                  return (
                    <div
                      key={sc.step}
                      style={{
                        padding: '12px 14px',
                        borderRadius: 8,
                        background: isCurrent 
                          ? 'rgba(59, 130, 246, 0.1)' 
                          : isDone 
                            ? 'rgba(16, 185, 129, 0.08)' 
                            : 'var(--bg-secondary)',
                        border: isCurrent 
                          ? '1px solid rgba(59, 130, 246, 0.4)' 
                          : isDone 
                            ? '1px solid rgba(16, 185, 129, 0.25)' 
                            : '1px solid var(--border-subtle)',
                        display: 'flex',
                        flexDirection: 'column',
                        gap: 4
                      }}
                    >
                      <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between' }}>
                        <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                          {isDone ? (
                            <div style={{ background: '#10b981', color: '#fff', borderRadius: '50%', width: 20, height: 20, display: 'flex', alignItems: 'center', justifyContent: 'center', fontSize: '0.7rem' }}>
                              <Check size={12} strokeWidth={3} />
                            </div>
                          ) : isCurrent ? (
                            <div style={{ background: '#3b82f6', color: '#fff', borderRadius: '50%', width: 20, height: 20, display: 'flex', alignItems: 'center', justifyContent: 'center', fontSize: '0.75rem', fontWeight: 800 }}>
                              {sc.step}
                            </div>
                          ) : (
                            <div style={{ background: 'var(--border-subtle)', color: 'var(--text-muted)', borderRadius: '50%', width: 20, height: 20, display: 'flex', alignItems: 'center', justifyContent: 'center', fontSize: '0.75rem' }}>
                              <Lock size={11} />
                            </div>
                          )}
                          <span style={{ fontWeight: 700, fontSize: '0.88rem', color: isCurrent ? 'var(--text-primary)' : isDone ? '#10b981' : 'var(--text-muted)' }}>
                            Step {sc.step}: {sc.title}
                          </span>
                        </div>

                        {isDone && <span style={{ fontSize: '0.75rem', color: '#10b981', fontWeight: 700 }}>Passed</span>}
                        {isCurrent && <span style={{ fontSize: '0.75rem', color: '#3b82f6', fontWeight: 700 }}>Active</span>}
                      </div>

                      <div style={{ fontSize: '0.82rem', color: isLocked ? 'var(--text-muted)' : 'var(--text-secondary)', marginLeft: 28, marginTop: 2 }}>
                        {sc.instruction}
                      </div>
                    </div>
                  );
                })}
              </div>
            </div>

            {/* Interactive Visual DAG & Staging Preview Rail */}
            <div className="card" style={{ padding: 16 }}>
              <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', marginBottom: 10 }}>
                <span style={{ fontSize: '0.85rem', fontWeight: 700, color: 'var(--text-primary)', display: 'flex', alignItems: 'center', gap: 6 }}>
                  <GitCommit size={15} style={{ color: '#8b5cf6' }} /> Live Repository State Visualizer
                </span>
                <span style={{ fontSize: '0.75rem', color: 'var(--text-muted)', fontFamily: 'var(--font-mono)' }}>
                  HEAD ➔ {activeBranch}
                </span>
              </div>

              <div style={{ padding: '14px', background: 'var(--bg-secondary)', borderRadius: 8, border: '1px solid var(--border-subtle)', display: 'flex', flexDirection: 'column', gap: 10 }}>
                {/* Visual Branch Nodes */}
                <div style={{ display: 'flex', alignItems: 'center', gap: 8, overflowX: 'auto', paddingBottom: 4 }}>
                  <div style={{ display: 'flex', alignItems: 'center', gap: 6, padding: '6px 12px', background: 'rgba(59, 130, 246, 0.15)', borderRadius: 6, border: '1px solid #3b82f6', fontSize: '0.8rem', fontWeight: 600, color: '#60a5fa' }}>
                    <GitBranch size={13} />
                    <span>main (c1)</span>
                  </div>

                  <span style={{ color: 'var(--text-muted)', fontSize: '0.8rem' }}>➔</span>

                  <div style={{ display: 'flex', alignItems: 'center', gap: 6, padding: '6px 12px', background: completedSteps.length >= 1 ? 'rgba(16, 185, 129, 0.15)' : 'rgba(255, 255, 255, 0.05)', borderRadius: 6, border: completedSteps.length >= 1 ? '1px solid #10b981' : '1px dashed var(--border-subtle)', fontSize: '0.8rem', fontWeight: 600, color: completedSteps.length >= 1 ? '#34d399' : 'var(--text-muted)' }}>
                    <GitCommit size={13} />
                    <span>{activeBranch !== 'main' ? activeBranch : 'feature'} (c2)</span>
                  </div>

                  {scenarios.length > 2 && (
                    <>
                      <span style={{ color: 'var(--text-muted)', fontSize: '0.8rem' }}>➔</span>
                      <div style={{ display: 'flex', alignItems: 'center', gap: 6, padding: '6px 12px', background: completedSteps.length >= 2 ? 'rgba(139, 92, 246, 0.15)' : 'rgba(255, 255, 255, 0.05)', borderRadius: 6, border: completedSteps.length >= 2 ? '1px solid #8b5cf6' : '1px dashed var(--border-subtle)', fontSize: '0.8rem', fontWeight: 600, color: completedSteps.length >= 2 ? '#a78bfa' : 'var(--text-muted)' }}>
                        <GitPullRequest size={13} />
                        <span>{challenge.domain === 'github' ? 'PR #42' : 'merged'}</span>
                      </div>
                    </>
                  )}
                </div>

                <div style={{ fontSize: '0.78rem', color: 'var(--text-muted)', display: 'flex', justifyContent: 'space-between', alignItems: 'center', borderTop: '1px solid var(--border-subtle)', paddingTop: 8 }}>
                  <span>Status: {isChallengeCompleted ? '🎉 Complete & Verified' : `Working on Step ${activeStepIdx + 1}`}</span>
                  <span style={{ color: '#10b981', fontWeight: 600 }}>{completedSteps.length} of {scenarios.length} actions verified</span>
                </div>
              </div>
            </div>

            {/* Hint Box */}
            {currentScenario && currentScenario.hint && (
              <div className="card" style={{ padding: 14 }}>
                <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: unlockedHintsCount > activeStepIdx ? 8 : 0 }}>
                  <div style={{ display: 'flex', alignItems: 'center', gap: 6 }}>
                    <Lightbulb size={15} style={{ color: '#fbbf24' }} />
                    <h4 style={{ fontSize: '0.85rem', margin: 0 }}>Step {currentScenario.step} Hint</h4>
                  </div>
                  {unlockedHintsCount <= activeStepIdx && (
                    <button onClick={handleUnlockHint} className="btn btn-secondary btn-sm" style={{ padding: '3px 10px', fontSize: '0.75rem' }}>
                      Unlock Hint
                    </button>
                  )}
                </div>

                {unlockedHintsCount > activeStepIdx && (
                  <div style={{ padding: '8px 12px', borderRadius: 6, background: 'rgba(245, 158, 11, 0.1)', border: '1px solid rgba(245, 158, 11, 0.25)', fontSize: '0.8rem', color: '#fbbf24' }}>
                    {currentScenario.hint}
                  </div>
                )}
              </div>
            )}

          </div>

          {/* Right Column: Interactive Git Terminal & Quick Actions */}
          <div style={{ display: 'flex', flexDirection: 'column', gap: 12, minHeight: 0 }}>
            {/* Terminal Card */}
            <div 
              className="card" 
              style={{ 
                flex: 1, 
                padding: 0, 
                display: 'flex', 
                flexDirection: 'column', 
                background: 'var(--color-neutral-900, #0f172a)', 
                border: '1px solid var(--border-subtle)', 
                overflow: 'hidden',
                boxShadow: '0 8px 30px rgba(0,0,0,0.3)'
              }}
            >
              {/* Terminal Title Bar */}
              <div 
                style={{ 
                  padding: '8px 14px', 
                  background: '#1e293b', 
                  borderBottom: '1px solid #334155', 
                  display: 'flex', 
                  justifyContent: 'space-between', 
                  alignItems: 'center' 
                }}
              >
                <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                  <div style={{ display: 'flex', gap: 6 }}>
                    <span style={{ width: 10, height: 10, borderRadius: '50%', background: '#ef4444', display: 'inline-block' }}></span>
                    <span style={{ width: 10, height: 10, borderRadius: '50%', background: '#f59e0b', display: 'inline-block' }}></span>
                    <span style={{ width: 10, height: 10, borderRadius: '50%', background: '#10b981', display: 'inline-block' }}></span>
                  </div>
                  <span style={{ fontSize: '0.78rem', color: '#94a3b8', fontFamily: 'var(--font-mono)', marginLeft: 6 }}>
                    git-bash • {activeBranch}
                  </span>
                </div>

                <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                  <button 
                    onClick={() => setCommandLog([{ type: 'system', text: '⚡ Terminal cleared.' }])} 
                    className="btn btn-ghost btn-sm"
                    style={{ fontSize: '0.75rem', padding: '2px 8px', color: '#94a3b8' }}
                  >
                    Clear
                  </button>
                </div>
              </div>

              {/* Terminal Logs Window */}
              <div 
                style={{ 
                  flex: 1, 
                  padding: 16, 
                  overflowY: 'auto', 
                  fontFamily: 'var(--font-mono, monospace)', 
                  fontSize: '0.85rem', 
                  lineHeight: 1.6,
                  display: 'flex',
                  flexDirection: 'column',
                  gap: 8
                }}
              >
                {commandLog.map((log, idx) => {
                  let color = '#e2e8f0';
                  let bg = 'transparent';
                  let padding = '0';
                  let borderRadius = '0';

                  if (log.type === 'system') {
                    color = '#38bdf8';
                  } else if (log.type === 'info') {
                    color = '#94a3b8';
                  } else if (log.type === 'prompt') {
                    color = '#34d399';
                  } else if (log.type === 'success') {
                    color = '#10b981';
                    bg = 'rgba(16, 185, 129, 0.12)';
                    padding = '6px 10px';
                    borderRadius = '4px';
                  } else if (log.type === 'warning') {
                    color = '#f87171';
                  } else if (log.type === 'celebration') {
                    color = '#fbbf24';
                    bg = 'rgba(245, 158, 11, 0.15)';
                    padding = '8px 12px';
                    borderRadius = '6px';
                  }

                  return (
                    <div 
                      key={idx} 
                      style={{ 
                        color, 
                        background: bg, 
                        padding, 
                        borderRadius, 
                        whiteSpace: 'pre-wrap', 
                        wordBreak: 'break-word' 
                      }}
                    >
                      {log.text}
                    </div>
                  );
                })}
                <div ref={terminalEndRef} />
              </div>

              {/* Terminal Input Bar */}
              <div 
                style={{ 
                  padding: '10px 14px', 
                  background: '#0b1120', 
                  borderTop: '1px solid #1e293b', 
                  display: 'flex', 
                  alignItems: 'center', 
                  gap: 8 
                }}
              >
                <span style={{ color: '#10b981', fontFamily: 'var(--font-mono)', fontWeight: 700, fontSize: '0.88rem' }}>
                  $
                </span>
                <input
                  type="text"
                  value={terminalInput}
                  onChange={(e) => setTerminalInput(e.target.value)}
                  onKeyDown={handleTerminalKeyDown}
                  placeholder={currentScenario ? `Type Git command for Step ${currentScenario.step}...` : "All steps completed!"}
                  style={{
                    flex: 1,
                    background: 'transparent',
                    border: 'none',
                    outline: 'none',
                    color: '#f8fafc',
                    fontFamily: 'var(--font-mono, monospace)',
                    fontSize: '0.88rem'
                  }}
                  autoFocus
                />
                <button
                  onClick={() => executeTerminalCommand(terminalInput)}
                  className="btn btn-primary btn-sm"
                  style={{ padding: '4px 12px', fontSize: '0.78rem' }}
                >
                  Run
                </button>
              </div>
            </div>

            {/* Quick-Help Hint Pills for Fast Interaction */}
            {currentScenario && (
              <div className="card" style={{ padding: '10px 14px' }}>
                <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', marginBottom: 6 }}>
                  <span style={{ fontSize: '0.78rem', color: 'var(--text-muted)', fontWeight: 600 }}>
                    💡 Suggested Command Starters for Step {currentScenario.step}:
                  </span>
                  <span style={{ fontSize: '0.72rem', color: 'var(--text-muted)' }}>Click pill to load</span>
                </div>
                <div style={{ display: 'flex', flexWrap: 'wrap', gap: 6 }}>
                  {challenge.id === 'git-fast-forward' && (
                    <>
                      <button onClick={() => setTerminalInput('git checkout -b feature/auth')} className="btn btn-secondary btn-sm" style={{ fontSize: '0.75rem', fontFamily: 'var(--font-mono)' }}>git checkout -b feature/auth</button>
                      <button onClick={() => setTerminalInput('git commit -m "feat: implement jwt auth token"')} className="btn btn-secondary btn-sm" style={{ fontSize: '0.75rem', fontFamily: 'var(--font-mono)' }}>git commit -m "feat: auth"</button>
                      <button onClick={() => setTerminalInput('git checkout main')} className="btn btn-secondary btn-sm" style={{ fontSize: '0.75rem', fontFamily: 'var(--font-mono)' }}>git checkout main</button>
                      <button onClick={() => setTerminalInput('git merge feature/auth')} className="btn btn-secondary btn-sm" style={{ fontSize: '0.75rem', fontFamily: 'var(--font-mono)' }}>git merge feature/auth</button>
                    </>
                  )}
                  {challenge.id === 'git-merge-base' && (
                    <>
                      <button onClick={() => setTerminalInput('git merge-base main feature/analytics')} className="btn btn-secondary btn-sm" style={{ fontSize: '0.75rem', fontFamily: 'var(--font-mono)' }}>git merge-base main feature/analytics</button>
                      <button onClick={() => setTerminalInput('git merge feature/analytics')} className="btn btn-secondary btn-sm" style={{ fontSize: '0.75rem', fontFamily: 'var(--font-mono)' }}>git merge feature/analytics</button>
                      <button onClick={() => setTerminalInput('git log --graph --oneline --all')} className="btn btn-secondary btn-sm" style={{ fontSize: '0.75rem', fontFamily: 'var(--font-mono)' }}>git log --graph</button>
                    </>
                  )}
                  {challenge.id === 'github-pr-conflict-detector' && (
                    <>
                      <button onClick={() => setTerminalInput('gh pr view 42')} className="btn btn-secondary btn-sm" style={{ fontSize: '0.75rem', fontFamily: 'var(--font-mono)' }}>gh pr view 42</button>
                      <button onClick={() => setTerminalInput('git merge main')} className="btn btn-secondary btn-sm" style={{ fontSize: '0.75rem', fontFamily: 'var(--font-mono)' }}>git merge main</button>
                      <button onClick={() => setTerminalInput('git add src/filters.py')} className="btn btn-secondary btn-sm" style={{ fontSize: '0.75rem', fontFamily: 'var(--font-mono)' }}>git add src/filters.py</button>
                      <button onClick={() => setTerminalInput('git push origin feature/search-filters')} className="btn btn-secondary btn-sm" style={{ fontSize: '0.75rem', fontFamily: 'var(--font-mono)' }}>git push origin feature/search-filters</button>
                    </>
                  )}
                  {challenge.id === 'github-actions-matrix' && (
                    <>
                      <button onClick={() => setTerminalInput('mkdir -p .github/workflows')} className="btn btn-secondary btn-sm" style={{ fontSize: '0.75rem', fontFamily: 'var(--font-mono)' }}>mkdir -p .github/workflows</button>
                      <button onClick={() => setTerminalInput('git add .github/workflows/ci.yml')} className="btn btn-secondary btn-sm" style={{ fontSize: '0.75rem', fontFamily: 'var(--font-mono)' }}>git add .github/workflows/ci.yml</button>
                      <button onClick={() => setTerminalInput('gh workflow run ci.yml')} className="btn btn-secondary btn-sm" style={{ fontSize: '0.75rem', fontFamily: 'var(--font-mono)' }}>gh workflow run ci.yml</button>
                    </>
                  )}
                  {challenge.id === 'git-blob-hasher' && (
                    <>
                      <button onClick={() => setTerminalInput('git hash-object -w README.md')} className="btn btn-secondary btn-sm" style={{ fontSize: '0.75rem', fontFamily: 'var(--font-mono)' }}>git hash-object -w README.md</button>
                      <button onClick={() => setTerminalInput('git cat-file -p HEAD:README.md')} className="btn btn-secondary btn-sm" style={{ fontSize: '0.75rem', fontFamily: 'var(--font-mono)' }}>git cat-file -p HEAD:README.md</button>
                      <button onClick={() => setTerminalInput('git verify-pack -v .git/objects/pack/*.idx')} className="btn btn-secondary btn-sm" style={{ fontSize: '0.75rem', fontFamily: 'var(--font-mono)' }}>git verify-pack</button>
                    </>
                  )}
                </div>
              </div>
            )}
          </div>
        </div>
      ) : (
        /* Python / ML Algorithmic Code Editor Workspace */
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
      )}
    </div>
  );
}
