import React from 'react';
import { useNavigate } from 'react-router-dom';
import { Search, Flame, Sun, Moon, LogOut, User as UserIcon } from 'lucide-react';
import { useAuth } from '../../contexts/AuthContext';
import { useTheme } from '../../contexts/ThemeContext';

export default function TopNav() {
  const { user, logout } = useAuth();
  const { theme, toggleTheme } = useTheme();
  const navigate = useNavigate();

  const streakCount = user?.streak?.current || 1;

  return (
    <header className="top-nav">
      <div className="search-trigger-box" onClick={() => navigate('/learn')} style={{ cursor: 'pointer' }}>
        <Search size={16} />
        <span>Search courses, concepts, lessons...</span>
        <span className="kbd-shortcut">Ctrl+K</span>
      </div>

      <div className="top-nav-actions">
        {/* Streak Pill */}
        <div className="streak-pill" title="Current Daily Learning Streak">
          <Flame size={16} style={{ fill: '#fbbf24', color: '#fbbf24' }} />
          <span>{streakCount} Day Streak</span>
        </div>

        {/* Theme Toggle */}
        <button
          onClick={toggleTheme}
          className="btn btn-ghost"
          style={{ width: 36, height: 36, padding: 0, borderRadius: '50%' }}
          title={`Switch to ${theme === 'dark' ? 'Light' : 'Dark'} Mode`}
        >
          {theme === 'dark' ? <Sun size={18} /> : <Moon size={18} />}
        </button>

        {/* User profile dropdown / status */}
        {user ? (
          <div style={{ display: 'flex', alignItems: 'center', gap: 10 }}>
            <div
              className="user-profile-badge"
              onClick={() => navigate('/settings')}
              title="Open Settings"
            >
              <img
                src={user.avatar_url || `https://api.dicebear.com/7.x/bottts/svg?seed=${user.name}`}
                alt={user.name}
                className="user-avatar"
              />
              <div>
                <div style={{ fontSize: '0.85rem', fontWeight: 600 }}>{user.name}</div>
                <div style={{ fontSize: '0.7rem', color: 'var(--text-muted)' }}>Student • Level 1</div>
              </div>
            </div>

            <button
              onClick={logout}
              className="btn btn-ghost"
              style={{ padding: '6px 8px', color: 'var(--text-muted)' }}
              title="Sign Out"
            >
              <LogOut size={16} />
            </button>
          </div>
        ) : (
          <button onClick={() => navigate('/login')} className="btn btn-primary btn-sm">
            Sign In
          </button>
        )}
      </div>
    </header>
  );
}
