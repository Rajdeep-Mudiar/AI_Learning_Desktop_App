import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { researchService } from '../services/researchService';
import { FileText, ArrowRight, BookOpen, ExternalLink } from 'lucide-react';

export default function ResearchPage() {
  const [papers, setPapers] = useState([]);
  const [loading, setLoading] = useState(true);
  const [selectedCategory, setSelectedCategory] = useState('all');
  const navigate = useNavigate();

  useEffect(() => {
    loadPapers();
  }, []);

  const loadPapers = async () => {
    try {
      setLoading(true);
      const data = await researchService.getPapers();
      setPapers(data);
    } catch (err) {
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  const categories = ['all', 'Transformers', 'Vision', 'Fine-Tuning'];
  const filtered = selectedCategory === 'all' ? papers : papers.filter((p) => p.category === selectedCategory);

  return (
    <div className="container" style={{ paddingBottom: 'var(--space-2xl)' }}>
      {/* Header */}
      <div style={{ marginBottom: 'var(--space-xl)' }}>
        <h1 style={{ fontSize: 'var(--font-2xl)', fontWeight: 800, margin: '0 0 var(--space-xs) 0', color: 'var(--color-text-main)', display: 'flex', alignItems: 'center', gap: '8px' }}>
          <FileText size={24} color="var(--color-primary-400)" /> AI Research Mode & Paper Reproduction
        </h1>
        <p style={{ margin: 0, color: 'var(--color-text-muted)', fontSize: 'var(--font-sm)' }}>
          Read seminal AI papers, inspect mathematical equations with plain-English vector intuitions, and track experimental reproductions.
        </p>
      </div>

      {/* Category Tabs */}
      <div style={{ display: 'flex', gap: 'var(--space-xs)', marginBottom: 'var(--space-xl)' }}>
        {categories.map((cat) => (
          <button
            key={cat}
            onClick={() => setSelectedCategory(cat)}
            style={{
              padding: '6px 14px',
              borderRadius: 'var(--radius-full)',
              background: selectedCategory === cat ? 'rgba(99, 102, 241, 0.15)' : 'var(--color-surface)',
              border: selectedCategory === cat ? '1px solid var(--color-primary-400)' : '1px solid var(--color-border)',
              color: selectedCategory === cat ? 'var(--color-primary-400)' : 'var(--color-text-muted)',
              fontSize: 'var(--font-xs)',
              fontWeight: selectedCategory === cat ? 700 : 500,
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
          Loading research paper catalog...
        </div>
      ) : (
        <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(360px, 1fr))', gap: 'var(--space-xl)' }}>
          {filtered.map((paper) => (
            <div
              key={paper.id}
              className="card"
              style={{
                padding: 'var(--space-xl)',
                display: 'flex',
                flexDirection: 'column',
                gap: 'var(--space-md)',
                cursor: 'pointer',
                transition: 'transform 0.15s ease, box-shadow 0.15s ease',
              }}
              onClick={() => navigate(`/research/${paper.id}`)}
            >
              <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start' }}>
                <span style={{ fontSize: '10px', textTransform: 'uppercase', color: 'var(--color-primary-400)', fontWeight: 700, padding: '2px 8px', borderRadius: 'var(--radius-full)', background: 'rgba(99, 102, 241, 0.12)' }}>
                  {paper.category} • {paper.conference} ({paper.year})
                </span>
                <span style={{ fontSize: '10px', color: 'var(--color-text-muted)', fontFamily: 'var(--font-mono)' }}>
                  arXiv:{paper.arxiv_id}
                </span>
              </div>

              <h3 style={{ margin: 0, fontSize: 'var(--font-lg)', color: 'var(--color-text-main)', lineHeight: 1.3 }}>
                {paper.title}
              </h3>

              <div style={{ fontSize: '11px', color: 'var(--color-text-muted)' }}>
                By {paper.authors.slice(0, 3).join(', ')}{paper.authors.length > 3 ? ' et al.' : ''}
              </div>

              <p style={{ margin: 0, fontSize: 'var(--font-xs)', color: 'var(--color-text-muted)', lineHeight: 1.5, display: '-webkit-box', WebkitLineClamp: 3, WebkitBoxOrient: 'vertical', overflow: 'hidden' }}>
                {paper.abstract}
              </p>

              <div style={{ marginTop: 'auto', paddingTop: 'var(--space-sm)', borderTop: '1px solid var(--color-border)', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                <span style={{ fontSize: '11px', color: 'var(--color-text-muted)' }}>
                  {paper.reproduction_steps_count} Reproduction Checkpoints
                </span>
                <div style={{ display: 'flex', alignItems: 'center', gap: '4px', color: 'var(--color-primary-400)', fontSize: 'var(--font-xs)', fontWeight: 700 }}>
                  <span>Explore Paper & Equations</span>
                  <ArrowRight size={14} />
                </div>
              </div>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}
