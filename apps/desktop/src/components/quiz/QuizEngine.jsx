import React, { useState, useEffect } from 'react';
import { HelpCircle, CheckCircle2, XCircle, Award, RotateCcw, ArrowRight, Lightbulb } from 'lucide-react';
import { quizService } from '../../services/quizService';
import LoadingSpinner from '../common/LoadingSpinner';

export default function QuizEngine({ quizId, onQuizCompleted }) {
  const [quiz, setQuiz] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [selectedAnswers, setSelectedAnswers] = useState({});
  const [submitting, setSubmitting] = useState(false);
  const [gradedResult, setGradedResult] = useState(null);

  useEffect(() => {
    async function loadQuiz() {
      if (!quizId) return;
      try {
        setLoading(true);
        const data = await quizService.getQuiz(quizId);
        setQuiz(data);
        setSelectedAnswers({});
        setGradedResult(null);
      } catch (err) {
        setError(err.message);
      } finally {
        setLoading(false);
      }
    }
    loadQuiz();
  }, [quizId]);

  const handleSelectOption = (questionId, optionIdx) => {
    if (gradedResult) return; // Prevent change after grading
    setSelectedAnswers((prev) => ({
      ...prev,
      [questionId]: optionIdx,
    }));
  };

  const handleFillBlankChange = (questionId, val) => {
    if (gradedResult) return;
    setSelectedAnswers((prev) => ({
      ...prev,
      [questionId]: val,
    }));
  };

  const handleSubmit = async () => {
    if (!quiz) return;
    try {
      setSubmitting(true);
      const formattedAnswers = Object.entries(selectedAnswers).map(([qId, ans]) => ({
        question_id: qId,
        selected_answer: ans,
      }));

      const res = await quizService.submitQuiz(quizId, formattedAnswers);
      setGradedResult(res);
      if (onQuizCompleted) {
        onQuizCompleted(res);
      }
    } catch (err) {
      setError(err.message);
    } finally {
      setSubmitting(false);
    }
  };

  const handleRetake = () => {
    setSelectedAnswers({});
    setGradedResult(null);
  };

  if (loading) return <LoadingSpinner message="Loading interactive quiz..." />;
  if (error) return <div className="card" style={{ color: 'var(--accent-danger)' }}>Error loading quiz: {error}</div>;
  if (!quiz) return null;

  return (
    <div className="card" style={{ marginTop: 32, borderTop: '4px solid var(--accent-primary)' }}>
      {/* Quiz Header */}
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: 20 }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: 10 }}>
          <div style={{
            width: 32,
            height: 32,
            borderRadius: 8,
            background: 'rgba(99, 102, 241, 0.15)',
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center',
            color: 'var(--accent-primary)'
          }}>
            <HelpCircle size={18} />
          </div>
          <div>
            <h3 style={{ fontSize: '1.15rem' }}>{quiz.title}</h3>
            <p style={{ fontSize: '0.8rem', color: 'var(--text-muted)' }}>
              Pass threshold: {quiz.passing_score}% • {quiz.questions.length} questions
            </p>
          </div>
        </div>

        {gradedResult && (
          <div style={{
            display: 'flex',
            alignItems: 'center',
            gap: 8,
            padding: '6px 14px',
            borderRadius: 999,
            background: gradedResult.passed ? 'rgba(16, 185, 129, 0.15)' : 'rgba(239, 68, 68, 0.15)',
            color: gradedResult.passed ? '#34d399' : '#f87171',
            fontWeight: 700,
            fontSize: '0.85rem',
            border: `1px solid ${gradedResult.passed ? 'rgba(16, 185, 129, 0.3)' : 'rgba(239, 68, 68, 0.3)'}`
          }}>
            <Award size={16} />
            <span>Score: {gradedResult.percentage}% ({gradedResult.passed ? 'PASSED' : 'RETRY'})</span>
          </div>
        )}
      </div>

      {/* Questions list */}
      <div style={{ display: 'flex', flexDirection: 'column', gap: 24 }}>
        {quiz.questions.map((q, qIndex) => {
          const gradedQ = gradedResult?.results?.find((r) => r.question_id === q.id);
          const isAnswered = selectedAnswers[q.id] !== undefined;

          return (
            <div
              key={q.id}
              style={{
                padding: '20px',
                borderRadius: 'var(--radius-md)',
                background: 'var(--bg-secondary)',
                border: gradedQ
                  ? gradedQ.is_correct
                    ? '1.5px solid rgba(16, 185, 129, 0.4)'
                    : '1.5px solid rgba(239, 68, 68, 0.4)'
                  : '1px solid var(--border-subtle)',
              }}
            >
              <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', marginBottom: 12 }}>
                <h4 style={{ fontSize: '0.95rem', fontWeight: 600, lineHeight: 1.5 }}>
                  <span style={{ color: 'var(--accent-primary)', marginRight: 8 }}>{qIndex + 1}.</span>
                  {q.question}
                </h4>
                <span className="badge badge-gray">{q.points} pts</span>
              </div>

              {/* Options */}
              {q.options && (
                <div style={{ display: 'flex', flexDirection: 'column', gap: 8, marginTop: 12 }}>
                  {q.options.map((opt, optIdx) => {
                    const isSelected = selectedAnswers[q.id] === optIdx;
                    let optionClass = 'quiz-option-card';

                    if (gradedQ) {
                      if (gradedQ.correct_answer === optIdx) {
                        optionClass += ' correct';
                      } else if (isSelected && !gradedQ.is_correct) {
                        optionClass += ' incorrect';
                      }
                    } else if (isSelected) {
                      optionClass += ' selected';
                    }

                    return (
                      <div
                        key={optIdx}
                        className={optionClass}
                        onClick={() => handleSelectOption(q.id, optIdx)}
                        style={{ margin: 0 }}
                      >
                        <div style={{
                          width: 20,
                          height: 20,
                          borderRadius: '50%',
                          border: '2px solid var(--border-subtle)',
                          display: 'flex',
                          alignItems: 'center',
                          justifyContent: 'center',
                          fontSize: '0.75rem',
                          fontWeight: 700,
                          flexShrink: 0
                        }}>
                          {String.fromCharCode(65 + optIdx)}
                        </div>
                        <span style={{ fontSize: '0.875rem' }}>{opt}</span>
                      </div>
                    );
                  })}
                </div>
              )}

              {/* Fill-in-the-blank input */}
              {q.type === 'fill_blank' && (
                <div style={{ marginTop: 12 }}>
                  <input
                    type="text"
                    className="form-input"
                    placeholder="Type your answer..."
                    value={selectedAnswers[q.id] || ''}
                    onChange={(e) => handleFillBlankChange(q.id, e.target.value)}
                    disabled={!!gradedResult}
                    style={{ width: '100%', maxWidth: '320px' }}
                  />
                </div>
              )}

              {/* Graded explanation and breakdown */}
              {gradedQ && (
                <div
                  style={{
                    marginTop: 16,
                    padding: '14px 16px',
                    borderRadius: 'var(--radius-md)',
                    background: gradedQ.is_correct ? 'rgba(16, 185, 129, 0.08)' : 'rgba(239, 68, 68, 0.08)',
                    borderLeft: `4px solid ${gradedQ.is_correct ? '#10b981' : '#ef4444'}`,
                    fontSize: '0.85rem',
                    lineHeight: 1.5,
                  }}
                >
                  <div style={{ display: 'flex', alignItems: 'center', gap: 6, fontWeight: 700, marginBottom: 6, color: gradedQ.is_correct ? '#34d399' : '#f87171' }}>
                    {gradedQ.is_correct ? <CheckCircle2 size={16} /> : <XCircle size={16} />}
                    <span>{gradedQ.is_correct ? 'Correct Concept Mastery' : 'Conceptual Misconception'}</span>
                  </div>
                  <p style={{ color: 'var(--text-primary)', marginBottom: 6 }}>{gradedQ.explanation}</p>
                  {gradedQ.remedial_tip && (
                    <div style={{ display: 'flex', alignItems: 'center', gap: 6, color: '#fbbf24', fontSize: '0.8rem', marginTop: 6 }}>
                      <Lightbulb size={14} />
                      <span><b>Study Tip:</b> {gradedQ.remedial_tip}</span>
                    </div>
                  )}
                </div>
              )}
            </div>
          );
        })}
      </div>

      {/* Submission & Action Bar */}
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginTop: 24, paddingTop: 16, borderTop: '1px solid var(--border-subtle)' }}>
        <span style={{ fontSize: '0.825rem', color: 'var(--text-muted)' }}>
          {Object.keys(selectedAnswers).length} of {quiz.questions.length} questions answered
        </span>

        {gradedResult ? (
          <button onClick={handleRetake} className="btn btn-secondary">
            <RotateCcw size={16} /> Retake Quiz
          </button>
        ) : (
          <button
            onClick={handleSubmit}
            className="btn btn-primary"
            disabled={submitting || Object.keys(selectedAnswers).length === 0}
            style={{ opacity: Object.keys(selectedAnswers).length === 0 ? 0.6 : 1 }}
          >
            {submitting ? 'Evaluating...' : 'Submit & Grade Answers'}
          </button>
        )}
      </div>
    </div>
  );
}
