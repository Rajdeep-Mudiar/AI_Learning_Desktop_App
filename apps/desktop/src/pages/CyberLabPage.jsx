import React, { useState, useEffect } from 'react';
import {
  ShieldCheck,
  Lock,
  Unlock,
  Key,
  Terminal,
  AlertTriangle,
  Play,
  RotateCcw,
  Sparkles,
  ShieldAlert,
  Cpu,
  CheckCircle2,
  XCircle,
  Network,
  Eye,
  EyeOff,
  Server,
  Layers,
  Flag,
  FileCode2,
  Sliders
} from 'lucide-react';
import Badge from '../components/common/Badge';

export default function CyberLabPage() {
  const [activeTab, setActiveTab] = useState('crypto'); // 'crypto' | 'sqli' | 'firewall' | 'jwt' | 'password' | 'ctf'

  // ==========================================
  // MODULE 1: CRYPTOGRAPHY & SHA-256 AVALANCHE
  // ==========================================
  const [cryptoPlaintext, setCryptoPlaintext] = useState('Confidential Project');
  const [cryptoKey, setCryptoKey] = useState('Secr3tK3y#2026');
  const [caesarShift, setCaesarShift] = useState(3);
  const [avalancheInput1, setAvalancheInput1] = useState('Security1');
  const [avalancheInput2, setAvalancheInput2] = useState('Security2');

  // Simple Caesar Cipher implementation
  const encodeCaesar = (str, shift) => {
    return str.split('').map(char => {
      const code = char.charCodeAt(0);
      if (code >= 65 && code <= 90) {
        return String.fromCharCode(((code - 65 + shift) % 26) + 65);
      }
      if (code >= 97 && code <= 122) {
        return String.fromCharCode(((code - 97 + shift) % 26) + 97);
      }
      return char;
    }).join('');
  };

  // Pseudo-hash generator for visual demonstration
  const simpleHash = (s) => {
    let hash = 0;
    for (let i = 0; i < s.length; i++) {
      hash = (hash << 5) - hash + s.charCodeAt(i);
      hash |= 0;
    }
    const hex = (hash >>> 0).toString(16).padStart(8, '0');
    // expand to 64 chars
    return (hex + hex + hex + hex + hex + hex + hex + hex).slice(0, 64);
  };

  const hash1 = simpleHash(avalancheInput1);
  const hash2 = simpleHash(avalancheInput2);
  let bitDifferences = 0;
  for (let i = 0; i < hash1.length; i++) {
    if (hash1[i] !== hash2[i]) bitDifferences++;
  }
  const avalanchePct = Math.round((bitDifferences / hash1.length) * 100);

  // ==========================================
  // MODULE 2: SQL INJECTION & XSS SANDBOX
  // ==========================================
  const [sqliInput, setSqliInput] = useState("' OR '1'='1");
  const [usePreparedStatement, setUsePreparedStatement] = useState(false);
  const [xssPayload, setXssPayload] = useState("<script>alert('Cookie Steal')</script>");
  const [enableHtmlEscape, setEnableHtmlEscape] = useState(true);

  const rawSqlQuery = `SELECT * FROM users WHERE username = '${sqliInput}' AND password = '***'`;
  const preparedSqlQuery = `SELECT * FROM users WHERE username = ? AND password = ? [PARAM: "${sqliInput}"]`;
  const isSqliExploited = !usePreparedStatement && (sqliInput.includes("' OR '1'='1") || sqliInput.includes("' OR 1=1") || sqliInput.includes("--"));

  // ==========================================
  // MODULE 3: FIREWALL & PORT SCANNER
  // ==========================================
  const initialPorts = [
    { port: 21, service: 'FTP', status: 'CLOSED', defaultAction: 'DROP' },
    { port: 22, service: 'SSH', status: 'OPEN', defaultAction: 'ALLOW' },
    { port: 80, service: 'HTTP', status: 'OPEN', defaultAction: 'ALLOW' },
    { port: 443, service: 'HTTPS', status: 'OPEN', defaultAction: 'ALLOW' },
    { port: 3306, service: 'MySQL', status: 'FILTERED', defaultAction: 'DROP' },
    { port: 8080, service: 'Admin Web', status: 'CLOSED', defaultAction: 'DROP' },
  ];

  const [firewallRules, setFirewallRules] = useState({
    21: 'DROP',
    22: 'ALLOW',
    80: 'ALLOW',
    443: 'ALLOW',
    3306: 'DROP',
    8080: 'DROP'
  });

  const [scanResults, setScanResults] = useState([]);
  const [isScanning, setIsScanning] = useState(false);

  const runPortScan = async () => {
    setIsScanning(true);
    setScanResults([]);

    for (let p of initialPorts) {
      await new Promise(r => setTimeout(r, 350));
      const rule = firewallRules[p.port];
      let finalState = 'FILTERED / DROPPED';
      let latency = 'Timed Out';

      if (rule === 'ALLOW') {
        finalState = p.status === 'OPEN' ? 'OPEN (SYN-ACK)' : 'CLOSED (RST)';
        latency = `${Math.floor(Math.random() * 15) + 4}ms`;
      }

      setScanResults(prev => [...prev, {
        port: p.port,
        service: p.service,
        rule,
        state: finalState,
        latency
      }]);
    }
    setIsScanning(false);
  };

  // ==========================================
  // MODULE 4: JWT SECURITY ANALYZER
  // ==========================================
  const [jwtHeader, setJwtHeader] = useState({ alg: 'HS256', typ: 'JWT' });
  const [jwtPayload, setJwtPayload] = useState({
    sub: 'usr_882910',
    name: 'Alex Vance',
    role: 'standard_user',
    iat: 1726900000
  });
  const [jwtSecret, setJwtSecret] = useState('super-secret-key-321');
  const [tamperedRole, setTamperedRole] = useState(false);

  const currentRole = tamperedRole ? 'admin' : jwtPayload.role;
  const isSignatureValid = !tamperedRole;

  // ==========================================
  // MODULE 5: PASSWORD ENTROPY & CRACKING
  // ==========================================
  const [passwordInput, setPasswordInput] = useState('Tr0ub4dor&3');
  const [showPassword, setShowPassword] = useState(false);

  const calculateEntropy = (pwd) => {
    let pool = 0;
    if (/[a-z]/.test(pwd)) pool += 26;
    if (/[A-Z]/.test(pwd)) pool += 26;
    if (/[0-9]/.test(pwd)) pool += 10;
    if (/[^a-zA-Z0-9]/.test(pwd)) pool += 32;

    if (pool === 0 || pwd.length === 0) return { bits: 0, poolSize: 0, crackTime: 'Instant' };
    const bits = Math.round(pwd.length * Math.log2(pool));

    let time = 'Instant';
    if (bits > 75) time = 'Hundreds of Centuries';
    else if (bits > 60) time = '450 Years (GPU Cluster)';
    else if (bits > 45) time = '3 Weeks';
    else if (bits > 30) time = '4 Hours';
    else time = 'Under 2 Seconds';

    return { bits, poolSize: pool, crackTime: time };
  };

  const entropyData = calculateEntropy(passwordInput);

  // ==========================================
  // MODULE 6: CTF CHALLENGE DEFENSE
  // ==========================================
  const [ctfAnswer, setCtfAnswer] = useState('');
  const [ctfSolved, setCtfSolved] = useState(false);

  const handleCtfSubmit = () => {
    if (ctfAnswer.trim().toLowerCase() === 'flag{parameterized_queries_win}') {
      setCtfSolved(true);
    } else {
      setCtfSolved(false);
    }
  };

  return (
    <div className="animate-fade-in" style={{ paddingBottom: 'var(--space-2xl)' }}>
      {/* Header */}
      <div style={{ marginBottom: 24, display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', flexWrap: 'wrap', gap: 16 }}>
        <div>
          <div style={{ display: 'flex', alignItems: 'center', gap: 8, marginBottom: 4 }}>
            <Badge variant="teal">Cyber Security Laboratory</Badge>
            <span style={{ fontSize: '0.8rem', color: 'var(--text-muted)' }}>Offensive Attack Mechanics & Defensive Hardening</span>
          </div>
          <h1 style={{ fontSize: '1.75rem', marginBottom: 6 }}>Cyber Security & Defensive Engineering Lab</h1>
          <p style={{ color: 'var(--text-secondary)', fontSize: '0.925rem' }}>
            Experiment with cryptography engines, live vulnerability mitigations, stateful firewalls, token signatures, and CTF challenges.
          </p>
        </div>
      </div>

      {/* Navigation Tabs */}
      <div style={{ display: 'flex', gap: 8, overflowX: 'auto', paddingBottom: 12, marginBottom: 24 }}>
        {[
          { id: 'crypto', label: 'Cryptography & Hashing Studio', icon: Lock },
          { id: 'sqli', label: 'SQLi & OWASP Vulnerabilities', icon: ShieldAlert },
          { id: 'firewall', label: 'Firewall & Port Defense', icon: Network },
          { id: 'jwt', label: 'JWT Token Security Analyzer', icon: Key },
          { id: 'password', label: 'Password Entropy & Hashes', icon: Cpu },
          { id: 'ctf', label: 'CTF Challenge Sandbox', icon: Flag },
        ].map(tab => {
          const Icon = tab.icon;
          const isActive = activeTab === tab.id;
          return (
            <button
              key={tab.id}
              onClick={() => setActiveTab(tab.id)}
              className={isActive ? 'btn btn-primary' : 'btn btn-secondary'}
              style={{
                borderRadius: 999,
                fontSize: '0.85rem',
                padding: '8px 16px',
                display: 'flex',
                alignItems: 'center',
                gap: 8,
                background: isActive ? 'linear-gradient(135deg, #14B8A6, #0D9488)' : undefined,
                border: isActive ? 'none' : undefined
              }}
            >
              <Icon size={16} />
              <span>{tab.label}</span>
            </button>
          );
        })}
      </div>

      {/* ======================================================== */}
      {/* TAB 1: CRYPTOGRAPHY & HASHING STUDIO                     */}
      {/* ======================================================== */}
      {activeTab === 'crypto' && (
        <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: 20 }}>
          {/* Caesar & Symmetric Cipher */}
          <div className="card" style={{ padding: 24 }}>
            <h3 style={{ fontSize: '1.15rem', marginBottom: 6, display: 'flex', alignItems: 'center', gap: 8 }}>
              <Key size={18} style={{ color: '#14B8A6' }} /> Symmetric Cipher & Shift Simulator
            </h3>
            <p style={{ fontSize: '0.82rem', color: 'var(--text-secondary)', marginBottom: 20 }}>
              Symmetric encryption uses a shared mathematical key to transform plaintext into unreadable ciphertext.
            </p>

            <div style={{ display: 'flex', flexDirection: 'column', gap: 14 }}>
              <div>
                <label style={{ fontSize: '0.8rem', fontWeight: 600, display: 'block', marginBottom: 4 }}>Plaintext Message:</label>
                <input
                  type="text"
                  value={cryptoPlaintext}
                  onChange={e => setCryptoPlaintext(e.target.value)}
                  className="input"
                  style={{ width: '100%' }}
                />
              </div>

              <div>
                <div style={{ display: 'flex', justifyContent: 'space-between', fontSize: '0.8rem', marginBottom: 4 }}>
                  <span style={{ fontWeight: 600 }}>Shift / Secret Key Offset: <b>ROT-{caesarShift}</b></span>
                </div>
                <input
                  type="range"
                  min="1"
                  max="25"
                  value={caesarShift}
                  onChange={e => setCaesarShift(parseInt(e.target.value))}
                  style={{ width: '100%' }}
                />
              </div>

              <div style={{ background: '#0b1120', padding: 14, borderRadius: 8, border: '1px solid #1e293b' }}>
                <span style={{ fontSize: '0.72rem', color: '#94a3b8', fontWeight: 700 }}>CIPHERTEXT RESULT:</span>
                <div style={{ fontFamily: 'var(--font-mono)', fontSize: '1.1rem', color: '#38bdf8', marginTop: 4, wordBreak: 'break-all' }}>
                  {encodeCaesar(cryptoPlaintext, caesarShift)}
                </div>
              </div>
            </div>
          </div>

          {/* SHA-256 Avalanche Effect */}
          <div className="card" style={{ padding: 24 }}>
            <h3 style={{ fontSize: '1.15rem', marginBottom: 6, display: 'flex', alignItems: 'center', gap: 8 }}>
              <Sparkles size={18} style={{ color: '#14B8A6' }} /> SHA-256 Avalanche Effect
            </h3>
            <p style={{ fontSize: '0.82rem', color: 'var(--text-secondary)', marginBottom: 20 }}>
              A 1-bit input change causes a dramatic, pseudo-random &gt;50% change in the resulting hash digest.
            </p>

            <div style={{ display: 'flex', flexDirection: 'column', gap: 12 }}>
              <div>
                <label style={{ fontSize: '0.78rem', color: '#94a3b8' }}>Input A:</label>
                <input
                  type="text"
                  value={avalancheInput1}
                  onChange={e => setAvalancheInput1(e.target.value)}
                  className="input"
                  style={{ width: '100%', fontSize: '0.85rem' }}
                />
                <div style={{ fontFamily: 'var(--font-mono)', fontSize: '0.72rem', color: '#a5b4fc', marginTop: 4 }}>
                  Hash A: {hash1}
                </div>
              </div>

              <div>
                <label style={{ fontSize: '0.78rem', color: '#94a3b8' }}>Input B (1 letter diff):</label>
                <input
                  type="text"
                  value={avalancheInput2}
                  onChange={e => setAvalancheInput2(e.target.value)}
                  className="input"
                  style={{ width: '100%', fontSize: '0.85rem' }}
                />
                <div style={{ fontFamily: 'var(--font-mono)', fontSize: '0.72rem', color: '#f43f5e', marginTop: 4 }}>
                  Hash B: {hash2}
                </div>
              </div>

              <div style={{ background: '#0b1120', padding: 12, borderRadius: 8, display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginTop: 8 }}>
                <div>
                  <span style={{ fontSize: '0.72rem', color: '#94a3b8' }}>Avalanche Variance:</span>
                  <div style={{ fontSize: '1.2rem', fontWeight: 800, color: '#10b981' }}>{avalanchePct}% Modified</div>
                </div>
                <Badge variant={avalanchePct >= 45 ? 'green' : 'pink'}>
                  {avalanchePct >= 45 ? 'Strong Cryptographic Diffusion' : 'Low Diffusion'}
                </Badge>
              </div>
            </div>
          </div>
        </div>
      )}

      {/* ======================================================== */}
      {/* TAB 2: SQL INJECTION & OWASP VULNERABILITIES             */}
      {/* ======================================================== */}
      {activeTab === 'sqli' && (
        <div style={{ display: 'grid', gridTemplateColumns: '1fr 340px', gap: 20 }}>
          <div className="card" style={{ padding: 24 }}>
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: 20 }}>
              <div>
                <h3 style={{ fontSize: '1.15rem', marginBottom: 4 }}>SQL Injection (SQLi) Interactive Defense</h3>
                <p style={{ fontSize: '0.85rem', color: 'var(--text-secondary)' }}>
                  Demonstrating how unescaped user inputs alter SQL Abstract Syntax Trees (AST).
                </p>
              </div>

              <div style={{ display: 'flex', alignItems: 'center', gap: 10 }}>
                <span style={{ fontSize: '0.82rem', fontWeight: 600 }}>Mitigation:</span>
                <button
                  onClick={() => setUsePreparedStatement(!usePreparedStatement)}
                  className={usePreparedStatement ? 'btn btn-success btn-sm' : 'btn btn-outline btn-sm'}
                >
                  {usePreparedStatement ? '✔ Parameterized Queries (Safe)' : '✖ Raw Concatenation (Vulnerable)'}
                </button>
              </div>
            </div>

            {/* Attack Payload Input */}
            <div style={{ marginBottom: 20 }}>
              <label style={{ fontSize: '0.85rem', fontWeight: 600, display: 'block', marginBottom: 6 }}>
                Simulated User Login Input (Username field):
              </label>
              <div style={{ display: 'flex', gap: 8 }}>
                <input
                  type="text"
                  value={sqliInput}
                  onChange={e => setSqliInput(e.target.value)}
                  className="input"
                  style={{ flex: 1, fontFamily: 'var(--font-mono)' }}
                />
                <button
                  onClick={() => setSqliInput("' OR '1'='1")}
                  className="btn btn-secondary btn-sm"
                  title="Insert classic SQLi payload"
                >
                  Classic Bypass
                </button>
                <button
                  onClick={() => setSqliInput("admin' --")}
                  className="btn btn-secondary btn-sm"
                  title="Insert comment truncation payload"
                >
                  Comment Out
                </button>
              </div>
            </div>

            {/* Backend Query Execution Preview */}
            <div style={{ background: '#0b1120', borderRadius: 12, padding: 18, border: '1px solid #1e293b', marginBottom: 20 }}>
              <div style={{ fontSize: '0.75rem', color: '#94a3b8', fontWeight: 700, marginBottom: 8 }}>
                DATABASE ENGINE QUERY COMPILATION:
              </div>
              <div style={{ fontFamily: 'var(--font-mono)', fontSize: '0.95rem', color: isSqliExploited ? '#f43f5e' : '#38bdf8', lineHeight: 1.5 }}>
                {usePreparedStatement ? preparedSqlQuery : rawSqlQuery}
              </div>
            </div>

            {/* Attack Status Callout */}
            <div
              style={{
                padding: '16px 20px',
                borderRadius: 10,
                background: isSqliExploited ? 'rgba(244, 63, 94, 0.12)' : 'rgba(16, 185, 129, 0.12)',
                border: isSqliExploited ? '1px solid rgba(244, 63, 94, 0.3)' : '1px solid rgba(16, 185, 129, 0.3)',
                display: 'flex',
                alignItems: 'center',
                gap: 14
              }}
            >
              {isSqliExploited ? (
                <ShieldAlert size={28} style={{ color: '#f43f5e', flexShrink: 0 }} />
              ) : (
                <ShieldCheck size={28} style={{ color: '#10b981', flexShrink: 0 }} />
              )}
              <div>
                <div style={{ fontWeight: 700, color: isSqliExploited ? '#f43f5e' : '#10b981', fontSize: '0.95rem' }}>
                  {isSqliExploited ? 'CRITICAL: Authentication Bypassed!' : 'DEFENDED: Parameter Treated as Literal Data'}
                </div>
                <div style={{ fontSize: '0.82rem', color: 'var(--text-secondary)', marginTop: 2 }}>
                  {isSqliExploited
                    ? "The boolean condition `'1'='1'` evaluates to true for all database records, granting unauthorized root access without password."
                    : 'Prepared statements separate SQL code from user parameters at the protocol level. Malicious syntax cannot alter execution logic.'}
                </div>
              </div>
            </div>
          </div>

          {/* XSS Sanitizer Sidebar */}
          <div className="card" style={{ padding: 20 }}>
            <h4 style={{ fontSize: '0.95rem', marginBottom: 12, display: 'flex', alignItems: 'center', gap: 6 }}>
              <FileCode2 size={16} style={{ color: '#14B8A6' }} /> XSS HTML Entity Encoder
            </h4>
            <div style={{ marginBottom: 14 }}>
              <label style={{ fontSize: '0.78rem', color: 'var(--text-muted)' }}>Raw User Payload:</label>
              <input
                type="text"
                value={xssPayload}
                onChange={e => setXssPayload(e.target.value)}
                className="input"
                style={{ width: '100%', fontSize: '0.82rem', fontFamily: 'var(--font-mono)' }}
              />
            </div>

            <div style={{ background: '#0b1120', padding: 12, borderRadius: 8, fontSize: '0.78rem' }}>
              <div style={{ color: '#94a3b8', marginBottom: 4, fontWeight: 700 }}>SANITIZED OUTPUT:</div>
              <div style={{ color: '#34d399', fontFamily: 'var(--font-mono)', wordBreak: 'break-all' }}>
                {xssPayload.replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;')}
              </div>
            </div>
          </div>
        </div>
      )}

      {/* ======================================================== */}
      {/* TAB 3: FIREWALL & PORT DEFENSE                          */}
      {/* ======================================================== */}
      {activeTab === 'firewall' && (
        <div style={{ display: 'grid', gridTemplateColumns: '1fr 360px', gap: 20 }}>
          <div className="card" style={{ padding: 24 }}>
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: 20 }}>
              <div>
                <h3 style={{ fontSize: '1.15rem', marginBottom: 4 }}>Stateful Packet Inspection (SPI) Firewall</h3>
                <p style={{ fontSize: '0.85rem', color: 'var(--text-secondary)' }}>
                  Configure layer 4 ingress filtering rules for target host <code>192.168.1.100</code>.
                </p>
              </div>

              <button
                onClick={runPortScan}
                disabled={isScanning}
                className="btn btn-primary btn-sm"
                style={{ background: '#14B8A6', border: 'none' }}
              >
                <Play size={14} /> {isScanning ? 'Probing Ports...' : 'Launch SYN Port Scan'}
              </button>
            </div>

            {/* Rules Configuration Table */}
            <div style={{ overflowX: 'auto', marginBottom: 20 }}>
              <table style={{ width: '100%', borderCollapse: 'collapse', fontSize: '0.85rem' }}>
                <thead>
                  <tr style={{ background: 'var(--bg-secondary)', borderBottom: '1px solid var(--border-color)' }}>
                    <th style={{ padding: '10px 14px', textAlign: 'left' }}>Port</th>
                    <th style={{ padding: '10px 14px', textAlign: 'left' }}>Service</th>
                    <th style={{ padding: '10px 14px', textAlign: 'left' }}>Underlying Daemon</th>
                    <th style={{ padding: '10px 14px', textAlign: 'center' }}>Firewall Policy</th>
                  </tr>
                </thead>
                <tbody>
                  {initialPorts.map((p) => {
                    const rule = firewallRules[p.port];
                    return (
                      <tr key={p.port} style={{ borderBottom: '1px solid var(--border-subtle)' }}>
                        <td style={{ padding: '10px 14px', fontFamily: 'var(--font-mono)', fontWeight: 700, color: '#38bdf8' }}>
                          {p.port}/TCP
                        </td>
                        <td style={{ padding: '10px 14px', fontWeight: 600 }}>{p.service}</td>
                        <td style={{ padding: '10px 14px', color: p.status === 'OPEN' ? '#10b981' : '#94a3b8' }}>
                          {p.status === 'OPEN' ? 'Listening' : 'Inactive'}
                        </td>
                        <td style={{ padding: '10px 14px', textAlign: 'center' }}>
                          <button
                            onClick={() => setFirewallRules(r => ({ ...r, [p.port]: r[p.port] === 'ALLOW' ? 'DROP' : 'ALLOW' }))}
                            className={rule === 'ALLOW' ? 'btn btn-success btn-sm' : 'btn btn-secondary btn-sm'}
                            style={{ padding: '3px 12px', fontSize: '0.75rem' }}
                          >
                            {rule}
                          </button>
                        </td>
                      </tr>
                    );
                  })}
                </tbody>
              </table>
            </div>
          </div>

          {/* Scanner Output Terminal */}
          <div className="card" style={{ padding: 20 }}>
            <h4 style={{ fontSize: '0.95rem', marginBottom: 12, display: 'flex', alignItems: 'center', gap: 6 }}>
              <Terminal size={16} style={{ color: '#14B8A6' }} /> Nmap SYN Scan Probe Log
            </h4>

            <div style={{ background: '#0b1120', borderRadius: 8, padding: 12, height: '260px', overflowY: 'auto', fontFamily: 'var(--font-mono)', fontSize: '0.78rem', display: 'flex', flexDirection: 'column', gap: 6 }}>
              <div style={{ color: '#64748b' }}>$ nmap -sS -Pn 192.168.1.100</div>
              {scanResults.map((r, i) => (
                <div key={i} style={{ color: r.state.includes('OPEN') ? '#34d399' : '#94a3b8' }}>
                  &gt; Port {r.port} ({r.service}): {r.state} [{r.latency}]
                </div>
              ))}
              {scanResults.length === initialPorts.length && (
                <div style={{ color: '#38bdf8', marginTop: 8 }}>✔ Nmap done: 6 IP addresses scanned.</div>
              )}
            </div>
          </div>
        </div>
      )}

      {/* ======================================================== */}
      {/* TAB 4: JWT SECURITY ANALYZER                             */}
      {/* ======================================================== */}
      {activeTab === 'jwt' && (
        <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: 20 }}>
          <div className="card" style={{ padding: 24 }}>
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: 16 }}>
              <h3 style={{ fontSize: '1.15rem' }}>JSON Web Token (JWT) Structure</h3>
              <button
                onClick={() => setTamperedRole(!tamperedRole)}
                className={tamperedRole ? 'btn btn-primary btn-sm' : 'btn btn-secondary btn-sm'}
                style={{ background: tamperedRole ? '#f43f5e' : undefined, border: 'none' }}
              >
                {tamperedRole ? 'Tampered: Role Escalated to Admin' : 'Tamper Payload Role'}
              </button>
            </div>

            {/* Colorized Token Segments */}
            <div style={{ background: '#0b1120', padding: 16, borderRadius: 10, border: '1px solid #1e293b', marginBottom: 20 }}>
              <span style={{ color: '#f43f5e', fontFamily: 'var(--font-mono)', fontSize: '0.85rem', wordBreak: 'break-all' }}>
                eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9
              </span>
              <span style={{ color: '#ffffff' }}>.</span>
              <span style={{ color: '#c084fc', fontFamily: 'var(--font-mono)', fontSize: '0.85rem', wordBreak: 'break-all' }}>
                {tamperedRole ? 'eyJzdWIiOiJ1c3JfODgyOTEwIiwicm9sZSI6ImFkbWluIn0' : 'eyJzdWIiOiJ1c3JfODgyOTEwIiwicm9sZSI6InVzZXIifQ'}
              </span>
              <span style={{ color: '#ffffff' }}>.</span>
              <span style={{ color: '#38bdf8', fontFamily: 'var(--font-mono)', fontSize: '0.85rem', wordBreak: 'break-all' }}>
                db9c7a2164f9104fa28e19e7bc1
              </span>
            </div>

            {/* Signature Verification State */}
            <div
              style={{
                padding: '14px 18px',
                borderRadius: 8,
                background: isSignatureValid ? 'rgba(16, 185, 129, 0.15)' : 'rgba(244, 63, 94, 0.15)',
                border: isSignatureValid ? '1px solid #10b981' : '1px solid #f43f5e',
                display: 'flex',
                alignItems: 'center',
                gap: 12
              }}
            >
              {isSignatureValid ? <CheckCircle2 size={20} color="#10b981" /> : <XCircle size={20} color="#f43f5e" />}
              <div>
                <div style={{ fontWeight: 700, color: isSignatureValid ? '#10b981' : '#f43f5e', fontSize: '0.9rem' }}>
                  {isSignatureValid ? 'Signature Verified (Authentic Token)' : 'INVALID SIGNATURE: Token Was Tampered!'}
                </div>
                <span style={{ fontSize: '0.78rem', color: 'var(--text-secondary)' }}>
                  {isSignatureValid ? 'HMAC-SHA256 signature matches payload.' : 'Server rejects request: signature does not match tampered payload.'}
                </span>
              </div>
            </div>
          </div>

          {/* Decoded Payload Explorer */}
          <div className="card" style={{ padding: 24 }}>
            <h3 style={{ fontSize: '1.15rem', marginBottom: 12 }}>Decoded Claims</h3>
            <div style={{ background: '#0b1120', borderRadius: 8, padding: 14, fontFamily: 'var(--font-mono)', fontSize: '0.85rem', color: '#f8fafc' }}>
              <div><span style={{ color: '#f43f5e' }}>HEADER:</span> {JSON.stringify(jwtHeader)}</div>
              <div style={{ marginTop: 10 }}>
                <span style={{ color: '#c084fc' }}>PAYLOAD:</span>{' '}
                {JSON.stringify({ ...jwtPayload, role: currentRole }, null, 2)}
              </div>
              <div style={{ marginTop: 10 }}><span style={{ color: '#38bdf8' }}>SECRET:</span> "{jwtSecret}"</div>
            </div>
          </div>
        </div>
      )}

      {/* ======================================================== */}
      {/* TAB 5: PASSWORD ENTROPY & HASHE                          */}
      {/* ======================================================== */}
      {activeTab === 'password' && (
        <div style={{ display: 'grid', gridTemplateColumns: '1fr 340px', gap: 20 }}>
          <div className="card" style={{ padding: 24 }}>
            <h3 style={{ fontSize: '1.15rem', marginBottom: 4 }}>Password Entropy Calculator</h3>
            <p style={{ fontSize: '0.85rem', color: 'var(--text-secondary)', marginBottom: 20 }}>
              Entropy equation: <code>E = L × log₂(R)</code> where L is length and R is character set size.
            </p>

            <div style={{ marginBottom: 20 }}>
              <label style={{ fontSize: '0.85rem', fontWeight: 600, display: 'block', marginBottom: 6 }}>
                Test Password String:
              </label>
              <div style={{ display: 'flex', gap: 8 }}>
                <input
                  type={showPassword ? 'text' : 'password'}
                  value={passwordInput}
                  onChange={e => setPasswordInput(e.target.value)}
                  className="input"
                  style={{ flex: 1, fontFamily: 'var(--font-mono)' }}
                />
                <button
                  onClick={() => setShowPassword(!showPassword)}
                  className="btn btn-secondary btn-sm"
                >
                  {showPassword ? <EyeOff size={16} /> : <Eye size={16} />}
                </button>
              </div>
            </div>

            {/* Metrics */}
            <div style={{ display: 'grid', gridTemplateColumns: 'repeat(3, 1fr)', gap: 12 }}>
              <div style={{ background: '#0b1120', padding: 14, borderRadius: 8, textAlign: 'center' }}>
                <span style={{ fontSize: '0.75rem', color: '#94a3b8' }}>Entropy Bits</span>
                <div style={{ fontSize: '1.4rem', fontWeight: 800, color: '#14B8A6' }}>{entropyData.bits} bits</div>
              </div>
              <div style={{ background: '#0b1120', padding: 14, borderRadius: 8, textAlign: 'center' }}>
                <span style={{ fontSize: '0.75rem', color: '#94a3b8' }}>Character Pool (R)</span>
                <div style={{ fontSize: '1.4rem', fontWeight: 800, color: '#38bdf8' }}>{entropyData.poolSize} chars</div>
              </div>
              <div style={{ background: '#0b1120', padding: 14, borderRadius: 8, textAlign: 'center' }}>
                <span style={{ fontSize: '0.75rem', color: '#94a3b8' }}>Crack Time (8x RTX 4090)</span>
                <div style={{ fontSize: '1.1rem', fontWeight: 800, color: entropyData.bits > 60 ? '#10b981' : '#f43f5e' }}>
                  {entropyData.crackTime}
                </div>
              </div>
            </div>
          </div>

          <div className="card" style={{ padding: 20 }}>
            <h4 style={{ fontSize: '0.95rem', marginBottom: 12 }}>Salted Hashing vs Rainbow Tables</h4>
            <p style={{ fontSize: '0.82rem', color: 'var(--text-secondary)', lineHeight: 1.6 }}>
              A <b>Salt</b> is a unique 128-bit cryptographic random string prepended before hashing (e.g. <code>SHA256(password + salt)</code>).
              <br /><br />
              Salting guarantees that two users with identical passwords have completely distinct hashes, completely neutralizing precomputed rainbow table attacks.
            </p>
          </div>
        </div>
      )}

      {/* ======================================================== */}
      {/* TAB 6: CTF CHALLENGE SANDBOX                            */}
      {/* ======================================================== */}
      {activeTab === 'ctf' && (
        <div className="card" style={{ padding: 24, maxWidth: '780px', margin: '0 auto' }}>
          <div style={{ display: 'flex', alignItems: 'center', gap: 10, marginBottom: 14 }}>
            <Flag size={24} style={{ color: '#14B8A6' }} />
            <div>
              <h3 style={{ fontSize: '1.25rem' }}>Challenge: Mitigate the SQL Injection Vulnerability</h3>
              <span style={{ fontSize: '0.8rem', color: 'var(--text-muted)' }}>Difficulty: Intermediate | 100 Points</span>
            </div>
          </div>

          <div style={{ background: '#0b1120', padding: 16, borderRadius: 10, border: '1px solid #1e293b', marginBottom: 20 }}>
            <p style={{ fontSize: '0.88rem', color: '#e2e8f0', lineHeight: 1.6, marginBottom: 12 }}>
              <b>Scenario:</b> A web backend is running raw queries. What is the fundamental defensive technique in database drivers (e.g. PDO, SQLAlchemy, pg) that passes input as literal data parameters instead of concatenating strings?
            </p>
            <div style={{ fontSize: '0.78rem', color: '#94a3b8' }}>
              Hint: Format as <code>flag&#123;parameterized_queries_win&#125;</code>
            </div>
          </div>

          <div style={{ display: 'flex', gap: 10, marginBottom: 16 }}>
            <input
              type="text"
              value={ctfAnswer}
              onChange={e => setCtfAnswer(e.target.value)}
              placeholder="flag{...}"
              className="input"
              style={{ flex: 1, fontFamily: 'var(--font-mono)' }}
            />
            <button onClick={handleCtfSubmit} className="btn btn-primary" style={{ background: '#14B8A6', border: 'none' }}>
              Submit Flag
            </button>
          </div>

          {ctfSolved && (
            <div style={{ background: 'rgba(16, 185, 129, 0.15)', border: '1px solid #10b981', padding: 16, borderRadius: 10, display: 'flex', alignItems: 'center', gap: 12 }}>
              <CheckCircle2 size={24} color="#10b981" />
              <div>
                <div style={{ fontWeight: 700, color: '#10b981' }}>Flag Solved! +100 Points</div>
                <div style={{ fontSize: '0.82rem', color: 'var(--text-secondary)' }}>
                  You successfully mastered database input parameterization and defensive tokenization.
                </div>
              </div>
            </div>
          )}
        </div>
      )}
    </div>
  );
}
