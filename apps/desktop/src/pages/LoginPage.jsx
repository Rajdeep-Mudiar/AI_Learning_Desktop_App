import React, { useState } from 'react';
import { useNavigate, Link } from 'react-router-dom';
import { Sparkles, ArrowRight, Lock, Mail, AlertCircle } from 'lucide-react';
import { useAuth } from '../contexts/AuthContext';
import { authService } from '../services/authService';

export default function LoginPage() {
  const [email, setEmail] = useState('rajdeep@ailearnlab.io');
  const [password, setPassword] = useState('Password123!');
  const [error, setError] = useState('');
  const [loading, setLoading] = useState(false);
  const { login } = useAuth();
  const navigate = useNavigate();

  const handleLogin = async (e) => {
    e.preventDefault();
    setError('');
    setLoading(true);
    try {
      await login(email, password);
      navigate('/dashboard');
    } catch (err) {
      setError(err.message || 'Login failed. Please verify credentials.');
    } finally {
      setLoading(false);
    }
  };

  const handleQuickDemo = async () => {
    setError('');
    setLoading(true);
    try {
      // Try to login with demo account, or auto-register if not present
      try {
        await login('rajdeep@ailearnlab.io', 'Password123!');
      } catch {
        await authService.register('Rajdeep', 'rajdeep@ailearnlab.io', 'Password123!', 'ai_engineer');
        await login('rajdeep@ailearnlab.io', 'Password123!');
      }
      navigate('/dashboard');
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={{
      minHeight: '100vh',
      display: 'flex',
      alignItems: 'center',
      justifyContent: 'center',
      background: 'var(--bg-primary)',
      padding: '24px'
    }}>
      <div className="card" style={{ width: '100%', maxWidth: '420px', padding: 36, borderTop: '4px solid var(--accent-primary)' }}>
        <div style={{ textAlign: 'center', marginBottom: 28 }}>
          <div style={{
            width: 44,
            height: 44,
            borderRadius: 12,
            background: 'linear-gradient(135deg, #6366f1, #38bdf8)',
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center',
            color: '#ffffff',
            margin: '0 auto 12px auto'
          }}>
            <Sparkles size={22} />
          </div>
          <h1 style={{ fontSize: '1.45rem', marginBottom: 6 }}>Sign In to AI Learning Lab</h1>
          <p style={{ fontSize: '0.825rem', color: 'var(--text-secondary)' }}>
            Enter your credentials to resume your AI laboratory sessions.
          </p>
        </div>

        {error && (
          <div style={{
            padding: '10px 14px',
            borderRadius: 'var(--radius-md)',
            background: 'rgba(239, 68, 68, 0.12)',
            border: '1px solid rgba(239, 68, 68, 0.3)',
            color: '#f87171',
            fontSize: '0.825rem',
            display: 'flex',
            alignItems: 'center',
            gap: 8,
            marginBottom: 20
          }}>
            <AlertCircle size={16} />
            <span>{error}</span>
          </div>
        )}

        <form onSubmit={handleLogin} style={{ display: 'flex', flexDirection: 'column', gap: 16 }}>
          <div className="form-group" style={{ margin: 0 }}>
            <label className="form-label">Email Address</label>
            <div style={{ position: 'relative' }}>
              <Mail size={16} style={{ position: 'absolute', left: 12, top: 12, color: 'var(--text-muted)' }} />
              <input
                type="email"
                className="form-input"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                placeholder="name@domain.com"
                required
                style={{ width: '100%', paddingLeft: 36 }}
              />
            </div>
          </div>

          <div className="form-group" style={{ margin: 0 }}>
            <label className="form-label">Password</label>
            <div style={{ position: 'relative' }}>
              <Lock size={16} style={{ position: 'absolute', left: 12, top: 12, color: 'var(--text-muted)' }} />
              <input
                type="password"
                className="form-input"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                placeholder="••••••••"
                required
                style={{ width: '100%', paddingLeft: 36 }}
              />
            </div>
          </div>

          <button
            type="submit"
            className="btn btn-primary btn-lg"
            disabled={loading}
            style={{ width: '100%', marginTop: 8 }}
          >
            {loading ? 'Authenticating...' : 'Sign In'}
          </button>
        </form>

        <div style={{ margin: '20px 0', textAlign: 'center', position: 'relative' }}>
          <hr style={{ borderColor: 'var(--border-subtle)', borderStyle: 'solid', borderWidth: '1px 0 0 0' }} />
          <span style={{ position: 'relative', top: '-10px', background: 'var(--bg-card)', padding: '0 10px', fontSize: '0.75rem', color: 'var(--text-muted)' }}>
            OR
          </span>
        </div>

        <button
          type="button"
          onClick={handleQuickDemo}
          className="btn btn-secondary"
          disabled={loading}
          style={{ width: '100%' }}
        >
          <Sparkles size={16} style={{ color: 'var(--accent-primary)' }} />
          <span>Launch Instant Demo Learner</span>
        </button>

        <p style={{ textAlign: 'center', fontSize: '0.825rem', color: 'var(--text-secondary)', marginTop: 24 }}>
          Don't have an account?{' '}
          <Link to="/register" style={{ color: 'var(--accent-primary)', fontWeight: 600 }}>
            Create Account
          </Link>
        </p>
      </div>
    </div>
  );
}
