import React from 'react';
import { NavLink } from 'react-router-dom';
import {
  LayoutDashboard,
  BookOpen,
  GitFork,
  Cpu,
  AlertTriangle,
  Terminal,
  Award,
  Bot,
  Database,
  FlaskConical,
  Network,
  FolderGit2,
  FileText,
  Video,
  Flame,
  Users,
  Briefcase,
  Trophy,
  Settings,
  Sparkles,
} from 'lucide-react';

const MAIN_NAV = [
  { path: '/dashboard', label: 'Dashboard', icon: LayoutDashboard },
  { path: '/learn', label: 'Learn & Courses', icon: BookOpen },
  { path: '/skills', label: 'Skill Tree', icon: GitFork },
  { path: '/algorithms', label: 'Algorithm Lab', icon: Cpu },
  { path: '/deep-learning', label: 'Deep Learning Lab', icon: Network },
  { path: '/break-the-model', label: 'Break the Model', icon: AlertTriangle },
  { path: '/playground', label: 'Python Playground', icon: Terminal },
  { path: '/challenges', label: 'Coding Challenges', icon: Award },
];

const LABS_NAV = [
  { path: '/tutor', label: 'AI Tutor', icon: Bot },
  { path: '/datasets', label: 'Datasets', icon: Database },
  { path: '/experiments', label: 'ML Experiments', icon: FlaskConical },
  { path: '/projects', label: 'AI Projects', icon: FolderGit2 },
  { path: '/research', label: 'Research Mode', icon: FileText },
  { path: '/interviews', label: 'AI Interview Prep', icon: Video },
  { path: '/hackathons', label: 'Hackathons', icon: Flame },
];

const COMMUNITY_NAV = [
  { path: '/community', label: 'Community', icon: Users },
  { path: '/career', label: 'Career Paths', icon: Briefcase },
  { path: '/achievements', label: 'Achievements', icon: Trophy },
  { path: '/settings', label: 'Settings', icon: Settings },
];

export default function Sidebar() {
  return (
    <aside className="sidebar">
      <div className="sidebar-header">
        <div style={{
          width: 34,
          height: 34,
          borderRadius: 10,
          background: 'linear-gradient(135deg, #6366f1, #38bdf8)',
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
          color: '#ffffff',
          boxShadow: '0 2px 10px rgba(99, 102, 241, 0.4)'
        }}>
          <Sparkles size={18} />
        </div>
        <div>
          <h1 className="sidebar-logo-text">AI Learning Lab</h1>
          <p style={{ fontSize: '0.65rem', color: 'var(--text-muted)', fontWeight: 600, letterSpacing: '0.04em' }}>DESKTOP v1.0</p>
        </div>
      </div>

      <nav className="sidebar-nav">
        <div className="nav-section-title">Core Learning</div>
        {MAIN_NAV.map((item) => {
          const Icon = item.icon;
          return (
            <NavLink
              key={item.path}
              to={item.path}
              className={({ isActive }) => `nav-item ${isActive ? 'nav-item-active' : ''}`}
            >
              <div className="nav-item-left">
                <Icon size={18} />
                <span>{item.label}</span>
              </div>
            </NavLink>
          );
        })}

        <div className="nav-section-title" style={{ marginTop: 8 }}>AI Laboratories</div>
        {LABS_NAV.map((item) => {
          const Icon = item.icon;
          return (
            <NavLink
              key={item.path}
              to={item.path}
              className={({ isActive }) => `nav-item ${isActive ? 'nav-item-active' : ''}`}
            >
              <div className="nav-item-left">
                <Icon size={17} style={{ opacity: 0.85 }} />
                <span>{item.label}</span>
              </div>
              {item.phase && <span className="phase-pill">{item.phase}</span>}
            </NavLink>
          );
        })}

        <div className="nav-section-title" style={{ marginTop: 8 }}>Career & System</div>
        {COMMUNITY_NAV.map((item) => {
          const Icon = item.icon;
          return (
            <NavLink
              key={item.path}
              to={item.path}
              className={({ isActive }) => `nav-item ${isActive ? 'nav-item-active' : ''}`}
            >
              <div className="nav-item-left">
                <Icon size={17} style={{ opacity: 0.85 }} />
                <span>{item.label}</span>
              </div>
              {item.phase && <span className="phase-pill">{item.phase}</span>}
            </NavLink>
          );
        })}
      </nav>
    </aside>
  );
}
