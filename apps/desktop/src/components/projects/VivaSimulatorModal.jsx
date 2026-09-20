import React, { useState, useEffect } from 'react';
import { projectService } from '../../services/projectService';
import { Award, CheckCircle, AlertCircle, Sparkles } from 'lucide-react';

export default function VivaSimulatorModal({ projectId, onClose }) {
  const [step, setStep] = useState(1);
  const [questionData, setQuestionData] = useState(null);
  const [answer, setAnswer] = useState('');
  const [loading, setLoading] = useState(true);
  const [evaluating, setEvaluating] = useState(false);
  const [evaluation, setEvaluation] = useState(null);

  useEffect(() => {
    loadQuestion(step);
  }, [step, projectId]);

  const loadQuestion = async (qStep) => {
    try {
      setLoading(true);
      setEvaluation(null);
      setAnswer('');
      const q = await projectService.getVivaQuestion(projectId, qStep);
      setQuestionData(q);
    } catch (err) {
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!answer.trim() || evaluating) return;
    try {
      setEvaluating(true);
      const res = await projectService.submitVivaAnswer(projectId, {
        project_id: projectId,
        question_id: questionData.question_id,
        question: questionData.question,
        answer: answer.trim(),
      });
      setEvaluation(res);
    } catch (err) {
      console.error(err);
    } finally {
      setEvaluating(false);
    }
  };

  return (
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
      onClick={onClose}
    >
      <div
        style={{
          background: 'var(--color-surface)',
          border: '1px solid var(--color-border)',
          borderRadius: 'var(--radius-lg)',
          width: '100%',
          maxWidth: '700px',
          padding: 'var(--space-xl)',
          boxShadow: 'var(--shadow-xl)',
          display: 'flex',
          flexDirection: 'column',
          gap: 'var(--space-lg)',
          maxHeight: '90vh',
          overflowY: 'auto',
        }}
        onClick={(e) => e.stopPropagation()}
      >
        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', borderBottom: '1px solid var(--color-border)', paddingBottom: 'var(--space-sm)' }}>
          <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
            <Award size={20} color="var(--color-primary-400)" />
            <h3 style={{ margin: 0, fontSize: 'var(--font-lg)', color: 'var(--color-text-main)' }}>
              AI Project Viva & Oral Defense Simulator
            </h3>
          </div>
          <button
            onClick={onClose}
            className="btn btn-secondary"
            style={{ padding: '4px 10px', fontSize: 'var(--font-xs)' }}
          >
            ✕
          </button>
        </div>

        {loading ? (
          <div style={{ padding: 'var(--space-xl)', textAlign: 'center', color: 'var(--color-text-muted)' }}>
            Connecting to AI Viva Examiner...
          </div>
        ) : questionData ? (
          <div style={{ display: 'flex', flexDirection: 'column', gap: 'var(--space-md)' }}>
            {/* Question Card */}
            <div className="card" style={{ padding: 'var(--space-md)', background: 'var(--color-surface-elevated)', borderLeft: '4px solid var(--color-primary-400)' }}>
              <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '4px' }}>
                <span style={{ fontSize: '10px', textTransform: 'uppercase', color: 'var(--color-primary-400)', fontWeight: 700 }}>
                  Question {step} of 3 • Focus: {questionData.focus_area}
                </span>
              </div>
              <p style={{ margin: 0, fontSize: 'var(--font-sm)', fontWeight: 600, color: 'var(--color-text-main)', lineHeight: 1.5 }}>
                {questionData.question}
              </p>
              <div style={{ marginTop: '8px', fontSize: '11px', color: 'var(--color-text-muted)', background: 'rgba(0,0,0,0.2)', padding: '6px 10px', borderRadius: 'var(--radius-sm)' }}>
                <strong>Examiner Rubric:</strong> {questionData.rubric}
              </div>
            </div>

            {/* Response Form */}
            {!evaluation ? (
              <form onSubmit={handleSubmit} style={{ display: 'flex', flexDirection: 'column', gap: 'var(--space-md)' }}>
                <div>
                  <label style={{ display: 'block', fontSize: 'var(--font-xs)', fontWeight: 600, marginBottom: '4px' }}>
                    Your Oral Defense Response
                  </label>
                  <textarea
                    className="input"
                    rows={5}
                    placeholder="Articulate your technical rationale, mathematical justification, and system trade-offs..."
                    value={answer}
                    onChange={(e) => setAnswer(e.target.value)}
                    required
                    style={{ fontSize: 'var(--font-sm)', lineHeight: 1.5 }}
                  />
                </div>
                <div style={{ display: 'flex', justifyContent: 'flex-end', gap: 'var(--space-sm)' }}>
                  <button type="button" onClick={onClose} className="btn btn-secondary">
                    Cancel
                  </button>
                  <button type="submit" disabled={evaluating || !answer.trim()} className="btn btn-primary" style={{ display: 'flex', alignItems: 'center', gap: '6px' }}>
                    <Sparkles size={14} />
                    <span>{evaluating ? 'Examiner Evaluating...' : 'Submit Defense Answer'}</span>
                  </button>
                </div>
              </form>
            ) : (
              /* Graded Evaluation Results */
              <div className="card" style={{ padding: 'var(--space-lg)', display: 'flex', flexDirection: 'column', gap: 'var(--space-md)', background: 'var(--color-surface-elevated)' }}>
                <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                  <div>
                    <h4 style={{ margin: 0, fontSize: 'var(--font-md)', color: 'var(--color-text-main)' }}>
                      Examiner Score: <strong>{evaluation.score} / 100</strong>
                    </h4>
                    <span style={{ fontSize: 'var(--font-xs)', color: 'var(--color-text-muted)' }}>
                      Assessment Grade: <strong style={{ color: evaluation.score >= 85 ? '#10b981' : '#f59e0b' }}>{evaluation.grade}</strong>
                    </span>
                  </div>
                  <div
                    style={{
                      padding: '6px 14px',
                      borderRadius: 'var(--radius-full)',
                      background: evaluation.score >= 85 ? 'rgba(16, 185, 129, 0.15)' : 'rgba(245, 158, 11, 0.15)',
                      color: evaluation.score >= 85 ? '#10b981' : '#f59e0b',
                      fontSize: 'var(--font-xs)',
                      fontWeight: 700,
                    }}
                  >
                    {evaluation.grade}
                  </div>
                </div>

                <p style={{ margin: 0, fontSize: 'var(--font-sm)', color: 'var(--color-text-main)', fontStyle: 'italic', background: 'var(--color-surface)', padding: '10px 12px', borderRadius: 'var(--radius-sm)' }}>
                  "{evaluation.examiner_feedback}"
                </p>

                {/* Strengths */}
                <div>
                  <h5 style={{ margin: '0 0 4px 0', fontSize: 'var(--font-xs)', color: '#10b981', display: 'flex', alignItems: 'center', gap: '4px' }}>
                    <CheckCircle size={13} /> Key Strengths
                  </h5>
                  <ul style={{ margin: 0, paddingLeft: '18px', fontSize: 'var(--font-xs)', color: 'var(--color-text-muted)' }}>
                    {evaluation.strengths.map((s, idx) => (
                      <li key={idx}>{s}</li>
                    ))}
                  </ul>
                </div>

                {/* Improvements */}
                <div>
                  <h5 style={{ margin: '0 0 4px 0', fontSize: 'var(--font-xs)', color: '#f59e0b', display: 'flex', alignItems: 'center', gap: '4px' }}>
                    <AlertCircle size={13} /> Areas for Further Deepening
                  </h5>
                  <ul style={{ margin: 0, paddingLeft: '18px', fontSize: 'var(--font-xs)', color: 'var(--color-text-muted)' }}>
                    {evaluation.areas_for_improvement.map((imp, idx) => (
                      <li key={idx}>{imp}</li>
                    ))}
                  </ul>
                </div>

                <div style={{ display: 'flex', justifyContent: 'flex-end', gap: 'var(--space-sm)', marginTop: 'var(--space-sm)' }}>
                  {step < 3 ? (
                    <button onClick={() => setStep(step + 1)} className="btn btn-primary">
                      Next Question ➜
                    </button>
                  ) : (
                    <button onClick={onClose} className="btn btn-primary">
                      Finish Viva Defense ✓
                    </button>
                  )}
                </div>
              </div>
            )}
          </div>
        ) : null}
      </div>
    </div>
  );
}
