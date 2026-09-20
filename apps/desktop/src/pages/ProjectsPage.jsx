import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { projectService } from '../services/projectService';
import { FolderGit2, ArrowRight, Clock, Layers, Award } from 'lucide-react';

export default function ProjectsPage() {
  const [projects, setProjects] = useState([]);
  const [loading, setLoading] = useState(true);
  const [filterCategory, setFilterCategory] = useState('all');
  const navigate = useNavigate();

  useEffect(() => {
    loadProjects();
  }, []);

  const loadProjects = async () => {
    try {
      setLoading(true);
      const data = await projectService.getProjects();
      setProjects(data);
    } catch (err) {
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  const categories = ['all', 'NLP', 'RAG & LLM', 'Computer Vision'];
  const filtered = filterCategory === 'all' ? projects : projects.filter((p) => p.category === filterCategory);

  return (
    <div className="container" style={{ paddingBottom: 'var(--space-2xl)' }}>
      {/* Header */}
      <div style={{ marginBottom: 'var(--space-xl)' }}>
        <h1 style={{ fontSize: 'var(--font-2xl)', fontWeight: 800, margin: '0 0 var(--space-xs) 0', color: 'var(--color-text-main)', display: 'flex', alignItems: 'center', gap: '8px' }}>
          <FolderGit2 size={24} color="var(--color-primary-400)" /> Guided AI Project Portfolio Builder
        </h1>
        <p style={{ margin: 0, color: 'var(--color-text-muted)', fontSize: 'var(--font-sm)' }}>
          Build production-grade AI systems, defend your design choices in an AI Oral Viva exam, and export GitHub-ready README portfolios.
        </p>
      </div>

      {/* Category filters */}
      <div style={{ display: 'flex', gap: 'var(--space-xs)', marginBottom: 'var(--space-xl)' }}>
        {categories.map((cat) => (
          <button
            key={cat}
            onClick={() => setFilterCategory(cat)}
            style={{
              padding: '6px 14px',
              borderRadius: 'var(--radius-full)',
              background: filterCategory === cat ? 'rgba(99, 102, 241, 0.15)' : 'var(--color-surface)',
              border: filterCategory === cat ? '1px solid var(--color-primary-400)' : '1px solid var(--color-border)',
              color: filterCategory === cat ? 'var(--color-primary-400)' : 'var(--color-text-muted)',
              fontSize: 'var(--font-xs)',
              fontWeight: filterCategory === cat ? 700 : 500,
              cursor: 'pointer',
              textTransform: 'capitalize',
            }}
          >
            {cat}
          </button>
        ))}
      </div>

      {loading ? (
        <div style={{ padding: 'var(--space-2xl)', textAlign: 'center', color: 'var(--color-text-muted)' }}>
          Loading project tracks...
        </div>
      ) : (
        <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(360px, 1fr))', gap: 'var(--space-xl)' }}>
          {filtered.map((proj) => {
            const completedCount = proj.milestones.filter((m) => m.is_completed).length;
            const progressPct = Math.round((completedCount / proj.milestones.length) * 100);

            return (
              <div
                key={proj.id}
                className="card"
                style={{
                  padding: 0,
                  overflow: 'hidden',
                  display: 'flex',
                  flexDirection: 'column',
                  transition: 'transform 0.15s ease, box-shadow 0.15s ease',
                  cursor: 'pointer',
                }}
                onClick={() => navigate(`/projects/${proj.id}`)}
              >
                {/* Banner */}
                <div style={{ background: proj.banner_gradient, padding: 'var(--space-md) var(--space-lg)', color: '#ffffff' }}>
                  <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '4px' }}>
                    <span style={{ fontSize: '10px', textTransform: 'uppercase', letterSpacing: '0.05em', fontWeight: 700, opacity: 0.9 }}>
                      {proj.category} • {proj.difficulty}
                    </span>
                    <span style={{ fontSize: '11px', display: 'flex', alignItems: 'center', gap: '4px', opacity: 0.9 }}>
                      <Clock size={12} /> {proj.estimated_hours}h
                    </span>
                  </div>
                  <h3 style={{ margin: 0, fontSize: 'var(--font-md)', fontWeight: 700 }}>{proj.title}</h3>
                </div>

                {/* Body */}
                <div style={{ padding: 'var(--space-lg)', display: 'flex', flexDirection: 'column', gap: 'var(--space-md)', flex: 1 }}>
                  <p style={{ margin: 0, fontSize: 'var(--font-xs)', color: 'var(--color-text-muted)', lineHeight: 1.5 }}>
                    {proj.tagline}
                  </p>

                  <div style={{ display: 'flex', flexDirection: 'column', gap: '4px' }}>
                    <span style={{ fontSize: '10px', color: 'var(--color-text-muted)', fontWeight: 600 }}>Skills Demonstrated:</span>
                    <div style={{ display: 'flex', gap: '4px', flexWrap: 'wrap' }}>
                      {proj.skills_covered.slice(0, 3).map((skill, idx) => (
                        <span
                          key={idx}
                          style={{
                            fontSize: '10px',
                            padding: '2px 8px',
                            borderRadius: 'var(--radius-sm)',
                            background: 'var(--color-surface-elevated)',
                            color: 'var(--color-text-main)',
                            border: '1px solid var(--color-border)',
                          }}
                        >
                          {skill}
                        </span>
                      ))}
                    </div>
                  </div>

                  {/* Milestone Progress */}
                  <div style={{ marginTop: 'auto', paddingTop: 'var(--space-sm)' }}>
                    <div style={{ display: 'flex', justifyContent: 'space-between', fontSize: '11px', marginBottom: '4px' }}>
                      <span>Milestones Progress</span>
                      <strong style={{ color: progressPct === 100 ? '#10b981' : 'var(--color-primary-400)' }}>
                        {completedCount} / {proj.milestones.length} ({progressPct}%)
                      </strong>
                    </div>
                    <div style={{ height: '6px', background: 'var(--color-surface-elevated)', borderRadius: 'var(--radius-full)', overflow: 'hidden' }}>
                      <div
                        style={{
                          height: '100%',
                          width: `${progressPct}%`,
                          background: progressPct === 100 ? '#10b981' : 'var(--color-primary-400)',
                          borderRadius: 'var(--radius-full)',
                        }}
                      />
                    </div>
                  </div>

                  <div style={{ display: 'flex', justifyContent: 'flex-end', alignItems: 'center', gap: '4px', color: 'var(--color-primary-400)', fontSize: 'var(--font-xs)', fontWeight: 700 }}>
                    <span>Open Project Workspace</span>
                    <ArrowRight size={14} />
                  </div>
                </div>
              </div>
            );
          })}
        </div>
      )}
    </div>
  );
}
