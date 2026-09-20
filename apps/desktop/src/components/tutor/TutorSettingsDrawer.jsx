import React from 'react';
import { Settings, RefreshCw, Cpu, Server } from 'lucide-react';

export default function TutorSettingsDrawer({
  isOpen,
  onClose,
  provider,
  onProviderChange,
  modelName,
  onModelNameChange,
  ollamaUrl,
  onOllamaUrlChange,
  modelsList = [],
  isOllamaOnline,
  onRefreshModels,
  refreshing,
}) {
  if (!isOpen) return null;

  return (
    <div
      style={{
        position: 'fixed',
        top: 0,
        right: 0,
        bottom: 0,
        width: '340px',
        background: 'var(--color-surface)',
        borderLeft: '1px solid var(--color-border)',
        boxShadow: 'var(--shadow-xl)',
        zIndex: 999,
        padding: 'var(--space-lg)',
        display: 'flex',
        flexDirection: 'column',
        gap: 'var(--space-lg)',
        overflowY: 'auto',
      }}
    >
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', borderBottom: '1px solid var(--color-border)', paddingBottom: 'var(--space-sm)' }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
          <Settings size={18} color="var(--color-primary-400)" />
          <h3 style={{ margin: 0, fontSize: 'var(--font-md)', color: 'var(--color-text-main)' }}>
            AI Tutor Settings
          </h3>
        </div>
        <button
          onClick={onClose}
          style={{ background: 'none', border: 'none', color: 'var(--color-text-muted)', fontSize: '18px', cursor: 'pointer' }}
        >
          ✕
        </button>
      </div>

      {/* Ollama Status Indicator */}
      <div
        style={{
          padding: 'var(--space-sm) var(--space-md)',
          borderRadius: 'var(--radius-md)',
          background: isOllamaOnline ? 'rgba(16, 185, 129, 0.1)' : 'rgba(245, 158, 11, 0.1)',
          border: isOllamaOnline ? '1px solid #10b981' : '1px solid #f59e0b',
          display: 'flex',
          justifyContent: 'space-between',
          alignItems: 'center',
        }}
      >
        <div style={{ display: 'flex', alignItems: 'center', gap: '8px', fontSize: 'var(--font-xs)' }}>
          <Server size={14} color={isOllamaOnline ? '#10b981' : '#f59e0b'} />
          <span>
            Ollama Status: <strong>{isOllamaOnline ? 'Connected' : 'Offline / Standby'}</strong>
          </span>
        </div>
        <button
          onClick={onRefreshModels}
          disabled={refreshing}
          style={{ background: 'none', border: 'none', color: 'var(--color-text-main)', cursor: 'pointer', display: 'flex', alignItems: 'center' }}
          title="Refresh Ollama Models"
        >
          <RefreshCw size={13} style={{ animation: refreshing ? 'spin 1s linear infinite' : 'none' }} />
        </button>
      </div>

      {/* Inference Provider Selection */}
      <div>
        <label style={{ fontSize: 'var(--font-xs)', fontWeight: 600, color: 'var(--color-text-main)', display: 'block', marginBottom: '6px' }}>
          Inference Engine Provider
        </label>
        <div style={{ display: 'flex', flexDirection: 'column', gap: '6px' }}>
          {[
            { id: 'auto', label: 'Auto (Ollama if running, else Local Engine)' },
            { id: 'ollama', label: 'Local Ollama LLM (Llama 3, Mistral, Gemma)' },
            { id: 'heuristic_local', label: 'Built-in Semantic Reasoning Engine (Offline)' },
          ].map((p) => (
            <label
              key={p.id}
              style={{
                display: 'flex',
                alignItems: 'center',
                gap: '8px',
                padding: '6px 10px',
                borderRadius: 'var(--radius-sm)',
                background: provider === p.id ? 'rgba(99, 102, 241, 0.12)' : 'var(--color-surface-elevated)',
                border: provider === p.id ? '1px solid var(--color-primary-400)' : '1px solid var(--color-border)',
                fontSize: '11px',
                cursor: 'pointer',
              }}
            >
              <input
                type="radio"
                name="provider"
                value={p.id}
                checked={provider === p.id}
                onChange={() => onProviderChange(p.id)}
              />
              <span>{p.label}</span>
            </label>
          ))}
        </div>
      </div>

      {/* Ollama Endpoint */}
      <div>
        <label style={{ fontSize: 'var(--font-xs)', fontWeight: 600, color: 'var(--color-text-main)', display: 'block', marginBottom: '4px' }}>
          Ollama Server URL
        </label>
        <input
          type="text"
          className="input"
          value={ollamaUrl}
          onChange={(e) => onOllamaUrlChange(e.target.value)}
          placeholder="http://localhost:11434"
          style={{ fontSize: 'var(--font-xs)' }}
        />
      </div>

      {/* Model Selection */}
      <div>
        <label style={{ fontSize: 'var(--font-xs)', fontWeight: 600, color: 'var(--color-text-main)', display: 'block', marginBottom: '4px' }}>
          LLM Model Architecture
        </label>
        <select
          className="input"
          value={modelName}
          onChange={(e) => onModelNameChange(e.target.value)}
          style={{ fontSize: 'var(--font-xs)' }}
        >
          {modelsList.map((m) => (
            <option key={m.name} value={m.name}>
              {m.name} {m.size ? `(${m.size})` : ''}
            </option>
          ))}
        </select>
        <p style={{ margin: '4px 0 0', fontSize: '10px', color: 'var(--color-text-muted)' }}>
          To pull models locally: <code>ollama run llama3</code> or <code>ollama run qwen2.5-coder</code>
        </p>
      </div>

      <button
        onClick={onClose}
        className="btn btn-primary"
        style={{ marginTop: 'auto', width: '100%', padding: '10px', fontSize: 'var(--font-xs)', fontWeight: 700 }}
      >
        Save & Close
      </button>
    </div>
  );
}
