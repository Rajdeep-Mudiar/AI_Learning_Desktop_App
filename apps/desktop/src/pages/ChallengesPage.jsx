import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { Award, Code2, ArrowRight, Sparkles, CheckCircle2, ChevronRight } from 'lucide-react';
import { challengeService } from '../services/challengeService';
import { useDomain } from '../contexts/DomainContext';
import LoadingSpinner from '../components/common/LoadingSpinner';
import Badge from '../components/common/Badge';

export default function ChallengesPage() {
  const { currentDomain, domainInfo } = useDomain();
  const [challenges, setChallenges] = useState([]);
  const [loading, setLoading] = useState(true);
  const [filterDifficulty, setFilterDifficulty] = useState('All');
  const navigate = useNavigate();

  useEffect(() => {
    async function loadChallenges() {
      try {
        setLoading(true);
        const data = await challengeService.listChallenges();
        setChallenges(data);
      } catch (err) {
        console.error('Failed to load challenges:', err);
      } finally {
        setLoading(false);
      }
    }
    loadChallenges();
  }, []);

  const filtered = challenges.filter((c) => {
    const matchesDomain = currentDomain === 'all' || (c.domain || 'ai-ml') === currentDomain;
    const matchesDiff = filterDifficulty === 'All' || c.difficulty === filterDifficulty;
    return matchesDomain && matchesDiff;
  });

  const getDifficultyBadge = (diff) => {
    switch (diff) {
      case 'Beginner': return 'green';
      case 'Intermediate': return 'purple';
      case 'Advanced': return 'pink';
      default: return 'blue';
    }
  };

  if (loading) return <LoadingSpinner message="Loading coding challenges..." />;

  return (
    <div className="animate-fade-in" style={{ maxWidth: '1000px' }}>
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: 24, flexWrap: 'wrap', gap: 12 }}>
        <div>
          <div style={{ display: 'flex', alignItems: 'center', gap: 8, marginBottom: 4 }}>
            <span className="badge badge-purple" style={{ background: `${domainInfo.color}20`, color: domainInfo.color, border: `1px solid ${domainInfo.color}40` }}>
              {currentDomain === 'all' ? 'All Tracks Autograder' : `${domainInfo.title} Autograder`}
            </span>
          </div>
          <h1 style={{ fontSize: '1.75rem', marginBottom: 6 }}>
            {currentDomain === 'all' ? 'Engineering Challenges' : `${domainInfo.title} Challenges`}
          </h1>
          <p style={{ color: 'var(--text-secondary)', fontSize: '0.925rem' }}>
            Implement core algorithms and data patterns from scratch and verify against automated sandbox test suites.
          </p>
        </div>

        {/* Difficulty Filter */}
        <div style={{ display: 'flex', gap: 6 }}>
          {['All', 'Beginner', 'Intermediate'].map((diff) => (
            <button
              key={diff}
              onClick={() => setFilterDifficulty(diff)}
              className={filterDifficulty === diff ? 'btn btn-primary btn-sm' : 'btn btn-secondary btn-sm'}
            >
              {diff}
            </button>
          ))}
        </div>
      </div>

      {/* Challenges Grid */}
      <div style={{ display: 'flex', flexDirection: 'column', gap: 14 }}>
        {filtered.map((item) => (
          <div
            key={item.id}
            onClick={() => navigate(`/challenges/${item.id}`)}
            className="card card-hoverable"
            style={{
              padding: '20px 24px',
              display: 'flex',
              justifyContent: 'space-between',
              alignItems: 'center',
              cursor: 'pointer'
            }}
          >
            <div style={{ flex: 1, paddingRight: 20 }}>
              <div style={{ display: 'flex', alignItems: 'center', gap: 8, marginBottom: 6 }}>
                <Badge variant={getDifficultyBadge(item.difficulty)}>{item.difficulty}</Badge>
                <span style={{ fontSize: '0.75rem', color: 'var(--text-muted)' }}>• {item.category}</span>
              </div>
              <h3 style={{ fontSize: '1.1rem', color: 'var(--text-primary)', marginBottom: 6 }}>{item.title}</h3>
              <p style={{ fontSize: '0.85rem', color: 'var(--text-secondary)', marginBottom: 10 }}>{item.description}</p>

              <div style={{ display: 'flex', gap: 6, flexWrap: 'wrap' }}>
                {item.skills_tested?.map((skill, idx) => (
                  <span
                    key={idx}
                    style={{
                      fontSize: '0.7rem',
                      padding: '2px 8px',
                      borderRadius: 4,
                      background: 'var(--bg-tertiary)',
                      color: 'var(--text-muted)',
                      border: '1px solid var(--border-subtle)'
                    }}
                  >
                    {skill}
                  </span>
                ))}
              </div>
            </div>

            <div style={{ display: 'flex', alignItems: 'center', gap: 16 }}>
              <span className="badge badge-amber">+{item.xp_reward} XP</span>
              <button className="btn btn-primary btn-sm">
                <span>Solve</span>
                <ChevronRight size={14} />
              </button>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}
