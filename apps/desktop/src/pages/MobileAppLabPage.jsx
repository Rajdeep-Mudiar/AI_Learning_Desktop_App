import React, { useState, useEffect } from 'react';
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
  ToggleRight,
  Wifi,
  WifiOff,
  RefreshCw,
  Trash2,
  Database,
  Activity,
  CheckCircle2,
  AlertTriangle,
  Move,
  Clock
} from 'lucide-react';
import Badge from '../components/common/Badge';

export default function MobileAppLabPage() {
  const [activeSimMode, setActiveSimMode] = useState('feed-state'); // 'feed-state' | 'gestures' | 'offline-sync' | 'fps-profiler'
  const [deviceFrame, setDeviceFrame] = useState('ios'); // 'ios' or 'android'
  const [codeSyntax, setCodeSyntax] = useState('react-native'); // 'react-native' or 'flutter'

  // --- Simulation 1: Feed & State ---
  const [activeScreen, setActiveScreen] = useState('feed');
  const [selectedPost, setSelectedPost] = useState(null);
  const [likes, setLikes] = useState({ 1: 42, 2: 128, 3: 19 });
  const [isLiked, setIsLiked] = useState({});

  // --- Simulation 2: Swipe Gestures ---
  const [gestureCards, setGestureCards] = useState([
    { id: 'g1', title: 'Payment Receipt ($49.00)', desc: 'Stripe webhook completed', tag: 'Finance' },
    { id: 'g2', title: 'Security Alert: New Sign-in', desc: 'San Francisco, CA (Chrome on macOS)', tag: 'Security' },
    { id: 'g3', title: 'GitHub PR #42 Merged', desc: 'feat: dynamic route isolation', tag: 'DevOps' }
  ]);
  const [swipedId, setSwipedId] = useState(null);
  const [isRefreshing, setIsRefreshing] = useState(false);

  // --- Simulation 3: Offline Sync Engine ---
  const [isOnline, setIsOnline] = useState(true);
  const [offlineQueue, setOfflineQueue] = useState([]);
  const [localDbItems, setLocalDbItems] = useState([
    { id: 'd1', text: 'Prepare mobile release build', synced: true },
    { id: 'd2', text: 'Configure push notifications payload', synced: true }
  ]);
  const [newTodoInput, setNewTodoInput] = useState('');

  // --- Simulation 4: 120 FPS Profiler ---
  const [jsThreadLoad, setJsThreadLoad] = useState(30); // 0-100%
  const [fps, setFps] = useState(120);
  const [frameDrops, setFrameDrops] = useState(0);

  // Dynamic FPS calculation
  useEffect(() => {
    if (jsThreadLoad > 75) {
      setFps(Math.max(24, Math.round(120 - (jsThreadLoad - 75) * 3.8)));
      setFrameDrops(prev => prev + 1);
    } else {
      setFps(120);
    }
  }, [jsThreadLoad]);

  const toggleLike = (id) => {
    setIsLiked(prev => ({ ...prev, [id]: !prev[id] }));
    setLikes(prev => ({
      ...prev,
      [id]: isLiked[id] ? prev[id] - 1 : prev[id] + 1
    }));
  };

  const deleteGestureCard = (id) => {
    setSwipedId(id);
    setTimeout(() => {
      setGestureCards(prev => prev.filter(c => c.id !== id));
      setSwipedId(null);
    }, 250);
  };

  const handlePullToRefresh = () => {
    setIsRefreshing(true);
    setTimeout(() => {
      setGestureCards([
        { id: `g${Date.now()}`, title: '⚡ Live Push: Server Health 100%', desc: 'Real-time telemetry event received', tag: 'System' },
        ...gestureCards
      ]);
      setIsRefreshing(false);
    }, 800);
  };

  const handleAddOfflineItem = (e) => {
    e.preventDefault();
    if (!newTodoInput.trim()) return;

    const newItem = {
      id: `local_${Date.now()}`,
      text: newTodoInput.trim(),
      synced: isOnline
    };

    setLocalDbItems(prev => [newItem, ...prev]);

    if (!isOnline) {
      setOfflineQueue(prev => [...prev, { action: 'INSERT', item: newItem, timestamp: new Date().toLocaleTimeString() }]);
    }
    setNewTodoInput('');
  };

  const syncOfflineQueue = () => {
    if (!isOnline || offlineQueue.length === 0) return;
    setLocalDbItems(prev => prev.map(item => ({ ...item, synced: true })));
    setOfflineQueue([]);
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
    }
  ];

  return (
    <div className="animate-fade-in" style={{ paddingBottom: 40 }}>
      {/* Header */}
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', flexWrap: 'wrap', gap: 16, marginBottom: 20 }}>
        <div>
          <div style={{ display: 'flex', alignItems: 'center', gap: 10, marginBottom: 6 }}>
            <Badge variant="pink"><Smartphone size={14} /> Mobile App Emulator</Badge>
            <span style={{ fontSize: '0.85rem', color: 'var(--text-muted)' }}>Interactive Mobile Runtime & Viewport</span>
          </div>
          <h1 style={{ fontSize: '1.85rem', fontWeight: 800 }}>Mobile Engineering Interactive Simulations</h1>
          <p style={{ color: 'var(--text-secondary)', fontSize: '0.95rem' }}>
            Simulate gesture physics, touch animations, offline SQLite queues, and 120 FPS thread budget profilers.
          </p>
        </div>

        {/* Device & Syntax Toggles */}
        <div style={{ display: 'flex', gap: 10, alignItems: 'center' }}>
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

      {/* Simulation Mode Tabs (Basics -> Advanced) */}
      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(200px, 1fr))', gap: 10, marginBottom: 24 }}>
        {[
          { id: 'feed-state', level: 'Basics (Level 1)', title: '1. UI State & Touch Widgets', color: '#10b981' },
          { id: 'gestures', level: 'Intermediate (Level 2)', title: '2. Swipe Gestures & Physics', color: '#38bdf8' },
          { id: 'offline-sync', level: 'Advanced (Level 3)', title: '3. Offline-First SQLite Queue', color: '#f59e0b' },
          { id: 'fps-profiler', level: 'Architecture (Level 4)', title: '4. 120 FPS Thread Budget', color: '#ec4899' }
        ].map((mode) => {
          const isActive = activeSimMode === mode.id;
          return (
            <button
              key={mode.id}
              onClick={() => setActiveSimMode(mode.id)}
              style={{
                background: isActive ? 'var(--bg-card)' : 'var(--bg-tertiary)',
                border: isActive ? `2px solid ${mode.color}` : '1px solid var(--border-color)',
                padding: '10px 14px',
                borderRadius: '12px',
                textAlign: 'left',
                cursor: 'pointer',
                transition: 'all 0.15s ease'
              }}
            >
              <div style={{ fontSize: '0.7rem', fontWeight: 700, color: mode.color, textTransform: 'uppercase' }}>{mode.level}</div>
              <div style={{ fontSize: '0.85rem', fontWeight: 700, color: 'var(--text-primary)', marginTop: 2 }}>{mode.title}</div>
            </button>
          );
        })}
      </div>

      {/* Main Grid: Mobile Simulator (Left) & Inspector / Code (Right) */}
      <div style={{ display: 'grid', gridTemplateColumns: 'minmax(340px, 380px) 1fr', gap: 32, alignItems: 'start' }}>
        {/* Mobile Device Frame */}
        <div style={{ display: 'flex', justifyContent: 'center' }}>
          <div
            style={{
              width: '360px',
              height: '680px',
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

            {/* Mobile App Header Bar */}
            <div style={{ padding: '12px 18px', display: 'flex', justifyContent: 'space-between', alignItems: 'center', borderBottom: '1px solid #1e293b', background: '#0f172a' }}>
              <span style={{ fontWeight: 800, fontSize: '1rem', color: '#f8fafc' }}>
                {activeSimMode === 'feed-state' && '📱 PulseFeed'}
                {activeSimMode === 'gestures' && '👆 GestureHub'}
                {activeSimMode === 'offline-sync' && '💾 OfflineSync DB'}
                {activeSimMode === 'fps-profiler' && '⚡ 120 FPS Profiler'}
              </span>

              {activeSimMode === 'offline-sync' ? (
                <button
                  onClick={() => setIsOnline(!isOnline)}
                  style={{
                    background: isOnline ? 'rgba(16, 185, 129, 0.2)' : 'rgba(244, 63, 94, 0.2)',
                    border: 'none',
                    color: isOnline ? '#10b981' : '#f43f5e',
                    padding: '4px 8px',
                    borderRadius: '8px',
                    fontSize: '0.7rem',
                    fontWeight: 700,
                    display: 'flex',
                    alignItems: 'center',
                    gap: 4,
                    cursor: 'pointer'
                  }}
                >
                  {isOnline ? <Wifi size={12} /> : <WifiOff size={12} />}
                  {isOnline ? 'Online' : 'Offline'}
                </button>
              ) : (
                <Bell size={16} style={{ color: '#94a3b8' }} />
              )}
            </div>

            {/* Screen Content Container */}
            <div style={{ flex: 1, overflowY: 'auto', padding: '14px', display: 'flex', flexDirection: 'column', gap: 12 }}>
              
              {/* MODE 1: FEED & STATE */}
              {activeSimMode === 'feed-state' && (
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
                      <div style={{ display: 'flex', gap: 10, alignItems: 'center', marginBottom: 8 }}>
                        <img src={post.avatar} alt={post.author} style={{ width: 34, height: 34, borderRadius: '50%', objectFit: 'cover' }} />
                        <div>
                          <div style={{ fontSize: '0.85rem', fontWeight: 700, color: '#f8fafc' }}>{post.author}</div>
                          <div style={{ fontSize: '0.7rem', color: '#94a3b8' }}>{post.handle} • {post.timestamp}</div>
                        </div>
                      </div>
                      <p style={{ fontSize: '0.85rem', color: '#e2e8f0', lineHeight: 1.4, margin: '8px 0' }}>{post.content}</p>
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
                      </div>
                    </div>
                  ))}
                </>
              )}

              {/* MODE 2: GESTURES & SWIPE */}
              {activeSimMode === 'gestures' && (
                <>
                  <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                    <span style={{ fontSize: '0.75rem', color: '#94a3b8' }}>Swipe or click delete to test gestures:</span>
                    <button onClick={handlePullToRefresh} className="btn btn-ghost btn-sm" style={{ padding: '2px 8px', fontSize: '0.7rem', gap: 4 }}>
                      <RefreshCw size={10} className={isRefreshing ? 'animate-spin' : ''} /> Pull-to-Refresh
                    </button>
                  </div>

                  {gestureCards.map((card) => (
                    <div
                      key={card.id}
                      style={{
                        background: '#1e293b',
                        padding: '12px 14px',
                        borderRadius: '12px',
                        border: '1px solid #334155',
                        display: 'flex',
                        justifyContent: 'space-between',
                        alignItems: 'center',
                        transition: 'all 0.25s ease',
                        opacity: swipedId === card.id ? 0 : 1,
                        transform: swipedId === card.id ? 'translateX(100px)' : 'none'
                      }}
                    >
                      <div>
                        <div style={{ fontSize: '0.8rem', fontWeight: 700, color: '#f8fafc' }}>{card.title}</div>
                        <div style={{ fontSize: '0.7rem', color: '#94a3b8', marginTop: 2 }}>{card.desc}</div>
                      </div>
                      <button
                        onClick={() => deleteGestureCard(card.id)}
                        style={{ background: 'rgba(244, 63, 94, 0.15)', border: 'none', color: '#f43f5e', padding: '6px 8px', borderRadius: '8px', cursor: 'pointer' }}
                        title="Swipe to Delete"
                      >
                        <Trash2 size={14} />
                      </button>
                    </div>
                  ))}
                </>
              )}

              {/* MODE 3: OFFLINE SYNC */}
              {activeSimMode === 'offline-sync' && (
                <>
                  <form onSubmit={handleAddOfflineItem} style={{ display: 'flex', gap: 6 }}>
                    <input
                      type="text"
                      value={newTodoInput}
                      onChange={(e) => setNewTodoInput(e.target.value)}
                      placeholder="Add local record..."
                      style={{ flex: 1, padding: '8px 10px', background: '#1e293b', border: '1px solid #334155', borderRadius: '8px', color: '#fff', fontSize: '0.8rem' }}
                    />
                    <button type="submit" className="btn btn-primary btn-sm" style={{ fontSize: '0.75rem', padding: '8px 12px' }}>
                      + Add
                    </button>
                  </form>

                  {offlineQueue.length > 0 && isOnline && (
                    <button
                      onClick={syncOfflineQueue}
                      className="btn btn-sm"
                      style={{ background: '#10b981', color: '#090d16', fontWeight: 700, fontSize: '0.75rem', width: '100%' }}
                    >
                      ⚡ Flush & Sync {offlineQueue.length} Pending Records
                    </button>
                  )}

                  <div style={{ fontSize: '0.75rem', fontWeight: 700, color: '#94a3b8', marginTop: 6 }}>Local SQLite Database:</div>
                  {localDbItems.map((item) => (
                    <div
                      key={item.id}
                      style={{
                        padding: '10px 12px',
                        background: '#1e293b',
                        borderRadius: '8px',
                        border: `1px solid ${item.synced ? '#334155' : '#f59e0b'}`,
                        display: 'flex',
                        justifyContent: 'space-between',
                        alignItems: 'center'
                      }}
                    >
                      <span style={{ fontSize: '0.8rem', color: '#f8fafc' }}>{item.text}</span>
                      <span style={{ fontSize: '0.65rem', padding: '2px 6px', borderRadius: '4px', background: item.synced ? 'rgba(16, 185, 129, 0.2)' : 'rgba(245, 158, 11, 0.2)', color: item.synced ? '#10b981' : '#f59e0b', fontWeight: 700 }}>
                        {item.synced ? 'SYNCED' : 'PENDING'}
                      </span>
                    </div>
                  ))}
                </>
              )}

              {/* MODE 4: 120 FPS PROFILER */}
              {activeSimMode === 'fps-profiler' && (
                <>
                  <div style={{ padding: '14px', background: '#1e293b', borderRadius: '12px', border: '1px solid #334155' }}>
                    <div style={{ fontSize: '0.8rem', color: '#94a3b8' }}>Target Refresh Rate:</div>
                    <div style={{ fontSize: '2.4rem', fontWeight: 800, color: fps >= 90 ? '#10b981' : '#f43f5e' }}>
                      {fps} <span style={{ fontSize: '1rem' }}>FPS</span>
                    </div>
                    <div style={{ fontSize: '0.75rem', color: '#94a3b8', marginTop: 4 }}>
                      Frame Budget: <strong>{fps >= 90 ? '8.3ms' : '16.6ms'}</strong> • Dropped Frames: <strong style={{ color: '#f43f5e' }}>{frameDrops}</strong>
                    </div>
                  </div>

                  <div style={{ padding: '12px', background: '#0f172a', borderRadius: '10px', border: '1px solid #1e293b' }}>
                    <div style={{ display: 'flex', justifyContent: 'space-between', fontSize: '0.75rem', marginBottom: 6 }}>
                      <span>JS Main Thread Workload:</span>
                      <strong>{jsThreadLoad}%</strong>
                    </div>
                    <input
                      type="range"
                      min="0"
                      max="100"
                      value={jsThreadLoad}
                      onChange={(e) => setJsThreadLoad(Number(e.target.value))}
                      style={{ width: '100%', cursor: 'pointer' }}
                    />
                  </div>
                </>
              )}

            </div>

            {/* Bottom Tab Bar */}
            <div style={{ display: 'flex', justifyContent: 'space-around', padding: '12px 0', borderTop: '1px solid #1e293b', background: '#0f172a' }}>
              <button style={{ background: 'none', border: 'none', color: '#38bdf8', cursor: 'pointer' }}><Home size={20} /></button>
              <button style={{ background: 'none', border: 'none', color: '#64748b', cursor: 'pointer' }}><Search size={20} /></button>
              <button style={{ background: 'none', border: 'none', color: '#64748b', cursor: 'pointer' }}><User size={20} /></button>
            </div>
          </div>
        </div>

        {/* Inspector & Architecture Panel */}
        <div className="card" style={{ padding: 24 }}>
          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: 16 }}>
            <h3 style={{ fontSize: '1.15rem', fontWeight: 700, display: 'flex', alignItems: 'center', gap: 8 }}>
              <Code2 size={18} color="#ec4899" /> Mobile Engineering Code Architecture
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
                Flutter
              </button>
            </div>
          </div>

          {/* Dynamic Code Generator */}
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
              maxHeight: '520px'
            }}
          >
            {activeSimMode === 'offline-sync' ? (
              codeSyntax === 'react-native' ? `// React Native Offline-First SQLite Sync
import SQLite from 'react-native-sqlite-storage';
import NetInfo from '@react-native-community/netinfo';

const db = SQLite.openDatabase({ name: 'app.db', location: 'default' });

export async function insertRecord(text) {
  const isConnected = (await NetInfo.fetch()).isConnected;
  
  db.transaction(tx => {
    tx.executeSql(
      'INSERT INTO items (text, synced) VALUES (?, ?)',
      [text, isConnected ? 1 : 0]
    );
  });

  if (!isConnected) {
    queueSyncJob({ action: 'INSERT', payload: text });
  }
}` : `// Flutter Offline-First SQLite with sqflite & connectivity_plus
import 'package:sqflite/sqflite.dart';
import 'package:connectivity_plus/connectivity_plus.dart';

Future<void> insertRecord(String text) async {
  final db = await openDatabase('app.db');
  final connectivity = await Connectivity().checkConnectivity();
  final bool isOnline = connectivity != ConnectivityResult.none;

  await db.insert('items', {
    'text': text,
    'synced': isOnline ? 1 : 0,
  });

  if (!isOnline) {
    SyncQueue.addJob(action: 'INSERT', data: text);
  }
}`
            ) : activeSimMode === 'fps-profiler' ? (
              codeSyntax === 'react-native' ? `// React Native 120 FPS Reanimated Worklet & Frame Budget
import { useSharedValue, useAnimatedStyle, withSpring, runOnUI } from 'react-native-reanimated';

export function HighPerformance60FPSList() {
  const offset = useSharedValue(0);

  // Runs directly on the native UI thread (off the JS bridge)
  const animatedStyles = useAnimatedStyle(() => {
    'worklet';
    return {
      transform: [{ translateY: withSpring(offset.value, { damping: 15 }) }],
    };
  });

  return <Animated.View style={[styles.box, animatedStyles]} />;
}` : `// Flutter RepaintBoundary & 120Hz Display Sync
import 'package:flutter/material.dart';

class OptimizedSmoothWidget extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    // Isolates rasterization to prevent full-tree repaint jank
    return RepaintBoundary(
      child: CustomPaint(
        painter: ParticleMeshPainter(),
        isComplex: true,
        willChange: true,
      ),
    );
  }
}`
            ) : (
              codeSyntax === 'react-native' ? `// React Native Animated Gestures & State
import React, { useState } from 'react';
import { View, Text, FlatList, TouchableOpacity, StyleSheet } from 'react-native';

export default function FeedScreen() {
  const [likes, setLikes] = useState(${JSON.stringify(likes)});

  return (
    <View style={styles.container}>
      <FlatList
        data={POSTS}
        keyExtractor={(item) => item.id.toString()}
        renderItem={({ item }) => (
          <View style={styles.card}>
            <Text style={styles.author}>{item.author}</Text>
            <Text style={styles.content}>{item.content}</Text>
          </View>
        )}
      />
    </View>
  );
}` : `// Flutter Reactive Feed & Widget Tree
import 'package:flutter/material.dart';

class FeedScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('📱 PulseApp')),
      body: ListView.builder(
        itemCount: posts.length,
        itemBuilder: (context, index) {
          return Card(
            child: ListTile(
              title: Text(posts[index].author),
              subtitle: Text(posts[index].content),
            ),
          );
        },
      ),
    );
  }
}`
            )}
          </pre>
        </div>
      </div>
    </div>
  );
}

