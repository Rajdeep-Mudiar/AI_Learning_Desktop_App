import React, { useState, useEffect } from 'react';
import { GitFork, CheckCircle2, Lock, Sparkles, BookOpen } from 'lucide-react';
import { skillService } from '../../services/skillService';
import { useDomain } from '../../contexts/DomainContext';
import LoadingSpinner from '../common/LoadingSpinner';
import ProgressBar from '../common/ProgressBar';
import Badge from '../common/Badge';

export default function SkillTreeGraph() {
  const { currentDomain, domainInfo } = useDomain();
  const [skillData, setSkillData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [activeCategory, setActiveCategory] = useState(null);

  useEffect(() => {
    async function loadTree() {
      try {
        setLoading(true);
        const data = await skillService.getSkillTree();
        setSkillData(data);
      } catch (err) {
        console.error('Failed to load skill tree:', err);
      } finally {
        setLoading(false);
      }
    }
    loadTree();
  }, []);

  // Filter categories according to active domain
  const visibleCategories = React.useMemo(() => {
    if (!skillData?.categories) return [];
    return skillData.categories.filter((cat) => {
      const name = cat.category.toLowerCase();
      if (currentDomain === 'all') return true;
      if (currentDomain === 'dsa') return name.includes('dsa') || name.includes('algorithm') || name.includes('array') || name.includes('tree') || name.includes('stack') || name.includes('graph') || name.includes('structure');
      if (currentDomain === 'cybersecurity') return name.includes('cyber') || name.includes('security') || name.includes('cryptography') || name.includes('network') || name.includes('owasp') || name.includes('threat');
      if (currentDomain === 'web-dev') return name.includes('web') || name.includes('frontend') || name.includes('javascript');
      if (currentDomain === 'app-dev') return name.includes('app') || name.includes('mobile');
      if (currentDomain === 'system-design') return name.includes('system') || name.includes('distributed');
      if (currentDomain === 'github') return name.includes('git') || name.includes('github');
      // ai-ml
      return !name.includes('web') && !name.includes('app') && !name.includes('system') && !name.includes('git') && !name.includes('dsa') && !name.includes('cyber') && !name.includes('security');
    });
  }, [skillData, currentDomain]);

  useEffect(() => {
    if (visibleCategories.length > 0) {
      if (!visibleCategories.some((c) => c.category === activeCategory)) {
        setActiveCategory(visibleCategories[0].category);
      }
    }
  }, [visibleCategories, activeCategory]);

  if (loading) return <LoadingSpinner message="Calculating dynamic skill knowledge graph..." />;
  if (!skillData || visibleCategories.length === 0) {
    return <div className="card" style={{ textAlign: 'center', padding: 32 }}>No skill categories available for this track.</div>;
  }

  const currentCategoryObj = visibleCategories.find((c) => c.category === activeCategory) || visibleCategories[0];

  const getMasteryColor = (pct) => {
    if (pct >= 80) return '#10b981';
    if (pct >= 50) return '#6366f1';
    if (pct >= 20) return '#f59e0b';
    return '#64748b';
  };

  return (
    <div>
      {/* Category Tabs */}
      <div style={{ display: 'flex', gap: 8, overflowX: 'auto', paddingBottom: 12, marginBottom: 20 }}>
        {visibleCategories.map((cat) => {
          const isActive = cat.category === activeCategory;
          return (
            <button
              key={cat.category}
              onClick={() => setActiveCategory(cat.category)}
              className={isActive ? 'btn btn-primary' : 'btn btn-secondary'}
              style={{ padding: '8px 16px', borderRadius: 999, fontSize: '0.85rem' }}
            >
              <span>{cat.category}</span>
              <span style={{
                fontSize: '0.75rem',
                background: isActive ? 'rgba(255, 255, 255, 0.2)' : 'var(--bg-card)',
                padding: '2px 8px',
                borderRadius: 999,
                marginLeft: 4
              }}>
                {cat.overall_mastery}%
              </span>
            </button>
          );
        })}
      </div>

      {/* Selected Category Skill Node Grid */}
      <div className="card" style={{ padding: 28 }}>
        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: 24 }}>
          <div>
            <h2 style={{ fontSize: '1.25rem', marginBottom: 4 }}>{currentCategoryObj.category} Tree</h2>
            <p style={{ fontSize: '0.85rem', color: 'var(--text-secondary)' }}>{currentCategoryObj.description}</p>
          </div>
          <div style={{ textAlign: 'right' }}>
            <div style={{ fontSize: '0.75rem', color: 'var(--text-muted)', textTransform: 'uppercase' }}>Domain Mastery</div>
            <div style={{ fontSize: '1.5rem', fontWeight: 800, color: getMasteryColor(currentCategoryObj.overall_mastery) }}>
              {currentCategoryObj.overall_mastery}%
            </div>
          </div>
        </div>

        {/* Nodes */}
        <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fill, minmax(280px, 1fr))', gap: 18 }}>
          {currentCategoryObj.skills.map((node) => {
            const mastery = node.mastery_percentage || 0;
            const nodeColor = getMasteryColor(mastery);
            const isMastered = mastery >= 80;

            return (
              <div
                key={node.id}
                className="card card-hoverable"
                style={{
                  background: 'var(--bg-secondary)',
                  border: `1.5px solid ${mastery > 0 ? nodeColor : 'var(--border-subtle)'}`,
                  position: 'relative'
                }}
              >
                <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', marginBottom: 10 }}>
                  <span className="badge badge-gray">Level {node.level}</span>
                  {isMastered ? (
                    <CheckCircle2 size={18} style={{ color: '#10b981' }} />
                  ) : mastery > 0 ? (
                    <Sparkles size={18} style={{ color: nodeColor }} />
                  ) : (
                    <Lock size={16} style={{ color: 'var(--text-muted)' }} />
                  )}
                </div>

                <h3 style={{ fontSize: '1rem', fontWeight: 600, marginBottom: 6, color: 'var(--text-primary)' }}>
                  {node.title}
                </h3>
                <p style={{ fontSize: '0.8rem', color: 'var(--text-secondary)', lineHeight: 1.4, marginBottom: 14 }}>
                  {node.description}
                </p>

                {node.prerequisites?.length > 0 && (
                  <div style={{ fontSize: '0.725rem', color: 'var(--text-muted)', marginBottom: 12 }}>
                    Prerequisites: <i>{node.prerequisites.join(', ')}</i>
                  </div>
                )}

                <div style={{ marginTop: 'auto' }}>
                  <div style={{ display: 'flex', justifyContent: 'space-between', fontSize: '0.75rem', marginBottom: 4 }}>
                    <span style={{ color: 'var(--text-muted)' }}>Mastery</span>
                    <span style={{ fontWeight: 700, color: nodeColor }}>{mastery}%</span>
                  </div>
                  <ProgressBar percentage={mastery} color={nodeColor} height={6} />
                </div>
              </div>
            );
          })}
        </div>
      </div>
    </div>
  );
}
