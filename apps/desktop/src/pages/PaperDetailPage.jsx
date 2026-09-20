import React, { useState, useEffect } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import { researchService } from '../services/researchService';
import EquationExplainerCard from '../components/research/EquationExplainerCard';
import ReproductionChecklist from '../components/research/ReproductionChecklist';
import { ArrowLeft, BookOpen, ExternalLink, Award, CheckCircle2, Save } from 'lucide-react';

export default function PaperDetailPage() {
  const { paperId } = useParams();
  const navigate = useNavigate();

  const [paper, setPaper] = useState(null);
  const [loading, setLoading] = useState(true);
  const [activeTab, setActiveTab] = useState('equations'); // 'equations' | 'reproduction' | 'notes'
  const [notes, setNotes] = useState('');
  const [savedNotes, setSavedNotes] = useState(false);

  useEffect(() => {
    loadPaper();
    const saved = localStorage.getItem(`notes_${paperId}`);
    if (saved) setNotes(saved);
  }, [paperId]);

  const loadPaper = async () => {
    try {
      setLoading(true);
      const data = await researchService.getPaper(paperId);
      setPaper(data);
    } catch (err) {
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  const handleSaveNotes = () => {
    localStorage.setItem(`notes_${paperId}`, notes);
    setSavedNotes(true);
    setTimeout(() => setSavedNotes(false), 2000);
  };

  const handleToggleReproductionStep = (stepNumber) => {
    if (!paper) return;
    setPaper((prev) => ({
      ...prev,
      reproduction_steps: prev.reproduction_steps.map((s) =>
        s.step_number === stepNumber ? { ...s, is_completed: !s.is_completed } : s
      ),
    }));
  };

  if (loading) {
    return (
      <div className="container" style={{ padding: 'var(--space-2xl)', textAlign: 'center', color: 'var(--color-text-muted)' }}>
        Loading paper breakdown and equations...
      </div>
    );
  }

  if (!paper) {
    return (
      <div className="container" style={{ padding: 'var(--space-2xl)', textAlign: 'center' }}>
        <h2>Research Paper Not Found</h2>
        <button onClick={() => navigate('/research')} className="btn btn-primary" style={{ marginTop: 'var(--space-md)' }}>
          Back to Research Mode
        </button>
      </div>
    );
  }

  const completedSteps = paper.reproduction_steps.filter((s) => s.is_completed).length;

  return (
    <div className="container" style={{ paddingBottom: 'var(--space-2xl)' }}>
      {/* Back button */}
      <button
        onClick={() => navigate('/research')}
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
        <span>Back to Paper Catalog</span>
      </button>

      {/* Paper Header Card */}
      <div className="card" style={{ padding: 'var(--space-xl)', marginBottom: 'var(--space-xl)', display: 'flex', flexDirection: 'column', gap: 'var(--space-md)' }}>
        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', flexWrap: 'wrap', gap: 'var(--space-sm)' }}>
          <div>
            <span style={{ fontSize: '10px', textTransform: 'uppercase', color: 'var(--color-primary-400)', fontWeight: 700, padding: '2px 8px', borderRadius: 'var(--radius-full)', background: 'rgba(99, 102, 241, 0.12)' }}>
              {paper.category} • {paper.conference} ({paper.year})
            </span>
            <h1 style={{ margin: '6px 0', fontSize: 'var(--font-xl)', fontWeight: 800, color: 'var(--color-text-main)' }}>
              {paper.title}
            </h1>
            <div style={{ fontSize: 'var(--font-xs)', color: 'var(--color-text-muted)' }}>
              By {paper.authors.join(', ')}
            </div>
          </div>

          <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
            <a
              href={`https://arxiv.org/abs/${paper.arxiv_id}`}
              target="_blank"
              rel="noreferrer"
              className="btn btn-secondary"
              style={{ display: 'flex', alignItems: 'center', gap: '6px', fontSize: '11px', padding: '6px 12px' }}
            >
              <ExternalLink size={13} />
              <span>arXiv:{paper.arxiv_id}</span>
            </a>
          </div>
        </div>

        {/* Abstract */}
        <div style={{ background: 'var(--color-surface-elevated)', padding: 'var(--space-md)', borderRadius: 'var(--radius-md)', fontSize: 'var(--font-xs)', color: 'var(--color-text-muted)', lineHeight: 1.6 }}>
          <strong>Abstract:</strong> {paper.abstract}
        </div>

        {/* Key Innovations */}
        <div>
          <h4 style={{ margin: '0 0 var(--space-xs) 0', fontSize: 'var(--font-xs)', textTransform: 'uppercase', color: 'var(--color-primary-400)' }}>
            Key Conceptual Breakthroughs
          </h4>
          <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(280px, 1fr))', gap: 'var(--space-xs)' }}>
            {paper.key_innovations.map((inn, idx) => (
              <div key={idx} style={{ display: 'flex', alignItems: 'center', gap: '6px', fontSize: 'var(--font-xs)', color: 'var(--color-text-main)' }}>
                <CheckCircle2 size={13} color="#10b981" />
                <span>{inn}</span>
              </div>
            ))}
          </div>
        </div>
      </div>

      {/* Tabs */}
      <div style={{ display: 'flex', gap: 'var(--space-sm)', borderBottom: '1px solid var(--color-border)', marginBottom: 'var(--space-xl)' }}>
        {[
          { id: 'equations', label: `📐 Mathematical Equations (${paper.equations.length})` },
          { id: 'reproduction', label: `🧪 Reproduction Checklist (${completedSteps}/${paper.reproduction_steps.length})` },
          { id: 'notes', label: '📝 Linked Research Notes' },
        ].map((tab) => (
          <button
            key={tab.id}
            onClick={() => setActiveTab(tab.id)}
            style={{
              background: 'none',
              border: 'none',
              padding: '12px 18px',
              color: activeTab === tab.id ? 'var(--color-primary-400)' : 'var(--color-text-muted)',
              borderBottom: activeTab === tab.id ? '2px solid var(--color-primary-400)' : '2px solid transparent',
              fontWeight: activeTab === tab.id ? 700 : 500,
              fontSize: 'var(--font-sm)',
              cursor: 'pointer',
              transition: 'all 0.15s ease',
            }}
          >
            {tab.label}
          </button>
        ))}
      </div>

      {/* Tab 1: Equations */}
      {activeTab === 'equations' && (
        <div style={{ display: 'flex', flexDirection: 'column', gap: 'var(--space-lg)' }}>
          {paper.equations.map((eq, idx) => (
            <EquationExplainerCard key={idx} equation={eq} />
          ))}
        </div>
      )}

      {/* Tab 2: Reproduction */}
      {activeTab === 'reproduction' && (
        <ReproductionChecklist steps={paper.reproduction_steps} onToggleStep={handleToggleReproductionStep} />
      )}

      {/* Tab 3: Notes */}
      {activeTab === 'notes' && (
        <div className="card" style={{ padding: 'var(--space-xl)', display: 'flex', flexDirection: 'column', gap: 'var(--space-md)' }}>
          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
            <h4 style={{ margin: 0, fontSize: 'var(--font-sm)', color: 'var(--color-text-main)' }}>
              Research Notebook for "{paper.title}"
            </h4>
            <button
              onClick={handleSaveNotes}
              className="btn btn-primary"
              style={{ display: 'flex', alignItems: 'center', gap: '6px', fontSize: '11px', padding: '6px 12px' }}
            >
              <Save size={13} />
              <span>{savedNotes ? 'Saved ✓' : 'Save Notes'}</span>
            </button>
          </div>
          <textarea
            className="input"
            rows={12}
            value={notes}
            onChange={(e) => setNotes(e.target.value)}
            placeholder="Record experimental findings, parameter tweaks, mathematical questions, and notes..."
            style={{ fontFamily: 'var(--font-mono)', fontSize: 'var(--font-xs)', lineHeight: 1.6 }}
          />
        </div>
      )}
    </div>
  );
}
