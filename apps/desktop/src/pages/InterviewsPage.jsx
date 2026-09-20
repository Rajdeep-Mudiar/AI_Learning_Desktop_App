import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { interviewService } from '../services/interviewService';
import { Video, Clock, HelpCircle, ArrowRight, Award } from 'lucide-react';

export default function InterviewsPage() {
  const [tracks, setTracks] = useState([]);
  const [loading, setLoading] = useState(true);
  const navigate = useNavigate();

  useEffect(() => {
    loadTracks();
  }, []);

  const loadTracks = async () => {
    try {
      setLoading(true);
      const data = await interviewService.getTracks();
      setTracks(data);
    } catch (err) {
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="container" style={{ paddingBottom: 'var(--space-2xl)' }}>
      {/* Header */}
      <div style={{ marginBottom: 'var(--space-xl)' }}>
        <h1 style={{ fontSize: 'var(--font-2xl)', fontWeight: 800, margin: '0 0 var(--space-xs) 0', color: 'var(--color-text-main)', display: 'flex', alignItems: 'center', gap: '8px' }}>
          <Video size={24} color="var(--color-primary-400)" /> AI Technical Interview & Viva Simulator
        </h1>
        <p style={{ margin: 0, color: 'var(--color-text-muted)', fontSize: 'var(--font-sm)' }}>
          Simulate real-world ML engineering and AI research interviews with dynamic AI evaluation rubrics and hire/no-hire recommendations.
        </p>
      </div>

      {loading ? (
        <div style={{ padding: 'var(--space-2xl)', textAlign: 'center', color: 'var(--color-text-muted)' }}>
          Loading interview tracks...
        </div>
      ) : (
        <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(360px, 1fr))', gap: 'var(--space-xl)' }}>
          {tracks.map((track) => (
            <div
              key={track.id}
              className="card"
              style={{
                padding: 0,
                overflow: 'hidden',
                display: 'flex',
                flexDirection: 'column',
                cursor: 'pointer',
                transition: 'transform 0.15s ease, box-shadow 0.15s ease',
              }}
              onClick={() => navigate(`/interviews/${track.id}`)}
            >
              <div style={{ background: track.banner_color, padding: 'var(--space-md) var(--space-lg)', color: '#ffffff' }}>
                <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '4px' }}>
                  <span style={{ fontSize: '10px', textTransform: 'uppercase', fontWeight: 700, letterSpacing: '0.05em' }}>
                    {track.difficulty} Track
                  </span>
                  <span style={{ fontSize: '11px', display: 'flex', alignItems: 'center', gap: '4px' }}>
                    <Clock size={12} /> {track.duration_minutes} mins
                  </span>
                </div>
                <h3 style={{ margin: 0, fontSize: 'var(--font-md)', fontWeight: 700 }}>
                  {track.title}
                </h3>
              </div>

              <div style={{ padding: 'var(--space-lg)', display: 'flex', flexDirection: 'column', gap: 'var(--space-md)', flex: 1 }}>
                <div style={{ fontSize: '11px', color: 'var(--color-primary-400)', fontWeight: 600 }}>
                  Target Role: {track.role_target}
                </div>

                <p style={{ margin: 0, fontSize: 'var(--font-xs)', color: 'var(--color-text-muted)', lineHeight: 1.5 }}>
                  {track.description}
                </p>

                <div style={{ marginTop: 'auto', paddingTop: 'var(--space-sm)', borderTop: '1px solid var(--color-border)', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                  <span style={{ fontSize: '11px', color: 'var(--color-text-muted)' }}>
                    {track.questions_count} Assessment Questions
                  </span>
                  <div style={{ display: 'flex', alignItems: 'center', gap: '4px', color: 'var(--color-primary-400)', fontSize: 'var(--font-xs)', fontWeight: 700 }}>
                    <span>Start Mock Interview</span>
                    <ArrowRight size={14} />
                  </div>
                </div>
              </div>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}
