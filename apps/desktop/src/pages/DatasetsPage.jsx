import React, { useState, useEffect } from 'react';
import { datasetService } from '../services/datasetService';

export default function DatasetsPage() {
  const [datasets, setDatasets] = useState([]);
  const [selectedId, setSelectedId] = useState('iris');
  const [profile, setProfile] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [activeTab, setActiveTab] = useState('stats'); // 'stats' | 'correlation' | 'diagnostics' | 'preview'

  // Custom Upload Modal State
  const [showUploadModal, setShowUploadModal] = useState(false);
  const [uploadName, setUploadName] = useState('');
  const [uploadTask, setUploadTask] = useState('classification');
  const [uploadTarget, setUploadTarget] = useState('');
  const [uploadCsv, setUploadCsv] = useState('');
  const [uploadLoading, setUploadLoading] = useState(false);
  const [uploadError, setUploadError] = useState(null);

  useEffect(() => {
    loadDatasetsCatalog();
  }, []);

  useEffect(() => {
    if (selectedId) {
      loadProfile(selectedId);
    }
  }, [selectedId]);

  const loadDatasetsCatalog = async () => {
    try {
      const list = await datasetService.getDatasets();
      setDatasets(list);
    } catch (err) {
      console.error(err);
      setError('Failed to load datasets list.');
    }
  };

  const loadProfile = async (id) => {
    try {
      setLoading(true);
      setError(null);
      const data = await datasetService.getDatasetProfile(id);
      setProfile(data);
    } catch (err) {
      console.error(err);
      setError(err.message || 'Failed to profile dataset.');
    } finally {
      setLoading(false);
    }
  };

  const handleFileUpload = (e) => {
    const file = e.target.files?.[0];
    if (!file) return;
    const reader = new FileReader();
    reader.onload = (event) => {
      setUploadCsv(event.target.result);
      if (!uploadName) {
        setUploadName(file.name.replace(/\.[^/.]+$/, ''));
      }
    };
    reader.readAsText(file);
  };

  const handleUploadSubmit = async (e) => {
    e.preventDefault();
    if (!uploadCsv.trim()) {
      setUploadError('Please provide CSV content or select a file.');
      return;
    }
    try {
      setUploadLoading(true);
      setUploadError(null);
      const res = await datasetService.uploadCustomDataset({
        name: uploadName || 'Custom Dataset',
        task_type: uploadTask,
        target_column: uploadTarget || null,
        csv_content: uploadCsv,
      });
      setShowUploadModal(false);
      await loadDatasetsCatalog();
      setSelectedId(res.id);
      setProfile(res);
    } catch (err) {
      setUploadError(err.message || 'Failed to upload dataset.');
    } finally {
      setUploadLoading(false);
    }
  };

  return (
    <div className="container" style={{ paddingBottom: 'var(--space-2xl)' }}>
      {/* Page Header */}
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', marginBottom: 'var(--space-xl)' }}>
        <div>
          <h1 style={{ fontSize: 'var(--font-2xl)', fontWeight: 800, margin: '0 0 var(--space-xs) 0', color: 'var(--color-text-main)' }}>
            Dataset Explorer & Diagnostics
          </h1>
          <p style={{ margin: 0, color: 'var(--color-text-muted)', fontSize: 'var(--font-sm)' }}>
            Inspect distributions, correlation structures, class imbalances, and data quality warnings across ML benchmarks.
          </p>
        </div>
        <button
          onClick={() => setShowUploadModal(true)}
          className="btn btn-primary"
          style={{ display: 'flex', alignItems: 'center', gap: 'var(--space-xs)' }}
        >
          <span>📁</span> Upload Custom CSV
        </button>
      </div>

      {/* Dataset Selector Chips */}
      <div style={{ display: 'flex', gap: 'var(--space-sm)', overflowX: 'auto', paddingBottom: 'var(--space-sm)', marginBottom: 'var(--space-lg)' }}>
        {datasets.map((d) => (
          <button
            key={d.id}
            onClick={() => setSelectedId(d.id)}
            style={{
              padding: '8px 16px',
              borderRadius: 'var(--radius-full)',
              border: selectedId === d.id ? '2px solid var(--color-primary-400)' : '1px solid var(--color-border)',
              background: selectedId === d.id ? 'rgba(99, 102, 241, 0.15)' : 'var(--color-surface)',
              color: selectedId === d.id ? 'var(--color-primary-400)' : 'var(--color-text-main)',
              fontWeight: selectedId === d.id ? 700 : 500,
              fontSize: 'var(--font-xs)',
              cursor: 'pointer',
              whiteSpace: 'nowrap',
              transition: 'all 0.15s ease',
            }}
          >
            {d.name} <span style={{ opacity: 0.7 }}>({d.num_rows} × {d.num_columns})</span>
          </button>
        ))}
      </div>

      {loading ? (
        <div style={{ padding: 'var(--space-2xl)', textAlign: 'center', color: 'var(--color-text-muted)' }}>
          Profiling dataset and calculating correlation matrix...
        </div>
      ) : error ? (
        <div style={{ padding: 'var(--space-lg)', background: 'rgba(239, 68, 68, 0.1)', border: '1px solid #ef4444', borderRadius: 'var(--radius-md)', color: '#ef4444' }}>
          {error}
        </div>
      ) : profile ? (
        <div style={{ display: 'flex', flexDirection: 'column', gap: 'var(--space-xl)' }}>
          {/* Metadata Cards */}
          <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(180px, 1fr))', gap: 'var(--space-md)' }}>
            <div className="card" style={{ padding: 'var(--space-md)' }}>
              <div style={{ fontSize: 'var(--font-xs)', color: 'var(--color-text-muted)' }}>Total Samples</div>
              <div style={{ fontSize: 'var(--font-xl)', fontWeight: 800, color: 'var(--color-primary-400)', marginTop: '4px' }}>
                {profile.num_rows.toLocaleString()}
              </div>
            </div>
            <div className="card" style={{ padding: 'var(--space-md)' }}>
              <div style={{ fontSize: 'var(--font-xs)', color: 'var(--color-text-muted)' }}>Features</div>
              <div style={{ fontSize: 'var(--font-xl)', fontWeight: 800, color: 'var(--color-text-main)', marginTop: '4px' }}>
                {profile.features.length}
              </div>
            </div>
            <div className="card" style={{ padding: 'var(--space-md)' }}>
              <div style={{ fontSize: 'var(--font-xs)', color: 'var(--color-text-muted)' }}>Task Type</div>
              <div style={{ fontSize: 'var(--font-md)', fontWeight: 700, color: '#10b981', marginTop: '6px', textTransform: 'capitalize' }}>
                {profile.task_type}
              </div>
            </div>
            <div className="card" style={{ padding: 'var(--space-md)' }}>
              <div style={{ fontSize: 'var(--font-xs)', color: 'var(--color-text-muted)' }}>Target Column</div>
              <div style={{ fontSize: 'var(--font-md)', fontWeight: 700, color: 'var(--color-text-main)', marginTop: '6px' }}>
                {profile.target_column || 'None'}
              </div>
            </div>
            <div className="card" style={{ padding: 'var(--space-md)' }}>
              <div style={{ fontSize: 'var(--font-xs)', color: 'var(--color-text-muted)' }}>Diagnostic Alerts</div>
              <div style={{ fontSize: 'var(--font-md)', fontWeight: 700, color: profile.diagnostic_warnings.length > 0 ? '#f59e0b' : '#10b981', marginTop: '6px' }}>
                {profile.diagnostic_warnings.length} issues detected
              </div>
            </div>
          </div>

          {/* Navigation Tabs */}
          <div style={{ display: 'flex', borderBottom: '1px solid var(--color-border)', gap: 'var(--space-md)' }}>
            {[
              { id: 'stats', label: '📊 Feature Statistics & Distributions' },
              { id: 'correlation', label: '🔥 Correlation Matrix' },
              { id: 'diagnostics', label: `⚠️ Data Diagnostics (${profile.diagnostic_warnings.length})` },
              { id: 'preview', label: '📄 Raw Data Sample' },
            ].map((tab) => (
              <button
                key={tab.id}
                onClick={() => setActiveTab(tab.id)}
                style={{
                  background: 'none',
                  border: 'none',
                  padding: '10px 16px',
                  color: activeTab === tab.id ? 'var(--color-primary-400)' : 'var(--color-text-muted)',
                  borderBottom: activeTab === tab.id ? '2px solid var(--color-primary-400)' : '2px solid transparent',
                  fontWeight: activeTab === tab.id ? 700 : 500,
                  fontSize: 'var(--font-sm)',
                  cursor: 'pointer',
                  transition: 'all 0.15s ease',
                }}
              >
                {tab.label}
              </button>
            ))}
          </div>

          {/* Tab 1: Stats */}
          {activeTab === 'stats' && (
            <div className="card" style={{ padding: 'var(--space-lg)', overflowX: 'auto' }}>
              <table style={{ width: '100%', borderCollapse: 'collapse', textAlign: 'left', fontSize: 'var(--font-xs)' }}>
                <thead>
                  <tr style={{ background: 'var(--color-surface-elevated)', borderBottom: '1px solid var(--color-border)' }}>
                    <th style={{ padding: '10px' }}>Column</th>
                    <th style={{ padding: '10px' }}>Type</th>
                    <th style={{ padding: '10px' }}>Missing</th>
                    <th style={{ padding: '10px' }}>Mean ± Std</th>
                    <th style={{ padding: '10px' }}>Min / Q25 / Med / Q75 / Max</th>
                    <th style={{ padding: '10px' }}>Skewness</th>
                    <th style={{ padding: '10px' }}>Sample Values</th>
                  </tr>
                </thead>
                <tbody>
                  {profile.columns_summary.map((col, idx) => (
                    <tr key={idx} style={{ borderBottom: '1px solid var(--color-border)' }}>
                      <td style={{ padding: '10px', fontWeight: 600, color: col.name === profile.target_column ? 'var(--color-primary-400)' : 'var(--color-text-main)' }}>
                        {col.name} {col.name === profile.target_column && <span style={{ fontSize: '10px', opacity: 0.7 }}>(Target)</span>}
                      </td>
                      <td style={{ padding: '10px', color: 'var(--color-text-muted)' }}>{col.data_type}</td>
                      <td style={{ padding: '10px', color: col.missing_count > 0 ? '#ef4444' : 'var(--color-text-muted)' }}>
                        {col.missing_count} ({(col.missing_ratio * 100).toFixed(1)}%)
                      </td>
                      <td style={{ padding: '10px' }}>
                        {col.mean !== null && col.mean !== undefined ? `${col.mean} ± ${col.std}` : '—'}
                      </td>
                      <td style={{ padding: '10px', fontFamily: 'var(--font-mono)' }}>
                        {col.min !== null ? `${col.min} / ${col.q25} / ${col.median} / ${col.q75} / ${col.max}` : '—'}
                      </td>
                      <td style={{ padding: '10px', color: col.skewness && Math.abs(col.skewness) > 1.5 ? '#f59e0b' : 'inherit' }}>
                        {col.skewness ?? '—'}
                      </td>
                      <td style={{ padding: '10px', color: 'var(--color-text-muted)', maxWidth: '180px', overflow: 'hidden', textOverflow: 'ellipsis', whiteSpace: 'nowrap' }}>
                        {col.sample_values?.join(', ')}
                      </td>
                    </tr>
                  ))}
                </tbody>
              </table>

              {/* Class distribution visual if classification */}
              {profile.class_distribution && (
                <div style={{ marginTop: 'var(--space-xl)', paddingTop: 'var(--space-lg)', borderTop: '1px solid var(--color-border)' }}>
                  <h4 style={{ fontSize: 'var(--font-sm)', margin: '0 0 var(--space-md) 0' }}>Class Target Distribution</h4>
                  <div style={{ display: 'flex', gap: 'var(--space-lg)', flexWrap: 'wrap' }}>
                    {Object.entries(profile.class_distribution).map(([cls, cnt]) => {
                      const total = profile.num_rows;
                      const pct = Math.round((cnt / total) * 100);
                      return (
                        <div key={cls} style={{ minWidth: '160px' }}>
                          <div style={{ display: 'flex', justifyContent: 'space-between', fontSize: 'var(--font-xs)', marginBottom: '4px' }}>
                            <span style={{ fontWeight: 600 }}>{cls}</span>
                            <span style={{ color: 'var(--color-text-muted)' }}>{cnt} ({pct}%)</span>
                          </div>
                          <div style={{ height: '8px', background: 'var(--color-surface-elevated)', borderRadius: 'var(--radius-full)', overflow: 'hidden' }}>
                            <div style={{ height: '100%', width: `${pct}%`, background: 'var(--color-primary-400)', borderRadius: 'var(--radius-full)' }} />
                          </div>
                        </div>
                      );
                    })}
                  </div>
                </div>
              )}
            </div>
          )}

          {/* Tab 2: Correlation */}
          {activeTab === 'correlation' && (
            <div className="card" style={{ padding: 'var(--space-lg)' }}>
              {profile.correlation_matrix ? (
                <div>
                  <h4 style={{ margin: '0 0 var(--space-sm) 0', fontSize: 'var(--font-sm)' }}>
                    Pearson Correlation Matrix (r ∈ [-1.0, 1.0])
                  </h4>
                  <p style={{ margin: '0 0 var(--space-md) 0', fontSize: 'var(--font-xs)', color: 'var(--color-text-muted)' }}>
                    Values close to 1.0 indicate strong positive linear association; values near -1.0 indicate inverse correlation.
                  </p>
                  <div style={{ overflowX: 'auto' }}>
                    <table style={{ borderCollapse: 'collapse', textAlign: 'center', fontSize: '11px' }}>
                      <thead>
                        <tr>
                          <th style={{ padding: '6px', borderBottom: '1px solid var(--color-border)' }}></th>
                          {profile.correlation_matrix.features.map((f, i) => (
                            <th key={i} style={{ padding: '6px', maxWidth: '80px', overflow: 'hidden', textOverflow: 'ellipsis', whiteSpace: 'nowrap', borderBottom: '1px solid var(--color-border)', color: 'var(--color-primary-400)' }} title={f}>
                              {f}
                            </th>
                          ))}
                        </tr>
                      </thead>
                      <tbody>
                        {profile.correlation_matrix.matrix.map((row, rIdx) => (
                          <tr key={rIdx}>
                            <td style={{ padding: '6px 12px', fontWeight: 600, textAlign: 'right', borderRight: '1px solid var(--color-border)' }}>
                              {profile.correlation_matrix.features[rIdx]}
                            </td>
                            {row.map((val, cIdx) => {
                              const isDiagonal = rIdx === cIdx;
                              let bg = 'rgba(255, 255, 255, 0.02)';
                              if (!isDiagonal) {
                                if (val > 0) {
                                  bg = `rgba(99, 102, 241, ${Math.abs(val) * 0.8})`;
                                } else if (val < 0) {
                                  bg = `rgba(239, 68, 68, ${Math.abs(val) * 0.8})`;
                                }
                              } else {
                                bg = 'rgba(99, 102, 241, 0.2)';
                              }
                              return (
                                <td
                                  key={cIdx}
                                  title={`${profile.correlation_matrix.features[rIdx]} & ${profile.correlation_matrix.features[cIdx]}: ${val}`}
                                  style={{
                                    padding: '8px 10px',
                                    background: bg,
                                    border: '1px solid var(--color-border)',
                                    fontWeight: isDiagonal ? 700 : 500,
                                  }}
                                >
                                  {val}
                                </td>
                              );
                            })}
                          </tr>
                        ))}
                      </tbody>
                    </table>
                  </div>
                </div>
              ) : (
                <div style={{ color: 'var(--color-text-muted)', fontSize: 'var(--font-xs)' }}>
                  Not enough numeric features to compute correlation matrix.
                </div>
              )}
            </div>
          )}

          {/* Tab 3: Diagnostics */}
          {activeTab === 'diagnostics' && (
            <div style={{ display: 'flex', flexDirection: 'column', gap: 'var(--space-md)' }}>
              {profile.diagnostic_warnings.length === 0 ? (
                <div className="card" style={{ padding: 'var(--space-xl)', textAlign: 'center', color: '#10b981' }}>
                  <div style={{ fontSize: 'var(--font-2xl)', marginBottom: 'var(--space-xs)' }}>✓</div>
                  <h3 style={{ margin: 0, fontSize: 'var(--font-md)' }}>Dataset is in Pristine Health</h3>
                  <p style={{ margin: '4px 0 0', fontSize: 'var(--font-xs)', color: 'var(--color-text-muted)' }}>
                    No multicollinearity, severe class imbalance, or missing value anomalies detected.
                  </p>
                </div>
              ) : (
                profile.diagnostic_warnings.map((warn, idx) => {
                  const borderCol = warn.severity === 'critical' ? '#ef4444' : warn.severity === 'warning' ? '#f59e0b' : '#3b82f6';
                  const bgCol = warn.severity === 'critical' ? 'rgba(239, 68, 68, 0.08)' : warn.severity === 'warning' ? 'rgba(245, 158, 11, 0.08)' : 'rgba(59, 130, 246, 0.08)';
                  return (
                    <div
                      key={idx}
                      className="card"
                      style={{
                        padding: 'var(--space-lg)',
                        borderLeft: `4px solid ${borderCol}`,
                        background: bgCol,
                        display: 'flex',
                        flexDirection: 'column',
                        gap: 'var(--space-xs)',
                      }}
                    >
                      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                        <h4 style={{ margin: 0, fontSize: 'var(--font-md)', color: 'var(--color-text-main)' }}>
                          {warn.title}
                        </h4>
                        <span style={{ fontSize: '10px', textTransform: 'uppercase', fontWeight: 700, padding: '2px 8px', borderRadius: 'var(--radius-full)', background: borderCol, color: '#ffffff' }}>
                          {warn.severity}
                        </span>
                      </div>
                      <p style={{ margin: 0, fontSize: 'var(--font-sm)', color: 'var(--color-text-main)' }}>
                        {warn.description}
                      </p>
                      <div style={{ marginTop: 'var(--space-xs)', padding: 'var(--space-sm)', background: 'var(--color-surface)', borderRadius: 'var(--radius-sm)', fontSize: 'var(--font-xs)' }}>
                        <strong>💡 AI Recommendation:</strong> {warn.recommendation}
                      </div>
                    </div>
                  );
                })
              )}
            </div>
          )}

          {/* Tab 4: Preview */}
          {activeTab === 'preview' && (
            <div className="card" style={{ padding: 'var(--space-lg)', overflowX: 'auto' }}>
              <h4 style={{ margin: '0 0 var(--space-md) 0', fontSize: 'var(--font-sm)' }}>
                Sample Records (First {profile.sample_rows.length} rows)
              </h4>
              <table style={{ width: '100%', borderCollapse: 'collapse', textAlign: 'left', fontSize: 'var(--font-xs)' }}>
                <thead>
                  <tr style={{ background: 'var(--color-surface-elevated)', borderBottom: '1px solid var(--color-border)' }}>
                    <th style={{ padding: '8px' }}>#</th>
                    {profile.columns_summary.map((col, i) => (
                      <th key={i} style={{ padding: '8px', color: col.name === profile.target_column ? 'var(--color-primary-400)' : 'var(--color-text-main)' }}>
                        {col.name}
                      </th>
                    ))}
                  </tr>
                </thead>
                <tbody>
                  {profile.sample_rows.map((row, rIdx) => (
                    <tr key={rIdx} style={{ borderBottom: '1px solid var(--color-border)' }}>
                      <td style={{ padding: '8px', color: 'var(--color-text-muted)' }}>{rIdx + 1}</td>
                      {profile.columns_summary.map((col, cIdx) => (
                        <td key={cIdx} style={{ padding: '8px' }}>
                          {row[col.name] !== null ? String(row[col.name]) : <span style={{ color: 'var(--color-text-muted)' }}>null</span>}
                        </td>
                      ))}
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          )}
        </div>
      ) : null}

      {/* Upload Custom Modal */}
      {showUploadModal && (
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
          onClick={() => setShowUploadModal(false)}
        >
          <div
            style={{
              background: 'var(--color-surface)',
              border: '1px solid var(--color-border)',
              borderRadius: 'var(--radius-lg)',
              width: '100%',
              maxWidth: '550px',
              padding: 'var(--space-lg)',
              boxShadow: 'var(--shadow-xl)',
            }}
            onClick={(e) => e.stopPropagation()}
          >
            <h3 style={{ margin: '0 0 var(--space-sm) 0', fontSize: 'var(--font-lg)' }}>Upload Custom Dataset</h3>
            <p style={{ margin: '0 0 var(--space-md) 0', fontSize: 'var(--font-xs)', color: 'var(--color-text-muted)' }}>
              Provide CSV headers and comma-delimited data for instant automated profiling.
            </p>

            {uploadError && (
              <div style={{ padding: 'var(--space-sm)', background: 'rgba(239, 68, 68, 0.1)', color: '#ef4444', borderRadius: 'var(--radius-sm)', marginBottom: 'var(--space-md)', fontSize: 'var(--font-xs)' }}>
                {uploadError}
              </div>
            )}

            <form onSubmit={handleUploadSubmit} style={{ display: 'flex', flexDirection: 'column', gap: 'var(--space-md)' }}>
              <div>
                <label style={{ display: 'block', fontSize: 'var(--font-xs)', fontWeight: 600, marginBottom: '4px' }}>Dataset Name</label>
                <input
                  type="text"
                  className="input"
                  placeholder="e.g. Customer Churn Data"
                  value={uploadName}
                  onChange={(e) => setUploadName(e.target.value)}
                  required
                />
              </div>

              <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: 'var(--space-md)' }}>
                <div>
                  <label style={{ display: 'block', fontSize: 'var(--font-xs)', fontWeight: 600, marginBottom: '4px' }}>Task Type</label>
                  <select
                    className="input"
                    value={uploadTask}
                    onChange={(e) => setUploadTask(e.target.value)}
                  >
                    <option value="classification">Classification</option>
                    <option value="regression">Regression</option>
                  </select>
                </div>
                <div>
                  <label style={{ display: 'block', fontSize: 'var(--font-xs)', fontWeight: 600, marginBottom: '4px' }}>Target Column (Optional)</label>
                  <input
                    type="text"
                    className="input"
                    placeholder="Defaults to last column"
                    value={uploadTarget}
                    onChange={(e) => setUploadTarget(e.target.value)}
                  />
                </div>
              </div>

              <div>
                <label style={{ display: 'block', fontSize: 'var(--font-xs)', fontWeight: 600, marginBottom: '4px' }}>CSV File</label>
                <input type="file" accept=".csv" onChange={handleFileUpload} style={{ fontSize: 'var(--font-xs)' }} />
              </div>

              <div>
                <label style={{ display: 'block', fontSize: 'var(--font-xs)', fontWeight: 600, marginBottom: '4px' }}>Or Paste CSV Text</label>
                <textarea
                  className="input"
                  rows={5}
                  placeholder="age,income,churn\n25,50000,0\n45,120000,1"
                  value={uploadCsv}
                  onChange={(e) => setUploadCsv(e.target.value)}
                  style={{ fontFamily: 'var(--font-mono)', fontSize: '11px' }}
                />
              </div>

              <div style={{ display: 'flex', justifyContent: 'flex-end', gap: 'var(--space-sm)', marginTop: 'var(--space-sm)' }}>
                <button type="button" onClick={() => setShowUploadModal(false)} className="btn btn-secondary">
                  Cancel
                </button>
                <button type="submit" disabled={uploadLoading} className="btn btn-primary">
                  {uploadLoading ? 'Profiling...' : 'Upload & Profile'}
                </button>
              </div>
            </form>
          </div>
        </div>
      )}
    </div>
  );
}
