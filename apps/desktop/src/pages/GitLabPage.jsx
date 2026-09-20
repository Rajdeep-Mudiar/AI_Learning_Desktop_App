import React, { useState } from 'react';
import {
  GitBranch,
  GitCommit,
  GitMerge,
  GitPullRequest,
  Terminal,
  Play,
  RotateCcw,
  Sparkles,
  CheckCircle2,
  AlertCircle,
  HelpCircle,
  Layers,
  FileCode,
  ArrowRight,
  ShieldCheck,
  RefreshCw,
  GitFork
} from 'lucide-react';
import Badge from '../components/common/Badge';

export default function GitLabPage() {
  const [activeTab, setActiveTab] = useState('dag-terminal'); // 'three-trees' | 'dag-terminal' | 'rebase-studio' | 'conflict-resolver' | 'cicd-runner'

  // --- Module 1: 3-Trees State ---
  const [workingDirFiles, setWorkingDirFiles] = useState([
    { name: 'auth_middleware.py', status: 'modified' },
    { name: 'routes/billing.py', status: 'untracked' }
  ]);
  const [stagedFiles, setStagedFiles] = useState([]);
  const [repoCommitsCount, setRepoCommitsCount] = useState(4);

  // --- Module 2: DAG Terminal State ---
  const [commits, setCommits] = useState([
    { id: 'c1', hash: 'e4f1a0', message: 'Initial commit', branch: 'main', parent: null },
    { id: 'c2', hash: '7b89d2', message: 'Setup project config', branch: 'main', parent: 'c1' },
    { id: 'c3', hash: '3c19e4', message: 'Add authentication routes', branch: 'feature/auth', parent: 'c2' },
    { id: 'c4', hash: '9a01f8', message: 'JWT token generation', branch: 'feature/auth', parent: 'c3' }
  ]);
  const [branches, setBranches] = useState(['main', 'feature/auth']);
  const [currentBranch, setCurrentBranch] = useState('feature/auth');
  const [commandInput, setCommandInput] = useState('');
  const [history, setHistory] = useState([
    'Welcome to Interactive Git Visualizer Terminal.',
    'Try typing: git commit -m "your message", git branch <name>, git checkout <name>, or git merge <name>'
  ]);

  // --- Module 3: Merge Conflict Resolver State ---
  const [conflictResolved, setConflictResolved] = useState(false);
  const [resolvedContent, setResolvedContent] = useState(null);

  // --- Module 4: CI/CD Pipeline State ---
  const [pipelineSteps, setPipelineSteps] = useState([
    { id: 1, name: '1. Lint & Code Style (Black & Flake8)', status: 'pending' },
    { id: 2, name: '2. Unit & Integration Tests (pytest)', status: 'pending' },
    { id: 3, name: '3. Security Vulnerability Audit (Trivy)', status: 'pending' },
    { id: 4, name: '4. Docker Image Matrix Build & Push', status: 'pending' }
  ]);
  const [pipelineRunning, setPipelineRunning] = useState(false);

  // 3-Trees actions
  const stageAllFiles = () => {
    setStagedFiles([...stagedFiles, ...workingDirFiles]);
    setWorkingDirFiles([]);
  };

  const commitStaged = () => {
    if (stagedFiles.length === 0) return;
    setRepoCommitsCount(prev => prev + 1);
    setStagedFiles([]);
  };

  const resetThreeTrees = () => {
    setWorkingDirFiles([
      { name: 'auth_middleware.py', status: 'modified' },
      { name: 'routes/billing.py', status: 'untracked' }
    ]);
    setStagedFiles([]);
  };

  // DAG command execution
  const handleCommand = (e) => {
    e.preventDefault();
    const cmd = commandInput.trim();
    if (!cmd) return;

    setHistory(prev => [...prev, `$ ${cmd}`]);
    setCommandInput('');

    if (cmd.startsWith('git commit')) {
      const match = cmd.match(/-m\s+["'](.*?)["']/);
      const msg = match ? match[1] : 'Update codebase';
      const newHash = Math.random().toString(16).substring(2, 8);
      const parentId = commits[commits.length - 1].id;
      const newCommit = {
        id: `c${commits.length + 1}`,
        hash: newHash,
        message: msg,
        branch: currentBranch,
        parent: parentId
      };
      setCommits(prev => [...prev, newCommit]);
      setHistory(prev => [...prev, `[${currentBranch} ${newHash}] ${msg}`]);
    } else if (cmd.startsWith('git branch ')) {
      const newBranch = cmd.replace('git branch ', '').trim();
      if (!branches.includes(newBranch)) {
        setBranches(prev => [...prev, newBranch]);
        setHistory(prev => [...prev, `Created branch '${newBranch}'`]);
      } else {
        setHistory(prev => [...prev, `fatal: A branch named '${newBranch}' already exists.`]);
      }
    } else if (cmd.startsWith('git checkout ') || cmd.startsWith('git switch ')) {
      const target = cmd.replace('git checkout ', '').replace('git switch ', '').trim();
      if (branches.includes(target)) {
        setCurrentBranch(target);
        setHistory(prev => [...prev, `Switched to branch '${target}'`]);
      } else {
        setHistory(prev => [...prev, `error: pathspec '${target}' did not match any file(s) known to git`]);
      }
    } else if (cmd.startsWith('git merge ')) {
      const sourceBranch = cmd.replace('git merge ', '').trim();
      const newHash = Math.random().toString(16).substring(2, 8);
      const newCommit = {
        id: `c${commits.length + 1}`,
        hash: newHash,
        message: `Merge branch '${sourceBranch}' into ${currentBranch}`,
        branch: currentBranch,
        parent: commits[commits.length - 1].id
      };
      setCommits(prev => [...prev, newCommit]);
      setHistory(prev => [...prev, `Merge made by the 'ort' strategy. [${currentBranch} ${newHash}]`]);
    } else if (cmd === 'clear') {
      setHistory([]);
    } else {
      setHistory(prev => [...prev, `git: '${cmd}' is not a recognized command. Try 'git commit', 'git branch', 'git checkout', 'git merge'`]);
    }
  };

  // CI/CD Runner execution
  const runCicdPipeline = async () => {
    setPipelineRunning(true);
    for (let i = 0; i < pipelineSteps.length; i++) {
      setPipelineSteps(prev => prev.map((s, idx) => idx === i ? { ...s, status: 'running' } : s));
      await new Promise(r => setTimeout(r, 600));
      setPipelineSteps(prev => prev.map((s, idx) => idx === i ? { ...s, status: 'success' } : s));
    }
    setPipelineRunning(false);
  };

  return (
    <div className="animate-fade-in" style={{ paddingBottom: 40 }}>
      {/* Header */}
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', flexWrap: 'wrap', gap: 16, marginBottom: 20 }}>
        <div>
          <div style={{ display: 'flex', alignItems: 'center', gap: 10, marginBottom: 6 }}>
            <Badge variant="yellow"><GitBranch size={14} /> Git & GitHub Studio</Badge>
            <span style={{ fontSize: '0.85rem', color: 'var(--text-muted)' }}>Interactive DAG & DevOps Lab</span>
          </div>
          <h1 style={{ fontSize: '1.85rem', fontWeight: 800 }}>Git & GitHub Interactive Simulations</h1>
          <p style={{ color: 'var(--text-secondary)', fontSize: '0.95rem' }}>
            Learn Git internals through progressive simulations: 3-Tree Working Trees, Directed Acyclic Graph (DAG) Branching, Merge Conflict Resolution, and CI/CD Pipeline Runners.
          </p>
        </div>
      </div>

      {/* Progressive Git Level Tabs */}
      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(200px, 1fr))', gap: 10, marginBottom: 20 }}>
        {[
          { id: 'three-trees', level: 'Basics (Level 1)', title: '1. Git 3-Trees Architecture', color: '#10b981' },
          { id: 'dag-terminal', level: 'Intermediate (Level 2)', title: '2. DAG Branch & Merge Shell', color: '#38bdf8' },
          { id: 'conflict-resolver', level: 'Advanced (Level 3)', title: '3. Merge Conflict Studio', color: '#f59e0b' },
          { id: 'cicd-runner', level: 'DevOps (Level 4)', title: '4. GitHub Actions CI/CD', color: '#8b5cf6' }
        ].map((tab) => {
          const isActive = activeTab === tab.id;
          return (
            <button
              key={tab.id}
              onClick={() => setActiveTab(tab.id)}
              style={{
                background: isActive ? 'var(--bg-card)' : 'var(--bg-tertiary)',
                border: isActive ? `2px solid ${tab.color}` : '1px solid var(--border-color)',
                padding: '10px 14px',
                borderRadius: '12px',
                textAlign: 'left',
                cursor: 'pointer',
                transition: 'all 0.15s ease'
              }}
            >
              <div style={{ fontSize: '0.7rem', fontWeight: 700, color: tab.color, textTransform: 'uppercase' }}>{tab.level}</div>
              <div style={{ fontSize: '0.85rem', fontWeight: 700, color: 'var(--text-primary)', marginTop: 2 }}>{tab.title}</div>
            </button>
          );
        })}
      </div>

      {/* TAB 1: GIT 3-TREES ARCHITECTURE */}
      {activeTab === 'three-trees' && (
        <div style={{ display: 'grid', gap: 20 }}>
          <div className="card" style={{ padding: 24, background: '#090d16', border: '1px solid #1e293b' }}>
            <h3 style={{ fontSize: '1.1rem', fontWeight: 700, marginBottom: 20, display: 'flex', alignItems: 'center', gap: 8 }}>
              <Layers size={18} color="#10b981" /> Git 3-Tree Architecture (Working Dir ➔ Staging Index ➔ Commit Repo)
            </h3>

            <div style={{ display: 'grid', gridTemplateColumns: '1fr auto 1fr auto 1fr', gap: 14, alignItems: 'center' }}>
              {/* 1. Working Directory */}
              <div style={{ background: '#1e293b', padding: 18, borderRadius: 12, border: '1px solid #334155' }}>
                <div style={{ fontWeight: 700, fontSize: '0.85rem', color: '#f43f5e', marginBottom: 8 }}>1. Working Directory</div>
                <div style={{ display: 'flex', flexDirection: 'column', gap: 6, minHeight: '100px' }}>
                  {workingDirFiles.map((f, idx) => (
                    <div key={idx} style={{ padding: '6px 10px', background: '#090d16', borderRadius: '6px', fontSize: '0.75rem', color: '#fca5a5' }}>
                      📄 {f.name} ({f.status})
                    </div>
                  ))}
                  {workingDirFiles.length === 0 && <span style={{ fontSize: '0.75rem', color: '#94a3b8' }}>Clean working tree</span>}
                </div>
              </div>

              <div style={{ color: '#64748b' }}>➔</div>

              {/* 2. Staging Index */}
              <div style={{ background: '#1e293b', padding: 18, borderRadius: 12, border: '1px solid #334155' }}>
                <div style={{ fontWeight: 700, fontSize: '0.85rem', color: '#10b981', marginBottom: 8 }}>2. Staging Area (Index)</div>
                <div style={{ display: 'flex', flexDirection: 'column', gap: 6, minHeight: '100px' }}>
                  {stagedFiles.map((f, idx) => (
                    <div key={idx} style={{ padding: '6px 10px', background: '#090d16', borderRadius: '6px', fontSize: '0.75rem', color: '#86efac' }}>
                      ✓ {f.name} (staged)
                    </div>
                  ))}
                  {stagedFiles.length === 0 && <span style={{ fontSize: '0.75rem', color: '#94a3b8' }}>No files staged</span>}
                </div>
              </div>

              <div style={{ color: '#64748b' }}>➔</div>

              {/* 3. Local Repository */}
              <div style={{ background: '#1e293b', padding: 18, borderRadius: 12, border: '1px solid #334155' }}>
                <div style={{ fontWeight: 700, fontSize: '0.85rem', color: '#38bdf8', marginBottom: 8 }}>3. Local Repository (HEAD)</div>
                <div style={{ minHeight: '100px', display: 'flex', flexDirection: 'column', justifyContent: 'center', textAlign: 'center' }}>
                  <div style={{ fontSize: '1.8rem', fontWeight: 800, color: '#38bdf8' }}>{repoCommitsCount}</div>
                  <div style={{ fontSize: '0.75rem', color: '#94a3b8' }}>Immutable Commits in DAG</div>
                </div>
              </div>
            </div>
          </div>

          {/* Action Bar */}
          <div className="card" style={{ padding: 16, display: 'flex', gap: 12, justifyContent: 'space-between' }}>
            <div style={{ display: 'flex', gap: 10 }}>
              <button onClick={stageAllFiles} disabled={workingDirFiles.length === 0} className="btn btn-primary btn-sm">
                Stage All Files (git add .)
              </button>
              <button onClick={commitStaged} disabled={stagedFiles.length === 0} className="btn btn-secondary btn-sm">
                Commit Staged Changes (git commit)
              </button>
            </div>
            <button onClick={resetThreeTrees} className="btn btn-ghost btn-sm">
              <RotateCcw size={12} /> Reset Working Files
            </button>
          </div>
        </div>
      )}

      {/* TAB 2: DAG BRANCH & MERGE TERMINAL */}
      {activeTab === 'dag-terminal' && (
        <div style={{ display: 'grid', gap: 20 }}>
          {/* Visual Graph Canvas */}
          <div className="card" style={{ padding: 24, background: '#090d16', border: '1px solid #1e293b' }}>
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: 20 }}>
              <h3 style={{ fontSize: '1.1rem', fontWeight: 700, display: 'flex', alignItems: 'center', gap: 8 }}>
                <GitCommit size={18} color="#f59e0b" /> Commit Directed Acyclic Graph (DAG)
              </h3>
              <div style={{ display: 'flex', alignItems: 'center', gap: 8, background: '#1e293b', padding: '6px 14px', borderRadius: '12px', border: '1px solid #334155' }}>
                <span style={{ fontSize: '0.8rem', color: '#94a3b8' }}>HEAD ➔</span>
                <span style={{ fontSize: '0.85rem', fontWeight: 700, color: '#38bdf8' }}>{currentBranch}</span>
              </div>
            </div>

            <div style={{ display: 'flex', alignItems: 'center', gap: 24, overflowX: 'auto', padding: '16px 10px', minHeight: '140px' }}>
              {commits.map((c, idx) => {
                const isHead = c.branch === currentBranch && idx === commits.map(x => x.branch).lastIndexOf(currentBranch);
                return (
                  <div key={c.id} style={{ display: 'flex', alignItems: 'center', gap: 16 }}>
                    <div
                      style={{
                        background: c.branch === 'main' ? '#1e293b' : '#312e81',
                        border: isHead ? '2px solid #38bdf8' : `1px solid ${c.branch === 'main' ? '#334155' : '#6366f1'}`,
                        padding: '12px 16px',
                        borderRadius: '12px',
                        minWidth: '150px'
                      }}
                    >
                      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: 4 }}>
                        <span style={{ fontFamily: 'monospace', fontSize: '0.75rem', color: '#f59e0b', fontWeight: 700 }}>{c.hash}</span>
                        <span style={{ fontSize: '0.65rem', padding: '2px 6px', borderRadius: '4px', background: c.branch === 'main' ? '#0f172a' : '#4338ca', color: '#e2e8f0' }}>{c.branch}</span>
                      </div>
                      <div style={{ fontSize: '0.8rem', fontWeight: 600, color: '#f8fafc', whiteSpace: 'nowrap' }}>{c.message}</div>
                    </div>
                    {idx < commits.length - 1 && <div style={{ color: '#475569', fontSize: '1.2rem' }}>➔</div>}
                  </div>
                );
              })}
            </div>
          </div>

          {/* Terminal */}
          <div className="card" style={{ padding: 0, overflow: 'hidden', background: '#090d16', border: '1px solid #1e293b' }}>
            <div style={{ display: 'flex', alignItems: 'center', gap: 8, padding: '10px 16px', background: '#0f172a', borderBottom: '1px solid #1e293b' }}>
              <Terminal size={16} color="#38bdf8" />
              <span style={{ fontSize: '0.8rem', fontWeight: 600, color: '#94a3b8' }}>Git Interactive Shell</span>
            </div>

            <div style={{ padding: '16px', minHeight: '160px', maxHeight: '200px', overflowY: 'auto', fontFamily: 'monospace', fontSize: '0.85rem', color: '#94a3b8', lineHeight: 1.5 }}>
              {history.map((line, idx) => (
                <div key={idx} style={{ color: line.startsWith('$') ? '#38bdf8' : line.startsWith('fatal') || line.startsWith('error') ? '#f43f5e' : '#cbd5e1' }}>
                  {line}
                </div>
              ))}
            </div>

            <form onSubmit={handleCommand} style={{ display: 'flex', borderTop: '1px solid #1e293b', background: '#0f172a' }}>
              <span style={{ padding: '12px 0 12px 16px', color: '#10b981', fontFamily: 'monospace', fontWeight: 700 }}>(repo) $</span>
              <input
                type="text"
                value={commandInput}
                onChange={(e) => setCommandInput(e.target.value)}
                placeholder="e.g. git commit -m 'new login', git checkout main, git merge feature/auth"
                style={{ flex: 1, background: 'transparent', border: 'none', padding: '12px', color: '#f8fafc', fontFamily: 'monospace', fontSize: '0.85rem', outline: 'none' }}
              />
            </form>
          </div>
        </div>
      )}

      {/* TAB 3: MERGE CONFLICT STUDIO */}
      {activeTab === 'conflict-resolver' && (
        <div style={{ display: 'grid', gap: 20 }}>
          <div className="card" style={{ padding: 24, background: '#090d16', border: '1px solid #1e293b' }}>
            <h3 style={{ fontSize: '1.1rem', fontWeight: 700, marginBottom: 16, display: 'flex', alignItems: 'center', gap: 8 }}>
              <AlertCircle size={18} color="#f59e0b" /> Interactive Merge Conflict Resolution Workbench
            </h3>

            {!conflictResolved ? (
              <div>
                <p style={{ fontSize: '0.85rem', color: '#94a3b8', marginBottom: 14 }}>
                  Conflict detected in <code>config/database.py</code> during merge. Choose a resolution strategy below:
                </p>

                <div style={{ background: '#1e293b', padding: 18, borderRadius: 10, fontFamily: 'monospace', fontSize: '0.8rem', lineHeight: 1.6, border: '1px solid #334155', marginBottom: 16 }}>
                  <div style={{ color: '#38bdf8' }}>&lt;&lt;&lt;&lt;&lt;&lt;&lt; HEAD (Current Change: main)</div>
                  <div style={{ color: '#e2e8f0' }}>DB_MAX_CONNECTIONS = 50</div>
                  <div style={{ color: '#e2e8f0' }}>DB_TIMEOUT_MS = 2000</div>
                  <div style={{ color: '#64748b' }}>=======</div>
                  <div style={{ color: '#10b981' }}>DB_MAX_CONNECTIONS = 150</div>
                  <div style={{ color: '#10b981' }}>DB_TIMEOUT_MS = 5000</div>
                  <div style={{ color: '#f59e0b' }}>&gt;&gt;&gt;&gt;&gt;&gt;&gt; feature/scale-db (Incoming Change)</div>
                </div>

                <div style={{ display: 'flex', gap: 10, flexWrap: 'wrap' }}>
                  <button onClick={() => { setResolvedContent('Current (main: 50 conn)'); setConflictResolved(true); }} className="btn btn-secondary btn-sm">
                    Accept Current Change (main)
                  </button>
                  <button onClick={() => { setResolvedContent('Incoming (feature: 150 conn)'); setConflictResolved(true); }} className="btn btn-primary btn-sm">
                    Accept Incoming Change (feature/scale-db)
                  </button>
                </div>
              </div>
            ) : (
              <div style={{ padding: 20, background: 'rgba(16, 185, 129, 0.1)', border: '1px solid #10b981', borderRadius: 10, textAlign: 'center' }}>
                <CheckCircle2 size={32} color="#10b981" style={{ margin: '0 auto 8px' }} />
                <h4 style={{ margin: 0, color: '#f8fafc' }}>Conflict Resolved Successfully!</h4>
                <p style={{ fontSize: '0.85rem', color: '#94a3b8', margin: '4px 0 14px 0' }}>Resolved using strategy: <strong>{resolvedContent}</strong></p>
                <button onClick={() => setConflictResolved(false)} className="btn btn-outline btn-sm">
                  Simulate New Conflict
                </button>
              </div>
            )}
          </div>
        </div>
      )}

      {/* TAB 4: GITHUB ACTIONS CI/CD RUNNER */}
      {activeTab === 'cicd-runner' && (
        <div style={{ display: 'grid', gap: 20 }}>
          <div className="card" style={{ padding: 24, background: '#090d16', border: '1px solid #1e293b' }}>
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: 16 }}>
              <h3 style={{ fontSize: '1.1rem', fontWeight: 700, display: 'flex', alignItems: 'center', gap: 8 }}>
                <ShieldCheck size={18} color="#8b5cf6" /> GitHub Actions CI/CD Pipeline Simulator
              </h3>
              <button onClick={runCicdPipeline} disabled={pipelineRunning} className="btn btn-primary btn-sm" style={{ gap: 6 }}>
                <Play size={12} /> {pipelineRunning ? 'Executing Stages...' : 'Trigger Workflow (push to main)'}
              </button>
            </div>

            <div style={{ display: 'flex', flexDirection: 'column', gap: 10 }}>
              {pipelineSteps.map((step) => (
                <div
                  key={step.id}
                  style={{
                    padding: '14px 18px',
                    background: '#1e293b',
                    borderRadius: '10px',
                    border: `1px solid ${step.status === 'success' ? '#10b981' : step.status === 'running' ? '#38bdf8' : '#334155'}`,
                    display: 'flex',
                    justifyContent: 'space-between',
                    alignItems: 'center'
                  }}
                >
                  <span style={{ fontSize: '0.85rem', fontWeight: 600, color: '#f8fafc' }}>{step.name}</span>
                  <span
                    style={{
                      fontSize: '0.75rem',
                      fontWeight: 700,
                      padding: '4px 10px',
                      borderRadius: '6px',
                      background: step.status === 'success' ? 'rgba(16, 185, 129, 0.2)' : step.status === 'running' ? 'rgba(56, 189, 248, 0.2)' : 'rgba(255, 255, 255, 0.05)',
                      color: step.status === 'success' ? '#10b981' : step.status === 'running' ? '#38bdf8' : '#94a3b8'
                    }}
                  >
                    {step.status.toUpperCase()}
                  </span>
                </div>
              ))}
            </div>
          </div>
        </div>
      )}
    </div>
  );
}

