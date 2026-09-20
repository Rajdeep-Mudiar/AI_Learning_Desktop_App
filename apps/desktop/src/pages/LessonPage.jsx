import React, { useState, useEffect } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import { ArrowLeft, ArrowRight, CheckCircle2, BookOpen, Clock, Target, Lightbulb, Sparkles, BookCheck } from 'lucide-react';
import { courseService } from '../services/courseService';
import VisualExplainerCard from '../components/lesson/VisualExplainerCard';
import CodeSnippetBox from '../components/lesson/CodeSnippetBox';
import QuizEngine from '../components/quiz/QuizEngine';
import LoadingSpinner from '../components/common/LoadingSpinner';
import Badge from '../components/common/Badge';
import MathFormula, { formatMathString } from '../components/common/MathFormula';

function FormattedSectionContent({ content }) {
  if (!content) return null;

  // Split content into blocks by double newlines or equation markers ($$...$$)
  const blocks = content.split(/(\$\$[\s\S]*?\$\$)/g);

  return (
    <div style={{ display: 'flex', flexDirection: 'column', gap: '14px' }}>
      {blocks.map((block, idx) => {
        const trimmed = block.trim();
        if (!trimmed) return null;

        // If block is an equation: $$ formula $$
        if (trimmed.startsWith('$$') && trimmed.endsWith('$$')) {
          const rawFormula = trimmed.slice(2, -2).trim();
          return (
            <MathFormula
              key={idx}
              formula={rawFormula}
              title="Mathematical Formula"
            />
          );
        }

        // Regular paragraph or bullet list
        const lines = trimmed.split('\n');
        return (
          <div key={idx} style={{ fontSize: '0.925rem', lineHeight: 1.7, color: 'var(--text-primary)' }}>
            {lines.map((line, lIdx) => {
              const lineTrimmed = line.trim();
              if (lineTrimmed.startsWith('* ') || lineTrimmed.startsWith('- ')) {
                return (
                  <div key={lIdx} style={{ display: 'flex', gap: '8px', paddingLeft: '8px', margin: '4px 0' }}>
                    <span style={{ color: 'var(--color-primary-400)' }}>•</span>
                    <span>{formatMathString(lineTrimmed.slice(2))}</span>
                  </div>
                );
              }
              if (lineTrimmed.startsWith('### ')) {
                return (
                  <h4 key={lIdx} style={{ fontSize: '1.05rem', margin: '14px 0 6px 0', color: 'var(--color-text-main)' }}>
                    {lineTrimmed.slice(4)}
                  </h4>
                );
              }
              if (lineTrimmed.startsWith('**') && lineTrimmed.endsWith('**')) {
                return (
                  <div key={lIdx} style={{ fontWeight: 700, margin: '6px 0', color: 'var(--color-text-main)' }}>
                    {formatMathString(lineTrimmed.slice(2, -2))}
                  </div>
                );
              }
              return (
                <p key={lIdx} style={{ margin: '0 0 8px 0' }}>
                  {formatMathString(line)}
                </p>
              );
            })}
          </div>
        );
      })}
    </div>
  );
}

export default function LessonPage() {
  const { lessonSlug } = useParams();
  const navigate = useNavigate();
  const [lesson, setLesson] = useState(null);
  const [loading, setLoading] = useState(true);
  const [completing, setCompleting] = useState(false);
  const [isCompleted, setIsCompleted] = useState(false);
  const [quizScore, setQuizScore] = useState(null);

  useEffect(() => {
    async function fetchLesson() {
      try {
        setLoading(true);
        const data = await courseService.getLessonBySlug(lessonSlug);
        setLesson(data);
        setIsCompleted(data.is_completed || false);
        setQuizScore(null);
      } catch (err) {
        console.error('Failed to load lesson:', err);
      } finally {
        setLoading(false);
      }
    }
    fetchLesson();
  }, [lessonSlug]);

  const handleMarkComplete = async () => {
    try {
      setCompleting(true);
      await courseService.completeLesson(lessonSlug);
      setIsCompleted(true);
    } catch (err) {
      console.error('Error marking lesson complete:', err);
    } finally {
      setCompleting(false);
    }
  };

  const handleQuizCompleted = (result) => {
    setQuizScore(result);
    if (result.passed) {
      setIsCompleted(true);
    }
  };

  if (loading) return <LoadingSpinner message="Loading interactive lesson laboratory..." />;
  if (!lesson) return <div className="card">Lesson not found.</div>;

  return (
    <div className="animate-fade-in" style={{ maxWidth: '920px', margin: '0 auto', paddingBottom: 60 }}>
      {/* Top Breadcrumb & Navigation */}
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: 20 }}>
        <button
          onClick={() => navigate(`/courses/${lesson.course_slug}`)}
          className="btn btn-ghost btn-sm"
          style={{ padding: '4px 8px' }}
        >
          <ArrowLeft size={16} /> Back to Course Syllabus
        </button>

        <div style={{ display: 'flex', alignItems: 'center', gap: 10 }}>
          <div style={{ display: 'flex', alignItems: 'center', gap: 6, fontSize: '0.8rem', color: 'var(--text-muted)' }}>
            <Clock size={14} />
            <span>~{lesson.estimated_minutes} mins</span>
          </div>

          <button
            onClick={handleMarkComplete}
            className={isCompleted ? 'btn btn-success btn-sm' : 'btn btn-outline btn-sm'}
            disabled={completing}
          >
            <CheckCircle2 size={16} />
            <span>{isCompleted ? 'Completed' : 'Mark Complete'}</span>
          </button>
        </div>
      </div>

      {/* Lesson Title Header */}
      <div style={{ marginBottom: 24 }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: 8, marginBottom: 8 }}>
          <Badge variant="blue">Interactive Lesson</Badge>
          <span style={{ fontSize: '0.8rem', color: 'var(--text-muted)' }}>Difficulty: {lesson.difficulty}</span>
        </div>
        <h1 style={{ fontSize: '2rem', lineHeight: 1.3, color: 'var(--text-primary)' }}>{lesson.title}</h1>
      </div>

      {/* Learning Objectives */}
      {lesson.learning_objectives?.length > 0 && (
        <div className="card" style={{ background: 'var(--bg-secondary)', marginBottom: 28, padding: 20 }}>
          <div style={{ display: 'flex', alignItems: 'center', gap: 8, marginBottom: 12 }}>
            <Target size={18} style={{ color: 'var(--accent-primary)' }} />
            <h3 style={{ fontSize: '0.95rem' }}>Learning Objectives</h3>
          </div>
          <ul style={{ paddingLeft: 20, display: 'flex', flexDirection: 'column', gap: 6, fontSize: '0.875rem', color: 'var(--text-secondary)' }}>
            {lesson.learning_objectives.map((obj, idx) => (
              <li key={idx}>{formatMathString(obj)}</li>
            ))}
          </ul>
        </div>
      )}

      {/* Theory Sections */}
      <div style={{ display: 'flex', flexDirection: 'column', gap: 24, marginBottom: 32 }}>
        {lesson.theory_sections?.map((sec, idx) => (
          <div key={idx} className="card" style={{ padding: 24 }}>
            <h2 style={{ fontSize: '1.25rem', marginBottom: 14 }}>{sec.title}</h2>
            <FormattedSectionContent content={sec.content_markdown} />

            {sec.key_takeaway && (
              <div style={{
                marginTop: 18,
                padding: '14px 18px',
                borderRadius: 'var(--radius-md)',
                background: 'rgba(99, 102, 241, 0.08)',
                borderLeft: '4px solid var(--accent-primary)',
                fontSize: '0.875rem',
                color: 'var(--text-secondary)',
                display: 'flex',
                alignItems: 'center',
                gap: 12,
                lineHeight: 1.5,
              }}>
                <Lightbulb size={18} style={{ color: 'var(--accent-primary)', flexShrink: 0 }} />
                <span><b>Core Principle:</b> {formatMathString(sec.key_takeaway)}</span>
              </div>
            )}
          </div>
        ))}
      </div>

      {/* Interactive Visual Explainer */}
      {lesson.visual_explainer && (
        <VisualExplainerCard visual={lesson.visual_explainer} />
      )}

      {/* Code Snippet Box */}
      {lesson.code_example && (
        <CodeSnippetBox snippet={lesson.code_example} />
      )}

      {/* Embedded Quiz Engine */}
      {lesson.quiz_id && (
        <QuizEngine
          quizId={lesson.quiz_id}
          onQuizCompleted={handleQuizCompleted}
        />
      )}

      {/* Bottom Lesson Navigation Bar */}
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginTop: 40, paddingTop: 24, borderTop: '1px solid var(--border-subtle)' }}>
        {lesson.prev_lesson_slug ? (
          <button
            onClick={() => navigate(`/lessons/${lesson.prev_lesson_slug}`)}
            className="btn btn-secondary"
          >
            <ArrowLeft size={16} /> Previous Lesson
          </button>
        ) : <div />}

        {lesson.next_lesson_slug ? (
          <button
            onClick={() => navigate(`/lessons/${lesson.next_lesson_slug}`)}
            className="btn btn-primary"
          >
            <span>Next Lesson</span>
            <ArrowRight size={16} />
          </button>
        ) : (
          <button
            onClick={() => navigate(`/courses/${lesson.course_slug}`)}
            className="btn btn-primary"
          >
            <Sparkles size={16} />
            <span>Finish Course Track</span>
          </button>
        )}
      </div>
    </div>
  );
}
