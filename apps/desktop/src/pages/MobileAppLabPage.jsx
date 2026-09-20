import React, { useState } from 'react';
import {
  Smartphone,
  Layers,
  ChevronRight,
  ArrowLeft,
  Heart,
  MessageCircle,
  Share2,
  Home,
  User,
  Search,
  Bell,
  Code2,
  Sparkles,
  ToggleLeft,
  ToggleRight
} from 'lucide-react';
import Badge from '../components/common/Badge';

export default function MobileAppLabPage() {
  const [deviceFrame, setDeviceFrame] = useState('ios'); // 'ios' or 'android'
  const [activeScreen, setActiveScreen] = useState('feed'); // 'feed', 'details', 'profile'
  const [selectedPost, setSelectedPost] = useState(null);
  const [likes, setLikes] = useState({ 1: 42, 2: 128, 3: 19 });
  const [isLiked, setIsLiked] = useState({});
  const [codeSyntax, setCodeSyntax] = useState('react-native'); // 'react-native' or 'flutter'

  const toggleLike = (id) => {
    setIsLiked(prev => ({ ...prev, [id]: !prev[id] }));
    setLikes(prev => ({
      ...prev,
      [id]: isLiked[id] ? prev[id] - 1 : prev[id] + 1
    }));
  };

  const POSTS = [
    {
      id: 1,
      author: 'Alex Chen',
      handle: '@alex_dev',
      avatar: 'https://images.unsplash.com/photo-1535713875002-d1d0cf377fde?w=100&auto=format&fit=crop&q=80',
      content: 'Just launched my first React Native app with animated layout transitions! 🚀📱',
      timestamp: '2h ago',
      tags: ['#reactnative', '#mobile', '#ios']
    },
    {
      id: 2,
      author: 'Sophia Rossi',
      handle: '@sophia_codes',
      avatar: 'https://images.unsplash.com/photo-1494790108377-be9c29b29330?w=100&auto=format&fit=crop&q=80',
      content: 'Flutter 3.x widget trees make cross-platform fluid 120 FPS UI feel like magic.',
      timestamp: '5h ago',
      tags: ['#flutter', '#dart', '#android']
    },
    {
      id: 3,
      author: 'Liam Vance',
      handle: '@liam_vance',
      avatar: 'https://images.unsplash.com/photo-1570295999919-56ceb5ecca61?w=100&auto=format&fit=crop&q=80',
      content: 'Tip: Always use FlatList with getItemLayout for long mobile feeds to keep memory steady.',
      timestamp: '1d ago',
      tags: ['#performance', '#mobileui']
    }
  ];

  return (
    <div className="animate-fade-in" style={{ paddingBottom: 40 }}>
      {/* Header */}
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', flexWrap: 'wrap', gap: 16, marginBottom: 24 }}>
        <div>
          <div style={{ display: 'flex', alignItems: 'center', gap: 10, marginBottom: 6 }}>
            <Badge variant="pink"><Smartphone size={14} /> Mobile App Lab</Badge>
            <span style={{ fontSize: '0.85rem', color: 'var(--text-muted)' }}>Interactive Viewport & State Emulator</span>
          </div>
          <h1 style={{ fontSize: '1.85rem', fontWeight: 800 }}>Cross-Platform Mobile Emulator</h1>
          <p style={{ color: 'var(--text-secondary)', fontSize: '0.95rem' }}>
            Interact with mobile components, test gesture interactions, and inspect synchronized React Native & Flutter code.
          </p>
        </div>

        {/* Device & Syntax Toggles */}
        <div style={{ display: 'flex', gap: 12, alignItems: 'center' }}>
          <div style={{ display: 'flex', background: 'var(--bg-tertiary)', padding: 4, borderRadius: 12, border: '1px solid var(--border-color)' }}>
            <button
              onClick={() => setDeviceFrame('ios')}
              className={`btn btn-sm ${deviceFrame === 'ios' ? 'btn-primary' : 'btn-ghost'}`}
              style={{ borderRadius: 8 }}
            >
              iOS iPhone
            </button>
            <button
              onClick={() => setDeviceFrame('android')}
              className={`btn btn-sm ${deviceFrame === 'android' ? 'btn-primary' : 'btn-ghost'}`}
              style={{ borderRadius: 8 }}
            >
              Android
            </button>
          </div>
        </div>
      </div>

      {/* Main Grid: Mobile Simulator (Left) & Component Inspector (Right) */}
      <div style={{ display: 'grid', gridTemplateColumns: 'minmax(340px, 380px) 1fr', gap: 32, alignItems: 'start' }}>
        {/* Mobile Device Frame */}
        <div style={{ display: 'flex', justifyContent: 'center' }}>
          <div
            style={{
              width: '360px',
              height: '700px',
              background: '#090d16',
              borderRadius: deviceFrame === 'ios' ? '50px' : '32px',
              border: '10px solid #1e293b',
              boxShadow: '0 25px 60px -15px rgba(0, 0, 0, 0.8), 0 0 0 2px #334155',
              display: 'flex',
              flexDirection: 'column',
              overflow: 'hidden',
              position: 'relative'
            }}
          >
            {/* Dynamic Island / Notch */}
            <div style={{ display: 'flex', justifyContent: 'center', paddingTop: 10, paddingBottom: 6, background: '#090d16', zIndex: 10 }}>
              {deviceFrame === 'ios' ? (
                <div style={{ width: 100, height: 24, borderRadius: 16, background: '#000000', display: 'flex', alignItems: 'center', justifyContent: 'space-between', padding: '0 8px' }}>
                  <div style={{ width: 8, height: 8, borderRadius: '50%', background: '#1e293b' }} />
                  <div style={{ width: 8, height: 8, borderRadius: '50%', background: '#064e3b' }} />
                </div>
              ) : (
                <div style={{ width: 12, height: 12, borderRadius: '50%', background: '#000000' }} />
              )}
            </div>

            {/* Mobile App Header */}
            <div style={{ padding: '12px 18px', display: 'flex', justifyContent: 'space-between', alignItems: 'center', borderBottom: '1px solid #1e293b', background: '#0f172a' }}>
              {activeScreen !== 'feed' ? (
                <button
                  onClick={() => setActiveScreen('feed')}
                  style={{ background: 'none', border: 'none', color: '#38bdf8', display: 'flex', alignItems: 'center', gap: 4, cursor: 'pointer', padding: 0 }}
                >
                  <ArrowLeft size={18} /> Back
                </button>
              ) : (
                <span style={{ fontWeight: 800, fontSize: '1.1rem', color: '#f8fafc' }}>📱 PulseApp</span>
              )}
              <Bell size={18} style={{ color: '#94a3b8' }} />
            </div>

            {/* Screen Content */}
            <div style={{ flex: 1, overflowY: 'auto', padding: '14px', display: 'flex', flexDirection: 'column', gap: 14 }}>
              {activeScreen === 'feed' && (
                <>
                  {POSTS.map((post) => (
                    <div
                      key={post.id}
                      style={{
                        background: '#1e293b',
                        padding: '14px',
                        borderRadius: '16px',
                        border: '1px solid #334155'
                      }}
                    >
                      {/* Author */}
                      <div style={{ display: 'flex', gap: 10, alignItems: 'center', marginBottom: 8 }}>
                        <img
                          src={post.avatar}
                          alt={post.author}
                          style={{ width: 34, height: 34, borderRadius: '50%', objectFit: 'cover' }}
                        />
                        <div>
                          <div style={{ fontSize: '0.85rem', fontWeight: 700, color: '#f8fafc' }}>{post.author}</div>
                          <div style={{ fontSize: '0.7rem', color: '#94a3b8' }}>{post.handle} • {post.timestamp}</div>
                        </div>
                      </div>

                      {/* Text */}
                      <p style={{ fontSize: '0.85rem', color: '#e2e8f0', lineHeight: 1.4, margin: '8px 0' }}>
                        {post.content}
                      </p>

                      {/* Actions */}
                      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginTop: 10, paddingTop: 8, borderTop: '1px solid #334155' }}>
                        <button
                          onClick={() => toggleLike(post.id)}
                          style={{
                            background: 'none',
                            border: 'none',
                            color: isLiked[post.id] ? '#f43f5e' : '#94a3b8',
                            display: 'flex',
                            alignItems: 'center',
                            gap: 6,
                            cursor: 'pointer',
                            fontSize: '0.8rem',
                            fontWeight: 600
                          }}
                        >
                          <Heart size={16} fill={isLiked[post.id] ? '#f43f5e' : 'none'} />
                          <span>{likes[post.id]}</span>
                        </button>

                        <button
                          onClick={() => {
                            setSelectedPost(post);
                            setActiveScreen('details');
                          }}
                          style={{
                            background: 'rgba(56, 189, 248, 0.1)',
                            border: 'none',
                            color: '#38bdf8',
                            padding: '4px 10px',
                            borderRadius: '8px',
                            fontSize: '0.75rem',
                            cursor: 'pointer',
                            fontWeight: 600
                          }}
                        >
                          View Details <ChevronRight size={12} />
                        </button>
                      </div>
                    </div>
                  ))}
                </>
              )}

              {activeScreen === 'details' && selectedPost && (
                <div style={{ background: '#1e293b', padding: '18px', borderRadius: '18px', border: '1px solid #334155' }}>
                  <div style={{ display: 'flex', gap: 10, alignItems: 'center', marginBottom: 12 }}>
                    <img
                      src={selectedPost.avatar}
                      alt={selectedPost.author}
                      style={{ width: 44, height: 44, borderRadius: '50%', objectFit: 'cover' }}
                    />
                    <div>
                      <div style={{ fontWeight: 700, color: '#f8fafc' }}>{selectedPost.author}</div>
                      <div style={{ fontSize: '0.75rem', color: '#94a3b8' }}>{selectedPost.handle}</div>
                    </div>
                  </div>
                  <p style={{ fontSize: '0.95rem', color: '#e2e8f0', lineHeight: 1.5 }}>{selectedPost.content}</p>
                  <div style={{ display: 'flex', gap: 6, marginTop: 12 }}>
                    {selectedPost.tags.map((t, idx) => (
                      <span key={idx} style={{ color: '#38bdf8', fontSize: '0.75rem' }}>{t}</span>
                    ))}
                  </div>
                </div>
              )}
            </div>

            {/* Bottom Tab Bar */}
            <div style={{ display: 'flex', justifyContent: 'space-around', padding: '12px 0', borderTop: '1px solid #1e293b', background: '#0f172a' }}>
              <button
                onClick={() => setActiveScreen('feed')}
                style={{ background: 'none', border: 'none', color: activeScreen === 'feed' ? '#38bdf8' : '#64748b', cursor: 'pointer' }}
              >
                <Home size={20} />
              </button>
              <button style={{ background: 'none', border: 'none', color: '#64748b', cursor: 'pointer' }}>
                <Search size={20} />
              </button>
              <button
                onClick={() => setActiveScreen('profile')}
                style={{ background: 'none', border: 'none', color: activeScreen === 'profile' ? '#38bdf8' : '#64748b', cursor: 'pointer' }}
              >
                <User size={20} />
              </button>
            </div>
          </div>
        </div>

        {/* Inspector & Code Generator Panel */}
        <div className="card" style={{ padding: 24 }}>
          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: 16 }}>
            <h3 style={{ fontSize: '1.2rem', fontWeight: 700, display: 'flex', alignItems: 'center', gap: 8 }}>
              <Code2 size={18} color="#ec4899" /> Generated Mobile Component Code
            </h3>
            <div style={{ display: 'flex', background: 'var(--bg-tertiary)', padding: 3, borderRadius: 8 }}>
              <button
                onClick={() => setCodeSyntax('react-native')}
                className={`btn btn-sm ${codeSyntax === 'react-native' ? 'btn-primary' : 'btn-ghost'}`}
                style={{ borderRadius: 6 }}
              >
                React Native
              </button>
              <button
                onClick={() => setCodeSyntax('flutter')}
                className={`btn btn-sm ${codeSyntax === 'flutter' ? 'btn-primary' : 'btn-ghost'}`}
                style={{ borderRadius: 6 }}
              >
                Flutter / Dart
              </button>
            </div>
          </div>

          {/* Code Block */}
          <pre
            style={{
              background: '#090d16',
              padding: 20,
              borderRadius: 14,
              border: '1px solid #1e293b',
              color: '#38bdf8',
              fontFamily: 'monospace',
              fontSize: '0.85rem',
              lineHeight: 1.6,
              overflowX: 'auto',
              maxHeight: '480px'
            }}
          >
            {codeSyntax === 'react-native' ? `import React, { useState } from 'react';
import { View, Text, FlatList, TouchableOpacity, StyleSheet, Image } from 'react-native';
import { Heart } from 'lucide-react-native';

export default function FeedScreen({ navigation }) {
  const [likes, setLikes] = useState(${JSON.stringify(likes)});

  return (
    <View style={styles.container}>
      <FlatList
        data={POSTS}
        keyExtractor={(item) => item.id.toString()}
        renderItem={({ item }) => (
          <View style={styles.card}>
            <Image source={{ uri: item.avatar }} style={styles.avatar} />
            <Text style={styles.author}>{item.author}</Text>
            <Text style={styles.content}>{item.content}</Text>
            <TouchableOpacity 
              onPress={() => navigation.navigate('Details', { post: item })}
              style={styles.detailBtn}
            >
              <Text style={styles.btnText}>View Details</Text>
            </TouchableOpacity>
          </View>
        )}
      />
    </View>
  );
}` : `import 'package:flutter/material.dart';

class FeedScreen extends StatefulWidget {
  @override
  _FeedScreenState createState() => _FeedScreenState();
}

class _FeedScreenState extends State<FeedScreen> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('📱 PulseApp')),
      body: ListView.builder(
        itemCount: posts.length,
        itemBuilder: (context, index) {
          final post = posts[index];
          return Card(
            margin: EdgeInsets.symmetric(horizontal: 16, vertical: 8),
            child: ListTile(
              leading: CircleAvatar(backgroundImage: NetworkImage(post.avatar)),
              title: Text(post.author),
              subtitle: Text(post.content),
              trailing: IconButton(
                icon: Icon(Icons.favorite_border),
                onPressed: () {},
              ),
            ),
          );
        },
      ),
    );
  }
}`}
          </pre>
        </div>
      </div>
    </div>
  );
}
