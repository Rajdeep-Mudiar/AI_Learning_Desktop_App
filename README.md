# AI Learning Lab

**AI Learning Lab** is a desktop-first interactive artificial intelligence education and experimentation platform. Designed for students, university learners, ML practitioners, and AI researchers, the platform combines interactive simulations, sandboxed Python programming, context-aware AI tutoring, ML experimentation, neural visualizers, ArXiv paper reproduction workspaces, mock interview simulators, and career roadmaps into an integrated desktop developer environment.

---

## Central Educational Philosophy

> **Learn → Visualize → Experiment → Code → Break → Debug → Challenge → Build → Evaluate → Explain**

---

## Architectural Stack

* **Desktop Application**: Tauri 2.0 native container with responsive desktop windowing.
* **Frontend UI**: React 18, Vite, Monaco Editor (`@monaco-editor/react`), Lucide Icons, Plain CSS Design System (zero Tailwind CSS, custom design tokens, dark/light modes, glassmorphic surfaces).
* **Backend Services**: FastAPI (Python 3.13), Pydantic v2, JWT Security with bcrypt, async MongoDB (Motor/PyMongo), and in-memory mock fallback.
* **Math & AI Computation Engines**: PyTorch, Scikit-learn, NumPy, SciPy.
* **Sandbox Execution**: Subprocess runner with resource caps (5s timeout, peak memory measurement).
* **AI Tutor Engine**: Local LLM integration (Ollama `llama3`, `mistral`, `deepseek`) with rule-based fallback.

---

## Complete Feature Matrix (Phases 1 through 11)

| Phase | Feature Module | URL Route | Key Capabilities |
| :--- | :--- | :--- | :--- |
| **Phase 1** | **Core Learning & Quizzes** | `/learn`, `/skills`, `/dashboard` | Syllabus, lesson reader, multi-stage quizzes with step-by-step math breakdowns, interactive skill tree graph. |
| **Phase 2** | **Algorithm Lab & Diagnostics** | `/algorithms`, `/break-the-model` | Interactive canvas visualizers (Linear Regression, KNN Voronoi, Decision Tree, K-Means, PCA) & "Break the Model" diagnostic scenarios. |
| **Phase 3** | **Python Coding Sandbox** | `/playground`, `/challenges` | Monaco Python editor, isolated execution engine with memory/timeout caps, autograded algorithmic coding challenges. |
| **Phase 4** | **Datasets & ML Experiments** | `/datasets`, `/experiments` | Dataset explorer (Moons, Circles, Iris, Housing, Custom CSV), side-by-side model training (RF, SVM, Ridge), Confusion Matrices, ROC curves. |
| **Phase 5** | **Deep Learning Lab** | `/deep-learning` | MLP forward/backward pass gradient flow graphs, CNN spatial 2D convolution & pooling filters, Transformer Multi-Head self-attention heatmaps. |
| **Phase 6** | **Context-Aware AI Tutor** | `/tutor` | Socratic mentor personas (Socratic, Code Debugger, Mathematical Rigor, Intuitive Visualizer), auto-extracting current UI and code context. |
| **Phase 7** | **Projects, Viva & Badges** | `/projects`, `/achievements` | Real-world AI project specifications, AI oral defense viva exam simulator, PDF/JSON portfolio exporter, gamified achievement badges. |
| **Phase 8/9** | **AI Research Mode** | `/research`, `/research/:paperId` | ArXiv paper catalog (*Transformers*, *ResNet*, *LoRA*), mathematical equation explainer cards, step-by-step reproduction pipeline, linked Markdown scratchpad. |
| **Phase 10** | **Interviews & Hackathons** | `/interviews`, `/hackathons` | Mock technical interview tracks with multi-rubric scoring & hire recommendations; competitive timed hackathons with live automated leaderboards. |
| **Phase 11** | **Community & Career Paths** | `/community`, `/career` | Student discussion forum with code snippets and upvoting; career readiness roadmap mapping against market demand and salary benchmarks. |

---

## Quick-Start Guide & How to Run

### Prerequisites
* **Python 3.10+** (Python 3.13 recommended)
* **Node.js 18+** & npm
* *(Optional)* **Rust & Cargo** (Download from [rustup.rs](https://rustup.rs/) — only needed for running the native Tauri desktop window)
* *(Optional)* **MongoDB** (running on `localhost:27017` — fallback mock engine included)
* *(Optional)* **Ollama** (running on `localhost:11434` for local AI models)

---

### Step 1: Initial Setup (One-Time)

#### Backend Setup:
```powershell
cd apps\backend
python -m venv venv
.\venv\Scripts\python.exe -m pip install --upgrade pip
.\venv\Scripts\pip.exe install -r requirements.txt
```

#### Frontend Setup:
```powershell
cd ..\desktop
npm install
```

#### Seed Initial Curriculum & Quizzes:
```powershell
cd ..\..
$env:PYTHONPATH="f:\Vibe_Coding\AI_Learning_Desktop_App\apps\backend"
.\apps\backend\venv\Scripts\python.exe apps\backend\app\seed\seed_runner.py
```

---

### Step 2: Running the Application

You can run the application in any of the following 3 ways:

#### Option A: One-Click Launch (Windows Batch File)
From the project root:
```cmd
.\scripts\start_dev.bat
```
*(Or simply double-click `scripts\start_dev.bat` in File Explorer)*

---

#### Option B: Browser Web Mode (Fast & Recommended for Development)

1. **Terminal 1 (Backend - FastAPI)**:
   ```powershell
   cd apps\backend
   .\venv\Scripts\python.exe main.py
   ```
   > Backend runs at: `http://127.0.0.1:8000` (Interactive API Swagger Docs: `http://127.0.0.1:8000/docs`)

2. **Terminal 2 (Frontend - Vite Dev Server)**:
   ```powershell
   cd apps\desktop
   npm run dev
   ```
   > Open your browser at: **`http://localhost:5173`**

---

#### Option C: Native Tauri Desktop Window Mode

1. **Terminal 1 (Backend - FastAPI)**:
   ```powershell
   cd apps\backend
   .\venv\Scripts\python.exe main.py
   ```

2. **Terminal 2 (Native Desktop Window)**:
   ```powershell
   cd apps\desktop
   npm run tauri dev
   ```

---

### Common Gotchas & Troubleshooting

* **`ModuleNotFoundError: No module named 'jose'` (or other package)**:
  * You are running the global/conda python instead of the virtual environment. Use `.\venv\Scripts\python.exe main.py` or activate the environment via `.\venv\Scripts\Activate.ps1`.
* **`npm error ENOENT: Could not read package.json`**:
  * The root folder does not contain `package.json`. Make sure to navigate into `apps\desktop` first before running `npm` commands (`cd apps\desktop`).
* **`cargo: program not found`**:
  * Rust is not installed or not in your current terminal's PATH. Install Rust from [rustup.rs](https://rustup.rs/) and refresh PATH with `$env:Path += ";$env:USERPROFILE\.cargo\bin"`, or simply use **Option B (Browser Web Mode)** which requires no Rust setup.

---

### Step 3: Running Automated Tests

Run the full automated test suite (28 comprehensive test suites across auth, learning, simulations, sandboxes, and AI tutor):
```powershell
.\scripts\run_tests.bat
```
Or directly in PowerShell:
```powershell
$env:PYTHONPATH="f:\Vibe_Coding\AI_Learning_Desktop_App\apps\backend"
.\apps\backend\venv\Scripts\pytest.exe tests/ -v
```

---

### Step 4: Build Production Desktop Executable (.exe / .msi)
```cmd
.\scripts\build_desktop.bat
```

---

## Key Keyboard Shortcuts & Navigation

* `Ctrl + Enter` (in Monaco Editor): Run Python code in sandbox.
* `Esc`: Close modals (Viva simulator, portfolio export, dataset uploader, post creator).
* Navigation sidebar links to all 16 specialized laboratories and modules.
