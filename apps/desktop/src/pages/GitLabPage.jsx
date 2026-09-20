import React, { useState, useEffect } from 'react';
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
  GitFork,
  Archive,
  Tag,
  UploadCloud,
  DownloadCloud,
  RotateCw,
  Sliders,
  Code2,
  Eye,
  Check,
  X,
  FileText,
  Workflow
} from 'lucide-react';
import Badge from '../components/common/Badge';

export default function GitLabPage() {
  const [activeTab, setActiveTab] = useState('all-terminal'); 
  // 'all-terminal' | 'snapshots' | 'branching' | 'undo-rebase' | 'remotes-sync' | 'github-pr' | 'github-actions'

  // --- Global DAG / Repo State ---
  const [repoInitialized, setRepoInitialized] = useState(true);
  const [commits, setCommits] = useState([
    { id: 'c1', hash: 'e4f1a0', message: 'Initial commit', branch: 'main', parent: null, author: 'Alex Chen', tag: 'v0.1.0' },
    { id: 'c2', hash: '7b89d2', message: 'Setup project config & Vite', branch: 'main', parent: 'c1', author: 'Alex Chen' },
    { id: 'c3', hash: '3c19e4', message: 'Add JWT auth middleware', branch: 'feature/auth', parent: 'c2', author: 'Alex Chen' },
    { id: 'c4', hash: '9a01f8', message: 'Implement login and register API', branch: 'feature/auth', parent: 'c3', author: 'Alex Chen' }
  ]);
  const [branches, setBranches] = useState(['main', 'feature/auth']);
  const [currentBranch, setCurrentBranch] = useState('feature/auth');
  const [tags, setTags] = useState([{ name: 'v0.1.0', commitHash: 'e4f1a0' }]);
  const [stashStack, setStashStack] = useState([]);
  const [remoteOriginUrl, setRemoteOriginUrl] = useState('https://github.com/developer/ai-lab-app.git');
  const [remoteCommitsCount, setRemoteCommitsCount] = useState(2); // origin/main is at c2

  // --- Snapshotting / 3-Trees State ---
  const [workingFiles, setWorkingFiles] = useState([
    { name: 'src/auth/jwt.py', status: 'modified', additions: 14, deletions: 3 },
    { name: 'config/database.env', status: 'untracked', additions: 8, deletions: 0 },
    { name: 'src/utils/logger.py', status: 'clean', additions: 0, deletions: 0 }
  ]);
  const [stagedFiles, setStagedFiles] = useState([]);

  // --- Diff Inspector State ---
  const [selectedDiffFile, setSelectedDiffFile] = useState('src/auth/jwt.py');

  // --- Interactive Terminal State ---
  const [commandInput, setCommandInput] = useState('');
  const [terminalHistory, setTerminalHistory] = useState([
    '⚡ Interactive Git 2.45 Command Engine Ready.',
    'Type any Git command below or click a quick-command chip to execute simulations in real time.'
  ]);

  // --- GitHub PR Simulation State ---
  const [prStatus, setPrStatus] = useState('open'); // 'open' | 'merged' | 'closed'
  const [mergeStrategy, setMergeStrategy] = useState('merge-commit'); // 'merge-commit' | 'squash' | 'rebase'
  const [prReviews, setPrReviews] = useState([
    { reviewer: 'Senior Reviewer (Sarah)', status: 'APPROVED', comment: 'LGTM! Clean JWT signing logic.' },
    { reviewer: 'Security Bot (CodeQL)', status: 'APPROVED', comment: 'No high-severity vulnerabilities found.' }
  ]);

  // --- GitHub Actions CI/CD Pipeline State ---
  const [pipelineSteps, setPipelineSteps] = useState([
    { id: 1, name: '1. Lint & Format Check (ruff / black)', status: 'pending', duration: '4s' },
    { id: 2, name: '2. Unit & Integration Test Matrix (pytest 3.11, 3.12)', status: 'pending', duration: '12s' },
    { id: 3, name: '3. Security Vulnerability Scan (Trivy & Bandit)', status: 'pending', duration: '8s' },
    { id: 4, name: '4. Build Multi-Arch Docker Container', status: 'pending', duration: '22s' },
    { id: 5, name: '5. Automated Deployment to Production (Kubernetes)', status: 'pending', duration: '15s' }
  ]);
  const [pipelineRunning, setPipelineRunning] = useState(false);

  // Command Execution Parser
  const executeGitCommand = (rawCmd) => {
    const cmd = rawCmd.trim();
    if (!cmd) return;

    setTerminalHistory(prev => [...prev, `$ ${cmd}`]);
    setCommandInput('');

    if (cmd === 'git init') {
      setRepoInitialized(true);
      setTerminalHistory(prev => [...prev, 'Initialized empty Git repository in /workspace/.git/']);
    } 
    else if (cmd.startsWith('git clone ')) {
      const url = cmd.replace('git clone ', '').trim();
      setRemoteOriginUrl(url);
      setTerminalHistory(prev => [
        ...prev,
        `Cloning into 'repo'...`,
        `remote: Enumerating objects: 14, done.`,
        `remote: Total 14 (delta 2), reused 12`,
        `Receiving objects: 100% (14/14), done.`
      ]);
    }
    else if (cmd === 'git status' || cmd === 'git status -s') {
      const stagedNames = stagedFiles.map(f => `  (use "git restore --staged <file>..." to unstage)\n\tnew file:   ${f.name}`);
      const untracked = workingFiles.filter(f => f.status === 'untracked').map(f => `\t${f.name}`);
      const modified = workingFiles.filter(f => f.status === 'modified').map(f => `\tmodified:   ${f.name}`);

      setTerminalHistory(prev => [
        ...prev,
        `On branch ${currentBranch}`,
        stagedFiles.length > 0 ? `Changes to be committed:\n${stagedNames.join('\n')}` : 'No changes added to commit (use "git add")',
        modified.length > 0 ? `Changes not staged for commit:\n${modified.join('\n')}` : '',
        untracked.length > 0 ? `Untracked files:\n${untracked.join('\n')}` : '',
        stagedFiles.length === 0 && workingFiles.filter(f => f.status !== 'clean').length === 0 ? 'nothing to commit, working tree clean' : ''
      ].filter(Boolean));
    }
    else if (cmd === 'git add .' || cmd.startsWith('git add ')) {
      setStagedFiles([...stagedFiles, ...workingFiles.filter(f => f.status !== 'clean')]);
      setWorkingFiles(prev => prev.map(f => ({ ...f, status: 'clean' })));
      setTerminalHistory(prev => [...prev, `Staged all modified & untracked changes to index.`]);
    }
    else if (cmd.startsWith('git commit -m ') || cmd.startsWith('git commit -am ')) {
      const match = cmd.match(/-m\s+["'](.*?)["']/);
      const msg = match ? match[1] : 'Update codebase';
      const newHash = Math.random().toString(16).substring(2, 8);
      const parentId = commits[commits.length - 1].id;
      const newCommit = {
        id: `c${commits.length + 1}`,
        hash: newHash,
        message: msg,
        branch: currentBranch,
        parent: parentId,
        author: 'Alex Chen'
      };
      setCommits(prev => [...prev, newCommit]);
      setStagedFiles([]);
      setTerminalHistory(prev => [...prev, `[${currentBranch} ${newHash}] ${msg}`, ` 2 files changed, 22 insertions(+), 3 deletions(-)`]);
    }
    else if (cmd === 'git commit --amend' || cmd.startsWith('git commit --amend -m')) {
      const match = cmd.match(/-m\s+["'](.*?)["']/);
      const newMsg = match ? match[1] : `${commits[commits.length - 1].message} (amended)`;
      setCommits(prev => {
        const copy = [...prev];
        copy[copy.length - 1] = { ...copy[copy.length - 1], message: newMsg };
        return copy;
      });
      setTerminalHistory(prev => [...prev, `[${currentBranch} ${commits[commits.length - 1].hash}] ${newMsg} (amended)`]);
    }
    else if (cmd.startsWith('git branch -d ') || cmd.startsWith('git branch -D ')) {
      const target = cmd.replace(/git branch -[dD]\s+/, '').trim();
      if (target === currentBranch) {
        setTerminalHistory(prev => [...prev, `error: Cannot delete branch '${target}' checked out at current HEAD.`]);
      } else if (branches.includes(target)) {
        setBranches(prev => prev.filter(b => b !== target));
        setTerminalHistory(prev => [...prev, `Deleted branch ${target} (was ${commits[commits.length - 1].hash}).`]);
      } else {
        setTerminalHistory(prev => [...prev, `error: branch '${target}' not found.`]);
      }
    }
    else if (cmd.startsWith('git branch ')) {
      const newBranch = cmd.replace('git branch ', '').trim();
      if (!branches.includes(newBranch)) {
        setBranches(prev => [...prev, newBranch]);
        setTerminalHistory(prev => [...prev, `Created branch '${newBranch}'`]);
      } else {
        setTerminalHistory(prev => [...prev, `fatal: A branch named '${newBranch}' already exists.`]);
      }
    }
    else if (cmd === 'git branch' || cmd === 'git branch -a') {
      setTerminalHistory(prev => [
        ...prev,
        ...branches.map(b => (b === currentBranch ? `* \x1b[32m${b}\x1b[0m` : `  ${b}`))
      ]);
    }
    else if (cmd.startsWith('git checkout -b ') || cmd.startsWith('git switch -c ')) {
      const newBranch = cmd.replace('git checkout -b ', '').replace('git switch -c ', '').trim();
      setBranches(prev => [...prev, newBranch]);
      setCurrentBranch(newBranch);
      setTerminalHistory(prev => [...prev, `Switched to a new branch '${newBranch}'`]);
    }
    else if (cmd.startsWith('git checkout ') || cmd.startsWith('git switch ')) {
      const target = cmd.replace('git checkout ', '').replace('git switch ', '').trim();
      if (branches.includes(target)) {
        setCurrentBranch(target);
        setTerminalHistory(prev => [...prev, `Switched to branch '${target}'`]);
      } else {
        setTerminalHistory(prev => [...prev, `error: pathspec '${target}' did not match any file(s) known to git`]);
      }
    }
    else if (cmd.startsWith('git merge ')) {
      const sourceBranch = cmd.replace('git merge ', '').trim();
      const newHash = Math.random().toString(16).substring(2, 8);
      const newCommit = {
        id: `c${commits.length + 1}`,
        hash: newHash,
        message: `Merge branch '${sourceBranch}' into ${currentBranch}`,
        branch: currentBranch,
        parent: commits[commits.length - 1].id,
        author: 'Alex Chen'
      };
      setCommits(prev => [...prev, newCommit]);
      setTerminalHistory(prev => [...prev, `Merge made by the 'ort' strategy. [${currentBranch} ${newHash}]`]);
    }
    else if (cmd.startsWith('git rebase ')) {
      const baseBranch = cmd.replace('git rebase ', '').trim();
      setTerminalHistory(prev => [
        ...prev,
        `First, rewinding head to replay your work on top of '${baseBranch}'...`,
        `Applying: ${commits[commits.length - 1].message}`,
        `Successfully rebased and updated refs/heads/${currentBranch}.`
      ]);
    }
    else if (cmd.startsWith('git cherry-pick ')) {
      const pickHash = cmd.replace('git cherry-pick ', '').trim();
      const newHash = Math.random().toString(16).substring(2, 8);
      const picked = {
        id: `c${commits.length + 1}`,
        hash: newHash,
        message: `Cherry-picked: ${pickHash}`,
        branch: currentBranch,
        parent: commits[commits.length - 1].id,
        author: 'Alex Chen'
      };
      setCommits(prev => [...prev, picked]);
      setTerminalHistory(prev => [...prev, `[${currentBranch} ${newHash}] Cherry-picked ${pickHash}`]);
    }
    else if (cmd.startsWith('git reset --hard')) {
      if (commits.length > 1) {
        setCommits(prev => prev.slice(0, prev.length - 1));
        setStagedFiles([]);
        setTerminalHistory(prev => [...prev, `HEAD is now at ${commits[commits.length - 2].hash} ${commits[commits.length - 2].message}`]);
      }
    }
    else if (cmd.startsWith('git reset --soft')) {
      setTerminalHistory(prev => [...prev, `HEAD moved back 1 commit. Previous changes retained in staging index.`]);
    }
    else if (cmd.startsWith('git reset')) {
      setStagedFiles([]);
      setTerminalHistory(prev => [...prev, `Unstaged all changes. Working tree files preserved.`]);
    }
    else if (cmd.startsWith('git revert ')) {
      const revHash = cmd.replace('git revert ', '').trim();
      const newHash = Math.random().toString(16).substring(2, 8);
      const revertCommit = {
        id: `c${commits.length + 1}`,
        hash: newHash,
        message: `Revert "${revHash}"`,
        branch: currentBranch,
        parent: commits[commits.length - 1].id,
        author: 'Alex Chen'
      };
      setCommits(prev => [...prev, revertCommit]);
      setTerminalHistory(prev => [...prev, `[${currentBranch} ${newHash}] Revert "${revHash}"`]);
    }
    else if (cmd === 'git stash' || cmd === 'git stash push') {
      const stashed = workingFiles.filter(f => f.status !== 'clean');
      setStashStack(prev => [{ id: `stash@{${prev.length}}`, items: stashed, branch: currentBranch }, ...prev]);
      setWorkingFiles(prev => prev.map(f => ({ ...f, status: 'clean' })));
      setTerminalHistory(prev => [...prev, `Saved working directory and index state WIP on ${currentBranch}: ${commits[commits.length - 1].hash}`]);
    }
    else if (cmd === 'git stash pop') {
      if (stashStack.length > 0) {
        setStashStack(prev => prev.slice(1));
        setTerminalHistory(prev => [...prev, `Dropped stash@{0} and restored changes into working directory.`]);
      } else {
        setTerminalHistory(prev => [...prev, `error: No stash entries found.`]);
      }
    }
    else if (cmd === 'git stash list') {
      setTerminalHistory(prev => [
        ...prev,
        ...(stashStack.length > 0 ? stashStack.map(s => `${s.id}: WIP on ${s.branch}`) : ['(no stash entries)'])
      ]);
    }
    else if (cmd.startsWith('git tag -a ') || cmd.startsWith('git tag ')) {
      const match = cmd.match(/git tag\s+(-a\s+)?([v\d\.]+)/);
      const tagName = match ? match[2] : 'v1.0.0';
      setTags(prev => [...prev, { name: tagName, commitHash: commits[commits.length - 1].hash }]);
      setTerminalHistory(prev => [...prev, `Created tag '${tagName}' pointing to commit ${commits[commits.length - 1].hash}`]);
    }
    else if (cmd === 'git tag') {
      setTerminalHistory(prev => [...prev, ...tags.map(t => t.name)]);
    }
    else if (cmd.startsWith('git remote -v')) {
      setTerminalHistory(prev => [
        ...prev,
        `origin\t${remoteOriginUrl} (fetch)`,
        `origin\t${remoteOriginUrl} (push)`
      ]);
    }
    else if (cmd.startsWith('git fetch')) {
      setTerminalHistory(prev => [
        ...prev,
        `remote: Enumerating objects: 6, done.`,
        `From ${remoteOriginUrl}`,
        ` * [new branch]      main       -> origin/main`
      ]);
    }
    else if (cmd.startsWith('git pull')) {
      setTerminalHistory(prev => [
        ...prev,
        `Updating ${commits[0].hash}..${commits[commits.length - 1].hash}`,
        `Fast-forward`,
        ` 3 files changed, 45 insertions(+)`
      ]);
    }
    else if (cmd.startsWith('git push')) {
      setRemoteCommitsCount(commits.length);
      setTerminalHistory(prev => [
        ...prev,
        `Enumerating objects: 12, done.`,
        `Writing objects: 100% (12/12), 1.84 KiB | 1.84 MiB/s, done.`,
        `To ${remoteOriginUrl}`,
        `   ${commits[0].hash}..${commits[commits.length - 1].hash}  ${currentBranch} -> ${currentBranch}`
      ]);
    }
    else if (cmd === 'git log' || cmd === 'git log --oneline' || cmd === 'git log --oneline --graph') {
      setTerminalHistory(prev => [
        ...prev,
        ...commits.slice().reverse().map(c => `* ${c.hash} (${c.branch}) ${c.message}`)
      ]);
    }
    else if (cmd === 'git diff' || cmd === 'git diff --staged') {
      setTerminalHistory(prev => [
        ...prev,
        `diff --git a/src/auth/jwt.py b/src/auth/jwt.py`,
        `index e4a19b..8f12d4 100644`,
        `--- a/src/auth/jwt.py`,
        `+++ b/src/auth/jwt.py`,
        `@@ -14,6 +14,8 @@ def create_token(payload: dict):`,
        `-    return jwt.encode(payload, SECRET, algorithm="HS256")`,
        `+    expire = datetime.utcnow() + timedelta(minutes=60)`,
        `+    payload.update({"exp": expire})`,
        `+    return jwt.encode(payload, SECRET, algorithm="RS256")`
      ]);
    }
    else if (cmd === 'clear') {
      setTerminalHistory([]);
    }
    else {
      setTerminalHistory(prev => [
        ...prev,
        `git: '${cmd}' is not a recognized command. Click a command pill below or type 'git --help'`
      ]);
    }
  };

  // CI/CD Pipeline execution
  const runCicdPipeline = async () => {
    setPipelineRunning(true);
    for (let i = 0; i < pipelineSteps.length; i++) {
      setPipelineSteps(prev => prev.map((s, idx) => idx === i ? { ...s, status: 'running' } : s));
      await new Promise(r => setTimeout(r, 600));
      setPipelineSteps(prev => prev.map((s, idx) => idx === i ? { ...s, status: 'success' } : s));
    }
    setPipelineRunning(false);
  };

  const handleMergePr = () => {
    setPrStatus('merged');
    executeGitCommand(`git merge feature/auth`);
  };

  const COMMAND_PRESETS = [
    { label: 'git status', cmd: 'git status', category: 'Inspection' },
    { label: 'git add .', cmd: 'git add .', category: 'Staging' },
    { label: 'git commit -m "..."', cmd: 'git commit -m "feat: implement security filters"', category: 'Snapshot' },
    { label: 'git commit --amend', cmd: 'git commit --amend -m "feat: implement security filters & tests"', category: 'Snapshot' },
    { label: 'git branch', cmd: 'git branch', category: 'Branch' },
    { label: 'git checkout -b new-feat', cmd: 'git checkout -b feature/payments', category: 'Branch' },
    { label: 'git switch main', cmd: 'git switch main', category: 'Branch' },
    { label: 'git merge feature/auth', cmd: 'git merge feature/auth', category: 'Merge' },
    { label: 'git rebase main', cmd: 'git rebase main', category: 'History' },
    { label: 'git cherry-pick 3c19e4', cmd: 'git cherry-pick 3c19e4', category: 'History' },
    { label: 'git reset --soft HEAD~1', cmd: 'git reset --soft HEAD~1', category: 'Undo' },
    { label: 'git reset --hard HEAD~1', cmd: 'git reset --hard HEAD~1', category: 'Undo' },
    { label: 'git revert 9a01f8', cmd: 'git revert 9a01f8', category: 'Undo' },
    { label: 'git stash', cmd: 'git stash', category: 'Stash' },
    { label: 'git stash pop', cmd: 'git stash pop', category: 'Stash' },
    { label: 'git tag -a v1.0.0', cmd: 'git tag -a v1.0.0', category: 'Release' },
    { label: 'git diff', cmd: 'git diff', category: 'Inspection' },
    { label: 'git log --oneline', cmd: 'git log --oneline --graph', category: 'Inspection' },
    { label: 'git remote -v', cmd: 'git remote -v', category: 'Remote' },
    { label: 'git fetch origin', cmd: 'git fetch origin', category: 'Remote' },
    { label: 'git pull origin main', cmd: 'git pull origin main', category: 'Remote' },
    { label: 'git push origin main', cmd: 'git push origin main', category: 'Remote' }
  ];

  return (
    <div className="animate-fade-in" style={{ paddingBottom: 40 }}>
      {/* Header */}
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', flexWrap: 'wrap', gap: 16, marginBottom: 20 }}>
        <div>
          <div style={{ display: 'flex', alignItems: 'center', gap: 10, marginBottom: 6 }}>
            <Badge variant="yellow"><GitBranch size={14} /> Git & GitHub Command Suite</Badge>
            <span style={{ fontSize: '0.85rem', color: 'var(--text-muted)' }}>Interactive Command Visualizer</span>
          </div>
          <h1 style={{ fontSize: '1.85rem', fontWeight: 800 }}>Complete Git & GitHub Command Simulator</h1>
          <p style={{ color: 'var(--text-secondary)', fontSize: '0.95rem' }}>
            Simulate and visualize every command: staging trees, DAG branches, rebasing, cherry-picking, hard/soft resets, stash stacks, GitHub PRs, and CI/CD pipelines.
          </p>
        </div>
      </div>

      {/* Primary Navigation Tabs */}
      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(170px, 1fr))', gap: 8, marginBottom: 20 }}>
        {[
          { id: 'all-terminal', title: '💻 Interactive Terminal & DAG', level: 'Every Command', color: '#38bdf8' },
          { id: 'snapshots', title: '📄 3-Trees & Diff Staging', level: 'add / commit / diff', color: '#10b981' },
          { id: 'branching', title: '🌿 Branching & Merges', level: 'branch / switch / merge', color: '#f59e0b' },
          { id: 'undo-rebase', title: '⚡ History, Rebase & Stash', level: 'rebase / reset / cherry-pick', color: '#ec4899' },
          { id: 'remotes-sync', title: '☁️ Remote Sync & Fetch', level: 'fetch / pull / push', color: '#8b5cf6' },
          { id: 'github-pr', title: '🔀 GitHub PR & Review', level: 'Pull Requests & Squash', color: '#6366f1' },
          { id: 'github-actions', title: '🚀 GitHub Actions CI/CD', level: 'Matrix Workflows', color: '#06b6d4' }
        ].map((tab) => {
          const isActive = activeTab === tab.id;
          return (
            <button
              key={tab.id}
              onClick={() => setActiveTab(tab.id)}
              style={{
                background: isActive ? 'var(--bg-card)' : 'var(--bg-tertiary)',
                border: isActive ? `2px solid ${tab.color}` : '1px solid var(--border-color)',
                padding: '10px 12px',
                borderRadius: '10px',
                textAlign: 'left',
                cursor: 'pointer',
                transition: 'all 0.15s ease'
              }}
            >
              <div style={{ fontSize: '0.65rem', fontWeight: 700, color: tab.color, textTransform: 'uppercase' }}>{tab.level}</div>
              <div style={{ fontSize: '0.8rem', fontWeight: 700, color: 'var(--text-primary)', marginTop: 2 }}>{tab.title}</div>
            </button>
          );
        })}
      </div>

      {/* Quick Interactive Command Bar */}
      <div className="card" style={{ padding: '12px 16px', marginBottom: 20, background: 'var(--bg-tertiary)' }}>
        <div style={{ fontSize: '0.75rem', fontWeight: 700, color: 'var(--text-muted)', marginBottom: 8, display: 'flex', alignItems: 'center', gap: 6 }}>
          <Sparkles size={14} color="#38bdf8" /> Quick Command Dispatcher (Click to Execute Instantly):
        </div>
        <div style={{ display: 'flex', gap: 6, flexWrap: 'wrap' }}>
          {COMMAND_PRESETS.map((item, idx) => (
            <button
              key={idx}
              onClick={() => executeGitCommand(item.cmd)}
              className="btn btn-ghost btn-sm"
              style={{
                fontFamily: 'monospace',
                fontSize: '0.75rem',
                background: 'var(--bg-card)',
                border: '1px solid var(--border-color)',
                padding: '4px 8px',
                borderRadius: '6px',
                color: '#38bdf8'
              }}
              title={`Run ${item.cmd}`}
            >
              {item.label}
            </button>
          ))}
        </div>
      </div>

      {/* TAB 1: ALL-COMMAND INTERACTIVE TERMINAL & DAG */}
      {activeTab === 'all-terminal' && (
        <div style={{ display: 'grid', gap: 20 }}>
          {/* Live DAG Commit Graph Canvas */}
          <div className="card" style={{ padding: 20, background: '#090d16', border: '1px solid #1e293b' }}>
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: 16 }}>
              <h3 style={{ fontSize: '1.05rem', fontWeight: 700, display: 'flex', alignItems: 'center', gap: 8 }}>
                <GitCommit size={18} color="#f59e0b" /> Live Directed Acyclic Graph (DAG)
              </h3>
              <div style={{ display: 'flex', alignItems: 'center', gap: 10 }}>
                <div style={{ background: '#1e293b', padding: '4px 12px', borderRadius: '8px', fontSize: '0.8rem', color: '#f8fafc' }}>
                  HEAD ➔ <strong style={{ color: '#38bdf8' }}>{currentBranch}</strong>
                </div>
                {tags.length > 0 && (
                  <div style={{ background: 'rgba(245, 158, 11, 0.2)', color: '#f59e0b', padding: '4px 10px', borderRadius: '8px', fontSize: '0.75rem', fontWeight: 700 }}>
                    🏷️ {tags.map(t => t.name).join(', ')}
                  </div>
                )}
              </div>
            </div>

            <div style={{ display: 'flex', alignItems: 'center', gap: 20, overflowX: 'auto', padding: '12px 6px', minHeight: '130px' }}>
              {commits.map((c, idx) => {
                const isHead = c.branch === currentBranch && idx === commits.map(x => x.branch).lastIndexOf(currentBranch);
                const hasTag = tags.find(t => t.commitHash === c.hash);
                return (
                  <div key={c.id} style={{ display: 'flex', alignItems: 'center', gap: 14 }}>
                    <div
                      style={{
                        background: c.branch === 'main' ? '#1e293b' : '#312e81',
                        border: isHead ? '2px solid #38bdf8' : `1px solid ${c.branch === 'main' ? '#334155' : '#6366f1'}`,
                        padding: '10px 14px',
                        borderRadius: '10px',
                        minWidth: '150px',
                        boxShadow: isHead ? '0 0 12px rgba(56, 189, 248, 0.35)' : 'none'
                      }}
                    >
                      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: 2 }}>
                        <span style={{ fontFamily: 'monospace', fontSize: '0.75rem', color: '#f59e0b', fontWeight: 700 }}>{c.hash}</span>
                        <span style={{ fontSize: '0.65rem', padding: '2px 5px', borderRadius: '4px', background: c.branch === 'main' ? '#0f172a' : '#4338ca', color: '#e2e8f0' }}>{c.branch}</span>
                      </div>
                      <div style={{ fontSize: '0.8rem', fontWeight: 600, color: '#f8fafc', whiteSpace: 'nowrap' }}>{c.message}</div>
                      {hasTag && <div style={{ fontSize: '0.65rem', color: '#fbbf24', marginTop: 4 }}>🏷️ {hasTag.name}</div>}
                    </div>
                    {idx < commits.length - 1 && <div style={{ color: '#475569', fontSize: '1.2rem' }}>➔</div>}
                  </div>
                );
              })}
            </div>
          </div>

          {/* Terminal Console */}
          <div className="card" style={{ padding: 0, overflow: 'hidden', background: '#090d16', border: '1px solid #1e293b' }}>
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', padding: '8px 16px', background: '#0f172a', borderBottom: '1px solid #1e293b' }}>
              <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                <Terminal size={15} color="#38bdf8" />
                <span style={{ fontSize: '0.8rem', fontWeight: 600, color: '#94a3b8' }}>Git Shell Emulator</span>
              </div>
              <button onClick={() => setTerminalHistory([])} className="btn btn-ghost btn-sm" style={{ padding: '2px 6px', fontSize: '0.7rem' }}>
                Clear Output
              </button>
            </div>

            <div style={{ padding: '14px', minHeight: '180px', maxHeight: '240px', overflowY: 'auto', fontFamily: 'monospace', fontSize: '0.8rem', color: '#94a3b8', lineHeight: 1.5 }}>
              {terminalHistory.map((line, idx) => (
                <div key={idx} style={{ color: line.startsWith('$') ? '#38bdf8' : line.startsWith('fatal') || line.startsWith('error') ? '#f43f5e' : '#cbd5e1' }}>
                  {line}
                </div>
              ))}
            </div>

            <form onSubmit={(e) => { e.preventDefault(); executeGitCommand(commandInput); }} style={{ display: 'flex', borderTop: '1px solid #1e293b', background: '#0f172a' }}>
              <span style={{ padding: '10px 0 10px 14px', color: '#10b981', fontFamily: 'monospace', fontWeight: 700, fontSize: '0.85rem' }}>(repo) $</span>
              <input
                type="text"
                value={commandInput}
                onChange={(e) => setCommandInput(e.target.value)}
                placeholder="Type git commands here (e.g. git status, git commit -m 'feat', git branch, git merge)..."
                style={{ flex: 1, background: 'transparent', border: 'none', padding: '10px', color: '#f8fafc', fontFamily: 'monospace', fontSize: '0.85rem', outline: 'none' }}
              />
            </form>
          </div>
        </div>
      )}

      {/* TAB 2: 3-TREES & DIFF STAGING */}
      {activeTab === 'snapshots' && (
        <div style={{ display: 'grid', gap: 20 }}>
          <div className="card" style={{ padding: 20, background: '#090d16', border: '1px solid #1e293b' }}>
            <h3 style={{ fontSize: '1.05rem', fontWeight: 700, marginBottom: 16, display: 'flex', alignItems: 'center', gap: 8 }}>
              <Layers size={18} color="#10b981" /> Git 3-Trees Workflow (`git status`, `git add`, `git diff`)
            </h3>

            <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr 1fr', gap: 16 }}>
              {/* Working Tree */}
              <div style={{ background: '#1e293b', padding: 16, borderRadius: 10, border: '1px solid #334155' }}>
                <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: 8 }}>
                  <span style={{ fontWeight: 700, fontSize: '0.8rem', color: '#f43f5e' }}>1. Working Directory</span>
                  <button onClick={() => executeGitCommand('git add .')} className="btn btn-primary btn-sm" style={{ padding: '2px 8px', fontSize: '0.7rem' }}>
                    + Stage All (git add .)
                  </button>
                </div>
                <div style={{ display: 'flex', flexDirection: 'column', gap: 6 }}>
                  {workingFiles.map((f, idx) => (
                    <div key={idx} style={{ padding: '6px 10px', background: '#090d16', borderRadius: '6px', fontSize: '0.75rem', display: 'flex', justifyContent: 'space-between' }}>
                      <span>📄 {f.name}</span>
                      <span style={{ color: f.status === 'clean' ? '#10b981' : '#f43f5e' }}>{f.status}</span>
                    </div>
                  ))}
                </div>
              </div>

              {/* Staging Area */}
              <div style={{ background: '#1e293b', padding: 16, borderRadius: 10, border: '1px solid #334155' }}>
                <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: 8 }}>
                  <span style={{ fontWeight: 700, fontSize: '0.8rem', color: '#10b981' }}>2. Staging Index (Cache)</span>
                  <button onClick={() => executeGitCommand('git reset')} disabled={stagedFiles.length === 0} className="btn btn-ghost btn-sm" style={{ padding: '2px 8px', fontSize: '0.7rem' }}>
                    Unstage (git reset)
                  </button>
                </div>
                <div style={{ display: 'flex', flexDirection: 'column', gap: 6 }}>
                  {stagedFiles.map((f, idx) => (
                    <div key={idx} style={{ padding: '6px 10px', background: '#090d16', borderRadius: '6px', fontSize: '0.75rem', display: 'flex', justifyContent: 'space-between' }}>
                      <span>✓ {f.name}</span>
                      <span style={{ color: '#10b981' }}>STAGED</span>
                    </div>
                  ))}
                  {stagedFiles.length === 0 && <span style={{ fontSize: '0.75rem', color: '#94a3b8' }}>No staged snapshots</span>}
                </div>
              </div>

              {/* Local HEAD Commit */}
              <div style={{ background: '#1e293b', padding: 16, borderRadius: 10, border: '1px solid #334155' }}>
                <div style={{ fontWeight: 700, fontSize: '0.8rem', color: '#38bdf8', marginBottom: 8 }}>3. Local Repository (HEAD)</div>
                <div style={{ padding: '12px', background: '#090d16', borderRadius: '8px' }}>
                  <div style={{ fontSize: '0.75rem', color: '#f59e0b', fontWeight: 700 }}>Commit: {commits[commits.length - 1].hash}</div>
                  <div style={{ fontSize: '0.8rem', color: '#f8fafc', marginTop: 4 }}>{commits[commits.length - 1].message}</div>
                  <div style={{ fontSize: '0.7rem', color: '#94a3b8', marginTop: 2 }}>Branch: {commits[commits.length - 1].branch}</div>
                </div>
              </div>
            </div>
          </div>
        </div>
      )}

      {/* TAB 3: BRANCHING & MERGES */}
      {activeTab === 'branching' && (
        <div style={{ display: 'grid', gap: 20 }}>
          <div className="card" style={{ padding: 20, background: '#090d16', border: '1px solid #1e293b' }}>
            <h3 style={{ fontSize: '1.05rem', fontWeight: 700, marginBottom: 16, display: 'flex', alignItems: 'center', gap: 8 }}>
              <GitBranch size={18} color="#f59e0b" /> Branching, Switching & Fast-Forward Merges
            </h3>

            <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: 16 }}>
              <div style={{ background: '#1e293b', padding: 16, borderRadius: 10 }}>
                <div style={{ fontWeight: 700, fontSize: '0.85rem', color: '#38bdf8', marginBottom: 8 }}>Active Branches:</div>
                <div style={{ display: 'flex', flexDirection: 'column', gap: 6 }}>
                  {branches.map((b, idx) => (
                    <div key={idx} style={{ padding: '8px 12px', background: '#090d16', borderRadius: '6px', fontSize: '0.8rem', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                      <span style={{ color: b === currentBranch ? '#10b981' : '#f8fafc', fontWeight: b === currentBranch ? 700 : 400 }}>
                        {b === currentBranch ? '● ' : ''}{b}
                      </span>
                      {b !== currentBranch && (
                        <button onClick={() => executeGitCommand(`git checkout ${b}`)} className="btn btn-ghost btn-sm" style={{ padding: '2px 8px', fontSize: '0.7rem' }}>
                          Checkout
                        </button>
                      )}
                    </div>
                  ))}
                </div>
              </div>

              <div style={{ background: '#1e293b', padding: 16, borderRadius: 10 }}>
                <div style={{ fontWeight: 700, fontSize: '0.85rem', color: '#10b981', marginBottom: 8 }}>Merge Operations:</div>
                <div style={{ display: 'flex', flexDirection: 'column', gap: 8 }}>
                  <button onClick={() => executeGitCommand(`git merge main`)} className="btn btn-primary btn-sm">
                    Merge 'main' into '{currentBranch}'
                  </button>
                  <button onClick={() => executeGitCommand(`git checkout -b feature/analytics`)} className="btn btn-secondary btn-sm">
                    Create & Switch Branch: 'feature/analytics'
                  </button>
                </div>
              </div>
            </div>
          </div>
        </div>
      )}

      {/* TAB 4: HISTORY REWRITING, REBASE & STASH */}
      {activeTab === 'undo-rebase' && (
        <div style={{ display: 'grid', gap: 20 }}>
          <div className="card" style={{ padding: 20, background: '#090d16', border: '1px solid #1e293b' }}>
            <h3 style={{ fontSize: '1.05rem', fontWeight: 700, marginBottom: 16, display: 'flex', alignItems: 'center', gap: 8 }}>
              <RotateCcw size={18} color="#ec4899" /> History Rewriting: `rebase`, `cherry-pick`, `reset`, `revert`, `stash`
            </h3>

            <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(220px, 1fr))', gap: 14 }}>
              <div style={{ background: '#1e293b', padding: 14, borderRadius: 10 }}>
                <div style={{ fontWeight: 700, fontSize: '0.8rem', color: '#ec4899', marginBottom: 4 }}>1. Linearize History (rebase)</div>
                <p style={{ fontSize: '0.75rem', color: '#94a3b8', margin: '0 0 10px 0' }}>Replays commits on top of base without merge nodes.</p>
                <button onClick={() => executeGitCommand('git rebase main')} className="btn btn-outline btn-sm" style={{ width: '100%', fontSize: '0.75rem' }}>
                  git rebase main
                </button>
              </div>

              <div style={{ background: '#1e293b', padding: 14, borderRadius: 10 }}>
                <div style={{ fontWeight: 700, fontSize: '0.8rem', color: '#38bdf8', marginBottom: 4 }}>2. Cherry-Pick Commit</div>
                <p style={{ fontSize: '0.75rem', color: '#94a3b8', margin: '0 0 10px 0' }}>Applies a single commit delta onto HEAD.</p>
                <button onClick={() => executeGitCommand('git cherry-pick 3c19e4')} className="btn btn-outline btn-sm" style={{ width: '100%', fontSize: '0.75rem' }}>
                  git cherry-pick 3c19e4
                </button>
              </div>

              <div style={{ background: '#1e293b', padding: 14, borderRadius: 10 }}>
                <div style={{ fontWeight: 700, fontSize: '0.8rem', color: '#f59e0b', marginBottom: 4 }}>3. Stash Stack (git stash)</div>
                <p style={{ fontSize: '0.75rem', color: '#94a3b8', margin: '0 0 10px 0' }}>Items in stack: <strong>{stashStack.length}</strong></p>
                <div style={{ display: 'flex', gap: 6 }}>
                  <button onClick={() => executeGitCommand('git stash')} className="btn btn-outline btn-sm" style={{ flex: 1, fontSize: '0.75rem' }}>Stash</button>
                  <button onClick={() => executeGitCommand('git stash pop')} className="btn btn-outline btn-sm" style={{ flex: 1, fontSize: '0.75rem' }}>Pop</button>
                </div>
              </div>

              <div style={{ background: '#1e293b', padding: 14, borderRadius: 10 }}>
                <div style={{ fontWeight: 700, fontSize: '0.8rem', color: '#f43f5e', marginBottom: 4 }}>4. Reset & Revert</div>
                <p style={{ fontSize: '0.75rem', color: '#94a3b8', margin: '0 0 10px 0' }}>Undo commits destructively or via inverse patches.</p>
                <div style={{ display: 'flex', gap: 6 }}>
                  <button onClick={() => executeGitCommand('git reset --hard HEAD~1')} className="btn btn-outline btn-sm" style={{ flex: 1, fontSize: '0.7rem' }}>Hard Reset</button>
                  <button onClick={() => executeGitCommand('git revert 9a01f8')} className="btn btn-outline btn-sm" style={{ flex: 1, fontSize: '0.7rem' }}>Revert</button>
                </div>
              </div>
            </div>
          </div>
        </div>
      )}

      {/* TAB 5: REMOTE SYNC & COLLABORATION */}
      {activeTab === 'remotes-sync' && (
        <div style={{ display: 'grid', gap: 20 }}>
          <div className="card" style={{ padding: 20, background: '#090d16', border: '1px solid #1e293b' }}>
            <h3 style={{ fontSize: '1.05rem', fontWeight: 700, marginBottom: 16, display: 'flex', alignItems: 'center', gap: 8 }}>
              <UploadCloud size={18} color="#8b5cf6" /> Remote Synchronization (`remote`, `fetch`, `pull`, `push`)
            </h3>

            <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: 16 }}>
              <div style={{ background: '#1e293b', padding: 16, borderRadius: 10 }}>
                <div style={{ fontWeight: 700, fontSize: '0.85rem', color: '#8b5cf6', marginBottom: 4 }}>Remote Endpoints (origin):</div>
                <div style={{ fontFamily: 'monospace', fontSize: '0.75rem', color: '#38bdf8', padding: '8px', background: '#090d16', borderRadius: '6px' }}>
                  {remoteOriginUrl}
                </div>
                <div style={{ fontSize: '0.75rem', color: '#94a3b8', marginTop: 8 }}>
                  Commits on Remote: <strong>{remoteCommitsCount}</strong> • Local Commits: <strong>{commits.length}</strong>
                </div>
              </div>

              <div style={{ background: '#1e293b', padding: 16, borderRadius: 10, display: 'flex', flexDirection: 'column', gap: 8 }}>
                <button onClick={() => executeGitCommand('git fetch origin')} className="btn btn-outline btn-sm">
                  <DownloadCloud size={14} /> Fetch Remote Objects (git fetch origin)
                </button>
                <button onClick={() => executeGitCommand('git pull origin main')} className="btn btn-secondary btn-sm">
                  <RotateCw size={14} /> Pull & Merge Remote (git pull origin main)
                </button>
                <button onClick={() => executeGitCommand('git push origin main')} className="btn btn-primary btn-sm">
                  <UploadCloud size={14} /> Push Local Commits (git push origin main)
                </button>
              </div>
            </div>
          </div>
        </div>
      )}

      {/* TAB 6: GITHUB PULL REQUESTS & REVIEWS */}
      {activeTab === 'github-pr' && (
        <div style={{ display: 'grid', gap: 20 }}>
          <div className="card" style={{ padding: 20, background: '#090d16', border: '1px solid #1e293b' }}>
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: 16 }}>
              <div>
                <span style={{ fontSize: '0.75rem', color: '#8b5cf6', fontWeight: 700 }}>PULL REQUEST #42</span>
                <h3 style={{ fontSize: '1.2rem', fontWeight: 800, margin: '2px 0 0 0', color: '#f8fafc' }}>
                  feat: implement enterprise JWT authentication and security headers
                </h3>
              </div>
              <span
                style={{
                  padding: '4px 12px',
                  borderRadius: '20px',
                  fontSize: '0.75rem',
                  fontWeight: 700,
                  background: prStatus === 'merged' ? 'rgba(139, 92, 246, 0.2)' : 'rgba(16, 185, 129, 0.2)',
                  color: prStatus === 'merged' ? '#8b5cf6' : '#10b981'
                }}
              >
                {prStatus.toUpperCase()}
              </span>
            </div>

            {/* Reviewers Feedback */}
            <div style={{ display: 'flex', flexDirection: 'column', gap: 8, marginBottom: 16 }}>
              {prReviews.map((r, idx) => (
                <div key={idx} style={{ padding: '10px 14px', background: '#1e293b', borderRadius: '8px', border: '1px solid #334155', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                  <div>
                    <span style={{ fontSize: '0.8rem', fontWeight: 700, color: '#f8fafc' }}>{r.reviewer}</span>
                    <div style={{ fontSize: '0.75rem', color: '#94a3b8', marginTop: 2 }}>{r.comment}</div>
                  </div>
                  <span style={{ fontSize: '0.7rem', color: '#10b981', fontWeight: 700 }}>✓ {r.status}</span>
                </div>
              ))}
            </div>

            {/* Merge Actions */}
            {prStatus === 'open' && (
              <div style={{ display: 'flex', gap: 10, alignItems: 'center', background: '#0f172a', padding: 14, borderRadius: 10, border: '1px solid #1e293b' }}>
                <select className="input" value={mergeStrategy} onChange={(e) => setMergeStrategy(e.target.value)} style={{ fontSize: '0.8rem' }}>
                  <option value="merge-commit">Create a merge commit</option>
                  <option value="squash">Squash and merge (1 commit)</option>
                  <option value="rebase">Rebase and merge</option>
                </select>
                <button onClick={handleMergePr} className="btn btn-primary" style={{ padding: '8px 16px', fontWeight: 700, fontSize: '0.8rem' }}>
                  <GitPullRequest size={14} /> Merge Pull Request
                </button>
              </div>
            )}
          </div>
        </div>
      )}

      {/* TAB 7: GITHUB ACTIONS CI/CD */}
      {activeTab === 'github-actions' && (
        <div style={{ display: 'grid', gap: 20 }}>
          <div className="card" style={{ padding: 20, background: '#090d16', border: '1px solid #1e293b' }}>
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: 16 }}>
              <div>
                <span style={{ fontSize: '0.75rem', color: '#06b6d4', fontWeight: 700 }}>WORKFLOW: .github/workflows/main.yml</span>
                <h3 style={{ fontSize: '1.1rem', fontWeight: 700, margin: '2px 0 0 0', color: '#f8fafc' }}>
                  🚀 Enterprise CI/CD Automated Deployment Matrix
                </h3>
              </div>
              <button onClick={runCicdPipeline} disabled={pipelineRunning} className="btn btn-primary btn-sm" style={{ gap: 6 }}>
                <Play size={12} /> {pipelineRunning ? 'Executing Stages...' : 'Trigger Workflow Dispatch'}
              </button>
            </div>

            <div style={{ display: 'flex', flexDirection: 'column', gap: 8 }}>
              {pipelineSteps.map((step) => (
                <div
                  key={step.id}
                  style={{
                    padding: '12px 16px',
                    background: '#1e293b',
                    borderRadius: '8px',
                    border: `1px solid ${step.status === 'success' ? '#10b981' : step.status === 'running' ? '#38bdf8' : '#334155'}`,
                    display: 'flex',
                    justifyContent: 'space-between',
                    alignItems: 'center'
                  }}
                >
                  <span style={{ fontSize: '0.8rem', fontWeight: 600, color: '#f8fafc' }}>{step.name}</span>
                  <span
                    style={{
                      fontSize: '0.7rem',
                      fontWeight: 700,
                      padding: '3px 8px',
                      borderRadius: '6px',
                      background: step.status === 'success' ? 'rgba(16, 185, 129, 0.2)' : step.status === 'running' ? 'rgba(56, 189, 248, 0.2)' : 'rgba(255, 255, 255, 0.05)',
                      color: step.status === 'success' ? '#10b981' : step.status === 'running' ? '#38bdf8' : '#94a3b8'
                    }}
                  >
                    {step.status.toUpperCase()} ({step.duration})
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


