import React, { useState, useEffect } from 'react';
import { communityService } from '../services/communityService';
import { Users, ThumbsUp, MessageSquare, Plus, Send, Code } from 'lucide-react';

export default function CommunityPage() {
  const [posts, setPosts] = useState([]);
  const [loading, setLoading] = useState(true);
  const [showCreateModal, setShowCreateModal] = useState(false);

  // Form State
  const [title, setTitle] = useState('');
  const [category, setCategory] = useState('Show & Tell');
  const [content, setContent] = useState('');
  const [codeSnippet, setCodeSnippet] = useState('');
  const [tags, setTags] = useState('Transformers, PyTorch');
  const [submitting, setSubmitting] = useState(false);

  useEffect(() => {
    loadPosts();
  }, []);

  const loadPosts = async () => {
    try {
      setLoading(true);
      const data = await communityService.getPosts();
      setPosts(data);
    } catch (err) {
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  const handleUpvote = async (postId) => {
    try {
      const updated = await communityService.upvotePost(postId);
      setPosts((prev) => prev.map((p) => (p.id === postId ? updated : p)));
    } catch (err) {
      console.error(err);
    }
  };

  const handleCreatePost = async (e) => {
    e.preventDefault();
    if (!title.trim() || !content.trim()) return;
    try {
      setSubmitting(true);
      const newPost = await communityService.createPost({
        title,
        category,
        content,
        code_snippet: codeSnippet || null,
        tags: tags.split(',').map((t) => t.trim()).filter(Boolean),
      });
      setPosts([newPost, ...posts]);
      setShowCreateModal(false);
      setTitle('');
      setContent('');
      setCodeSnippet('');
    } catch (err) {
      console.error(err);
    } finally {
      setSubmitting(false);
    }
  };

  return (
    <div className="container" style={{ paddingBottom: 'var(--space-2xl)' }}>
      {/* Header */}
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', marginBottom: 'var(--space-xl)' }}>
        <div>
          <h1 style={{ fontSize: 'var(--font-2xl)', fontWeight: 800, margin: '0 0 var(--space-xs) 0', color: 'var(--color-text-main)', display: 'flex', alignItems: 'center', gap: '8px' }}>
            <Users size={24} color="var(--color-primary-400)" /> Student AI Community & Project Showcase
          </h1>
          <p style={{ margin: 0, color: 'var(--color-text-muted)', fontSize: 'var(--font-sm)' }}>
            Share your custom visualizers, discuss tricky algorithmic edge cases, and collaborate with fellow AI engineers.
          </p>
        </div>
        <button
          onClick={() => setShowCreateModal(true)}
          className="btn btn-primary"
          style={{ display: 'flex', alignItems: 'center', gap: '6px' }}
        >
          <Plus size={16} />
          <span>New Discussion Post</span>
        </button>
      </div>

      {loading ? (
        <div style={{ padding: 'var(--space-2xl)', textAlign: 'center', color: 'var(--color-text-muted)' }}>
          Loading community posts...
        </div>
      ) : (
        <div style={{ display: 'flex', flexDirection: 'column', gap: 'var(--space-lg)' }}>
          {posts.map((post) => (
            <div key={post.id} className="card" style={{ padding: 'var(--space-xl)', display: 'flex', flexDirection: 'column', gap: 'var(--space-md)' }}>
              <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start' }}>
                <div style={{ display: 'flex', alignItems: 'center', gap: '10px' }}>
                  <span style={{ fontSize: '24px' }}>{post.author_avatar}</span>
                  <div>
                    <h4 style={{ margin: 0, fontSize: 'var(--font-sm)', color: 'var(--color-text-main)' }}>
                      {post.author_name}
                    </h4>
                    <span style={{ fontSize: '10px', color: 'var(--color-text-muted)' }}>
                      {post.author_title} • {post.created_at}
                    </span>
                  </div>
                </div>

                <span style={{ fontSize: '10px', textTransform: 'uppercase', color: 'var(--color-primary-400)', fontWeight: 700, padding: '2px 8px', borderRadius: 'var(--radius-full)', background: 'rgba(99, 102, 241, 0.12)' }}>
                  {post.category}
                </span>
              </div>

              <h3 style={{ margin: 0, fontSize: 'var(--font-md)', color: 'var(--color-text-main)' }}>
                {post.title}
              </h3>

              <p style={{ margin: 0, fontSize: 'var(--font-xs)', color: 'var(--color-text-main)', lineHeight: 1.6 }}>
                {post.content}
              </p>

              {post.code_snippet && (
                <pre
                  style={{
                    padding: 'var(--space-md)',
                    background: '#0d1117',
                    color: '#e6edf3',
                    borderRadius: 'var(--radius-md)',
                    fontFamily: 'var(--font-mono)',
                    fontSize: '11px',
                    overflowX: 'auto',
                    margin: 0,
                  }}
                >
                  {post.code_snippet}
                </pre>
              )}

              <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', borderTop: '1px solid var(--color-border)', paddingTop: 'var(--space-sm)' }}>
                <div style={{ display: 'flex', gap: '4px' }}>
                  {post.tags.map((tag, idx) => (
                    <span key={idx} style={{ fontSize: '10px', padding: '2px 6px', borderRadius: 'var(--radius-sm)', background: 'var(--color-surface-elevated)', color: 'var(--color-text-muted)' }}>
                      #{tag}
                    </span>
                  ))}
                </div>

                <div style={{ display: 'flex', gap: 'var(--space-md)' }}>
                  <button
                    onClick={() => handleUpvote(post.id)}
                    style={{ background: 'none', border: 'none', color: 'var(--color-text-main)', cursor: 'pointer', display: 'flex', alignItems: 'center', gap: '6px', fontSize: 'var(--font-xs)' }}
                  >
                    <ThumbsUp size={14} color="var(--color-primary-400)" />
                    <span>{post.upvotes} Upvotes</span>
                  </button>
                  <span style={{ display: 'flex', alignItems: 'center', gap: '6px', fontSize: 'var(--font-xs)', color: 'var(--color-text-muted)' }}>
                    <MessageSquare size={14} />
                    <span>{post.comments_count} Comments</span>
                  </span>
                </div>
              </div>
            </div>
          ))}
        </div>
      )}

      {/* Create Post Modal */}
      {showCreateModal && (
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
          onClick={() => setShowCreateModal(false)}
        >
          <div
            style={{
              background: 'var(--color-surface)',
              border: '1px solid var(--color-border)',
              borderRadius: 'var(--radius-lg)',
              width: '100%',
              maxWidth: '600px',
              padding: 'var(--space-xl)',
              boxShadow: 'var(--shadow-xl)',
            }}
            onClick={(e) => e.stopPropagation()}
          >
            <h3 style={{ margin: '0 0 var(--space-md) 0', fontSize: 'var(--font-lg)' }}>
              Create Community Discussion
            </h3>

            <form onSubmit={handleCreatePost} style={{ display: 'flex', flexDirection: 'column', gap: 'var(--space-md)' }}>
              <div>
                <label style={{ display: 'block', fontSize: 'var(--font-xs)', fontWeight: 600, marginBottom: '4px' }}>Title</label>
                <input
                  type="text"
                  className="input"
                  placeholder="e.g. How to prevent exploding gradients in deep RNNs"
                  value={title}
                  onChange={(e) => setTitle(e.target.value)}
                  required
                />
              </div>

              <div>
                <label style={{ display: 'block', fontSize: 'var(--font-xs)', fontWeight: 600, marginBottom: '4px' }}>Category</label>
                <select className="input" value={category} onChange={(e) => setCategory(e.target.value)}>
                  <option value="Show & Tell">Show & Tell (Showcase Model/Code)</option>
                  <option value="Algorithm Debugging">Algorithm Debugging & Gotchas</option>
                  <option value="Research Paper Club">Research Paper Club</option>
                  <option value="Interview Prep">Interview Preparation</option>
                </select>
              </div>

              <div>
                <label style={{ display: 'block', fontSize: 'var(--font-xs)', fontWeight: 600, marginBottom: '4px' }}>Content</label>
                <textarea
                  className="input"
                  rows={4}
                  placeholder="Describe your question, observation, or breakthrough..."
                  value={content}
                  onChange={(e) => setContent(e.target.value)}
                  required
                />
              </div>

              <div>
                <label style={{ display: 'block', fontSize: 'var(--font-xs)', fontWeight: 600, marginBottom: '4px' }}>Code Snippet (Optional)</label>
                <textarea
                  className="input"
                  rows={3}
                  placeholder="Paste Python snippet..."
                  value={codeSnippet}
                  onChange={(e) => setCodeSnippet(e.target.value)}
                  style={{ fontFamily: 'var(--font-mono)', fontSize: '11px' }}
                />
              </div>

              <div style={{ display: 'flex', justifyContent: 'flex-end', gap: 'var(--space-sm)' }}>
                <button type="button" onClick={() => setShowCreateModal(false)} className="btn btn-secondary">
                  Cancel
                </button>
                <button type="submit" disabled={submitting} className="btn btn-primary">
                  {submitting ? 'Publishing...' : 'Publish Post'}
                </button>
              </div>
            </form>
          </div>
        </div>
      )}
    </div>
  );
}
