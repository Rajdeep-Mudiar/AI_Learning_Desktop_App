import React from 'react';
import { Settings, RefreshCw, Cpu, Server, Key, Globe, Zap, Sparkles } from 'lucide-react';

export default function TutorSettingsDrawer({
  isOpen,
  onClose,
  provider,
  onProviderChange,
  modelName,
  onModelNameChange,
  ollamaUrl,
  onOllamaUrlChange,
  apiKey,
  onApiKeyChange,
  apiBase,
  onApiBaseChange,
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
        width: '370px',
        background: 'var(--color-surface)',
        borderLeft: '1px solid var(--color-border)',
        boxShadow: 'var(--shadow-xl)',
        zIndex: 999,
        padding: 'var(--space-lg)',
        display: 'flex',
        flexDirection: 'column',
        gap: 'var(--space-md)',
        overflowY: 'auto',
      }}
    >
      {/* Header */}
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', borderBottom: '1px solid var(--color-border)', paddingBottom: 'var(--space-sm)' }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
          <Settings size={18} color="var(--color-primary-400)" />
          <h3 style={{ margin: 0, fontSize: 'var(--font-md)', color: 'var(--color-text-main)' }}>
            AI Tutor Inference Engine
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
          background: isOllamaOnline ? 'rgba(16, 185, 129, 0.12)' : 'rgba(245, 158, 11, 0.12)',
          border: isOllamaOnline ? '1px solid #10b981' : '1px solid #f59e0b',
          display: 'flex',
          justifyContent: 'space-between',
          alignItems: 'center',
        }}
      >
        <div style={{ display: 'flex', alignItems: 'center', gap: '8px', fontSize: 'var(--font-xs)' }}>
          <Server size={14} color={isOllamaOnline ? '#10b981' : '#f59e0b'} />
          <span>
            Local Ollama: <strong>{isOllamaOnline ? 'Online & Ready' : 'Standby / Offline'}</strong>
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
          Active AI Provider
        </label>
        <div style={{ display: 'flex', flexDirection: 'column', gap: '6px' }}>
          {[
            { id: 'auto', label: '⚡ Auto (Ollama if running, else Dynamic Engine)', desc: 'Recommended: Seamless intelligent switching' },
            { id: 'ollama', label: '🖥️ Local Ollama LLM (Llama 3.2, Qwen, Mistral)', desc: '100% Private, on-device offline inference' },
            { id: 'cloud_api', label: '☁️ Cloud API (Groq, OpenAI, OpenRouter, Gemini)', desc: 'Ultra-fast sub-second cloud intelligence' },
            { id: 'heuristic_local', label: '🧠 Dynamic Semantic Engine (Built-in)', desc: 'Lightweight, domain-grounded reasoning' },
          ].map((p) => (
            <label
              key={p.id}
              style={{
                display: 'flex',
                alignItems: 'flex-start',
                gap: '8px',
                padding: '8px 10px',
                borderRadius: 'var(--radius-sm)',
                background: provider === p.id ? 'rgba(99, 102, 241, 0.12)' : 'var(--color-surface-elevated)',
                border: provider === p.id ? '1.5px solid var(--color-primary-400)' : '1px solid var(--color-border)',
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
                style={{ marginTop: '2px' }}
              />
              <div>
                <div style={{ fontWeight: provider === p.id ? 700 : 500, color: 'var(--color-text-main)' }}>{p.label}</div>
                <div style={{ fontSize: '10px', color: 'var(--color-text-muted)' }}>{p.desc}</div>
              </div>
            </label>
          ))}
        </div>
      </div>

      {/* Ollama Model Selection */}
      {(provider === 'auto' || provider === 'ollama') && (
        <div style={{ background: 'var(--color-surface-elevated)', padding: 'var(--space-sm)', borderRadius: 'var(--radius-md)', border: '1px solid var(--color-border)' }}>
          <label style={{ fontSize: 'var(--font-xs)', fontWeight: 600, color: 'var(--color-text-main)', display: 'block', marginBottom: '4px' }}>
            Local Ollama Model
          </label>
          <select
            className="input"
            value={modelName}
            onChange={(e) => onModelNameChange(e.target.value)}
            style={{ fontSize: 'var(--font-xs)', width: '100%', marginBottom: '8px' }}
          >
            {modelsList.length > 0 ? (
              modelsList.map((m) => (
                <option key={m.name} value={m.name}>
                  {m.name} {m.size ? `(${m.size})` : ''}
                </option>
              ))
            ) : (
              <option value="llama3.2:1b">llama3.2:1b (1.3 GB)</option>
            )}
          </select>

          <label style={{ fontSize: '10px', fontWeight: 600, color: 'var(--color-text-muted)', display: 'block', marginBottom: '2px' }}>
            Ollama URL
          </label>
          <input
            type="text"
            className="input"
            value={ollamaUrl}
            onChange={(e) => onOllamaUrlChange(e.target.value)}
            placeholder="http://localhost:11434"
            style={{ fontSize: '11px', width: '100%' }}
          />
        </div>
      )}

      {/* Cloud API Key Configuration */}
      {(provider === 'cloud_api' || provider === 'auto') && (
        <div style={{ background: 'var(--color-surface-elevated)', padding: 'var(--space-sm)', borderRadius: 'var(--radius-md)', border: '1px solid var(--color-border)' }}>
          <div style={{ display: 'flex', alignItems: 'center', gap: '6px', marginBottom: '4px' }}>
            <Key size={13} color="var(--color-primary-400)" />
            <label style={{ fontSize: 'var(--font-xs)', fontWeight: 600, color: 'var(--color-text-main)' }}>
              Cloud API Key (Optional)
            </label>
          </div>
          <p style={{ margin: '0 0 6px', fontSize: '10px', color: 'var(--color-text-muted)' }}>
            Compatible with Groq, OpenAI, OpenRouter, or Gemini.
          </p>
          <input
            type="password"
            className="input"
            value={apiKey || ''}
            onChange={(e) => onApiKeyChange(e.target.value)}
            placeholder="gsk_... or sk-..."
            style={{ fontSize: '11px', width: '100%', marginBottom: '6px' }}
          />
          <input
            type="text"
            className="input"
            value={apiBase || ''}
            onChange={(e) => onApiBaseChange(e.target.value)}
            placeholder="https://api.groq.com/openai/v1 or https://openrouter.ai/api/v1"
            style={{ fontSize: '10px', width: '100%' }}
          />
        </div>
      )}

      <button
        onClick={onClose}
        className="btn btn-primary"
        style={{ marginTop: 'auto', width: '100%', padding: '10px', fontSize: 'var(--font-xs)', fontWeight: 700 }}
      >
        Save & Apply Configuration
      </button>
    </div>
  );
}
