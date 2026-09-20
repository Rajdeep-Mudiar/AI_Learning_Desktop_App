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

## Quick-Start Guide & How to Run the Desktop App

### Prerequisites
* **Python 3.10+** (Python 3.13 recommended)
* **Node.js 18+** & npm
* **Rust & Cargo** (Download installer from [rustup.rs](https://rustup.rs/) — required for compiling the native Tauri desktop container)
* *(Optional)* **MongoDB** (running on `localhost:27017` — automatic fallback mock engine included)
* *(Optional)* **Ollama** (running on `localhost:11434` for local AI models)

---

### Quick Launch Commands

#### Method 1: One-Click Windows Launch (Recommended)
From the root project directory:
```cmd
.\scripts\start_dev.bat
```
*(Or double-click [`scripts/start_dev.bat`](file:///f:/Vibe_Coding/AI_Learning_Desktop_App/scripts/start_dev.bat) in File Explorer)*

---

#### Method 2: Running the Native Desktop App (Tauri Window)
Open two PowerShell terminals:

**Terminal 1: Start Backend**
```powershell
cd apps\backend
.\venv\Scripts\python.exe main.py
```
> Backend starts at: `http://127.0.0.1:8000` (API Docs: `http://127.0.0.1:8000/docs`)

**Terminal 2: Launch Tauri Desktop Window**
```powershell
cd apps\desktop
$env:Path += ";$env:USERPROFILE\.cargo\bin"
npm run tauri dev
```
> This opens the native desktop application window with access to all 5 learning tracks (**AI/ML, Web Dev, App Dev, System Design, Git/GitHub**).

---

#### Method 3: Running in Web Browser Mode (Fast UI Dev)

**Terminal 1: Start Backend**
```powershell
cd apps\backend
.\venv\Scripts\python.exe main.py
```

**Terminal 2: Start Frontend**
```powershell
cd apps\desktop
npm run dev
```
> Open **`http://localhost:5173`** in your web browser.

---

### Step-by-Step Initial Setup (First Time Only)

#### 1. Setup Backend Python Virtual Environment
```powershell
cd apps\backend
python -m venv venv
.\venv\Scripts\python.exe -m pip install --upgrade pip
.\venv\Scripts\pip.exe install -r requirements.txt
```

#### 2. Install Desktop & Frontend Node Packages
```powershell
cd ..\desktop
npm install
```

#### 3. Seed All 5 Domain Curriculums & Quizzes
```powershell
cd ..\..
$env:PYTHONPATH="f:\Vibe_Coding\AI_Learning_Desktop_App\apps\backend"
.\apps\backend\venv\Scripts\python.exe apps\backend\app\seed\seed_runner.py
```

---

### Common Gotchas & Troubleshooting

* **`cargo: program not found`**:
  * Rust is not installed or not loaded in your current terminal. Run `$env:Path += ";$env:USERPROFILE\.cargo\bin"` in PowerShell after installing from [rustup.rs](https://rustup.rs/).
* **`npm error ENOENT: Could not read package.json`**:
  * Ensure you navigate into the `apps\desktop` directory first (`cd apps\desktop`) before running `npm` commands.
* **`ModuleNotFoundError: No module named 'jose'`**:
  * You are running global Python instead of the virtual environment. Always execute using `.\venv\Scripts\python.exe main.py` or activate the virtual environment via `.\venv\Scripts\Activate.ps1`.

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
