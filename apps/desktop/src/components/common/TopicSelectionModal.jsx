import React from 'react';
import { useNavigate } from 'react-router-dom';
import {
  Bot,
  Globe,
  Smartphone,
  Layers,
  GitBranch,
  Sparkles,
  ArrowRight,
  CheckCircle2,
  X,
  Code2,
  Cpu,
  Terminal,
  Zap
} from 'lucide-react';
import { useDomain } from '../../contexts/DomainContext';

const DOMAIN_ICONS = {
  'ai-ml': Bot,
  'web-dev': Globe,
  'app-dev': Smartphone,
  'system-design': Layers,
  'github': GitBranch
};

export default function TopicSelectionModal() {
  const { currentDomain, allDomains, selectDomain, isPickerOpen, closePicker } = useDomain();
  const navigate = useNavigate();

  if (!isPickerOpen) return null;

  const handleSelect = (domainId) => {
    selectDomain(domainId);
    const domain = allDomains[domainId];
    if (domain?.defaultRoute) {
      navigate(domain.defaultRoute);
    }
  };

  return (
    <div
      style={{
        position: 'fixed',
        inset: 0,
        zIndex: 9999,
        background: 'rgba(5, 7, 15, 0.85)',
        backdropFilter: 'blur(16px)',
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'center',
        padding: '24px',
        animation: 'fadeIn 0.25s ease-out'
      }}
    >
      <div
        className="card"
        style={{
          width: '100%',
          maxWidth: '1080px',
          maxHeight: '90vh',
          overflowY: 'auto',
          padding: '36px 40px',
          background: 'var(--bg-secondary)',
          border: '1px solid var(--border-color)',
          borderRadius: '24px',
          boxShadow: '0 25px 60px -15px rgba(0, 0, 0, 0.7)',
          position: 'relative'
        }}
      >
        {/* Close button if user already had a domain selected */}
        {currentDomain && (
          <button
            onClick={closePicker}
            className="btn btn-ghost"
            style={{
              position: 'absolute',
              top: 24,
              right: 24,
              width: 38,
              height: 38,
              borderRadius: '50%',
              padding: 0,
              color: 'var(--text-muted)'
            }}
            title="Close"
          >
            <X size={20} />
          </button>
        )}

        {/* Header */}
        <div style={{ textAlign: 'center', marginBottom: 36 }}>
          <div
            style={{
              display: 'inline-flex',
              alignItems: 'center',
              gap: 8,
              padding: '6px 14px',
              borderRadius: '20px',
              background: 'rgba(99, 102, 241, 0.12)',
              border: '1px solid rgba(99, 102, 241, 0.3)',
              color: '#818cf8',
              fontSize: '0.85rem',
              fontWeight: 600,
              marginBottom: 14
            }}
          >
            <Sparkles size={16} /> Choose Your Learning Track
          </div>
          <h1 style={{ fontSize: '2.2rem', fontWeight: 800, letterSpacing: '-0.02em', marginBottom: 10 }}>
            What do you want to master today?
          </h1>
          <p style={{ color: 'var(--text-secondary)', fontSize: '1rem', maxWidth: '640px', margin: '0 auto' }}>
            Select your primary engineering discipline. The platform will dynamically configure courses, interactive visual labs, code sandboxes, and interview simulators tailored to your track.
          </p>
        </div>

        {/* 5 Domain Grid Cards */}
        <div
          style={{
            display: 'grid',
            gridTemplateColumns: 'repeat(auto-fit, minmax(300px, 1fr))',
            gap: '20px',
            marginBottom: '32px'
          }}
        >
          {Object.values(allDomains).map((domain) => {
            const Icon = DOMAIN_ICONS[domain.id] || Sparkles;
            const isSelected = currentDomain === domain.id;

            return (
              <div
                key={domain.id}
                onClick={() => handleSelect(domain.id)}
                className="interactive-domain-card"
                style={{
                  background: isSelected ? 'var(--bg-tertiary)' : 'var(--bg-card)',
                  border: isSelected ? `2px solid ${domain.color}` : '1px solid var(--border-color)',
                  borderRadius: '18px',
                  padding: '24px',
                  cursor: 'pointer',
                  transition: 'all 0.25s cubic-bezier(0.4, 0, 0.2, 1)',
                  display: 'flex',
                  flexDirection: 'column',
                  justifyContent: 'space-between',
                  position: 'relative',
                  boxShadow: isSelected ? `0 10px 30px -10px ${domain.color}40` : 'none'
                }}
              >
                {/* Active check / badge */}
                <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: 16 }}>
                  <div
                    style={{
                      width: 48,
                      height: 48,
                      borderRadius: '14px',
                      background: domain.gradient,
                      display: 'flex',
                      alignItems: 'center',
                      justifyContent: 'center',
                      color: '#ffffff',
                      boxShadow: `0 4px 14px ${domain.color}50`
                    }}
                  >
                    <Icon size={24} />
                  </div>

                  {isSelected ? (
                    <div
                      style={{
                        display: 'flex',
                        alignItems: 'center',
                        gap: 6,
                        color: domain.color,
                        fontWeight: 700,
                        fontSize: '0.85rem'
                      }}
                    >
                      <CheckCircle2 size={18} /> Active Track
                    </div>
                  ) : (
                    <span
                      style={{
                        fontSize: '0.75rem',
                        fontWeight: 700,
                        padding: '3px 10px',
                        borderRadius: '12px',
                        background: 'var(--bg-secondary)',
                        color: 'var(--text-muted)',
                        border: '1px solid var(--border-color)'
                      }}
                    >
                      {domain.badge}
                    </span>
                  )}
                </div>

                {/* Content */}
                <div>
                  <h3 style={{ fontSize: '1.25rem', fontWeight: 700, marginBottom: 8, color: isSelected ? domain.color : 'var(--text-primary)' }}>
                    {domain.title}
                  </h3>
                  <p style={{ fontSize: '0.88rem', color: 'var(--text-secondary)', lineHeight: 1.5, marginBottom: 16 }}>
                    {domain.tagline}
                  </p>

                  {/* Key Skills Pills */}
                  <div style={{ display: 'flex', flexWrap: 'wrap', gap: 6, marginBottom: 20 }}>
                    {domain.skills.slice(0, 4).map((skill, idx) => (
                      <span
                        key={idx}
                        style={{
                          fontSize: '0.75rem',
                          padding: '3px 8px',
                          borderRadius: '6px',
                          background: 'var(--bg-secondary)',
                          color: 'var(--text-secondary)',
                          border: '1px solid var(--border-color)'
                        }}
                      >
                        {skill}
                      </span>
                    ))}
                    {domain.skills.length > 4 && (
                      <span style={{ fontSize: '0.75rem', color: 'var(--text-muted)', alignSelf: 'center' }}>
                        +{domain.skills.length - 4} more
                      </span>
                    )}
                  </div>
                </div>

                {/* Select button */}
                <button
                  className="btn"
                  style={{
                    width: '100%',
                    background: isSelected ? domain.gradient : 'var(--bg-secondary)',
                    color: isSelected ? '#ffffff' : 'var(--text-primary)',
                    border: isSelected ? 'none' : '1px solid var(--border-color)',
                    display: 'flex',
                    alignItems: 'center',
                    justifyContent: 'center',
                    gap: 8,
                    padding: '10px 16px',
                    borderRadius: '12px',
                    fontWeight: 600,
                    fontSize: '0.9rem'
                  }}
                >
                  <span>{isSelected ? 'Continue in This Track' : 'Launch This Track'}</span>
                  <ArrowRight size={16} />
                </button>
              </div>
            );
          })}
        </div>

        {/* Footer Note */}
        <div style={{ textAlign: 'center', fontSize: '0.85rem', color: 'var(--text-muted)' }}>
          💡 <span style={{ fontWeight: 600 }}>Tip:</span> You can seamlessly switch between tracks anytime using the topic selector in the top navigation bar!
        </div>
      </div>
    </div>
  );
}
