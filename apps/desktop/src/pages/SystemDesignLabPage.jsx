import React, { useState, useEffect } from 'react';
import {
  Layers,
  Server,
  Database,
  Cpu,
  Zap,
  Activity,
  AlertTriangle,
  Play,
  RotateCcw,
  Sparkles,
  ShieldAlert,
  Sliders,
  CheckCircle2,
  HardDrive,
  Network,
  Lock,
  RefreshCw,
  Clock,
  Compass
} from 'lucide-react';
import Badge from '../components/common/Badge';

export default function SystemDesignLabPage() {
  const [activeTab, setActiveTab] = useState('load-balancer'); // 'load-balancer' | 'cache-engine' | 'rate-limiter' | 'consistent-hash' | 'circuit-breaker'

  // --- Module 1: Load Balancer State ---
  const [lbAlgorithm, setLbAlgorithm] = useState('round-robin'); // 'round-robin', 'least-conn', 'ip-hash'
  const [rps, setRps] = useState(3000);
  const [serverCount, setServerCount] = useState(3);
  const [chaosFailure, setChaosFailure] = useState(false);

  // --- Module 2: Redis Cache State ---
  const [cacheStrategy, setCacheStrategy] = useState('cache-aside'); // 'cache-aside', 'write-through'
  const [cacheTtl, setCacheTtl] = useState(60); // seconds
  const [cacheMutexLock, setCacheMutexLock] = useState(true);
  const [cacheHits, setCacheHits] = useState(88);

  // --- Module 3: Rate Limiter State ---
  const [bucketCapacity, setBucketCapacity] = useState(100);
  const [refillRate, setRefillRate] = useState(25); // tokens per second
  const [currentTokens, setCurrentTokens] = useState(100);
  const [incomingBurst, setIncomingBurst] = useState(40);
  const [rateLimitDropped, setRateLimitDropped] = useState(0);

  // --- Module 4: Consistent Hashing Ring ---
  const [nodes, setNodes] = useState(['Node A (0°)', 'Node B (120°)', 'Node C (240°)']);
  const [virtualNodesPerNode, setVirtualNodesPerNode] = useState(3);
  const [sampleKeys, setSampleKeys] = useState([
    { key: 'user_102', hashAngle: 45, assignedNode: 'Node A (0°)' },
    { key: 'session_892', hashAngle: 180, assignedNode: 'Node B (120°)' },
    { key: 'order_551', hashAngle: 310, assignedNode: 'Node C (240°)' }
  ]);

  // --- Module 5: Circuit Breaker ---
  const [breakerState, setBreakerState] = useState('CLOSED'); // 'CLOSED', 'OPEN', 'HALF_OPEN'
  const [failureCount, setFailureCount] = useState(0);
  const [failureThreshold, setFailureThreshold] = useState(5);

  // Auto-refill Token Bucket simulation
  useEffect(() => {
    const timer = setInterval(() => {
      setCurrentTokens(prev => Math.min(bucketCapacity, prev + Math.round(refillRate / 5)));
    }, 200);
    return () => clearInterval(timer);
  }, [bucketCapacity, refillRate]);

  const triggerBurstRequest = () => {
    if (currentTokens >= incomingBurst) {
      setCurrentTokens(prev => prev - incomingBurst);
    } else {
      const allowed = currentTokens;
      const dropped = incomingBurst - allowed;
      setCurrentTokens(0);
      setRateLimitDropped(prev => prev + dropped);
    }
  };

  const simulateUpstreamFailure = () => {
    const newFailures = failureCount + 1;
    setFailureCount(newFailures);
    if (newFailures >= failureThreshold) {
      setBreakerState('OPEN');
    }
  };

  const resetCircuitBreaker = () => {
    setBreakerState('CLOSED');
    setFailureCount(0);
  };

  // Derived dynamic metrics
  const activeServers = chaosFailure ? Math.max(1, serverCount - 1) : serverCount;
  const loadPerServer = Math.round(rps / activeServers);
  const cpuLoad = Math.min(100, Math.round((loadPerServer / 2000) * 100));
  const latencyMs = Math.round(
    (cacheHits > 50 ? 8 : 45) + (cpuLoad > 85 ? (cpuLoad - 85) * 4 : 0) + (chaosFailure ? 35 : 0)
  );

  return (
    <div className="animate-fade-in" style={{ paddingBottom: 40 }}>
      {/* Header */}
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', flexWrap: 'wrap', gap: 16, marginBottom: 20 }}>
        <div>
          <div style={{ display: 'flex', alignItems: 'center', gap: 10, marginBottom: 6 }}>
            <Badge variant="green"><Layers size={14} /> System Architecture Studio</Badge>
            <span style={{ fontSize: '0.85rem', color: 'var(--text-muted)' }}>High-Scale Distributed Simulator</span>
          </div>
          <h1 style={{ fontSize: '1.85rem', fontWeight: 800 }}>Distributed System Interactive Simulations</h1>
          <p style={{ color: 'var(--text-secondary)', fontSize: '0.95rem' }}>
            Experiment with Load Balancing, Distributed Caching, Token Bucket Rate Limiting, Consistent Hashing, and Circuit Breakers.
          </p>
        </div>
      </div>

      {/* Progressive Architecture Level Tabs */}
      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(200px, 1fr))', gap: 10, marginBottom: 20 }}>
        {[
          { id: 'load-balancer', level: 'Basics (Level 1)', title: '1. Load Balancing & Cluster', color: '#10b981' },
          { id: 'cache-engine', level: 'Intermediate (Level 2)', title: '2. Redis Cache & Invalidation', color: '#38bdf8' },
          { id: 'rate-limiter', level: 'Advanced (Level 3)', title: '3. Token Bucket Rate Limiter', color: '#f59e0b' },
          { id: 'consistent-hash', level: 'Advanced (Level 4)', title: '4. Consistent Hashing Ring', color: '#8b5cf6' },
          { id: 'circuit-breaker', level: 'Resilience (Level 5)', title: '5. Circuit Breaker States', color: '#ec4899' }
        ].map((tab) => {
          const isActive = activeTab === tab.id;
          return (
            <button
              key={tab.id}
              onClick={() => setActiveTab(tab.id)}
              style={{
                background: isActive ? 'var(--bg-card)' : 'var(--bg-tertiary)',
                border: isActive ? `2px solid ${tab.color}` : '1px solid var(--border-color)',
                padding: '10px 14px',
                borderRadius: '12px',
                textAlign: 'left',
                cursor: 'pointer',
                transition: 'all 0.15s ease'
              }}
            >
              <div style={{ fontSize: '0.7rem', fontWeight: 700, color: tab.color, textTransform: 'uppercase' }}>{tab.level}</div>
              <div style={{ fontSize: '0.85rem', fontWeight: 700, color: 'var(--text-primary)', marginTop: 2 }}>{tab.title}</div>
            </button>
          );
        })}
      </div>

      {/* Top Telemetry Metric Cards */}
      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(200px, 1fr))', gap: 14, marginBottom: 20 }}>
        <div className="card" style={{ padding: 16, borderLeft: '4px solid #10b981' }}>
          <div style={{ fontSize: '0.75rem', color: 'var(--text-muted)', marginBottom: 2 }}>Incoming Traffic</div>
          <div style={{ fontSize: '1.5rem', fontWeight: 800, color: '#10b981' }}>{rps.toLocaleString()} <span style={{ fontSize: '0.8rem', color: 'var(--text-muted)' }}>RPS</span></div>
        </div>

        <div className="card" style={{ padding: 16, borderLeft: `4px solid ${latencyMs > 50 ? '#f43f5e' : '#38bdf8'}` }}>
          <div style={{ fontSize: '0.75rem', color: 'var(--text-muted)', marginBottom: 2 }}>P99 Response Latency</div>
          <div style={{ fontSize: '1.5rem', fontWeight: 800, color: latencyMs > 50 ? '#f43f5e' : '#38bdf8' }}>{latencyMs} ms</div>
        </div>

        <div className="card" style={{ padding: 16, borderLeft: '4px solid #8b5cf6' }}>
          <div style={{ fontSize: '0.75rem', color: 'var(--text-muted)', marginBottom: 2 }}>Active App Cluster Nodes</div>
          <div style={{ fontSize: '1.5rem', fontWeight: 800, color: '#8b5cf6' }}>{activeServers} <span style={{ fontSize: '0.8rem', color: 'var(--text-muted)' }}>/ {serverCount} Nodes</span></div>
        </div>

        <div className="card" style={{ padding: 16, borderLeft: `4px solid ${cpuLoad > 85 ? '#f43f5e' : '#eab308'}` }}>
          <div style={{ fontSize: '0.75rem', color: 'var(--text-muted)', marginBottom: 2 }}>Server CPU Utilization</div>
          <div style={{ fontSize: '1.5rem', fontWeight: 800, color: cpuLoad > 85 ? '#f43f5e' : '#eab308' }}>{cpuLoad}% {cpuLoad > 85 && '⚠️'}</div>
        </div>
      </div>

      {/* TAB 1: LOAD BALANCER & CLUSTER */}
      {activeTab === 'load-balancer' && (
        <div style={{ display: 'grid', gap: 20 }}>
          <div className="card" style={{ padding: 24, background: '#090d16', border: '1px solid #1e293b' }}>
            <h3 style={{ fontSize: '1.1rem', fontWeight: 700, marginBottom: 20, display: 'flex', alignItems: 'center', gap: 8 }}>
              <Zap size={18} color="#10b981" /> Load Balancer Traffic Distribution
            </h3>

            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', flexWrap: 'wrap', gap: 20 }}>
              {/* Clients */}
              <div style={{ textAlign: 'center', padding: '16px 20px', background: '#1e293b', borderRadius: '12px', border: '1px solid #334155' }}>
                <div style={{ fontSize: '1.6rem' }}>👥</div>
                <div style={{ fontWeight: 700, fontSize: '0.85rem', marginTop: 4 }}>Clients ({rps} RPS)</div>
              </div>

              <div style={{ color: '#64748b', fontSize: '1.2rem' }}>➔</div>

              {/* LB Node */}
              <div style={{ textAlign: 'center', padding: '16px 20px', background: '#1e293b', borderRadius: '12px', border: '1px solid #38bdf8' }}>
                <Activity size={24} color="#38bdf8" style={{ margin: '0 auto 4px' }} />
                <div style={{ fontWeight: 700, fontSize: '0.85rem' }}>Nginx / Envoy LB</div>
                <div style={{ fontSize: '0.7rem', color: '#38bdf8' }}>Strategy: {lbAlgorithm}</div>
              </div>

              <div style={{ color: '#64748b', fontSize: '1.2rem' }}>➔</div>

              {/* Cluster Nodes */}
              <div style={{ display: 'flex', flexDirection: 'column', gap: 8 }}>
                {Array.from({ length: serverCount }).map((_, idx) => {
                  const isDead = chaosFailure && idx === serverCount - 1;
                  return (
                    <div
                      key={idx}
                      style={{
                        padding: '10px 16px',
                        background: isDead ? '#450a0a' : '#1e293b',
                        borderRadius: '8px',
                        border: `1px solid ${isDead ? '#ef4444' : '#334155'}`,
                        display: 'flex',
                        alignItems: 'center',
                        gap: 12,
                        minWidth: '220px'
                      }}
                    >
                      <Server size={16} color={isDead ? '#ef4444' : '#10b981'} />
                      <div>
                        <div style={{ fontSize: '0.8rem', fontWeight: 700, color: isDead ? '#fca5a5' : '#f8fafc' }}>
                          App Server #{idx + 1} {isDead ? '(FAILOVER)' : ''}
                        </div>
                        <div style={{ fontSize: '0.7rem', color: '#94a3b8' }}>
                          {isDead ? '0 req/s' : `${loadPerServer} RPS • ${cpuLoad}% CPU`}
                        </div>
                      </div>
                    </div>
                  );
                })}
              </div>
            </div>
          </div>

          {/* Controls */}
          <div className="card" style={{ padding: 20, display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(220px, 1fr))', gap: 16 }}>
            <div>
              <label style={{ fontSize: '0.8rem', color: 'var(--text-muted)' }}>Load Balancing Algorithm</label>
              <select className="input" value={lbAlgorithm} onChange={(e) => setLbAlgorithm(e.target.value)} style={{ marginTop: 4 }}>
                <option value="round-robin">Round Robin (Cyclic Distribution)</option>
                <option value="least-conn">Weighted Least Connections</option>
                <option value="ip-hash">Consistent Client IP Hash</option>
              </select>
            </div>

            <div>
              <div style={{ display: 'flex', justifyContent: 'space-between', fontSize: '0.8rem' }}>
                <span>Traffic: <strong>{rps.toLocaleString()} RPS</strong></span>
              </div>
              <input type="range" min="1000" max="15000" step="1000" value={rps} onChange={(e) => setRps(Number(e.target.value))} style={{ width: '100%', marginTop: 6 }} />
            </div>

            <div style={{ display: 'flex', alignItems: 'flex-end' }}>
              <button onClick={() => setChaosFailure(!chaosFailure)} className={`btn ${chaosFailure ? 'btn-danger' : 'btn-outline'}`} style={{ width: '100%' }}>
                <ShieldAlert size={14} /> {chaosFailure ? 'Recover Node' : 'Inject Chaos Outage'}
              </button>
            </div>
          </div>
        </div>
      )}

      {/* TAB 2: REDIS CACHE ENGINE */}
      {activeTab === 'cache-engine' && (
        <div style={{ display: 'grid', gap: 20 }}>
          <div className="card" style={{ padding: 24, background: '#090d16', border: '1px solid #1e293b' }}>
            <h3 style={{ fontSize: '1.1rem', fontWeight: 700, marginBottom: 16, display: 'flex', alignItems: 'center', gap: 8 }}>
              <Cpu size={18} color="#38bdf8" /> Redis Distributed Caching Architecture
            </h3>

            <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: 20 }}>
              <div style={{ background: '#1e293b', padding: 18, borderRadius: 12, border: '1px solid #334155' }}>
                <div style={{ fontWeight: 700, fontSize: '0.9rem', color: '#38bdf8', marginBottom: 6 }}>Strategy: {cacheStrategy === 'cache-aside' ? 'Cache-Aside (Lazy Loading)' : 'Write-Through'}</div>
                <p style={{ fontSize: '0.8rem', color: '#94a3b8', margin: 0, lineHeight: 1.4 }}>
                  Application checks Redis first. On Cache Miss, fetches from MySQL, writes to Redis with a {cacheTtl}s TTL, and returns.
                </p>
                <div style={{ marginTop: 12, fontSize: '0.85rem' }}>
                  <span>Cache Hit Ratio: <strong style={{ color: '#10b981' }}>{cacheHits}%</strong></span>
                </div>
              </div>

              <div style={{ background: '#1e293b', padding: 18, borderRadius: 12, border: '1px solid #334155' }}>
                <div style={{ fontWeight: 700, fontSize: '0.9rem', color: '#8b5cf6', marginBottom: 6 }}>Cache Stampede Mutex Protection</div>
                <p style={{ fontSize: '0.8rem', color: '#94a3b8', margin: 0, lineHeight: 1.4 }}>
                  Prevents thousands of concurrent threads from hitting the primary database simultaneously during TTL cache expiration.
                </p>
                <div style={{ marginTop: 12, fontSize: '0.85rem' }}>
                  <span>Distributed Lock: <strong style={{ color: cacheMutexLock ? '#10b981' : '#f43f5e' }}>{cacheMutexLock ? 'ENABLED (Redlock)' : 'DISABLED'}</strong></span>
                </div>
              </div>
            </div>
          </div>

          {/* Controls */}
          <div className="card" style={{ padding: 20, display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(220px, 1fr))', gap: 16 }}>
            <div>
              <label style={{ fontSize: '0.8rem', color: 'var(--text-muted)' }}>Caching Pattern</label>
              <select className="input" value={cacheStrategy} onChange={(e) => setCacheStrategy(e.target.value)} style={{ marginTop: 4 }}>
                <option value="cache-aside">Cache-Aside Pattern</option>
                <option value="write-through">Write-Through Pattern</option>
              </select>
            </div>

            <div>
              <div style={{ display: 'flex', justifyContent: 'space-between', fontSize: '0.8rem' }}>
                <span>TTL Expiration: <strong>{cacheTtl}s</strong></span>
              </div>
              <input type="range" min="10" max="300" step="10" value={cacheTtl} onChange={(e) => setCacheTtl(Number(e.target.value))} style={{ width: '100%', marginTop: 6 }} />
            </div>

            <div style={{ display: 'flex', alignItems: 'center' }}>
              <label style={{ display: 'flex', alignItems: 'center', gap: 8, cursor: 'pointer', fontSize: '0.85rem', fontWeight: 600 }}>
                <input type="checkbox" checked={cacheMutexLock} onChange={(e) => setCacheMutexLock(e.target.checked)} />
                <span>Enable Redlock Mutex Lock</span>
              </label>
            </div>
          </div>
        </div>
      )}

      {/* TAB 3: TOKEN BUCKET RATE LIMITER */}
      {activeTab === 'rate-limiter' && (
        <div style={{ display: 'grid', gap: 20 }}>
          <div className="card" style={{ padding: 24, background: '#090d16', border: '1px solid #1e293b' }}>
            <h3 style={{ fontSize: '1.1rem', fontWeight: 700, marginBottom: 16, display: 'flex', alignItems: 'center', gap: 8 }}>
              <Sliders size={18} color="#f59e0b" /> Token Bucket Rate Limiting Engine
            </h3>

            <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: 20, alignItems: 'center' }}>
              <div style={{ background: '#1e293b', padding: 20, borderRadius: 12, border: '1px solid #334155', textAlign: 'center' }}>
                <div style={{ fontSize: '0.8rem', color: '#94a3b8' }}>Available Tokens in Bucket:</div>
                <div style={{ fontSize: '3rem', fontWeight: 800, color: currentTokens > 20 ? '#10b981' : '#f43f5e' }}>
                  {currentTokens} <span style={{ fontSize: '1rem', color: '#94a3b8' }}>/ {bucketCapacity}</span>
                </div>
                <div style={{ height: 8, background: '#090d16', borderRadius: 4, overflow: 'hidden', marginTop: 8 }}>
                  <div style={{ height: '100%', width: `${(currentTokens / bucketCapacity) * 100}%`, background: currentTokens > 20 ? '#10b981' : '#f43f5e', transition: 'width 0.2s ease' }} />
                </div>
              </div>

              <div>
                <div style={{ fontSize: '0.85rem', color: '#94a3b8', marginBottom: 10 }}>
                  Dropped (HTTP 429 Too Many Requests): <strong style={{ color: '#f43f5e' }}>{rateLimitDropped} requests</strong>
                </div>
                <button onClick={triggerBurstRequest} className="btn btn-primary" style={{ width: '100%', padding: '12px', fontWeight: 700 }}>
                  ⚡ Send Burst Traffic ({incomingBurst} reqs)
                </button>
              </div>
            </div>
          </div>

          <div className="card" style={{ padding: 20, display: 'grid', gridTemplateColumns: '1fr 1fr', gap: 16 }}>
            <div>
              <div style={{ display: 'flex', justifyContent: 'space-between', fontSize: '0.8rem' }}>
                <span>Max Bucket Capacity: <strong>{bucketCapacity} tokens</strong></span>
              </div>
              <input type="range" min="50" max="300" step="25" value={bucketCapacity} onChange={(e) => setBucketCapacity(Number(e.target.value))} style={{ width: '100%', marginTop: 6 }} />
            </div>

            <div>
              <div style={{ display: 'flex', justifyContent: 'space-between', fontSize: '0.8rem' }}>
                <span>Refill Rate: <strong>{refillRate} tokens/sec</strong></span>
              </div>
              <input type="range" min="5" max="100" step="5" value={refillRate} onChange={(e) => setRefillRate(Number(e.target.value))} style={{ width: '100%', marginTop: 6 }} />
            </div>
          </div>
        </div>
      )}

      {/* TAB 4: CONSISTENT HASHING RING */}
      {activeTab === 'consistent-hash' && (
        <div style={{ display: 'grid', gap: 20 }}>
          <div className="card" style={{ padding: 24, background: '#090d16', border: '1px solid #1e293b' }}>
            <h3 style={{ fontSize: '1.1rem', fontWeight: 700, marginBottom: 16, display: 'flex', alignItems: 'center', gap: 8 }}>
              <Compass size={18} color="#8b5cf6" /> 360° Consistent Hashing Ring & Sharding
            </h3>

            <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: 20 }}>
              <div style={{ background: '#1e293b', padding: 18, borderRadius: 12, border: '1px solid #334155' }}>
                <div style={{ fontWeight: 700, fontSize: '0.85rem', color: '#8b5cf6', marginBottom: 8 }}>Active Physical Nodes on Ring:</div>
                <div style={{ display: 'flex', flexDirection: 'column', gap: 6 }}>
                  {nodes.map((n, idx) => (
                    <div key={idx} style={{ padding: '6px 12px', background: '#090d16', borderRadius: '6px', fontSize: '0.8rem', color: '#f8fafc', display: 'flex', justifyContent: 'space-between' }}>
                      <span>🖥️ {n}</span>
                      <span style={{ color: '#8b5cf6' }}>{virtualNodesPerNode} Virtual Replicas</span>
                    </div>
                  ))}
                </div>
              </div>

              <div style={{ background: '#1e293b', padding: 18, borderRadius: 12, border: '1px solid #334155' }}>
                <div style={{ fontWeight: 700, fontSize: '0.85rem', color: '#38bdf8', marginBottom: 8 }}>Key Placement Hash Routing:</div>
                <div style={{ display: 'flex', flexDirection: 'column', gap: 6 }}>
                  {sampleKeys.map((k, idx) => (
                    <div key={idx} style={{ padding: '6px 12px', background: '#090d16', borderRadius: '6px', fontSize: '0.8rem', color: '#f8fafc', display: 'flex', justifyContent: 'space-between' }}>
                      <span>🔑 {k.key} ({k.hashAngle}°)</span>
                      <span style={{ color: '#10b981' }}>➔ {k.assignedNode}</span>
                    </div>
                  ))}
                </div>
              </div>
            </div>
          </div>
        </div>
      )}

      {/* TAB 5: CIRCUIT BREAKER */}
      {activeTab === 'circuit-breaker' && (
        <div style={{ display: 'grid', gap: 20 }}>
          <div className="card" style={{ padding: 24, background: '#090d16', border: '1px solid #1e293b' }}>
            <h3 style={{ fontSize: '1.1rem', fontWeight: 700, marginBottom: 16, display: 'flex', alignItems: 'center', gap: 8 }}>
              <ShieldAlert size={18} color="#ec4899" /> Microservice Circuit Breaker State Machine
            </h3>

            <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: 20, alignItems: 'center' }}>
              <div style={{ background: '#1e293b', padding: 20, borderRadius: 12, border: '1px solid #334155', textAlign: 'center' }}>
                <div style={{ fontSize: '0.8rem', color: '#94a3b8' }}>Current Breaker State:</div>
                <div
                  style={{
                    fontSize: '2rem',
                    fontWeight: 800,
                    color: breakerState === 'CLOSED' ? '#10b981' : breakerState === 'OPEN' ? '#f43f5e' : '#f59e0b',
                    margin: '8px 0'
                  }}
                >
                  ● {breakerState}
                </div>
                <div style={{ fontSize: '0.75rem', color: '#94a3b8' }}>
                  Consecutive Upstream Failures: <strong>{failureCount} / {failureThreshold}</strong>
                </div>
              </div>

              <div style={{ display: 'flex', flexDirection: 'column', gap: 10 }}>
                <button onClick={simulateUpstreamFailure} className="btn btn-danger" style={{ padding: '12px', fontWeight: 700 }}>
                  ⚠️ Simulate Upstream API Failure (+1 Error)
                </button>
                <button onClick={resetCircuitBreaker} className="btn btn-outline" style={{ padding: '10px' }}>
                  <RotateCcw size={14} /> Reset Breaker to CLOSED State
                </button>
              </div>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}

