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
    { label: 'git status', cmd: 'git status' },
    { label: 'git add .', cmd: 'git add .' },
    { label: 'git commit -m "..."', cmd: 'git commit -m "feat: implement security filters"' },
    { label: 'git commit --amend', cmd: 'git commit --amend -m "feat: implement security filters & tests"' },
    { label: 'git branch', cmd: 'git branch' },
    { label: 'git checkout -b new-feat', cmd: 'git checkout -b feature/payments' },
    { label: 'git switch main', cmd: 'git switch main' },
    { label: 'git merge feature/auth', cmd: 'git merge feature/auth' },
    { label: 'git rebase main', cmd: 'git rebase main' },
    { label: 'git cherry-pick 3c19e4', cmd: 'git cherry-pick 3c19e4' },
    { label: 'git reset --soft HEAD~1', cmd: 'git reset --soft HEAD~1' },
    { label: 'git reset --hard HEAD~1', cmd: 'git reset --hard HEAD~1' },
    { label: 'git revert 9a01f8', cmd: 'git revert 9a01f8' },
    { label: 'git stash', cmd: 'git stash' },
    { label: 'git stash pop', cmd: 'git stash pop' },
    { label: 'git tag -a v1.0.0', cmd: 'git tag -a v1.0.0' },
    { label: 'git diff', cmd: 'git diff' },
    { label: 'git log --oneline', cmd: 'git log --oneline --graph' },
    { label: 'git remote -v', cmd: 'git remote -v' },
    { label: 'git fetch origin', cmd: 'git fetch origin' },
    { label: 'git pull origin main', cmd: 'git pull origin main' },
    { label: 'git push origin main', cmd: 'git push origin main' }
  ];

  const SIMULATION_VIEWS = [
    { id: 'dag', label: 'DAG Graph', icon: GitCommit, color: '#f59e0b', glow: 'rgba(245, 158, 11, 0.4)' },
    { id: 'staging-trees', label: '3-Trees Staging', icon: Layers, color: '#10b981', glow: 'rgba(16, 185, 129, 0.4)' },
    { id: 'diff-inspector', label: 'Diff Inspector', icon: FileCode, color: '#38bdf8', glow: 'rgba(56, 189, 248, 0.4)' },
    { id: 'branch-network', label: 'Branch Network', icon: GitBranch, color: '#a855f7', glow: 'rgba(168, 85, 247, 0.4)' },
    { id: 'rebase-replay', label: 'Rebase & Cherry-Pick', icon: RefreshCw, color: '#ec4899', glow: 'rgba(236, 72, 153, 0.4)' },
    { id: 'stash-stack', label: 'Stash Stack', icon: Archive, color: '#eab308', glow: 'rgba(234, 179, 8, 0.4)' },
    { id: 'remote-sync', label: 'Remote Sync', icon: UploadCloud, color: '#8b5cf6', glow: 'rgba(139, 92, 246, 0.4)' },
    { id: 'reset-rollback', label: 'Reset Matrix', icon: RotateCcw, color: '#f43f5e', glow: 'rgba(244, 63, 94, 0.4)' }
  ];

  return (
    <div className="animate-fade-in" style={{ paddingBottom: 40, width: '100%', maxWidth: '100%', minWidth: 0, boxSizing: 'border-box' }}>
      
      {/* Top Header */}
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', flexWrap: 'wrap', gap: 12, marginBottom: 16, width: '100%', minWidth: 0 }}>
        <div style={{ minWidth: 0, flex: 1 }}>
          <div style={{ display: 'flex', alignItems: 'center', gap: 8, marginBottom: 6, flexWrap: 'wrap' }}>
            <Badge variant="yellow"><GitBranch size={14} /> Git & GitHub Command Suite</Badge>
            <span style={{ fontSize: '0.85rem', color: '#94a3b8', fontWeight: 600 }}>Interactive Visual Simulator</span>
          </div>
          <h1 style={{ fontSize: '1.75rem', fontWeight: 800, color: '#ffffff', letterSpacing: '-0.02em' }}>Complete Git & GitHub Simulator</h1>
          <p style={{ color: '#cbd5e1', fontSize: '0.92rem', marginTop: 4 }}>
            Execute any command in the shell emulator to trigger live, reactive visual animations in real time.
          </p>
        </div>
      </div>

      {/* Primary Navigation Tabs */}
      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(135px, 1fr))', gap: 6, marginBottom: 16, width: '100%', minWidth: 0 }}>
        {[
          { id: 'all-terminal', title: '💻 Interactive Terminal', level: 'Every Command', color: '#38bdf8' },
          { id: 'snapshots', title: '📄 3-Trees & Staging', level: 'add / commit / diff', color: '#10b981' },
          { id: 'branching', title: '🌿 Branching & Merges', level: 'branch / switch / merge', color: '#f59e0b' },
          { id: 'undo-rebase', title: '⚡ Rebase & Stash', level: 'rebase / reset / cherry-pick', color: '#ec4899' },
          { id: 'remotes-sync', title: '☁️ Remote Sync', level: 'fetch / pull / push', color: '#8b5cf6' },
          { id: 'github-pr', title: '🔀 Pull Requests', level: 'PRs & Code Review', color: '#6366f1' },
          { id: 'github-actions', title: '🚀 GitHub Actions', level: 'CI/CD Matrix', color: '#06b6d4' }
        ].map((tab) => {
          const isActive = activeTab === tab.id;
          return (
            <button
              key={tab.id}
              onClick={() => setActiveTab(tab.id)}
              style={{
                background: isActive ? '#1e293b' : '#0b1120',
                border: isActive ? `2px solid ${tab.color}` : '1px solid #1e293b',
                padding: '9px 12px',
                borderRadius: '8px',
                textAlign: 'left',
                cursor: 'pointer',
                transition: 'all 0.15s ease',
                boxShadow: isActive ? `0 0 12px ${tab.color}33` : 'none',
                minWidth: 0
              }}
            >
              <div style={{ fontSize: '0.65rem', fontWeight: 800, color: tab.color, textTransform: 'uppercase', letterSpacing: '0.04em' }}>{tab.level}</div>
              <div style={{ fontSize: '0.78rem', fontWeight: 700, color: '#f8fafc', marginTop: 2, whiteSpace: 'nowrap', overflow: 'hidden', textOverflow: 'ellipsis' }}>{tab.title}</div>
            </button>
          );
        })}
      </div>

      {/* Quick Interactive Command Dispatcher Bar (Dark High-Contrast Card) */}
      <div style={{ padding: '12px 16px', marginBottom: 16, background: '#0b1120', border: '1px solid #1e293b', borderRadius: '10px', width: '100%', minWidth: 0, boxSizing: 'border-box' }}>
        <div style={{ fontSize: '0.78rem', fontWeight: 700, color: '#94a3b8', marginBottom: 8, display: 'flex', alignItems: 'center', gap: 6 }}>
          <Sparkles size={14} color="#38bdf8" /> Click any command pill to execute instantly:
        </div>
        <div style={{ display: 'flex', gap: 6, flexWrap: 'wrap', width: '100%' }}>
          {COMMAND_PRESETS.map((item, idx) => (
            <button
              key={idx}
              onClick={() => executeGitCommand(item.cmd)}
              style={{
                fontFamily: 'JetBrains Mono, Fira Code, Consolas, monospace',
                fontSize: '0.75rem',
                fontWeight: 600,
                background: '#131d31',
                border: '1px solid #0284c7',
                padding: '4px 10px',
                borderRadius: '6px',
                color: '#38bdf8',
                cursor: 'pointer',
                transition: 'all 0.15s ease'
              }}
              onMouseEnter={(e) => {
                e.currentTarget.style.background = '#0284c7';
                e.currentTarget.style.color = '#ffffff';
              }}
              onMouseLeave={(e) => {
                e.currentTarget.style.background = '#131d31';
                e.currentTarget.style.color = '#38bdf8';
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
          
          {/* REACTIVE SIMULATION STAGE CONTAINER */}
          <div style={{ padding: '18px 20px', background: '#070b14', border: '1px solid #1e293b', borderRadius: '12px', width: '100%', minWidth: 0, boxSizing: 'border-box', boxShadow: '0 8px 30px rgba(0,0,0,0.6)' }}>
            
            {/* Stage Info Header */}
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', flexWrap: 'wrap', gap: 10, marginBottom: 12, width: '100%' }}>
              <div style={{ display: 'flex', alignItems: 'center', gap: 10, flexWrap: 'wrap' }}>
                <div style={{ padding: '6px 12px', borderRadius: '8px', background: 'rgba(56, 189, 248, 0.15)', border: '1px solid #38bdf8', display: 'flex', alignItems: 'center', gap: 6 }}>
                  <Sparkles size={15} color="#38bdf8" />
                  <span style={{ fontSize: '0.85rem', fontWeight: 800, color: '#f8fafc' }}>
                    Live Stage:
                  </span>
                  <span style={{ fontSize: '0.85rem', fontWeight: 800, color: SIMULATION_VIEWS.find(v => v.id === activeSimView)?.color || '#38bdf8' }}>
                    {SIMULATION_VIEWS.find(v => v.id === activeSimView)?.label}
                  </span>
                </div>

                <div style={{ background: '#1e293b', border: '1px solid #334155', padding: '5px 12px', borderRadius: '8px', fontSize: '0.8rem', color: '#f8fafc', fontWeight: 600 }}>
                  Active Branch: <strong style={{ color: '#38bdf8', fontWeight: 800 }}>{currentBranch}</strong>
                </div>
              </div>
            </div>

            {/* Simulation View Switcher Pills (Crisp High-Contrast Buttons) */}
            <div style={{ display: 'flex', gap: 6, flexWrap: 'wrap', marginBottom: 14, width: '100%' }}>
              {SIMULATION_VIEWS.map(v => {
                const isCurrent = activeSimView === v.id;
                const Icon = v.icon;
                return (
                  <button
                    key={v.id}
                    onClick={() => setActiveSimView(v.id)}
                    style={{
                      padding: '6px 12px',
                      borderRadius: '7px',
                      fontSize: '0.75rem',
                      fontWeight: 700,
                      display: 'flex',
                      alignItems: 'center',
                      gap: 6,
                      background: isCurrent ? v.color : '#131d31',
                      color: isCurrent ? '#050811' : '#e2e8f0',
                      border: isCurrent ? `1px solid ${v.color}` : '1px solid #334155',
                      boxShadow: isCurrent ? `0 0 14px ${v.glow}` : 'none',
                      cursor: 'pointer',
                      transition: 'all 0.15s ease'
                    }}
                  >
                    <Icon size={13} color={isCurrent ? '#050811' : v.color} />
                    {v.label}
                  </button>
                );
              })}
            </div>

            {/* Dynamic Status Alert Message Banner (High Contrast) */}
            <div style={{ padding: '10px 14px', borderRadius: '8px', background: '#0f1d36', border: '1px solid #1e3a5f', marginBottom: 16, display: 'flex', alignItems: 'center', gap: 8, fontSize: '0.82rem', color: '#f8fafc', wordBreak: 'break-word' }}>
              <span style={{ color: '#38bdf8', fontWeight: 800, whiteSpace: 'nowrap' }}>⚡ Last Action:</span>
              <span style={{ flex: 1, minWidth: 0, fontWeight: 600 }}>{simAlertMsg}</span>
            </div>

            {/* VIEW 1: DAG COMMIT GRAPH CANVAS */}
            {activeSimView === 'dag' && (
              <div style={{ width: '100%', minWidth: 0, overflow: 'hidden' }}>
                <div style={{ display: 'flex', alignItems: 'center', gap: 14, overflowX: 'auto', padding: '14px 6px', minHeight: '135px', width: '100%', boxSizing: 'border-box' }}>
                  {commits.map((c, idx) => {
                    const isHead = c.branch === currentBranch && idx === commits.map(x => x.branch).lastIndexOf(currentBranch);
                    const hasTag = tags.find(t => t.commitHash === c.hash);
                    return (
                      <div key={c.id} style={{ display: 'flex', alignItems: 'center', gap: 12, flexShrink: 0 }}>
                        <div
                          style={{
                            background: c.branch === 'main' ? '#131d31' : '#1e1b4b',
                            border: isHead ? '2px solid #38bdf8' : `1px solid ${c.branch === 'main' ? '#334155' : '#6366f1'}`,
                            padding: '12px 16px',
                            borderRadius: '10px',
                            minWidth: '160px',
                            maxWidth: '220px',
                            boxShadow: isHead ? '0 0 18px rgba(56, 189, 248, 0.45)' : 'none',
                            position: 'relative'
                          }}
                        >
                          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: 4 }}>
                            <span style={{ fontFamily: 'monospace', fontSize: '0.82rem', color: '#fbbf24', fontWeight: 800 }}>{c.hash}</span>
                            <span style={{ fontSize: '0.68rem', padding: '2px 7px', borderRadius: '4px', background: c.branch === 'main' ? '#0f172a' : '#4338ca', color: '#f8fafc', fontWeight: 700 }}>{c.branch}</span>
                          </div>
                          <div style={{ fontSize: '0.85rem', fontWeight: 700, color: '#ffffff', whiteSpace: 'nowrap', overflow: 'hidden', textOverflow: 'ellipsis' }}>{c.message}</div>
                          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginTop: 6, fontSize: '0.72rem', color: '#94a3b8' }}>
                            <span>{c.author}</span>
                            {isHead && <span style={{ color: '#38bdf8', fontWeight: 800 }}>HEAD ➔</span>}
                          </div>
                          {hasTag && (
                            <div style={{ position: 'absolute', top: -10, right: 10, background: '#f59e0b', color: '#090d16', fontSize: '0.65rem', fontWeight: 900, padding: '2px 7px', borderRadius: '4px', boxShadow: '0 2px 6px rgba(0,0,0,0.4)' }}>
                              🏷️ {hasTag.name}
                            </div>
                          )}
                        </div>
                        {idx < commits.length - 1 && <div style={{ color: '#38bdf8', fontSize: '1.4rem', fontWeight: 800, flexShrink: 0 }}>➔</div>}
                      </div>
                    );
                  })}
                </div>
              </div>
            )}

            {/* VIEW 2: 3-TREES STAGING INSPECTOR */}
            {activeSimView === 'staging-trees' && (
              <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(210px, 1fr))', gap: 14, width: '100%', minWidth: 0 }}>
                {/* 1. Working Directory */}
                <div style={{ background: '#131d31', padding: 14, borderRadius: '10px', border: '1px solid #f43f5e', minWidth: 0 }}>
                  <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: 10 }}>
                    <span style={{ fontWeight: 800, fontSize: '0.85rem', color: '#fb7185', display: 'flex', alignItems: 'center', gap: 5 }}>
                      <FileCode size={15} /> 1. Working Directory
                    </span>
                    <button onClick={() => executeGitCommand('git add .')} style={{ background: '#f43f5e', color: '#ffffff', border: 'none', padding: '3px 8px', borderRadius: '5px', fontWeight: 700, fontSize: '0.72rem', cursor: 'pointer' }}>
                      + git add .
                    </button>
                  </div>
                  <div style={{ display: 'flex', flexDirection: 'column', gap: 6 }}>
                    {workingFiles.map((f, idx) => (
                      <div key={idx} style={{ padding: '8px 10px', background: '#0b1120', borderRadius: '6px', fontSize: '0.78rem', display: 'flex', justifyContent: 'space-between', alignItems: 'center', border: '1px solid #1e293b' }}>
                        <span style={{ overflow: 'hidden', textOverflow: 'ellipsis', whiteSpace: 'nowrap', color: '#f8fafc', fontWeight: 600 }}>📄 {f.name}</span>
                        <span style={{ color: f.status === 'clean' ? '#34d399' : '#fb7185', fontWeight: 800, fontSize: '0.72rem', marginLeft: 6, textTransform: 'uppercase' }}>{f.status}</span>
                      </div>
                    ))}
                  </div>
                </div>

                {/* 2. Staging Index */}
                <div style={{ background: '#131d31', padding: 14, borderRadius: '10px', border: '1px solid #10b981', minWidth: 0 }}>
                  <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: 10 }}>
                    <span style={{ fontWeight: 800, fontSize: '0.85rem', color: '#34d399', display: 'flex', alignItems: 'center', gap: 5 }}>
                      <Layers size={15} /> 2. Staging Index
                    </span>
                    <button onClick={() => executeGitCommand('git reset')} disabled={stagedFiles.length === 0} style={{ background: '#1e293b', color: '#e2e8f0', border: '1px solid #475569', padding: '3px 8px', borderRadius: '5px', fontWeight: 700, fontSize: '0.72rem', cursor: 'pointer', opacity: stagedFiles.length === 0 ? 0.5 : 1 }}>
                      git reset
                    </button>
                  </div>
                  <div style={{ display: 'flex', flexDirection: 'column', gap: 6 }}>
                    {stagedFiles.map((f, idx) => (
                      <div key={idx} style={{ padding: '8px 10px', background: '#0b1120', borderRadius: '6px', fontSize: '0.78rem', display: 'flex', justifyContent: 'space-between', alignItems: 'center', border: '1px solid #1e293b' }}>
                        <span style={{ overflow: 'hidden', textOverflow: 'ellipsis', whiteSpace: 'nowrap', color: '#f8fafc', fontWeight: 600 }}>✓ {f.name}</span>
                        <span style={{ color: '#34d399', fontWeight: 800, fontSize: '0.72rem' }}>STAGED</span>
                      </div>
                    ))}
                    {stagedFiles.length === 0 && <span style={{ fontSize: '0.78rem', color: '#94a3b8', fontStyle: 'italic', padding: '8px 0' }}>No staged snapshots</span>}
                  </div>
                </div>

                {/* 3. HEAD Commit */}
                <div style={{ background: '#131d31', padding: 14, borderRadius: '10px', border: '1px solid #38bdf8', minWidth: 0 }}>
                  <div style={{ fontWeight: 800, fontSize: '0.85rem', color: '#38bdf8', marginBottom: 10, display: 'flex', alignItems: 'center', gap: 5 }}>
                    <GitCommit size={15} /> 3. Repository (HEAD)
                  </div>
                  <div style={{ padding: '12px', background: '#0b1120', borderRadius: '8px', border: '1px solid #1e293b' }}>
                    <div style={{ fontSize: '0.8rem', color: '#fbbf24', fontWeight: 800 }}>Commit: {commits[commits.length - 1]?.hash}</div>
                    <div style={{ fontSize: '0.85rem', color: '#ffffff', fontWeight: 700, marginTop: 4 }}>{commits[commits.length - 1]?.message}</div>
                    <div style={{ fontSize: '0.75rem', color: '#94a3b8', marginTop: 4 }}>Branch: {commits[commits.length - 1]?.branch}</div>
                  </div>
                </div>
              </div>
            )}

            {/* VIEW 3: DIFF INSPECTOR */}
            {activeSimView === 'diff-inspector' && (
              <div style={{ background: '#0b1120', padding: 16, borderRadius: '10px', border: '1px solid #334155', width: '100%', minWidth: 0, boxSizing: 'border-box' }}>
                <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: 10, flexWrap: 'wrap', gap: 6 }}>
                  <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                    <FileText size={16} color="#38bdf8" />
                    <span style={{ fontFamily: 'monospace', fontSize: '0.85rem', fontWeight: 800, color: '#ffffff' }}>
                      diff --git a/{selectedDiffFile} b/{selectedDiffFile}
                    </span>
                  </div>
                  <span style={{ fontSize: '0.75rem', color: '#34d399', fontWeight: 800, background: 'rgba(52, 211, 153, 0.15)', padding: '2px 8px', borderRadius: '4px' }}>+14 lines</span>
                </div>

                <div style={{ fontFamily: 'JetBrains Mono, Fira Code, Consolas, monospace', fontSize: '0.82rem', background: '#050811', padding: 14, borderRadius: '8px', lineHeight: 1.6, overflowX: 'auto', width: '100%', boxSizing: 'border-box', border: '1px solid #1e293b' }}>
                  <div style={{ color: '#94a3b8' }}>--- a/src/auth/jwt.py (Index)</div>
                  <div style={{ color: '#94a3b8' }}>+++ b/src/auth/jwt.py (Working Tree)</div>
                  <div style={{ color: '#64748b' }}>@@ -12,8 +12,12 @@ def generate_session_token(user_id: str):</div>
                  <div style={{ color: '#e2e8f0' }}>     payload = {`{"sub": user_id}`}</div>
                  <div style={{ background: 'rgba(244, 63, 94, 0.25)', color: '#fca5a5', padding: '3px 6px', borderRadius: '4px', borderLeft: '3px solid #f43f5e', fontWeight: 600 }}>
                    -    return jwt.encode(payload, SECRET_KEY, algorithm="HS256")
                  </div>
                  <div style={{ background: 'rgba(16, 185, 129, 0.25)', color: '#6ee7b7', padding: '3px 6px', borderRadius: '4px', borderLeft: '3px solid #10b981', fontWeight: 600 }}>
                    +    expire = datetime.utcnow() + timedelta(minutes=60)
                  </div>
                  <div style={{ background: 'rgba(16, 185, 129, 0.25)', color: '#6ee7b7', padding: '3px 6px', borderRadius: '4px', borderLeft: '3px solid #10b981', fontWeight: 600 }}>
                    +    payload.update({`{"exp": expire, "role": "admin"}`})
                  </div>
                  <div style={{ background: 'rgba(16, 185, 129, 0.25)', color: '#6ee7b7', padding: '3px 6px', borderRadius: '4px', borderLeft: '3px solid #10b981', fontWeight: 600 }}>
                    +    return jwt.encode(payload, RSA_PRIVATE_KEY, algorithm="RS256")
                  </div>
                </div>
              </div>
            )}

            {/* VIEW 4: BRANCH NETWORK (High Visibility Redesign) */}
            {activeSimView === 'branch-network' && (
              <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(240px, 1fr))', gap: 14, width: '100%', minWidth: 0 }}>
                
                {/* Active Branch Pointers List */}
                <div style={{ background: '#131d31', padding: 16, borderRadius: '10px', border: '1px solid #334155', minWidth: 0 }}>
                  <div style={{ fontWeight: 800, fontSize: '0.88rem', color: '#c084fc', marginBottom: 12, display: 'flex', alignItems: 'center', gap: 6 }}>
                    <GitBranch size={16} /> Active Branch Pointers:
                  </div>
                  <div style={{ display: 'flex', flexDirection: 'column', gap: 8 }}>
                    {branches.map((b, idx) => {
                      const isCurrent = b === currentBranch;
                      return (
                        <div
                          key={idx}
                          style={{
                            padding: '10px 14px',
                            background: isCurrent ? '#1e293b' : '#0b1120',
                            borderRadius: '8px',
                            fontSize: '0.85rem',
                            display: 'flex',
                            justifyContent: 'space-between',
                            alignItems: 'center',
                            border: isCurrent ? '2px solid #38bdf8' : '1px solid #334155',
                            boxShadow: isCurrent ? '0 0 14px rgba(56, 189, 248, 0.25)' : 'none'
                          }}
                        >
                          <span style={{ color: isCurrent ? '#38bdf8' : '#ffffff', fontWeight: isCurrent ? 800 : 600, display: 'flex', alignItems: 'center', gap: 6 }}>
                            {isCurrent ? '● (HEAD)' : '○'} {b}
                          </span>
                          {!isCurrent && (
                            <button
                              onClick={() => executeGitCommand(`git checkout ${b}`)}
                              style={{
                                background: '#1e293b',
                                color: '#38bdf8',
                                border: '1px solid #0284c7',
                                padding: '4px 10px',
                                borderRadius: '5px',
                                fontSize: '0.75rem',
                                fontWeight: 700,
                                cursor: 'pointer',
                                transition: 'all 0.15s ease'
                              }}
                              onMouseEnter={(e) => {
                                e.currentTarget.style.background = '#0284c7';
                                e.currentTarget.style.color = '#ffffff';
                              }}
                              onMouseLeave={(e) => {
                                e.currentTarget.style.background = '#1e293b';
                                e.currentTarget.style.color = '#38bdf8';
                              }}
                            >
                              checkout
                            </button>
                          )}
                        </div>
                      );
                    })}
                  </div>
                </div>

                {/* Fast Branch Actions */}
                <div style={{ background: '#131d31', padding: 16, borderRadius: '10px', border: '1px solid #334155', minWidth: 0 }}>
                  <div style={{ fontWeight: 800, fontSize: '0.88rem', color: '#38bdf8', marginBottom: 12 }}>
                    Fast Branch Actions:
                  </div>
                  <div style={{ display: 'flex', flexDirection: 'column', gap: 8 }}>
                    <button
                      onClick={() => executeGitCommand('git checkout -b feature/analytics')}
                      style={{
                        background: 'linear-gradient(135deg, #6366f1, #4f46e5)',
                        color: '#ffffff',
                        border: 'none',
                        padding: '10px 14px',
                        borderRadius: '8px',
                        fontSize: '0.82rem',
                        fontWeight: 700,
                        cursor: 'pointer',
                        boxShadow: '0 4px 12px rgba(99, 102, 241, 0.35)'
                      }}
                    >
                      + Branch 'feature/analytics'
                    </button>
                    
                    <button
                      onClick={() => executeGitCommand('git merge main')}
                      style={{
                        background: 'linear-gradient(135deg, #10b981, #059669)',
                        color: '#ffffff',
                        border: 'none',
                        padding: '10px 14px',
                        borderRadius: '8px',
                        fontSize: '0.82rem',
                        fontWeight: 700,
                        cursor: 'pointer',
                        boxShadow: '0 4px 12px rgba(16, 185, 129, 0.35)'
                      }}
                    >
                      🔀 Merge 'main' into '{currentBranch}'
                    </button>
                    
                    <button
                      onClick={() => executeGitCommand('git switch main')}
                      style={{
                        background: '#1e293b',
                        color: '#fbbf24',
                        border: '1px solid #d97706',
                        padding: '10px 14px',
                        borderRadius: '8px',
                        fontSize: '0.82rem',
                        fontWeight: 700,
                        cursor: 'pointer'
                      }}
                    >
                      👉 Switch to 'main'
                    </button>
                  </div>
                </div>
              </div>
            )}

            {/* VIEW 5: REBASE & CHERRY-PICK REPLAY */}
            {activeSimView === 'rebase-replay' && (
              <div style={{ background: '#0b1120', padding: 16, borderRadius: '10px', border: '1px solid #ec4899', width: '100%', minWidth: 0, boxSizing: 'border-box' }}>
                <div style={{ fontWeight: 800, fontSize: '0.88rem', color: '#f472b6', marginBottom: 8, display: 'flex', alignItems: 'center', gap: 6 }}>
                  <RefreshCw size={16} /> Linear Commit Replay vs Merge Commit:
                </div>
                <p style={{ fontSize: '0.82rem', color: '#cbd5e1', marginBottom: 12 }}>
                  `git rebase` rewinds current branch commits, fast-forwards to base `main`, and reapplies commits sequentially without creating merge clutter.
                </p>
                <div style={{ display: 'flex', gap: 10, flexWrap: 'wrap' }}>
                  <button onClick={() => executeGitCommand('git rebase main')} style={{ background: '#1e293b', border: '1px solid #ec4899', color: '#f472b6', padding: '8px 14px', borderRadius: '6px', fontWeight: 700, fontSize: '0.8rem', cursor: 'pointer' }}>
                    ⚡ git rebase main
                  </button>
                  <button onClick={() => executeGitCommand('git cherry-pick 3c19e4')} style={{ background: '#1e293b', border: '1px solid #38bdf8', color: '#38bdf8', padding: '8px 14px', borderRadius: '6px', fontWeight: 700, fontSize: '0.8rem', cursor: 'pointer' }}>
                    🍒 git cherry-pick 3c19e4
                  </button>
                </div>
              </div>
            )}

            {/* VIEW 6: LIFO STASH STACK */}
            {activeSimView === 'stash-stack' && (
              <div style={{ background: '#0b1120', padding: 16, borderRadius: '10px', border: '1px solid #eab308', width: '100%', minWidth: 0, boxSizing: 'border-box' }}>
                <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: 10, flexWrap: 'wrap', gap: 6 }}>
                  <span style={{ fontWeight: 800, fontSize: '0.88rem', color: '#fde047', display: 'flex', alignItems: 'center', gap: 6 }}>
                    <Archive size={16} /> LIFO Stash Stack ({stashStack.length} items)
                  </span>
                  <div style={{ display: 'flex', gap: 8 }}>
                    <button onClick={() => executeGitCommand('git stash')} style={{ background: '#eab308', color: '#090d16', border: 'none', padding: '5px 12px', borderRadius: '6px', fontWeight: 800, fontSize: '0.75rem', cursor: 'pointer' }}>git stash</button>
                    <button onClick={() => executeGitCommand('git stash pop')} style={{ background: '#1e293b', color: '#fde047', border: '1px solid #eab308', padding: '5px 12px', borderRadius: '6px', fontWeight: 800, fontSize: '0.75rem', cursor: 'pointer' }}>git stash pop</button>
                  </div>
                </div>

                <div style={{ display: 'flex', flexDirection: 'column', gap: 6 }}>
                  {stashStack.map((s, idx) => (
                    <div key={idx} style={{ padding: '10px 14px', background: '#131d31', borderRadius: '6px', fontSize: '0.82rem', display: 'flex', justifyContent: 'space-between', border: '1px solid #334155' }}>
                      <span style={{ fontFamily: 'monospace', color: '#fde047', fontWeight: 700 }}>{s.id}: WIP on {s.branch}</span>
                      <span style={{ color: '#94a3b8', fontSize: '0.75rem' }}>{s.items?.length || 1} file(s)</span>
                    </div>
                  ))}
                  {stashStack.length === 0 && (
                    <div style={{ color: '#94a3b8', fontSize: '0.8rem', fontStyle: 'italic', padding: 6 }}>
                      No stashed snapshots. Run 'git stash' to store temporary uncommitted state.
                    </div>
                  )}
                </div>
              </div>
            )}

            {/* VIEW 7: REMOTE SYNC & FETCH */}
            {activeSimView === 'remote-sync' && (
              <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(200px, 1fr))', gap: 12, alignItems: 'center', width: '100%', minWidth: 0 }}>
                <div style={{ background: '#131d31', padding: 14, borderRadius: '10px', border: '1px solid #10b981', minWidth: 0 }}>
                  <div style={{ fontWeight: 800, fontSize: '0.85rem', color: '#34d399', marginBottom: 4 }}>💻 Local Repository</div>
                  <div style={{ fontSize: '0.78rem', color: '#e2e8f0' }}>Branch: <strong style={{ color: '#38bdf8' }}>{currentBranch}</strong></div>
                  <div style={{ fontSize: '0.78rem', color: '#34d399', fontWeight: 800, marginTop: 4 }}>{commits.length} Local Commits</div>
                </div>

                <div style={{ display: 'flex', flexDirection: 'column', gap: 6, alignItems: 'stretch', minWidth: 0 }}>
                  <button onClick={() => executeGitCommand('git fetch origin')} style={{ background: '#1e293b', border: '1px solid #38bdf8', color: '#38bdf8', padding: '6px', borderRadius: '6px', fontWeight: 700, fontSize: '0.75rem', cursor: 'pointer' }}>
                    Fetch ⬇️
                  </button>
                  <button onClick={() => executeGitCommand('git pull origin main')} style={{ background: '#1e293b', border: '1px solid #10b981', color: '#34d399', padding: '6px', borderRadius: '6px', fontWeight: 700, fontSize: '0.75rem', cursor: 'pointer' }}>
                    Pull 🔄
                  </button>
                  <button onClick={() => executeGitCommand('git push origin main')} style={{ background: '#10b981', color: '#090d16', border: 'none', padding: '6px', borderRadius: '6px', fontWeight: 800, fontSize: '0.75rem', cursor: 'pointer' }}>
                    Push ⬆️
                  </button>
                </div>

                <div style={{ background: '#131d31', padding: 14, borderRadius: '10px', border: '1px solid #8b5cf6', minWidth: 0 }}>
                  <div style={{ fontWeight: 800, fontSize: '0.85rem', color: '#a78bfa', marginBottom: 4 }}>☁️ GitHub Remote (origin)</div>
                  <div style={{ fontSize: '0.72rem', color: '#e2e8f0', wordBreak: 'break-all' }}>{remoteOriginUrl}</div>
                  <div style={{ fontSize: '0.78rem', color: '#a78bfa', fontWeight: 800, marginTop: 4 }}>{remoteCommitsCount} Remote Commits</div>
                </div>
              </div>
            )}

            {/* VIEW 8: RESET & ROLLBACK MATRIX */}
            {activeSimView === 'reset-rollback' && (
              <div style={{ background: '#0b1120', padding: 16, borderRadius: '10px', border: '1px solid #f43f5e', width: '100%', minWidth: 0, boxSizing: 'border-box' }}>
                <div style={{ fontWeight: 800, fontSize: '0.88rem', color: '#fb7185', marginBottom: 10, display: 'flex', alignItems: 'center', gap: 6 }}>
                  <RotateCcw size={16} /> Git Reset Comparison Matrix:
                </div>
                <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(150px, 1fr))', gap: 10, width: '100%', minWidth: 0 }}>
                  <div style={{ background: '#131d31', padding: 10, borderRadius: '8px', border: '1px solid #38bdf8', minWidth: 0 }}>
                    <div style={{ fontWeight: 800, fontSize: '0.78rem', color: '#38bdf8' }}>--soft HEAD~1</div>
                    <div style={{ fontSize: '0.72rem', color: '#cbd5e1', marginTop: 3 }}>Preserves Index.</div>
                    <button onClick={() => executeGitCommand('git reset --soft HEAD~1')} style={{ marginTop: 6, fontSize: '0.7rem', padding: '3px 6px', background: '#1e293b', color: '#38bdf8', border: '1px solid #0284c7', borderRadius: '4px', cursor: 'pointer', fontWeight: 700 }}>Soft Reset</button>
                  </div>
                  <div style={{ background: '#131d31', padding: 10, borderRadius: '8px', border: '1px solid #f59e0b', minWidth: 0 }}>
                    <div style={{ fontWeight: 800, fontSize: '0.78rem', color: '#fbbf24' }}>--mixed (default)</div>
                    <div style={{ fontSize: '0.72rem', color: '#cbd5e1', marginTop: 3 }}>Unstages Index.</div>
                    <button onClick={() => executeGitCommand('git reset')} style={{ marginTop: 6, fontSize: '0.7rem', padding: '3px 6px', background: '#1e293b', color: '#fbbf24', border: '1px solid #d97706', borderRadius: '4px', cursor: 'pointer', fontWeight: 700 }}>Mixed Reset</button>
                  </div>
                  <div style={{ background: '#131d31', padding: 10, borderRadius: '8px', border: '1px solid #f43f5e', minWidth: 0 }}>
                    <div style={{ fontWeight: 800, fontSize: '0.78rem', color: '#fb7185' }}>--hard HEAD~1</div>
                    <div style={{ fontSize: '0.72rem', color: '#cbd5e1', marginTop: 3 }}>Wipes uncommitted work.</div>
                    <button onClick={() => executeGitCommand('git reset --hard HEAD~1')} style={{ marginTop: 6, fontSize: '0.7rem', padding: '3px 6px', background: '#f43f5e', color: '#ffffff', border: 'none', borderRadius: '4px', cursor: 'pointer', fontWeight: 700 }}>Hard Reset</button>
                  </div>
                  <div style={{ background: '#131d31', padding: 10, borderRadius: '8px', border: '1px solid #10b981', minWidth: 0 }}>
                    <div style={{ fontWeight: 800, fontSize: '0.78rem', color: '#34d399' }}>git revert</div>
                    <div style={{ fontSize: '0.72rem', color: '#cbd5e1', marginTop: 3 }}>Safe forward patch.</div>
                    <button onClick={() => executeGitCommand('git revert 9a01f8')} style={{ marginTop: 6, fontSize: '0.7rem', padding: '3px 6px', background: '#10b981', color: '#090d16', border: 'none', borderRadius: '4px', cursor: 'pointer', fontWeight: 800 }}>Revert</button>
                  </div>
                </div>
              </div>
            )}
          </div>

          {/* Terminal Console (Crystal-Clear High-Contrast Terminal) */}
          <div style={{ padding: 0, overflow: 'hidden', background: '#050811', border: '1px solid #1e293b', borderRadius: '12px', width: '100%', minWidth: 0, boxSizing: 'border-box', boxShadow: '0 8px 30px rgba(0,0,0,0.6)' }}>
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', padding: '10px 16px', background: '#0b1120', borderBottom: '1px solid #1e293b' }}>
              <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                <Terminal size={15} color="#38bdf8" />
                <span style={{ fontSize: '0.82rem', fontWeight: 700, color: '#f8fafc' }}>Git Shell Emulator (Dynamic Live Simulation Sync)</span>
              </div>
              <button onClick={() => setTerminalHistory([])} style={{ background: '#1e293b', color: '#94a3b8', border: '1px solid #334155', padding: '3px 8px', borderRadius: '5px', fontSize: '0.72rem', cursor: 'pointer', fontWeight: 600 }}>
                Clear Output
              </button>
            </div>

            <div style={{ padding: '14px 16px', minHeight: '180px', maxHeight: '240px', overflowY: 'auto', fontFamily: 'JetBrains Mono, Fira Code, Consolas, monospace', fontSize: '0.82rem', lineHeight: 1.6, width: '100%', boxSizing: 'border-box', wordBreak: 'break-all' }}>
              {terminalHistory.map((line, idx) => (
                <div key={idx} style={{ color: line.startsWith('$') ? '#38bdf8' : line.startsWith('fatal') || line.startsWith('error') ? '#fb7185' : '#f1f5f9', fontWeight: line.startsWith('$') ? 700 : 400 }}>
                  {line}
                </div>
              ))}
            </div>

            <form onSubmit={(e) => { e.preventDefault(); executeGitCommand(commandInput); }} style={{ display: 'flex', borderTop: '1px solid #1e293b', background: '#0b1120', width: '100%', minWidth: 0 }}>
              <span style={{ padding: '10px 0 10px 16px', color: '#10b981', fontFamily: 'monospace', fontWeight: 800, fontSize: '0.85rem', whiteSpace: 'nowrap' }}>(repo) $</span>
              <input
                type="text"
                value={commandInput}
                onChange={(e) => handleInputChange(e.target.value)}
                placeholder="Type git commands here (e.g. git status, git commit -m 'feat', git diff, git branch, git stash, git push)..."
                style={{ flex: 1, minWidth: 0, width: '100%', background: 'transparent', border: 'none', padding: '10px 14px', color: '#ffffff', fontFamily: 'JetBrains Mono, monospace', fontSize: '0.85rem', outline: 'none', fontWeight: 600 }}
              />
            </form>
          </div>
        </div>
      )}

      {/* TAB 2: 3-TREES & DIFF STAGING */}
      {activeTab === 'snapshots' && (
        <div style={{ display: 'grid', gap: 16, width: '100%', minWidth: 0 }}>
          <div style={{ padding: 18, background: '#070b14', border: '1px solid #1e293b', borderRadius: '12px', width: '100%', minWidth: 0, boxSizing: 'border-box' }}>
            <h3 style={{ fontSize: '1.05rem', fontWeight: 800, color: '#ffffff', marginBottom: 14, display: 'flex', alignItems: 'center', gap: 6 }}>
              <Layers size={17} color="#10b981" /> Git 3-Trees Workflow (`git status`, `git add`, `git diff`)
            </h3>

            <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(220px, 1fr))', gap: 14, width: '100%', minWidth: 0 }}>
              {/* Working Tree */}
              <div style={{ background: '#131d31', padding: 14, borderRadius: '10px', border: '1px solid #f43f5e', minWidth: 0 }}>
                <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: 10 }}>
                  <span style={{ fontWeight: 800, fontSize: '0.85rem', color: '#fb7185' }}>1. Working Directory</span>
                  <button onClick={() => executeGitCommand('git add .')} style={{ background: '#f43f5e', color: '#ffffff', border: 'none', padding: '3px 8px', borderRadius: '5px', fontWeight: 700, fontSize: '0.72rem', cursor: 'pointer' }}>
                    + Stage All (git add .)
                  </button>
                </div>
                <div style={{ display: 'flex', flexDirection: 'column', gap: 6 }}>
                  {workingFiles.map((f, idx) => (
                    <div key={idx} style={{ padding: '8px 10px', background: '#0b1120', borderRadius: '6px', fontSize: '0.78rem', display: 'flex', justifyContent: 'space-between', border: '1px solid #1e293b' }}>
                      <span style={{ overflow: 'hidden', textOverflow: 'ellipsis', whiteSpace: 'nowrap', color: '#f8fafc', fontWeight: 600 }}>📄 {f.name}</span>
                      <span style={{ color: f.status === 'clean' ? '#34d399' : '#fb7185', fontWeight: 800 }}>{f.status}</span>
                    </div>
                  ))}
                </div>
              </div>

              {/* Staging Area */}
              <div style={{ background: '#131d31', padding: 14, borderRadius: '10px', border: '1px solid #10b981', minWidth: 0 }}>
                <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: 10 }}>
                  <span style={{ fontWeight: 800, fontSize: '0.85rem', color: '#34d399' }}>2. Staging Index (Cache)</span>
                  <button onClick={() => executeGitCommand('git reset')} disabled={stagedFiles.length === 0} style={{ background: '#1e293b', color: '#e2e8f0', border: '1px solid #475569', padding: '3px 8px', borderRadius: '5px', fontWeight: 700, fontSize: '0.72rem', cursor: 'pointer', opacity: stagedFiles.length === 0 ? 0.5 : 1 }}>
                    Unstage (git reset)
                  </button>
                </div>
                <div style={{ display: 'flex', flexDirection: 'column', gap: 6 }}>
                  {stagedFiles.map((f, idx) => (
                    <div key={idx} style={{ padding: '8px 10px', background: '#0b1120', borderRadius: '6px', fontSize: '0.78rem', display: 'flex', justifyContent: 'space-between', border: '1px solid #1e293b' }}>
                      <span style={{ color: '#f8fafc', fontWeight: 600 }}>✓ {f.name}</span>
                      <span style={{ color: '#34d399', fontWeight: 800 }}>STAGED</span>
                    </div>
                  ))}
                  {stagedFiles.length === 0 && <span style={{ fontSize: '0.78rem', color: '#94a3b8' }}>No staged snapshots</span>}
                </div>
              </div>

              {/* Local HEAD Commit */}
              <div style={{ background: '#131d31', padding: 14, borderRadius: '10px', border: '1px solid #38bdf8', minWidth: 0 }}>
                <div style={{ fontWeight: 800, fontSize: '0.85rem', color: '#38bdf8', marginBottom: 10 }}>3. Local Repository (HEAD)</div>
                <div style={{ padding: '12px', background: '#0b1120', borderRadius: '8px', border: '1px solid #1e293b' }}>
                  <div style={{ fontSize: '0.8rem', color: '#fbbf24', fontWeight: 800 }}>Commit: {commits[commits.length - 1]?.hash}</div>
                  <div style={{ fontSize: '0.85rem', color: '#ffffff', fontWeight: 700, marginTop: 4 }}>{commits[commits.length - 1]?.message}</div>
                  <div style={{ fontSize: '0.75rem', color: '#94a3b8', marginTop: 4 }}>Branch: {commits[commits.length - 1]?.branch}</div>
                </div>
              </div>
            </div>
          </div>
        </div>
      )}

      {/* TAB 3: BRANCHING & MERGES */}
      {activeTab === 'branching' && (
        <div style={{ display: 'grid', gap: 16, width: '100%', minWidth: 0 }}>
          <div style={{ padding: 18, background: '#070b14', border: '1px solid #1e293b', borderRadius: '12px', width: '100%', minWidth: 0, boxSizing: 'border-box' }}>
            <h3 style={{ fontSize: '1.05rem', fontWeight: 800, color: '#ffffff', marginBottom: 14, display: 'flex', alignItems: 'center', gap: 6 }}>
              <GitBranch size={17} color="#f59e0b" /> Branching, Switching & Fast-Forward Merges
            </h3>

            <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(220px, 1fr))', gap: 14, width: '100%', minWidth: 0 }}>
              <div style={{ background: '#131d31', padding: 14, borderRadius: '10px', border: '1px solid #334155', minWidth: 0 }}>
                <div style={{ fontWeight: 800, fontSize: '0.85rem', color: '#38bdf8', marginBottom: 10 }}>Active Branches:</div>
                <div style={{ display: 'flex', flexDirection: 'column', gap: 6 }}>
                  {branches.map((b, idx) => (
                    <div key={idx} style={{ padding: '8px 12px', background: '#0b1120', borderRadius: '6px', fontSize: '0.82rem', display: 'flex', justifyContent: 'space-between', alignItems: 'center', border: '1px solid #1e293b' }}>
                      <span style={{ color: b === currentBranch ? '#34d399' : '#ffffff', fontWeight: b === currentBranch ? 800 : 600 }}>
                        {b === currentBranch ? '● (HEAD) ' : '○ '}{b}
                      </span>
                      {b !== currentBranch && (
                        <button onClick={() => executeGitCommand(`git checkout ${b}`)} style={{ background: '#1e293b', color: '#38bdf8', border: '1px solid #0284c7', padding: '3px 8px', borderRadius: '5px', fontSize: '0.72rem', fontWeight: 700, cursor: 'pointer' }}>
                          Checkout
                        </button>
                      )}
                    </div>
                  ))}
                </div>
              </div>

              <div style={{ background: '#131d31', padding: 14, borderRadius: '10px', border: '1px solid #334155', minWidth: 0 }}>
                <div style={{ fontWeight: 800, fontSize: '0.85rem', color: '#34d399', marginBottom: 10 }}>Merge Operations:</div>
                <div style={{ display: 'flex', flexDirection: 'column', gap: 8 }}>
                  <button onClick={() => executeGitCommand(`git merge main`)} style={{ background: 'linear-gradient(135deg, #10b981, #059669)', color: '#ffffff', border: 'none', padding: '10px', borderRadius: '8px', fontSize: '0.82rem', fontWeight: 800, cursor: 'pointer' }}>
                    Merge 'main' into '{currentBranch}'
                  </button>
                  <button onClick={() => executeGitCommand(`git checkout -b feature/analytics`)} style={{ background: 'linear-gradient(135deg, #6366f1, #4f46e5)', color: '#ffffff', border: 'none', padding: '10px', borderRadius: '8px', fontSize: '0.82rem', fontWeight: 800, cursor: 'pointer' }}>
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
          <div style={{ padding: 18, background: '#070b14', border: '1px solid #1e293b', borderRadius: '12px', width: '100%', minWidth: 0, boxSizing: 'border-box' }}>
            <h3 style={{ fontSize: '1.05rem', fontWeight: 800, color: '#ffffff', marginBottom: 14, display: 'flex', alignItems: 'center', gap: 6 }}>
              <RotateCcw size={17} color="#ec4899" /> History Rewriting: `rebase`, `cherry-pick`, `reset`, `revert`, `stash`
            </h3>

            <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(200px, 1fr))', gap: 12, width: '100%', minWidth: 0 }}>
              <div style={{ background: '#131d31', padding: 12, borderRadius: '8px', border: '1px solid #ec4899', minWidth: 0 }}>
                <div style={{ fontWeight: 800, fontSize: '0.82rem', color: '#f472b6', marginBottom: 4 }}>1. Linearize (rebase)</div>
                <p style={{ fontSize: '0.75rem', color: '#cbd5e1', margin: '0 0 10px 0' }}>Replays commits on top of base.</p>
                <button onClick={() => executeGitCommand('git rebase main')} style={{ width: '100%', background: '#1e293b', color: '#f472b6', border: '1px solid #ec4899', padding: '6px', borderRadius: '6px', fontWeight: 700, fontSize: '0.75rem', cursor: 'pointer' }}>
                  git rebase main
                </button>
              </div>

              <div style={{ background: '#131d31', padding: 12, borderRadius: '8px', border: '1px solid #38bdf8', minWidth: 0 }}>
                <div style={{ fontWeight: 800, fontSize: '0.82rem', color: '#38bdf8', marginBottom: 4 }}>2. Cherry-Pick</div>
                <p style={{ fontSize: '0.75rem', color: '#cbd5e1', margin: '0 0 10px 0' }}>Applies a single commit delta.</p>
                <button onClick={() => executeGitCommand('git cherry-pick 3c19e4')} style={{ width: '100%', background: '#1e293b', color: '#38bdf8', border: '1px solid #38bdf8', padding: '6px', borderRadius: '6px', fontWeight: 700, fontSize: '0.75rem', cursor: 'pointer' }}>
                  git cherry-pick 3c19e4
                </button>
              </div>

              <div style={{ background: '#131d31', padding: 12, borderRadius: '8px', border: '1px solid #eab308', minWidth: 0 }}>
                <div style={{ fontWeight: 800, fontSize: '0.82rem', color: '#fde047', marginBottom: 4 }}>3. Stash Stack</div>
                <p style={{ fontSize: '0.75rem', color: '#cbd5e1', margin: '0 0 10px 0' }}>Items in stack: <strong>{stashStack.length}</strong></p>
                <div style={{ display: 'flex', gap: 6 }}>
                  <button onClick={() => executeGitCommand('git stash')} style={{ flex: 1, background: '#eab308', color: '#090d16', border: 'none', padding: '5px', borderRadius: '5px', fontWeight: 800, fontSize: '0.72rem', cursor: 'pointer' }}>Stash</button>
                  <button onClick={() => executeGitCommand('git stash pop')} style={{ flex: 1, background: '#1e293b', color: '#fde047', border: '1px solid #eab308', padding: '5px', borderRadius: '5px', fontWeight: 800, fontSize: '0.72rem', cursor: 'pointer' }}>Pop</button>
                </div>
              </div>

              <div style={{ background: '#131d31', padding: 12, borderRadius: '8px', border: '1px solid #f43f5e', minWidth: 0 }}>
                <div style={{ fontWeight: 800, fontSize: '0.82rem', color: '#fb7185', marginBottom: 4 }}>4. Reset & Revert</div>
                <p style={{ fontSize: '0.75rem', color: '#cbd5e1', margin: '0 0 10px 0' }}>Undo commits or create patch.</p>
                <div style={{ display: 'flex', gap: 6 }}>
                  <button onClick={() => executeGitCommand('git reset --hard HEAD~1')} style={{ flex: 1, background: '#f43f5e', color: '#ffffff', border: 'none', padding: '5px', borderRadius: '5px', fontWeight: 700, fontSize: '0.7rem', cursor: 'pointer' }}>Hard Reset</button>
                  <button onClick={() => executeGitCommand('git revert 9a01f8')} style={{ flex: 1, background: '#10b981', color: '#090d16', border: 'none', padding: '5px', borderRadius: '5px', fontWeight: 800, fontSize: '0.7rem', cursor: 'pointer' }}>Revert</button>
                </div>
              </div>
            </div>
          </div>
        </div>
      )}

      {/* TAB 5: REMOTE SYNC & COLLABORATION */}
      {activeTab === 'remotes-sync' && (
        <div style={{ display: 'grid', gap: 16, width: '100%', minWidth: 0 }}>
          <div style={{ padding: 18, background: '#070b14', border: '1px solid #1e293b', borderRadius: '12px', width: '100%', minWidth: 0, boxSizing: 'border-box' }}>
            <h3 style={{ fontSize: '1.05rem', fontWeight: 800, color: '#ffffff', marginBottom: 14, display: 'flex', alignItems: 'center', gap: 6 }}>
              <UploadCloud size={17} color="#8b5cf6" /> Remote Synchronization (`remote`, `fetch`, `pull`, `push`)
            </h3>

            <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(220px, 1fr))', gap: 14, width: '100%', minWidth: 0 }}>
              <div style={{ background: '#131d31', padding: 14, borderRadius: '10px', border: '1px solid #8b5cf6', minWidth: 0 }}>
                <div style={{ fontWeight: 800, fontSize: '0.85rem', color: '#a78bfa', marginBottom: 4 }}>Remote Endpoints (origin):</div>
                <div style={{ fontFamily: 'monospace', fontSize: '0.75rem', color: '#38bdf8', padding: '8px', background: '#0b1120', borderRadius: '6px', wordBreak: 'break-all', border: '1px solid #1e293b' }}>
                  {remoteOriginUrl}
                </div>
                <div style={{ fontSize: '0.78rem', color: '#cbd5e1', marginTop: 8 }}>
                  Commits on Remote: <strong style={{ color: '#a78bfa' }}>{remoteCommitsCount}</strong> • Local: <strong style={{ color: '#34d399' }}>{commits.length}</strong>
                </div>
              </div>

              <div style={{ background: '#131d31', padding: 14, borderRadius: '10px', display: 'flex', flexDirection: 'column', gap: 8, minWidth: 0, border: '1px solid #334155' }}>
                <button onClick={() => executeGitCommand('git fetch origin')} style={{ background: '#1e293b', color: '#38bdf8', border: '1px solid #0284c7', padding: '8px', borderRadius: '6px', fontWeight: 700, fontSize: '0.78rem', cursor: 'pointer', display: 'flex', alignItems: 'center', justifyContent: 'center', gap: 6 }}>
                  <DownloadCloud size={14} /> Fetch Remote Objects (git fetch)
                </button>
                <button onClick={() => executeGitCommand('git pull origin main')} style={{ background: '#1e293b', color: '#34d399', border: '1px solid #10b981', padding: '8px', borderRadius: '6px', fontWeight: 700, fontSize: '0.78rem', cursor: 'pointer', display: 'flex', alignItems: 'center', justifyContent: 'center', gap: 6 }}>
                  <RotateCw size={14} /> Pull & Merge Remote (git pull)
                </button>
                <button onClick={() => executeGitCommand('git push origin main')} style={{ background: 'linear-gradient(135deg, #10b981, #059669)', color: '#ffffff', border: 'none', padding: '8px', borderRadius: '6px', fontWeight: 800, fontSize: '0.78rem', cursor: 'pointer', display: 'flex', alignItems: 'center', justifyContent: 'center', gap: 6 }}>
                  <UploadCloud size={14} /> Push Local Commits (git push)
                </button>
              </div>
            </div>
          </div>
        </div>
      )}

      {/* TAB 6: GITHUB PULL REQUESTS & REVIEWS */}
      {activeTab === 'github-pr' && (
        <div style={{ display: 'grid', gap: 16, width: '100%', minWidth: 0 }}>
          <div style={{ padding: 18, background: '#070b14', border: '1px solid #1e293b', borderRadius: '12px', width: '100%', minWidth: 0, boxSizing: 'border-box' }}>
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: 14, flexWrap: 'wrap', gap: 6 }}>
              <div>
                <span style={{ fontSize: '0.75rem', color: '#a78bfa', fontWeight: 800 }}>PULL REQUEST #42</span>
                <h3 style={{ fontSize: '1.15rem', fontWeight: 800, margin: '2px 0 0 0', color: '#ffffff' }}>
                  feat: implement enterprise JWT authentication and security headers
                </h3>
              </div>
              <span
                style={{
                  padding: '4px 12px',
                  borderRadius: '16px',
                  fontSize: '0.75rem',
                  fontWeight: 800,
                  background: prStatus === 'merged' ? 'rgba(139, 92, 246, 0.25)' : 'rgba(16, 185, 129, 0.25)',
                  color: prStatus === 'merged' ? '#a78bfa' : '#34d399',
                  border: `1px solid ${prStatus === 'merged' ? '#8b5cf6' : '#10b981'}`
                }}
              >
                {prStatus.toUpperCase()}
              </span>
            </div>

            {/* Reviewers Feedback */}
            <div style={{ display: 'flex', flexDirection: 'column', gap: 8, marginBottom: 14 }}>
              {prReviews.map((r, idx) => (
                <div key={idx} style={{ padding: '10px 14px', background: '#131d31', borderRadius: '8px', border: '1px solid #334155', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                  <div>
                    <span style={{ fontSize: '0.82rem', fontWeight: 800, color: '#f8fafc' }}>{r.reviewer}</span>
                    <div style={{ fontSize: '0.75rem', color: '#cbd5e1', marginTop: 2 }}>{r.comment}</div>
                  </div>
                  <span style={{ fontSize: '0.72rem', color: '#34d399', fontWeight: 800 }}>✓ {r.status}</span>
                </div>
              ))}
            </div>

            {/* Merge Actions */}
            {prStatus === 'open' && (
              <div style={{ display: 'flex', gap: 10, alignItems: 'center', background: '#0b1120', padding: 12, borderRadius: '8px', border: '1px solid #1e293b', flexWrap: 'wrap' }}>
                <select className="input" value={mergeStrategy} onChange={(e) => setMergeStrategy(e.target.value)} style={{ fontSize: '0.8rem', flex: 1, minWidth: '160px', background: '#1e293b', color: '#f8fafc', border: '1px solid #334155' }}>
                  <option value="merge-commit">Create a merge commit</option>
                  <option value="squash">Squash and merge</option>
                  <option value="rebase">Rebase and merge</option>
                </select>
                <button onClick={handleMergePr} style={{ background: 'linear-gradient(135deg, #6366f1, #4f46e5)', color: '#ffffff', border: 'none', padding: '8px 16px', borderRadius: '6px', fontWeight: 800, fontSize: '0.8rem', cursor: 'pointer', display: 'flex', alignItems: 'center', gap: 6 }}>
                  <GitPullRequest size={14} /> Merge Pull Request
                </button>
              </div>
            )}
          </div>
        </div>
      )}

      {/* TAB 7: GITHUB ACTIONS CI/CD */}
      {activeTab === 'github-actions' && (
        <div style={{ display: 'grid', gap: 16, width: '100%', minWidth: 0 }}>
          <div style={{ padding: 18, background: '#070b14', border: '1px solid #1e293b', borderRadius: '12px', width: '100%', minWidth: 0, boxSizing: 'border-box' }}>
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: 14, flexWrap: 'wrap', gap: 6 }}>
              <div>
                <span style={{ fontSize: '0.75rem', color: '#38bdf8', fontWeight: 800 }}>WORKFLOW: .github/workflows/main.yml</span>
                <h3 style={{ fontSize: '1.1rem', fontWeight: 800, margin: '2px 0 0 0', color: '#ffffff' }}>
                  🚀 Enterprise CI/CD Automated Deployment Matrix
                </h3>
              </div>
              <button onClick={runCicdPipeline} disabled={pipelineRunning} style={{ background: 'linear-gradient(135deg, #0ea5e9, #0284c7)', color: '#ffffff', border: 'none', padding: '6px 14px', borderRadius: '6px', fontWeight: 800, fontSize: '0.78rem', cursor: 'pointer', display: 'flex', alignItems: 'center', gap: 6, opacity: pipelineRunning ? 0.6 : 1 }}>
                <Play size={13} /> {pipelineRunning ? 'Executing...' : 'Trigger Workflow'}
              </button>
            </div>

            <div style={{ display: 'flex', flexDirection: 'column', gap: 8 }}>
              {pipelineSteps.map((step) => (
                <div
                  key={step.id}
                  style={{
                    padding: '12px 16px',
                    background: '#131d31',
                    borderRadius: '8px',
                    border: `1px solid ${step.status === 'success' ? '#10b981' : step.status === 'running' ? '#38bdf8' : '#334155'}`,
                    display: 'flex',
                    justifyContent: 'space-between',
                    alignItems: 'center'
                  }}
                >
                  <span style={{ fontSize: '0.82rem', fontWeight: 700, color: '#f8fafc' }}>{step.name}</span>
                  <span
                    style={{
                      fontSize: '0.72rem',
                      fontWeight: 800,
                      padding: '3px 8px',
                      borderRadius: '5px',
                      background: step.status === 'success' ? 'rgba(16, 185, 129, 0.2)' : step.status === 'running' ? 'rgba(56, 189, 248, 0.2)' : 'rgba(255, 255, 255, 0.05)',
                      color: step.status === 'success' ? '#34d399' : step.status === 'running' ? '#38bdf8' : '#94a3b8'
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
