import React, { createContext, useContext, useState, useEffect } from 'react';

export const DOMAINS = {
  'all': {
    id: 'all',
    title: 'All Engineering Disciplines',
    shortTitle: 'All Tracks',
    tagline: 'Complete Engineering Suite: AI & ML, Web Dev, Mobile Apps, System Design, Git, DSA & Cyber Security',
    icon: 'Sparkles',
    color: '#6366F1',
    gradient: 'linear-gradient(135deg, #6366F1, #EC4899)',
    badge: 'Complete Suite',
    categories: ['All Categories'],
    skills: ['AI & ML', 'Web Engineering', 'Mobile Apps', 'Distributed Systems', 'Git & CI/CD', 'DSA & Algorithms', 'Cyber Security'],
    defaultRoute: '/dashboard'
  },
  'ai-ml': {
    id: 'ai-ml',
    title: 'AI & Machine Learning',
    shortTitle: 'AI & ML',
    tagline: 'Master Machine Learning, Deep Neural Networks, Transformers & AI Agents',
    icon: 'Bot',
    color: '#8B5CF6',
    gradient: 'linear-gradient(135deg, #8B5CF6, #3B82F6)',
    badge: 'Popular',
    categories: ['Programming Foundations', 'Mathematics', 'Machine Learning', 'Deep Learning', 'Generative AI', 'Practical AI'],
    skills: ['Python & NumPy', 'Linear Algebra', 'Calculus', 'Scikit-Learn', 'PyTorch', 'Transformers', 'Prompt Engineering'],
    defaultRoute: '/dashboard'
  },
  'web-dev': {
    id: 'web-dev',
    title: 'Web Development',
    shortTitle: 'Web Dev',
    tagline: 'Full-Stack Modern Web: HTML5, CSS3, React 18, Node.js & REST APIs',
    icon: 'Globe',
    color: '#06B6D4',
    gradient: 'linear-gradient(135deg, #06B6D4, #3B82F6)',
    badge: 'High Demand',
    categories: ['Web Development', 'Frontend Engineering', 'Backend & APIs'],
    skills: ['Semantic HTML', 'Modern CSS & Flexbox', 'JavaScript ES6+', 'React Hooks', 'REST & APIs', 'State Management'],
    defaultRoute: '/web-lab'
  },
  'app-dev': {
    id: 'app-dev',
    title: 'App Development',
    shortTitle: 'App Dev',
    tagline: 'Cross-Platform Mobile Engineering: React Native, Flutter, Mobile Viewports & Offline APIs',
    icon: 'Smartphone',
    color: '#EC4899',
    gradient: 'linear-gradient(135deg, #EC4899, #F43F5E)',
    badge: 'Trending',
    categories: ['App Development', 'Mobile UI', 'React Native & Flutter'],
    skills: ['Mobile Layouts', 'React Native', 'Flutter Widgets', 'Mobile Navigation', 'Async Storage', 'Device APIs'],
    defaultRoute: '/app-lab'
  },
  'system-design': {
    id: 'system-design',
    title: 'System Design',
    shortTitle: 'System Design',
    tagline: 'Architect Scalable High-Load Distributed Systems, Microservices & Redis Caching',
    icon: 'Layers',
    color: '#10B981',
    gradient: 'linear-gradient(135deg, #10B981, #059669)',
    badge: 'Staff Level',
    categories: ['System Design', 'Distributed Systems', 'Caching & Sharding'],
    skills: ['Load Balancers', 'Redis Caching', 'Database Sharding', 'Microservices', 'CAP Theorem', 'Rate Limiting'],
    defaultRoute: '/system-design-lab'
  },
  'dsa': {
    id: 'dsa',
    title: 'Data Structures & Algorithms',
    shortTitle: 'DSA',
    tagline: 'Master Array Pointers, Binary Trees, Stacks & Queues, Graphs & Dynamic Programming',
    icon: 'Binary',
    color: '#F43F5E',
    gradient: 'linear-gradient(135deg, #F43F5E, #E11D48)',
    badge: 'Interview Essential',
    categories: ['Arrays & Strings', 'Linked Lists & Stacks', 'Trees & Graphs', 'Dynamic Programming'],
    skills: ['Two Pointers & Sliding Window', 'Monotonic Stacks', 'Binary Search Trees', 'Graph BFS/DFS & Dijkstra', 'Dynamic Programming', 'Big-O Analysis'],
    defaultRoute: '/dsa-lab'
  },
  'cybersecurity': {
    id: 'cybersecurity',
    title: 'Cyber Security & Defense',
    shortTitle: 'Cyber Security',
    tagline: 'Master Network Defense, Cryptography, OWASP Web Security, Threat Hunting & Zero Trust',
    icon: 'ShieldCheck',
    color: '#14B8A6',
    gradient: 'linear-gradient(135deg, #14B8A6, #0D9488)',
    badge: 'Mission Critical',
    categories: ['Network Security', 'Applied Cryptography', 'Web App Security & OWASP', 'Threat Hunting & Zero Trust'],
    skills: ['Network Packet Analysis', 'AES & RSA Cryptography', 'SQLi & XSS Prevention', 'JWT & Auth Defense', 'Zero Trust Architecture', 'Incident Response'],
    defaultRoute: '/cyber-lab'
  },
  'github': {
    id: 'github',
    title: 'Git & GitHub Workflows',
    shortTitle: 'Git & GitHub',
    tagline: 'Master Version Control, Directed Acyclic Graph Commits, Branching, Rebasing & CI/CD Pipelines',
    icon: 'GitBranch',
    color: '#F59E0B',
    gradient: 'linear-gradient(135deg, #F59E0B, #EA580C)',
    badge: 'Core Skill',
    categories: ['Git & GitHub', 'Branching & Merging', 'CI/CD Automation'],
    skills: ['Git Internals', 'Branching & Merging', 'Merge Conflicts', 'Interactive Rebase', 'Pull Requests', 'CI/CD Automation'],
    defaultRoute: '/git-lab'
  }
};

const DomainContext = createContext(null);

export function DomainProvider({ children }) {
  const [currentDomain, setCurrentDomain] = useState(() => {
    return localStorage.getItem('ailearn_active_domain') || null;
  });
  const [isPickerOpen, setIsPickerOpen] = useState(false);

  useEffect(() => {
    if (!currentDomain) {
      // First time opening: automatically trigger domain picker
      setIsPickerOpen(true);
    }
  }, [currentDomain]);

  const selectDomain = (domainId) => {
    if (DOMAINS[domainId]) {
      setCurrentDomain(domainId);
      localStorage.setItem('ailearn_active_domain', domainId);
      setIsPickerOpen(false);
    }
  };

  const openPicker = () => setIsPickerOpen(true);
  const closePicker = () => {
    if (currentDomain) {
      setIsPickerOpen(false);
    }
  };

  const domainInfo = DOMAINS[currentDomain] || DOMAINS['ai-ml'];

  return (
    <DomainContext.Provider
      value={{
        currentDomain: currentDomain || 'ai-ml',
        domainInfo,
        allDomains: DOMAINS,
        selectDomain,
        isPickerOpen,
        openPicker,
        closePicker
      }}
    >
      {children}
    </DomainContext.Provider>
  );
}

export function useDomain() {
  const context = useContext(DomainContext);
  if (!context) {
    throw new Error('useDomain must be used within a DomainProvider');
  }
  return context;
}
