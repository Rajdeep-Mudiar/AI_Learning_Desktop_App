import React, { useState, useEffect } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import { projectService } from '../services/projectService';
import VivaSimulatorModal from '../components/projects/VivaSimulatorModal';
import PortfolioExportModal from '../components/projects/PortfolioExportModal';
import { ArrowLeft, CheckCircle2, Circle, Award, FileText, Download, Code, Play } from 'lucide-react';

export default function ProjectDetailPage() {
  const { projectId } = useParams();
  const navigate = useNavigate();

  const [project, setProject] = useState(null);
  const [loading, setLoading] = useState(true);
  const [activeStep, setActiveStep] = useState(1);

  // Modals
  const [showVivaModal, setShowVivaModal] = useState(false);
  const [showExportModal, setShowExportModal] = useState(false);
  const [exportData, setExportData] = useState(null);

  useEffect(() => {
    loadProjectDetail();
  }, [projectId]);

  const loadProjectDetail = async () => {
    try {
      setLoading(true);
      const data = await projectService.getProject(projectId);
      setProject(data);
    } catch (err) {
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  const handleOpenExport = async () => {
    try {
      const data = await projectService.getPortfolioExport(projectId);
      setExportData(data);
      setShowExportModal(true);
    } catch (err) {
      console.error(err);
    }
  };

  const toggleMilestoneCompleted = (milestoneId) => {
    if (!project) return;
    setProject((prev) => ({
      ...prev,
      milestones: prev.milestones.map((m) =>
        m.id === milestoneId ? { ...m, is_completed: !m.is_completed } : m
      ),
    }));
  };

  if (loading) {
    return (
      <div className="container" style={{ padding: 'var(--space-2xl)', textAlign: 'center', color: 'var(--color-text-muted)' }}>
        Loading project workspace...
      </div>
    );
  }

  if (!project) {
    return (
      <div className="container" style={{ padding: 'var(--space-2xl)', textAlign: 'center' }}>
        <h2>Project Track Not Found</h2>
        <button onClick={() => navigate('/projects')} className="btn btn-primary" style={{ marginTop: 'var(--space-md)' }}>
          Back to Projects
        </button>
      </div>
    );
  }

  const currentMilestone = project.milestones[activeStep - 1] || project.milestones[0];
  const completedCount = project.milestones.filter((m) => m.is_completed).length;
  const progressPct = Math.round((completedCount / project.milestones.length) * 100);

  return (
    <div className="container" style={{ paddingBottom: 'var(--space-2xl)' }}>
      {/* Back navigation */}
      <button
        onClick={() => navigate('/projects')}
        style={{
          background: 'none',
          border: 'none',
          color: 'var(--color-text-muted)',
          display: 'flex',
          alignItems: 'center',
          gap: '6px',
          cursor: 'pointer',
          fontSize: 'var(--font-xs)',
          marginBottom: 'var(--space-md)',
        }}
      >
        <ArrowLeft size={14} />
        <span>Back to Project Catalog</span>
      </button>

      {/* Project Banner Header */}
      <div
        style={{
          background: project.banner_gradient,
          borderRadius: 'var(--radius-lg)',
          padding: 'var(--space-xl)',
          color: '#ffffff',
          marginBottom: 'var(--space-xl)',
          display: 'flex',
          justifyContent: 'space-between',
          alignItems: 'flex-start',
          flexWrap: 'wrap',
          gap: 'var(--space-md)',
          boxShadow: 'var(--shadow-md)',
        }}
      >
        <div style={{ maxWidth: '650px' }}>
          <div style={{ fontSize: '11px', textTransform: 'uppercase', letterSpacing: '0.05em', opacity: 0.9, marginBottom: '4px', fontWeight: 700 }}>
            {project.category} • {project.difficulty} Track • Dataset: {project.dataset_name}
          </div>
          <h1 style={{ margin: '0 0 var(--space-xs) 0', fontSize: 'var(--font-xl)', fontWeight: 800 }}>
            {project.title}
          </h1>
          <p style={{ margin: 0, fontSize: 'var(--font-xs)', opacity: 0.95, lineHeight: 1.5 }}>
            {project.description}
          </p>
        </div>

        <div style={{ display: 'flex', gap: 'var(--space-sm)' }}>
          <button
            onClick={() => setShowVivaModal(true)}
            className="btn btn-secondary"
            style={{ background: 'rgba(255,255,255,0.2)', border: '1px solid rgba(255,255,255,0.4)', color: '#ffffff', display: 'flex', alignItems: 'center', gap: '6px' }}
          >
            <Award size={16} />
            <span>AI Oral Viva Exam</span>
          </button>
          <button
            onClick={handleOpenExport}
            className="btn"
            style={{ background: '#ffffff', color: '#1e293b', fontWeight: 700, display: 'flex', alignItems: 'center', gap: '6px' }}
          >
            <FileText size={16} />
            <span>Export Portfolio</span>
          </button>
        </div>
      </div>

      {/* Main Workspace Layout */}
      <div style={{ display: 'grid', gridTemplateColumns: '320px 1fr', gap: 'var(--space-xl)', alignItems: 'start' }}>
        
        {/* Left: Milestones Timeline Navigation */}
        <div className="card" style={{ padding: 'var(--space-lg)', display: 'flex', flexDirection: 'column', gap: 'var(--space-md)' }}>
          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
            <h3 style={{ margin: 0, fontSize: 'var(--font-sm)', color: 'var(--color-text-main)' }}>
              Project Milestones
            </h3>
            <span style={{ fontSize: '11px', fontWeight: 700, color: progressPct === 100 ? '#10b981' : 'var(--color-primary-400)' }}>
              {completedCount}/{project.milestones.length} Done
            </span>
          </div>

          <div style={{ display: 'flex', flexDirection: 'column', gap: 'var(--space-xs)' }}>
            {project.milestones.map((m, idx) => {
              const isActive = activeStep === m.step_number;
              return (
                <button
                  key={m.id}
                  onClick={() => setActiveStep(m.step_number)}
                  style={{
                    padding: '10px 12px',
                    borderRadius: 'var(--radius-md)',
                    background: isActive ? 'rgba(99, 102, 241, 0.15)' : 'var(--color-surface-elevated)',
                    border: isActive ? '1.5px solid var(--color-primary-400)' : '1px solid var(--color-border)',
                    display: 'flex',
                    alignItems: 'center',
                    gap: '10px',
                    textAlign: 'left',
                    cursor: 'pointer',
                    transition: 'all 0.15s ease',
                  }}
                >
                  <div
                    onClick={(e) => {
                      e.stopPropagation();
                      toggleMilestoneCompleted(m.id);
                    }}
                    style={{ cursor: 'pointer' }}
                  >
                    {m.is_completed ? (
                      <CheckCircle2 size={18} color="#10b981" />
                    ) : (
                      <Circle size={18} color="var(--color-text-muted)" />
                    )}
                  </div>
                  <div style={{ overflow: 'hidden' }}>
                    <div style={{ fontSize: '10px', color: 'var(--color-text-muted)', textTransform: 'uppercase', fontWeight: 700 }}>
                      Step {m.step_number}
                    </div>
                    <div style={{ fontSize: 'var(--font-xs)', fontWeight: isActive ? 700 : 500, color: isActive ? 'var(--color-primary-400)' : 'var(--color-text-main)', whiteSpace: 'nowrap', overflow: 'hidden', textOverflow: 'ellipsis' }}>
                      {m.title}
                    </div>
                  </div>
                </button>
              );
            })}
          </div>
        </div>

        {/* Right: Milestone Workspace & Code Area */}
        <div className="card" style={{ padding: 'var(--space-xl)', display: 'flex', flexDirection: 'column', gap: 'var(--space-lg)' }}>
          {/* Milestone Header */}
          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', borderBottom: '1px solid var(--color-border)', paddingBottom: 'var(--space-md)' }}>
            <div>
              <span style={{ fontSize: '11px', textTransform: 'uppercase', color: 'var(--color-primary-400)', fontWeight: 700 }}>
                Milestone #{currentMilestone.step_number}
              </span>
              <h2 style={{ margin: '4px 0', fontSize: 'var(--font-lg)', color: 'var(--color-text-main)' }}>
                {currentMilestone.title}
              </h2>
              <p style={{ margin: 0, fontSize: 'var(--font-xs)', color: 'var(--color-text-muted)' }}>
                {currentMilestone.description}
              </p>
            </div>

            <button
              onClick={() => toggleMilestoneCompleted(currentMilestone.id)}
              className={currentMilestone.is_completed ? 'btn btn-secondary' : 'btn btn-primary'}
              style={{ padding: '6px 14px', fontSize: 'var(--font-xs)', display: 'flex', alignItems: 'center', gap: '6px' }}
            >
              {currentMilestone.is_completed ? (
                <>
                  <CheckCircle2 size={14} color="#10b981" />
                  <span>Marked Completed</span>
                </>
              ) : (
                <span>Mark as Completed ✓</span>
              )}
            </button>
          </div>

          {/* Tasks Checklist */}
          <div>
            <h4 style={{ margin: '0 0 var(--space-sm) 0', fontSize: 'var(--font-xs)', textTransform: 'uppercase', color: 'var(--color-text-muted)' }}>
              Engineering Deliverables
            </h4>
            <div style={{ display: 'flex', flexDirection: 'column', gap: '6px' }}>
              {currentMilestone.tasks.map((task, idx) => (
                <div key={idx} style={{ display: 'flex', alignItems: 'center', gap: '8px', fontSize: 'var(--font-xs)', color: 'var(--color-text-main)' }}>
                  <span style={{ color: 'var(--color-primary-400)', fontWeight: 700 }}>{idx + 1}.</span>
                  <span>{task}</span>
                </div>
              ))}
            </div>
          </div>

          {/* Starter Code Block */}
          {currentMilestone.starter_code && (
            <div>
              <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '6px' }}>
                <h4 style={{ margin: 0, fontSize: 'var(--font-xs)', color: 'var(--color-text-main)', display: 'flex', alignItems: 'center', gap: '6px' }}>
                  <Code size={14} /> Starter Template
                </h4>
                <button
                  onClick={() => navigator.clipboard.writeText(currentMilestone.starter_code)}
                  style={{ background: 'none', border: 'none', color: 'var(--color-primary-400)', fontSize: '11px', cursor: 'pointer' }}
                >
                  Copy Code
                </button>
              </div>
              <pre
                style={{
                  padding: 'var(--space-md)',
                  background: '#0d1117',
                  color: '#e6edf3',
                  borderRadius: 'var(--radius-md)',
                  fontFamily: 'var(--font-mono)',
                  fontSize: '11px',
                  overflowX: 'auto',
                  margin: 0,
                }}
              >
                {currentMilestone.starter_code}
              </pre>
            </div>
          )}
        </div>
      </div>

      {/* Viva Exam Modal */}
      {showVivaModal && (
        <VivaSimulatorModal projectId={projectId} onClose={() => setShowVivaModal(false)} />
      )}

      {/* Portfolio Export Modal */}
      {showExportModal && (
        <PortfolioExportModal exportData={exportData} onClose={() => setShowExportModal(false)} />
      )}
    </div>
  );
}
