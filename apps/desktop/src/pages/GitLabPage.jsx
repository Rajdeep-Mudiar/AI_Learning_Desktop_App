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
  Workflow,
  Cpu,
  CornerDownRight,
  Database
} from 'lucide-react';
import Badge from '../components/common/Badge';

export default function GitLabPage() {
  const [activeTab, setActiveTab] = useState('all-terminal'); 
  // 'all-terminal' | 'snapshots' | 'branching' | 'undo-rebase' | 'remotes-sync' | 'github-pr' | 'github-actions'

  // --- Dynamic Command Simulation State (Reacts dynamically to typed commands) ---
  const [activeSimView, setActiveSimView] = useState('dag'); 
  // 'dag' | 'staging-trees' | 'diff-inspector' | 'branch-network' | 'rebase-replay' | 'stash-stack' | 'remote-sync' | 'reset-rollback'
  const [lastExecutedCmd, setLastExecutedCmd] = useState('git status');
  const [simAlertMsg, setSimAlertMsg] = useState('Type any Git command below or click a quick-command pill to trigger live visual simulations.');

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
    'Type any Git command below or click a quick-command pill to execute simulations in real time.'
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

  // Live input detection to dynamically switch simulations as the user types
  const handleInputChange = (val) => {
    setCommandInput(val);
    const clean = val.trim().toLowerCase();
    if (!clean) return;

    if (clean.startsWith('git status') || clean.startsWith('git add')) {
      setActiveSimView('staging-trees');
    } else if (clean.startsWith('git diff')) {
      setActiveSimView('diff-inspector');
    } else if (clean.startsWith('git branch') || clean.startsWith('git checkout') || clean.startsWith('git switch')) {
      setActiveSimView('branch-network');
    } else if (clean.startsWith('git rebase') || clean.startsWith('git cherry-pick')) {
      setActiveSimView('rebase-replay');
    } else if (clean.startsWith('git stash')) {
      setActiveSimView('stash-stack');
    } else if (clean.startsWith('git remote') || clean.startsWith('git fetch') || clean.startsWith('git pull') || clean.startsWith('git push') || clean.startsWith('git clone')) {
      setActiveSimView('remote-sync');
    } else if (clean.startsWith('git reset') || clean.startsWith('git revert')) {
      setActiveSimView('reset-rollback');
    } else if (clean.startsWith('git commit') || clean.startsWith('git log') || clean.startsWith('git merge') || clean.startsWith('git tag') || clean.startsWith('git init')) {
      setActiveSimView('dag');
    }
  };

  // Command Execution Parser
  const executeGitCommand = (rawCmd) => {
    const cmd = rawCmd.trim();
    if (!cmd) return;

    setTerminalHistory(prev => [...prev, `$ ${cmd}`]);
    setCommandInput('');
    setLastExecutedCmd(cmd);

    const lowerCmd = cmd.toLowerCase();

    if (cmd === 'git init') {
      setRepoInitialized(true);
      setActiveSimView('dag');
      setSimAlertMsg('✅ Created `.git/` metadata folder, initialized object database & refs/heads/main.');
      setTerminalHistory(prev => [...prev, 'Initialized empty Git repository in /workspace/.git/']);
    } 
    else if (lowerCmd.startsWith('git clone')) {
      const url = cmd.replace(/git clone\s*/i, '').trim() || 'https://github.com/developer/ai-lab-app.git';
      setRemoteOriginUrl(url);
      setActiveSimView('remote-sync');
      setSimAlertMsg(`☁️ Cloned remote repository from ${url} into local working directory.`);
      setTerminalHistory(prev => [
        ...prev,
        `Cloning into 'repo'...`,
        `remote: Enumerating objects: 14, done.`,
        `remote: Total 14 (delta 2), reused 12`,
        `Receiving objects: 100% (14/14), done.`
      ]);
    }
    else if (lowerCmd === 'git status' || lowerCmd.startsWith('git status')) {
      setActiveSimView('staging-trees');
      setSimAlertMsg('🔍 3-Trees Status Inspector: Comparing Working Directory, Staging Index, and HEAD.');
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
    else if (lowerCmd === 'git add .' || lowerCmd.startsWith('git add')) {
      setActiveSimView('staging-trees');
      const newlyStaged = workingFiles.filter(f => f.status !== 'clean');
      setStagedFiles(prev => [...prev, ...newlyStaged]);
      setWorkingFiles(prev => prev.map(f => ({ ...f, status: 'clean' })));
      setSimAlertMsg(`📦 Staged ${newlyStaged.length || 'all'} file snapshot(s) into the Git Index.`);
      setTerminalHistory(prev => [...prev, `Staged all modified & untracked changes to index.`]);
    }
    else if (lowerCmd.startsWith('git commit -m') || lowerCmd.startsWith('git commit -am') || lowerCmd.startsWith('git commit --message')) {
      setActiveSimView('dag');
      const match = cmd.match(/-m\s+["'](.*?)["']/i);
      const msg = match ? match[1] : 'Update codebase';
      const newHash = Math.random().toString(16).substring(2, 8);
      const parentId = commits.length > 0 ? commits[commits.length - 1].id : null;
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
      setSimAlertMsg(`✨ Created immutable DAG commit object [${newHash}] on branch '${currentBranch}'.`);
      setTerminalHistory(prev => [...prev, `[${currentBranch} ${newHash}] ${msg}`, ` 2 files changed, 22 insertions(+), 3 deletions(-)`]);
    }
    else if (lowerCmd.startsWith('git commit --amend')) {
      setActiveSimView('dag');
      const match = cmd.match(/-m\s+["'](.*?)["']/i);
      const newMsg = match ? match[1] : `${commits[commits.length - 1].message} (amended)`;
      setCommits(prev => {
        const copy = [...prev];
        if (copy.length > 0) {
          copy[copy.length - 1] = { ...copy[copy.length - 1], message: newMsg };
        }
        return copy;
      });
      setSimAlertMsg(`✏️ Amended commit ${commits[commits.length - 1]?.hash || ''} with updated message & snapshot.`);
      setTerminalHistory(prev => [...prev, `[${currentBranch} ${commits[commits.length - 1]?.hash}] ${newMsg} (amended)`]);
    }
    else if (lowerCmd.startsWith('git branch -d') || lowerCmd.startsWith('git branch -d')) {
      setActiveSimView('branch-network');
      const target = cmd.replace(/git branch -[dD]\s+/i, '').trim();
      if (target === currentBranch) {
        setSimAlertMsg(`⚠️ Error: Cannot delete branch '${target}' checked out at current HEAD.`);
        setTerminalHistory(prev => [...prev, `error: Cannot delete branch '${target}' checked out at current HEAD.`]);
      } else if (branches.includes(target)) {
        setBranches(prev => prev.filter(b => b !== target));
        setSimAlertMsg(`🗑️ Deleted branch pointer '${target}'.`);
        setTerminalHistory(prev => [...prev, `Deleted branch ${target} (was ${commits[commits.length - 1]?.hash}).`]);
      } else {
        setTerminalHistory(prev => [...prev, `error: branch '${target}' not found.`]);
      }
    }
    else if (lowerCmd.startsWith('git branch') && lowerCmd !== 'git branch' && lowerCmd !== 'git branch -a') {
      setActiveSimView('branch-network');
      const newBranch = cmd.replace(/git branch\s+/i, '').trim();
      if (!branches.includes(newBranch)) {
        setBranches(prev => [...prev, newBranch]);
        setSimAlertMsg(`🌿 Created new branch pointer '${newBranch}' pointing to commit ${commits[commits.length - 1]?.hash}.`);
        setTerminalHistory(prev => [...prev, `Created branch '${newBranch}'`]);
      } else {
        setTerminalHistory(prev => [...prev, `fatal: A branch named '${newBranch}' already exists.`]);
      }
    }
    else if (lowerCmd === 'git branch' || lowerCmd === 'git branch -a') {
      setActiveSimView('branch-network');
      setSimAlertMsg(`🌿 Active branch: '${currentBranch}'. Total branches: ${branches.length}.`);
      setTerminalHistory(prev => [
        ...prev,
        ...branches.map(b => (b === currentBranch ? `* \x1b[32m${b}\x1b[0m` : `  ${b}`))
      ]);
    }
    else if (lowerCmd.startsWith('git checkout -b') || lowerCmd.startsWith('git switch -c')) {
      setActiveSimView('branch-network');
      const newBranch = cmd.replace(/git checkout -b\s+/i, '').replace(/git switch -c\s+/i, '').trim();
      setBranches(prev => [...prev, newBranch]);
      setCurrentBranch(newBranch);
      setSimAlertMsg(`🌿 Created branch '${newBranch}' and moved HEAD pointer to it.`);
      setTerminalHistory(prev => [...prev, `Switched to a new branch '${newBranch}'`]);
    }
    else if (lowerCmd.startsWith('git checkout') || lowerCmd.startsWith('git switch')) {
      setActiveSimView('branch-network');
      const target = cmd.replace(/git checkout\s+/i, '').replace(/git switch\s+/i, '').trim();
      if (branches.includes(target)) {
        setCurrentBranch(target);
        setSimAlertMsg(`👉 HEAD pointer moved to branch '${target}'.`);
        setTerminalHistory(prev => [...prev, `Switched to branch '${target}'`]);
      } else {
        setTerminalHistory(prev => [...prev, `error: pathspec '${target}' did not match any file(s) known to git`]);
      }
    }
    else if (lowerCmd.startsWith('git merge')) {
      setActiveSimView('dag');
      const sourceBranch = cmd.replace(/git merge\s+/i, '').trim() || 'feature/auth';
      const newHash = Math.random().toString(16).substring(2, 8);
      const newCommit = {
        id: `c${commits.length + 1}`,
        hash: newHash,
        message: `Merge branch '${sourceBranch}' into ${currentBranch}`,
        branch: currentBranch,
        parent: commits[commits.length - 1]?.id || null,
        author: 'Alex Chen'
      };
      setCommits(prev => [...prev, newCommit]);
      setSimAlertMsg(`🔀 Merged branch '${sourceBranch}' into '${currentBranch}' with 3-way merge commit [${newHash}].`);
      setTerminalHistory(prev => [...prev, `Merge made by the 'ort' strategy. [${currentBranch} ${newHash}]`]);
    }
    else if (lowerCmd.startsWith('git rebase')) {
      setActiveSimView('rebase-replay');
      const baseBranch = cmd.replace(/git rebase\s+/i, '').trim() || 'main';
      setSimAlertMsg(`⚡ Replayed ${currentBranch} commits linearly on top of ${baseBranch} without merge clutter.`);
      setTerminalHistory(prev => [
        ...prev,
        `First, rewinding head to replay your work on top of '${baseBranch}'...`,
        `Applying: ${commits[commits.length - 1]?.message || 'Current work'}`,
        `Successfully rebased and updated refs/heads/${currentBranch}.`
      ]);
    }
    else if (lowerCmd.startsWith('git cherry-pick')) {
      setActiveSimView('rebase-replay');
      const pickHash = cmd.replace(/git cherry-pick\s+/i, '').trim() || '3c19e4';
      const newHash = Math.random().toString(16).substring(2, 8);
      const picked = {
        id: `c${commits.length + 1}`,
        hash: newHash,
        message: `Cherry-picked: ${pickHash}`,
        branch: currentBranch,
        parent: commits[commits.length - 1]?.id || null,
        author: 'Alex Chen'
      };
      setCommits(prev => [...prev, picked]);
      setSimAlertMsg(`🍒 Cherry-picked commit ${pickHash} and applied its diff directly onto HEAD [${newHash}].`);
      setTerminalHistory(prev => [...prev, `[${currentBranch} ${newHash}] Cherry-picked ${pickHash}`]);
    }
    else if (lowerCmd.startsWith('git reset --hard')) {
      setActiveSimView('reset-rollback');
      if (commits.length > 1) {
        setCommits(prev => prev.slice(0, prev.length - 1));
        setStagedFiles([]);
        setSimAlertMsg(`⚠️ Hard Reset: Rolled HEAD back 1 commit and wiped Staged Index & Working Tree.`);
        setTerminalHistory(prev => [...prev, `HEAD is now at ${commits[commits.length - 2]?.hash} ${commits[commits.length - 2]?.message}`]);
      } else {
        setTerminalHistory(prev => [...prev, `Cannot reset further back; only 1 commit exists.`]);
      }
    }
    else if (lowerCmd.startsWith('git reset --soft')) {
      setActiveSimView('reset-rollback');
      setSimAlertMsg(`↩️ Soft Reset: Rolled HEAD back 1 commit while preserving all changes in the Staging Index.`);
      setTerminalHistory(prev => [...prev, `HEAD moved back 1 commit. Previous changes retained in staging index.`]);
    }
    else if (lowerCmd.startsWith('git reset')) {
      setActiveSimView('reset-rollback');
      setStagedFiles([]);
      setSimAlertMsg(`↩️ Mixed Reset: Unstaged all changes from Index; working files remain intact.`);
      setTerminalHistory(prev => [...prev, `Unstaged all changes. Working tree files preserved.`]);
    }
    else if (lowerCmd.startsWith('git revert')) {
      setActiveSimView('reset-rollback');
      const revHash = cmd.replace(/git revert\s+/i, '').trim() || '9a01f8';
      const newHash = Math.random().toString(16).substring(2, 8);
      const revertCommit = {
        id: `c${commits.length + 1}`,
        hash: newHash,
        message: `Revert "${revHash}"`,
        branch: currentBranch,
        parent: commits[commits.length - 1]?.id || null,
        author: 'Alex Chen'
      };
      setCommits(prev => [...prev, revertCommit]);
      setSimAlertMsg(`⏪ Reverted commit ${revHash} safely by appending inverse forward patch [${newHash}].`);
      setTerminalHistory(prev => [...prev, `[${currentBranch} ${newHash}] Revert "${revHash}"`]);
    }
    else if (lowerCmd === 'git stash' || lowerCmd === 'git stash push' || lowerCmd.startsWith('git stash push')) {
      setActiveSimView('stash-stack');
      const stashed = workingFiles.filter(f => f.status !== 'clean');
      setStashStack(prev => [{ id: `stash@{${prev.length}}`, items: stashed, branch: currentBranch }, ...prev]);
      setWorkingFiles(prev => prev.map(f => ({ ...f, status: 'clean' })));
      setSimAlertMsg(`📦 Saved uncommitted working changes into LIFO Stash Stack (stash@{0}).`);
      setTerminalHistory(prev => [...prev, `Saved working directory and index state WIP on ${currentBranch}: ${commits[commits.length - 1]?.hash}`]);
    }
    else if (lowerCmd === 'git stash pop') {
      setActiveSimView('stash-stack');
      if (stashStack.length > 0) {
        setStashStack(prev => prev.slice(1));
        setSimAlertMsg(`📤 Popped stash@{0} from stack and re-applied changes to working directory.`);
        setTerminalHistory(prev => [...prev, `Dropped stash@{0} and restored changes into working directory.`]);
      } else {
        setTerminalHistory(prev => [...prev, `error: No stash entries found.`]);
      }
    }
    else if (lowerCmd === 'git stash list') {
      setActiveSimView('stash-stack');
      setSimAlertMsg(`📋 Stash Stack contains ${stashStack.length} stashed item(s).`);
      setTerminalHistory(prev => [
        ...prev,
        ...(stashStack.length > 0 ? stashStack.map(s => `${s.id}: WIP on ${s.branch}`) : ['(no stash entries)'])
      ]);
    }
    else if (lowerCmd.startsWith('git tag -a') || lowerCmd.startsWith('git tag')) {
      if (lowerCmd === 'git tag') {
        setActiveSimView('dag');
        setSimAlertMsg(`🏷️ Displaying all repository release tags.`);
        setTerminalHistory(prev => [...prev, ...tags.map(t => t.name)]);
      } else {
        setActiveSimView('dag');
        const match = cmd.match(/git tag\s+(-a\s+)?([v\d\.]+)/i);
        const tagName = match ? match[2] : 'v1.0.0';
        setTags(prev => [...prev, { name: tagName, commitHash: commits[commits.length - 1]?.hash }]);
        setSimAlertMsg(`🏷️ Created release tag '${tagName}' pinned to commit ${commits[commits.length - 1]?.hash}.`);
        setTerminalHistory(prev => [...prev, `Created tag '${tagName}' pointing to commit ${commits[commits.length - 1]?.hash}`]);
      }
    }
    else if (lowerCmd.startsWith('git remote -v') || lowerCmd === 'git remote') {
      setActiveSimView('remote-sync');
      setSimAlertMsg(`☁️ Remote origin tracking configured to: ${remoteOriginUrl}`);
      setTerminalHistory(prev => [
        ...prev,
        `origin\t${remoteOriginUrl} (fetch)`,
        `origin\t${remoteOriginUrl} (push)`
      ]);
    }
    else if (lowerCmd.startsWith('git fetch')) {
      setActiveSimView('remote-sync');
      setSimAlertMsg(`⬇️ Fetched latest remote objects from ${remoteOriginUrl} into origin/main without merging.`);
      setTerminalHistory(prev => [
        ...prev,
        `remote: Enumerating objects: 6, done.`,
        `From ${remoteOriginUrl}`,
        ` * [new branch]      main       -> origin/main`
      ]);
    }
    else if (lowerCmd.startsWith('git pull')) {
      setActiveSimView('remote-sync');
      setSimAlertMsg(`🔄 Fetched & merged remote updates into local branch '${currentBranch}'.`);
      setTerminalHistory(prev => [
        ...prev,
        `Updating ${commits[0]?.hash}..${commits[commits.length - 1]?.hash}`,
        `Fast-forward`,
        ` 3 files changed, 45 insertions(+)`
      ]);
    }
    else if (lowerCmd.startsWith('git push')) {
      setActiveSimView('remote-sync');
      setRemoteCommitsCount(commits.length);
      setSimAlertMsg(`⬆️ Pushed ${commits.length} local commit objects to remote origin repository (${remoteOriginUrl}).`);
      setTerminalHistory(prev => [
        ...prev,
        `Enumerating objects: 12, done.`,
        `Writing objects: 100% (12/12), 1.84 KiB | 1.84 MiB/s, done.`,
        `To ${remoteOriginUrl}`,
        `   ${commits[0]?.hash}..${commits[commits.length - 1]?.hash}  ${currentBranch} -> ${currentBranch}`
      ]);
    }
    else if (lowerCmd === 'git log' || lowerCmd.startsWith('git log')) {
      setActiveSimView('dag');
      setSimAlertMsg(`📜 Log Output: Displaying linear DAG history from HEAD to root commit.`);
      setTerminalHistory(prev => [
        ...prev,
        ...commits.slice().reverse().map(c => `* ${c.hash} (${c.branch}) ${c.message}`)
      ]);
    }
    else if (lowerCmd === 'git diff' || lowerCmd.startsWith('git diff')) {
      setActiveSimView('diff-inspector');
      setSimAlertMsg(`📊 Visual Code Diff Inspector: Showing unified code additions & deletions.`);
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
    else if (lowerCmd === 'clear' || lowerCmd === 'cls') {
      setTerminalHistory([]);
    }
    else {
      setTerminalHistory(prev => [
        ...prev,
        `git: '${cmd}' is not a recognized command. Click a command pill below or type 'git status', 'git commit', 'git diff', 'git stash', 'git branch', etc.`
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

  const SIMULATION_VIEWS = [
    { id: 'dag', label: 'DAG Graph', icon: GitCommit, color: '#f59e0b' },
    { id: 'staging-trees', label: '3-Trees Staging', icon: Layers, color: '#10b981' },
    { id: 'diff-inspector', label: 'Diff Inspector', icon: FileCode, color: '#38bdf8' },
    { id: 'branch-network', label: 'Branch Network', icon: GitBranch, color: '#a855f7' },
    { id: 'rebase-replay', label: 'Rebase & Cherry-Pick', icon: RefreshCw, color: '#ec4899' },
    { id: 'stash-stack', label: 'Stash Stack', icon: Archive, color: '#eab308' },
    { id: 'remote-sync', label: 'Remote Sync', icon: UploadCloud, color: '#8b5cf6' },
    { id: 'reset-rollback', label: 'Reset Matrix', icon: RotateCcw, color: '#f43f5e' }
  ];

  return (
    <div className="animate-fade-in" style={{ paddingBottom: 40, width: '100%', maxWidth: '100%', minWidth: 0, boxSizing: 'border-box' }}>
      {/* Header */}
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', flexWrap: 'wrap', gap: 12, marginBottom: 16, width: '100%', minWidth: 0 }}>
        <div style={{ minWidth: 0, flex: 1 }}>
          <div style={{ display: 'flex', alignItems: 'center', gap: 8, marginBottom: 4, flexWrap: 'wrap' }}>
            <Badge variant="yellow"><GitBranch size={13} /> Git & GitHub Command Suite</Badge>
            <span style={{ fontSize: '0.8rem', color: 'var(--text-muted)' }}>Real-Time Reactive Simulator</span>
          </div>
          <h1 style={{ fontSize: '1.65rem', fontWeight: 800, wordBreak: 'break-word' }}>Complete Git & GitHub Command Simulator</h1>
          <p style={{ color: 'var(--text-secondary)', fontSize: '0.9rem', marginTop: 2 }}>
            Simulate every command: typed commands dynamically update live visual models in real time without horizontal page overflow.
          </p>
        </div>
      </div>

      {/* Primary Navigation Tabs */}
      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(130px, 1fr))', gap: 6, marginBottom: 16, width: '100%', minWidth: 0 }}>
        {[
          { id: 'all-terminal', title: '💻 Interactive Terminal & Stage', level: 'Every Command', color: '#38bdf8' },
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
                padding: '8px 10px',
                borderRadius: '8px',
                textAlign: 'left',
                cursor: 'pointer',
                transition: 'all 0.15s ease',
                minWidth: 0
              }}
            >
              <div style={{ fontSize: '0.62rem', fontWeight: 700, color: tab.color, textTransform: 'uppercase' }}>{tab.level}</div>
              <div style={{ fontSize: '0.75rem', fontWeight: 700, color: 'var(--text-primary)', marginTop: 2, whiteSpace: 'nowrap', overflow: 'hidden', textOverflow: 'ellipsis' }}>{tab.title}</div>
            </button>
          );
        })}
      </div>

      {/* Quick Interactive Command Dispatcher Bar */}
      <div className="card" style={{ padding: '10px 14px', marginBottom: 16, background: 'var(--bg-tertiary)', width: '100%', minWidth: 0, boxSizing: 'border-box' }}>
        <div style={{ fontSize: '0.75rem', fontWeight: 700, color: 'var(--text-muted)', marginBottom: 6, display: 'flex', alignItems: 'center', gap: 6 }}>
          <Sparkles size={13} color="#38bdf8" /> Quick Command Dispatcher (Click to Execute Instantly):
        </div>
        <div style={{ display: 'flex', gap: 5, flexWrap: 'wrap', width: '100%' }}>
          {COMMAND_PRESETS.map((item, idx) => (
            <button
              key={idx}
              onClick={() => executeGitCommand(item.cmd)}
              className="btn btn-ghost btn-sm"
              style={{
                fontFamily: 'monospace',
                fontSize: '0.72rem',
                background: 'var(--bg-card)',
                border: '1px solid var(--border-color)',
                padding: '3px 7px',
                borderRadius: '5px',
                color: '#38bdf8'
              }}
              title={`Run ${item.cmd}`}
            >
              {item.label}
            </button>
          ))}
        </div>
      </div>

      {/* TAB 1: ALL-COMMAND INTERACTIVE TERMINAL & DYNAMIC SIMULATION STAGE */}
      {activeTab === 'all-terminal' && (
        <div style={{ display: 'grid', gap: 16, width: '100%', minWidth: 0 }}>
          
          {/* REACTIVE SIMULATION STAGE */}
          <div className="card" style={{ padding: 16, background: '#090d16', border: '1px solid #1e293b', width: '100%', minWidth: 0, boxSizing: 'border-box' }}>
            
            {/* Stage Info Header */}
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', flexWrap: 'wrap', gap: 8, marginBottom: 10, width: '100%' }}>
              <div style={{ display: 'flex', alignItems: 'center', gap: 8, flexWrap: 'wrap' }}>
                <div style={{ padding: '4px 8px', borderRadius: '6px', background: 'rgba(56, 189, 248, 0.1)', border: '1px solid rgba(56, 189, 248, 0.3)', display: 'flex', alignItems: 'center', gap: 5 }}>
                  <Sparkles size={14} color="#38bdf8" />
                  <span style={{ fontSize: '0.8rem', fontWeight: 800, color: '#f8fafc' }}>
                    Live Stage:
                  </span>
                  <span style={{ fontSize: '0.8rem', fontWeight: 700, color: SIMULATION_VIEWS.find(v => v.id === activeSimView)?.color || '#38bdf8' }}>
                    {SIMULATION_VIEWS.find(v => v.id === activeSimView)?.label}
                  </span>
                </div>

                <div style={{ background: '#1e293b', padding: '3px 8px', borderRadius: '6px', fontSize: '0.72rem', color: '#94a3b8' }}>
                  HEAD: <strong style={{ color: '#38bdf8' }}>{currentBranch}</strong>
                </div>
              </div>
            </div>

            {/* Simulation View Switcher Pills (Wrap cleanly without pushing off-screen) */}
            <div style={{ display: 'flex', gap: 5, flexWrap: 'wrap', marginBottom: 12, width: '100%' }}>
              {SIMULATION_VIEWS.map(v => {
                const isCurrent = activeSimView === v.id;
                const Icon = v.icon;
                return (
                  <button
                    key={v.id}
                    onClick={() => setActiveSimView(v.id)}
                    style={{
                      padding: '4px 8px',
                      borderRadius: '6px',
                      fontSize: '0.68rem',
                      fontWeight: 600,
                      display: 'flex',
                      alignItems: 'center',
                      gap: 4,
                      background: isCurrent ? v.color : '#1e293b',
                      color: isCurrent ? '#090d16' : '#94a3b8',
                      border: 'none',
                      cursor: 'pointer',
                      transition: 'all 0.15s ease'
                    }}
                  >
                    <Icon size={11} />
                    {v.label}
                  </button>
                );
              })}
            </div>

            {/* Dynamic Status Alert Message Banner */}
            <div style={{ padding: '8px 12px', borderRadius: '6px', background: '#0f172a', border: '1px solid #334155', marginBottom: 14, display: 'flex', alignItems: 'center', gap: 6, fontSize: '0.78rem', color: '#e2e8f0', wordBreak: 'break-word' }}>
              <span style={{ color: '#38bdf8', fontWeight: 700, whiteSpace: 'nowrap' }}>Last Action:</span>
              <span style={{ flex: 1, minWidth: 0 }}>{simAlertMsg}</span>
            </div>

            {/* VIEW 1: DAG COMMIT GRAPH CANVAS */}
            {activeSimView === 'dag' && (
              <div style={{ width: '100%', minWidth: 0, overflow: 'hidden' }}>
                <div style={{ display: 'flex', alignItems: 'center', gap: 14, overflowX: 'auto', padding: '12px 4px', minHeight: '125px', width: '100%', boxSizing: 'border-box' }}>
                  {commits.map((c, idx) => {
                    const isHead = c.branch === currentBranch && idx === commits.map(x => x.branch).lastIndexOf(currentBranch);
                    const hasTag = tags.find(t => t.commitHash === c.hash);
                    return (
                      <div key={c.id} style={{ display: 'flex', alignItems: 'center', gap: 10, flexShrink: 0 }}>
                        <div
                          style={{
                            background: c.branch === 'main' ? '#1e293b' : '#312e81',
                            border: isHead ? '2px solid #38bdf8' : `1px solid ${c.branch === 'main' ? '#334155' : '#6366f1'}`,
                            padding: '10px 14px',
                            borderRadius: '8px',
                            minWidth: '145px',
                            maxWidth: '200px',
                            boxShadow: isHead ? '0 0 14px rgba(56, 189, 248, 0.35)' : 'none',
                            position: 'relative'
                          }}
                        >
                          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: 3 }}>
                            <span style={{ fontFamily: 'monospace', fontSize: '0.75rem', color: '#f59e0b', fontWeight: 700 }}>{c.hash}</span>
                            <span style={{ fontSize: '0.62rem', padding: '1px 5px', borderRadius: '4px', background: c.branch === 'main' ? '#0f172a' : '#4338ca', color: '#e2e8f0', fontWeight: 600 }}>{c.branch}</span>
                          </div>
                          <div style={{ fontSize: '0.8rem', fontWeight: 600, color: '#f8fafc', whiteSpace: 'nowrap', overflow: 'hidden', textOverflow: 'ellipsis' }}>{c.message}</div>
                          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginTop: 4, fontSize: '0.68rem', color: '#94a3b8' }}>
                            <span>{c.author}</span>
                            {isHead && <span style={{ color: '#38bdf8', fontWeight: 700 }}>HEAD ➔</span>}
                          </div>
                          {hasTag && (
                            <div style={{ position: 'absolute', top: -8, right: 8, background: '#f59e0b', color: '#090d16', fontSize: '0.6rem', fontWeight: 800, padding: '1px 5px', borderRadius: '4px' }}>
                              🏷️ {hasTag.name}
                            </div>
                          )}
                        </div>
                        {idx < commits.length - 1 && <div style={{ color: '#475569', fontSize: '1.2rem', flexShrink: 0 }}>➔</div>}
                      </div>
                    );
                  })}
                </div>
              </div>
            )}

            {/* VIEW 2: 3-TREES STAGING INSPECTOR */}
            {activeSimView === 'staging-trees' && (
              <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(200px, 1fr))', gap: 12, width: '100%', minWidth: 0 }}>
                {/* 1. Working Directory */}
                <div style={{ background: '#1e293b', padding: 12, borderRadius: 8, border: '1px solid #334155', minWidth: 0 }}>
                  <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: 8 }}>
                    <span style={{ fontWeight: 700, fontSize: '0.78rem', color: '#f43f5e', display: 'flex', alignItems: 'center', gap: 4 }}>
                      <FileCode size={13} /> 1. Working Tree
                    </span>
                    <button onClick={() => executeGitCommand('git add .')} className="btn btn-primary btn-sm" style={{ padding: '2px 6px', fontSize: '0.65rem' }}>
                      + git add .
                    </button>
                  </div>
                  <div style={{ display: 'flex', flexDirection: 'column', gap: 5 }}>
                    {workingFiles.map((f, idx) => (
                      <div key={idx} style={{ padding: '6px 8px', background: '#090d16', borderRadius: '5px', fontSize: '0.72rem', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                        <span style={{ overflow: 'hidden', textOverflow: 'ellipsis', whiteSpace: 'nowrap' }}>📄 {f.name}</span>
                        <span style={{ color: f.status === 'clean' ? '#10b981' : '#f43f5e', fontWeight: 700, fontSize: '0.68rem', marginLeft: 6 }}>{f.status}</span>
                      </div>
                    ))}
                  </div>
                </div>

                {/* 2. Staging Index */}
                <div style={{ background: '#1e293b', padding: 12, borderRadius: 8, border: '1px solid #334155', minWidth: 0 }}>
                  <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: 8 }}>
                    <span style={{ fontWeight: 700, fontSize: '0.78rem', color: '#10b981', display: 'flex', alignItems: 'center', gap: 4 }}>
                      <Layers size={13} /> 2. Staging Index
                    </span>
                    <button onClick={() => executeGitCommand('git reset')} disabled={stagedFiles.length === 0} className="btn btn-ghost btn-sm" style={{ padding: '2px 6px', fontSize: '0.65rem' }}>
                      git reset
                    </button>
                  </div>
                  <div style={{ display: 'flex', flexDirection: 'column', gap: 5 }}>
                    {stagedFiles.map((f, idx) => (
                      <div key={idx} style={{ padding: '6px 8px', background: '#090d16', borderRadius: '5px', fontSize: '0.72rem', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                        <span style={{ overflow: 'hidden', textOverflow: 'ellipsis', whiteSpace: 'nowrap' }}>✓ {f.name}</span>
                        <span style={{ color: '#10b981', fontWeight: 700, fontSize: '0.68rem' }}>STAGED</span>
                      </div>
                    ))}
                    {stagedFiles.length === 0 && <span style={{ fontSize: '0.72rem', color: '#94a3b8', fontStyle: 'italic', padding: '6px 0' }}>No staged snapshots</span>}
                  </div>
                </div>

                {/* 3. HEAD Commit */}
                <div style={{ background: '#1e293b', padding: 12, borderRadius: 8, border: '1px solid #334155', minWidth: 0 }}>
                  <div style={{ fontWeight: 700, fontSize: '0.78rem', color: '#38bdf8', marginBottom: 8, display: 'flex', alignItems: 'center', gap: 4 }}>
                    <GitCommit size={13} /> 3. Repository (HEAD)
                  </div>
                  <div style={{ padding: '10px', background: '#090d16', borderRadius: '6px' }}>
                    <div style={{ fontSize: '0.72rem', color: '#f59e0b', fontWeight: 700 }}>Commit: {commits[commits.length - 1]?.hash}</div>
                    <div style={{ fontSize: '0.78rem', color: '#f8fafc', fontWeight: 600, marginTop: 3 }}>{commits[commits.length - 1]?.message}</div>
                    <div style={{ fontSize: '0.7rem', color: '#94a3b8', marginTop: 2 }}>Branch: {commits[commits.length - 1]?.branch}</div>
                  </div>
                </div>
              </div>
            )}

            {/* VIEW 3: DIFF INSPECTOR */}
            {activeSimView === 'diff-inspector' && (
              <div style={{ background: '#0f172a', padding: 14, borderRadius: 8, border: '1px solid #334155', width: '100%', minWidth: 0, boxSizing: 'border-box' }}>
                <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: 8, flexWrap: 'wrap', gap: 6 }}>
                  <div style={{ display: 'flex', alignItems: 'center', gap: 6 }}>
                    <FileText size={14} color="#38bdf8" />
                    <span style={{ fontFamily: 'monospace', fontSize: '0.8rem', fontWeight: 700, color: '#f8fafc' }}>
                      diff --git a/{selectedDiffFile} b/{selectedDiffFile}
                    </span>
                  </div>
                  <span style={{ fontSize: '0.7rem', color: '#10b981', fontWeight: 700 }}>+14 lines</span>
                </div>

                <div style={{ fontFamily: 'monospace', fontSize: '0.75rem', background: '#090d16', padding: 10, borderRadius: 6, lineHeight: 1.5, overflowX: 'auto', width: '100%', boxSizing: 'border-box' }}>
                  <div style={{ color: '#94a3b8' }}>--- a/src/auth/jwt.py (Index)</div>
                  <div style={{ color: '#94a3b8' }}>+++ b/src/auth/jwt.py (Working Tree)</div>
                  <div style={{ color: '#64748b' }}>@@ -12,8 +12,12 @@ def generate_session_token(user_id: str):</div>
                  <div style={{ color: '#cbd5e1' }}>     payload = {`{"sub": user_id}`}</div>
                  <div style={{ background: 'rgba(244, 63, 94, 0.15)', color: '#f43f5e', padding: '2px 4px', borderRadius: '4px' }}>
                    -    return jwt.encode(payload, SECRET_KEY, algorithm="HS256")
                  </div>
                  <div style={{ background: 'rgba(16, 185, 129, 0.15)', color: '#10b981', padding: '2px 4px', borderRadius: '4px' }}>
                    +    expire = datetime.utcnow() + timedelta(minutes=60)
                  </div>
                  <div style={{ background: 'rgba(16, 185, 129, 0.15)', color: '#10b981', padding: '2px 4px', borderRadius: '4px' }}>
                    +    payload.update({`{"exp": expire, "role": "admin"}`})
                  </div>
                  <div style={{ background: 'rgba(16, 185, 129, 0.15)', color: '#10b981', padding: '2px 4px', borderRadius: '4px' }}>
                    +    return jwt.encode(payload, RSA_PRIVATE_KEY, algorithm="RS256")
                  </div>
                </div>
              </div>
            )}

            {/* VIEW 4: BRANCH NETWORK */}
            {activeSimView === 'branch-network' && (
              <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(200px, 1fr))', gap: 12, width: '100%', minWidth: 0 }}>
                <div style={{ background: '#1e293b', padding: 12, borderRadius: 8, minWidth: 0 }}>
                  <div style={{ fontWeight: 700, fontSize: '0.8rem', color: '#a855f7', marginBottom: 8, display: 'flex', alignItems: 'center', gap: 5 }}>
                    <GitBranch size={14} /> Active Branch Pointers:
                  </div>
                  <div style={{ display: 'flex', flexDirection: 'column', gap: 6 }}>
                    {branches.map((b, idx) => (
                      <div key={idx} style={{ padding: '6px 10px', background: '#090d16', borderRadius: '5px', fontSize: '0.75rem', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                        <span style={{ color: b === currentBranch ? '#10b981' : '#f8fafc', fontWeight: b === currentBranch ? 800 : 400 }}>
                          {b === currentBranch ? '● (HEAD) ' : '○ '}{b}
                        </span>
                        {b !== currentBranch && (
                          <button onClick={() => executeGitCommand(`git checkout ${b}`)} className="btn btn-ghost btn-sm" style={{ padding: '2px 6px', fontSize: '0.65rem' }}>
                            checkout
                          </button>
                        )}
                      </div>
                    ))}
                  </div>
                </div>

                <div style={{ background: '#1e293b', padding: 12, borderRadius: 8, minWidth: 0 }}>
                  <div style={{ fontWeight: 700, fontSize: '0.8rem', color: '#38bdf8', marginBottom: 8 }}>
                    Fast Branch Actions:
                  </div>
                  <div style={{ display: 'flex', flexDirection: 'column', gap: 6 }}>
                    <button onClick={() => executeGitCommand('git checkout -b feature/analytics')} className="btn btn-primary btn-sm" style={{ fontSize: '0.72rem', padding: '6px' }}>
                      + Branch 'feature/analytics'
                    </button>
                    <button onClick={() => executeGitCommand('git merge main')} className="btn btn-secondary btn-sm" style={{ fontSize: '0.72rem', padding: '6px' }}>
                      🔀 Merge 'main' into '{currentBranch}'
                    </button>
                    <button onClick={() => executeGitCommand('git switch main')} className="btn btn-outline btn-sm" style={{ fontSize: '0.72rem', padding: '6px' }}>
                      👉 Switch to 'main'
                    </button>
                  </div>
                </div>
              </div>
            )}

            {/* VIEW 5: REBASE & CHERRY-PICK REPLAY */}
            {activeSimView === 'rebase-replay' && (
              <div style={{ background: '#0f172a', padding: 14, borderRadius: 8, border: '1px solid #334155', width: '100%', minWidth: 0, boxSizing: 'border-box' }}>
                <div style={{ fontWeight: 700, fontSize: '0.8rem', color: '#ec4899', marginBottom: 6, display: 'flex', alignItems: 'center', gap: 5 }}>
                  <RefreshCw size={14} /> Linear Commit Replay vs Merge Commit:
                </div>
                <p style={{ fontSize: '0.75rem', color: '#94a3b8', marginBottom: 10 }}>
                  `git rebase` rewinds current branch commits, fast-forwards to base `main`, and reapplies commits sequentially without creating merge clutter.
                </p>
                <div style={{ display: 'flex', gap: 8, flexWrap: 'wrap' }}>
                  <button onClick={() => executeGitCommand('git rebase main')} className="btn btn-outline btn-sm" style={{ borderColor: '#ec4899', color: '#ec4899', fontSize: '0.72rem' }}>
                    ⚡ git rebase main
                  </button>
                  <button onClick={() => executeGitCommand('git cherry-pick 3c19e4')} className="btn btn-outline btn-sm" style={{ borderColor: '#38bdf8', color: '#38bdf8', fontSize: '0.72rem' }}>
                    🍒 git cherry-pick 3c19e4
                  </button>
                </div>
              </div>
            )}

            {/* VIEW 6: LIFO STASH STACK */}
            {activeSimView === 'stash-stack' && (
              <div style={{ background: '#0f172a', padding: 14, borderRadius: 8, border: '1px solid #334155', width: '100%', minWidth: 0, boxSizing: 'border-box' }}>
                <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: 8, flexWrap: 'wrap', gap: 6 }}>
                  <span style={{ fontWeight: 700, fontSize: '0.8rem', color: '#eab308', display: 'flex', alignItems: 'center', gap: 5 }}>
                    <Archive size={14} /> LIFO Stash Stack ({stashStack.length} items)
                  </span>
                  <div style={{ display: 'flex', gap: 6 }}>
                    <button onClick={() => executeGitCommand('git stash')} className="btn btn-primary btn-sm" style={{ padding: '2px 7px', fontSize: '0.68rem' }}>git stash</button>
                    <button onClick={() => executeGitCommand('git stash pop')} className="btn btn-secondary btn-sm" style={{ padding: '2px 7px', fontSize: '0.68rem' }}>git stash pop</button>
                  </div>
                </div>

                <div style={{ display: 'flex', flexDirection: 'column', gap: 5 }}>
                  {stashStack.map((s, idx) => (
                    <div key={idx} style={{ padding: '6px 10px', background: '#1e293b', borderRadius: '5px', fontSize: '0.75rem', display: 'flex', justifyContent: 'space-between' }}>
                      <span style={{ fontFamily: 'monospace', color: '#eab308' }}>{s.id}: WIP on {s.branch}</span>
                      <span style={{ color: '#94a3b8', fontSize: '0.7rem' }}>{s.items?.length || 1} file(s)</span>
                    </div>
                  ))}
                  {stashStack.length === 0 && (
                    <div style={{ color: '#94a3b8', fontSize: '0.72rem', fontStyle: 'italic', padding: 4 }}>
                      No stashed snapshots. Run 'git stash' to store temporary uncommitted state.
                    </div>
                  )}
                </div>
              </div>
            )}

            {/* VIEW 7: REMOTE SYNC & FETCH */}
            {activeSimView === 'remote-sync' && (
              <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(180px, 1fr))', gap: 10, alignItems: 'center', width: '100%', minWidth: 0 }}>
                <div style={{ background: '#1e293b', padding: 12, borderRadius: 8, minWidth: 0 }}>
                  <div style={{ fontWeight: 700, fontSize: '0.78rem', color: '#10b981', marginBottom: 3 }}>💻 Local Repo</div>
                  <div style={{ fontSize: '0.72rem', color: '#94a3b8' }}>Branch: {currentBranch}</div>
                  <div style={{ fontSize: '0.72rem', color: '#38bdf8', fontWeight: 700, marginTop: 2 }}>{commits.length} Local Commits</div>
                </div>

                <div style={{ display: 'flex', flexDirection: 'column', gap: 5, alignItems: 'stretch', minWidth: 0 }}>
                  <button onClick={() => executeGitCommand('git fetch origin')} className="btn btn-ghost btn-sm" style={{ fontSize: '0.68rem', padding: '4px' }}>
                    Fetch ⬇️
                  </button>
                  <button onClick={() => executeGitCommand('git pull origin main')} className="btn btn-secondary btn-sm" style={{ fontSize: '0.68rem', padding: '4px' }}>
                    Pull 🔄
                  </button>
                  <button onClick={() => executeGitCommand('git push origin main')} className="btn btn-primary btn-sm" style={{ fontSize: '0.68rem', padding: '4px' }}>
                    Push ⬆️
                  </button>
                </div>

                <div style={{ background: '#1e293b', padding: 12, borderRadius: 8, minWidth: 0 }}>
                  <div style={{ fontWeight: 700, fontSize: '0.78rem', color: '#8b5cf6', marginBottom: 3 }}>☁️ GitHub Remote</div>
                  <div style={{ fontSize: '0.68rem', color: '#94a3b8', wordBreak: 'break-all' }}>{remoteOriginUrl}</div>
                  <div style={{ fontSize: '0.72rem', color: '#8b5cf6', fontWeight: 700, marginTop: 2 }}>{remoteCommitsCount} Remote Commits</div>
                </div>
              </div>
            )}

            {/* VIEW 8: RESET & ROLLBACK MATRIX */}
            {activeSimView === 'reset-rollback' && (
              <div style={{ background: '#0f172a', padding: 14, borderRadius: 8, border: '1px solid #334155', width: '100%', minWidth: 0, boxSizing: 'border-box' }}>
                <div style={{ fontWeight: 700, fontSize: '0.8rem', color: '#f43f5e', marginBottom: 8, display: 'flex', alignItems: 'center', gap: 5 }}>
                  <RotateCcw size={14} /> Git Reset Comparison Matrix:
                </div>
                <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(140px, 1fr))', gap: 8, width: '100%', minWidth: 0 }}>
                  <div style={{ background: '#1e293b', padding: 8, borderRadius: 6, minWidth: 0 }}>
                    <div style={{ fontWeight: 700, fontSize: '0.72rem', color: '#38bdf8' }}>--soft HEAD~1</div>
                    <div style={{ fontSize: '0.65rem', color: '#94a3b8', marginTop: 2 }}>Preserves Index.</div>
                    <button onClick={() => executeGitCommand('git reset --soft HEAD~1')} className="btn btn-ghost btn-sm" style={{ marginTop: 4, fontSize: '0.62rem', padding: '2px 4px' }}>Soft Reset</button>
                  </div>
                  <div style={{ background: '#1e293b', padding: 8, borderRadius: 6, minWidth: 0 }}>
                    <div style={{ fontWeight: 700, fontSize: '0.72rem', color: '#f59e0b' }}>--mixed</div>
                    <div style={{ fontSize: '0.65rem', color: '#94a3b8', marginTop: 2 }}>Unstages Index.</div>
                    <button onClick={() => executeGitCommand('git reset')} className="btn btn-ghost btn-sm" style={{ marginTop: 4, fontSize: '0.62rem', padding: '2px 4px' }}>Mixed Reset</button>
                  </div>
                  <div style={{ background: '#1e293b', padding: 8, borderRadius: 6, minWidth: 0 }}>
                    <div style={{ fontWeight: 700, fontSize: '0.72rem', color: '#f43f5e' }}>--hard HEAD~1</div>
                    <div style={{ fontSize: '0.65rem', color: '#94a3b8', marginTop: 2 }}>Wipes uncommitted work.</div>
                    <button onClick={() => executeGitCommand('git reset --hard HEAD~1')} className="btn btn-ghost btn-sm" style={{ marginTop: 4, fontSize: '0.62rem', padding: '2px 4px', color: '#f43f5e' }}>Hard Reset</button>
                  </div>
                  <div style={{ background: '#1e293b', padding: 8, borderRadius: 6, minWidth: 0 }}>
                    <div style={{ fontWeight: 700, fontSize: '0.72rem', color: '#10b981' }}>git revert</div>
                    <div style={{ fontSize: '0.65rem', color: '#94a3b8', marginTop: 2 }}>Safe forward patch.</div>
                    <button onClick={() => executeGitCommand('git revert 9a01f8')} className="btn btn-ghost btn-sm" style={{ marginTop: 4, fontSize: '0.62rem', padding: '2px 4px' }}>Revert</button>
                  </div>
                </div>
              </div>
            )}
          </div>

          {/* Terminal Console */}
          <div className="card" style={{ padding: 0, overflow: 'hidden', background: '#090d16', border: '1px solid #1e293b', width: '100%', minWidth: 0, boxSizing: 'border-box' }}>
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', padding: '8px 14px', background: '#0f172a', borderBottom: '1px solid #1e293b' }}>
              <div style={{ display: 'flex', alignItems: 'center', gap: 6 }}>
                <Terminal size={14} color="#38bdf8" />
                <span style={{ fontSize: '0.78rem', fontWeight: 600, color: '#94a3b8' }}>Git Shell Emulator (Dynamic Live Simulation Sync)</span>
              </div>
              <button onClick={() => setTerminalHistory([])} className="btn btn-ghost btn-sm" style={{ padding: '2px 6px', fontSize: '0.68rem' }}>
                Clear Output
              </button>
            </div>

            <div style={{ padding: '12px 14px', minHeight: '160px', maxHeight: '220px', overflowY: 'auto', fontFamily: 'monospace', fontSize: '0.78rem', color: '#94a3b8', lineHeight: 1.5, width: '100%', boxSizing: 'border-box', wordBreak: 'break-all' }}>
              {terminalHistory.map((line, idx) => (
                <div key={idx} style={{ color: line.startsWith('$') ? '#38bdf8' : line.startsWith('fatal') || line.startsWith('error') ? '#f43f5e' : '#cbd5e1' }}>
                  {line}
                </div>
              ))}
            </div>

            <form onSubmit={(e) => { e.preventDefault(); executeGitCommand(commandInput); }} style={{ display: 'flex', borderTop: '1px solid #1e293b', background: '#0f172a', width: '100%', minWidth: 0 }}>
              <span style={{ padding: '8px 0 8px 12px', color: '#10b981', fontFamily: 'monospace', fontWeight: 700, fontSize: '0.8rem', whiteSpace: 'nowrap' }}>(repo) $</span>
              <input
                type="text"
                value={commandInput}
                onChange={(e) => handleInputChange(e.target.value)}
                placeholder="Type git commands here (e.g. git status, git commit -m 'feat', git diff, git branch, git stash, git push)..."
                style={{ flex: 1, minWidth: 0, width: '100%', background: 'transparent', border: 'none', padding: '8px 12px', color: '#f8fafc', fontFamily: 'monospace', fontSize: '0.8rem', outline: 'none' }}
              />
            </form>
          </div>
        </div>
      )}

      {/* TAB 2: 3-TREES & DIFF STAGING */}
      {activeTab === 'snapshots' && (
        <div style={{ display: 'grid', gap: 16, width: '100%', minWidth: 0 }}>
          <div className="card" style={{ padding: 16, background: '#090d16', border: '1px solid #1e293b', width: '100%', minWidth: 0, boxSizing: 'border-box' }}>
            <h3 style={{ fontSize: '1rem', fontWeight: 700, marginBottom: 14, display: 'flex', alignItems: 'center', gap: 6 }}>
              <Layers size={16} color="#10b981" /> Git 3-Trees Workflow (`git status`, `git add`, `git diff`)
            </h3>

            <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(200px, 1fr))', gap: 12, width: '100%', minWidth: 0 }}>
              {/* Working Tree */}
              <div style={{ background: '#1e293b', padding: 12, borderRadius: 8, border: '1px solid #334155', minWidth: 0 }}>
                <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: 8 }}>
                  <span style={{ fontWeight: 700, fontSize: '0.78rem', color: '#f43f5e' }}>1. Working Directory</span>
                  <button onClick={() => executeGitCommand('git add .')} className="btn btn-primary btn-sm" style={{ padding: '2px 6px', fontSize: '0.65rem' }}>
                    + Stage All (git add .)
                  </button>
                </div>
                <div style={{ display: 'flex', flexDirection: 'column', gap: 5 }}>
                  {workingFiles.map((f, idx) => (
                    <div key={idx} style={{ padding: '6px 8px', background: '#090d16', borderRadius: '5px', fontSize: '0.72rem', display: 'flex', justifyContent: 'space-between' }}>
                      <span style={{ overflow: 'hidden', textOverflow: 'ellipsis', whiteSpace: 'nowrap' }}>📄 {f.name}</span>
                      <span style={{ color: f.status === 'clean' ? '#10b981' : '#f43f5e' }}>{f.status}</span>
                    </div>
                  ))}
                </div>
              </div>

              {/* Staging Area */}
              <div style={{ background: '#1e293b', padding: 12, borderRadius: 8, border: '1px solid #334155', minWidth: 0 }}>
                <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: 8 }}>
                  <span style={{ fontWeight: 700, fontSize: '0.78rem', color: '#10b981' }}>2. Staging Index (Cache)</span>
                  <button onClick={() => executeGitCommand('git reset')} disabled={stagedFiles.length === 0} className="btn btn-ghost btn-sm" style={{ padding: '2px 6px', fontSize: '0.65rem' }}>
                    Unstage (git reset)
                  </button>
                </div>
                <div style={{ display: 'flex', flexDirection: 'column', gap: 5 }}>
                  {stagedFiles.map((f, idx) => (
                    <div key={idx} style={{ padding: '6px 8px', background: '#090d16', borderRadius: '5px', fontSize: '0.72rem', display: 'flex', justifyContent: 'space-between' }}>
                      <span>✓ {f.name}</span>
                      <span style={{ color: '#10b981' }}>STAGED</span>
                    </div>
                  ))}
                  {stagedFiles.length === 0 && <span style={{ fontSize: '0.72rem', color: '#94a3b8' }}>No staged snapshots</span>}
                </div>
              </div>

              {/* Local HEAD Commit */}
              <div style={{ background: '#1e293b', padding: 12, borderRadius: 8, border: '1px solid #334155', minWidth: 0 }}>
                <div style={{ fontWeight: 700, fontSize: '0.78rem', color: '#38bdf8', marginBottom: 8 }}>3. Local Repository (HEAD)</div>
                <div style={{ padding: '10px', background: '#090d16', borderRadius: '6px' }}>
                  <div style={{ fontSize: '0.72rem', color: '#f59e0b', fontWeight: 700 }}>Commit: {commits[commits.length - 1]?.hash}</div>
                  <div style={{ fontSize: '0.78rem', color: '#f8fafc', marginTop: 3 }}>{commits[commits.length - 1]?.message}</div>
                  <div style={{ fontSize: '0.68rem', color: '#94a3b8', marginTop: 2 }}>Branch: {commits[commits.length - 1]?.branch}</div>
                </div>
              </div>
            </div>
          </div>
        </div>
      )}

      {/* TAB 3: BRANCHING & MERGES */}
      {activeTab === 'branching' && (
        <div style={{ display: 'grid', gap: 16, width: '100%', minWidth: 0 }}>
          <div className="card" style={{ padding: 16, background: '#090d16', border: '1px solid #1e293b', width: '100%', minWidth: 0, boxSizing: 'border-box' }}>
            <h3 style={{ fontSize: '1rem', fontWeight: 700, marginBottom: 14, display: 'flex', alignItems: 'center', gap: 6 }}>
              <GitBranch size={16} color="#f59e0b" /> Branching, Switching & Fast-Forward Merges
            </h3>

            <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(200px, 1fr))', gap: 12, width: '100%', minWidth: 0 }}>
              <div style={{ background: '#1e293b', padding: 12, borderRadius: 8, minWidth: 0 }}>
                <div style={{ fontWeight: 700, fontSize: '0.8rem', color: '#38bdf8', marginBottom: 8 }}>Active Branches:</div>
                <div style={{ display: 'flex', flexDirection: 'column', gap: 5 }}>
                  {branches.map((b, idx) => (
                    <div key={idx} style={{ padding: '6px 10px', background: '#090d16', borderRadius: '5px', fontSize: '0.75rem', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                      <span style={{ color: b === currentBranch ? '#10b981' : '#f8fafc', fontWeight: b === currentBranch ? 700 : 400 }}>
                        {b === currentBranch ? '● ' : ''}{b}
                      </span>
                      {b !== currentBranch && (
                        <button onClick={() => executeGitCommand(`git checkout ${b}`)} className="btn btn-ghost btn-sm" style={{ padding: '2px 6px', fontSize: '0.65rem' }}>
                          Checkout
                        </button>
                      )}
                    </div>
                  ))}
                </div>
              </div>

              <div style={{ background: '#1e293b', padding: 12, borderRadius: 8, minWidth: 0 }}>
                <div style={{ fontWeight: 700, fontSize: '0.8rem', color: '#10b981', marginBottom: 8 }}>Merge Operations:</div>
                <div style={{ display: 'flex', flexDirection: 'column', gap: 6 }}>
                  <button onClick={() => executeGitCommand(`git merge main`)} className="btn btn-primary btn-sm" style={{ fontSize: '0.72rem', padding: '6px' }}>
                    Merge 'main' into '{currentBranch}'
                  </button>
                  <button onClick={() => executeGitCommand(`git checkout -b feature/analytics`)} className="btn btn-secondary btn-sm" style={{ fontSize: '0.72rem', padding: '6px' }}>
                    Create Branch: 'feature/analytics'
                  </button>
                </div>
              </div>
            </div>
          </div>
        </div>
      )}

      {/* TAB 4: HISTORY REWRITING, REBASE & STASH */}
      {activeTab === 'undo-rebase' && (
        <div style={{ display: 'grid', gap: 16, width: '100%', minWidth: 0 }}>
          <div className="card" style={{ padding: 16, background: '#090d16', border: '1px solid #1e293b', width: '100%', minWidth: 0, boxSizing: 'border-box' }}>
            <h3 style={{ fontSize: '1rem', fontWeight: 700, marginBottom: 14, display: 'flex', alignItems: 'center', gap: 6 }}>
              <RotateCcw size={16} color="#ec4899" /> History Rewriting: `rebase`, `cherry-pick`, `reset`, `revert`, `stash`
            </h3>

            <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(180px, 1fr))', gap: 10, width: '100%', minWidth: 0 }}>
              <div style={{ background: '#1e293b', padding: 10, borderRadius: 8, minWidth: 0 }}>
                <div style={{ fontWeight: 700, fontSize: '0.78rem', color: '#ec4899', marginBottom: 3 }}>1. Linearize (rebase)</div>
                <p style={{ fontSize: '0.7rem', color: '#94a3b8', margin: '0 0 8px 0' }}>Replays commits on top of base.</p>
                <button onClick={() => executeGitCommand('git rebase main')} className="btn btn-outline btn-sm" style={{ width: '100%', fontSize: '0.7rem', padding: '4px' }}>
                  git rebase main
                </button>
              </div>

              <div style={{ background: '#1e293b', padding: 10, borderRadius: 8, minWidth: 0 }}>
                <div style={{ fontWeight: 700, fontSize: '0.78rem', color: '#38bdf8', marginBottom: 3 }}>2. Cherry-Pick</div>
                <p style={{ fontSize: '0.7rem', color: '#94a3b8', margin: '0 0 8px 0' }}>Applies a single commit delta.</p>
                <button onClick={() => executeGitCommand('git cherry-pick 3c19e4')} className="btn btn-outline btn-sm" style={{ width: '100%', fontSize: '0.7rem', padding: '4px' }}>
                  git cherry-pick 3c19e4
                </button>
              </div>

              <div style={{ background: '#1e293b', padding: 10, borderRadius: 8, minWidth: 0 }}>
                <div style={{ fontWeight: 700, fontSize: '0.78rem', color: '#f59e0b', marginBottom: 3 }}>3. Stash Stack</div>
                <p style={{ fontSize: '0.7rem', color: '#94a3b8', margin: '0 0 8px 0' }}>Items in stack: <strong>{stashStack.length}</strong></p>
                <div style={{ display: 'flex', gap: 4 }}>
                  <button onClick={() => executeGitCommand('git stash')} className="btn btn-outline btn-sm" style={{ flex: 1, fontSize: '0.68rem', padding: '3px' }}>Stash</button>
                  <button onClick={() => executeGitCommand('git stash pop')} className="btn btn-outline btn-sm" style={{ flex: 1, fontSize: '0.68rem', padding: '3px' }}>Pop</button>
                </div>
              </div>

              <div style={{ background: '#1e293b', padding: 10, borderRadius: 8, minWidth: 0 }}>
                <div style={{ fontWeight: 700, fontSize: '0.78rem', color: '#f43f5e', marginBottom: 3 }}>4. Reset & Revert</div>
                <p style={{ fontSize: '0.7rem', color: '#94a3b8', margin: '0 0 8px 0' }}>Undo commits or create patch.</p>
                <div style={{ display: 'flex', gap: 4 }}>
                  <button onClick={() => executeGitCommand('git reset --hard HEAD~1')} className="btn btn-outline btn-sm" style={{ flex: 1, fontSize: '0.65rem', padding: '3px' }}>Hard Reset</button>
                  <button onClick={() => executeGitCommand('git revert 9a01f8')} className="btn btn-outline btn-sm" style={{ flex: 1, fontSize: '0.65rem', padding: '3px' }}>Revert</button>
                </div>
              </div>
            </div>
          </div>
        </div>
      )}

      {/* TAB 5: REMOTE SYNC & COLLABORATION */}
      {activeTab === 'remotes-sync' && (
        <div style={{ display: 'grid', gap: 16, width: '100%', minWidth: 0 }}>
          <div className="card" style={{ padding: 16, background: '#090d16', border: '1px solid #1e293b', width: '100%', minWidth: 0, boxSizing: 'border-box' }}>
            <h3 style={{ fontSize: '1rem', fontWeight: 700, marginBottom: 14, display: 'flex', alignItems: 'center', gap: 6 }}>
              <UploadCloud size={16} color="#8b5cf6" /> Remote Synchronization (`remote`, `fetch`, `pull`, `push`)
            </h3>

            <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(200px, 1fr))', gap: 12, width: '100%', minWidth: 0 }}>
              <div style={{ background: '#1e293b', padding: 12, borderRadius: 8, minWidth: 0 }}>
                <div style={{ fontWeight: 700, fontSize: '0.8rem', color: '#8b5cf6', marginBottom: 3 }}>Remote Endpoints:</div>
                <div style={{ fontFamily: 'monospace', fontSize: '0.7rem', color: '#38bdf8', padding: '6px', background: '#090d16', borderRadius: '5px', wordBreak: 'break-all' }}>
                  {remoteOriginUrl}
                </div>
                <div style={{ fontSize: '0.72rem', color: '#94a3b8', marginTop: 6 }}>
                  Commits on Remote: <strong>{remoteCommitsCount}</strong> • Local: <strong>{commits.length}</strong>
                </div>
              </div>

              <div style={{ background: '#1e293b', padding: 12, borderRadius: 8, display: 'flex', flexDirection: 'column', gap: 6, minWidth: 0 }}>
                <button onClick={() => executeGitCommand('git fetch origin')} className="btn btn-outline btn-sm" style={{ fontSize: '0.72rem', padding: '5px' }}>
                  <DownloadCloud size={12} /> Fetch (git fetch)
                </button>
                <button onClick={() => executeGitCommand('git pull origin main')} className="btn btn-secondary btn-sm" style={{ fontSize: '0.72rem', padding: '5px' }}>
                  <RotateCw size={12} /> Pull (git pull)
                </button>
                <button onClick={() => executeGitCommand('git push origin main')} className="btn btn-primary btn-sm" style={{ fontSize: '0.72rem', padding: '5px' }}>
                  <UploadCloud size={12} /> Push (git push)
                </button>
              </div>
            </div>
          </div>
        </div>
      )}

      {/* TAB 6: GITHUB PULL REQUESTS & REVIEWS */}
      {activeTab === 'github-pr' && (
        <div style={{ display: 'grid', gap: 16, width: '100%', minWidth: 0 }}>
          <div className="card" style={{ padding: 16, background: '#090d16', border: '1px solid #1e293b', width: '100%', minWidth: 0, boxSizing: 'border-box' }}>
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: 14, flexWrap: 'wrap', gap: 6 }}>
              <div>
                <span style={{ fontSize: '0.7rem', color: '#8b5cf6', fontWeight: 700 }}>PULL REQUEST #42</span>
                <h3 style={{ fontSize: '1.05rem', fontWeight: 800, margin: '2px 0 0 0', color: '#f8fafc' }}>
                  feat: implement enterprise JWT authentication and security headers
                </h3>
              </div>
              <span
                style={{
                  padding: '3px 10px',
                  borderRadius: '16px',
                  fontSize: '0.7rem',
                  fontWeight: 700,
                  background: prStatus === 'merged' ? 'rgba(139, 92, 246, 0.2)' : 'rgba(16, 185, 129, 0.2)',
                  color: prStatus === 'merged' ? '#8b5cf6' : '#10b981'
                }}
              >
                {prStatus.toUpperCase()}
              </span>
            </div>

            {/* Reviewers Feedback */}
            <div style={{ display: 'flex', flexDirection: 'column', gap: 6, marginBottom: 12 }}>
              {prReviews.map((r, idx) => (
                <div key={idx} style={{ padding: '8px 12px', background: '#1e293b', borderRadius: '6px', border: '1px solid #334155', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                  <div>
                    <span style={{ fontSize: '0.75rem', fontWeight: 700, color: '#f8fafc' }}>{r.reviewer}</span>
                    <div style={{ fontSize: '0.7rem', color: '#94a3b8', marginTop: 1 }}>{r.comment}</div>
                  </div>
                  <span style={{ fontSize: '0.68rem', color: '#10b981', fontWeight: 700 }}>✓ {r.status}</span>
                </div>
              ))}
            </div>

            {/* Merge Actions */}
            {prStatus === 'open' && (
              <div style={{ display: 'flex', gap: 8, alignItems: 'center', background: '#0f172a', padding: 10, borderRadius: 8, border: '1px solid #1e293b', flexWrap: 'wrap' }}>
                <select className="input" value={mergeStrategy} onChange={(e) => setMergeStrategy(e.target.value)} style={{ fontSize: '0.75rem', flex: 1, minWidth: '150px' }}>
                  <option value="merge-commit">Create a merge commit</option>
                  <option value="squash">Squash and merge</option>
                  <option value="rebase">Rebase and merge</option>
                </select>
                <button onClick={handleMergePr} className="btn btn-primary btn-sm" style={{ fontWeight: 700, fontSize: '0.75rem' }}>
                  <GitPullRequest size={13} /> Merge Pull Request
                </button>
              </div>
            )}
          </div>
        </div>
      )}

      {/* TAB 7: GITHUB ACTIONS CI/CD */}
      {activeTab === 'github-actions' && (
        <div style={{ display: 'grid', gap: 16, width: '100%', minWidth: 0 }}>
          <div className="card" style={{ padding: 16, background: '#090d16', border: '1px solid #1e293b', width: '100%', minWidth: 0, boxSizing: 'border-box' }}>
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: 14, flexWrap: 'wrap', gap: 6 }}>
              <div>
                <span style={{ fontSize: '0.7rem', color: '#06b6d4', fontWeight: 700 }}>WORKFLOW: .github/workflows/main.yml</span>
                <h3 style={{ fontSize: '1rem', fontWeight: 700, margin: '2px 0 0 0', color: '#f8fafc' }}>
                  🚀 Enterprise CI/CD Automated Deployment Matrix
                </h3>
              </div>
              <button onClick={runCicdPipeline} disabled={pipelineRunning} className="btn btn-primary btn-sm" style={{ gap: 5, fontSize: '0.72rem' }}>
                <Play size={11} /> {pipelineRunning ? 'Executing...' : 'Trigger Workflow'}
              </button>
            </div>

            <div style={{ display: 'flex', flexDirection: 'column', gap: 6 }}>
              {pipelineSteps.map((step) => (
                <div
                  key={step.id}
                  style={{
                    padding: '10px 14px',
                    background: '#1e293b',
                    borderRadius: '6px',
                    border: `1px solid ${step.status === 'success' ? '#10b981' : step.status === 'running' ? '#38bdf8' : '#334155'}`,
                    display: 'flex',
                    justifyContent: 'space-between',
                    alignItems: 'center'
                  }}
                >
                  <span style={{ fontSize: '0.75rem', fontWeight: 600, color: '#f8fafc' }}>{step.name}</span>
                  <span
                    style={{
                      fontSize: '0.65rem',
                      fontWeight: 700,
                      padding: '2px 6px',
                      borderRadius: '5px',
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
