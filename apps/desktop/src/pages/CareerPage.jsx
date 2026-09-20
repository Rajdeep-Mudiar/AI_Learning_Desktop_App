import React, { useState, useEffect } from 'react';
import { careerService } from '../services/careerService';
import { Briefcase, CheckCircle2, Circle, TrendingUp, DollarSign, Lightbulb } from 'lucide-react';

export default function CareerPage() {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    loadCareerOverview();
  }, []);

  const loadCareerOverview = async () => {
    try {
      setLoading(true);
      const res = await careerService.getCareerOverview();
      setData(res);
    } catch (err) {
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  if (loading || !data) {
    return (
      <div className="container" style={{ padding: 'var(--space-2xl)', textAlign: 'center', color: 'var(--color-text-muted)' }}>
        Loading career roadmaps and skill gap analysis...
      </div>
    );
  }

  return (
    <div className="container" style={{ paddingBottom: 'var(--space-2xl)' }}>
      {/* Header */}
      <div style={{ marginBottom: 'var(--space-xl)' }}>
        <h1 style={{ fontSize: 'var(--font-2xl)', fontWeight: 800, margin: '0 0 var(--space-xs) 0', color: 'var(--color-text-main)', display: 'flex', alignItems: 'center', gap: '8px' }}>
          <Briefcase size={24} color="var(--color-primary-400)" /> AI Career Roadmaps & Skill Gap Analysis
        </h1>
        <p style={{ margin: 0, color: 'var(--color-text-muted)', fontSize: 'var(--font-sm)' }}>
          Map your conceptual mastery, autograded challenges, and viva evaluations against industry hiring benchmarks.
        </p>
      </div>

      {/* Recommended Focus Areas */}
      {data.recommended_focus_areas?.length > 0 && (
        <div className="card" style={{ padding: 'var(--space-lg)', marginBottom: 'var(--space-xl)', background: 'linear-gradient(135deg, rgba(99, 102, 241, 0.1), rgba(56, 189, 248, 0.1))', border: '1px solid var(--color-primary-400)' }}>
          <h3 style={{ margin: '0 0 var(--space-xs) 0', fontSize: 'var(--font-sm)', color: 'var(--color-text-main)', display: 'flex', alignItems: 'center', gap: '6px' }}>
            <Lightbulb size={16} color="var(--color-primary-400)" /> Actionable Career Recommendations
          </h3>
          <ul style={{ margin: 0, paddingLeft: '18px', fontSize: 'var(--font-xs)', color: 'var(--color-text-main)', lineHeight: 1.6 }}>
            {data.recommended_focus_areas.map((rec, idx) => (
              <li key={idx}>{rec}</li>
            ))}
          </ul>
        </div>
      )}

      {/* Career Roles Grid */}
      <div style={{ display: 'flex', flexDirection: 'column', gap: 'var(--space-xl)' }}>
        {data.career_paths.map((path) => (
          <div key={path.id} className="card" style={{ padding: 'var(--space-xl)', display: 'flex', flexDirection: 'column', gap: 'var(--space-lg)' }}>
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', flexWrap: 'wrap', gap: 'var(--space-md)' }}>
              <div>
                <h2 style={{ margin: 0, fontSize: 'var(--font-lg)', color: 'var(--color-text-main)' }}>
                  {path.role_title}
                </h2>
                <p style={{ margin: '4px 0 0', fontSize: 'var(--font-xs)', color: 'var(--color-text-muted)' }}>
                  {path.description}
                </p>
              </div>

              <div style={{ display: 'flex', gap: 'var(--space-md)' }}>
                <div style={{ background: 'var(--color-surface-elevated)', padding: '6px 12px', borderRadius: 'var(--radius-md)', display: 'flex', alignItems: 'center', gap: '6px', fontSize: 'var(--font-xs)' }}>
                  <DollarSign size={14} color="#10b981" />
                  <span>Avg: <strong>{path.average_salary}</strong></span>
                </div>
                <div style={{ background: 'var(--color-surface-elevated)', padding: '6px 12px', borderRadius: 'var(--radius-md)', display: 'flex', alignItems: 'center', gap: '6px', fontSize: 'var(--font-xs)' }}>
                  <TrendingUp size={14} color="var(--color-primary-400)" />
                  <span>Demand: <strong>{path.market_demand}</strong></span>
                </div>
              </div>
            </div>

            {/* Readiness Bar */}
            <div>
              <div style={{ display: 'flex', justifyContent: 'space-between', fontSize: '11px', marginBottom: '4px' }}>
                <span>Job Readiness Match</span>
                <strong style={{ color: path.readiness_percentage >= 80 ? '#10b981' : 'var(--color-primary-400)' }}>
                  {path.readiness_percentage}% Ready
                </strong>
              </div>
              <div style={{ height: '8px', background: 'var(--color-surface-elevated)', borderRadius: 'var(--radius-full)', overflow: 'hidden' }}>
                <div
                  style={{
                    height: '100%',
                    width: `${path.readiness_percentage}%`,
                    background: path.readiness_percentage >= 80 ? '#10b981' : 'var(--color-primary-400)',
                    borderRadius: 'var(--radius-full)',
                  }}
                />
              </div>
            </div>

            {/* Skill Requirements Checklist */}
            <div>
              <h4 style={{ margin: '0 0 var(--space-sm) 0', fontSize: 'var(--font-xs)', textTransform: 'uppercase', color: 'var(--color-text-muted)' }}>
                Role Skills & Portfolio Verification
              </h4>
              <div style={{ display: 'flex', flexDirection: 'column', gap: '6px' }}>
                {path.skills_required.map((skill, idx) => (
                  <div
                    key={idx}
                    style={{
                      padding: '8px 12px',
                      borderRadius: 'var(--radius-sm)',
                      background: 'var(--color-surface-elevated)',
                      display: 'flex',
                      justifyContent: 'space-between',
                      alignItems: 'center',
                      fontSize: 'var(--font-xs)',
                    }}
                  >
                    <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                      {skill.is_mastered ? (
                        <CheckCircle2 size={16} color="#10b981" />
                      ) : (
                        <Circle size={16} color="var(--color-text-muted)" />
                      )}
                      <span style={{ fontWeight: 600, color: 'var(--color-text-main)' }}>
                        {skill.skill_name}
                      </span>
                    </div>

                    <div style={{ display: 'flex', alignItems: 'center', gap: '12px' }}>
                      <span style={{ fontSize: '10px', color: skill.importance === 'Must Have' ? '#ef4444' : 'var(--color-text-muted)' }}>
                        {skill.importance}
                      </span>
                      <span style={{ fontSize: '10px', color: 'var(--color-primary-400)' }}>
                        📖 {skill.matching_course}
                      </span>
                    </div>
                  </div>
                ))}
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}
