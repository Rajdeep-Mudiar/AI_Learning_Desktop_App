import React from 'react';

export default function ExperimentComparisonModal({ experiments, onClose }) {
  if (!experiments || experiments.length === 0) return null;

  const isClassification = experiments[0].task_type === 'classification';

  return (
    <div
      style={{
        position: 'fixed',
        top: 0,
        left: 0,
        right: 0,
        bottom: 0,
        backgroundColor: 'rgba(0, 0, 0, 0.75)',
        backdropFilter: 'blur(6px)',
        zIndex: 9999,
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'center',
        padding: 'var(--space-md)',
      }}
      onClick={onClose}
    >
      <div
        style={{
          background: 'var(--color-surface)',
          border: '1px solid var(--color-border)',
          borderRadius: 'var(--radius-lg)',
          width: '100%',
          maxWidth: '900px',
          maxHeight: '90vh',
          overflowY: 'auto',
          boxShadow: 'var(--shadow-xl)',
          padding: 'var(--space-lg)',
          display: 'flex',
          flexDirection: 'column',
          gap: 'var(--space-lg)',
        }}
        onClick={(e) => e.stopPropagation()}
      >
        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
          <div>
            <h3 style={{ margin: 0, fontSize: 'var(--font-lg)', color: 'var(--color-text-main)' }}>
              Side-by-Side Model Comparison
            </h3>
            <p style={{ margin: '4px 0 0', fontSize: 'var(--font-xs)', color: 'var(--color-text-muted)' }}>
              Comparing {experiments.length} experiment runs
            </p>
          </div>
          <button
            onClick={onClose}
            className="btn btn-secondary"
            style={{ padding: '4px 10px', fontSize: 'var(--font-sm)' }}
          >
            Close ✕
          </button>
        </div>

        {/* Metrics Overview Table */}
        <div>
          <h4 style={{ fontSize: 'var(--font-sm)', color: 'var(--color-text-main)', marginBottom: 'var(--space-sm)' }}>
            Evaluation Metrics
          </h4>
          <div style={{ overflowX: 'auto' }}>
            <table style={{ width: '100%', borderCollapse: 'collapse', textAlign: 'left', fontSize: 'var(--font-xs)' }}>
              <thead>
                <tr style={{ background: 'var(--color-surface-elevated)', borderBottom: '1px solid var(--color-border)' }}>
                  <th style={{ padding: '10px' }}>Attribute</th>
                  {experiments.map((exp) => (
                    <th key={exp.id} style={{ padding: '10px', color: 'var(--color-primary-400)', fontWeight: 600 }}>
                      {exp.experiment_name}
                      <div style={{ fontSize: '10px', color: 'var(--color-text-muted)', fontWeight: 400 }}>
                        {exp.model_type} ({exp.id})
                      </div>
                    </th>
                  ))}
                </tr>
              </thead>
              <tbody>
                <tr style={{ borderBottom: '1px solid var(--color-border)' }}>
                  <td style={{ padding: '8px 10px', fontWeight: 600 }}>Dataset</td>
                  {experiments.map((exp) => (
                    <td key={exp.id} style={{ padding: '8px 10px' }}>{exp.dataset_id}</td>
                  ))}
                </tr>

                {isClassification ? (
                  <>
                    <tr style={{ borderBottom: '1px solid var(--color-border)' }}>
                      <td style={{ padding: '8px 10px', fontWeight: 600 }}>Test Accuracy</td>
                      {experiments.map((exp) => (
                        <td key={exp.id} style={{ padding: '8px 10px', fontWeight: 700, color: '#10b981' }}>
                          {exp.metrics.accuracy !== undefined ? `${(exp.metrics.accuracy * 100).toFixed(1)}%` : 'N/A'}
                        </td>
                      ))}
                    </tr>
                    <tr style={{ borderBottom: '1px solid var(--color-border)' }}>
                      <td style={{ padding: '8px 10px', fontWeight: 600 }}>Train Accuracy</td>
                      {experiments.map((exp) => (
                        <td key={exp.id} style={{ padding: '8px 10px' }}>
                          {exp.metrics.train_score !== undefined ? `${(exp.metrics.train_score * 100).toFixed(1)}%` : 'N/A'}
                        </td>
                      ))}
                    </tr>
                    <tr style={{ borderBottom: '1px solid var(--color-border)' }}>
                      <td style={{ padding: '8px 10px', fontWeight: 600 }}>F1-Score (Weighted)</td>
                      {experiments.map((exp) => (
                        <td key={exp.id} style={{ padding: '8px 10px' }}>{exp.metrics.f1_score ?? 'N/A'}</td>
                      ))}
                    </tr>
                    <tr style={{ borderBottom: '1px solid var(--color-border)' }}>
                      <td style={{ padding: '8px 10px', fontWeight: 600 }}>Precision / Recall</td>
                      {experiments.map((exp) => (
                        <td key={exp.id} style={{ padding: '8px 10px' }}>
                          {exp.metrics.precision ?? 'N/A'} / {exp.metrics.recall ?? 'N/A'}
                        </td>
                      ))}
                    </tr>
                  </>
                ) : (
                  <>
                    <tr style={{ borderBottom: '1px solid var(--color-border)' }}>
                      <td style={{ padding: '8px 10px', fontWeight: 600 }}>R² Score</td>
                      {experiments.map((exp) => (
                        <td key={exp.id} style={{ padding: '8px 10px', fontWeight: 700, color: '#10b981' }}>
                          {exp.metrics.r2_score ?? 'N/A'}
                        </td>
                      ))}
                    </tr>
                    <tr style={{ borderBottom: '1px solid var(--color-border)' }}>
                      <td style={{ padding: '8px 10px', fontWeight: 600 }}>MSE / RMSE</td>
                      {experiments.map((exp) => (
                        <td key={exp.id} style={{ padding: '8px 10px' }}>
                          {exp.metrics.mse ?? 'N/A'} / {exp.metrics.rmse ?? 'N/A'}
                        </td>
                      ))}
                    </tr>
                    <tr style={{ borderBottom: '1px solid var(--color-border)' }}>
                      <td style={{ padding: '8px 10px', fontWeight: 600 }}>MAE</td>
                      {experiments.map((exp) => (
                        <td key={exp.id} style={{ padding: '8px 10px' }}>{exp.metrics.mae ?? 'N/A'}</td>
                      ))}
                    </tr>
                  </>
                )}

                <tr style={{ borderBottom: '1px solid var(--color-border)' }}>
                  <td style={{ padding: '8px 10px', fontWeight: 600 }}>Train Time</td>
                  {experiments.map((exp) => (
                    <td key={exp.id} style={{ padding: '8px 10px' }}>{exp.metrics.training_time_ms} ms</td>
                  ))}
                </tr>

                <tr style={{ borderBottom: '1px solid var(--color-border)' }}>
                  <td style={{ padding: '8px 10px', fontWeight: 600 }}>Overfitting Check (Train - Test Gap)</td>
                  {experiments.map((exp) => {
                    const diff = Math.abs((exp.metrics.train_score || 0) - (exp.metrics.test_score || 0));
                    const isSevere = diff > 0.15;
                    return (
                      <td key={exp.id} style={{ padding: '8px 10px', color: isSevere ? '#ef4444' : '#10b981' }}>
                        Δ {diff.toFixed(3)} {isSevere ? '⚠️ Overfitting Risk' : '✓ Well Generalised'}
                      </td>
                    );
                  })}
                </tr>

                <tr style={{ borderBottom: '1px solid var(--color-border)' }}>
                  <td style={{ padding: '8px 10px', fontWeight: 600 }}>Scaling / Imputation</td>
                  {experiments.map((exp) => (
                    <td key={exp.id} style={{ padding: '8px 10px' }}>
                      {exp.preprocessing.scaling} / {exp.preprocessing.imputation}
                    </td>
                  ))}
                </tr>

                <tr>
                  <td style={{ padding: '8px 10px', fontWeight: 600 }}>Hyperparameters</td>
                  {experiments.map((exp) => (
                    <td key={exp.id} style={{ padding: '8px 10px' }}>
                      <pre style={{ margin: 0, fontSize: '11px', background: 'rgba(0,0,0,0.2)', padding: '4px 6px', borderRadius: 'var(--radius-sm)' }}>
                        {JSON.stringify(exp.hyperparameters, null, 1)}
                      </pre>
                    </td>
                  ))}
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>
  );
}
