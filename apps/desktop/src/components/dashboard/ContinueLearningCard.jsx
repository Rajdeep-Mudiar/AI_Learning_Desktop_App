import React from 'react';
import { useNavigate } from 'react-router-dom';
import { PlayCircle, Clock, BookOpen } from 'lucide-react';
import ProgressBar from '../common/ProgressBar';

export default function ContinueLearningCard({ data }) {
  const navigate = useNavigate();

  if (!data) {
    return (
      <div className="card" style={{ padding: 24, textAlign: 'center' }}>
        <h3 style={{ fontSize: '1.1rem', marginBottom: 8 }}>Ready to start learning?</h3>
        <p style={{ color: 'var(--text-secondary)', fontSize: '0.9rem', marginBottom: 16 }}>
          Explore our curriculum from Python fundamentals to Transformers and Deep Learning.
        </p>
        <button onClick={() => navigate('/learn')} className="btn btn-primary">
          <BookOpen size={16} /> Browse Courses
        </button>
      </div>
    );
  }

  return (
    <div
      className="card card-hoverable"
      style={{
        background: 'linear-gradient(135deg, rgba(99, 102, 241, 0.08) 0%, var(--bg-card) 100%)',
        borderLeft: `4px solid ${data.course_color || 'var(--accent-primary)'}`,
      }}
    >
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', marginBottom: 16 }}>
        <div>
          <div style={{ display: 'flex', alignItems: 'center', gap: 8, marginBottom: 4 }}>
            <span style={{ fontSize: '0.75rem', textTransform: 'uppercase', fontWeight: 700, color: data.course_color }}>
              {data.course_title}
            </span>
            <span style={{ fontSize: '0.75rem', color: 'var(--text-muted)' }}>• {data.module_title}</span>
          </div>
          <h2 style={{ fontSize: '1.35rem', color: 'var(--text-primary)' }}>{data.lesson_title}</h2>
        </div>

        <button
          onClick={() => navigate(`/lessons/${data.lesson_slug}`)}
          className="btn btn-primary"
          style={{ padding: '10px 20px', display: 'flex', alignItems: 'center', gap: 8 }}
        >
          <PlayCircle size={18} />
          <span>Resume Lesson</span>
        </button>
      </div>

      <div style={{ display: 'flex', alignItems: 'center', gap: 20, marginBottom: 16 }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: 6, fontSize: '0.825rem', color: 'var(--text-secondary)' }}>
          <Clock size={15} />
          <span>~{data.estimated_minutes} mins remaining</span>
        </div>
      </div>

      <ProgressBar
        percentage={data.course_percentage}
        color={data.course_color}
        showLabel={true}
        labelText="Course Completion"
      />
    </div>
  );
}
