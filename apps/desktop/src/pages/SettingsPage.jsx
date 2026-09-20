import React, { useState, useEffect } from 'react';
import { Settings, Moon, Sun, Server, Download, Shield, User as UserIcon, CheckCircle2, AlertCircle } from 'lucide-react';
import { useAuth } from '../contexts/AuthContext';
import { useTheme } from '../contexts/ThemeContext';
import { dashboardService } from '../services/dashboardService';

export default function SettingsPage() {
  const { user, updateUser } = useAuth();
  const { theme, setTheme } = useTheme();
  const [name, setName] = useState(user?.name || '');
  const [systemStatus, setSystemStatus] = useState(null);
  const [checkingSystem, setCheckingSystem] = useState(false);
  const [saveSuccess, setSaveSuccess] = useState(false);

  useEffect(() => {
    async function checkStatus() {
      try {
        setCheckingSystem(true);
        const data = await dashboardService.getSystemStatus();
        setSystemStatus(data);
      } catch (err) {
        console.error('Failed to get system status:', err);
      } finally {
        setCheckingSystem(false);
      }
    }
    checkStatus();
  }, []);

  const handleExportData = () => {
    const exportPayload = {
      user,
      systemStatus,
      exportedAt: new Date().toISOString(),
      platform: 'AI Learning Lab Desktop v1.0',
    };
    const blob = new Blob([JSON.stringify(exportPayload, null, 2)], { type: 'application/json' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = `ai_learning_lab_profile_${Date.now()}.json`;
    a.click();
    URL.revokeObjectURL(url);
  };

  return (
    <div className="animate-fade-in" style={{ maxWidth: '800px' }}>
      <div style={{ marginBottom: 28 }}>
        <h1 style={{ fontSize: '1.75rem', marginBottom: 6 }}>Settings & Environment</h1>
        <p style={{ color: 'var(--text-secondary)', fontSize: '0.925rem' }}>
          Configure your workspace, local AI model connections, and learning preferences.
        </p>
      </div>

      <div style={{ display: 'flex', flexDirection: 'column', gap: 24 }}>
        {/* Profile Settings */}
        <div className="card">
          <div style={{ display: 'flex', alignItems: 'center', gap: 8, marginBottom: 16 }}>
            <UserIcon size={18} style={{ color: 'var(--accent-primary)' }} />
            <h3 style={{ fontSize: '1.05rem' }}>Learner Profile</h3>
          </div>

          <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: 16, marginBottom: 16 }}>
            <div className="form-group">
              <label className="form-label">Full Name</label>
              <input
                type="text"
                className="form-input"
                value={name}
                onChange={(e) => setName(e.target.value)}
              />
            </div>
            <div className="form-group">
              <label className="form-label">Email Address</label>
              <input
                type="email"
                className="form-input"
                value={user?.email || ''}
                disabled
                style={{ opacity: 0.7 }}
              />
            </div>
          </div>
        </div>

        {/* Theme Settings */}
        <div className="card">
          <div style={{ display: 'flex', alignItems: 'center', gap: 8, marginBottom: 16 }}>
            <Sun size={18} style={{ color: '#f59e0b' }} />
            <h3 style={{ fontSize: '1.05rem' }}>Visual Theme</h3>
          </div>

          <div style={{ display: 'flex', gap: 12 }}>
            <button
              onClick={() => setTheme('dark')}
              className={theme === 'dark' ? 'btn btn-primary' : 'btn btn-secondary'}
              style={{ flex: 1, padding: '14px', borderRadius: 'var(--radius-md)' }}
            >
              <Moon size={18} />
              <span>Developer Dark Mode</span>
            </button>

            <button
              onClick={() => setTheme('light')}
              className={theme === 'light' ? 'btn btn-primary' : 'btn btn-secondary'}
              style={{ flex: 1, padding: '14px', borderRadius: 'var(--radius-md)' }}
            >
              <Sun size={18} />
              <span>Studio Light Mode</span>
            </button>
          </div>
        </div>

        {/* Local AI & System Status */}
        <div className="card">
          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: 16 }}>
            <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
              <Server size={18} style={{ color: 'var(--accent-secondary)' }} />
              <h3 style={{ fontSize: '1.05rem' }}>Local AI & Hardware Environment</h3>
            </div>
            <span className="badge badge-gray">{systemStatus?.api_version || 'v1.0.0'}</span>
          </div>

          <div style={{ display: 'flex', flexDirection: 'column', gap: 12 }}>
            {/* Database status */}
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', padding: '12px 16px', background: 'var(--bg-tertiary)', borderRadius: 'var(--radius-md)' }}>
              <div>
                <div style={{ fontSize: '0.85rem', fontWeight: 600 }}>MongoDB Database Engine</div>
                <div style={{ fontSize: '0.75rem', color: 'var(--text-muted)' }}>Collection Store: {systemStatus?.database?.database_name || 'ai_learning_lab'}</div>
              </div>
              <span className={`badge ${systemStatus?.database?.connected ? 'badge-green' : 'badge-amber'}`}>
                {systemStatus?.database?.connected ? 'Connected' : 'Connecting'}
              </span>
            </div>

            {/* Ollama status */}
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', padding: '12px 16px', background: 'var(--bg-tertiary)', borderRadius: 'var(--radius-md)' }}>
              <div>
                <div style={{ fontSize: '0.85rem', fontWeight: 600 }}>Local Ollama LLM Service</div>
                <div style={{ fontSize: '0.75rem', color: 'var(--text-muted)' }}>{systemStatus?.local_ai?.note}</div>
              </div>
              <span className={`badge ${systemStatus?.local_ai?.ollama_connected ? 'badge-green' : 'badge-gray'}`}>
                {systemStatus?.local_ai?.ollama_connected ? 'Active (Local AI)' : 'Ready for Phase 6'}
              </span>
            </div>
          </div>
        </div>

        {/* Data Export & Privacy */}
        <div className="card">
          <div style={{ display: 'flex', alignItems: 'center', gap: 8, marginBottom: 16 }}>
            <Shield size={18} style={{ color: '#10b981' }} />
            <h3 style={{ fontSize: '1.05rem' }}>Data Export & Local Privacy</h3>
          </div>

          <p style={{ fontSize: '0.85rem', color: 'var(--text-secondary)', marginBottom: 16 }}>
            All your code submissions, quiz evaluations, learning telemetry, and experiments are stored locally on your desktop.
          </p>

          <button onClick={handleExportData} className="btn btn-secondary">
            <Download size={16} /> Export Learning Data (JSON)
          </button>
        </div>
      </div>
    </div>
  );
}
