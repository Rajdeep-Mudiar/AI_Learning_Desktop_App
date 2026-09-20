import React from 'react';
import { useNavigate } from 'react-router-dom';
import { Clock, BookOpen, Layers, CheckCircle } from 'lucide-react';
import ProgressBar from '../common/ProgressBar';
import Badge from '../common/Badge';

export default function CourseCard({ course }) {
  const navigate = useNavigate();

  const getLevelVariant = (level) => {
    switch (level) {
      case 'Beginner': return 'green';
      case 'Intermediate': return 'purple';
      case 'Advanced': return 'pink';
      default: return 'blue';
    }
  };

  return (
    <div
      onClick={() => navigate(`/courses/${course.slug}`)}
      className="card card-hoverable"
      style={{
        display: 'flex',
        flexDirection: 'column',
        justifyContent: 'space-between',
        cursor: 'pointer',
        borderTop: `4px solid ${course.color || 'var(--accent-primary)'}`,
        height: '100%',
        minHeight: '260px'
      }}
    >
      <div>
        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: 12 }}>
          <Badge variant={getLevelVariant(course.level)}>{course.level}</Badge>
          <div style={{ display: 'flex', alignItems: 'center', gap: 6, fontSize: '0.75rem', color: 'var(--text-muted)' }}>
            <Clock size={13} />
            <span>{course.estimated_hours}h</span>
          </div>
        </div>

        <h3 style={{ fontSize: '1.15rem', marginBottom: 8, color: 'var(--text-primary)' }}>{course.title}</h3>
        <p style={{
          fontSize: '0.825rem',
          color: 'var(--text-secondary)',
          lineHeight: 1.5,
          marginBottom: 16,
          display: '-webkit-box',
          WebkitLineClamp: 3,
          WebkitBoxOrient: 'vertical',
          overflow: 'hidden'
        }}>
          {course.description}
        </p>

        {/* Skills preview */}
        <div style={{ display: 'flex', flexWrap: 'wrap', gap: 6, marginBottom: 16 }}>
          {course.skills_taught?.slice(0, 3).map((skill, idx) => (
            <span
              key={idx}
              style={{
                fontSize: '0.7rem',
                padding: '2px 8px',
                borderRadius: 4,
                background: 'var(--bg-tertiary)',
                color: 'var(--text-muted)',
                border: '1px solid var(--border-subtle)'
              }}
            >
              {skill}
            </span>
          ))}
          {course.skills_taught?.length > 3 && (
            <span style={{ fontSize: '0.7rem', color: 'var(--text-muted)', alignSelf: 'center' }}>
              +{course.skills_taught.length - 3} more
            </span>
          )}
        </div>
      </div>

      <div>
        <div style={{ display: 'flex', justifyContent: 'space-between', fontSize: '0.75rem', color: 'var(--text-muted)', marginBottom: 6 }}>
          <span>{course.completed_lessons} of {course.total_lessons} lessons</span>
          <span style={{ fontWeight: 600, color: course.color }}>{course.progress_percentage}%</span>
        </div>
        <ProgressBar percentage={course.progress_percentage} color={course.color} height={6} />
      </div>
    </div>
  );
}
