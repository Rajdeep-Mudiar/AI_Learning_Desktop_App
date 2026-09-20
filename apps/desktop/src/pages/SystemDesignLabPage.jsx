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
  HardDrive
} from 'lucide-react';
import Badge from '../components/common/Badge';

export default function SystemDesignLabPage() {
  const [rps, setRps] = useState(2500); // Requests per second
  const [cacheEnabled, setCacheEnabled] = useState(true);
  const [serverCount, setServerCount] = useState(3);
  const [dbReplicas, setDbReplicas] = useState(2);
  const [chaosFailure, setChaosFailure] = useState(false); // Simulated server outage

  // Derived dynamic metrics
  const activeServers = chaosFailure ? Math.max(1, serverCount - 1) : serverCount;
  const loadPerServer = Math.round(rps / activeServers);
  const cacheHitRatio = cacheEnabled ? 88 : 0;
  const dbQueriesPerSec = cacheEnabled ? Math.round(rps * 0.12) : rps;
  const cpuLoad = Math.min(100, Math.round((loadPerServer / 2000) * 100));
  const latencyMs = Math.round(
    (cacheEnabled ? 8 : 45) + (cpuLoad > 85 ? (cpuLoad - 85) * 4 : 0) + (chaosFailure ? 35 : 0)
  );
  const isOverloaded = cpuLoad > 90;

  return (
    <div className="animate-fade-in" style={{ paddingBottom: 40 }}>
      {/* Header */}
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', flexWrap: 'wrap', gap: 16, marginBottom: 24 }}>
        <div>
          <div style={{ display: 'flex', alignItems: 'center', gap: 10, marginBottom: 6 }}>
            <Badge variant="green"><Layers size={14} /> System Architecture Lab</Badge>
            <span style={{ fontSize: '0.85rem', color: 'var(--text-muted)' }}>High-Scale Distributed Simulator</span>
          </div>
          <h1 style={{ fontSize: '1.85rem', fontWeight: 800 }}>Scalable Distributed System Simulator</h1>
          <p style={{ color: 'var(--text-secondary)', fontSize: '0.95rem' }}>
            Experiment with Load Balancers, Redis Caching, Microservices autoscaling, and database replication under real-time traffic spikes.
          </p>
        </div>
      </div>

      {/* Top Metrics Row */}
      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(200px, 1fr))', gap: 16, marginBottom: 24 }}>
        <div className="card" style={{ padding: 18, borderLeft: '4px solid #10b981' }}>
          <div style={{ fontSize: '0.8rem', color: 'var(--text-muted)', marginBottom: 4 }}>Incoming Traffic</div>
          <div style={{ fontSize: '1.6rem', fontWeight: 800, color: '#10b981' }}>{rps.toLocaleString()} <span style={{ fontSize: '0.9rem', color: 'var(--text-muted)' }}>RPS</span></div>
        </div>

        <div className="card" style={{ padding: 18, borderLeft: `4px solid ${latencyMs > 50 ? '#f43f5e' : '#38bdf8'}` }}>
          <div style={{ fontSize: '0.8rem', color: 'var(--text-muted)', marginBottom: 4 }}>P99 Latency</div>
          <div style={{ fontSize: '1.6rem', fontWeight: 800, color: latencyMs > 50 ? '#f43f5e' : '#38bdf8' }}>
            {latencyMs} <span style={{ fontSize: '0.9rem', color: 'var(--text-muted)' }}>ms</span>
          </div>
        </div>

        <div className="card" style={{ padding: 18, borderLeft: '4px solid #8b5cf6' }}>
          <div style={{ fontSize: '0.8rem', color: 'var(--text-muted)', marginBottom: 4 }}>Redis Cache Hit Rate</div>
          <div style={{ fontSize: '1.6rem', fontWeight: 800, color: '#8b5cf6' }}>{cacheHitRatio}%</div>
        </div>

        <div className="card" style={{ padding: 18, borderLeft: `4px solid ${isOverloaded ? '#f43f5e' : '#eab308'}` }}>
          <div style={{ fontSize: '0.8rem', color: 'var(--text-muted)', marginBottom: 4 }}>App Server CPU Load</div>
          <div style={{ fontSize: '1.6rem', fontWeight: 800, color: isOverloaded ? '#f43f5e' : '#eab308' }}>
            {cpuLoad}% {isOverloaded && '⚠️'}
          </div>
        </div>
      </div>

      {/* Main Architecture Visual Canvas */}
      <div className="card" style={{ padding: 28, marginBottom: 24, position: 'relative', background: '#090d16', border: '1px solid #1e293b' }}>
        <h3 style={{ fontSize: '1.1rem', fontWeight: 700, marginBottom: 24, display: 'flex', alignItems: 'center', gap: 8 }}>
          <Activity size={18} color="#10b981" /> Live Architecture Topology
        </h3>

        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', flexWrap: 'wrap', gap: 20 }}>
          {/* 1. Client Tier */}
          <div style={{ textAlign: 'center', padding: '16px 20px', background: '#1e293b', borderRadius: '14px', border: '1px solid #334155', minWidth: '130px' }}>
            <div style={{ fontSize: '1.8rem', marginBottom: 4 }}>👥</div>
            <div style={{ fontWeight: 700, fontSize: '0.85rem' }}>Clients / Apps</div>
            <div style={{ fontSize: '0.75rem', color: '#10b981', marginTop: 4 }}>{rps} req/sec</div>
          </div>

          <div style={{ color: '#64748b', fontSize: '1.2rem' }}>➔</div>

          {/* 2. Load Balancer */}
          <div style={{ textAlign: 'center', padding: '16px 20px', background: '#1e293b', borderRadius: '14px', border: '1px solid #38bdf8', minWidth: '150px' }}>
            <Zap size={28} color="#38bdf8" style={{ margin: '0 auto 6px' }} />
            <div style={{ fontWeight: 700, fontSize: '0.85rem' }}>Nginx Load Balancer</div>
            <div style={{ fontSize: '0.7rem', color: '#94a3b8' }}>Round-Robin</div>
          </div>

          <div style={{ color: '#64748b', fontSize: '1.2rem' }}>➔</div>

          {/* 3. Microservice App Cluster */}
          <div style={{ display: 'flex', flexDirection: 'column', gap: 10 }}>
            {Array.from({ length: serverCount }).map((_, idx) => {
              const isDead = chaosFailure && idx === serverCount - 1;
              return (
                <div
                  key={idx}
                  style={{
                    padding: '10px 18px',
                    background: isDead ? '#450a0a' : '#1e293b',
                    borderRadius: '10px',
                    border: `1px solid ${isDead ? '#ef4444' : '#334155'}`,
                    display: 'flex',
                    alignItems: 'center',
                    gap: 12,
                    minWidth: '200px'
                  }}
                >
                  <Server size={18} color={isDead ? '#ef4444' : '#10b981'} />
                  <div>
                    <div style={{ fontSize: '0.8rem', fontWeight: 700, color: isDead ? '#fca5a5' : '#f8fafc' }}>
                      App Server #{idx + 1} {isDead ? '(OUTAGE)' : ''}
                    </div>
                    <div style={{ fontSize: '0.7rem', color: '#94a3b8' }}>
                      {isDead ? '0 RPS' : `${loadPerServer} RPS • ${cpuLoad}% CPU`}
                    </div>
                  </div>
                </div>
              );
            })}
          </div>

          <div style={{ color: '#64748b', fontSize: '1.2rem' }}>➔</div>

          {/* 4. Cache & Database Tier */}
          <div style={{ display: 'flex', flexDirection: 'column', gap: 14 }}>
            {/* Redis Cache */}
            <div
              style={{
                padding: '12px 18px',
                background: cacheEnabled ? '#1e293b' : '#0f172a',
                borderRadius: '12px',
                border: `1px solid ${cacheEnabled ? '#8b5cf6' : '#334155'}`,
                opacity: cacheEnabled ? 1 : 0.4
              }}
            >
              <div style={{ display: 'flex', alignItems: 'center', gap: 8, marginBottom: 4 }}>
                <Cpu size={16} color="#8b5cf6" />
                <span style={{ fontWeight: 700, fontSize: '0.8rem' }}>Redis Distributed Cache</span>
              </div>
              <div style={{ fontSize: '0.7rem', color: '#94a3b8' }}>
                {cacheEnabled ? `88% Hits • ~1ms Latency` : 'Bypassed (0% Hits)'}
              </div>
            </div>

            {/* Primary & Replica DBs */}
            <div style={{ padding: '12px 18px', background: '#1e293b', borderRadius: '12px', border: '1px solid #334155' }}>
              <div style={{ display: 'flex', alignItems: 'center', gap: 8, marginBottom: 4 }}>
                <Database size={16} color="#f59e0b" />
                <span style={{ fontWeight: 700, fontSize: '0.8rem' }}>Primary DB + {dbReplicas} Replicas</span>
              </div>
              <div style={{ fontSize: '0.7rem', color: '#f59e0b' }}>
                {dbQueriesPerSec} queries/sec (Writes & Misses)
              </div>
            </div>
          </div>
        </div>
      </div>

      {/* Control Panel: Knobs, Sliders & Chaos Engineering */}
      <div className="card" style={{ padding: 24 }}>
        <h3 style={{ fontSize: '1.1rem', fontWeight: 700, marginBottom: 20, display: 'flex', alignItems: 'center', gap: 8 }}>
          <Sliders size={18} /> System Controls & Chaos Engineering
        </h3>

        <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(240px, 1fr))', gap: 24 }}>
          {/* Traffic Slider */}
          <div>
            <div style={{ display: 'flex', justifyContent: 'space-between', marginBottom: 8, fontSize: '0.85rem' }}>
              <span>Traffic Load (RPS)</span>
              <strong>{rps.toLocaleString()} RPS</strong>
            </div>
            <input
              type="range"
              min="500"
              max="20000"
              step="500"
              value={rps}
              onChange={(e) => setRps(Number(e.target.value))}
              style={{ width: '100%', cursor: 'pointer' }}
            />
          </div>

          {/* Server Count Slider */}
          <div>
            <div style={{ display: 'flex', justifyContent: 'space-between', marginBottom: 8, fontSize: '0.85rem' }}>
              <span>App Servers (Autoscale)</span>
              <strong>{serverCount} Nodes</strong>
            </div>
            <input
              type="range"
              min="1"
              max="6"
              value={serverCount}
              onChange={(e) => setServerCount(Number(e.target.value))}
              style={{ width: '100%', cursor: 'pointer' }}
            />
          </div>

          {/* Cache Toggle */}
          <div style={{ display: 'flex', flexDirection: 'column', justifyContent: 'center' }}>
            <label style={{ display: 'flex', alignItems: 'center', gap: 10, cursor: 'pointer', fontSize: '0.9rem', fontWeight: 600 }}>
              <input
                type="checkbox"
                checked={cacheEnabled}
                onChange={(e) => setCacheEnabled(e.target.checked)}
              />
              <span>Enable Redis Caching Layer</span>
            </label>
            <p style={{ fontSize: '0.75rem', color: 'var(--text-muted)', margin: '4px 0 0 24px' }}>
              Buffers 88% of read queries from overloading the primary database.
            </p>
          </div>

          {/* Chaos Injection Button */}
          <div style={{ display: 'flex', alignItems: 'center' }}>
            <button
              onClick={() => setChaosFailure(!chaosFailure)}
              className={`btn ${chaosFailure ? 'btn-danger' : 'btn-outline'}`}
              style={{ width: '100%', padding: '10px 16px', gap: 8, borderRadius: 10 }}
            >
              <ShieldAlert size={16} />
              <span>{chaosFailure ? 'Recover Failed Server' : 'Inject Server Outage (Chaos)'}</span>
            </button>
          </div>
        </div>
      </div>
    </div>
  );
}
