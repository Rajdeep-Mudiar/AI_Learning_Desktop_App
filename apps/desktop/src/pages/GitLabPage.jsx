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
  HelpCircle
} from 'lucide-react';
import Badge from '../components/common/Badge';

export default function GitLabPage() {
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

  const handleCommand = (e) => {
    e.preventDefault();
    const cmd = commandInput.trim();
    if (!cmd) return;

    setHistory(prev => [...prev, `$ ${cmd}`]);
    setCommandInput('');

    // Parse git commands
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

  const resetGraph = () => {
    setCommits([
      { id: 'c1', hash: 'e4f1a0', message: 'Initial commit', branch: 'main', parent: null },
      { id: 'c2', hash: '7b89d2', message: 'Setup project config', branch: 'main', parent: 'c1' },
      { id: 'c3', hash: '3c19e4', message: 'Add authentication routes', branch: 'feature/auth', parent: 'c2' },
      { id: 'c4', hash: '9a01f8', message: 'JWT token generation', branch: 'feature/auth', parent: 'c3' }
    ]);
    setBranches(['main', 'feature/auth']);
    setCurrentBranch('feature/auth');
    setHistory(['Git tree reset to default.']);
  };

  return (
    <div className="animate-fade-in" style={{ paddingBottom: 40 }}>
      {/* Header */}
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', flexWrap: 'wrap', gap: 16, marginBottom: 24 }}>
        <div>
          <div style={{ display: 'flex', alignItems: 'center', gap: 10, marginBottom: 6 }}>
            <Badge variant="yellow"><GitBranch size={14} /> Git & GitHub Lab</Badge>
            <span style={{ fontSize: '0.85rem', color: 'var(--text-muted)' }}>Interactive DAG Commit Visualizer</span>
          </div>
          <h1 style={{ fontSize: '1.85rem', fontWeight: 800 }}>Interactive Git Tree & Terminal Simulator</h1>
          <p style={{ color: 'var(--text-secondary)', fontSize: '0.95rem' }}>
            Execute real Git commands in the terminal and watch branches, merges, and commit trees animate in real time.
          </p>
        </div>

        <button onClick={resetGraph} className="btn btn-ghost btn-sm" style={{ gap: 6 }}>
          <RotateCcw size={14} /> Reset Tree
        </button>
      </div>

      {/* Main Grid: Visual DAG Graph (Top) & Terminal (Bottom) */}
      <div style={{ display: 'grid', gap: 24 }}>
        {/* Visual Graph Canvas */}
        <div className="card" style={{ padding: 28, background: '#090d16', border: '1px solid #1e293b' }}>
          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: 24 }}>
            <h3 style={{ fontSize: '1.1rem', fontWeight: 700, display: 'flex', alignItems: 'center', gap: 8 }}>
              <GitCommit size={18} color="#f59e0b" /> Commit Directed Acyclic Graph (DAG)
            </h3>

            {/* Active HEAD indicator */}
            <div style={{ display: 'flex', alignItems: 'center', gap: 8, background: '#1e293b', padding: '6px 14px', borderRadius: '12px', border: '1px solid #334155' }}>
              <span style={{ fontSize: '0.8rem', color: '#94a3b8' }}>HEAD ➔</span>
              <span style={{ fontSize: '0.85rem', fontWeight: 700, color: '#38bdf8' }}>{currentBranch}</span>
            </div>
          </div>

          {/* Interactive DAG Nodes */}
          <div style={{ display: 'flex', alignItems: 'center', gap: 28, overflowX: 'auto', padding: '20px 10px', minHeight: '160px' }}>
            {commits.map((c, idx) => {
              const isHead = c.branch === currentBranch && idx === commits.map(x => x.branch).lastIndexOf(currentBranch);
              return (
                <div key={c.id} style={{ display: 'flex', alignItems: 'center', gap: 20 }}>
                  <div
                    style={{
                      background: c.branch === 'main' ? '#1e293b' : '#312e81',
                      border: isHead ? '2px solid #38bdf8' : `1px solid ${c.branch === 'main' ? '#334155' : '#6366f1'}`,
                      padding: '12px 18px',
                      borderRadius: '14px',
                      minWidth: '160px',
                      boxShadow: isHead ? '0 0 15px rgba(56, 189, 248, 0.4)' : 'none',
                      transition: 'all 0.2s ease'
                    }}
                  >
                    <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: 4 }}>
                      <span style={{ fontFamily: 'monospace', fontSize: '0.75rem', color: '#f59e0b', fontWeight: 700 }}>
                        {c.hash}
                      </span>
                      <span
                        style={{
                          fontSize: '0.65rem',
                          padding: '2px 6px',
                          borderRadius: '6px',
                          background: c.branch === 'main' ? '#0f172a' : '#4338ca',
                          color: '#e2e8f0',
                          fontWeight: 600
                        }}
                      >
                        {c.branch}
                      </span>
                    </div>
                    <div style={{ fontSize: '0.85rem', fontWeight: 600, color: '#f8fafc', whiteSpace: 'nowrap', overflow: 'hidden', textOverflow: 'ellipsis' }}>
                      {c.message}
                    </div>
                  </div>

                  {idx < commits.length - 1 && (
                    <div style={{ color: '#475569', fontSize: '1.2rem', fontWeight: 700 }}>➔</div>
                  )}
                </div>
              );
            })}
          </div>
        </div>

        {/* Git Interactive Terminal */}
        <div className="card" style={{ padding: 0, overflow: 'hidden', background: '#090d16', border: '1px solid #1e293b' }}>
          {/* Header */}
          <div style={{ display: 'flex', alignItems: 'center', gap: 8, padding: '10px 16px', background: '#0f172a', borderBottom: '1px solid #1e293b' }}>
            <Terminal size={16} color="#38bdf8" />
            <span style={{ fontSize: '0.8rem', fontWeight: 600, color: '#94a3b8' }}>Git Interactive Shell</span>
          </div>

          {/* Console logs */}
          <div style={{ padding: '16px', minHeight: '180px', maxHeight: '240px', overflowY: 'auto', fontFamily: 'monospace', fontSize: '0.85rem', color: '#94a3b8', lineHeight: 1.5 }}>
            {history.map((line, idx) => (
              <div key={idx} style={{ color: line.startsWith('$') ? '#38bdf8' : line.startsWith('fatal') || line.startsWith('error') ? '#f43f5e' : '#cbd5e1' }}>
                {line}
              </div>
            ))}
          </div>

          {/* Input form */}
          <form onSubmit={handleCommand} style={{ display: 'flex', borderTop: '1px solid #1e293b', background: '#0f172a' }}>
            <span style={{ padding: '12px 0 12px 16px', color: '#10b981', fontFamily: 'monospace', fontWeight: 700 }}>
              (repo) $
            </span>
            <input
              type="text"
              value={commandInput}
              onChange={(e) => setCommandInput(e.target.value)}
              placeholder="e.g. git commit -m 'feat: new login', git checkout main, git merge feature/auth"
              style={{
                flex: 1,
                background: 'transparent',
                border: 'none',
                padding: '12px',
                color: '#f8fafc',
                fontFamily: 'monospace',
                fontSize: '0.85rem',
                outline: 'none'
              }}
              autoFocus
            />
          </form>
        </div>
      </div>
    </div>
  );
}
