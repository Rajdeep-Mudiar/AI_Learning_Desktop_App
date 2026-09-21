"""
Git & GitHub Engineering Track Seed Data
Levels 1 - 5 + Advanced covering:
- Level 1: Git Plumbing & Core Commands (init, clone, add, commit, log, diff)
- Level 2: Branching Topologies & Merges (branch, switch, checkout, merge)
- Level 3: Remote Git & Tracking (remote, fetch, pull, push, upstream)
- Level 4: Collaboration & Review Workflows (PRs, code review, releases, branch protection)
- Level 5: Advanced Time-Travel & History Rewriting (rebase, cherry-pick, stash, reset, reflog, bisect)
- Advanced: GitHub Actions CI/CD, Secrets, Dependabot, CodeQL, Pages
"""

COURSES_DATA = [
    {
        "id": "course-git-lvl1",
        "title": "Git Level 1: Git Object Model & Working Tree Mechanics",
        "slug": "git-level-1-object-model-basics",
        "domain": "github",
        "color": "#F59E0B",
        "icon": "GitBranch",
        "is_published": True,
        "skills_taught": ['Git Internals', 'Branching Topologies', 'Interactive Rebase', 'GitHub Actions'],
        "description": "Understand Git internals (Blobs, Trees, Commits, Annotated Tags), SHA-1/SHA-256 DAG hashes, and Working Directory $\\to$ Staging Area $\\to$ Repository transitions.",
        "category": "Git & GitHub",
        "level": "beginner",
        "estimated_hours": 10,
        "thumbnail_url": "/assets/courses/git-basics.png",
        "modules": [
            {
                "id": "mod-git-1-1",
                "title": "Module 1: The Three Trees & Core Operations",
                "description": "Working tree, Index staging area, Git commit DAG, `git status`, and `git diff`.",
                "order": 1,
                "lesson_ids": ["git-internals-blobs-trees-commits", "git-three-trees-staging-workflow"]
            }
        ]
    },
    {
        "id": "course-git-lvl2",
        "title": "Git Level 2: Branching Strategies & Fast-Forward Merges",
        "slug": "git-level-2-branching-merges",
        "domain": "github",
        "color": "#F59E0B",
        "icon": "GitBranch",
        "is_published": True,
        "skills_taught": ['Git Internals', 'Branching Topologies', 'Interactive Rebase', 'GitHub Actions'],
        "description": "Master branch pointers, `git switch`, 3-way recursive merges, merge conflict resolution, and Trunk-Based vs GitFlow branching.",
        "category": "Git & GitHub",
        "level": "intermediate",
        "estimated_hours": 12,
        "thumbnail_url": "/assets/courses/git-branching.png",
        "modules": [
            {
                "id": "mod-git-2-1",
                "title": "Module 1: Branch Pointers & Merge Conflict Engines",
                "description": "Fast-forward vs 3-way merge commits, conflict marker parsing, and branch management.",
                "order": 1,
                "lesson_ids": ["git-branch-pointers-switch-merge", "git-merge-conflicts-resolution-strategies"]
            }
        ]
    },
    {
        "id": "course-git-lvl3",
        "title": "Git Level 3: Remote Repositories & Tracking Branches",
        "slug": "git-level-3-remotes-collaboration",
        "domain": "github",
        "color": "#F59E0B",
        "icon": "GitBranch",
        "is_published": True,
        "skills_taught": ['Git Internals', 'Branching Topologies', 'Interactive Rebase', 'GitHub Actions'],
        "description": "Remotes (`origin`, `upstream`), `git fetch` vs `git pull --rebase`, remote tracking branches, and SSH authentication.",
        "category": "Git & GitHub",
        "level": "intermediate",
        "estimated_hours": 12,
        "thumbnail_url": "/assets/courses/git-remotes.png",
        "modules": [
            {
                "id": "mod-git-3-1",
                "title": "Module 1: Upstream Tracking & Remote Synchronization",
                "description": "Fetch, pull, push --force-with-lease, and tracking configurations.",
                "order": 1,
                "lesson_ids": ["git-remotes-fetch-pull-tracking", "git-pull-rebase-force-with-lease"]
            }
        ]
    },
    {
        "id": "course-git-lvl4",
        "title": "Git Level 4: Advanced History Rewriting, Rebase & Reflog",
        "slug": "git-level-4-rebase-reflog-bisect",
        "domain": "github",
        "color": "#F59E0B",
        "icon": "GitBranch",
        "is_published": True,
        "skills_taught": ['Git Internals', 'Branching Topologies', 'Interactive Rebase', 'GitHub Actions'],
        "description": "Interactive rebase (`git rebase -i`), squashing commits, `git cherry-pick`, `git reset` (soft, mixed, hard), `git reflog` recovery, and `git bisect` binary search debugging.",
        "category": "Git & GitHub",
        "level": "advanced",
        "estimated_hours": 16,
        "thumbnail_url": "/assets/courses/git-rebase.png",
        "modules": [
            {
                "id": "mod-git-4-1",
                "title": "Module 1: Interactive Rebase, Reflog & Binary Search Debugging",
                "description": "Rewriting commit history, recovering lost commits with reflog, and automating regression isolation with bisect.",
                "order": 1,
                "lesson_ids": ["git-interactive-rebase-squash-fixup", "git-reflog-recovery-bisect-debugging"]
            }
        ]
    },
    {
        "id": "course-git-lvl5",
        "title": "Git Level 5: Production GitHub Actions CI/CD & DevSecOps",
        "slug": "git-level-5-github-actions-cicd",
        "domain": "github",
        "color": "#F59E0B",
        "icon": "GitBranch",
        "is_published": True,
        "skills_taught": ['Git Internals', 'Branching Topologies', 'Interactive Rebase', 'GitHub Actions'],
        "description": "GitHub Actions workflow syntax, matrix builds, automated test pipelines, secrets management, CodeQL security scanning, and automated multi-platform desktop release pipelines.",
        "category": "Git & GitHub",
        "level": "expert",
        "estimated_hours": 18,
        "thumbnail_url": "/assets/courses/git-actions.png",
        "modules": [
            {
                "id": "mod-git-5-1",
                "title": "Module 1: Automated CI/CD Pipelines & Release Engineering",
                "description": "Workflow runners, composite actions, matrix cross-compilation, and release tagging automation.",
                "order": 1,
                "lesson_ids": ["git-actions-workflow-matrix-builds", "git-cicd-release-automation-codeql"]
            }
        ]
    }
]

LESSONS_DATA = [
    {
        "id": "git-internals-blobs-trees-commits",
        "title": "Git Internals: Blobs, Trees, Commits & Directed Acyclic Graphs",
        "slug": "git-internals-blobs-trees-commits",
        "domain": "github",
        "color": "#F59E0B",
        "icon": "GitBranch",
        "is_published": True,
        "skills_taught": ['Git Internals', 'Branching Topologies', 'Interactive Rebase', 'GitHub Actions'],
        "course_id": "course-git-lvl1",
        "order": 1,
        "xp_reward": 50,
        "visual_diagram_type": "two_pointers_array",
        "content": """# Git Object Database (`.git/objects`)

Git is a content-addressable filesystem. Every object is identified by its SHA-1 hash:
1. **Blob**: Stores raw file contents (uncompressed snapshot).
2. **Tree**: Represents a directory, linking filenames and file permissions to blob/tree hashes.
3. **Commit**: Points to a top-level Tree hash, parent commit hash(es), author, committer, and commit message.
4. **Annotated Tag**: Object pointing to a specific commit with cryptographic GPG signature.
"""
    },
    {
        "id": "git-three-trees-staging-workflow",
        "title": "The Three Trees: Working Directory, Index & Head",
        "slug": "git-three-trees-staging-workflow",
        "domain": "github",
        "color": "#F59E0B",
        "icon": "GitBranch",
        "is_published": True,
        "skills_taught": ['Git Internals', 'Branching Topologies', 'Interactive Rebase', 'GitHub Actions'],
        "course_id": "course-git-lvl1",
        "order": 2,
        "xp_reward": 55,
        "visual_diagram_type": "two_pointers_array",
        "content": """# Working Directory -> Staging Index -> HEAD

- `git add <file>`: Creates a blob object in `.git/objects` and records its hash in the `.git/index` staging area.
- `git commit`: Builds trees from `.git/index` and creates a new commit object pointing to previous `HEAD`.
- `git diff`: Compares Working Directory vs Index.
- `git diff --staged`: Compares Index vs HEAD.
"""
    },
    {
        "id": "git-branch-pointers-switch-merge",
        "title": "Branch Pointers, HEAD & Fast-Forward Merging",
        "slug": "git-branch-pointers-switch-merge",
        "domain": "github",
        "color": "#F59E0B",
        "icon": "GitBranch",
        "is_published": True,
        "skills_taught": ['Git Internals', 'Branching Topologies', 'Interactive Rebase', 'GitHub Actions'],
        "course_id": "course-git-lvl2",
        "order": 1,
        "xp_reward": 60,
        "visual_diagram_type": "two_pointers_array",
        "content": """# Branches Are Lightweight 41-Byte Pointers

A Git branch is simply a text file in `.git/refs/heads/<branch>` containing a 40-character commit hash.
`HEAD` is a symbolic reference in `.git/HEAD` pointing to the active branch ref (`ref: refs/heads/main`).
"""
    },
    {
        "id": "git-merge-conflicts-resolution-strategies",
        "title": "3-Way Merge Commits & Conflict Resolution",
        "slug": "git-merge-conflicts-resolution-strategies",
        "domain": "github",
        "color": "#F59E0B",
        "icon": "GitBranch",
        "is_published": True,
        "skills_taught": ['Git Internals', 'Branching Topologies', 'Interactive Rebase', 'GitHub Actions'],
        "course_id": "course-git-lvl2",
        "order": 2,
        "xp_reward": 65,
        "visual_diagram_type": "two_pointers_array",
        "content": """# 3-Way Merge Algorithm (ORT / Recursive)

Finds the Lowest Common Ancestor (LCA) commit. If both branches modified the same line relative to LCA, Git inserts conflict markers:
```text
<<<<<<< HEAD
const API_URL = "https://api.prod.com";
=======
const API_URL = "https://api.staging.com";
>>>>>>> feature/staging-url
```
"""
    },
    {
        "id": "git-remotes-fetch-pull-tracking",
        "title": "Remote Tracking Branches & Upstream Synchronization",
        "slug": "git-remotes-fetch-pull-tracking",
        "domain": "github",
        "color": "#F59E0B",
        "icon": "GitBranch",
        "is_published": True,
        "skills_taught": ['Git Internals', 'Branching Topologies', 'Interactive Rebase', 'GitHub Actions'],
        "course_id": "course-git-lvl3",
        "order": 1,
        "xp_reward": 65,
        "visual_diagram_type": "two_pointers_array",
        "content": """# Remote Tracking (`origin/main`)

`git fetch origin` downloads new objects and updates `refs/remotes/origin/main` without touching your local working directory.
"""
    },
    {
        "id": "git-pull-rebase-force-with-lease",
        "title": "Clean Pulls with Rebase & --force-with-lease",
        "slug": "git-pull-rebase-force-with-lease",
        "domain": "github",
        "color": "#F59E0B",
        "icon": "GitBranch",
        "is_published": True,
        "skills_taught": ['Git Internals', 'Branching Topologies', 'Interactive Rebase', 'GitHub Actions'],
        "course_id": "course-git-lvl3",
        "order": 2,
        "xp_reward": 70,
        "visual_diagram_type": "two_pointers_array",
        "content": """# Why You Should Use `git push --force-with-lease`

Unlike dangerous `git push --force` which overwrites remote changes blindly, `--force-with-lease` verifies that the remote ref matches your local remote-tracking ref before overwriting, preventing teammate commit loss.
"""
    },
    {
        "id": "git-interactive-rebase-squash-fixup",
        "title": "Interactive Rebase, Commit Squashing & History Polishing",
        "slug": "git-interactive-rebase-squash-fixup",
        "domain": "github",
        "color": "#F59E0B",
        "icon": "GitBranch",
        "is_published": True,
        "skills_taught": ['Git Internals', 'Branching Topologies', 'Interactive Rebase', 'GitHub Actions'],
        "course_id": "course-git-lvl4",
        "order": 1,
        "xp_reward": 80,
        "visual_diagram_type": "two_pointers_array",
        "content": """# Interactive Rebase (`git rebase -i HEAD~N`)

Commands:
- `pick`: Use commit
- `reword`: Change commit message
- `squash`: Meld into previous commit and combine messages
- `fixup`: Meld into previous commit, discarding this message
- `drop`: Remove commit entirely
"""
    },
    {
        "id": "git-reflog-recovery-bisect-debugging",
        "title": "Reflog Time-Travel Recovery & Git Bisect Binary Search",
        "slug": "git-reflog-recovery-bisect-debugging",
        "domain": "github",
        "color": "#F59E0B",
        "icon": "GitBranch",
        "is_published": True,
        "skills_taught": ['Git Internals', 'Branching Topologies', 'Interactive Rebase', 'GitHub Actions'],
        "course_id": "course-git-lvl4",
        "order": 2,
        "xp_reward": 85,
        "visual_diagram_type": "two_pointers_array",
        "content": """# `git reflog` and `git bisect`

- **`git reflog`**: Logs every time `HEAD` moved in your local repository. Even if you accidentally ran `git reset --hard`, you can recover lost commits: `git reset --hard HEAD@{2}`.
- **`git bisect`**: Performs binary search across commit history to pinpoint the exact commit that introduced a bug in $O(\\log N)$ test runs.
"""
    },
    {
        "id": "git-actions-workflow-matrix-builds",
        "title": "GitHub Actions: Matrix Cross-Compilation & CI Runners",
        "slug": "git-actions-workflow-matrix-builds",
        "domain": "github",
        "color": "#F59E0B",
        "icon": "GitBranch",
        "is_published": True,
        "skills_taught": ['Git Internals', 'Branching Topologies', 'Interactive Rebase', 'GitHub Actions'],
        "course_id": "course-git-lvl5",
        "order": 1,
        "xp_reward": 90,
        "visual_diagram_type": "two_pointers_array",
        "content": """# GitHub Actions CI Matrix Workflows

Building native desktop binaries across `windows-latest`, `macos-latest`, and `ubuntu-latest` simultaneously in parallel runners.
"""
    },
    {
        "id": "git-cicd-release-automation-codeql",
        "title": "Automated Semantic Releases, CodeQL & Branch Protection",
        "slug": "git-cicd-release-automation-codeql",
        "domain": "github",
        "color": "#F59E0B",
        "icon": "GitBranch",
        "is_published": True,
        "skills_taught": ['Git Internals', 'Branching Topologies', 'Interactive Rebase', 'GitHub Actions'],
        "course_id": "course-git-lvl5",
        "order": 2,
        "xp_reward": 95,
        "visual_diagram_type": "two_pointers_array",
        "content": """# Enterprise GitHub Engineering

Automated release drafting on tag pushes, Static Application Security Testing (SAST) with CodeQL, and enforcing required status checks on protected branches.
"""
    }
]

QUIZZES_DATA = [
    {
        "id": "quiz-git-lvl1",
        "lesson_id": "git-internals-blobs-trees-commits",
        "title": "Git Internals & Workflow Diagnostic",
        "passing_score": 80,
        "questions": [
            {
                "id": "q-git-1-1",
                "question": "What does a Git Tree object represent in the object database?",
                "options": [
                    "A raw binary file",
                    "A directory structure linking filenames and permissions to blob/tree SHA hashes",
                    "A commit message string",
                    "A remote repository URL"
                ],
                "correct_option_index": 1,
                "explanation": "A Tree object represents a directory snapshot, containing metadata and SHA-1 pointers to blobs (files) and sub-trees (subdirectories)."
            }
        ]
    }
]

SKILLS_DATA = [
    {
        "id": "skill-git-mastery",
        "name": "Git & GitHub Release Engineering",
        "category": "Git & GitHub",
        "level": 1,
        "unlocked": True,
        "progress": 0.0,
        "prerequisites": [],
        "description": "Master Git internals, interactive rebase, reflog recovery, and GitHub Actions CI/CD."
    }
]
