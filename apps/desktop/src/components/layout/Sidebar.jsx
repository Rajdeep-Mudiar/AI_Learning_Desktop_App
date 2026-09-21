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
  Binary,
  ShieldCheck,
  Lock,
} from 'lucide-react';
import { useDomain } from '../../contexts/DomainContext';

export default function Sidebar() {
  const { currentDomain, domainInfo, openPicker } = useDomain();

  // Dynamic specialized labs based on active domain
  const getDomainLabs = () => {
    switch (currentDomain) {
      case 'dsa':
        return [
          { path: '/dsa-lab', label: 'DSA Visualizer & Sandbox', icon: Binary },
          { path: '/playground', label: 'Code Playground', icon: Terminal },
          { path: '/challenges', label: 'DSA Challenges', icon: Award }
        ];
      case 'cybersecurity':
        return [
          { path: '/cyber-lab', label: 'Crypto & Threat Defense Lab', icon: ShieldCheck },
          { path: '/playground', label: 'Code Playground', icon: Terminal },
          { path: '/challenges', label: 'Security Challenges', icon: Award }
        ];
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
          { path: '/system-design-lab', label: 'Traffic & Topology Sim', icon: Layers },
          { path: '/challenges', label: 'Scalability Challenges', icon: Award }
        ];
      case 'github':
        return [
          { path: '/git-lab', label: 'Git DAG Graph & Shell', icon: GitBranch },
          { path: '/challenges', label: 'Git Workflow Challenges', icon: Award }
        ];
      case 'all':
        return [
          { path: '/algorithms', label: 'Algorithm Lab (AI)', icon: Cpu },
          { path: '/deep-learning', label: 'Deep Learning Lab', icon: Network },
          { path: '/dsa-lab', label: 'DSA Visualizer Lab', icon: Binary },
          { path: '/cyber-lab', label: 'Cyber Defense Lab', icon: ShieldCheck },
          { path: '/web-lab', label: 'Web Dev Sandbox', icon: Globe },
          { path: '/app-lab', label: 'Mobile App Lab', icon: Smartphone },
          { path: '/system-design-lab', label: 'System Design Lab', icon: Layers },
          { path: '/git-lab', label: 'Git DAG Visualizer', icon: GitBranch },
          { path: '/playground', label: 'Code Playground', icon: Terminal },
          { path: '/challenges', label: 'Coding Challenges', icon: Award }
        ];
      case 'ai-ml':
      default:
        return [
          { path: '/algorithms', label: 'Algorithm Lab', icon: Cpu },
          { path: '/deep-learning', label: 'Deep Learning Lab', icon: Network },
          { path: '/break-the-model', label: 'Break the Model', icon: AlertTriangle },
          { path: '/playground', label: 'Python Playground', icon: Terminal },
          { path: '/challenges', label: 'AI Challenges', icon: Award }
        ];
    }
  };

  const getTrackBrandTitle = () => {
    switch (currentDomain) {
      case 'dsa': return 'DSA & Algorithms';
      case 'cybersecurity': return 'Cyber Security Lab';
      case 'web-dev': return 'Web Dev Lab';
      case 'app-dev': return 'App Dev Lab';
      case 'system-design': return 'System Design';
      case 'github': return 'Git & GitHub';
      case 'all': return 'Engineering Suite';
      default: return 'AI Learning Lab';
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
          <h1 className="sidebar-logo-text">{getTrackBrandTitle()}</h1>
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
          {currentDomain === 'all' ? 'All Laboratories' : `${domainInfo.shortTitle} Laboratories`}
        </div>
        {domainLabs.map((item) => {
          const Icon = item.icon;
          return (
            <NavLink
              key={item.path + item.label}
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
            <span>
              {currentDomain === 'dsa'
                ? 'DSA AI Tutor'
                : currentDomain === 'cybersecurity'
                ? 'Cyber AI Tutor'
                : currentDomain === 'web-dev'
                ? 'Web AI Tutor'
                : currentDomain === 'app-dev'
                ? 'Mobile AI Tutor'
                : currentDomain === 'system-design'
                ? 'Systems AI Tutor'
                : currentDomain === 'github'
                ? 'Git AI Tutor'
                : 'AI Tutor'}
            </span>
          </div>
        </NavLink>

        <NavLink to="/projects" className={({ isActive }) => `nav-item ${isActive ? 'nav-item-active' : ''}`}>
          <div className="nav-item-left">
            <FolderGit2 size={18} />
            <span>Projects & Viva</span>
          </div>
        </NavLink>

        {/* Growth & Career */}
        <div className="nav-section-title" style={{ marginTop: 12 }}>Growth & Career</div>
        <NavLink to="/career" className={({ isActive }) => `nav-item ${isActive ? 'nav-item-active' : ''}`}>
          <div className="nav-item-left">
            <Briefcase size={18} />
            <span>Career Roadmaps</span>
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
