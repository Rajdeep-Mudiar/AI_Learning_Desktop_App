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
  Database,
  Folder,
  FolderOpen,
  Copy,
  ExternalLink,
  GitPullRequestDraft
} from 'lucide-react';
import Badge from '../components/common/Badge';
import { useTheme } from '../contexts/ThemeContext';

export default function GitLabPage() {
  const { theme } = useTheme();
  const isLight = theme === 'light';

  const [activeTab, setActiveTab] = useState('all-terminal'); 
  // 'all-terminal' | 'snapshots' | 'branching' | 'undo-rebase' | 'remotes-sync' | 'github-pr' | 'github-actions'

  // --- Dynamic Command Simulation State (Reacts dynamically to typed commands) ---
  const [activeSimView, setActiveSimView] = useState('staging-trees'); 
  // 'dag' | 'staging-trees' | 'diff-inspector' | 'branch-network' | 'rebase-replay' | 'stash-stack' | 'remote-sync' | 'reset-rollback'
  const [lastExecutedCmd, setLastExecutedCmd] = useState('git status');
  const [simAlertMsg, setSimAlertMsg] = useState('Shell emulator active. Navigate files (cd, ls, pwd, cat, touch) or run any Git command.');

  // --- Shell Working Directory State ---
  const [currentDir, setCurrentDir] = useState(''); // '' for root, 'src', 'config', 'src/auth', 'src/utils'

  // --- Global DAG / Repo State ---
  const [repoInitialized, setRepoInitialized] = useState(true);
  const [commits, setCommits] = useState([
    {
      id: 'c1',
      hash: 'e4f1a0',
      message: 'Initial commit',
      branch: 'main',
      parent: null,
      author: 'Alex Chen',
      email: 'alex@example.com',
      avatar: '👨‍💻',
      time: '2 days ago',
      verified: true,
      tag: 'v0.1.0',
      filesChanged: [
        { file: 'README.md', additions: 18, deletions: 0 },
        { file: '.gitignore', additions: 12, deletions: 0 }
      ],
      diffSnippet: `+++ b/README.md\n@@ -0,0 +1,18 @@\n+# AI Learning Lab App\n+Next-generation interactive platform for Git, AI, and Web Development.`
    },
    {
      id: 'c2',
      hash: '7b89d2',
      message: 'Setup project config & Vite build system',
      branch: 'main',
      parent: 'e4f1a0',
      author: 'Alex Chen',
      email: 'alex@example.com',
      avatar: '👨‍💻',
      time: '1 day ago',
      verified: true,
      filesChanged: [
        { file: 'vite.config.js', additions: 24, deletions: 0 },
        { file: 'package.json', additions: 35, deletions: 2 }
      ],
      diffSnippet: `+++ b/vite.config.js\n@@ -0,0 +1,24 @@\n+import { defineConfig } from 'vite';\n+import react from '@vitejs/plugin-react';\n+export default defineConfig({ plugins: [react()] });`
    },
    {
      id: 'c3',
      hash: '3c19e4',
      message: 'Add JWT auth middleware & security checks',
      branch: 'feature/auth',
      parent: '7b89d2',
      author: 'Alex Chen',
      email: 'alex@example.com',
      avatar: '👨‍💻',
      time: '4 hours ago',
      verified: true,
      filesChanged: [
        { file: 'src/auth/jwt.py', additions: 42, deletions: 5 },
        { file: 'src/auth/middleware.py', additions: 28, deletions: 0 }
      ],
      diffSnippet: `+++ b/src/auth/jwt.py\n@@ -1,5 +1,42 @@\n+import jwt\n+from datetime import datetime, timedelta\n+def encode_jwt(user_id: str):\n+    return jwt.encode({"sub": user_id}, SECRET_KEY, algorithm="RS256")`
    },
    {
      id: 'c4',
      hash: '9a01f8',
      message: 'Implement login and register API endpoints',
      branch: 'feature/auth',
      parent: '3c19e4',
      author: 'Alex Chen',
      email: 'alex@example.com',
      avatar: '👨‍💻',
      time: '2 hours ago',
      verified: true,
      filesChanged: [
        { file: 'src/auth/routes.py', additions: 65, deletions: 12 },
        { file: 'src/auth/jwt.py', additions: 14, deletions: 3 }
      ],
      diffSnippet: `+++ b/src/auth/routes.py\n@@ -10,8 +10,24 @@\n+@router.post("/register")\n+async def register_user(payload: UserRegister):\n+    return auth_service.register(payload)`
    }
  ]);
  const [branches, setBranches] = useState(['main', 'feature/auth']);
  const [currentBranch, setCurrentBranch] = useState('feature/auth');
  const [tags, setTags] = useState([{ name: 'v0.1.0', commitHash: 'e4f1a0' }]);
  const [stashStack, setStashStack] = useState([]);
  const [remoteOriginUrl, setRemoteOriginUrl] = useState('https://github.com/developer/ai-lab-app.git');
  const [remoteCommitsCount, setRemoteCommitsCount] = useState(2); // origin/main is at c2

  // --- Interactive GitHub Commits State ---
  const [selectedCommitHash, setSelectedCommitHash] = useState('9a01f8');
  const [commitViewMode, setCommitViewMode] = useState('graph'); // 'graph' | 'feed'
  const [commitFilterBranch, setCommitFilterBranch] = useState('all'); // 'all' | branch
  const [copiedHash, setCopiedHash] = useState('');

  // --- Snapshotting / 3-Trees Working Directory State ---
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
  const [commandHistory, setCommandHistory] = useState([]);
  const [historyIndex, setHistoryIndex] = useState(-1);
  const [terminalHistory, setTerminalHistory] = useState([
    '⚡ Interactive Git 2.45 Command & Shell Engine Ready.',
    'Type any Git or Shell command (cd, ls, pwd, cat, touch, git add, git status, git commit) below.'
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

    if (clean.startsWith('git status') || clean.startsWith('git add') || clean.startsWith('cd') || clean.startsWith('ls') || clean.startsWith('dir') || clean.startsWith('pwd') || clean.startsWith('touch')) {
      setActiveSimView('staging-trees');
    } else if (clean.startsWith('git diff') || clean.startsWith('cat')) {
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

  // Helper to resolve paths relative to currentDir
  const resolveFilePath = (target) => {
    const trimmed = target.trim();
    if (!trimmed) return '';
    if (trimmed.startsWith('/') || trimmed.startsWith('src/') || trimmed.startsWith('config/')) {
      return trimmed.replace(/^\//, '');
    }
    return currentDir ? `${currentDir}/${trimmed}` : trimmed;
  };

  // Command Execution Parser
  const executeGitCommand = (rawCmd) => {
    const cmd = rawCmd.trim();
    if (!cmd) return;

    const promptPrefix = `(repo${currentDir ? `/${currentDir}` : ''}) $`;
    setTerminalHistory(prev => [...prev, `${promptPrefix} ${cmd}`]);
    setCommandHistory(prev => (prev.length > 0 && prev[prev.length - 1] === cmd ? prev : [...prev, cmd]));
    setHistoryIndex(-1);
    setCommandInput('');
    setLastExecutedCmd(cmd);

    const lowerCmd = cmd.toLowerCase();

    // ==========================================
    // 1. SHELL COMMANDS (cd, ls, pwd, cat, touch, rm, clear)
    // ==========================================
    if (lowerCmd === 'cd ..') {
      if (!currentDir) {
        setSimAlertMsg('📁 Already at repository root directory `/workspace`.');
      } else {
        const parts = currentDir.split('/');
        parts.pop();
        const newDir = parts.join('/');
        setCurrentDir(newDir);
        setSimAlertMsg(`📁 Navigated up to \`/workspace${newDir ? '/' + newDir : ''}\`.`);
      }
      setActiveSimView('staging-trees');
    }
    else if (lowerCmd === 'cd' || lowerCmd === 'cd ~' || lowerCmd === 'cd /') {
      setCurrentDir('');
      setSimAlertMsg('📁 Navigated to repository root `/workspace`.');
      setActiveSimView('staging-trees');
    }
    else if (lowerCmd.startsWith('cd ')) {
      const target = cmd.substring(3).trim().replace(/^\//, '').replace(/\/$/, '');
      const validDirs = ['src', 'config', 'src/auth', 'src/utils', 'auth', 'utils'];
      
      let resolved = '';
      if (currentDir === '' && (target === 'src' || target === 'config' || target === 'src/auth' || target === 'src/utils')) {
        resolved = target;
      } else if (currentDir === 'src' && (target === 'auth' || target === 'utils')) {
        resolved = `src/${target}`;
      } else if (target === '..' || target === '../') {
        const parts = currentDir.split('/');
        parts.pop();
        resolved = parts.join('/');
      } else if (validDirs.includes(target)) {
        resolved = target;
      }

      if (resolved !== '' || target === '.' || target === '') {
        setCurrentDir(resolved);
        setSimAlertMsg(`📁 Changed directory to \`/workspace${resolved ? '/' + resolved : ''}\`.`);
        setActiveSimView('staging-trees');
      } else {
        setTerminalHistory(prev => [...prev, `bash: cd: ${target}: No such file or directory`]);
      }
    }
    else if (lowerCmd === 'pwd') {
      setTerminalHistory(prev => [...prev, `/workspace${currentDir ? '/' + currentDir : ''}`]);
      setSimAlertMsg(`📍 Working directory: \`/workspace${currentDir ? '/' + currentDir : ''}\`.`);
    }
    else if (lowerCmd === 'ls' || lowerCmd.startsWith('ls ') || lowerCmd === 'dir') {
      setActiveSimView('staging-trees');
      let listing = [];
      if (!currentDir) {
        listing = [
          'config/\tsrc/\t.gitignore\tREADME.md',
          'Modified: src/auth/jwt.py | Untracked: config/database.env'
        ];
      } else if (currentDir === 'config') {
        listing = ['database.env (untracked)'];
      } else if (currentDir === 'src') {
        listing = ['auth/\tutils/'];
      } else if (currentDir === 'src/auth') {
        listing = ['jwt.py (modified)'];
      } else if (currentDir === 'src/utils') {
        listing = ['logger.py (clean)'];
      }
      setTerminalHistory(prev => [...prev, ...listing]);
      setSimAlertMsg(`📂 Directory listing for \`/workspace${currentDir ? '/' + currentDir : ''}\`.`);
    }
    else if (lowerCmd.startsWith('cat ') || lowerCmd.startsWith('type ')) {
      const targetFile = resolveFilePath(cmd.replace(/^(cat|type)\s+/i, ''));
      setActiveSimView('diff-inspector');
      setSelectedDiffFile(targetFile || 'src/auth/jwt.py');
      if (targetFile.includes('jwt.py')) {
        setTerminalHistory(prev => [
          ...prev,
          `# ${targetFile}`,
          `import jwt`,
          `from datetime import datetime, timedelta`,
          `SECRET_KEY = "prod-secret-token"`,
          `def generate_session_token(user_id: str):`,
          `    expire = datetime.utcnow() + timedelta(minutes=60)`,
          `    return jwt.encode({"sub": user_id, "exp": expire}, RSA_PRIVATE_KEY, algorithm="RS256")`
        ]);
        setSimAlertMsg(`📄 Displaying contents of \`${targetFile}\`.`);
      } else if (targetFile.includes('database.env')) {
        setTerminalHistory(prev => [
          ...prev,
          `# ${targetFile}`,
          `DATABASE_URL=postgresql://app_user:secure_pwd@db.internal:5432/lab_db`,
          `DB_POOL_SIZE=20`
        ]);
        setSimAlertMsg(`📄 Displaying contents of \`${targetFile}\`.`);
      } else {
        setTerminalHistory(prev => [...prev, `[content of ${targetFile}]`]);
      }
    }
    else if (lowerCmd.startsWith('touch ')) {
      const fileName = resolveFilePath(cmd.replace(/^touch\s+/i, ''));
      if (!workingFiles.some(f => f.name === fileName)) {
        setWorkingFiles(prev => [...prev, { name: fileName, status: 'untracked', additions: 1, deletions: 0 }]);
        setSimAlertMsg(`✨ Created new untracked file \`${fileName}\` in working directory.`);
        setTerminalHistory(prev => [...prev, `Created file '${fileName}' (untracked).`]);
      } else {
        setTerminalHistory(prev => [...prev, `Updated timestamp for '${fileName}'.`]);
      }
      setActiveSimView('staging-trees');
    }
    else if (lowerCmd.startsWith('rm ')) {
      const targetFile = resolveFilePath(cmd.replace(/^rm\s+(-f\s+)?/i, ''));
      setWorkingFiles(prev => prev.filter(f => f.name !== targetFile));
      setStagedFiles(prev => prev.filter(f => f.name !== targetFile));
      setSimAlertMsg(`🗑️ Removed file \`${targetFile}\` from filesystem.`);
      setTerminalHistory(prev => [...prev, `Removed '${targetFile}'.`]);
      setActiveSimView('staging-trees');
    }

    // ==========================================
    // 2. GIT WORKFLOW & STAGING COMMANDS
    // ==========================================
    else if (cmd === 'git init') {
      setRepoInitialized(true);
      setActiveSimView('dag');
      setSimAlertMsg('✅ Initialized empty Git repository in /workspace/.git/.');
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
        `Receiving objects: 100% (14/14), done.`
      ]);
    }
    else if (lowerCmd === 'git status' || lowerCmd.startsWith('git status')) {
      setActiveSimView('staging-trees');
      setSimAlertMsg('🔍 3-Trees Status: Comparing Working Directory, Staging Index, and HEAD.');
      const stagedNames = stagedFiles.map(f => `\tnew file:   ${f.name}`);
      const untracked = workingFiles.filter(f => f.status === 'untracked').map(f => `\t${f.name}`);
      const modified = workingFiles.filter(f => f.status === 'modified').map(f => `\tmodified:   ${f.name}`);

      setTerminalHistory(prev => [
        ...prev,
        `On branch ${currentBranch}`,
        stagedFiles.length > 0 ? `Changes to be committed: (use "git restore --staged <file>..." to unstage)\n${stagedNames.join('\n')}` : 'No changes added to commit (use "git add")',
        modified.length > 0 ? `Changes not staged for commit:\n${modified.join('\n')}` : '',
        untracked.length > 0 ? `Untracked files:\n${untracked.join('\n')}` : '',
        stagedFiles.length === 0 && workingFiles.filter(f => f.status !== 'clean').length === 0 ? 'nothing to commit, working tree clean' : ''
      ].filter(Boolean));
    }
    else if (lowerCmd === 'git add -a' || lowerCmd === 'git add --all') {
      setActiveSimView('staging-trees');
      const newlyStaged = workingFiles.filter(f => f.status !== 'clean');
      setStagedFiles(prev => [...prev.filter(f => !newlyStaged.some(n => n.name === f.name)), ...newlyStaged]);
      setWorkingFiles(prev => prev.map(f => ({ ...f, status: 'clean' })));
      setSimAlertMsg(`📦 Staged all ${newlyStaged.length} repository file(s) into Git Index (--all).`);
      setTerminalHistory(prev => [...prev, `Staged all ${newlyStaged.length} file(s) across entire repository to index.`]);
    }
    else if (lowerCmd === 'git add .' || lowerCmd === 'git add') {
      setActiveSimView('staging-trees');
      // In Git, 'git add .' only stages files in the current working directory and subdirectories
      const newlyStaged = workingFiles.filter(f => {
        if (f.status === 'clean') return false;
        if (!currentDir) return true; // root stages all
        return f.name.startsWith(currentDir + '/') || f.name === currentDir;
      });

      if (newlyStaged.length > 0) {
        setStagedFiles(prev => [...prev.filter(f => !newlyStaged.some(n => n.name === f.name)), ...newlyStaged]);
        setWorkingFiles(prev => prev.map(f => newlyStaged.some(n => n.name === f.name) ? { ...f, status: 'clean' } : f));
        const scopeName = currentDir ? `\`${currentDir}/\`` : 'entire repository';
        setSimAlertMsg(`📦 Staged ${newlyStaged.length} file(s) in ${scopeName} into Git Index.`);
        setTerminalHistory(prev => [
          ...prev,
          `Staged ${newlyStaged.length} file(s) in '${currentDir || '.'}': ${newlyStaged.map(n => n.name).join(', ')}`
        ]);
      } else {
        const scopeName = currentDir ? `in folder '${currentDir}'` : 'in repository';
        setSimAlertMsg(`ℹ️ Nothing to add ${scopeName} (no modified or untracked files).`);
        setTerminalHistory(prev => [...prev, `nothing to add ${scopeName} (working tree clean in this path)`]);
      }
    }
    else if (lowerCmd.startsWith('git add ')) {
      setActiveSimView('staging-trees');
      const targetArg = cmd.replace(/git add\s+/i, '').trim();
      
      if (targetArg === '.' || targetArg === './') {
        executeGitCommand('git add .');
        return;
      }
      
      const resolved = resolveFilePath(targetArg);

      // Check if targetArg is a directory (e.g. 'config', 'src', 'src/auth')
      const dirMatches = workingFiles.filter(f => {
        if (f.status === 'clean') return false;
        return f.name.startsWith(resolved + '/') || f.name.startsWith(targetArg + '/');
      });

      if (dirMatches.length > 0) {
        setStagedFiles(prev => [...prev.filter(f => !dirMatches.some(n => n.name === f.name)), ...dirMatches]);
        setWorkingFiles(prev => prev.map(f => dirMatches.some(n => n.name === f.name) ? { ...f, status: 'clean' } : f));
        setSimAlertMsg(`📦 Staged ${dirMatches.length} file(s) in directory \`${targetArg}\`.`);
        setTerminalHistory(prev => [...prev, `Staged ${dirMatches.length} file(s) under '${targetArg}': ${dirMatches.map(n => n.name).join(', ')}`]);
        return;
      }
      
      // Check for single file match
      const fileToStage = workingFiles.find(f => f.name === resolved || f.name === targetArg || f.name.endsWith('/' + targetArg));
      if (fileToStage) {
        if (fileToStage.status !== 'clean') {
          setStagedFiles(prev => [...prev.filter(f => f.name !== fileToStage.name), fileToStage]);
          setWorkingFiles(prev => prev.map(f => f.name === fileToStage.name ? { ...f, status: 'clean' } : f));
          setSimAlertMsg(`📦 Staged \`${fileToStage.name}\` into the Git Index.`);
          setTerminalHistory(prev => [...prev, `Staged '${fileToStage.name}' to index.`]);
        } else {
          setSimAlertMsg(`ℹ️ \`${fileToStage.name}\` is already clean / up-to-date.`);
          setTerminalHistory(prev => [...prev, `'${fileToStage.name}' has no unstaged changes.`]);
        }
      } else {
        setTerminalHistory(prev => [...prev, `fatal: pathspec '${targetArg}' did not match any files`]);
      }
    }
    else if (lowerCmd.startsWith('git restore --staged') || lowerCmd.startsWith('git rm --cached') || lowerCmd === 'git reset' || lowerCmd.startsWith('git reset ')) {
      setActiveSimView('staging-trees');
      const targetArg = cmd.replace(/git (restore --staged|rm --cached|reset)\s*/i, '').trim();
      
      if (!targetArg || targetArg === '.' || targetArg === './') {
        // Unstage current folder or whole repo if at root
        const toUnstage = stagedFiles.filter(f => {
          if (!currentDir) return true;
          return f.name.startsWith(currentDir + '/') || f.name === currentDir;
        });

        if (toUnstage.length > 0) {
          setStagedFiles(prev => prev.filter(f => !toUnstage.some(u => u.name === f.name)));
          setWorkingFiles(prev => prev.map(f => {
            const unstagedItem = toUnstage.find(u => u.name === f.name);
            return unstagedItem ? { ...f, status: unstagedItem.status || 'modified' } : f;
          }));
          const scope = currentDir ? `in \`${currentDir}/\`` : 'from index';
          setSimAlertMsg(`↩️ Unstaged ${toUnstage.length} file(s) ${scope}.`);
          setTerminalHistory(prev => [...prev, `Unstaged ${toUnstage.length} file(s) in '${currentDir || '.'}'.`]);
        } else {
          setSimAlertMsg(`ℹ️ No staged changes to restore in \`/workspace/${currentDir}\`.`);
          setTerminalHistory(prev => [...prev, `nothing staged in '${currentDir || '.'}' to unstage.`]);
        }
        return;
      }

      const resolved = resolveFilePath(targetArg);
      const stagedMatch = stagedFiles.find(f => f.name === resolved || f.name === targetArg || f.name.endsWith('/' + targetArg));
      if (stagedMatch) {
        setStagedFiles(prev => prev.filter(f => f.name !== stagedMatch.name));
        setWorkingFiles(prev => prev.map(f => f.name === stagedMatch.name ? { ...f, status: stagedMatch.status || 'modified' } : f));
        setSimAlertMsg(`↩️ Unstaged \`${stagedMatch.name}\` back to working directory.`);
        setTerminalHistory(prev => [...prev, `Unstaged '${stagedMatch.name}'.`]);
      } else {
        setTerminalHistory(prev => [...prev, `fatal: pathspec '${targetArg}' did not match any staged files`]);
      }
    }
    else if (lowerCmd.startsWith('git restore ') || lowerCmd.startsWith('git checkout -- ')) {
      setActiveSimView('staging-trees');
      const targetArg = cmd.replace(/git (restore|checkout --)\s+/i, '').trim();
      const resolved = resolveFilePath(targetArg);
      setWorkingFiles(prev => prev.map(f => (f.name === resolved || f.name.endsWith(targetArg)) ? { ...f, status: 'clean' } : f));
      setSimAlertMsg(`↩️ Discarded working tree changes in \`${resolved}\`.`);
      setTerminalHistory(prev => [...prev, `Discarded working tree changes for '${resolved}'.`]);
    }
    else if (lowerCmd.startsWith('git commit -m') || lowerCmd.startsWith('git commit -am') || lowerCmd.startsWith('git commit --message')) {
      setActiveSimView('dag');
      const match = cmd.match(/-m\s+["'](.*?)["']/i);
      const msg = match ? match[1] : 'Update codebase';
      const newHash = Math.random().toString(16).substring(2, 8);
      const parentHash = commits.length > 0 ? commits[commits.length - 1].hash : null;
      
      const newCommitFiles = stagedFiles.length > 0 ? stagedFiles.map(f => ({
        file: f.name,
        additions: f.additions || Math.floor(Math.random() * 20) + 2,
        deletions: f.deletions || Math.floor(Math.random() * 4)
      })) : [
        { file: 'src/auth/jwt.py', additions: 14, deletions: 3 },
        { file: 'config/database.env', additions: 8, deletions: 0 }
      ];

      const newCommit = {
        id: `c${commits.length + 1}`,
        hash: newHash,
        message: msg,
        branch: currentBranch,
        parent: parentHash,
        author: 'Alex Chen',
        email: 'alex@example.com',
        avatar: '👨‍💻',
        time: 'Just now',
        verified: true,
        filesChanged: newCommitFiles,
        diffSnippet: `+++ b/${newCommitFiles[0]?.file || 'src/main.py'}\n@@ -1,4 +1,12 @@\n+// ${msg}\n+export const feature = true;`
      };
      setCommits(prev => [...prev, newCommit]);
      setSelectedCommitHash(newHash);
      setStagedFiles([]);
      setSimAlertMsg(`✨ Created immutable DAG commit [${newHash}] on branch '${currentBranch}'.`);
      setTerminalHistory(prev => [...prev, `[${currentBranch} ${newHash}] ${msg}`, ` ${newCommitFiles.length} files changed, 22 insertions(+), 3 deletions(-)`]);
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
      const rawTarget = cmd.replace(/git (checkout|switch)\s*/i, '').trim();
      const target = rawTarget.replace(/^[#\s]+/, '').trim();

      // 1. Check if branch exists
      if (branches.includes(target) || branches.includes(rawTarget)) {
        const branchName = branches.includes(target) ? target : rawTarget;
        setCurrentBranch(branchName);
        setActiveSimView('branch-network');
        setSimAlertMsg(`👉 HEAD pointer moved to branch '${branchName}'.`);
        setTerminalHistory(prev => [...prev, `Switched to branch '${branchName}'`]);
      }
      // 2. Check if commit hash or prefix matches any commit
      else if (commits.some(c => c.hash.toLowerCase() === target.toLowerCase() || c.hash.toLowerCase().startsWith(target.toLowerCase()))) {
        const commitMatch = commits.find(c => c.hash.toLowerCase() === target.toLowerCase() || c.hash.toLowerCase().startsWith(target.toLowerCase()));
        setCurrentBranch(commitMatch.hash);
        setActiveSimView('dag');
        setSimAlertMsg(`📍 Switched HEAD to commit [${commitMatch.hash}] (${commitMatch.message}) in detached HEAD state.`);
        setTerminalHistory(prev => [
          ...prev,
          `Note: switching to '${commitMatch.hash}'.`,
          `You are in 'detached HEAD' state. HEAD is now at ${commitMatch.hash} ${commitMatch.message}`
        ]);
      }
      // 3. Relative HEAD commit (e.g. HEAD~1, HEAD^)
      else if (target.toUpperCase() === 'HEAD~1' || target.toUpperCase() === 'HEAD^' || target.toUpperCase() === 'HEAD~') {
        if (commits.length > 1) {
          const targetCommit = commits[commits.length - 2];
          setCurrentBranch(targetCommit.hash);
          setActiveSimView('dag');
          setSimAlertMsg(`📍 Switched HEAD to parent commit [${targetCommit.hash}].`);
          setTerminalHistory(prev => [
            ...prev,
            `HEAD is now at ${targetCommit.hash} ${targetCommit.message}`
          ]);
        } else {
          setTerminalHistory(prev => [...prev, `fatal: reference is not a tree: HEAD~1`]);
        }
      }
      // 4. Check if tag exists
      else if (tags.some(t => t.name.toLowerCase() === target.toLowerCase())) {
        const tagMatch = tags.find(t => t.name.toLowerCase() === target.toLowerCase());
        setCurrentBranch(tagMatch.commitHash);
        setActiveSimView('dag');
        setSimAlertMsg(`🏷️ Switched HEAD to release tag '${tagMatch.name}' at commit [${tagMatch.commitHash}].`);
        setTerminalHistory(prev => [...prev, `HEAD is now at tag '${tagMatch.name}' (${tagMatch.commitHash})`]);
      }
      // 5. Check if file exists in working tree (git checkout <file> to discard)
      else if (workingFiles.some(f => f.name === resolveFilePath(target) || f.name === target || f.name.endsWith('/' + target))) {
        const fileMatch = workingFiles.find(f => f.name === resolveFilePath(target) || f.name === target || f.name.endsWith('/' + target));
        setActiveSimView('staging-trees');
        setWorkingFiles(prev => prev.map(f => f.name === fileMatch.name ? { ...f, status: 'clean' } : f));
        setSimAlertMsg(`↩️ Discarded working tree changes in \`${fileMatch.name}\`.`);
        setTerminalHistory(prev => [...prev, `Updated 1 path from the index for '${fileMatch.name}'.`]);
      }
      else {
        setTerminalHistory(prev => [...prev, `error: pathspec '${rawTarget}' did not match any file(s) or branch/commit known to git`]);
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
      const fileArg = cmd.replace(/git diff(\s+--staged)?\s*/i, '').trim();
      const resolved = resolveFilePath(fileArg);
      setActiveSimView('diff-inspector');
      if (resolved) setSelectedDiffFile(resolved);
      setSimAlertMsg(`📊 Visual Code Diff Inspector: Showing unified code additions & deletions.`);
      setTerminalHistory(prev => [
        ...prev,
        `diff --git a/${resolved || 'src/auth/jwt.py'} b/${resolved || 'src/auth/jwt.py'}`,
        `index e4a19b..8f12d4 100644`,
        `--- a/${resolved || 'src/auth/jwt.py'}`,
        `+++ b/${resolved || 'src/auth/jwt.py'}`,
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
        `sh: command not found: '${cmd}'. Try 'cd', 'ls', 'pwd', 'cat <file>', 'touch <file>', or 'git status', 'git add <file>', 'git commit'.`
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

  const getBranchStyle = (branchName) => {
    const palette = [
      { color: isLight ? '#1877f2' : '#38bdf8', bg: isLight ? '#e7f3ff' : 'rgba(56, 189, 248, 0.15)', border: isLight ? '#1877f2' : '#38bdf8' },
      { color: isLight ? '#16a34a' : '#34d399', bg: isLight ? '#e6ffec' : 'rgba(52, 211, 153, 0.15)', border: isLight ? '#16a34a' : '#34d399' },
      { color: isLight ? '#9333ea' : '#c084fc', bg: isLight ? '#f3e8ff' : 'rgba(192, 132, 252, 0.15)', border: isLight ? '#9333ea' : '#c084fc' },
      { color: isLight ? '#d97706' : '#fbbf24', bg: isLight ? '#fef3c7' : 'rgba(251, 191, 36, 0.15)', border: isLight ? '#d97706' : '#fbbf24' },
      { color: isLight ? '#e1306c' : '#f472b6', bg: isLight ? '#fdf2f8' : 'rgba(244, 114, 182, 0.15)', border: isLight ? '#e1306c' : '#f472b6' },
      { color: isLight ? '#0284c7' : '#06b6d4', bg: isLight ? '#e0f2fe' : 'rgba(6, 182, 212, 0.15)', border: isLight ? '#0284c7' : '#06b6d4' }
    ];
    const unique = ['main', ...branches.filter(b => b !== 'main')];
    const idx = Math.max(0, unique.indexOf(branchName));
    return palette[idx % palette.length];
  };

  const COMMAND_PRESETS = [
    { label: 'git status', cmd: 'git status' },
    { label: 'ls', cmd: 'ls' },
    { label: 'cd src', cmd: 'cd src' },
    { label: 'cd ..', cmd: 'cd ..' },
    { label: 'pwd', cmd: 'pwd' },
    { label: 'git add .', cmd: 'git add .' },
    { label: 'git add src/auth/jwt.py', cmd: 'git add src/auth/jwt.py' },
    { label: 'cat src/auth/jwt.py', cmd: 'cat src/auth/jwt.py' },
    { label: 'git commit -m "..."', cmd: 'git commit -m "feat: implement security filters"' },
    { label: 'git branch', cmd: 'git branch' },
    { label: 'git checkout -b feature/payments', cmd: 'git checkout -b feature/payments' },
    { label: 'git merge feature/auth', cmd: 'git merge feature/auth' },
    { label: 'git rebase main', cmd: 'git rebase main' },
    { label: 'git stash', cmd: 'git stash' },
    { label: 'git stash pop', cmd: 'git stash pop' },
    { label: 'git diff', cmd: 'git diff' },
    { label: 'git push origin main', cmd: 'git push origin main' }
  ];

  const SIMULATION_VIEWS = [
    { id: 'dag', label: 'DAG Graph', icon: GitCommit, color: isLight ? '#d97706' : '#f59e0b', glow: 'rgba(245, 158, 11, 0.4)' },
    { id: 'staging-trees', label: '3-Trees Staging', icon: Layers, color: isLight ? '#16a34a' : '#10b981', glow: 'rgba(16, 185, 129, 0.4)' },
    { id: 'diff-inspector', label: 'Diff Inspector', icon: FileCode, color: isLight ? '#1877f2' : '#38bdf8', glow: 'rgba(24, 119, 242, 0.4)' },
    { id: 'branch-network', label: 'Branch Network', icon: GitBranch, color: isLight ? '#9333ea' : '#a855f7', glow: 'rgba(147, 51, 234, 0.4)' },
    { id: 'rebase-replay', label: 'Rebase & Cherry-Pick', icon: RefreshCw, color: isLight ? '#e1306c' : '#ec4899', glow: 'rgba(225, 48, 108, 0.4)' },
    { id: 'stash-stack', label: 'Stash Stack', icon: Archive, color: isLight ? '#d97706' : '#eab308', glow: 'rgba(217, 119, 6, 0.4)' },
    { id: 'remote-sync', label: 'Remote Sync', icon: UploadCloud, color: isLight ? '#7c3aed' : '#8b5cf6', glow: 'rgba(124, 58, 237, 0.4)' },
    { id: 'reset-rollback', label: 'Reset Matrix', icon: RotateCcw, color: isLight ? '#dc2626' : '#f43f5e', glow: 'rgba(220, 38, 38, 0.4)' }
  ];

  return (
    <div className="animate-fade-in" style={{ paddingBottom: 40, width: '100%', maxWidth: '100%', minWidth: 0, boxSizing: 'border-box' }}>
      
      {/* Top Header */}
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', flexWrap: 'wrap', gap: 12, marginBottom: 16, width: '100%', minWidth: 0 }}>
        <div style={{ minWidth: 0, flex: 1 }}>
          <div style={{ display: 'flex', alignItems: 'center', gap: 8, marginBottom: 6, flexWrap: 'wrap' }}>
            <Badge variant="yellow"><GitBranch size={14} /> Git & Shell Command Suite</Badge>
            <span style={{ fontSize: '0.85rem', color: isLight ? '#65676b' : '#94a3b8', fontWeight: 600 }}>Interactive Filesystem & Git Simulator</span>
          </div>
          <h1 style={{ fontSize: '1.75rem', fontWeight: 800, color: isLight ? '#050505' : '#ffffff', letterSpacing: '-0.02em' }}>Complete Git & Shell Simulator</h1>
          <p style={{ color: isLight ? '#65676b' : '#cbd5e1', fontSize: '0.92rem', marginTop: 4 }}>
            Navigate directories (<code style={{ color: isLight ? '#1877f2' : '#38bdf8' }}>cd</code>, <code style={{ color: isLight ? '#1877f2' : '#38bdf8' }}>ls</code>, <code style={{ color: isLight ? '#1877f2' : '#38bdf8' }}>pwd</code>, <code style={{ color: isLight ? '#1877f2' : '#38bdf8' }}>cat</code>, <code style={{ color: isLight ? '#1877f2' : '#38bdf8' }}>touch</code>) and run Git commands with live reactive visual animations.
          </p>
        </div>
      </div>

      {/* Primary Navigation Tabs */}
      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(135px, 1fr))', gap: 6, marginBottom: 16, width: '100%', minWidth: 0 }}>
        {[
          { id: 'all-terminal', title: '💻 Shell & Terminal', level: 'Every Command', color: isLight ? '#1877f2' : '#38bdf8' },
          { id: 'snapshots', title: '📄 3-Trees & Staging', level: 'add / commit / diff', color: isLight ? '#16a34a' : '#10b981' },
          { id: 'branching', title: '🌿 Branching & Merges', level: 'branch / switch / merge', color: isLight ? '#d97706' : '#f59e0b' },
          { id: 'undo-rebase', title: '⚡ Rebase & Stash', level: 'rebase / reset / cherry-pick', color: isLight ? '#e1306c' : '#ec4899' },
          { id: 'remotes-sync', title: '☁️ Remote Sync', level: 'fetch / pull / push', color: isLight ? '#7c3aed' : '#8b5cf6' },
          { id: 'github-pr', title: '🔀 Pull Requests', level: 'PRs & Code Review', color: isLight ? '#4f46e5' : '#6366f1' },
          { id: 'github-actions', title: '🚀 GitHub Actions', level: 'CI/CD Matrix', color: isLight ? '#0284c7' : '#06b6d4' }
        ].map((tab) => {
          const isActive = activeTab === tab.id;
          return (
            <button
              key={tab.id}
              onClick={() => setActiveTab(tab.id)}
              style={{
                background: isActive ? (isLight ? '#e7f3ff' : '#1e293b') : (isLight ? '#ffffff' : '#0b1120'),
                border: isActive ? (isLight ? '2px solid #1877f2' : `2px solid ${tab.color}`) : (isLight ? '1px solid #e4e6eb' : '1px solid #1e293b'),
                padding: '9px 12px',
                borderRadius: '8px',
                textAlign: 'left',
                cursor: 'pointer',
                transition: 'all 0.15s ease',
                boxShadow: isActive ? (isLight ? '0 2px 8px rgba(24, 119, 242, 0.2)' : `0 0 12px ${tab.color}33`) : (isLight ? '0 1px 2px rgba(0,0,0,0.04)' : 'none'),
                minWidth: 0
              }}
            >
              <div style={{ fontSize: '0.65rem', fontWeight: 800, color: tab.color, textTransform: 'uppercase', letterSpacing: '0.04em' }}>{tab.level}</div>
              <div style={{ fontSize: '0.78rem', fontWeight: 700, color: isLight ? (isActive ? '#1877f2' : '#050505') : '#f8fafc', marginTop: 2, whiteSpace: 'nowrap', overflow: 'hidden', textOverflow: 'ellipsis' }}>{tab.title}</div>
            </button>
          );
        })}
      </div>

      {/* Quick Interactive Command Dispatcher Bar */}
      <div style={{ padding: '12px 16px', marginBottom: 16, background: isLight ? '#ffffff' : '#0b1120', border: isLight ? '1px solid #e4e6eb' : '1px solid #1e293b', borderRadius: '10px', width: '100%', minWidth: 0, boxSizing: 'border-box', boxShadow: isLight ? '0 1px 3px rgba(0,0,0,0.06)' : 'none' }}>
        <div style={{ fontSize: '0.78rem', fontWeight: 700, color: isLight ? '#65676b' : '#94a3b8', marginBottom: 8, display: 'flex', alignItems: 'center', gap: 6 }}>
          <Sparkles size={14} color={isLight ? '#1877f2' : '#38bdf8'} /> Click any shell or git command pill to execute:
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
                background: isLight ? '#f0f2f5' : '#131d31',
                border: isLight ? '1px solid #d8dadf' : '1px solid #0284c7',
                padding: '4px 10px',
                borderRadius: '6px',
                color: isLight ? '#1877f2' : '#38bdf8',
                cursor: 'pointer',
                transition: 'all 0.15s ease'
              }}
              onMouseEnter={(e) => {
                e.currentTarget.style.background = isLight ? '#1877f2' : '#0284c7';
                e.currentTarget.style.color = '#ffffff';
              }}
              onMouseLeave={(e) => {
                e.currentTarget.style.background = isLight ? '#f0f2f5' : '#131d31';
                e.currentTarget.style.color = isLight ? '#1877f2' : '#38bdf8';
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
          <div style={{ padding: '18px 20px', background: isLight ? '#ffffff' : '#070b14', border: isLight ? '1px solid #e4e6eb' : '1px solid #1e293b', borderRadius: '12px', width: '100%', minWidth: 0, boxSizing: 'border-box', boxShadow: isLight ? '0 2px 12px rgba(0,0,0,0.06)' : '0 8px 30px rgba(0,0,0,0.6)' }}>
            
            {/* Stage Info Header */}
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', flexWrap: 'wrap', gap: 10, marginBottom: 12, width: '100%' }}>
              <div style={{ display: 'flex', alignItems: 'center', gap: 10, flexWrap: 'wrap' }}>
                <div style={{ padding: '6px 12px', borderRadius: '8px', background: isLight ? '#e7f3ff' : 'rgba(56, 189, 248, 0.15)', border: isLight ? '1px solid #1877f2' : '1px solid #38bdf8', display: 'flex', alignItems: 'center', gap: 6 }}>
                  <Sparkles size={15} color={isLight ? '#1877f2' : '#38bdf8'} />
                  <span style={{ fontSize: '0.85rem', fontWeight: 800, color: isLight ? '#050505' : '#f8fafc' }}>
                    Live Stage:
                  </span>
                  <span style={{ fontSize: '0.85rem', fontWeight: 800, color: isLight ? '#1877f2' : (SIMULATION_VIEWS.find(v => v.id === activeSimView)?.color || '#38bdf8') }}>
                    {SIMULATION_VIEWS.find(v => v.id === activeSimView)?.label}
                  </span>
                </div>

                <div style={{ background: isLight ? '#f0f2f5' : '#1e293b', border: isLight ? '1px solid #e4e6eb' : '1px solid #334155', padding: '5px 12px', borderRadius: '8px', fontSize: '0.8rem', color: isLight ? '#65676b' : '#f8fafc', fontWeight: 600 }}>
                  Active Branch: <strong style={{ color: isLight ? '#1877f2' : '#38bdf8', fontWeight: 800 }}>{currentBranch}</strong>
                </div>

                <div style={{ background: isLight ? '#f0f2f5' : '#1e293b', border: isLight ? '1px solid #e4e6eb' : '1px solid #334155', padding: '5px 12px', borderRadius: '8px', fontSize: '0.8rem', color: isLight ? '#65676b' : '#f8fafc', fontWeight: 600 }}>
                  PWD: <strong style={{ color: isLight ? '#16a34a' : '#34d399', fontFamily: 'monospace' }}>/workspace{currentDir ? `/${currentDir}` : ''}</strong>
                </div>
              </div>
            </div>

            {/* Simulation View Switcher Pills */}
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
                      background: isCurrent ? (isLight ? '#1877f2' : v.color) : (isLight ? '#f0f2f5' : '#131d31'),
                      color: isCurrent ? '#ffffff' : (isLight ? '#050505' : '#e2e8f0'),
                      border: isCurrent ? (isLight ? '1px solid #1877f2' : `1px solid ${v.color}`) : (isLight ? '1px solid #e4e6eb' : '1px solid #334155'),
                      boxShadow: isCurrent ? (isLight ? '0 2px 8px rgba(24, 119, 242, 0.3)' : `0 0 14px ${v.glow}`) : 'none',
                      cursor: 'pointer',
                      transition: 'all 0.15s ease'
                    }}
                  >
                    <Icon size={13} color={isCurrent ? '#ffffff' : (isLight ? '#1877f2' : v.color)} />
                    {v.label}
                  </button>
                );
              })}
            </div>

            {/* Dynamic Status Alert Message Banner */}
            <div style={{ padding: '10px 14px', borderRadius: '8px', background: isLight ? '#f0f2f5' : '#0f1d36', border: isLight ? '1px solid #e4e6eb' : '1px solid #1e3a5f', marginBottom: 16, display: 'flex', alignItems: 'center', gap: 8, fontSize: '0.82rem', color: isLight ? '#050505' : '#f8fafc', wordBreak: 'break-word' }}>
              <span style={{ color: isLight ? '#1877f2' : '#38bdf8', fontWeight: 800, whiteSpace: 'nowrap' }}>⚡ Last Action:</span>
              <span style={{ flex: 1, minWidth: 0, fontWeight: 600 }}>{simAlertMsg}</span>
            </div>

            {/* VIEW 1: INTERACTIVE GITHUB COMMITS & DAG GRAPH CANVAS */}
            {activeSimView === 'dag' && (() => {
              const filteredCommits = commits.filter(c => {
                if (commitFilterBranch !== 'all' && c.branch !== commitFilterBranch) return false;
                return true;
              });

              const activeCommit = commits.find(c => c.hash === selectedCommitHash) || commits[commits.length - 1];

              return (
                <div style={{ display: 'flex', flexDirection: 'column', gap: 14, width: '100%', minWidth: 0 }}>
                  {/* Commits Navigation & View Controls Bar */}
                  <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', flexWrap: 'wrap', gap: 8, padding: '8px 12px', background: isLight ? '#f0f2f5' : '#131d31', borderRadius: '8px', border: isLight ? '1px solid #e4e6eb' : '1px solid #1e293b' }}>
                    {/* Branch Filter Pills */}
                    <div style={{ display: 'flex', alignItems: 'center', gap: 6, flexWrap: 'wrap' }}>
                      <span style={{ fontSize: '0.75rem', fontWeight: 800, color: isLight ? '#65676b' : '#94a3b8', display: 'flex', alignItems: 'center', gap: 4 }}>
                        <GitBranch size={13} /> Branch:
                      </span>
                      {['all', ...branches].map(b => (
                        <button
                          key={b}
                          onClick={() => setCommitFilterBranch(b)}
                          style={{
                            padding: '3px 9px',
                            borderRadius: '6px',
                            fontSize: '0.72rem',
                            fontWeight: 700,
                            border: commitFilterBranch === b ? (isLight ? '1px solid #1877f2' : '1px solid #38bdf8') : (isLight ? '1px solid #d8dadf' : '1px solid #334155'),
                            background: commitFilterBranch === b ? (isLight ? '#1877f2' : '#1e3a5f') : (isLight ? '#ffffff' : '#0b1120'),
                            color: commitFilterBranch === b ? '#ffffff' : (isLight ? '#050505' : '#cbd5e1'),
                            cursor: 'pointer'
                          }}
                        >
                          {b === 'all' ? `All (${commits.length})` : b}
                        </button>
                      ))}
                    </div>

                    {/* View Mode Toggle: Visual DAG vs GitHub Feed */}
                    <div style={{ display: 'flex', alignItems: 'center', gap: 4, background: isLight ? '#ffffff' : '#0b1120', padding: '3px', borderRadius: '6px', border: isLight ? '1px solid #d8dadf' : '1px solid #1e293b' }}>
                      <button
                        onClick={() => setCommitViewMode('graph')}
                        style={{
                          padding: '3px 10px',
                          borderRadius: '4px',
                          fontSize: '0.72rem',
                          fontWeight: 700,
                          border: 'none',
                          background: commitViewMode === 'graph' ? (isLight ? '#e7f3ff' : '#1e293b') : 'transparent',
                          color: commitViewMode === 'graph' ? (isLight ? '#1877f2' : '#38bdf8') : (isLight ? '#65676b' : '#94a3b8'),
                          cursor: 'pointer',
                          display: 'flex',
                          alignItems: 'center',
                          gap: 4
                        }}
                      >
                        <GitCommit size={13} /> Visual Graph
                      </button>
                      <button
                        onClick={() => setCommitViewMode('feed')}
                        style={{
                          padding: '3px 10px',
                          borderRadius: '4px',
                          fontSize: '0.72rem',
                          fontWeight: 700,
                          border: 'none',
                          background: commitViewMode === 'feed' ? (isLight ? '#e7f3ff' : '#1e293b') : 'transparent',
                          color: commitViewMode === 'feed' ? (isLight ? '#1877f2' : '#38bdf8') : (isLight ? '#65676b' : '#94a3b8'),
                          cursor: 'pointer',
                          display: 'flex',
                          alignItems: 'center',
                          gap: 4
                        }}
                      >
                        <FileText size={13} /> GitHub Commits Feed
                      </button>
                    </div>
                  </div>

                  {/* MODE A: VISUAL DAG GRAPH NODES WITH TREE BRANCH RAILS */}
                  {commitViewMode === 'graph' && (() => {
                    const uniqueBranches = ['main', ...branches.filter(b => b !== 'main')];
                    const laneHeight = 115;
                    const colWidth = 235;
                    const startX = 145; // left rail for branch pill labels

                    // Calculate 2D position (x, y) for every commit
                    const commitMap = {};
                    const positionedCommits = filteredCommits.map((c, idx) => {
                      let laneIdx = uniqueBranches.indexOf(c.branch);
                      if (laneIdx === -1) laneIdx = 0;
                      const x = idx * colWidth + startX;
                      const y = laneIdx * laneHeight + 65;
                      const pos = { ...c, idx, x, y, laneIdx };
                      commitMap[c.hash] = pos;
                      commitMap[c.id] = pos;
                      return pos;
                    });

                    const canvasWidth = Math.max(820, positionedCommits.length * colWidth + startX + 60);
                    const canvasHeight = Math.max(220, uniqueBranches.length * laneHeight + 35);

                    return (
                      <div style={{ width: '100%', minWidth: 0, overflowX: 'auto', background: isLight ? '#fcfcfd' : '#070b14', borderRadius: '10px', border: isLight ? '1px solid #e4e6eb' : '1px solid #1e293b', padding: '12px 10px', boxSizing: 'border-box' }}>
                        <div style={{ position: 'relative', width: canvasWidth, height: canvasHeight, minHeight: '180px' }}>
                          
                          {/* SVG Background Layer for Curved Tree Branch Rails & Connectors */}
                          <svg style={{ position: 'absolute', top: 0, left: 0, width: canvasWidth, height: canvasHeight, pointerEvents: 'none' }}>
                            {/* 1. Horizontal Rail Guides for Each Branch */}
                            {uniqueBranches.map((bName, lIdx) => {
                              const bTheme = getBranchStyle(bName);
                              const laneY = lIdx * laneHeight + 65;
                              return (
                                <g key={`lane-${bName}`}>
                                  <line
                                    x1={startX - 15}
                                    y1={laneY}
                                    x2={canvasWidth - 20}
                                    y2={laneY}
                                    stroke={bTheme.color}
                                    strokeWidth="2"
                                    strokeDasharray="4 6"
                                    opacity={isLight ? 0.35 : 0.25}
                                  />
                                </g>
                              );
                            })}

                            {/* 2. Commit Connector Lines (Parent to Child & Merges) */}
                            {positionedCommits.map((c) => {
                              const parentCommit = c.parent ? (commitMap[c.parent] || positionedCommits.find(p => p.hash === c.parent || p.id === c.parent)) : null;
                              const cTheme = getBranchStyle(c.branch);
                              const isMerge = c.message.toLowerCase().startsWith('merge');

                              return (
                                <g key={`lines-${c.id}`}>
                                  {/* Direct Parent Connection */}
                                  {parentCommit && (
                                    parentCommit.laneIdx === c.laneIdx ? (
                                      // Straight horizontal branch connection
                                      <line
                                        x1={parentCommit.x + 85}
                                        y1={parentCommit.y}
                                        x2={c.x - 85}
                                        y2={c.y}
                                        stroke={cTheme.color}
                                        strokeWidth="3.5"
                                        strokeLinecap="round"
                                      />
                                    ) : (
                                      // Smooth S-Curve Branching Out from Parent
                                      <path
                                        d={`M ${parentCommit.x + 40} ${parentCommit.y} C ${parentCommit.x + 110} ${parentCommit.y}, ${c.x - 110} ${c.y}, ${c.x - 85} ${c.y}`}
                                        fill="none"
                                        stroke={cTheme.color}
                                        strokeWidth="3.5"
                                        strokeLinecap="round"
                                      />
                                    )
                                  )}

                                  {/* Merge Curve (from another branch back into current) */}
                                  {isMerge && (
                                    <path
                                      d={`M ${c.x - 170} ${c.laneIdx === 0 ? 180 : 65} C ${c.x - 90} ${c.laneIdx === 0 ? 180 : 65}, ${c.x - 60} ${c.y}, ${c.x - 85} ${c.y}`}
                                      fill="none"
                                      stroke="#8b5cf6"
                                      strokeWidth="2.5"
                                      strokeDasharray="5 5"
                                      strokeLinecap="round"
                                    />
                                  )}
                                </g>
                              );
                            })}
                          </svg>

                          {/* 3. Sticky / Left-Aligned Branch Name Rails */}
                          {uniqueBranches.map((bName, lIdx) => {
                            const bTheme = getBranchStyle(bName);
                            const laneY = lIdx * laneHeight + 65;
                            const isCurrent = currentBranch === bName;

                            return (
                              <div
                                key={`label-${bName}`}
                                style={{
                                  position: 'absolute',
                                  left: 6,
                                  top: laneY - 18,
                                  zIndex: 3,
                                  background: isCurrent ? (isLight ? '#1877f2' : '#1e3a5f') : (isLight ? '#ffffff' : '#131d31'),
                                  color: isCurrent ? '#ffffff' : bTheme.color,
                                  border: `1.5px solid ${bTheme.color}`,
                                  padding: '4px 10px',
                                  borderRadius: '16px',
                                  fontSize: '0.72rem',
                                  fontWeight: 800,
                                  display: 'flex',
                                  alignItems: 'center',
                                  gap: 5,
                                  boxShadow: isCurrent ? (isLight ? '0 2px 8px rgba(24, 119, 242, 0.3)' : '0 0 12px rgba(56, 189, 248, 0.4)') : 'none'
                                }}
                              >
                                <GitBranch size={12} />
                                <span>{bName}</span>
                                {isCurrent && <span style={{ fontSize: '0.62rem', background: '#ffffff', color: '#1877f2', padding: '1px 5px', borderRadius: '8px', fontWeight: 900 }}>HEAD</span>}
                              </div>
                            );
                          })}

                          {/* 4. Positioned Commit Cards along the Rails */}
                          {positionedCommits.map((c) => {
                            const isHead = (c.branch === currentBranch && c.idx === positionedCommits.map(x => x.branch).lastIndexOf(currentBranch)) || currentBranch === c.hash;
                            const isSelected = activeCommit?.hash === c.hash;
                            const hasTag = tags.find(t => t.commitHash === c.hash);
                            const bTheme = getBranchStyle(c.branch);

                            return (
                              <div
                                key={c.id}
                                onClick={() => setSelectedCommitHash(c.hash)}
                                style={{
                                  position: 'absolute',
                                  left: c.x - 85,
                                  top: c.y - 42,
                                  width: '180px',
                                  zIndex: isSelected ? 10 : 4,
                                  background: isSelected ? (isLight ? '#ffffff' : '#1a2744') : (isLight ? '#ffffff' : (c.branch === 'main' ? '#131d31' : '#1e1b4b')),
                                  border: isSelected ? (isLight ? '2px solid #1877f2' : '2px solid #38bdf8') : isHead ? `2px dashed ${bTheme.color}` : (isLight ? '1px solid #e4e6eb' : `1px solid ${bTheme.border}`),
                                  padding: '10px 12px',
                                  borderRadius: '10px',
                                  boxShadow: isSelected ? (isLight ? '0 4px 18px rgba(24, 119, 242, 0.25)' : '0 0 20px rgba(56, 189, 248, 0.45)') : (isLight ? '0 1px 3px rgba(0,0,0,0.06)' : 'none'),
                                  cursor: 'pointer',
                                  transition: 'all 0.15s ease'
                                }}
                              >
                                <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: 4 }}>
                                  <div style={{ display: 'flex', alignItems: 'center', gap: 4 }}>
                                    <span style={{ fontFamily: 'monospace', fontSize: '0.78rem', color: isLight ? '#d97706' : '#fbbf24', fontWeight: 800 }}>#{c.hash}</span>
                                    {c.verified && (
                                      <span title="GPG Key Verified Commit" style={{ fontSize: '0.65rem', color: '#16a34a', display: 'flex', alignItems: 'center' }}>
                                        <ShieldCheck size={11} />
                                      </span>
                                    )}
                                  </div>
                                  <span style={{ fontSize: '0.62rem', padding: '2px 6px', borderRadius: '4px', background: bTheme.bg, color: bTheme.color, fontWeight: 700, border: `1px solid ${bTheme.color}33` }}>
                                    {c.branch}
                                  </span>
                                </div>

                                <div style={{ fontSize: '0.8rem', fontWeight: 700, color: isLight ? '#050505' : '#ffffff', whiteSpace: 'nowrap', overflow: 'hidden', textOverflow: 'ellipsis', marginBottom: 4 }}>
                                  {c.message}
                                </div>

                                <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', fontSize: '0.7rem', color: isLight ? '#65676b' : '#94a3b8' }}>
                                  <span>{c.avatar || '👨‍💻'} {c.author}</span>
                                  {isHead && <span style={{ color: isLight ? '#1877f2' : '#38bdf8', fontWeight: 800 }}>HEAD ➔</span>}
                                </div>

                                {hasTag && (
                                  <div style={{ position: 'absolute', top: -9, right: 8, background: 'linear-gradient(45deg, #f09433, #e1306c)', color: '#ffffff', fontSize: '0.6rem', fontWeight: 900, padding: '2px 6px', borderRadius: '4px', boxShadow: '0 2px 6px rgba(0,0,0,0.2)' }}>
                                    🏷️ {hasTag.name}
                                  </div>
                                )}
                              </div>
                            );
                          })}
                        </div>
                      </div>
                    );
                  })()}

                  {/* MODE B: GITHUB COMMITS FEED TIMELINE */}
                  {commitViewMode === 'feed' && (
                    <div style={{ background: isLight ? '#ffffff' : '#0b1120', border: isLight ? '1px solid #e4e6eb' : '1px solid #1e293b', borderRadius: '8px', overflow: 'hidden', width: '100%' }}>
                      <div style={{ padding: '10px 14px', background: isLight ? '#f0f2f5' : '#131d31', borderBottom: isLight ? '1px solid #e4e6eb' : '1px solid #1e293b', fontSize: '0.78rem', fontWeight: 800, color: isLight ? '#050505' : '#f8fafc', display: 'flex', alignItems: 'center', gap: 6 }}>
                        <GitCommit size={14} color={isLight ? '#1877f2' : '#38bdf8'} />
                        Commits on repository branch: <strong style={{ color: isLight ? '#1877f2' : '#38bdf8' }}>{commitFilterBranch === 'all' ? currentBranch : commitFilterBranch}</strong>
                      </div>

                      <div style={{ display: 'flex', flexDirection: 'column' }}>
                        {filteredCommits.slice().reverse().map((c, idx) => {
                          const isSelected = activeCommit?.hash === c.hash;
                          return (
                            <div
                              key={c.id || idx}
                              onClick={() => setSelectedCommitHash(c.hash)}
                              style={{
                                padding: '12px 16px',
                                borderBottom: idx < filteredCommits.length - 1 ? (isLight ? '1px solid #e4e6eb' : '1px solid #1e293b') : 'none',
                                background: isSelected ? (isLight ? '#e7f3ff' : 'rgba(56, 189, 248, 0.1)') : (isLight ? '#ffffff' : 'transparent'),
                                display: 'flex',
                                justifyContent: 'space-between',
                                alignItems: 'center',
                                flexWrap: 'wrap',
                                gap: 10,
                                cursor: 'pointer',
                                transition: 'background 0.15s ease'
                              }}
                            >
                              <div style={{ display: 'flex', alignItems: 'flex-start', gap: 10, minWidth: 0, flex: 1 }}>
                                <div style={{ fontSize: '1.2rem', marginTop: 2 }}>{c.avatar || '👨‍💻'}</div>
                                <div style={{ minWidth: 0, flex: 1 }}>
                                  <div style={{ display: 'flex', alignItems: 'center', gap: 8, flexWrap: 'wrap' }}>
                                    <span style={{ fontSize: '0.85rem', fontWeight: 800, color: isLight ? '#050505' : '#ffffff' }}>
                                      {c.message}
                                    </span>
                                    {c.verified && (
                                      <span style={{ fontSize: '0.65rem', padding: '1px 6px', borderRadius: '4px', background: isLight ? '#e6ffec' : 'rgba(16, 185, 129, 0.2)', color: '#16a34a', border: '1px solid #16a34a', fontWeight: 700, display: 'flex', alignItems: 'center', gap: 3 }}>
                                        <ShieldCheck size={11} /> Verified
                                      </span>
                                    )}
                                    <span style={{ fontSize: '0.68rem', padding: '1px 6px', borderRadius: '4px', background: isLight ? '#f0f2f5' : '#1e293b', color: isLight ? '#1877f2' : '#38bdf8', fontWeight: 700 }}>
                                      {c.branch}
                                    </span>
                                  </div>
                                  <div style={{ fontSize: '0.75rem', color: isLight ? '#65676b' : '#94a3b8', marginTop: 4 }}>
                                    <strong>{c.author}</strong> committed <span style={{ color: isLight ? '#65676b' : '#cbd5e1' }}>{c.time || 'recently'}</span>
                                    {c.filesChanged && (
                                      <span style={{ marginLeft: 8, color: isLight ? '#1877f2' : '#38bdf8' }}>
                                        • {c.filesChanged.length} file(s) changed
                                      </span>
                                    )}
                                  </div>
                                </div>
                              </div>

                              {/* Commit SHA & Direct Action Buttons */}
                              <div style={{ display: 'flex', alignItems: 'center', gap: 6 }}>
                                <button
                                  onClick={(e) => {
                                    e.stopPropagation();
                                    navigator.clipboard?.writeText(c.hash);
                                    setCopiedHash(c.hash);
                                    setTimeout(() => setCopiedHash(''), 2000);
                                  }}
                                  style={{
                                    fontFamily: 'monospace',
                                    fontSize: '0.72rem',
                                    fontWeight: 700,
                                    padding: '4px 8px',
                                    borderRadius: '5px',
                                    background: isLight ? '#f0f2f5' : '#131d31',
                                    border: isLight ? '1px solid #d8dadf' : '1px solid #334155',
                                    color: isLight ? '#050505' : '#cbd5e1',
                                    cursor: 'pointer',
                                    display: 'flex',
                                    alignItems: 'center',
                                    gap: 4
                                  }}
                                  title="Copy SHA"
                                >
                                  <Copy size={11} /> {copiedHash === c.hash ? 'Copied!' : c.hash}
                                </button>

                                <button
                                  onClick={(e) => {
                                    e.stopPropagation();
                                    executeGitCommand(`git checkout ${c.hash}`);
                                  }}
                                  style={{
                                    fontSize: '0.7rem',
                                    fontWeight: 700,
                                    padding: '4px 8px',
                                    borderRadius: '5px',
                                    background: isLight ? '#1877f2' : '#0284c7',
                                    color: '#ffffff',
                                    border: 'none',
                                    cursor: 'pointer'
                                  }}
                                >
                                  Checkout
                                </button>
                              </div>
                            </div>
                          );
                        })}
                      </div>
                    </div>
                  )}

                  {/* DEEP INTERACTIVE COMMIT INSPECTOR CARD */}
                  {activeCommit && (
                    <div style={{ background: isLight ? '#ffffff' : '#0e1726', border: isLight ? '1px solid #1877f2' : '1px solid #0284c7', borderRadius: '10px', padding: '14px 16px', width: '100%', boxSizing: 'border-box', boxShadow: isLight ? '0 2px 8px rgba(24, 119, 242, 0.08)' : '0 4px 20px rgba(0,0,0,0.4)' }}>
                      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', flexWrap: 'wrap', gap: 10, borderBottom: isLight ? '1px solid #e4e6eb' : '1px solid #1e293b', paddingBottom: 12 }}>
                        <div>
                          <div style={{ display: 'flex', alignItems: 'center', gap: 8, flexWrap: 'wrap', marginBottom: 4 }}>
                            <span style={{ fontSize: '0.75rem', fontWeight: 800, color: isLight ? '#1877f2' : '#38bdf8', textTransform: 'uppercase', letterSpacing: '0.04em' }}>
                              Interactive GitHub Commit Inspector
                            </span>
                            <span style={{ fontFamily: 'monospace', fontSize: '0.78rem', background: isLight ? '#e7f3ff' : '#1e3a5f', color: isLight ? '#1877f2' : '#38bdf8', padding: '2px 8px', borderRadius: '4px', fontWeight: 800 }}>
                              commit {activeCommit.hash}
                            </span>
                            {activeCommit.verified && (
                              <span style={{ fontSize: '0.68rem', padding: '2px 7px', borderRadius: '4px', background: isLight ? '#e6ffec' : 'rgba(16, 185, 129, 0.2)', color: '#16a34a', border: '1px solid #16a34a', fontWeight: 700, display: 'flex', alignItems: 'center', gap: 4 }}>
                                <ShieldCheck size={12} /> Verified GPG Signature
                              </span>
                            )}
                          </div>

                          <h3 style={{ fontSize: '1.05rem', fontWeight: 800, color: isLight ? '#050505' : '#ffffff', margin: '4px 0 6px 0' }}>
                            {activeCommit.message}
                          </h3>

                          <div style={{ fontSize: '0.78rem', color: isLight ? '#65676b' : '#94a3b8', display: 'flex', alignItems: 'center', gap: 8, flexWrap: 'wrap' }}>
                            <span><strong>{activeCommit.author}</strong> ({activeCommit.email || 'alex@example.com'})</span>
                            <span>• Authored {activeCommit.time || 'recently'}</span>
                            {activeCommit.parent && (
                              <span>• Parent: <button onClick={() => setSelectedCommitHash(activeCommit.parent)} style={{ background: 'none', border: 'none', color: isLight ? '#1877f2' : '#38bdf8', fontFamily: 'monospace', fontWeight: 700, cursor: 'pointer', padding: 0 }}>{activeCommit.parent}</button></span>
                            )}
                          </div>
                        </div>

                        {/* Interactive Git Action Buttons */}
                        <div style={{ display: 'flex', gap: 6, flexWrap: 'wrap' }}>
                          <button
                            onClick={() => executeGitCommand(`git checkout ${activeCommit.hash}`)}
                            style={{ background: isLight ? '#1877f2' : '#0284c7', color: '#ffffff', border: 'none', padding: '5px 10px', borderRadius: '6px', fontSize: '0.72rem', fontWeight: 700, cursor: 'pointer', display: 'flex', alignItems: 'center', gap: 4 }}
                          >
                            👉 git checkout {activeCommit.hash}
                          </button>
                          <button
                            onClick={() => executeGitCommand(`git revert ${activeCommit.hash}`)}
                            style={{ background: isLight ? '#f0f2f5' : '#1e293b', color: isLight ? '#fa383e' : '#fb7185', border: isLight ? '1px solid #d8dadf' : '1px solid #fa383e', padding: '5px 10px', borderRadius: '6px', fontSize: '0.72rem', fontWeight: 700, cursor: 'pointer', display: 'flex', alignItems: 'center', gap: 4 }}
                          >
                            <RotateCcw size={12} /> git revert
                          </button>
                          <button
                            onClick={() => executeGitCommand(`git cherry-pick ${activeCommit.hash}`)}
                            style={{ background: isLight ? '#f0f2f5' : '#1e293b', color: isLight ? '#7c3aed' : '#a78bfa', border: isLight ? '1px solid #d8dadf' : '1px solid #8b5cf6', padding: '5px 10px', borderRadius: '6px', fontSize: '0.72rem', fontWeight: 700, cursor: 'pointer', display: 'flex', alignItems: 'center', gap: 4 }}
                          >
                            <RefreshCw size={12} /> git cherry-pick
                          </button>
                        </div>
                      </div>

                      {/* Files Changed & Diff Preview */}
                      <div style={{ marginTop: 12 }}>
                        <div style={{ fontSize: '0.78rem', fontWeight: 700, color: isLight ? '#050505' : '#f8fafc', marginBottom: 8, display: 'flex', alignItems: 'center', justifyContent: 'space-between' }}>
                          <span>Showing {(activeCommit.filesChanged || []).length} changed file(s):</span>
                          <span style={{ color: '#16a34a', fontSize: '0.75rem' }}>+22 / -3 lines</span>
                        </div>

                        <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(200px, 1fr))', gap: 8, marginBottom: 10 }}>
                          {(activeCommit.filesChanged || [
                            { file: 'src/auth/jwt.py', additions: 14, deletions: 3 },
                            { file: 'config/database.env', additions: 8, deletions: 0 }
                          ]).map((f, fIdx) => (
                            <div key={fIdx} style={{ padding: '6px 10px', background: isLight ? '#f0f2f5' : '#0b1120', borderRadius: '6px', border: isLight ? '1px solid #e4e6eb' : '1px solid #1e293b', display: 'flex', justifyContent: 'space-between', alignItems: 'center', fontSize: '0.75rem' }}>
                              <span style={{ fontFamily: 'monospace', color: isLight ? '#050505' : '#ffffff', overflow: 'hidden', textOverflow: 'ellipsis', whiteSpace: 'nowrap' }}>📄 {f.file}</span>
                              <span style={{ display: 'flex', gap: 4, fontWeight: 700 }}>
                                <span style={{ color: '#16a34a' }}>+{f.additions}</span>
                                <span style={{ color: '#fa383e' }}>-{f.deletions}</span>
                              </span>
                            </div>
                          ))}
                        </div>

                        {/* Interactive Diff Hunk Preview */}
                        <div style={{ background: isLight ? '#f8f9fa' : '#070b14', border: isLight ? '1px solid #e4e6eb' : '1px solid #1e293b', borderRadius: '6px', padding: '10px 12px', fontFamily: 'JetBrains Mono, monospace', fontSize: '0.75rem', lineHeight: 1.5, overflowX: 'auto' }}>
                          <div style={{ color: isLight ? '#65676b' : '#94a3b8', fontWeight: 700, marginBottom: 4 }}>
                            {activeCommit.diffSnippet ? activeCommit.diffSnippet.split('\n')[0] : '+++ b/src/auth/jwt.py'}
                          </div>
                          <div style={{ background: isLight ? '#e6ffec' : 'rgba(16, 185, 129, 0.15)', color: isLight ? '#16a34a' : '#34d399', padding: '2px 4px', borderRadius: '3px' }}>
                            + import jwt, os, hashlib
                          </div>
                          <div style={{ background: isLight ? '#e6ffec' : 'rgba(16, 185, 129, 0.15)', color: isLight ? '#16a34a' : '#34d399', padding: '2px 4px', borderRadius: '3px' }}>
                            + def verify_session_token(token: str): return jwt.decode(token, SECRET)
                          </div>
                          <div style={{ background: isLight ? '#ffebe9' : 'rgba(244, 63, 94, 0.15)', color: isLight ? '#fa383e' : '#fb7185', padding: '2px 4px', borderRadius: '3px' }}>
                            - def legacy_auth_check(user): pass
                          </div>
                        </div>
                      </div>
                    </div>
                  )}
                </div>
              );
            })()}

            {/* VIEW 2: 3-TREES STAGING INSPECTOR (Shows accurate working directory files) */}
            {activeSimView === 'staging-trees' && (
              <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(210px, 1fr))', gap: 14, width: '100%', minWidth: 0 }}>
                {/* 1. Working Directory */}
                <div style={{ background: isLight ? '#ffffff' : '#131d31', padding: 14, borderRadius: '10px', border: isLight ? '1px solid #fa383e' : '1px solid #f43f5e', minWidth: 0, boxShadow: isLight ? '0 1px 3px rgba(0,0,0,0.06)' : 'none' }}>
                  <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: 10 }}>
                    <span style={{ fontWeight: 800, fontSize: '0.85rem', color: '#fa383e', display: 'flex', alignItems: 'center', gap: 5 }}>
                      <FileCode size={15} /> 1. Working Directory
                    </span>
                    <button onClick={() => executeGitCommand('git add .')} style={{ background: '#fa383e', color: '#ffffff', border: 'none', padding: '4px 10px', borderRadius: '5px', fontWeight: 700, fontSize: '0.72rem', cursor: 'pointer' }}>
                      + git add .
                    </button>
                  </div>
                  <div style={{ display: 'flex', flexDirection: 'column', gap: 6 }}>
                    {workingFiles.map((f, idx) => (
                      <div key={idx} style={{ padding: '8px 10px', background: isLight ? '#f0f2f5' : '#0b1120', borderRadius: '6px', fontSize: '0.78rem', display: 'flex', justifyContent: 'space-between', alignItems: 'center', border: isLight ? '1px solid #e4e6eb' : '1px solid #1e293b' }}>
                        <span style={{ overflow: 'hidden', textOverflow: 'ellipsis', whiteSpace: 'nowrap', color: isLight ? '#050505' : '#f8fafc', fontWeight: 600 }}>📄 {f.name}</span>
                        <div style={{ display: 'flex', alignItems: 'center', gap: 6 }}>
                          <span style={{ color: f.status === 'clean' ? '#42b72a' : '#fa383e', fontWeight: 800, fontSize: '0.72rem', textTransform: 'uppercase' }}>{f.status}</span>
                          {f.status !== 'clean' && (
                            <button onClick={() => executeGitCommand(`git add ${f.name}`)} style={{ background: '#1877f2', color: '#fff', border: 'none', padding: '2px 6px', borderRadius: '4px', fontSize: '0.65rem', fontWeight: 700, cursor: 'pointer' }}>
                              + stage
                            </button>
                          )}
                        </div>
                      </div>
                    ))}
                  </div>
                </div>

                {/* 2. Staging Index */}
                <div style={{ background: isLight ? '#ffffff' : '#131d31', padding: 14, borderRadius: '10px', border: isLight ? '1px solid #42b72a' : '1px solid #10b981', minWidth: 0, boxShadow: isLight ? '0 1px 3px rgba(0,0,0,0.06)' : 'none' }}>
                  <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: 10 }}>
                    <span style={{ fontWeight: 800, fontSize: '0.85rem', color: '#42b72a', display: 'flex', alignItems: 'center', gap: 5 }}>
                      <Layers size={15} /> 2. Staging Index
                    </span>
                    <button onClick={() => executeGitCommand('git reset')} disabled={stagedFiles.length === 0} style={{ background: isLight ? '#f0f2f5' : '#1e293b', color: isLight ? '#050505' : '#e2e8f0', border: isLight ? '1px solid #d8dadf' : '1px solid #475569', padding: '4px 10px', borderRadius: '5px', fontWeight: 700, fontSize: '0.72rem', cursor: 'pointer', opacity: stagedFiles.length === 0 ? 0.5 : 1 }}>
                      git reset
                    </button>
                  </div>
                  <div style={{ display: 'flex', flexDirection: 'column', gap: 6 }}>
                    {stagedFiles.map((f, idx) => (
                      <div key={idx} style={{ padding: '8px 10px', background: isLight ? '#f0f2f5' : '#0b1120', borderRadius: '6px', fontSize: '0.78rem', display: 'flex', justifyContent: 'space-between', alignItems: 'center', border: isLight ? '1px solid #e4e6eb' : '1px solid #1e293b' }}>
                        <span style={{ overflow: 'hidden', textOverflow: 'ellipsis', whiteSpace: 'nowrap', color: isLight ? '#050505' : '#f8fafc', fontWeight: 600 }}>✓ {f.name}</span>
                        <div style={{ display: 'flex', alignItems: 'center', gap: 6 }}>
                          <span style={{ color: '#42b72a', fontWeight: 800, fontSize: '0.72rem' }}>STAGED</span>
                          <button onClick={() => executeGitCommand(`git restore --staged ${f.name}`)} style={{ background: isLight ? '#e4e6eb' : '#334155', color: isLight ? '#050505' : '#fff', border: 'none', padding: '2px 6px', borderRadius: '4px', fontSize: '0.65rem', fontWeight: 700, cursor: 'pointer' }}>
                            unstage
                          </button>
                        </div>
                      </div>
                    ))}
                    {stagedFiles.length === 0 && <span style={{ fontSize: '0.78rem', color: isLight ? '#65676b' : '#94a3b8', fontStyle: 'italic', padding: '8px 0' }}>No staged snapshots (run `git add &lt;file&gt;` or `git add .`)</span>}
                  </div>
                </div>

                {/* 3. HEAD Commit */}
                <div style={{ background: isLight ? '#ffffff' : '#131d31', padding: 14, borderRadius: '10px', border: isLight ? '1px solid #1877f2' : '1px solid #38bdf8', minWidth: 0, boxShadow: isLight ? '0 1px 3px rgba(0,0,0,0.06)' : 'none' }}>
                  <div style={{ fontWeight: 800, fontSize: '0.85rem', color: isLight ? '#1877f2' : '#38bdf8', marginBottom: 10, display: 'flex', alignItems: 'center', gap: 5 }}>
                    <GitCommit size={15} /> 3. Repository (HEAD)
                  </div>
                  <div style={{ padding: '12px', background: isLight ? '#f0f2f5' : '#0b1120', borderRadius: '8px', border: isLight ? '1px solid #e4e6eb' : '1px solid #1e293b' }}>
                    <div style={{ fontSize: '0.8rem', color: isLight ? '#d97706' : '#fbbf24', fontWeight: 800 }}>Commit: {commits[commits.length - 1]?.hash}</div>
                    <div style={{ fontSize: '0.85rem', color: isLight ? '#050505' : '#ffffff', fontWeight: 700, marginTop: 4 }}>{commits[commits.length - 1]?.message}</div>
                    <div style={{ fontSize: '0.75rem', color: isLight ? '#65676b' : '#94a3b8', marginTop: 4 }}>Branch: {commits[commits.length - 1]?.branch}</div>
                  </div>
                </div>
              </div>
            )}

            {/* VIEW 3: DIFF INSPECTOR */}
            {activeSimView === 'diff-inspector' && (
              <div style={{ background: isLight ? '#ffffff' : '#0b1120', padding: 16, borderRadius: '10px', border: isLight ? '1px solid #e4e6eb' : '1px solid #334155', width: '100%', minWidth: 0, boxSizing: 'border-box' }}>
                <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: 10, flexWrap: 'wrap', gap: 6 }}>
                  <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                    <FileText size={16} color={isLight ? '#1877f2' : '#38bdf8'} />
                    <span style={{ fontFamily: 'monospace', fontSize: '0.85rem', fontWeight: 800, color: isLight ? '#050505' : '#ffffff' }}>
                      diff --git a/{selectedDiffFile} b/{selectedDiffFile}
                    </span>
                  </div>
                  <span style={{ fontSize: '0.75rem', color: isLight ? '#16a34a' : '#34d399', fontWeight: 800, background: isLight ? '#e6ffec' : 'rgba(52, 211, 153, 0.15)', padding: '2px 8px', borderRadius: '4px' }}>+14 lines</span>
                </div>

                <div style={{ fontFamily: 'JetBrains Mono, Fira Code, Consolas, monospace', fontSize: '0.82rem', background: isLight ? '#f8f9fa' : '#050811', padding: 14, borderRadius: '8px', lineHeight: 1.6, overflowX: 'auto', width: '100%', boxSizing: 'border-box', border: isLight ? '1px solid #e4e6eb' : '1px solid #1e293b' }}>
                  <div style={{ color: isLight ? '#65676b' : '#94a3b8' }}>--- a/{selectedDiffFile} (Index)</div>
                  <div style={{ color: isLight ? '#65676b' : '#94a3b8' }}>+++ b/{selectedDiffFile} (Working Tree)</div>
                  <div style={{ color: isLight ? '#65676b' : '#64748b' }}>@@ -12,8 +12,12 @@ def generate_session_token(user_id: str):</div>
                  <div style={{ color: isLight ? '#050505' : '#e2e8f0' }}>     payload = {`{"sub": user_id}`}</div>
                  <div style={{ background: isLight ? '#ffebe9' : 'rgba(244, 63, 94, 0.25)', color: isLight ? '#cf222e' : '#fca5a5', padding: '3px 6px', borderRadius: '4px', borderLeft: '3px solid #fa383e', fontWeight: 600 }}>
                    -    return jwt.encode(payload, SECRET_KEY, algorithm="HS256")
                  </div>
                  <div style={{ background: isLight ? '#e6ffec' : 'rgba(16, 185, 129, 0.25)', color: isLight ? '#1a7f37' : '#6ee7b7', padding: '3px 6px', borderRadius: '4px', borderLeft: '3px solid #42b72a', fontWeight: 600 }}>
                    +    expire = datetime.utcnow() + timedelta(minutes=60)
                  </div>
                  <div style={{ background: isLight ? '#e6ffec' : 'rgba(16, 185, 129, 0.25)', color: isLight ? '#1a7f37' : '#6ee7b7', padding: '3px 6px', borderRadius: '4px', borderLeft: '3px solid #42b72a', fontWeight: 600 }}>
                    +    payload.update({`{"exp": expire, "role": "admin"}`})
                  </div>
                  <div style={{ background: isLight ? '#e6ffec' : 'rgba(16, 185, 129, 0.25)', color: isLight ? '#1a7f37' : '#6ee7b7', padding: '3px 6px', borderRadius: '4px', borderLeft: '3px solid #42b72a', fontWeight: 600 }}>
                    +    return jwt.encode(payload, RSA_PRIVATE_KEY, algorithm="RS256")
                  </div>
                </div>
              </div>
            )}

            {/* VIEW 4: BRANCH NETWORK */}
            {activeSimView === 'branch-network' && (
              <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(240px, 1fr))', gap: 14, width: '100%', minWidth: 0 }}>
                {/* Active Branch Pointers List */}
                <div style={{ background: isLight ? '#ffffff' : '#131d31', padding: 16, borderRadius: '10px', border: isLight ? '1px solid #e4e6eb' : '1px solid #334155', minWidth: 0, boxShadow: isLight ? '0 1px 3px rgba(0,0,0,0.06)' : 'none' }}>
                  <div style={{ fontWeight: 800, fontSize: '0.88rem', color: isLight ? '#9333ea' : '#c084fc', marginBottom: 12, display: 'flex', alignItems: 'center', gap: 6 }}>
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
                            background: isCurrent ? (isLight ? '#e7f3ff' : '#1e293b') : (isLight ? '#f0f2f5' : '#0b1120'),
                            borderRadius: '8px',
                            fontSize: '0.85rem',
                            display: 'flex',
                            justifyContent: 'space-between',
                            alignItems: 'center',
                            border: isCurrent ? (isLight ? '2px solid #1877f2' : '2px solid #38bdf8') : (isLight ? '1px solid #e4e6eb' : '1px solid #334155'),
                            boxShadow: isCurrent ? (isLight ? '0 2px 8px rgba(24, 119, 242, 0.15)' : '0 0 14px rgba(56, 189, 248, 0.25)') : 'none'
                          }}
                        >
                          <span style={{ color: isCurrent ? (isLight ? '#1877f2' : '#38bdf8') : (isLight ? '#050505' : '#ffffff'), fontWeight: isCurrent ? 800 : 600, display: 'flex', alignItems: 'center', gap: 6 }}>
                            {isCurrent ? '● (HEAD)' : '○'} {b}
                          </span>
                          {!isCurrent && (
                            <button
                              onClick={() => executeGitCommand(`git checkout ${b}`)}
                              style={{
                                background: isLight ? '#ffffff' : '#1e293b',
                                color: isLight ? '#1877f2' : '#38bdf8',
                                border: isLight ? '1px solid #d8dadf' : '1px solid #0284c7',
                                padding: '4px 10px',
                                borderRadius: '5px',
                                fontSize: '0.75rem',
                                fontWeight: 700,
                                cursor: 'pointer',
                                transition: 'all 0.15s ease'
                              }}
                              onMouseEnter={(e) => {
                                e.currentTarget.style.background = isLight ? '#1877f2' : '#0284c7';
                                e.currentTarget.style.color = '#ffffff';
                              }}
                              onMouseLeave={(e) => {
                                e.currentTarget.style.background = isLight ? '#ffffff' : '#1e293b';
                                e.currentTarget.style.color = isLight ? '#1877f2' : '#38bdf8';
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
                <div style={{ background: isLight ? '#ffffff' : '#131d31', padding: 16, borderRadius: '10px', border: isLight ? '1px solid #e4e6eb' : '1px solid #334155', minWidth: 0, boxShadow: isLight ? '0 1px 3px rgba(0,0,0,0.06)' : 'none' }}>
                  <div style={{ fontWeight: 800, fontSize: '0.88rem', color: isLight ? '#1877f2' : '#38bdf8', marginBottom: 12 }}>
                    Fast Branch Actions:
                  </div>
                  <div style={{ display: 'flex', flexDirection: 'column', gap: 8 }}>
                    <button
                      onClick={() => executeGitCommand('git checkout -b feature/analytics')}
                      style={{
                        background: 'linear-gradient(45deg, #f09433 0%, #e6683c 25%, #dc2743 50%, #cc2366 75%, #bc1888 100%)',
                        color: '#ffffff',
                        border: 'none',
                        padding: '10px 14px',
                        borderRadius: '8px',
                        fontSize: '0.82rem',
                        fontWeight: 700,
                        cursor: 'pointer',
                        boxShadow: '0 3px 10px rgba(225, 48, 108, 0.3)'
                      }}
                    >
                      + Branch 'feature/analytics'
                    </button>
                    
                    <button
                      onClick={() => executeGitCommand('git merge main')}
                      style={{
                        background: isLight ? '#1877f2' : 'linear-gradient(135deg, #10b981, #059669)',
                        color: '#ffffff',
                        border: 'none',
                        padding: '10px 14px',
                        borderRadius: '8px',
                        fontSize: '0.82rem',
                        fontWeight: 700,
                        cursor: 'pointer',
                        boxShadow: isLight ? '0 3px 10px rgba(24, 119, 242, 0.3)' : '0 4px 12px rgba(16, 185, 129, 0.35)'
                      }}
                    >
                      🔀 Merge 'main' into '{currentBranch}'
                    </button>
                    
                    <button
                      onClick={() => executeGitCommand('git switch main')}
                      style={{
                        background: isLight ? '#f0f2f5' : '#1e293b',
                        color: isLight ? '#050505' : '#fbbf24',
                        border: isLight ? '1px solid #d8dadf' : '1px solid #d97706',
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
              <div style={{ background: isLight ? '#ffffff' : '#0b1120', padding: 16, borderRadius: '10px', border: isLight ? '1px solid #e1306c' : '1px solid #ec4899', width: '100%', minWidth: 0, boxSizing: 'border-box' }}>
                <div style={{ fontWeight: 800, fontSize: '0.88rem', color: isLight ? '#e1306c' : '#f472b6', marginBottom: 8, display: 'flex', alignItems: 'center', gap: 6 }}>
                  <RefreshCw size={16} /> Linear Commit Replay vs Merge Commit:
                </div>
                <p style={{ fontSize: '0.82rem', color: isLight ? '#65676b' : '#cbd5e1', marginBottom: 12 }}>
                  `git rebase` rewinds current branch commits, fast-forwards to base `main`, and reapplies commits sequentially without creating merge clutter.
                </p>
                <div style={{ display: 'flex', gap: 10, flexWrap: 'wrap' }}>
                  <button onClick={() => executeGitCommand('git rebase main')} style={{ background: isLight ? '#fff0f5' : '#1e293b', border: isLight ? '1px solid #e1306c' : '1px solid #ec4899', color: isLight ? '#e1306c' : '#f472b6', padding: '8px 14px', borderRadius: '6px', fontWeight: 700, fontSize: '0.8rem', cursor: 'pointer' }}>
                    ⚡ git rebase main
                  </button>
                  <button onClick={() => executeGitCommand('git cherry-pick 3c19e4')} style={{ background: isLight ? '#e7f3ff' : '#1e293b', border: isLight ? '1px solid #1877f2' : '1px solid #38bdf8', color: isLight ? '#1877f2' : '#38bdf8', padding: '8px 14px', borderRadius: '6px', fontWeight: 700, fontSize: '0.8rem', cursor: 'pointer' }}>
                    🍒 git cherry-pick 3c19e4
                  </button>
                </div>
              </div>
            )}

            {/* VIEW 6: LIFO STASH STACK */}
            {activeSimView === 'stash-stack' && (
              <div style={{ background: isLight ? '#ffffff' : '#0b1120', padding: 16, borderRadius: '10px', border: isLight ? '1px solid #f59e0b' : '1px solid #eab308', width: '100%', minWidth: 0, boxSizing: 'border-box' }}>
                <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: 10, flexWrap: 'wrap', gap: 6 }}>
                  <span style={{ fontWeight: 800, fontSize: '0.88rem', color: isLight ? '#d97706' : '#fde047', display: 'flex', alignItems: 'center', gap: 6 }}>
                    <Archive size={16} /> LIFO Stash Stack ({stashStack.length} items)
                  </span>
                  <div style={{ display: 'flex', gap: 8 }}>
                    <button onClick={() => executeGitCommand('git stash')} style={{ background: '#f59e0b', color: '#ffffff', border: 'none', padding: '5px 12px', borderRadius: '6px', fontWeight: 800, fontSize: '0.75rem', cursor: 'pointer' }}>git stash</button>
                    <button onClick={() => executeGitCommand('git stash pop')} style={{ background: isLight ? '#f0f2f5' : '#1e293b', color: isLight ? '#d97706' : '#fde047', border: '1px solid #f59e0b', padding: '5px 12px', borderRadius: '6px', fontWeight: 800, fontSize: '0.75rem', cursor: 'pointer' }}>git stash pop</button>
                  </div>
                </div>

                <div style={{ display: 'flex', flexDirection: 'column', gap: 6 }}>
                  {stashStack.map((s, idx) => (
                    <div key={idx} style={{ padding: '10px 14px', background: isLight ? '#f0f2f5' : '#131d31', borderRadius: '6px', fontSize: '0.82rem', display: 'flex', justifyContent: 'space-between', border: isLight ? '1px solid #e4e6eb' : '1px solid #334155' }}>
                      <span style={{ fontFamily: 'monospace', color: isLight ? '#d97706' : '#fde047', fontWeight: 700 }}>{s.id}: WIP on {s.branch}</span>
                      <span style={{ color: isLight ? '#65676b' : '#94a3b8', fontSize: '0.75rem' }}>{s.items?.length || 1} file(s)</span>
                    </div>
                  ))}
                  {stashStack.length === 0 && (
                    <div style={{ color: isLight ? '#65676b' : '#94a3b8', fontSize: '0.8rem', fontStyle: 'italic', padding: 6 }}>
                      No stashed snapshots. Run 'git stash' to store temporary uncommitted state.
                    </div>
                  )}
                </div>
              </div>
            )}

            {/* VIEW 7: REMOTE SYNC & FETCH */}
            {activeSimView === 'remote-sync' && (
              <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(200px, 1fr))', gap: 12, alignItems: 'center', width: '100%', minWidth: 0 }}>
                <div style={{ background: isLight ? '#ffffff' : '#131d31', padding: 14, borderRadius: '10px', border: isLight ? '1px solid #42b72a' : '1px solid #10b981', minWidth: 0, boxShadow: isLight ? '0 1px 3px rgba(0,0,0,0.06)' : 'none' }}>
                  <div style={{ fontWeight: 800, fontSize: '0.85rem', color: isLight ? '#42b72a' : '#34d399', marginBottom: 4 }}>💻 Local Repository</div>
                  <div style={{ fontSize: '0.78rem', color: isLight ? '#65676b' : '#e2e8f0' }}>Branch: <strong style={{ color: isLight ? '#1877f2' : '#38bdf8' }}>{currentBranch}</strong></div>
                  <div style={{ fontSize: '0.78rem', color: isLight ? '#42b72a' : '#34d399', fontWeight: 800, marginTop: 4 }}>{commits.length} Local Commits</div>
                </div>

                <div style={{ display: 'flex', flexDirection: 'column', gap: 6, alignItems: 'stretch', minWidth: 0 }}>
                  <button onClick={() => executeGitCommand('git fetch origin')} style={{ background: isLight ? '#e7f3ff' : '#1e293b', border: isLight ? '1px solid #1877f2' : '1px solid #38bdf8', color: isLight ? '#1877f2' : '#38bdf8', padding: '7px', borderRadius: '6px', fontWeight: 700, fontSize: '0.75rem', cursor: 'pointer' }}>
                    Fetch ⬇️
                  </button>
                  <button onClick={() => executeGitCommand('git pull origin main')} style={{ background: isLight ? '#f0f2f5' : '#1e293b', border: isLight ? '1px solid #42b72a' : '1px solid #10b981', color: isLight ? '#42b72a' : '#34d399', padding: '7px', borderRadius: '6px', fontWeight: 700, fontSize: '0.75rem', cursor: 'pointer' }}>
                    Pull 🔄
                  </button>
                  <button onClick={() => executeGitCommand('git push origin main')} style={{ background: isLight ? '#1877f2' : '#10b981', color: '#ffffff', border: 'none', padding: '7px', borderRadius: '6px', fontWeight: 800, fontSize: '0.75rem', cursor: 'pointer' }}>
                    Push ⬆️
                  </button>
                </div>

                <div style={{ background: isLight ? '#ffffff' : '#131d31', padding: 14, borderRadius: '10px', border: isLight ? '1px solid #8b5cf6' : '1px solid #8b5cf6', minWidth: 0, boxShadow: isLight ? '0 1px 3px rgba(0,0,0,0.06)' : 'none' }}>
                  <div style={{ fontWeight: 800, fontSize: '0.85rem', color: isLight ? '#7c3aed' : '#a78bfa', marginBottom: 4 }}>☁️ GitHub Remote (origin)</div>
                  <div style={{ fontSize: '0.72rem', color: isLight ? '#65676b' : '#e2e8f0', wordBreak: 'break-all' }}>{remoteOriginUrl}</div>
                  <div style={{ fontSize: '0.78rem', color: isLight ? '#7c3aed' : '#a78bfa', fontWeight: 800, marginTop: 4 }}>{remoteCommitsCount} Remote Commits</div>
                </div>
              </div>
            )}

            {/* VIEW 8: RESET & ROLLBACK MATRIX */}
            {activeSimView === 'reset-rollback' && (
              <div style={{ background: isLight ? '#ffffff' : '#0b1120', padding: 16, borderRadius: '10px', border: isLight ? '1px solid #fa383e' : '1px solid #f43f5e', width: '100%', minWidth: 0, boxSizing: 'border-box' }}>
                <div style={{ fontWeight: 800, fontSize: '0.88rem', color: isLight ? '#fa383e' : '#fb7185', marginBottom: 10, display: 'flex', alignItems: 'center', gap: 6 }}>
                  <RotateCcw size={16} /> Git Reset Comparison Matrix:
                </div>
                <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(150px, 1fr))', gap: 10, width: '100%', minWidth: 0 }}>
                  <div style={{ background: isLight ? '#f0f2f5' : '#131d31', padding: 10, borderRadius: '8px', border: isLight ? '1px solid #1877f2' : '1px solid #38bdf8', minWidth: 0 }}>
                    <div style={{ fontWeight: 800, fontSize: '0.78rem', color: isLight ? '#1877f2' : '#38bdf8' }}>--soft HEAD~1</div>
                    <div style={{ fontSize: '0.72rem', color: isLight ? '#65676b' : '#cbd5e1', marginTop: 3 }}>Preserves Index.</div>
                    <button onClick={() => executeGitCommand('git reset --soft HEAD~1')} style={{ marginTop: 6, fontSize: '0.7rem', padding: '4px 8px', background: isLight ? '#ffffff' : '#1e293b', color: isLight ? '#1877f2' : '#38bdf8', border: isLight ? '1px solid #1877f2' : '1px solid #0284c7', borderRadius: '4px', cursor: 'pointer', fontWeight: 700 }}>Soft Reset</button>
                  </div>
                  <div style={{ background: isLight ? '#f0f2f5' : '#131d31', padding: 10, borderRadius: '8px', border: isLight ? '1px solid #f59e0b' : '1px solid #f59e0b', minWidth: 0 }}>
                    <div style={{ fontWeight: 800, fontSize: '0.78rem', color: isLight ? '#d97706' : '#fbbf24' }}>--mixed (default)</div>
                    <div style={{ fontSize: '0.72rem', color: isLight ? '#65676b' : '#cbd5e1', marginTop: 3 }}>Unstages Index.</div>
                    <button onClick={() => executeGitCommand('git reset')} style={{ marginTop: 6, fontSize: '0.7rem', padding: '4px 8px', background: isLight ? '#ffffff' : '#1e293b', color: isLight ? '#d97706' : '#fbbf24', border: isLight ? '1px solid #f59e0b' : '1px solid #d97706', borderRadius: '4px', cursor: 'pointer', fontWeight: 700 }}>Mixed Reset</button>
                  </div>
                  <div style={{ background: isLight ? '#f0f2f5' : '#131d31', padding: 10, borderRadius: '8px', border: isLight ? '1px solid #fa383e' : '1px solid #f43f5e', minWidth: 0 }}>
                    <div style={{ fontWeight: 800, fontSize: '0.78rem', color: '#fa383e' }}>--hard HEAD~1</div>
                    <div style={{ fontSize: '0.72rem', color: isLight ? '#65676b' : '#cbd5e1', marginTop: 3 }}>Wipes work.</div>
                    <button onClick={() => executeGitCommand('git reset --hard HEAD~1')} style={{ marginTop: 6, fontSize: '0.7rem', padding: '4px 8px', background: '#fa383e', color: '#ffffff', border: 'none', borderRadius: '4px', cursor: 'pointer', fontWeight: 700 }}>Hard Reset</button>
                  </div>
                  <div style={{ background: isLight ? '#f0f2f5' : '#131d31', padding: 10, borderRadius: '8px', border: isLight ? '1px solid #42b72a' : '1px solid #10b981', minWidth: 0 }}>
                    <div style={{ fontWeight: 800, fontSize: '0.78rem', color: isLight ? '#42b72a' : '#34d399' }}>git revert</div>
                    <div style={{ fontSize: '0.72rem', color: isLight ? '#65676b' : '#cbd5e1', marginTop: 3 }}>Forward patch.</div>
                    <button onClick={() => executeGitCommand('git revert 9a01f8')} style={{ marginTop: 6, fontSize: '0.7rem', padding: '4px 8px', background: isLight ? '#42b72a' : '#10b981', color: '#ffffff', border: 'none', borderRadius: '4px', cursor: 'pointer', fontWeight: 800 }}>Revert</button>
                  </div>
                </div>
              </div>
            )}
          </div>

          {/* Terminal Console (Dynamic Shell Prompt with PWD tracking) */}
          <div style={{ padding: 0, overflow: 'hidden', background: '#050811', border: isLight ? '1px solid #e4e6eb' : '1px solid #1e293b', borderRadius: '12px', width: '100%', minWidth: 0, boxSizing: 'border-box', boxShadow: isLight ? '0 2px 12px rgba(0,0,0,0.1)' : '0 8px 30px rgba(0,0,0,0.6)' }}>
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', padding: '10px 16px', background: '#0b1120', borderBottom: '1px solid #1e293b' }}>
              <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                <Terminal size={15} color="#38bdf8" />
                <span style={{ fontSize: '0.82rem', fontWeight: 700, color: '#f8fafc' }}>Git Shell Emulator (Dynamic File Navigation & Staging Sync)</span>
              </div>
              <button onClick={() => setTerminalHistory([])} style={{ background: '#1e293b', color: '#94a3b8', border: '1px solid #334155', padding: '3px 8px', borderRadius: '5px', fontSize: '0.72rem', cursor: 'pointer', fontWeight: 600 }}>
                Clear Output
              </button>
            </div>

            <div style={{ padding: '14px 16px', minHeight: '180px', maxHeight: '240px', overflowY: 'auto', fontFamily: 'JetBrains Mono, Fira Code, Consolas, monospace', fontSize: '0.82rem', lineHeight: 1.6, width: '100%', boxSizing: 'border-box', wordBreak: 'break-all' }}>
              {terminalHistory.map((line, idx) => (
                <div key={idx} style={{ color: line.includes('$') ? '#38bdf8' : line.startsWith('bash:') || line.startsWith('fatal') || line.startsWith('error') ? '#fb7185' : '#f1f5f9', fontWeight: line.includes('$') ? 700 : 400 }}>
                  {line}
                </div>
              ))}
            </div>

            <form onSubmit={(e) => { e.preventDefault(); executeGitCommand(commandInput); }} style={{ display: 'flex', borderTop: '1px solid #1e293b', background: '#0b1120', width: '100%', minWidth: 0 }}>
              <span style={{ padding: '10px 0 10px 16px', color: '#10b981', fontFamily: 'monospace', fontWeight: 800, fontSize: '0.85rem', whiteSpace: 'nowrap' }}>
                (repo{currentDir ? `/${currentDir}` : ''}) $
              </span>
              <input
                type="text"
                value={commandInput}
                onChange={(e) => handleInputChange(e.target.value)}
                onKeyDown={(e) => {
                  if (e.key === 'ArrowUp') {
                    e.preventDefault();
                    if (commandHistory.length === 0) return;
                    setHistoryIndex(prev => {
                      const nextIdx = prev === -1 ? commandHistory.length - 1 : Math.max(0, prev - 1);
                      setCommandInput(commandHistory[nextIdx]);
                      return nextIdx;
                    });
                  } else if (e.key === 'ArrowDown') {
                    e.preventDefault();
                    if (historyIndex === -1) return;
                    if (historyIndex < commandHistory.length - 1) {
                      const nextIdx = historyIndex + 1;
                      setHistoryIndex(nextIdx);
                      setCommandInput(commandHistory[nextIdx]);
                    } else {
                      setHistoryIndex(-1);
                      setCommandInput('');
                    }
                  }
                }}
                placeholder="Type shell or git commands (e.g. cd src, ls, pwd, cat src/auth/jwt.py, git add src/auth/jwt.py, git status, git commit)..."
                style={{ flex: 1, minWidth: 0, width: '100%', background: 'transparent', border: 'none', padding: '10px 14px', color: '#ffffff', fontFamily: 'JetBrains Mono, monospace', fontSize: '0.85rem', outline: 'none', fontWeight: 600 }}
              />
            </form>
          </div>
        </div>
      )}

      {/* TAB 2: 3-TREES & DIFF STAGING */}
      {activeTab === 'snapshots' && (
        <div style={{ display: 'grid', gap: 16, width: '100%', minWidth: 0 }}>
          <div style={{ padding: 18, background: isLight ? '#ffffff' : '#070b14', border: isLight ? '1px solid #e4e6eb' : '1px solid #1e293b', borderRadius: '12px', width: '100%', minWidth: 0, boxSizing: 'border-box', boxShadow: isLight ? '0 1px 3px rgba(0,0,0,0.06)' : 'none' }}>
            <h3 style={{ fontSize: '1.05rem', fontWeight: 800, color: isLight ? '#050505' : '#ffffff', marginBottom: 14, display: 'flex', alignItems: 'center', gap: 6 }}>
              <Layers size={17} color={isLight ? '#16a34a' : '#10b981'} /> Git 3-Trees Workflow (`git status`, `git add`, `git diff`)
            </h3>

            <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(220px, 1fr))', gap: 14, width: '100%', minWidth: 0 }}>
              {/* Working Tree */}
              <div style={{ background: isLight ? '#f0f2f5' : '#131d31', padding: 14, borderRadius: '10px', border: isLight ? '1px solid #fa383e' : '1px solid #f43f5e', minWidth: 0 }}>
                <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: 10 }}>
                  <span style={{ fontWeight: 800, fontSize: '0.85rem', color: '#fa383e' }}>1. Working Directory</span>
                  <button onClick={() => executeGitCommand('git add .')} style={{ background: '#fa383e', color: '#ffffff', border: 'none', padding: '4px 10px', borderRadius: '5px', fontWeight: 700, fontSize: '0.72rem', cursor: 'pointer' }}>
                    + Stage All (git add .)
                  </button>
                </div>
                <div style={{ display: 'flex', flexDirection: 'column', gap: 6 }}>
                  {workingFiles.map((f, idx) => (
                    <div key={idx} style={{ padding: '8px 10px', background: isLight ? '#ffffff' : '#0b1120', borderRadius: '6px', fontSize: '0.78rem', display: 'flex', justifyContent: 'space-between', border: isLight ? '1px solid #e4e6eb' : '1px solid #1e293b' }}>
                      <span style={{ overflow: 'hidden', textOverflow: 'ellipsis', whiteSpace: 'nowrap', color: isLight ? '#050505' : '#f8fafc', fontWeight: 600 }}>📄 {f.name}</span>
                      <span style={{ color: f.status === 'clean' ? '#42b72a' : '#fa383e', fontWeight: 800 }}>{f.status}</span>
                    </div>
                  ))}
                </div>
              </div>

              {/* Staging Area */}
              <div style={{ background: isLight ? '#f0f2f5' : '#131d31', padding: 14, borderRadius: '10px', border: isLight ? '1px solid #42b72a' : '1px solid #10b981', minWidth: 0 }}>
                <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: 10 }}>
                  <span style={{ fontWeight: 800, fontSize: '0.85rem', color: '#42b72a' }}>2. Staging Index (Cache)</span>
                  <button onClick={() => executeGitCommand('git reset')} disabled={stagedFiles.length === 0} style={{ background: isLight ? '#ffffff' : '#1e293b', color: isLight ? '#050505' : '#e2e8f0', border: isLight ? '1px solid #d8dadf' : '1px solid #475569', padding: '4px 10px', borderRadius: '5px', fontWeight: 700, fontSize: '0.72rem', cursor: 'pointer', opacity: stagedFiles.length === 0 ? 0.5 : 1 }}>
                    Unstage (git reset)
                  </button>
                </div>
                <div style={{ display: 'flex', flexDirection: 'column', gap: 6 }}>
                  {stagedFiles.map((f, idx) => (
                    <div key={idx} style={{ padding: '8px 10px', background: isLight ? '#ffffff' : '#0b1120', borderRadius: '6px', fontSize: '0.78rem', display: 'flex', justifyContent: 'space-between', border: isLight ? '1px solid #e4e6eb' : '1px solid #1e293b' }}>
                      <span style={{ color: isLight ? '#050505' : '#f8fafc', fontWeight: 600 }}>✓ {f.name}</span>
                      <span style={{ color: '#42b72a', fontWeight: 800 }}>STAGED</span>
                    </div>
                  ))}
                  {stagedFiles.length === 0 && <span style={{ fontSize: '0.78rem', color: isLight ? '#65676b' : '#94a3b8' }}>No staged snapshots</span>}
                </div>
              </div>

              {/* Local HEAD Commit */}
              <div style={{ background: isLight ? '#f0f2f5' : '#131d31', padding: 14, borderRadius: '10px', border: isLight ? '1px solid #1877f2' : '1px solid #38bdf8', minWidth: 0 }}>
                <div style={{ fontWeight: 800, fontSize: '0.85rem', color: isLight ? '#1877f2' : '#38bdf8', marginBottom: 10 }}>3. Local Repository (HEAD)</div>
                <div style={{ padding: '12px', background: isLight ? '#ffffff' : '#0b1120', borderRadius: '8px', border: isLight ? '1px solid #e4e6eb' : '1px solid #1e293b' }}>
                  <div style={{ fontSize: '0.8rem', color: isLight ? '#d97706' : '#fbbf24', fontWeight: 800 }}>Commit: {commits[commits.length - 1]?.hash}</div>
                  <div style={{ fontSize: '0.85rem', color: isLight ? '#050505' : '#ffffff', fontWeight: 700, marginTop: 4 }}>{commits[commits.length - 1]?.message}</div>
                  <div style={{ fontSize: '0.75rem', color: isLight ? '#65676b' : '#94a3b8', marginTop: 4 }}>Branch: {commits[commits.length - 1]?.branch}</div>
                </div>
              </div>
            </div>
          </div>
        </div>
      )}

      {/* TAB 3: BRANCHING & MERGES */}
      {activeTab === 'branching' && (
        <div style={{ display: 'grid', gap: 16, width: '100%', minWidth: 0 }}>
          <div style={{ padding: 18, background: isLight ? '#ffffff' : '#070b14', border: isLight ? '1px solid #e4e6eb' : '1px solid #1e293b', borderRadius: '12px', width: '100%', minWidth: 0, boxSizing: 'border-box', boxShadow: isLight ? '0 1px 3px rgba(0,0,0,0.06)' : 'none' }}>
            <h3 style={{ fontSize: '1.05rem', fontWeight: 800, color: isLight ? '#050505' : '#ffffff', marginBottom: 14, display: 'flex', alignItems: 'center', gap: 6 }}>
              <GitBranch size={17} color={isLight ? '#d97706' : '#f59e0b'} /> Branching, Switching & Fast-Forward Merges
            </h3>

            <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(220px, 1fr))', gap: 14, width: '100%', minWidth: 0 }}>
              <div style={{ background: isLight ? '#f0f2f5' : '#131d31', padding: 14, borderRadius: '10px', border: isLight ? '1px solid #e4e6eb' : '1px solid #334155', minWidth: 0 }}>
                <div style={{ fontWeight: 800, fontSize: '0.85rem', color: isLight ? '#1877f2' : '#38bdf8', marginBottom: 10 }}>Active Branches:</div>
                <div style={{ display: 'flex', flexDirection: 'column', gap: 6 }}>
                  {branches.map((b, idx) => (
                    <div key={idx} style={{ padding: '8px 12px', background: isLight ? '#ffffff' : '#0b1120', borderRadius: '6px', fontSize: '0.82rem', display: 'flex', justifyContent: 'space-between', alignItems: 'center', border: isLight ? '1px solid #e4e6eb' : '1px solid #1e293b' }}>
                      <span style={{ color: b === currentBranch ? (isLight ? '#1877f2' : '#34d399') : (isLight ? '#050505' : '#ffffff'), fontWeight: b === currentBranch ? 800 : 600 }}>
                        {b === currentBranch ? '● (HEAD) ' : '○ '}{b}
                      </span>
                      {b !== currentBranch && (
                        <button onClick={() => executeGitCommand(`git checkout ${b}`)} style={{ background: isLight ? '#f0f2f5' : '#1e293b', color: isLight ? '#1877f2' : '#38bdf8', border: isLight ? '1px solid #d8dadf' : '1px solid #0284c7', padding: '3px 8px', borderRadius: '5px', fontSize: '0.72rem', fontWeight: 700, cursor: 'pointer' }}>
                          Checkout
                        </button>
                      )}
                    </div>
                  ))}
                </div>
              </div>

              <div style={{ background: isLight ? '#f0f2f5' : '#131d31', padding: 14, borderRadius: '10px', border: isLight ? '1px solid #e4e6eb' : '1px solid #334155', minWidth: 0 }}>
                <div style={{ fontWeight: 800, fontSize: '0.85rem', color: isLight ? '#1877f2' : '#34d399', marginBottom: 10 }}>Merge Operations:</div>
                <div style={{ display: 'flex', flexDirection: 'column', gap: 8 }}>
                  <button onClick={() => executeGitCommand(`git merge main`)} style={{ background: isLight ? '#1877f2' : 'linear-gradient(135deg, #10b981, #059669)', color: '#ffffff', border: 'none', padding: '10px', borderRadius: '8px', fontSize: '0.82rem', fontWeight: 800, cursor: 'pointer' }}>
                    Merge 'main' into '{currentBranch}'
                  </button>
                  <button onClick={() => executeGitCommand(`git checkout -b feature/analytics`)} style={{ background: 'linear-gradient(45deg, #f09433 0%, #e6683c 25%, #dc2743 50%, #cc2366 75%, #bc1888 100%)', color: '#ffffff', border: 'none', padding: '10px', borderRadius: '8px', fontSize: '0.82rem', fontWeight: 800, cursor: 'pointer' }}>
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
          <div style={{ padding: 18, background: isLight ? '#ffffff' : '#070b14', border: isLight ? '1px solid #e4e6eb' : '1px solid #1e293b', borderRadius: '12px', width: '100%', minWidth: 0, boxSizing: 'border-box', boxShadow: isLight ? '0 1px 3px rgba(0,0,0,0.06)' : 'none' }}>
            <h3 style={{ fontSize: '1.05rem', fontWeight: 800, color: isLight ? '#050505' : '#ffffff', marginBottom: 14, display: 'flex', alignItems: 'center', gap: 6 }}>
              <RotateCcw size={17} color={isLight ? '#e1306c' : '#ec4899'} /> History Rewriting: `rebase`, `cherry-pick`, `reset`, `revert`, `stash`
            </h3>

            <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(200px, 1fr))', gap: 12, width: '100%', minWidth: 0 }}>
              <div style={{ background: isLight ? '#f0f2f5' : '#131d31', padding: 12, borderRadius: '8px', border: isLight ? '1px solid #e1306c' : '1px solid #ec4899', minWidth: 0 }}>
                <div style={{ fontWeight: 800, fontSize: '0.82rem', color: isLight ? '#e1306c' : '#f472b6', marginBottom: 4 }}>1. Linearize (rebase)</div>
                <p style={{ fontSize: '0.75rem', color: isLight ? '#65676b' : '#cbd5e1', margin: '0 0 10px 0' }}>Replays commits on top of base.</p>
                <button onClick={() => executeGitCommand('git rebase main')} style={{ width: '100%', background: isLight ? '#ffffff' : '#1e293b', color: isLight ? '#e1306c' : '#f472b6', border: isLight ? '1px solid #e1306c' : '1px solid #ec4899', padding: '6px', borderRadius: '6px', fontWeight: 700, fontSize: '0.75rem', cursor: 'pointer' }}>
                  git rebase main
                </button>
              </div>

              <div style={{ background: isLight ? '#f0f2f5' : '#131d31', padding: 12, borderRadius: '8px', border: isLight ? '1px solid #1877f2' : '1px solid #38bdf8', minWidth: 0 }}>
                <div style={{ fontWeight: 800, fontSize: '0.82rem', color: isLight ? '#1877f2' : '#38bdf8', marginBottom: 4 }}>2. Cherry-Pick</div>
                <p style={{ fontSize: '0.75rem', color: isLight ? '#65676b' : '#cbd5e1', margin: '0 0 10px 0' }}>Applies a single commit delta.</p>
                <button onClick={() => executeGitCommand('git cherry-pick 3c19e4')} style={{ width: '100%', background: isLight ? '#ffffff' : '#1e293b', color: isLight ? '#1877f2' : '#38bdf8', border: isLight ? '1px solid #1877f2' : '1px solid #38bdf8', padding: '6px', borderRadius: '6px', fontWeight: 700, fontSize: '0.75rem', cursor: 'pointer' }}>
                  git cherry-pick 3c19e4
                </button>
              </div>

              <div style={{ background: isLight ? '#f0f2f5' : '#131d31', padding: 12, borderRadius: '8px', border: isLight ? '1px solid #f59e0b' : '1px solid #eab308', minWidth: 0 }}>
                <div style={{ fontWeight: 800, fontSize: '0.82rem', color: isLight ? '#d97706' : '#fde047', marginBottom: 4 }}>3. Stash Stack</div>
                <p style={{ fontSize: '0.75rem', color: isLight ? '#65676b' : '#cbd5e1', margin: '0 0 10px 0' }}>Items in stack: <strong>{stashStack.length}</strong></p>
                <div style={{ display: 'flex', gap: 6 }}>
                  <button onClick={() => executeGitCommand('git stash')} style={{ flex: 1, background: '#f59e0b', color: '#ffffff', border: 'none', padding: '5px', borderRadius: '5px', fontWeight: 800, fontSize: '0.72rem', cursor: 'pointer' }}>Stash</button>
                  <button onClick={() => executeGitCommand('git stash pop')} style={{ flex: 1, background: isLight ? '#ffffff' : '#1e293b', color: isLight ? '#d97706' : '#fde047', border: '1px solid #f59e0b', padding: '5px', borderRadius: '5px', fontWeight: 800, fontSize: '0.72rem', cursor: 'pointer' }}>Pop</button>
                </div>
              </div>

              <div style={{ background: isLight ? '#f0f2f5' : '#131d31', padding: 12, borderRadius: '8px', border: isLight ? '1px solid #fa383e' : '1px solid #f43f5e', minWidth: 0 }}>
                <div style={{ fontWeight: 800, fontSize: '0.82rem', color: '#fa383e', marginBottom: 4 }}>4. Reset & Revert</div>
                <p style={{ fontSize: '0.75rem', color: isLight ? '#65676b' : '#cbd5e1', margin: '0 0 10px 0' }}>Undo commits or create patch.</p>
                <div style={{ display: 'flex', gap: 6 }}>
                  <button onClick={() => executeGitCommand('git reset --hard HEAD~1')} style={{ flex: 1, background: '#fa383e', color: '#ffffff', border: 'none', padding: '5px', borderRadius: '5px', fontWeight: 700, fontSize: '0.7rem', cursor: 'pointer' }}>Hard Reset</button>
                  <button onClick={() => executeGitCommand('git revert 9a01f8')} style={{ flex: 1, background: isLight ? '#42b72a' : '#10b981', color: '#ffffff', border: 'none', padding: '5px', borderRadius: '5px', fontWeight: 800, fontSize: '0.7rem', cursor: 'pointer' }}>Revert</button>
                </div>
              </div>
            </div>
          </div>
        </div>
      )}

      {/* TAB 5: REMOTE SYNC & COLLABORATION */}
      {activeTab === 'remotes-sync' && (
        <div style={{ display: 'grid', gap: 16, width: '100%', minWidth: 0 }}>
          <div style={{ padding: 18, background: isLight ? '#ffffff' : '#070b14', border: isLight ? '1px solid #e4e6eb' : '1px solid #1e293b', borderRadius: '12px', width: '100%', minWidth: 0, boxSizing: 'border-box', boxShadow: isLight ? '0 1px 3px rgba(0,0,0,0.06)' : 'none' }}>
            <h3 style={{ fontSize: '1.05rem', fontWeight: 800, color: isLight ? '#050505' : '#ffffff', marginBottom: 14, display: 'flex', alignItems: 'center', gap: 6 }}>
              <UploadCloud size={17} color={isLight ? '#7c3aed' : '#8b5cf6'} /> Remote Synchronization (`remote`, `fetch`, `pull`, `push`)
            </h3>

            <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(220px, 1fr))', gap: 14, width: '100%', minWidth: 0 }}>
              <div style={{ background: isLight ? '#f0f2f5' : '#131d31', padding: 14, borderRadius: '10px', border: isLight ? '1px solid #e4e6eb' : '1px solid #8b5cf6', minWidth: 0 }}>
                <div style={{ fontWeight: 800, fontSize: '0.85rem', color: isLight ? '#7c3aed' : '#a78bfa', marginBottom: 4 }}>Remote Endpoints (origin):</div>
                <div style={{ fontFamily: 'monospace', fontSize: '0.75rem', color: isLight ? '#1877f2' : '#38bdf8', padding: '8px', background: isLight ? '#ffffff' : '#0b1120', borderRadius: '6px', wordBreak: 'break-all', border: isLight ? '1px solid #e4e6eb' : '1px solid #1e293b' }}>
                  {remoteOriginUrl}
                </div>
                <div style={{ fontSize: '0.78rem', color: isLight ? '#65676b' : '#cbd5e1', marginTop: 8 }}>
                  Commits on Remote: <strong style={{ color: isLight ? '#7c3aed' : '#a78bfa' }}>{remoteCommitsCount}</strong> • Local: <strong style={{ color: isLight ? '#42b72a' : '#34d399' }}>{commits.length}</strong>
                </div>
              </div>

              <div style={{ background: isLight ? '#f0f2f5' : '#131d31', padding: 14, borderRadius: '10px', display: 'flex', flexDirection: 'column', gap: 8, minWidth: 0, border: isLight ? '1px solid #e4e6eb' : '1px solid #334155' }}>
                <button onClick={() => executeGitCommand('git fetch origin')} style={{ background: isLight ? '#ffffff' : '#1e293b', color: isLight ? '#1877f2' : '#38bdf8', border: isLight ? '1px solid #d8dadf' : '1px solid #0284c7', padding: '8px', borderRadius: '6px', fontWeight: 700, fontSize: '0.78rem', cursor: 'pointer', display: 'flex', alignItems: 'center', justifyContent: 'center', gap: 6 }}>
                  <DownloadCloud size={14} /> Fetch Remote Objects (git fetch)
                </button>
                <button onClick={() => executeGitCommand('git pull origin main')} style={{ background: isLight ? '#ffffff' : '#1e293b', color: isLight ? '#42b72a' : '#34d399', border: isLight ? '1px solid #d8dadf' : '1px solid #10b981', padding: '8px', borderRadius: '6px', fontWeight: 700, fontSize: '0.78rem', cursor: 'pointer', display: 'flex', alignItems: 'center', justifyContent: 'center', gap: 6 }}>
                  <RotateCw size={14} /> Pull & Merge Remote (git pull)
                </button>
                <button onClick={() => executeGitCommand('git push origin main')} style={{ background: isLight ? '#1877f2' : 'linear-gradient(135deg, #10b981, #059669)', color: '#ffffff', border: 'none', padding: '8px', borderRadius: '6px', fontWeight: 800, fontSize: '0.78rem', cursor: 'pointer', display: 'flex', alignItems: 'center', justifyContent: 'center', gap: 6 }}>
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
          <div style={{ padding: 18, background: isLight ? '#ffffff' : '#070b14', border: isLight ? '1px solid #e4e6eb' : '1px solid #1e293b', borderRadius: '12px', width: '100%', minWidth: 0, boxSizing: 'border-box', boxShadow: isLight ? '0 1px 3px rgba(0,0,0,0.06)' : 'none' }}>
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: 14, flexWrap: 'wrap', gap: 6 }}>
              <div>
                <span style={{ fontSize: '0.75rem', color: isLight ? '#7c3aed' : '#a78bfa', fontWeight: 800 }}>PULL REQUEST #42</span>
                <h3 style={{ fontSize: '1.15rem', fontWeight: 800, margin: '2px 0 0 0', color: isLight ? '#050505' : '#ffffff' }}>
                  feat: implement enterprise JWT authentication and security headers
                </h3>
              </div>
              <span
                style={{
                  padding: '4px 12px',
                  borderRadius: '16px',
                  fontSize: '0.75rem',
                  fontWeight: 800,
                  background: prStatus === 'merged' ? (isLight ? '#f3e8ff' : 'rgba(139, 92, 246, 0.25)') : (isLight ? '#e6ffec' : 'rgba(16, 185, 129, 0.25)'),
                  color: prStatus === 'merged' ? (isLight ? '#7c3aed' : '#a78bfa') : (isLight ? '#16a34a' : '#34d399'),
                  border: `1px solid ${prStatus === 'merged' ? '#8b5cf6' : '#10b981'}`
                }}
              >
                {prStatus.toUpperCase()}
              </span>
            </div>

            {/* Reviewers Feedback */}
            <div style={{ display: 'flex', flexDirection: 'column', gap: 8, marginBottom: 14 }}>
              {prReviews.map((r, idx) => (
                <div key={idx} style={{ padding: '10px 14px', background: isLight ? '#f0f2f5' : '#131d31', borderRadius: '8px', border: isLight ? '1px solid #e4e6eb' : '1px solid #334155', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                  <div>
                    <span style={{ fontSize: '0.82rem', fontWeight: 800, color: isLight ? '#050505' : '#f8fafc' }}>{r.reviewer}</span>
                    <div style={{ fontSize: '0.75rem', color: isLight ? '#65676b' : '#cbd5e1', marginTop: 2 }}>{r.comment}</div>
                  </div>
                  <span style={{ fontSize: '0.72rem', color: isLight ? '#16a34a' : '#34d399', fontWeight: 800 }}>✓ {r.status}</span>
                </div>
              ))}
            </div>

            {/* Merge Actions */}
            {prStatus === 'open' && (
              <div style={{ display: 'flex', gap: 10, alignItems: 'center', background: isLight ? '#f0f2f5' : '#0b1120', padding: 12, borderRadius: '8px', border: isLight ? '1px solid #e4e6eb' : '1px solid #1e293b', flexWrap: 'wrap' }}>
                <select className="input" value={mergeStrategy} onChange={(e) => setMergeStrategy(e.target.value)} style={{ fontSize: '0.8rem', flex: 1, minWidth: '160px', background: isLight ? '#ffffff' : '#1e293b', color: isLight ? '#050505' : '#f8fafc', border: isLight ? '1px solid #d8dadf' : '1px solid #334155' }}>
                  <option value="merge-commit">Create a merge commit</option>
                  <option value="squash">Squash and merge</option>
                  <option value="rebase">Rebase and merge</option>
                </select>
                <button onClick={handleMergePr} style={{ background: isLight ? '#1877f2' : 'linear-gradient(135deg, #6366f1, #4f46e5)', color: '#ffffff', border: 'none', padding: '8px 16px', borderRadius: '6px', fontWeight: 800, fontSize: '0.8rem', cursor: 'pointer', display: 'flex', alignItems: 'center', gap: 6 }}>
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
          <div style={{ padding: 18, background: isLight ? '#ffffff' : '#070b14', border: isLight ? '1px solid #e4e6eb' : '1px solid #1e293b', borderRadius: '12px', width: '100%', minWidth: 0, boxSizing: 'border-box', boxShadow: isLight ? '0 1px 3px rgba(0,0,0,0.06)' : 'none' }}>
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: 14, flexWrap: 'wrap', gap: 6 }}>
              <div>
                <span style={{ fontSize: '0.75rem', color: isLight ? '#0284c7' : '#38bdf8', fontWeight: 800 }}>WORKFLOW: .github/workflows/main.yml</span>
                <h3 style={{ fontSize: '1.1rem', fontWeight: 800, margin: '2px 0 0 0', color: isLight ? '#050505' : '#ffffff' }}>
                  🚀 Enterprise CI/CD Automated Deployment Matrix
                </h3>
              </div>
              <button onClick={runCicdPipeline} disabled={pipelineRunning} style={{ background: isLight ? '#1877f2' : 'linear-gradient(135deg, #0ea5e9, #0284c7)', color: '#ffffff', border: 'none', padding: '6px 14px', borderRadius: '6px', fontWeight: 800, fontSize: '0.78rem', cursor: 'pointer', display: 'flex', alignItems: 'center', gap: 6, opacity: pipelineRunning ? 0.6 : 1 }}>
                <Play size={13} /> {pipelineRunning ? 'Executing...' : 'Trigger Workflow'}
              </button>
            </div>

            <div style={{ display: 'flex', flexDirection: 'column', gap: 8 }}>
              {pipelineSteps.map((step) => (
                <div
                  key={step.id}
                  style={{
                    padding: '12px 16px',
                    background: isLight ? '#f0f2f5' : '#131d31',
                    borderRadius: '8px',
                    border: `1px solid ${step.status === 'success' ? (isLight ? '#42b72a' : '#10b981') : step.status === 'running' ? (isLight ? '#1877f2' : '#38bdf8') : (isLight ? '#e4e6eb' : '#334155')}`,
                    display: 'flex',
                    justifyContent: 'space-between',
                    alignItems: 'center'
                  }}
                >
                  <span style={{ fontSize: '0.82rem', fontWeight: 700, color: isLight ? '#050505' : '#f8fafc' }}>{step.name}</span>
                  <span
                    style={{
                      fontSize: '0.72rem',
                      fontWeight: 800,
                      padding: '3px 8px',
                      borderRadius: '5px',
                      background: step.status === 'success' ? (isLight ? '#e6ffec' : 'rgba(16, 185, 129, 0.2)') : step.status === 'running' ? (isLight ? '#e7f3ff' : 'rgba(56, 189, 248, 0.2)') : (isLight ? '#ffffff' : 'rgba(255, 255, 255, 0.05)'),
                      color: step.status === 'success' ? (isLight ? '#16a34a' : '#34d399') : step.status === 'running' ? (isLight ? '#1877f2' : '#38bdf8') : (isLight ? '#65676b' : '#94a3b8')
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
