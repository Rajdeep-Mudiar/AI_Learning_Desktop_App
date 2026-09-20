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
  const [activeCategory, setActiveCategory] = useState('All');

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

  const filteredCourses = courses.filter((c) => {
    const matchesDomain = activeCategory === 'All' || c.domain === activeCategory || c.category === activeCategory || !c.domain;
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
            <span style={{ fontSize: '0.8rem', padding: '2px 8px', borderRadius: '10px', background: `${domainInfo.color}20`, color: domainInfo.color, fontWeight: 700 }}>
              {domainInfo.title}
            </span>
          </div>
          <h1 style={{ fontSize: '1.75rem', marginBottom: 6 }}>Engineering Curriculum & Tracks</h1>
          <p style={{ color: 'var(--text-secondary)', fontSize: '0.925rem' }}>
            Structured, interactive learning paths tailored to your selected discipline.
          </p>
        </div>

        {/* Domain Switcher Quick Pills */}
        <div style={{ display: 'flex', gap: 6, flexWrap: 'wrap' }}>
          {Object.values(allDomains).map((d) => (
            <button
              key={d.id}
              onClick={() => {
                selectDomain(d.id);
                setActiveCategory('All');
              }}
              className={`btn btn-sm ${currentDomain === d.id ? 'btn-primary' : 'btn-ghost'}`}
              style={{
                borderRadius: 16,
                borderColor: currentDomain === d.id ? d.color : 'var(--border-color)',
                background: currentDomain === d.id ? d.gradient : 'transparent',
                color: currentDomain === d.id ? '#fff' : 'var(--text-secondary)'
              }}
            >
              {d.shortTitle}
            </button>
          ))}
        </div>
      </div>

      {/* Filter and Search Bar */}
      <div style={{ display: 'flex', gap: 14, marginBottom: 24, flexWrap: 'wrap' }}>
        <div style={{ flex: 1, minWidth: '260px', position: 'relative' }}>
          <Search size={16} style={{ position: 'absolute', left: 14, top: 12, color: 'var(--text-muted)' }} />
          <input
            type="text"
            className="form-input"
            placeholder="Search by topic, algorithm, or skill (e.g., PyTorch, OLS, Attention)..."
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
            >
              {lvl}
            </button>
          ))}
        </div>
      </div>

      {/* Course Cards Grid */}
      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fill, minmax(320px, 1fr))', gap: 20 }}>
        {filteredCourses.map((course) => (
          <CourseCard key={course.slug} course={course} />
        ))}
      </div>

      {filteredCourses.length === 0 && (
        <div className="card" style={{ textAlign: 'center', padding: 48, color: 'var(--text-muted)' }}>
          No courses matching your search query.
        </div>
      )}
    </div>
  );
}
