import React, { useState, useEffect } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import { PlayCircle, CheckCircle, Clock, BookOpen, ChevronRight, ArrowLeft } from 'lucide-react';
import { courseService } from '../services/courseService';
import LoadingSpinner from '../components/common/LoadingSpinner';
import ProgressBar from '../components/common/ProgressBar';
import Badge from '../components/common/Badge';

export default function CourseDetail() {
  const { courseSlug } = useParams();
  const navigate = useNavigate();
  const [course, setCourse] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    async function loadDetail() {
      try {
        setLoading(true);
        const data = await courseService.getCourseBySlug(courseSlug);
        setCourse(data);
      } catch (err) {
        console.error('Failed to load course detail:', err);
      } finally {
        setLoading(false);
      }
    }
    loadDetail();
  }, [courseSlug]);

  if (loading) return <LoadingSpinner message="Loading course syllabus and module breakdown..." />;
  if (!course) return <div className="card">Course not found.</div>;

  return (
    <div className="animate-fade-in">
      {/* Back to courses */}
      <button
        onClick={() => navigate('/learn')}
        className="btn btn-ghost btn-sm"
        style={{ marginBottom: 16, padding: '4px 8px', color: 'var(--text-secondary)' }}
      >
        <ArrowLeft size={16} /> Back to Courses
      </button>

      {/* Hero Header */}
      <div className="card" style={{ padding: 32, marginBottom: 28, borderLeft: `6px solid ${course.color || 'var(--accent-primary)'}` }}>
        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', flexWrap: 'wrap', gap: 20 }}>
          <div style={{ flex: 1, minWidth: '300px' }}>
            <div style={{ display: 'flex', alignItems: 'center', gap: 10, marginBottom: 10 }}>
              <Badge variant="blue">{course.category}</Badge>
              <span style={{ fontSize: '0.8rem', color: 'var(--text-muted)' }}>• {course.level} Level</span>
              <span style={{ fontSize: '0.8rem', color: 'var(--text-muted)' }}>• ~{course.estimated_hours} Hours</span>
            </div>
            <h1 style={{ fontSize: '1.85rem', marginBottom: 12 }}>{course.title}</h1>
            <p style={{ fontSize: '0.95rem', color: 'var(--text-secondary)', lineHeight: 1.6, maxWidth: '720px' }}>
              {course.syllabus_overview || course.description}
            </p>
          </div>

          <div style={{ minWidth: '220px', display: 'flex', flexDirection: 'column', gap: 12 }}>
            {course.next_up_lesson_slug && (
              <button
                onClick={() => navigate(`/lessons/${course.next_up_lesson_slug}`)}
                className="btn btn-primary btn-lg"
                style={{ width: '100%' }}
              >
                <PlayCircle size={20} />
                <span>{course.completed_lessons > 0 ? 'Resume Course' : 'Start Course'}</span>
              </button>
            )}

            <div style={{ background: 'var(--bg-tertiary)', padding: 14, borderRadius: 'var(--radius-md)' }}>
              <div style={{ display: 'flex', justifyContent: 'space-between', fontSize: '0.8rem', marginBottom: 6 }}>
                <span style={{ color: 'var(--text-muted)' }}>Course Progress</span>
                <span style={{ fontWeight: 700, color: course.color }}>{course.progress_percentage}%</span>
              </div>
              <ProgressBar percentage={course.progress_percentage} color={course.color} height={6} />
              <div style={{ fontSize: '0.75rem', color: 'var(--text-muted)', marginTop: 6 }}>
                {course.completed_lessons} of {course.total_lessons} lessons completed
              </div>
            </div>
          </div>
        </div>
      </div>

      {/* Modules and Lessons Syllabus */}
      <h2 style={{ fontSize: '1.35rem', marginBottom: 16 }}>Syllabus Breakdown</h2>
      <div style={{ display: 'flex', flexDirection: 'column', gap: 20 }}>
        {course.modules?.map((mod, modIdx) => (
          <div key={mod.id} className="card" style={{ padding: 24 }}>
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: 14 }}>
              <div>
                <h3 style={{ fontSize: '1.1rem', marginBottom: 4 }}>{mod.title}</h3>
                {mod.description && (
                  <p style={{ fontSize: '0.825rem', color: 'var(--text-secondary)' }}>{mod.description}</p>
                )}
              </div>
              <span className="badge badge-gray">
                {mod.completed_count}/{mod.total_count} Done
              </span>
            </div>

            {/* Lesson Rows */}
            <div style={{ display: 'flex', flexDirection: 'column', gap: 8 }}>
              {mod.lessons?.map((lesson, lIdx) => (
                <div
                  key={lesson.slug}
                  onClick={() => navigate(`/lessons/${lesson.slug}`)}
                  className="card card-hoverable"
                  style={{
                    padding: '12px 16px',
                    background: 'var(--bg-secondary)',
                    display: 'flex',
                    justifyContent: 'space-between',
                    alignItems: 'center',
                    cursor: 'pointer'
                  }}
                >
                  <div style={{ display: 'flex', alignItems: 'center', gap: 12 }}>
                    <div style={{
                      width: 24,
                      height: 24,
                      borderRadius: '50%',
                      background: lesson.is_completed ? 'rgba(16, 185, 129, 0.15)' : 'var(--bg-tertiary)',
                      color: lesson.is_completed ? '#10b981' : 'var(--text-muted)',
                      display: 'flex',
                      alignItems: 'center',
                      justifyContent: 'center',
                      fontSize: '0.75rem',
                      fontWeight: 700
                    }}>
                      {lesson.is_completed ? <CheckCircle size={14} /> : lIdx + 1}
                    </div>
                    <div>
                      <h4 style={{ fontSize: '0.9rem', color: 'var(--text-primary)' }}>{lesson.title}</h4>
                      <span style={{ fontSize: '0.75rem', color: 'var(--text-muted)' }}>~{lesson.estimated_minutes} mins</span>
                    </div>
                  </div>

                  <ChevronRight size={16} style={{ color: 'var(--text-muted)' }} />
                </div>
              ))}
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}
