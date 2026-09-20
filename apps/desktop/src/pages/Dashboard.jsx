import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import {
  Sparkles,
  Trophy,
  BookOpen,
  Clock,
  Activity,
  CheckCircle,
  Cpu,
  Flame,
  Terminal,
  Network,
  FlaskConical,
  Bot,
  ArrowRight,
  TrendingUp,
} from 'lucide-react';
import { dashboardService } from '../services/dashboardService';
import { useAuth } from '../contexts/AuthContext';
import ContinueLearningCard from '../components/dashboard/ContinueLearningCard';
import SkillProgressWidget from '../components/dashboard/SkillProgressWidget';
import DailyChallengeCard from '../components/dashboard/DailyChallengeCard';
import RecommendedLearningCard from '../components/dashboard/RecommendedLearningCard';
import LoadingSpinner from '../components/common/LoadingSpinner';

export default function Dashboard() {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);
  const { user } = useAuth();
  const navigate = useNavigate();

  useEffect(() => {
    async function fetchDashboard() {
      try {
        setLoading(true);
        const res = await dashboardService.getDashboardSummary();
        setData(res);
      } catch (err) {
        console.error('Failed to load dashboard:', err);
      } finally {
        setLoading(false);
      }
    }
    fetchDashboard();
  }, []);

  if (loading) return <LoadingSpinner message="Assembling your personalized AI learning cockpit..." />;
  if (!data) return <div className="card">Unable to load dashboard data.</div>;

  const streakCount = user?.streak?.current || data.streak_days || 1;

  return (
    <div className="animate-fade-in" style={{ paddingBottom: 'var(--space-2xl)' }}>
      {/* Hero Welcome Banner */}
      <div
        style={{
          background: 'linear-gradient(135deg, rgba(99, 102, 241, 0.16) 0%, rgba(14, 165, 233, 0.08) 50%, var(--bg-card) 100%)',
          border: '1px solid var(--border-highlight)',
          borderRadius: 'var(--radius-lg)',
          padding: '28px 32px',
          marginBottom: 'var(--space-xl)',
          position: 'relative',
          overflow: 'hidden',
          boxShadow: '0 8px 32px -4px rgba(0, 0, 0, 0.4), inset 0 1px 0 rgba(255, 255, 255, 0.1)',
        }}
      >
        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', flexWrap: 'wrap', gap: 'var(--space-md)' }}>
          <div style={{ maxWidth: '640px' }}>
            <div style={{ display: 'inline-flex', alignItems: 'center', gap: '6px', background: 'rgba(99, 102, 241, 0.2)', border: '1px solid rgba(99, 102, 241, 0.4)', padding: '3px 10px', borderRadius: 'var(--radius-full)', fontSize: '0.725rem', fontWeight: 700, color: 'var(--color-primary-400)', textTransform: 'uppercase', marginBottom: '10px' }}>
              <Sparkles size={12} /> AI Engineering Cockpit
            </div>
            <h1 style={{ fontSize: 'var(--font-3xl)', fontWeight: 800, margin: '0 0 8px 0', color: 'var(--color-text-main)', letterSpacing: '-0.03em' }}>
              {data.greeting || `Welcome back, ${user?.name || 'Student'}!`}
            </h1>
            <p style={{ margin: 0, color: 'var(--color-text-secondary)', fontSize: 'var(--font-sm)', lineHeight: 1.6 }}>
              Master Artificial Intelligence through the loop: <strong>Learn → Visualize → Experiment → Code → Break → Debug → Challenge → Build</strong>.
            </p>
          </div>

          <div style={{ display: 'flex', gap: 'var(--space-sm)', alignItems: 'center' }}>
            <div
              style={{
                background: 'rgba(245, 158, 11, 0.15)',
                border: '1px solid rgba(245, 158, 11, 0.35)',
                borderRadius: 'var(--radius-md)',
                padding: '10px 16px',
                display: 'flex',
                alignItems: 'center',
                gap: '8px',
                color: '#fbbf24',
              }}
            >
              <Flame size={20} style={{ fill: '#fbbf24' }} />
              <div>
                <div style={{ fontSize: '1.25rem', fontWeight: 800, lineHeight: 1 }}>{streakCount} Days</div>
                <div style={{ fontSize: '0.675rem', color: 'rgba(251, 191, 36, 0.8)', fontWeight: 600 }}>ACTIVE STREAK</div>
              </div>
            </div>

            <button onClick={() => navigate('/learn')} className="btn btn-primary" style={{ padding: '12px 20px' }}>
              <BookOpen size={16} />
              <span>Explore Curriculum</span>
            </button>
          </div>
        </div>

        {/* Quick-Jump Lab Hub Bar */}
        <div style={{ display: 'flex', gap: '10px', marginTop: '22px', flexWrap: 'wrap', borderTop: '1px solid rgba(255, 255, 255, 0.08)', paddingTop: '18px' }}>
          <span style={{ fontSize: '0.75rem', color: 'var(--color-text-muted)', display: 'flex', alignItems: 'center', fontWeight: 600, marginRight: '4px' }}>
            Quick Labs:
          </span>
          {[
            { label: 'Algorithm Lab', icon: Cpu, path: '/algorithms', color: '#6366f1' },
            { label: 'Deep Learning', icon: Network, path: '/deep-learning', color: '#0ea5e9' },
            { label: 'Python Sandbox', icon: Terminal, path: '/playground', color: '#10b981' },
            { label: 'ML Experiments', icon: FlaskConical, path: '/experiments', color: '#a855f7' },
            { label: 'AI Tutor', icon: Bot, path: '/tutor', color: '#ec4899' },
          ].map((lab) => {
            const Icon = lab.icon;
            return (
              <button
                key={lab.path}
                onClick={() => navigate(lab.path)}
                style={{
                  background: 'var(--bg-tertiary)',
                  border: '1px solid var(--border-subtle)',
                  borderRadius: 'var(--radius-sm)',
                  padding: '6px 12px',
                  display: 'inline-flex',
                  alignItems: 'center',
                  gap: '6px',
                  fontSize: '0.775rem',
                  fontWeight: 600,
                  color: 'var(--color-text-main)',
                  transition: 'all var(--transition-fast)',
                }}
                onMouseEnter={(e) => {
                  e.currentTarget.style.borderColor = lab.color;
                  e.currentTarget.style.transform = 'translateY(-1px)';
                }}
                onMouseLeave={(e) => {
                  e.currentTarget.style.borderColor = 'var(--border-subtle)';
                  e.currentTarget.style.transform = 'none';
                }}
              >
                <Icon size={14} color={lab.color} />
                <span>{lab.label}</span>
              </button>
            );
          })}
        </div>
      </div>

      {/* Main Grid Layout */}
      <div className="dashboard-grid">
        {/* Left Primary Column */}
        <div className="dashboard-left-col">
          {/* Continue Learning Card */}
          <ContinueLearningCard data={data.continue_learning} />

          {/* Daily Challenge Widget */}
          <DailyChallengeCard challenge={data.daily_challenge} />

          {/* Recommended Next Lessons */}
          <RecommendedLearningCard recommendations={data.recommended_learning} />

          {/* Recent Experiments & Projects Summaries */}
          <div className="card" style={{ padding: 'var(--space-xl)' }}>
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: 'var(--space-md)' }}>
              <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                <Activity size={18} color="var(--color-primary-400)" />
                <h3 style={{ margin: 0, fontSize: 'var(--font-md)', color: 'var(--color-text-main)' }}>
                  Laboratory & Project Activity
                </h3>
              </div>
              <button onClick={() => navigate('/experiments')} className="btn btn-ghost btn-sm" style={{ fontSize: '0.75rem', color: 'var(--color-primary-400)' }}>
                View All Labs <ArrowRight size={12} />
              </button>
            </div>

            <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(240px, 1fr))', gap: 'var(--space-md)' }}>
              {/* Experiments */}
              <div style={{ background: 'var(--color-surface-elevated)', padding: '16px', borderRadius: 'var(--radius-md)', border: '1px solid var(--border-subtle)' }}>
                <div style={{ fontSize: '0.7rem', color: 'var(--color-text-muted)', textTransform: 'uppercase', fontWeight: 700, marginBottom: '8px', letterSpacing: '0.04em' }}>
                  Recent Model Runs
                </div>
                {data.recent_experiments?.map((exp) => (
                  <div key={exp.id} style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', fontSize: 'var(--font-xs)', padding: '6px 0', borderBottom: '1px solid rgba(255, 255, 255, 0.04)' }}>
                    <span style={{ fontWeight: 500 }}>{exp.title}</span>
                    <span style={{ color: '#10b981', fontWeight: 700 }}>{Math.round(exp.accuracy * 100)}% Acc</span>
                  </div>
                ))}
              </div>

              {/* Projects */}
              <div style={{ background: 'var(--color-surface-elevated)', padding: '16px', borderRadius: 'var(--radius-md)', border: '1px solid var(--border-subtle)' }}>
                <div style={{ fontSize: '0.7rem', color: 'var(--color-text-muted)', textTransform: 'uppercase', fontWeight: 700, marginBottom: '8px', letterSpacing: '0.04em' }}>
                  Portfolio Projects
                </div>
                {data.projects_in_progress?.map((prj) => (
                  <div key={prj.id} style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', fontSize: 'var(--font-xs)', padding: '6px 0', borderBottom: '1px solid rgba(255, 255, 255, 0.04)' }}>
                    <span style={{ fontWeight: 500 }}>{prj.title}</span>
                    <span style={{ color: '#38bdf8', fontWeight: 700 }}>{prj.completion_percentage}%</span>
                  </div>
                ))}
              </div>
            </div>
          </div>
        </div>

        {/* Right Secondary Column */}
        <div className="dashboard-right-col">
          {/* Skill Progress Widget */}
          <SkillProgressWidget skills={data.skill_mastery_bars} />

          {/* Stats Overview Card */}
          <div className="card" style={{ padding: 'var(--space-xl)', background: 'linear-gradient(135deg, var(--bg-card) 0%, rgba(99, 102, 241, 0.06) 100%)' }}>
            <h3 style={{ margin: '0 0 var(--space-md) 0', fontSize: 'var(--font-sm)', textTransform: 'uppercase', color: 'var(--color-text-muted)', fontWeight: 700, letterSpacing: '0.04em' }}>
              Your Progress Milestones
            </h3>
            <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: 'var(--space-md)' }}>
              <div style={{ background: 'var(--color-surface-elevated)', padding: '16px', borderRadius: 'var(--radius-md)', textAlign: 'center', border: '1px solid var(--border-subtle)' }}>
                <div style={{ fontSize: 'var(--font-2xl)', fontWeight: 800, color: '#38bdf8' }}>{data.total_lessons_completed}</div>
                <div style={{ fontSize: '0.7rem', color: 'var(--color-text-muted)', fontWeight: 600, textTransform: 'uppercase', marginTop: '2px' }}>Lessons Completed</div>
              </div>
              <div style={{ background: 'var(--color-surface-elevated)', padding: '16px', borderRadius: 'var(--radius-md)', textAlign: 'center', border: '1px solid var(--border-subtle)' }}>
                <div style={{ fontSize: 'var(--font-2xl)', fontWeight: 800, color: '#10b981' }}>{data.total_quizzes_passed}</div>
                <div style={{ fontSize: '0.7rem', color: 'var(--color-text-muted)', fontWeight: 600, textTransform: 'uppercase', marginTop: '2px' }}>Quizzes Mastered</div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
