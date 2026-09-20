import React, { useState, useEffect } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import { interviewService } from '../services/interviewService';
import { ArrowLeft, Clock, Award, CheckCircle2, AlertCircle, Sparkles, Send } from 'lucide-react';

export default function InterviewSessionPage() {
  const { trackId } = useParams();
  const navigate = useNavigate();

  const [track, setTrack] = useState(null);
  const [loading, setLoading] = useState(true);
  const [currentIdx, setCurrentIdx] = useState(0);
  const [answers, setAnswers] = useState({});
  const [currentAnswer, setCurrentAnswer] = useState('');
  const [evaluating, setEvaluating] = useState(false);
  const [report, setReport] = useState(null);

  useEffect(() => {
    loadTrack();
  }, [trackId]);

  const loadTrack = async () => {
    try {
      setLoading(true);
      const data = await interviewService.getTrack(trackId);
      setTrack(data);
    } catch (err) {
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  const handleSaveAndNext = () => {
    if (!track) return;
    const q = track.questions[currentIdx];
    const updated = { ...answers, [q.id]: currentAnswer };
    setAnswers(updated);

    if (currentIdx < track.questions.length - 1) {
      setCurrentIdx(currentIdx + 1);
      setCurrentAnswer(answers[track.questions[currentIdx + 1]?.id] || '');
    } else {
      // Final submission
      handleSubmitSession(updated);
    }
  };

  const handleSubmitSession = async (allAnswers) => {
    try {
      setEvaluating(true);
      const formatted = Object.entries(allAnswers).map(([qid, ans]) => ({
        question_id: qid,
        user_answer: ans,
      }));
      const res = await interviewService.evaluateInterview(trackId, formatted);
      setReport(res);
    } catch (err) {
      console.error(err);
    } finally {
      setEvaluating(false);
    }
  };

  if (loading || !track) {
    return (
      <div className="container" style={{ padding: 'var(--space-2xl)', textAlign: 'center', color: 'var(--color-text-muted)' }}>
        Loading interview session...
      </div>
    );
  }

  const currentQ = track.questions[currentIdx];

  return (
    <div className="container" style={{ paddingBottom: 'var(--space-2xl)', maxWidth: '800px' }}>
      {/* Back button */}
      <button
        onClick={() => navigate('/interviews')}
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
        <span>Exit Interview Session</span>
      </button>

      {!report ? (
        <div className="card" style={{ padding: 'var(--space-xl)', display: 'flex', flexDirection: 'column', gap: 'var(--space-lg)' }}>
          {/* Header */}
          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', borderBottom: '1px solid var(--color-border)', paddingBottom: 'var(--space-sm)' }}>
            <div>
              <span style={{ fontSize: '10px', textTransform: 'uppercase', color: 'var(--color-primary-400)', fontWeight: 700 }}>
                Question {currentIdx + 1} of {track.questions.length} • {currentQ.category}
              </span>
              <h2 style={{ margin: '4px 0', fontSize: 'var(--font-lg)', color: 'var(--color-text-main)' }}>
                {track.title}
              </h2>
            </div>
            <div style={{ display: 'flex', alignItems: 'center', gap: '4px', fontSize: 'var(--font-xs)', color: 'var(--color-text-muted)', background: 'var(--color-surface-elevated)', padding: '4px 10px', borderRadius: 'var(--radius-full)' }}>
              <Clock size={13} />
              <span>{track.duration_minutes}m target</span>
            </div>
          </div>

          {/* Question Text */}
          <div style={{ padding: 'var(--space-md)', background: 'var(--color-surface-elevated)', borderRadius: 'var(--radius-md)', borderLeft: '4px solid var(--color-primary-400)' }}>
            <p style={{ margin: 0, fontSize: 'var(--font-sm)', fontWeight: 600, color: 'var(--color-text-main)', lineHeight: 1.5 }}>
              {currentQ.question}
            </p>
          </div>

          {/* Answer Text Area */}
          <div>
            <label style={{ display: 'block', fontSize: 'var(--font-xs)', fontWeight: 600, marginBottom: '6px', color: 'var(--color-text-muted)' }}>
              Your Technical Response
            </label>
            <textarea
              className="input"
              rows={8}
              value={currentAnswer}
              onChange={(e) => setCurrentAnswer(e.target.value)}
              placeholder="Explain the mathematical foundations, asymptotic complexity, trade-offs, and practical edge cases..."
              style={{ fontSize: 'var(--font-sm)', lineHeight: 1.6 }}
            />
          </div>

          {/* Actions */}
          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
            {currentIdx > 0 && (
              <button
                onClick={() => {
                  setCurrentIdx(currentIdx - 1);
                  setCurrentAnswer(answers[track.questions[currentIdx - 1]?.id] || '');
                }}
                className="btn btn-secondary"
              >
                Previous Question
              </button>
            )}
            <button
              onClick={handleSaveAndNext}
              disabled={evaluating || !currentAnswer.trim()}
              className="btn btn-primary"
              style={{ marginLeft: 'auto', display: 'flex', alignItems: 'center', gap: '6px' }}
            >
              {evaluating ? (
                <span>AI Panel Evaluating...</span>
              ) : currentIdx < track.questions.length - 1 ? (
                <span>Save & Next Question ➜</span>
              ) : (
                <span>Complete Interview & Submit ✓</span>
              )}
            </button>
          </div>
        </div>
      ) : (
        /* Evaluation Report */
        <div className="card" style={{ padding: 'var(--space-xl)', display: 'flex', flexDirection: 'column', gap: 'var(--space-xl)' }}>
          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', borderBottom: '1px solid var(--color-border)', paddingBottom: 'var(--space-md)' }}>
            <div>
              <span style={{ fontSize: '10px', textTransform: 'uppercase', color: 'var(--color-primary-400)', fontWeight: 700 }}>
                Official Candidate Assessment Report
              </span>
              <h1 style={{ margin: '4px 0', fontSize: 'var(--font-xl)', color: 'var(--color-text-main)' }}>
                {track.title}
              </h1>
            </div>

            <div
              style={{
                padding: '8px 18px',
                borderRadius: 'var(--radius-full)',
                background: report.recommendation.includes('Hire') ? 'rgba(16, 185, 129, 0.15)' : 'rgba(239, 68, 68, 0.15)',
                color: report.recommendation.includes('Hire') ? '#10b981' : '#ef4444',
                fontSize: 'var(--font-sm)',
                fontWeight: 800,
              }}
            >
              {report.recommendation.toUpperCase()}
            </div>
          </div>

          {/* Scores Overview */}
          <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(140px, 1fr))', gap: 'var(--space-sm)' }}>
            <div style={{ background: 'var(--color-surface-elevated)', padding: 'var(--space-md)', borderRadius: 'var(--radius-md)', textAlign: 'center' }}>
              <div style={{ fontSize: '10px', color: 'var(--color-text-muted)' }}>Overall Score</div>
              <div style={{ fontSize: 'var(--font-2xl)', fontWeight: 800, color: '#f59e0b' }}>
                {report.overall_score}%
              </div>
            </div>
            <div style={{ background: 'var(--color-surface-elevated)', padding: 'var(--space-md)', borderRadius: 'var(--radius-md)', textAlign: 'center' }}>
              <div style={{ fontSize: '10px', color: 'var(--color-text-muted)' }}>Technical Depth</div>
              <div style={{ fontSize: 'var(--font-2xl)', fontWeight: 800, color: '#10b981' }}>
                {report.technical_depth_score}%
              </div>
            </div>
            <div style={{ background: 'var(--color-surface-elevated)', padding: 'var(--space-md)', borderRadius: 'var(--radius-md)', textAlign: 'center' }}>
              <div style={{ fontSize: '10px', color: 'var(--color-text-muted)' }}>Communication</div>
              <div style={{ fontSize: 'var(--font-2xl)', fontWeight: 800, color: 'var(--color-primary-400)' }}>
                {report.communication_score}%
              </div>
            </div>
          </div>

          {/* Detailed Question Feedback */}
          <div>
            <h3 style={{ fontSize: 'var(--font-sm)', color: 'var(--color-text-main)', marginBottom: 'var(--space-sm)' }}>
              Question Breakdown & Rubric Performance
            </h3>
            <div style={{ display: 'flex', flexDirection: 'column', gap: 'var(--space-md)' }}>
              {report.detailed_feedback.map((fb, idx) => (
                <div key={idx} style={{ background: 'var(--color-surface-elevated)', padding: 'var(--space-md)', borderRadius: 'var(--radius-md)' }}>
                  <div style={{ display: 'flex', justifyContent: 'space-between', fontSize: 'var(--font-xs)', fontWeight: 600, marginBottom: '4px' }}>
                    <span>Question {idx + 1}</span>
                    <span style={{ color: fb.score >= 75 ? '#10b981' : '#f59e0b' }}>Score: {fb.score}/100</span>
                  </div>
                  <p style={{ margin: 0, fontSize: 'var(--font-xs)', color: 'var(--color-text-muted)' }}>
                    {fb.feedback}
                  </p>
                </div>
              ))}
            </div>
          </div>

          <div style={{ display: 'flex', justifyContent: 'flex-end', gap: 'var(--space-sm)' }}>
            <button onClick={() => navigate('/interviews')} className="btn btn-primary">
              Return to Interview Tracks
            </button>
          </div>
        </div>
      )}
    </div>
  );
}
