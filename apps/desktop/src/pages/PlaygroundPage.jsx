import React, { useState } from 'react';
import { Play, RotateCcw, FileCode, Plus, Sparkles, Download, Clock, Terminal } from 'lucide-react';
import MonacoCodeEditor from '../components/playground/MonacoCodeEditor';
import OutputTerminal from '../components/playground/OutputTerminal';
import { sandboxService } from '../services/sandboxService';
import LoadingSpinner from '../components/common/LoadingSpinner';

const TEMPLATES = {
  numpy_basics: `# NumPy Vectorized Matrix Computing
import numpy as np

# Create 2D feature matrix X (4 samples x 3 features)
X = np.array([
    [1.0, 2.0, 3.0],
    [4.0, 5.0, 6.0],
    [7.0, 8.0, 9.0],
    [10.0, 11.0, 12.0]
])

# Weights vector w
w = np.array([0.5, -0.2, 0.8])

# Matrix-vector dot product: y_hat = X @ w
y_hat = X @ w

print("Feature Matrix X shape:", X.shape)
print("Weights vector w:", w)
print("Predictions y_hat:", y_hat)
print("Mean Prediction:", np.mean(y_hat))
`,
  linear_regression: `# Linear Regression from Scratch
import numpy as np

# Synthetic linear dataset
np.random.seed(42)
X = 2 * np.random.rand(50, 1)
y = 3.5 * X + 1.2 + np.random.randn(50, 1) * 0.1

# 1. Closed-Form OLS with Bias Trick: X_b = [1, X]
X_b = np.c_[np.ones((50, 1)), X]
best_w = np.linalg.pinv(X_b.T @ X_b) @ X_b.T @ y

print("--- OLS Closed Form Solution ---")
print(f"Computed Bias (intercept): {best_w[0][0]:.3f} (True: 1.200)")
print(f"Computed Slope (weight):   {best_w[1][0]:.3f} (True: 3.500)")

# 2. Mean Squared Error
y_pred = X_b @ best_w
mse = np.mean((y_pred - y) ** 2)
print(f"Final Model MSE Loss:      {mse:.5f}")
`,
  attention_mechanism: `# Scaled Dot-Product Attention in NumPy
import numpy as np

def softmax(x):
    e_x = np.exp(x - np.max(x, axis=-1, keepdims=True))
    return e_x / np.sum(e_x, axis=-1, keepdims=True)

# 3 Tokens, Projection Dimension = 4
Q = np.array([[1.0, 0.0, 1.0, 0.0], [0.0, 1.0, 0.0, 1.0], [1.0, 1.0, 0.0, 0.0]])
K = Q.copy()
V = np.array([[10.0, 0.0], [0.0, 20.0], [5.0, 5.0]])

d_k = Q.shape[-1]
scores = (Q @ K.T) / np.sqrt(d_k)
attention_weights = softmax(scores)
output = attention_weights @ V

print("Attention Weights Matrix (3x3):")
print(np.round(attention_weights, 3))
print("\\nAttended Context Representation (3x2):")
print(np.round(output, 2))
`
};

export default function PlaygroundPage() {
  const [activeTab, setActiveTab] = useState('main.py');
  const [files, setFiles] = useState({
    'main.py': TEMPLATES.numpy_basics,
    'model.py': `# Model helper module\ndef get_hyperparameters():\n    return {"learning_rate": 0.01, "epochs": 100}\n`,
  });
  const [executing, setExecuting] = useState(false);
  const [executionResult, setExecutionResult] = useState(null);

  const handleCodeChange = (newCode) => {
    setFiles((prev) => ({
      ...prev,
      [activeTab]: newCode,
    }));
  };

  const handleLoadTemplate = (key) => {
    if (TEMPLATES[key]) {
      setFiles((prev) => ({
        ...prev,
        [activeTab]: TEMPLATES[key],
      }));
    }
  };

  const handleRunCode = async () => {
    setExecuting(true);
    try {
      const codeToRun = files['main.py'];
      const auxiliaryFiles = { ...files };
      delete auxiliaryFiles['main.py'];

      const res = await sandboxService.executeCode(codeToRun, 6.0, auxiliaryFiles);
      setExecutionResult(res);
    } catch (err) {
      setExecutionResult({
        execution_id: 'err',
        status: 'error',
        stdout: '',
        stderr: err.message || 'Execution failed',
        exit_code: -1,
        duration_ms: 0,
      });
    } finally {
      setExecuting(false);
    }
  };

  const handleDownloadFile = () => {
    const blob = new Blob([files[activeTab]], { type: 'text/plain' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = activeTab;
    a.click();
    URL.revokeObjectURL(url);
  };

  return (
    <div className="animate-fade-in" style={{ height: 'calc(100vh - 120px)', display: 'flex', flexDirection: 'column' }}>
      {/* Top Action Bar */}
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: 14, flexShrink: 0 }}>
        <div>
          <div style={{ display: 'flex', alignItems: 'center', gap: 8, marginBottom: 2 }}>
            <span className="badge badge-blue">Python 3.13 Sandbox</span>
            <span style={{ fontSize: '0.75rem', color: 'var(--text-muted)' }}>• Isolated Subprocess Environment</span>
          </div>
          <h1 style={{ fontSize: '1.45rem' }}>Python Coding Playground</h1>
        </div>

        <div style={{ display: 'flex', alignItems: 'center', gap: 10 }}>
          {/* Starter Templates */}
          <select
            className="form-input"
            onChange={(e) => handleLoadTemplate(e.target.value)}
            defaultValue=""
            style={{ padding: '6px 12px', fontSize: '0.8rem' }}
          >
            <option value="" disabled>Load AI Template...</option>
            <option value="numpy_basics">NumPy Matrix Operations</option>
            <option value="linear_regression">Linear Regression from Scratch</option>
            <option value="attention_mechanism">Self-Attention Mechanism</option>
          </select>

          <button
            onClick={handleDownloadFile}
            className="btn btn-secondary btn-sm"
            title="Download active file"
          >
            <Download size={14} /> Export
          </button>

          {/* Run Button */}
          <button
            onClick={handleRunCode}
            className="btn btn-primary"
            disabled={executing}
            style={{ padding: '8px 20px', gap: 8 }}
          >
            <Play size={16} fill="currentColor" />
            <span>{executing ? 'Executing...' : 'Run Code (F5)'}</span>
          </button>
        </div>
      </div>

      {/* Editor & Terminal Split Workspace */}
      <div style={{ flex: 1, display: 'grid', gridTemplateColumns: '1.3fr 1fr', gap: 16, minHeight: 0 }}>
        {/* Editor Container */}
        <div className="card" style={{ padding: 0, display: 'flex', flexDirection: 'column', overflow: 'hidden' }}>
          {/* File Tabs */}
          <div style={{
            display: 'flex',
            alignItems: 'center',
            background: 'var(--bg-secondary)',
            borderBottom: '1px solid var(--border-subtle)',
            padding: '4px 8px',
            gap: 4
          }}>
            {Object.keys(files).map((fname) => (
              <button
                key={fname}
                onClick={() => setActiveTab(fname)}
                className={`btn btn-sm ${activeTab === fname ? 'btn-primary' : 'btn-ghost'}`}
                style={{ fontSize: '0.78rem', padding: '4px 10px', gap: 6 }}
              >
                <FileCode size={13} />
                <span>{fname}</span>
              </button>
            ))}
          </div>

          {/* Monaco Editor */}
          <div style={{ flex: 1, minHeight: 0 }}>
            <MonacoCodeEditor
              code={files[activeTab] || ''}
              onChange={handleCodeChange}
              language="python"
            />
          </div>
        </div>

        {/* Output Terminal */}
        <div style={{ height: '100%', minHeight: 0 }}>
          <OutputTerminal
            result={executionResult}
            onClear={() => setExecutionResult(null)}
          />
        </div>
      </div>
    </div>
  );
}
