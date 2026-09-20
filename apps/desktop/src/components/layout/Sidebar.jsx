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
  Globe,
  Smartphone,
  Layers,
  GitBranch,
} from 'lucide-react';
import { useDomain } from '../../contexts/DomainContext';

export default function Sidebar() {
  const { currentDomain, domainInfo, openPicker } = useDomain();

  // Dynamic specialized labs based on active domain
  const getDomainLabs = () => {
    switch (currentDomain) {
      case 'web-dev':
        return [
          { path: '/web-lab', label: 'Web Sandbox & Live Preview', icon: Globe },
          { path: '/playground', label: 'Code Playground', icon: Terminal },
          { path: '/challenges', label: 'Web Challenges', icon: Award }
        ];
      case 'app-dev':
        return [
          { path: '/app-lab', label: 'Mobile Viewport Emulator', icon: Smartphone },
          { path: '/playground', label: 'Code Playground', icon: Terminal },
          { path: '/challenges', label: 'App Challenges', icon: Award }
        ];
      case 'system-design':
        return [
          { path: '/system-design-lab', label: 'Architecture & Traffic Simulator', icon: Layers },
          { path: '/interviews', label: 'System Design Mock Interviews', icon: Video },
          { path: '/challenges', label: 'Scalability Challenges', icon: Award }
        ];
      case 'github':
        return [
          { path: '/git-lab', label: 'Git DAG Visualizer & Shell', icon: GitBranch },
          { path: '/challenges', label: 'Git Workflow Challenges', icon: Award },
          { path: '/projects', label: 'Open Source Repos', icon: FolderGit2 }
        ];
      default: // ai-ml
        return [
          { path: '/algorithms', label: 'Algorithm Lab', icon: Cpu },
          { path: '/deep-learning', label: 'Deep Learning Lab', icon: Network },
          { path: '/break-the-model', label: 'Break the Model', icon: AlertTriangle },
          { path: '/playground', label: 'Python Playground', icon: Terminal },
          { path: '/challenges', label: 'AI Challenges', icon: Award }
        ];
    }
  };

  const domainLabs = getDomainLabs();

  return (
    <aside className="sidebar">
      {/* Brand Header */}
      <div className="sidebar-header" onClick={openPicker} style={{ cursor: 'pointer' }} title="Click to Switch Track">
        <div style={{
          width: 34,
          height: 34,
          borderRadius: 10,
          background: domainInfo.gradient,
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
          color: '#ffffff',
          boxShadow: `0 2px 10px ${domainInfo.color}50`
        }}>
          <Sparkles size={18} />
        </div>
        <div>
          <h1 className="sidebar-logo-text">AI Learning Lab</h1>
          <p style={{ fontSize: '0.68rem', color: domainInfo.color, fontWeight: 700, letterSpacing: '0.04em' }}>
            {domainInfo.shortTitle.toUpperCase()} TRACK
          </p>
        </div>
      </div>

      <nav className="sidebar-nav">
        {/* Core Navigation */}
        <div className="nav-section-title">Core Learning</div>
        <NavLink to="/dashboard" className={({ isActive }) => `nav-item ${isActive ? 'nav-item-active' : ''}`}>
          <div className="nav-item-left">
            <LayoutDashboard size={18} />
            <span>Dashboard</span>
          </div>
        </NavLink>

        <NavLink to="/learn" className={({ isActive }) => `nav-item ${isActive ? 'nav-item-active' : ''}`}>
          <div className="nav-item-left">
            <BookOpen size={18} />
            <span>Courses & Lessons</span>
          </div>
        </NavLink>

        <NavLink to="/skills" className={({ isActive }) => `nav-item ${isActive ? 'nav-item-active' : ''}`}>
          <div className="nav-item-left">
            <GitFork size={18} />
            <span>Skill Tree</span>
          </div>
        </NavLink>

        {/* Specialized Domain Laboratories */}
        <div className="nav-section-title" style={{ marginTop: 12 }}>
          {domainInfo.shortTitle} Laboratories
        </div>
        {domainLabs.map((item) => {
          const Icon = item.icon;
          return (
            <NavLink
              key={item.path}
              to={item.path}
              className={({ isActive }) => `nav-item ${isActive ? 'nav-item-active' : ''}`}
            >
              <div className="nav-item-left">
                <Icon size={18} color={domainInfo.color} />
                <span>{item.label}</span>
              </div>
            </NavLink>
          );
        })}

        {/* Advanced Tools */}
        <div className="nav-section-title" style={{ marginTop: 12 }}>Shared Tools</div>
        <NavLink to="/tutor" className={({ isActive }) => `nav-item ${isActive ? 'nav-item-active' : ''}`}>
          <div className="nav-item-left">
            <Bot size={18} />
            <span>AI Tutor</span>
          </div>
        </NavLink>

        <NavLink to="/projects" className={({ isActive }) => `nav-item ${isActive ? 'nav-item-active' : ''}`}>
          <div className="nav-item-left">
            <FolderGit2 size={18} />
            <span>Projects & Viva</span>
          </div>
        </NavLink>

        <NavLink to="/interviews" className={({ isActive }) => `nav-item ${isActive ? 'nav-item-active' : ''}`}>
          <div className="nav-item-left">
            <Video size={18} />
            <span>Mock Interviews</span>
          </div>
        </NavLink>

        {/* Community & Career */}
        <div className="nav-section-title" style={{ marginTop: 12 }}>Growth & Career</div>
        <NavLink to="/career" className={({ isActive }) => `nav-item ${isActive ? 'nav-item-active' : ''}`}>
          <div className="nav-item-left">
            <Briefcase size={18} />
            <span>Career Roadmaps</span>
          </div>
        </NavLink>

        <NavLink to="/community" className={({ isActive }) => `nav-item ${isActive ? 'nav-item-active' : ''}`}>
          <div className="nav-item-left">
            <Users size={18} />
            <span>Community Forum</span>
          </div>
        </NavLink>

        <NavLink to="/achievements" className={({ isActive }) => `nav-item ${isActive ? 'nav-item-active' : ''}`}>
          <div className="nav-item-left">
            <Trophy size={18} />
            <span>Achievements</span>
          </div>
        </NavLink>

        <NavLink to="/settings" className={({ isActive }) => `nav-item ${isActive ? 'nav-item-active' : ''}`}>
          <div className="nav-item-left">
            <Settings size={18} />
            <span>Settings</span>
          </div>
        </NavLink>
      </nav>
    </aside>
  );
}
