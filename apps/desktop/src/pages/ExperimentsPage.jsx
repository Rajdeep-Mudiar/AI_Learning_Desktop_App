import React, { useState, useEffect } from 'react';
import { datasetService } from '../services/datasetService';
import { experimentService } from '../services/experimentService';
import ConfusionMatrixHeatmap from '../components/experiments/ConfusionMatrixHeatmap';
import ROCCurveChart from '../components/experiments/ROCCurveChart';
import ExperimentComparisonModal from '../components/experiments/ExperimentComparisonModal';

export default function ExperimentsPage() {
  const [datasets, setDatasets] = useState([]);
  const [selectedDatasetId, setSelectedDatasetId] = useState('iris');
  const [datasetProfile, setDatasetProfile] = useState(null);

  // Model & Task
  const [taskType, setTaskType] = useState('classification'); // 'classification' | 'regression'
  const [modelType, setModelType] = useState('random_forest_classifier');
  const [experimentName, setExperimentName] = useState('');

  // Preprocessing
  const [scaling, setScaling] = useState('standard');
  const [imputation, setImputation] = useState('mean');
  const [testSize, setTestSize] = useState(0.2);

  // Hyperparameters
  const [hyperparams, setHyperparams] = useState({
    n_estimators: 100,
    max_depth: 6,
    min_samples_split: 2,
    C: 1.0,
    alpha: 1.0,
    n_neighbors: 5,
    kernel: 'rbf',
    criterion: 'gini',
    weights: 'uniform',
  });

  // State
  const [training, setTraining] = useState(false);
  const [activeResult, setActiveResult] = useState(null);
  const [error, setError] = useState(null);

  // History & Comparison
  const [experimentsHistory, setExperimentsHistory] = useState([]);
  const [selectedForComparison, setSelectedForComparison] = useState([]);
  const [showComparisonModal, setShowComparisonModal] = useState(false);
  const [comparisonData, setComparisonData] = useState([]);

  useEffect(() => {
    loadDatasets();
    loadHistory();
  }, []);

  useEffect(() => {
    if (selectedDatasetId) {
      loadProfile(selectedDatasetId);
    }
  }, [selectedDatasetId]);

  const loadDatasets = async () => {
    try {
      const data = await datasetService.getDatasets();
      setDatasets(data);
    } catch (err) {
      console.error(err);
    }
  };

  const loadProfile = async (id) => {
    try {
      const p = await datasetService.getDatasetProfile(id);
      setDatasetProfile(p);
      setTaskType(p.task_type);
      if (p.task_type === 'classification') {
        setModelType('random_forest_classifier');
      } else {
        setModelType('random_forest_regressor');
      }
    } catch (err) {
      console.error(err);
    }
  };

  const loadHistory = async () => {
    try {
      const history = await experimentService.getExperiments();
      setExperimentsHistory(history);
    } catch (err) {
      console.error(err);
    }
  };

  const handleHyperparamChange = (key, value) => {
    setHyperparams((prev) => ({ ...prev, [key]: value }));
  };

  const handleTrain = async (e) => {
    e.preventDefault();
    setTraining(true);
    setError(null);
    try {
      const payload = {
        dataset_id: selectedDatasetId,
        model_type: modelType,
        task_type: taskType,
        hyperparameters: hyperparams,
        preprocessing: {
          scaling,
          imputation,
          test_size: parseFloat(testSize),
          random_state: 42,
        },
        experiment_name: experimentName.trim() || undefined,
      };

      const result = await experimentService.trainExperiment(payload);
      setActiveResult(result);
      await loadHistory();
    } catch (err) {
      setError(err.message || 'Training experiment failed.');
    } finally {
      setTraining(false);
    }
  };

  const toggleComparisonSelect = (expId) => {
    setSelectedForComparison((prev) =>
      prev.includes(expId) ? prev.filter((id) => id !== expId) : [...prev, expId]
    );
  };

  const openComparisonModal = async () => {
    if (selectedForComparison.length < 2) return;
    try {
      const res = await experimentService.compareExperiments(selectedForComparison);
      setComparisonData(res.experiments);
      setShowComparisonModal(true);
    } catch (err) {
      console.error(err);
    }
  };

  return (
    <div className="container" style={{ paddingBottom: 'var(--space-2xl)' }}>
      {/* Page Header */}
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', marginBottom: 'var(--space-xl)' }}>
        <div>
          <h1 style={{ fontSize: 'var(--font-2xl)', fontWeight: 800, margin: '0 0 var(--space-xs) 0', color: 'var(--color-text-main)' }}>
            ML Experimentation Lab & Benchmark
          </h1>
          <p style={{ margin: 0, color: 'var(--color-text-muted)', fontSize: 'var(--font-sm)' }}>
            Configure data transformations, tune algorithm hyperparameters, evaluate performance, and inspect diagnostics.
          </p>
        </div>
        {selectedForComparison.length >= 2 && (
          <button onClick={openComparisonModal} className="btn btn-primary" style={{ display: 'flex', alignItems: 'center', gap: 'var(--space-xs)' }}>
            <span>⚖️</span> Compare {selectedForComparison.length} Models Side-by-Side
          </button>
        )}
      </div>

      <div style={{ display: 'grid', gridTemplateColumns: '380px 1fr', gap: 'var(--space-xl)', alignItems: 'start' }}>
        {/* Left Column: Experiment Controls Form */}
        <form onSubmit={handleTrain} className="card" style={{ padding: 'var(--space-lg)', display: 'flex', flexDirection: 'column', gap: 'var(--space-lg)' }}>
          <h3 style={{ margin: 0, fontSize: 'var(--font-md)', color: 'var(--color-text-main)', borderBottom: '1px solid var(--color-border)', paddingBottom: 'var(--space-xs)' }}>
            Experiment Configuration
          </h3>

          {/* Experiment Name */}
          <div>
            <label style={{ display: 'block', fontSize: 'var(--font-xs)', fontWeight: 600, marginBottom: '4px' }}>
              Experiment Name (Optional)
            </label>
            <input
              type="text"
              className="input"
              placeholder="e.g. Tuned RF with Standard Scaling"
              value={experimentName}
              onChange={(e) => setExperimentName(e.target.value)}
            />
          </div>

          {/* Dataset Selection */}
          <div>
            <label style={{ display: 'block', fontSize: 'var(--font-xs)', fontWeight: 600, marginBottom: '4px' }}>
              Target Dataset
            </label>
            <select
              className="input"
              value={selectedDatasetId}
              onChange={(e) => setSelectedDatasetId(e.target.value)}
            >
              {datasets.map((d) => (
                <option key={d.id} value={d.id}>
                  {d.name} ({d.task_type})
                </option>
              ))}
            </select>
          </div>

          {/* Model Architecture */}
          <div>
            <label style={{ display: 'block', fontSize: 'var(--font-xs)', fontWeight: 600, marginBottom: '4px' }}>
              Algorithm Model
            </label>
            <select
              className="input"
              value={modelType}
              onChange={(e) => setModelType(e.target.value)}
            >
              {taskType === 'classification' ? (
                <>
                  <option value="random_forest_classifier">Random Forest Classifier</option>
                  <option value="logistic_regression">Logistic Regression</option>
                  <option value="svm_classifier">Support Vector Classifier (SVM)</option>
                  <option value="knn_classifier">K-Nearest Neighbors (KNN)</option>
                  <option value="decision_tree_classifier">Decision Tree Classifier</option>
                </>
              ) : (
                <>
                  <option value="random_forest_regressor">Random Forest Regressor</option>
                  <option value="linear_regression">Linear Regression (OLS)</option>
                  <option value="ridge_regression">Ridge Regression (L2)</option>
                  <option value="lasso_regression">Lasso Regression (L1)</option>
                  <option value="knn_regressor">K-Nearest Neighbors Regressor</option>
                </>
              )}
            </select>
          </div>

          {/* Preprocessing Settings */}
          <div style={{ background: 'var(--color-surface-elevated)', padding: 'var(--space-md)', borderRadius: 'var(--radius-md)', border: '1px solid var(--color-border)' }}>
            <h4 style={{ margin: '0 0 var(--space-sm) 0', fontSize: 'var(--font-xs)', textTransform: 'uppercase', color: 'var(--color-primary-400)' }}>
              Preprocessing Pipeline
            </h4>
            <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: 'var(--space-sm)' }}>
              <div>
                <label style={{ fontSize: '11px', color: 'var(--color-text-muted)', display: 'block', marginBottom: '2px' }}>Scaling</label>
                <select className="input" value={scaling} onChange={(e) => setScaling(e.target.value)} style={{ fontSize: 'var(--font-xs)' }}>
                  <option value="standard">Standard (Z-score)</option>
                  <option value="minmax">Min-Max [0, 1]</option>
                  <option value="robust">Robust (IQR)</option>
                  <option value="none">None</option>
                </select>
              </div>
              <div>
                <label style={{ fontSize: '11px', color: 'var(--color-text-muted)', display: 'block', marginBottom: '2px' }}>Imputation</label>
                <select className="input" value={imputation} onChange={(e) => setImputation(e.target.value)} style={{ fontSize: 'var(--font-xs)' }}>
                  <option value="mean">Mean Value</option>
                  <option value="median">Median Value</option>
                  <option value="drop">Drop NaNs</option>
                </select>
              </div>
            </div>

            <div style={{ marginTop: 'var(--space-sm)' }}>
              <div style={{ display: 'flex', justifyContent: 'space-between', fontSize: '11px', color: 'var(--color-text-muted)' }}>
                <span>Test Split</span>
                <span>{Math.round(testSize * 100)}% Test / {Math.round((1 - testSize) * 100)}% Train</span>
              </div>
              <input
                type="range"
                min="0.1"
                max="0.4"
                step="0.05"
                value={testSize}
                onChange={(e) => setTestSize(e.target.value)}
                style={{ width: '100%', marginTop: '4px' }}
              />
            </div>
          </div>

          {/* Hyperparameter Controls */}
          <div style={{ background: 'var(--color-surface-elevated)', padding: 'var(--space-md)', borderRadius: 'var(--radius-md)', border: '1px solid var(--color-border)' }}>
            <h4 style={{ margin: '0 0 var(--space-sm) 0', fontSize: 'var(--font-xs)', textTransform: 'uppercase', color: 'var(--color-primary-400)' }}>
              Hyperparameters
            </h4>

            {(modelType === 'random_forest_classifier' || modelType === 'random_forest_regressor') && (
              <div style={{ display: 'flex', flexDirection: 'column', gap: 'var(--space-sm)' }}>
                <div>
                  <div style={{ display: 'flex', justifyContent: 'space-between', fontSize: '11px' }}>
                    <span>n_estimators (Trees)</span>
                    <strong>{hyperparams.n_estimators}</strong>
                  </div>
                  <input
                    type="range"
                    min="10"
                    max="300"
                    step="10"
                    value={hyperparams.n_estimators}
                    onChange={(e) => handleHyperparamChange('n_estimators', parseInt(e.target.value))}
                    style={{ width: '100%' }}
                  />
                </div>
                <div>
                  <div style={{ display: 'flex', justifyContent: 'space-between', fontSize: '11px' }}>
                    <span>max_depth</span>
                    <strong>{hyperparams.max_depth || 'Unlimited'}</strong>
                  </div>
                  <input
                    type="range"
                    min="1"
                    max="20"
                    step="1"
                    value={hyperparams.max_depth || 10}
                    onChange={(e) => handleHyperparamChange('max_depth', parseInt(e.target.value))}
                    style={{ width: '100%' }}
                  />
                </div>
              </div>
            )}

            {(modelType === 'logistic_regression' || modelType === 'svm_classifier') && (
              <div style={{ display: 'flex', flexDirection: 'column', gap: 'var(--space-sm)' }}>
                <div>
                  <div style={{ display: 'flex', justifyContent: 'space-between', fontSize: '11px' }}>
                    <span>Regularization (C)</span>
                    <strong>{hyperparams.C}</strong>
                  </div>
                  <input
                    type="range"
                    min="0.01"
                    max="10.0"
                    step="0.05"
                    value={hyperparams.C}
                    onChange={(e) => handleHyperparamChange('C', parseFloat(e.target.value))}
                    style={{ width: '100%' }}
                  />
                </div>
                {modelType === 'svm_classifier' && (
                  <div>
                    <label style={{ fontSize: '11px', color: 'var(--color-text-muted)', display: 'block', marginBottom: '2px' }}>Kernel</label>
                    <select
                      className="input"
                      value={hyperparams.kernel}
                      onChange={(e) => handleHyperparamChange('kernel', e.target.value)}
                      style={{ fontSize: 'var(--font-xs)' }}
                    >
                      <option value="rbf">RBF (Gaussian)</option>
                      <option value="linear">Linear</option>
                      <option value="poly">Polynomial (deg 3)</option>
                    </select>
                  </div>
                )}
              </div>
            )}

            {(modelType === 'knn_classifier' || modelType === 'knn_regressor') && (
              <div style={{ display: 'flex', flexDirection: 'column', gap: 'var(--space-sm)' }}>
                <div>
                  <div style={{ display: 'flex', justifyContent: 'space-between', fontSize: '11px' }}>
                    <span>n_neighbors (K)</span>
                    <strong>{hyperparams.n_neighbors}</strong>
                  </div>
                  <input
                    type="range"
                    min="1"
                    max="25"
                    step="2"
                    value={hyperparams.n_neighbors}
                    onChange={(e) => handleHyperparamChange('n_neighbors', parseInt(e.target.value))}
                    style={{ width: '100%' }}
                  />
                </div>
              </div>
            )}

            {(modelType === 'ridge_regression' || modelType === 'lasso_regression') && (
              <div style={{ display: 'flex', flexDirection: 'column', gap: 'var(--space-sm)' }}>
                <div>
                  <div style={{ display: 'flex', justifyContent: 'space-between', fontSize: '11px' }}>
                    <span>Regularization Alpha (λ)</span>
                    <strong>{hyperparams.alpha}</strong>
                  </div>
                  <input
                    type="range"
                    min="0.01"
                    max="10.0"
                    step="0.1"
                    value={hyperparams.alpha}
                    onChange={(e) => handleHyperparamChange('alpha', parseFloat(e.target.value))}
                    style={{ width: '100%' }}
                  />
                </div>
              </div>
            )}

            {modelType === 'decision_tree_classifier' && (
              <div style={{ display: 'flex', flexDirection: 'column', gap: 'var(--space-sm)' }}>
                <div>
                  <div style={{ display: 'flex', justifyContent: 'space-between', fontSize: '11px' }}>
                    <span>max_depth</span>
                    <strong>{hyperparams.max_depth}</strong>
                  </div>
                  <input
                    type="range"
                    min="1"
                    max="15"
                    step="1"
                    value={hyperparams.max_depth}
                    onChange={(e) => handleHyperparamChange('max_depth', parseInt(e.target.value))}
                    style={{ width: '100%' }}
                  />
                </div>
                <div>
                  <label style={{ fontSize: '11px', color: 'var(--color-text-muted)', display: 'block', marginBottom: '2px' }}>Split Criterion</label>
                  <select
                    className="input"
                    value={hyperparams.criterion}
                    onChange={(e) => handleHyperparamChange('criterion', e.target.value)}
                    style={{ fontSize: 'var(--font-xs)' }}
                  >
                    <option value="gini">Gini Impurity</option>
                    <option value="entropy">Information Gain (Entropy)</option>
                  </select>
                </div>
              </div>
            )}
          </div>

          {error && (
            <div style={{ padding: 'var(--space-sm)', background: 'rgba(239, 68, 68, 0.1)', color: '#ef4444', borderRadius: 'var(--radius-sm)', fontSize: 'var(--font-xs)' }}>
              {error}
            </div>
          )}

          <button
            type="submit"
            disabled={training}
            className="btn btn-primary"
            style={{ width: '100%', padding: '12px', fontSize: 'var(--font-sm)', fontWeight: 700 }}
          >
            {training ? 'Training Model & Benchmarking...' : '⚡ Fit & Evaluate Model'}
          </button>
        </form>

        {/* Right Column: Results & Visualizations */}
        <div style={{ display: 'flex', flexDirection: 'column', gap: 'var(--space-xl)' }}>
          {activeResult ? (
            <div className="card" style={{ padding: 'var(--space-lg)', display: 'flex', flexDirection: 'column', gap: 'var(--space-lg)' }}>
              {/* Header */}
              <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', borderBottom: '1px solid var(--color-border)', paddingBottom: 'var(--space-sm)' }}>
                <div>
                  <h3 style={{ margin: 0, fontSize: 'var(--font-lg)', color: 'var(--color-text-main)' }}>
                    {activeResult.experiment_name}
                  </h3>
                  <span style={{ fontSize: 'var(--font-xs)', color: 'var(--color-text-muted)' }}>
                    Trained in {activeResult.metrics.training_time_ms} ms on {activeResult.dataset_id}
                  </span>
                </div>
                <span
                  style={{
                    padding: '4px 12px',
                    borderRadius: 'var(--radius-full)',
                    background: 'rgba(16, 185, 129, 0.15)',
                    color: '#10b981',
                    fontSize: 'var(--font-xs)',
                    fontWeight: 700,
                  }}
                >
                  Completed
                </span>
              </div>

              {/* Metric Badges */}
              <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(130px, 1fr))', gap: 'var(--space-sm)' }}>
                {activeResult.task_type === 'classification' ? (
                  <>
                    <div style={{ background: 'var(--color-surface-elevated)', padding: 'var(--space-sm)', borderRadius: 'var(--radius-sm)', textAlign: 'center' }}>
                      <div style={{ fontSize: '10px', color: 'var(--color-text-muted)' }}>Test Accuracy</div>
                      <div style={{ fontSize: 'var(--font-xl)', fontWeight: 800, color: '#10b981' }}>
                        {(activeResult.metrics.accuracy * 100).toFixed(1)}%
                      </div>
                    </div>
                    <div style={{ background: 'var(--color-surface-elevated)', padding: 'var(--space-sm)', borderRadius: 'var(--radius-sm)', textAlign: 'center' }}>
                      <div style={{ fontSize: '10px', color: 'var(--color-text-muted)' }}>Train Accuracy</div>
                      <div style={{ fontSize: 'var(--font-xl)', fontWeight: 800, color: 'var(--color-text-main)' }}>
                        {(activeResult.metrics.train_score * 100).toFixed(1)}%
                      </div>
                    </div>
                    <div style={{ background: 'var(--color-surface-elevated)', padding: 'var(--space-sm)', borderRadius: 'var(--radius-sm)', textAlign: 'center' }}>
                      <div style={{ fontSize: '10px', color: 'var(--color-text-muted)' }}>F1-Score</div>
                      <div style={{ fontSize: 'var(--font-xl)', fontWeight: 800, color: 'var(--color-primary-400)' }}>
                        {activeResult.metrics.f1_score}
                      </div>
                    </div>
                    <div style={{ background: 'var(--color-surface-elevated)', padding: 'var(--space-sm)', borderRadius: 'var(--radius-sm)', textAlign: 'center' }}>
                      <div style={{ fontSize: '10px', color: 'var(--color-text-muted)' }}>Precision</div>
                      <div style={{ fontSize: 'var(--font-xl)', fontWeight: 800, color: 'var(--color-text-main)' }}>
                        {activeResult.metrics.precision}
                      </div>
                    </div>
                  </>
                ) : (
                  <>
                    <div style={{ background: 'var(--color-surface-elevated)', padding: 'var(--space-sm)', borderRadius: 'var(--radius-sm)', textAlign: 'center' }}>
                      <div style={{ fontSize: '10px', color: 'var(--color-text-muted)' }}>R² Score</div>
                      <div style={{ fontSize: 'var(--font-xl)', fontWeight: 800, color: '#10b981' }}>
                        {activeResult.metrics.r2_score}
                      </div>
                    </div>
                    <div style={{ background: 'var(--color-surface-elevated)', padding: 'var(--space-sm)', borderRadius: 'var(--radius-sm)', textAlign: 'center' }}>
                      <div style={{ fontSize: '10px', color: 'var(--color-text-muted)' }}>MSE</div>
                      <div style={{ fontSize: 'var(--font-xl)', fontWeight: 800, color: 'var(--color-text-main)' }}>
                        {activeResult.metrics.mse}
                      </div>
                    </div>
                    <div style={{ background: 'var(--color-surface-elevated)', padding: 'var(--space-sm)', borderRadius: 'var(--radius-sm)', textAlign: 'center' }}>
                      <div style={{ fontSize: '10px', color: 'var(--color-text-muted)' }}>RMSE</div>
                      <div style={{ fontSize: 'var(--font-xl)', fontWeight: 800, color: 'var(--color-primary-400)' }}>
                        {activeResult.metrics.rmse}
                      </div>
                    </div>
                    <div style={{ background: 'var(--color-surface-elevated)', padding: 'var(--space-sm)', borderRadius: 'var(--radius-sm)', textAlign: 'center' }}>
                      <div style={{ fontSize: '10px', color: 'var(--color-text-muted)' }}>MAE</div>
                      <div style={{ fontSize: 'var(--font-xl)', fontWeight: 800, color: 'var(--color-text-main)' }}>
                        {activeResult.metrics.mae}
                      </div>
                    </div>
                  </>
                )}
              </div>

              {/* Overfitting analysis */}
              {(() => {
                const trainAcc = activeResult.metrics.train_score || 0;
                const testAcc = activeResult.metrics.test_score || 0;
                const diff = Math.abs(trainAcc - testAcc);
                if (diff > 0.15) {
                  return (
                    <div style={{ padding: 'var(--space-sm) var(--space-md)', background: 'rgba(239, 68, 68, 0.08)', borderLeft: '4px solid #ef4444', borderRadius: 'var(--radius-sm)', fontSize: 'var(--font-xs)' }}>
                      <strong>⚠️ Overfitting Warning:</strong> Model performs significantly better on training set (Δ {diff.toFixed(2)}). Consider increasing regularization, limiting tree depth, or collecting more samples.
                    </div>
                  );
                }
                return null;
              })()}

              {/* Visual Diagnostics Grid */}
              <div style={{ display: 'grid', gridTemplateColumns: activeResult.roc_curve ? '1fr 1fr' : '1fr', gap: 'var(--space-lg)' }}>
                {activeResult.confusion_matrix && (
                  <div style={{ background: 'var(--color-surface-elevated)', padding: 'var(--space-md)', borderRadius: 'var(--radius-md)' }}>
                    <ConfusionMatrixHeatmap data={activeResult.confusion_matrix} />
                  </div>
                )}
                {activeResult.roc_curve && (
                  <div style={{ background: 'var(--color-surface-elevated)', padding: 'var(--space-md)', borderRadius: 'var(--radius-md)' }}>
                    <ROCCurveChart data={activeResult.roc_curve} />
                  </div>
                )}
              </div>

              {/* Feature Importance Bars */}
              {activeResult.feature_importances && activeResult.feature_importances.length > 0 && (
                <div>
                  <h4 style={{ margin: '0 0 var(--space-sm) 0', fontSize: 'var(--font-sm)' }}>
                    Feature Importance Ranking
                  </h4>
                  <div style={{ display: 'flex', flexDirection: 'column', gap: '6px' }}>
                    {activeResult.feature_importances.slice(0, 6).map((item, idx) => (
                      <div key={idx} style={{ display: 'flex', alignItems: 'center', gap: 'var(--space-sm)', fontSize: 'var(--font-xs)' }}>
                        <span style={{ minWidth: '120px', textAlign: 'right', fontWeight: 500, overflow: 'hidden', textOverflow: 'ellipsis', whiteSpace: 'nowrap' }}>
                          {item.feature}
                        </span>
                        <div style={{ flex: 1, height: '8px', background: 'var(--color-surface-elevated)', borderRadius: 'var(--radius-full)', overflow: 'hidden' }}>
                          <div
                            style={{
                              height: '100%',
                              width: `${Math.min(100, Math.max(5, item.importance * 100))}%`,
                              background: 'var(--color-primary-400)',
                              borderRadius: 'var(--radius-full)',
                            }}
                          />
                        </div>
                        <span style={{ minWidth: '45px', color: 'var(--color-text-muted)', fontFamily: 'var(--font-mono)' }}>
                          {(item.importance * 100).toFixed(1)}%
                        </span>
                      </div>
                    ))}
                  </div>
                </div>
              )}
            </div>
          ) : (
            <div className="card" style={{ padding: 'var(--space-2xl)', textAlign: 'center', color: 'var(--color-text-muted)' }}>
              <div style={{ fontSize: 'var(--font-2xl)', marginBottom: 'var(--space-xs)' }}>🧪</div>
              <h3 style={{ margin: 0, fontSize: 'var(--font-md)' }}>No Active Experiment Run</h3>
              <p style={{ margin: '4px 0 0', fontSize: 'var(--font-xs)' }}>
                Configure parameters on the left and click "Fit & Evaluate Model" to benchmark.
              </p>
            </div>
          )}

          {/* Experiment History Table */}
          <div className="card" style={{ padding: 'var(--space-lg)' }}>
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: 'var(--space-md)' }}>
              <h3 style={{ margin: 0, fontSize: 'var(--font-md)' }}>
                Experiment Run Registry ({experimentsHistory.length})
              </h3>
              <span style={{ fontSize: 'var(--font-xs)', color: 'var(--color-text-muted)' }}>
                Select 2+ runs to compare
              </span>
            </div>

            {experimentsHistory.length === 0 ? (
              <div style={{ color: 'var(--color-text-muted)', fontSize: 'var(--font-xs)', textAlign: 'center', padding: 'var(--space-md)' }}>
                No past experiments found. Train your first model above!
              </div>
            ) : (
              <div style={{ overflowX: 'auto' }}>
                <table style={{ width: '100%', borderCollapse: 'collapse', textAlign: 'left', fontSize: 'var(--font-xs)' }}>
                  <thead>
                    <tr style={{ background: 'var(--color-surface-elevated)', borderBottom: '1px solid var(--color-border)' }}>
                      <th style={{ padding: '8px' }}>Compare</th>
                      <th style={{ padding: '8px' }}>Experiment</th>
                      <th style={{ padding: '8px' }}>Dataset</th>
                      <th style={{ padding: '8px' }}>Model</th>
                      <th style={{ padding: '8px' }}>Score</th>
                      <th style={{ padding: '8px' }}>Time</th>
                      <th style={{ padding: '8px' }}>Action</th>
                    </tr>
                  </thead>
                  <tbody>
                    {experimentsHistory.map((exp) => {
                      const isSelected = selectedForComparison.includes(exp.id);
                      const isClassification = exp.task_type === 'classification';
                      const scoreStr = isClassification
                        ? `${((exp.metrics.accuracy || 0) * 100).toFixed(1)}% Acc`
                        : `${exp.metrics.r2_score || 0} R²`;

                      return (
                        <tr key={exp.id} style={{ borderBottom: '1px solid var(--color-border)' }}>
                          <td style={{ padding: '8px' }}>
                            <input
                              type="checkbox"
                              checked={isSelected}
                              onChange={() => toggleComparisonSelect(exp.id)}
                            />
                          </td>
                          <td style={{ padding: '8px', fontWeight: 600 }}>{exp.experiment_name}</td>
                          <td style={{ padding: '8px', color: 'var(--color-text-muted)' }}>{exp.dataset_id}</td>
                          <td style={{ padding: '8px', color: 'var(--color-primary-400)' }}>{exp.model_type}</td>
                          <td style={{ padding: '8px', fontWeight: 700, color: '#10b981' }}>{scoreStr}</td>
                          <td style={{ padding: '8px', color: 'var(--color-text-muted)' }}>{exp.metrics.training_time_ms} ms</td>
                          <td style={{ padding: '8px' }}>
                            <button
                              onClick={() => setActiveResult(exp)}
                              className="btn btn-secondary"
                              style={{ padding: '2px 8px', fontSize: '10px' }}
                            >
                              Inspect
                            </button>
                          </td>
                        </tr>
                      );
                    })}
                  </tbody>
                </table>
              </div>
            )}
          </div>
        </div>
      </div>

      {/* Side-by-Side Comparison Modal */}
      {showComparisonModal && (
        <ExperimentComparisonModal
          experiments={comparisonData}
          onClose={() => setShowComparisonModal(false)}
        />
      )}
    </div>
  );
}
