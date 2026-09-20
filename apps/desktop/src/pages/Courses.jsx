import React, { useState, useEffect } from 'react';
import { Search, Filter, BookOpen, Sparkles } from 'lucide-react';
import { courseService } from '../services/courseService';
import { useDomain } from '../contexts/DomainContext';
import CourseCard from '../components/course/CourseCard';
import LoadingSpinner from '../components/common/LoadingSpinner';

export default function Courses() {
  const { currentDomain, domainInfo, allDomains, selectDomain } = useDomain();
  const [courses, setCourses] = useState([]);
  const [loading, setLoading] = useState(true);
  const [searchQuery, setSearchQuery] = useState('');
  const [selectedLevel, setSelectedLevel] = useState('All');
  const [showAllTracks, setShowAllTracks] = useState(false);

  useEffect(() => {
    async function loadCourses() {
      try {
        setLoading(true);
        const data = await courseService.getAllCourses();
        setCourses(data);
      } catch (err) {
        console.error('Failed to load courses:', err);
      } finally {
        setLoading(false);
      }
    }
    loadCourses();
  }, []);

  // Compute course counts per domain
  const getCourseCountForDomain = (domainId) => {
    return courses.filter((c) => (c.domain || 'ai-ml') === domainId).length;
  };

  const filteredCourses = courses.filter((c) => {
    const courseDomain = c.domain || 'ai-ml';
    const matchesDomain = currentDomain === 'all' || courseDomain === currentDomain;
    const matchesSearch =
      c.title.toLowerCase().includes(searchQuery.toLowerCase()) ||
      c.description.toLowerCase().includes(searchQuery.toLowerCase()) ||
      c.skills_taught?.some((s) => s.toLowerCase().includes(searchQuery.toLowerCase()));
    const matchesLevel = selectedLevel === 'All' || c.level === selectedLevel;
    return matchesDomain && matchesSearch && matchesLevel;
  });

  if (loading) return <LoadingSpinner message="Loading curriculum tracks..." />;

  return (
    <div className="animate-fade-in">
      {/* Page Header */}
      <div style={{ marginBottom: 24, display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', flexWrap: 'wrap', gap: 16 }}>
        <div>
          <div style={{ display: 'flex', alignItems: 'center', gap: 8, marginBottom: 4 }}>
            <span style={{ fontSize: '0.8rem', padding: '3px 10px', borderRadius: '12px', background: `${domainInfo.color}25`, color: domainInfo.color, fontWeight: 700, border: `1px solid ${domainInfo.color}40` }}>
              {currentDomain === 'all' ? '🌐 Complete Engineering Suite' : `${domainInfo.title} Track`}
            </span>
            <span style={{ fontSize: '0.8rem', color: 'var(--text-muted)' }}>
              ({filteredCourses.length} {filteredCourses.length === 1 ? 'course' : 'courses'} available)
            </span>
          </div>
          <h1 style={{ fontSize: '1.75rem', marginBottom: 6, letterSpacing: '-0.02em' }}>
            {currentDomain === 'all' ? 'Engineering Curriculum & Tracks' : `${domainInfo.title} Curriculum`}
          </h1>
          <p style={{ color: 'var(--text-secondary)', fontSize: '0.925rem' }}>
            {domainInfo.description || domainInfo.tagline}
          </p>
        </div>

        {/* Domain Switcher Quick 6 Pills */}
        <div style={{ display: 'flex', gap: 6, flexWrap: 'wrap', alignItems: 'center' }}>
          {Object.values(allDomains).map((d) => {
            const isSelected = currentDomain === d.id;
            const count = d.id === 'all' ? courses.length : getCourseCountForDomain(d.id);
            return (
              <button
                key={d.id}
                onClick={() => selectDomain(d.id)}
                className={`btn btn-sm ${isSelected ? 'btn-primary' : 'btn-ghost'}`}
                style={{
                  borderRadius: 16,
                  borderColor: isSelected ? d.color : 'var(--border-color)',
                  background: isSelected ? d.gradient : 'transparent',
                  color: isSelected ? '#fff' : 'var(--text-secondary)',
                  display: 'inline-flex',
                  alignItems: 'center',
                  gap: '6px',
                  fontSize: '0.785rem',
                  fontWeight: 600,
                  transition: 'all 0.2s ease',
                }}
              >
                <span>{d.shortTitle}</span>
                <span style={{
                  fontSize: '0.7rem',
                  padding: '1px 6px',
                  borderRadius: 10,
                  background: isSelected ? 'rgba(255,255,255,0.25)' : 'var(--bg-tertiary)',
                  color: isSelected ? '#fff' : 'var(--text-muted)'
                }}>
                  {count}
                </span>
              </button>
            );
          })}
        </div>
      </div>

      {/* Filter and Search Bar */}
      <div style={{ display: 'flex', gap: 14, marginBottom: 24, flexWrap: 'wrap' }}>
        <div style={{ flex: 1, minWidth: '260px', position: 'relative' }}>
          <Search size={16} style={{ position: 'absolute', left: 14, top: 12, color: 'var(--text-muted)' }} />
          <input
            type="text"
            className="form-input"
            placeholder={`Search ${showAllTracks ? 'all courses' : domainInfo.shortTitle} by topic, algorithm, or skill...`}
            value={searchQuery}
            onChange={(e) => setSearchQuery(e.target.value)}
            style={{ width: '100%', paddingLeft: 38 }}
          />
        </div>

        {/* Level Filters */}
        <div style={{ display: 'flex', gap: 6 }}>
          {['All', 'Beginner', 'Intermediate', 'Advanced'].map((lvl) => (
            <button
              key={lvl}
              onClick={() => setSelectedLevel(lvl)}
              className={selectedLevel === lvl ? 'btn btn-primary btn-sm' : 'btn btn-secondary btn-sm'}
              style={{ fontSize: '0.8rem' }}
            >
              {lvl}
            </button>
          ))}
        </div>
      </div>

      {/* Course Cards Grid */}
      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fill, minmax(340px, 1fr))', gap: 20 }}>
        {filteredCourses.map((course) => (
          <CourseCard key={course.slug} course={course} />
        ))}
      </div>

      {filteredCourses.length === 0 && (
        <div className="card" style={{ textAlign: 'center', padding: 48, color: 'var(--text-muted)' }}>
          <BookOpen size={32} style={{ margin: '0 auto 12px auto', opacity: 0.5 }} />
          <div style={{ fontWeight: 600, fontSize: '1rem', color: 'var(--text-secondary)' }}>
            No courses matching your criteria
          </div>
          <p style={{ fontSize: '0.85rem', marginTop: 4 }}>
            Try clearing your search query or selecting "All Tracks" to view the complete catalog.
          </p>
          <button
            onClick={() => {
              setSearchQuery('');
              setSelectedLevel('All');
              setShowAllTracks(true);
            }}
            className="btn btn-secondary btn-sm"
            style={{ marginTop: 12 }}
          >
            Show All Courses
          </button>
        </div>
      )}
    </div>
  );
}
