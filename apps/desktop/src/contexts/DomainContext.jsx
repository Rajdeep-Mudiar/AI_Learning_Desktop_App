import React, { createContext, useContext, useState, useEffect } from 'react';

export const DOMAINS = {
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
    tagline: 'Full-Stack Modern Web: HTML5, CSS3, React 18, Node.js & Next.js',
    icon: 'Globe',
    color: '#06B6D4',
    gradient: 'linear-gradient(135deg, #06B6D4, #3B82F6)',
    badge: 'High Demand',
    categories: ['Web Foundations', 'Frontend Engineering', 'Backend & APIs', 'Full-Stack Next.js', 'Web Security'],
    skills: ['Semantic HTML', 'Modern CSS & Flexbox', 'JavaScript ES6+', 'React Hooks', 'REST & GraphQL', 'State Management'],
    defaultRoute: '/web-lab'
  },
  'app-dev': {
    id: 'app-dev',
    title: 'App Development',
    shortTitle: 'App Dev',
    tagline: 'Cross-Platform Mobile Engineering: React Native, Flutter, Dart & iOS/Android',
    icon: 'Smartphone',
    color: '#EC4899',
    gradient: 'linear-gradient(135deg, #EC4899, #F43F5E)',
    badge: 'Trending',
    categories: ['Mobile UI Fundamentals', 'React Native & Expo', 'Flutter & Dart', 'Mobile State & APIs', 'Store Deployment'],
    skills: ['Mobile Layouts', 'React Native', 'Flutter Widgets', 'Mobile Navigation', 'Async Storage', 'Device APIs'],
    defaultRoute: '/app-lab'
  },
  'system-design': {
    id: 'system-design',
    title: 'System Design',
    shortTitle: 'System Design',
    tagline: 'Architect Scalable High-Load Distributed Systems & Microservices',
    icon: 'Layers',
    color: '#10B981',
    gradient: 'linear-gradient(135deg, #10B981, #059669)',
    badge: 'Staff Level',
    categories: ['Distributed Systems', 'Caching & Databases', 'Microservices & Queues', 'Scalability Patterns', 'Fault Tolerance'],
    skills: ['Load Balancers', 'Redis Caching', 'Database Sharding', 'Kafka & Message Queues', 'CAP Theorem', 'Rate Limiting'],
    defaultRoute: '/system-design-lab'
  },
  'github': {
    id: 'github',
    title: 'Git & GitHub Workflows',
    shortTitle: 'Git & GitHub',
    tagline: 'Master Version Control, Branching Strategies, Pull Requests & CI/CD Pipelines',
    icon: 'GitBranch',
    color: '#F59E0B',
    gradient: 'linear-gradient(135deg, #F59E0B, #EA580C)',
    badge: 'Core Skill',
    categories: ['Git Fundamentals', 'Branching & Merging', 'Rebase & Cherry-Pick', 'GitHub Team Flow', 'GitHub Actions CI/CD'],
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
