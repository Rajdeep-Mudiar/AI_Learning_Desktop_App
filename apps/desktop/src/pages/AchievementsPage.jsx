import React, { useState, useEffect } from 'react';
import { achievementService } from '../services/achievementService';
import BadgeCard from '../components/achievements/BadgeCard';
import { Trophy, Flame, Zap, Award, CheckCircle2, Download } from 'lucide-react';

export default function AchievementsPage() {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [categoryFilter, setCategoryFilter] = useState('all');
  const [showCertModal, setShowCertModal] = useState(false);

  useEffect(() => {
    loadAchievements();
  }, []);

  const loadAchievements = async () => {
    try {
      setLoading(true);
      const res = await achievementService.getAchievements();
      setData(res);
    } catch (err) {
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  const categories = ['all', 'Curriculum', 'Coding', 'Experimentation', 'Projects'];

  if (loading || !data) {
    return (
      <div className="container" style={{ padding: 'var(--space-2xl)', textAlign: 'center', color: 'var(--color-text-muted)' }}>
        Loading achievements and mastery badges...
      </div>
    );
  }

  const filteredBadges = categoryFilter === 'all' ? data.badges : data.badges.filter((b) => b.category === categoryFilter);
  const levelProgress = Math.min(100, Math.round(((data.total_xp % 250) / 250) * 100));

  return (
    <div className="container" style={{ paddingBottom: 'var(--space-2xl)' }}>
      {/* Header */}
      <div style={{ marginBottom: 'var(--space-xl)' }}>
        <h1 style={{ fontSize: 'var(--font-2xl)', fontWeight: 800, margin: '0 0 var(--space-xs) 0', color: 'var(--color-text-main)', display: 'flex', alignItems: 'center', gap: '8px' }}>
          <Trophy size={24} color="#f59e0b" /> Skill Mastery & Achievement Badges
        </h1>
        <p style={{ margin: 0, color: 'var(--color-text-muted)', fontSize: 'var(--font-sm)' }}>
          Track your journey from AI Novice to Senior AI Systems Architect with verifiable concept trophies and certifications.
        </p>
      </div>

      {/* Top Stats Overview */}
      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(220px, 1fr))', gap: 'var(--space-md)', marginBottom: 'var(--space-xl)' }}>
        {/* Level Card */}
        <div className="card" style={{ padding: 'var(--space-lg)', display: 'flex', flexDirection: 'column', gap: 'var(--space-xs)' }}>
          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
            <span style={{ fontSize: 'var(--font-xs)', color: 'var(--color-text-muted)', fontWeight: 600 }}>Current Rank</span>
            <Zap size={18} color="var(--color-primary-400)" />
          </div>
          <div style={{ fontSize: 'var(--font-xl)', fontWeight: 800, color: 'var(--color-text-main)' }}>
            Level {data.current_level}
          </div>
          <div style={{ fontSize: 'var(--font-xs)', color: 'var(--color-primary-400)', fontWeight: 700 }}>
            {data.level_title}
          </div>
          <div style={{ marginTop: '8px' }}>
            <div style={{ display: 'flex', justifyContent: 'space-between', fontSize: '10px', color: 'var(--color-text-muted)', marginBottom: '2px' }}>
              <span>Level Progress</span>
              <span>{levelProgress}%</span>
            </div>
            <div style={{ height: '6px', background: 'var(--color-surface-elevated)', borderRadius: 'var(--radius-full)', overflow: 'hidden' }}>
              <div style={{ height: '100%', width: `${levelProgress}%`, background: 'var(--color-primary-400)', borderRadius: 'var(--radius-full)' }} />
            </div>
          </div>
        </div>

        {/* Total XP */}
        <div className="card" style={{ padding: 'var(--space-lg)', display: 'flex', flexDirection: 'column', gap: 'var(--space-xs)' }}>
          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
            <span style={{ fontSize: 'var(--font-xs)', color: 'var(--color-text-muted)', fontWeight: 600 }}>Total Experience</span>
            <Trophy size={18} color="#f59e0b" />
          </div>
          <div style={{ fontSize: 'var(--font-2xl)', fontWeight: 800, color: '#f59e0b' }}>
            {data.total_xp.toLocaleString()} XP
          </div>
          <span style={{ fontSize: '11px', color: 'var(--color-text-muted)' }}>
            Next level at {data.next_level_xp} XP
          </span>
        </div>

        {/* Streak Days */}
        <div className="card" style={{ padding: 'var(--space-lg)', display: 'flex', flexDirection: 'column', gap: 'var(--space-xs)' }}>
          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
            <span style={{ fontSize: 'var(--font-xs)', color: 'var(--color-text-muted)', fontWeight: 600 }}>Daily Streak</span>
            <Flame size={18} color="#ef4444" />
          </div>
          <div style={{ fontSize: 'var(--font-2xl)', fontWeight: 800, color: '#ef4444' }}>
            {data.streak_days} Days 🔥
          </div>
          <span style={{ fontSize: '11px', color: 'var(--color-text-muted)' }}>
            Consistent practice active
          </span>
        </div>

        {/* Badges Unlocked */}
        <div className="card" style={{ padding: 'var(--space-lg)', display: 'flex', flexDirection: 'column', gap: 'var(--space-xs)' }}>
          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
            <span style={{ fontSize: 'var(--font-xs)', color: 'var(--color-text-muted)', fontWeight: 600 }}>Trophies Earned</span>
            <Award size={18} color="#10b981" />
          </div>
          <div style={{ fontSize: 'var(--font-2xl)', fontWeight: 800, color: '#10b981' }}>
            {data.unlocked_badges_count} / {data.total_badges_count}
          </div>
          <span style={{ fontSize: '11px', color: 'var(--color-text-muted)' }}>
            {Math.round((data.unlocked_badges_count / data.total_badges_count) * 100)}% Collection Unlocked
          </span>
        </div>
      </div>

      {/* Certificate Eligibility Banner */}
      {data.certificate_eligible && (
        <div
          style={{
            background: 'linear-gradient(135deg, rgba(99, 102, 241, 0.15), rgba(56, 189, 248, 0.15))',
            border: '1px solid var(--color-primary-400)',
            borderRadius: 'var(--radius-lg)',
            padding: 'var(--space-lg)',
            marginBottom: 'var(--space-xl)',
            display: 'flex',
            justifyContent: 'space-between',
            alignItems: 'center',
            flexWrap: 'wrap',
            gap: 'var(--space-md)',
          }}
        >
          <div style={{ display: 'flex', alignItems: 'center', gap: '12px' }}>
            <Award size={32} color="var(--color-primary-400)" />
            <div>
              <h3 style={{ margin: 0, fontSize: 'var(--font-md)', color: 'var(--color-text-main)' }}>
                🎓 Certificate of AI Competency Unlocked!
              </h3>
              <p style={{ margin: '2px 0 0', fontSize: 'var(--font-xs)', color: 'var(--color-text-muted)' }}>
                You have satisfied the required foundation badges and project defense milestones.
              </p>
            </div>
          </div>
          <button
            onClick={() => setShowCertModal(true)}
            className="btn btn-primary"
            style={{ display: 'flex', alignItems: 'center', gap: '6px', padding: '8px 16px' }}
          >
            <Download size={14} />
            <span>View Certificate</span>
          </button>
        </div>
      )}

      {/* Category Tabs */}
      <div style={{ display: 'flex', gap: 'var(--space-xs)', marginBottom: 'var(--space-lg)', borderBottom: '1px solid var(--color-border)', paddingBottom: 'var(--space-xs)' }}>
        {categories.map((cat) => (
          <button
            key={cat}
            onClick={() => setCategoryFilter(cat)}
            style={{
              padding: '6px 14px',
              borderRadius: 'var(--radius-full)',
              background: categoryFilter === cat ? 'rgba(99, 102, 241, 0.15)' : 'none',
              border: categoryFilter === cat ? '1px solid var(--color-primary-400)' : '1px solid transparent',
              color: categoryFilter === cat ? 'var(--color-primary-400)' : 'var(--color-text-muted)',
              fontSize: 'var(--font-xs)',
              fontWeight: categoryFilter === cat ? 700 : 500,
              cursor: 'pointer',
              textTransform: 'capitalize',
            }}
          >
            {cat}
          </button>
        ))}
      </div>

      {/* Badges Grid */}
      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(280px, 1fr))', gap: 'var(--space-lg)' }}>
        {filteredBadges.map((b) => (
          <BadgeCard key={b.id} badge={b} />
        ))}
      </div>

      {/* Certificate Modal */}
      {showCertModal && (
        <div
          style={{
            position: 'fixed',
            top: 0,
            left: 0,
            right: 0,
            bottom: 0,
            backgroundColor: 'rgba(0, 0, 0, 0.75)',
            backdropFilter: 'blur(6px)',
            zIndex: 9999,
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center',
            padding: 'var(--space-md)',
          }}
          onClick={() => setShowCertModal(false)}
        >
          <div
            style={{
              background: 'var(--color-surface)',
              border: '2px solid #f59e0b',
              borderRadius: 'var(--radius-xl)',
              width: '100%',
              maxWidth: '640px',
              padding: 'var(--space-2xl)',
              boxShadow: 'var(--shadow-xl)',
              textAlign: 'center',
              position: 'relative',
            }}
            onClick={(e) => e.stopPropagation()}
          >
            <div style={{ fontSize: '40px', marginBottom: '8px' }}>🏆</div>
            <h2 style={{ margin: '0 0 4px', fontSize: 'var(--font-xl)', color: 'var(--color-text-main)', letterSpacing: '0.05em', textTransform: 'uppercase' }}>
              Certificate of Achievement
            </h2>
            <p style={{ margin: '0 0 var(--space-lg)', fontSize: 'var(--font-xs)', color: 'var(--color-text-muted)' }}>
              AI Learning Lab • Verified Technical Competency
            </p>

            <div style={{ padding: 'var(--space-lg)', background: 'var(--color-surface-elevated)', borderRadius: 'var(--radius-md)', margin: 'var(--space-md) 0' }}>
              <p style={{ margin: '0 0 8px', fontSize: 'var(--font-xs)', color: 'var(--color-text-muted)' }}>This certifies that</p>
              <h3 style={{ margin: '0 0 8px', fontSize: 'var(--font-lg)', color: 'var(--color-primary-400)' }}>
                AI Engineer Candidate
              </h3>
              <p style={{ margin: 0, fontSize: 'var(--font-xs)', color: 'var(--color-text-main)', lineHeight: 1.5 }}>
                has successfully demonstrated proficiency in mathematical AI fundamentals, autograded algorithmic implementations, deep learning architectures, and defended real-world project pipelines.
              </p>
            </div>

            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', fontSize: '11px', color: 'var(--color-text-muted)', marginTop: 'var(--space-lg)' }}>
              <span>Verification ID: <strong>AILL-2026-CERT</strong></span>
              <span>Issued: {new Date().toLocaleDateString()}</span>
            </div>

            <div style={{ marginTop: 'var(--space-xl)', display: 'flex', justifyContent: 'center', gap: 'var(--space-sm)' }}>
              <button onClick={() => setShowCertModal(false)} className="btn btn-secondary">
                Close
              </button>
              <button onClick={() => alert('Certificate PDF generation ready for export!')} className="btn btn-primary">
                Download PDF
              </button>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}
