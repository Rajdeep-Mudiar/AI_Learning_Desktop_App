import React, { useState, useEffect } from 'react';
import Editor from '@monaco-editor/react';
import {
  Globe,
  Play,
  RotateCcw,
  Sparkles,
  Layout,
  Code2,
  Eye,
  Maximize2,
  CheckCircle2,
  Layers,
  Palette,
  Sliders,
  Cpu,
  Zap,
  Activity,
  Box
} from 'lucide-react';
import Badge from '../components/common/Badge';

const WEB_SIMULATION_PRESETS = {
  'basics-counter': {
    id: 'basics-counter',
    level: 'Basics (Level 1)',
    levelColor: '#10b981',
    title: '1. DOM & Reactive State Counter',
    description: 'DOM manipulation, event listeners, dynamic style updates, and state thresholds.',
    html: `<div class="card">
  <div class="badge">Basics • Level 1</div>
  <h2>⚡ Reactive State Counter</h2>
  <p>Learn event bubbling, listeners, and DOM updates.</p>
  <div class="counter-display" id="count">0</div>
  <div class="stats-row">
    <span>Status: <strong id="status-label">Neutral</strong></span>
    <span>Clicks: <strong id="click-count">0</strong></span>
  </div>
  <div class="button-group">
    <button id="dec" class="btn btn-secondary">- Decrement</button>
    <button id="reset" class="btn btn-outline">Reset</button>
    <button id="inc" class="btn btn-primary">+ Increment</button>
  </div>
</div>`,
    css: `body {
  font-family: system-ui, -apple-system, sans-serif;
  background: #090d16;
  color: #f8fafc;
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 90vh;
  margin: 0;
}
.card {
  background: #131b2e;
  padding: 2.5rem;
  border-radius: 1.25rem;
  box-shadow: 0 20px 30px -10px rgba(0, 0, 0, 0.6);
  text-align: center;
  max-width: 420px;
  border: 1px solid #1e293b;
}
.badge {
  display: inline-block;
  background: rgba(16, 185, 129, 0.15);
  color: #10b981;
  padding: 4px 10px;
  border-radius: 20px;
  font-size: 0.75rem;
  font-weight: 700;
  margin-bottom: 0.75rem;
}
h2 { margin: 0 0 0.5rem 0; color: #38bdf8; font-size: 1.5rem; }
p { color: #94a3b8; font-size: 0.9rem; margin: 0 0 1.5rem 0; }
.counter-display {
  font-size: 4.5rem;
  font-weight: 800;
  margin: 1rem 0;
  color: #38bdf8;
  font-variant-numeric: tabular-nums;
  transition: transform 0.15s ease, color 0.2s ease;
}
.stats-row {
  display: flex;
  justify-content: space-around;
  font-size: 0.85rem;
  color: #94a3b8;
  margin-bottom: 1.5rem;
  padding: 8px;
  background: #090d16;
  border-radius: 8px;
}
.stats-row strong { color: #f8fafc; }
.button-group {
  display: flex;
  gap: 0.75rem;
  justify-content: center;
}
.btn {
  padding: 0.65rem 1.25rem;
  border-radius: 0.5rem;
  border: none;
  font-weight: 600;
  cursor: pointer;
  transition: transform 0.1s, opacity 0.2s;
}
.btn:active { transform: scale(0.95); }
.btn-primary { background: #38bdf8; color: #090d16; }
.btn-secondary { background: #334155; color: #f8fafc; }
.btn-outline { background: transparent; border: 1px solid #475569; color: #cbd5e1; }`,
    js: `let count = 0;
let totalClicks = 0;
const display = document.getElementById('count');
const statusLabel = document.getElementById('status-label');
const clickDisplay = document.getElementById('click-count');

function updateUI() {
  display.textContent = count;
  clickDisplay.textContent = totalClicks;
  display.style.transform = 'scale(1.15)';
  setTimeout(() => display.style.transform = 'scale(1)', 150);

  if (count > 0) {
    display.style.color = '#38bdf8';
    statusLabel.textContent = 'Positive (Surplus)';
    statusLabel.style.color = '#38bdf8';
  } else if (count < 0) {
    display.style.color = '#f43f5e';
    statusLabel.textContent = 'Negative (Deficit)';
    statusLabel.style.color = '#f43f5e';
  } else {
    display.style.color = '#f8fafc';
    statusLabel.textContent = 'Neutral';
    statusLabel.style.color = '#94a3b8';
  }
}

document.getElementById('inc').addEventListener('click', () => {
  count++;
  totalClicks++;
  updateUI();
});

document.getElementById('dec').addEventListener('click', () => {
  count--;
  totalClicks++;
  updateUI();
});

document.getElementById('reset').addEventListener('click', () => {
  count = 0;
  totalClicks++;
  updateUI();
});`
  },

  'intermediate-flexgrid': {
    id: 'intermediate-flexgrid',
    level: 'Intermediate (Level 2)',
    levelColor: '#38bdf8',
    title: '2. CSS Grid & Glassmorphic Dashboard',
    description: 'Auto-fit grid layouts, backdrop filters, CSS custom variables, and responsive navigation.',
    html: `<div class="dashboard">
  <div class="badge">Intermediate • Level 2</div>
  <header class="header">
    <div class="logo">🚀 DevMetrics Studio</div>
    <div class="user-chip">Logged in as <strong>Admin</strong></div>
  </header>

  <div class="metrics-grid">
    <div class="metric-card">
      <div class="metric-title">Active Users</div>
      <div class="metric-value">24,580</div>
      <div class="metric-trend up">↑ +14.2% this week</div>
    </div>
    <div class="metric-card">
      <div class="metric-title">Server Response</div>
      <div class="metric-value">42 ms</div>
      <div class="metric-trend up">⚡ Optimized Edge</div>
    </div>
    <div class="metric-card">
      <div class="metric-title">Error Rate</div>
      <div class="metric-value">0.02%</div>
      <div class="metric-trend down">↓ -0.05% improvement</div>
    </div>
  </div>

  <div class="action-panel">
    <h3>Quick System Actions</h3>
    <div class="button-row">
      <button class="glass-btn" onclick="alert('Cache purged!')">Purge CDN Cache</button>
      <button class="glass-btn" onclick="alert('Logs exported!')">Export JSON Logs</button>
      <button class="glass-btn highlight" onclick="alert('Deploying hotfix...')">Deploy Hotfix</button>
    </div>
  </div>
</div>`,
    css: `body {
  font-family: system-ui, sans-serif;
  background: radial-gradient(circle at top right, #1e1b4b, #090d16);
  color: #fff;
  margin: 0;
  padding: 2rem;
  display: flex;
  justify-content: center;
}
.dashboard {
  max-width: 750px;
  width: 100%;
}
.badge {
  display: inline-block;
  background: rgba(56, 189, 248, 0.15);
  color: #38bdf8;
  padding: 4px 10px;
  border-radius: 20px;
  font-size: 0.75rem;
  font-weight: 700;
  margin-bottom: 1rem;
}
.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1.25rem 1.5rem;
  background: rgba(30, 41, 59, 0.6);
  backdrop-filter: blur(12px);
  border-radius: 14px;
  border: 1px solid rgba(255, 255, 255, 0.1);
  margin-bottom: 1.5rem;
}
.logo { font-weight: 800; font-size: 1.15rem; color: #38bdf8; }
.user-chip { font-size: 0.85rem; color: #94a3b8; }
.metrics-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 1.25rem;
  margin-bottom: 1.5rem;
}
.metric-card {
  background: rgba(19, 27, 46, 0.7);
  backdrop-filter: blur(10px);
  padding: 1.5rem;
  border-radius: 14px;
  border: 1px solid #1e293b;
  transition: transform 0.2s, border-color 0.2s;
}
.metric-card:hover {
  transform: translateY(-4px);
  border-color: #38bdf8;
}
.metric-title { font-size: 0.8rem; color: #94a3b8; text-transform: uppercase; letter-spacing: 0.5px; }
.metric-value { font-size: 2rem; font-weight: 800; color: #f8fafc; margin: 6px 0; }
.metric-trend { font-size: 0.75rem; font-weight: 600; }
.metric-trend.up { color: #10b981; }
.metric-trend.down { color: #38bdf8; }
.action-panel {
  background: rgba(30, 41, 59, 0.5);
  padding: 1.5rem;
  border-radius: 14px;
  border: 1px solid #1e293b;
}
.action-panel h3 { margin: 0 0 1rem 0; font-size: 1rem; color: #cbd5e1; }
.button-row { display: flex; gap: 10px; flex-wrap: wrap; }
.glass-btn {
  padding: 0.6rem 1.2rem;
  border-radius: 8px;
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid rgba(255, 255, 255, 0.15);
  color: #e2e8f0;
  cursor: pointer;
  font-weight: 600;
  transition: all 0.2s;
}
.glass-btn:hover { background: rgba(255, 255, 255, 0.12); color: #fff; }
.glass-btn.highlight { background: #6366f1; border-color: #6366f1; }
.glass-btn.highlight:hover { background: #4f46e5; }`,
    js: `console.log('Glassmorphic CSS Grid Dashboard loaded successfully.');`
  },

  'advanced-async-stream': {
    id: 'advanced-async-stream',
    level: 'Advanced (Level 3)',
    levelColor: '#f59e0b',
    title: '3. Async REST API & Real-Time Filter Engine',
    description: 'Async/await data streaming, debounced live searching, simulated network latency, and error states.',
    html: `<div class="app-container">
  <div class="badge">Advanced • Level 3</div>
  <h2>🌐 Async API Query & Filter Stream</h2>
  
  <div class="search-bar">
    <input type="text" id="filter-input" placeholder="Type to filter packages (e.g., 'react', 'fastapi', 'tailwind')..." />
    <button id="refresh-btn" class="btn">🔄 Fetch Remote Data</button>
  </div>

  <div id="status-bar" class="status-bar">Ready. Click Fetch or search.</div>

  <div id="results-list" class="results-grid">
    <!-- Populated dynamically by async JS -->
  </div>
</div>`,
    css: `body {
  font-family: system-ui, sans-serif;
  background: #090d16;
  color: #f8fafc;
  padding: 2rem;
  display: flex;
  justify-content: center;
}
.app-container { max-width: 720px; width: 100%; }
.badge {
  display: inline-block;
  background: rgba(245, 158, 11, 0.15);
  color: #f59e0b;
  padding: 4px 10px;
  border-radius: 20px;
  font-size: 0.75rem;
  font-weight: 700;
  margin-bottom: 0.5rem;
}
h2 { margin: 0 0 1rem 0; color: #f8fafc; }
.search-bar { display: flex; gap: 10px; margin-bottom: 1rem; }
input {
  flex: 1;
  padding: 0.75rem 1rem;
  background: #131b2e;
  border: 1px solid #1e293b;
  border-radius: 8px;
  color: #fff;
  outline: none;
  font-size: 0.9rem;
}
input:focus { border-color: #38bdf8; }
.btn {
  padding: 0.75rem 1.2rem;
  background: #38bdf8;
  color: #090d16;
  font-weight: 700;
  border: none;
  border-radius: 8px;
  cursor: pointer;
}
.status-bar {
  font-size: 0.8rem;
  color: #94a3b8;
  margin-bottom: 1.25rem;
  padding: 8px 12px;
  background: #131b2e;
  border-radius: 6px;
  border-left: 3px solid #38bdf8;
}
.results-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
  gap: 1rem;
}
.card-item {
  background: #131b2e;
  padding: 1.2rem;
  border-radius: 10px;
  border: 1px solid #1e293b;
  transition: transform 0.15s;
}
.card-item:hover { transform: translateY(-2px); border-color: #38bdf8; }
.pkg-name { font-weight: 700; font-size: 0.95rem; color: #38bdf8; margin-bottom: 4px; }
.pkg-desc { font-size: 0.8rem; color: #94a3b8; line-height: 1.3; }
.pkg-stars { font-size: 0.75rem; color: #fbbf24; margin-top: 8px; }`,
    js: `const MOCK_PACKAGES = [
  { name: 'react', desc: 'The library for web and native user interfaces', stars: '228k' },
  { name: 'fastapi', desc: 'High performance, easy to learn, fast to code Python framework', stars: '75k' },
  { name: 'tailwindcss', desc: 'A utility-first CSS framework for rapid UI development', stars: '81k' },
  { name: 'vite', desc: 'Next Generation Frontend Tooling with instant HMR', stars: '67k' },
  { name: 'monaco-editor', desc: 'The code editor that powers VS Code in the browser', stars: '38k' },
  { name: 'zustand', desc: 'Bear necessities for state management in React', stars: '45k' }
];

const resultsContainer = document.getElementById('results-list');
const statusBar = document.getElementById('status-bar');
const filterInput = document.getElementById('filter-input');
const refreshBtn = document.getElementById('refresh-btn');

async function simulateFetch(query = '') {
  statusBar.textContent = '⏳ Streaming data over HTTP/3... (Simulating 400ms network roundtrip)';
  statusBar.style.borderLeftColor = '#f59e0b';
  resultsContainer.innerHTML = '<div style="color: #94a3b8">Loading packets...</div>';

  await new Promise(r => setTimeout(r, 400));

  const filtered = MOCK_PACKAGES.filter(p => 
    p.name.toLowerCase().includes(query.toLowerCase()) || 
    p.desc.toLowerCase().includes(query.toLowerCase())
  );

  renderPackages(filtered);
  statusBar.textContent = \`✅ Fetched \${filtered.length} package(s) matching '\${query}'. Response Time: 412ms\`;
  statusBar.style.borderLeftColor = '#10b981';
}

function renderPackages(list) {
  if (list.length === 0) {
    resultsContainer.innerHTML = '<div style="color: #f43f5e">No packages matched your query.</div>';
    return;
  }
  resultsContainer.innerHTML = list.map(pkg => \`
    <div class="card-item">
      <div class="pkg-name">📦 \${pkg.name}</div>
      <div class="pkg-desc">\${pkg.desc}</div>
      <div class="pkg-stars">★ \${pkg.stars} GitHub stars</div>
    </div>
  \`).join('');
}

filterInput.addEventListener('input', (e) => {
  simulateFetch(e.target.value);
});

refreshBtn.addEventListener('click', () => {
  filterInput.value = '';
  simulateFetch('');
});

simulateFetch('');`
  },

  'advanced-physics-canvas': {
    id: 'advanced-physics-canvas',
    level: 'Advanced (Level 4)',
    levelColor: '#ec4899',
    title: '4. Canvas 2D Physics Particle Simulation',
    description: 'Interactive HTML5 Canvas, collision vectors, mouse gravitational repulsion, and velocity physics.',
    html: `<div class="canvas-wrapper">
  <div class="header-row">
    <div>
      <div class="badge">Advanced • Level 4</div>
      <h2>🪐 Interactive 2D Physics & Gravity Simulator</h2>
    </div>
    <div class="controls">
      <button id="add-btn" class="btn">+ Add 50 Particles</button>
      <button id="clear-btn" class="btn btn-outline">Clear Canvas</button>
    </div>
  </div>
  <p class="subtitle">Move your mouse over the canvas to exert kinetic gravity repulsion forces.</p>
  <canvas id="sim-canvas" width="680" height="380"></canvas>
</div>`,
    css: `body {
  font-family: system-ui, sans-serif;
  background: #090d16;
  color: #fff;
  padding: 1.5rem;
  display: flex;
  justify-content: center;
  margin: 0;
}
.canvas-wrapper { max-width: 720px; width: 100%; }
.badge {
  display: inline-block;
  background: rgba(236, 72, 153, 0.15);
  color: #ec4899;
  padding: 4px 10px;
  border-radius: 20px;
  font-size: 0.75rem;
  font-weight: 700;
  margin-bottom: 0.25rem;
}
h2 { margin: 0; font-size: 1.25rem; color: #f8fafc; }
.subtitle { font-size: 0.85rem; color: #94a3b8; margin: 6px 0 14px 0; }
.header-row { display: flex; justify-content: space-between; align-items: center; }
.controls { display: flex; gap: 8px; }
.btn {
  padding: 0.5rem 1rem;
  background: #ec4899;
  color: #fff;
  border: none;
  border-radius: 6px;
  font-weight: 600;
  cursor: pointer;
  font-size: 0.8rem;
}
.btn-outline { background: transparent; border: 1px solid #475569; color: #cbd5e1; }
#sim-canvas {
  background: #0f172a;
  border: 1px solid #1e293b;
  border-radius: 12px;
  box-shadow: 0 10px 25px -5px rgba(0,0,0,0.5);
  display: block;
  cursor: crosshair;
}`,
    js: `const canvas = document.getElementById('sim-canvas');
const ctx = canvas.getContext('2d');

let particles = [];
const colors = ['#38bdf8', '#ec4899', '#10b981', '#fbbf24', '#818cf8'];

let mouse = { x: -1000, y: -1000, radius: 90 };

canvas.addEventListener('mousemove', (e) => {
  const rect = canvas.getBoundingClientRect();
  mouse.x = e.clientX - rect.left;
  mouse.y = e.clientY - rect.top;
});

canvas.addEventListener('mouseleave', () => {
  mouse.x = -1000;
  mouse.y = -1000;
});

class Particle {
  constructor(x, y) {
    this.x = x || Math.random() * canvas.width;
    this.y = y || Math.random() * canvas.height;
    this.vx = (Math.random() - 0.5) * 3;
    this.vy = (Math.random() - 0.5) * 3;
    this.radius = Math.random() * 4 + 2;
    this.color = colors[Math.floor(Math.random() * colors.length)];
  }

  update() {
    this.x += this.vx;
    this.y += this.vy;

    if (this.x < this.radius || this.x > canvas.width - this.radius) this.vx *= -1;
    if (this.y < this.radius || this.y > canvas.height - this.radius) this.vy *= -1;

    // Mouse repulsion
    const dx = this.x - mouse.x;
    const dy = this.y - mouse.y;
    const dist = Math.sqrt(dx * dx + dy * dy);

    if (dist < mouse.radius) {
      const force = (mouse.radius - dist) / mouse.radius;
      const angle = Math.atan2(dy, dx);
      this.x += Math.cos(angle) * force * 6;
      this.y += Math.sin(angle) * force * 6;
    }
  }

  draw() {
    ctx.beginPath();
    ctx.arc(this.x, this.y, this.radius, 0, Math.PI * 2);
    ctx.fillStyle = this.color;
    ctx.shadowColor = this.color;
    ctx.shadowBlur = 8;
    ctx.fill();
    ctx.shadowBlur = 0;
  }
}

function init(count = 80) {
  for (let i = 0; i < count; i++) {
    particles.push(new Particle());
  }
}

function animate() {
  ctx.fillStyle = 'rgba(15, 23, 42, 0.25)';
  ctx.fillRect(0, 0, canvas.width, canvas.height);

  particles.forEach(p => {
    p.update();
    p.draw();
  });

  requestAnimationFrame(animate);
}

document.getElementById('add-btn').addEventListener('click', () => init(50));
document.getElementById('clear-btn').addEventListener('click', () => particles = []);

init(100);
animate();`
  },

  'advanced-pubsub-bus': {
    id: 'advanced-pubsub-bus',
    level: 'Architecture (Level 5)',
    levelColor: '#8b5cf6',
    title: '5. Micro-Frontend State Bus (Pub/Sub)',
    description: 'Decoupled component communication via custom JavaScript event bus with live action telemetry.',
    html: `<div class="container">
  <div class="badge">Architecture • Level 5</div>
  <h2>⚡ Decoupled Micro-Frontend Event Bus</h2>
  <p class="subtitle">Emit and subscribe to reactive system events across isolated UI components.</p>

  <div class="grid">
    <!-- Component A: Cart Publisher -->
    <div class="card">
      <div class="card-tag">Component A (Catalog)</div>
      <h4>🛍️ Product Store</h4>
      <button class="btn" onclick="EventBus.publish('CART_ADD', { item: 'MacBook Pro M3', price: 1999 })">+ Buy MacBook ($1999)</button>
      <button class="btn" onclick="EventBus.publish('CART_ADD', { item: 'Wireless Keyboard', price: 99 })">+ Buy Keyboard ($99)</button>
    </div>

    <!-- Component B: Notification Subscriber -->
    <div class="card">
      <div class="card-tag">Component B (Header)</div>
      <h4>🛒 Live Cart Summary</h4>
      <div class="cart-box">
        <div>Items Count: <strong id="cart-count">0</strong></div>
        <div>Total Value: <strong id="cart-total">$0</strong></div>
      </div>
    </div>
  </div>

  <!-- Component C: Event Audit Stream -->
  <div class="audit-card">
    <h4>📡 Event Bus Audit Log (Real-Time Telemetry)</h4>
    <div id="log-stream" class="log-stream">
      <div class="log-entry system">[SYSTEM] EventBus initialized. Listening for topic broadcasts...</div>
    </div>
  </div>
</div>`,
    css: `body {
  font-family: system-ui, sans-serif;
  background: #090d16;
  color: #fff;
  padding: 1.5rem;
  margin: 0;
  display: flex;
  justify-content: center;
}
.container { max-width: 720px; width: 100%; }
.badge {
  display: inline-block;
  background: rgba(139, 92, 246, 0.15);
  color: #8b5cf6;
  padding: 4px 10px;
  border-radius: 20px;
  font-size: 0.75rem;
  font-weight: 700;
  margin-bottom: 0.25rem;
}
h2 { margin: 0; font-size: 1.3rem; color: #f8fafc; }
.subtitle { font-size: 0.85rem; color: #94a3b8; margin: 4px 0 16px 0; }
.grid { display: grid; grid-template-columns: 1fr 1fr; gap: 14px; margin-bottom: 16px; }
.card {
  background: #131b2e;
  padding: 1.25rem;
  border-radius: 12px;
  border: 1px solid #1e293b;
  position: relative;
}
.card-tag { font-size: 0.7rem; color: #8b5cf6; font-weight: 700; text-transform: uppercase; margin-bottom: 6px; }
h4 { margin: 0 0 12px 0; font-size: 0.95rem; color: #38bdf8; }
.btn {
  display: block;
  width: 100%;
  margin-bottom: 8px;
  padding: 8px 12px;
  background: #1e293b;
  border: 1px solid #334155;
  color: #f8fafc;
  border-radius: 6px;
  cursor: pointer;
  font-size: 0.8rem;
  font-weight: 600;
  transition: all 0.15s;
}
.btn:hover { background: #8b5cf6; border-color: #8b5cf6; }
.cart-box { background: #090d16; padding: 12px; border-radius: 8px; font-size: 0.85rem; display: flex; flex-direction: column; gap: 6px; }
.cart-box strong { color: #10b981; }
.audit-card {
  background: #0f172a;
  border: 1px solid #1e293b;
  border-radius: 12px;
  padding: 1.25rem;
}
.log-stream {
  background: #090d16;
  border-radius: 8px;
  padding: 10px;
  font-family: monospace;
  font-size: 0.75rem;
  max-height: 140px;
  overflow-y: auto;
  display: flex;
  flex-direction: column;
  gap: 4px;
}
.log-entry { color: #38bdf8; }
.log-entry.system { color: #94a3b8; }`,
    js: `// Pub/Sub Event Bus Implementation
window.EventBus = {
  topics: {},
  subscribe(topic, listener) {
    if (!this.topics[topic]) this.topics[topic] = [];
    this.topics[topic].push(listener);
  },
  publish(topic, data) {
    logEvent(topic, data);
    if (!this.topics[topic]) return;
    this.topics[topic].forEach(listener => listener(data));
  }
};

let cart = [];
const countDisplay = document.getElementById('cart-count');
const totalDisplay = document.getElementById('cart-total');
const logStream = document.getElementById('log-stream');

function logEvent(topic, data) {
  const div = document.createElement('div');
  div.className = 'log-entry';
  div.textContent = \`[\${new Date().toLocaleTimeString()}] TOPIC: '\${topic}' => \${JSON.stringify(data)}\`;
  logStream.prepend(div);
}

// Subscriber
EventBus.subscribe('CART_ADD', (payload) => {
  cart.push(payload);
  countDisplay.textContent = cart.length;
  const total = cart.reduce((acc, cur) => acc + cur.price, 0);
  totalDisplay.textContent = \`$\${total}\`;
});`
  }
};

export default function WebDevLabPage() {
  const [selectedPreset, setSelectedPreset] = useState('basics-counter');
  const [activeTab, setActiveTab] = useState('html');
  const [htmlCode, setHtmlCode] = useState(WEB_SIMULATION_PRESETS['basics-counter'].html);
  const [cssCode, setCssCode] = useState(WEB_SIMULATION_PRESETS['basics-counter'].css);
  const [jsCode, setJsCode] = useState(WEB_SIMULATION_PRESETS['basics-counter'].js);
  const [previewSrcDoc, setPreviewSrcDoc] = useState('');

  // Update preview when code changes
  useEffect(() => {
    const combined = `
      <!DOCTYPE html>
      <html>
        <head>
          <style>${cssCode}</style>
        </head>
        <body>
          ${htmlCode}
          <script>
            try {
              ${jsCode}
            } catch (err) {
              console.error(err);
            }
          </script>
        </body>
      </html>
    `;
    setPreviewSrcDoc(combined);
  }, [htmlCode, cssCode, jsCode]);

  const loadPreset = (key) => {
    setSelectedPreset(key);
    setHtmlCode(WEB_SIMULATION_PRESETS[key].html);
    setCssCode(WEB_SIMULATION_PRESETS[key].css);
    setJsCode(WEB_SIMULATION_PRESETS[key].js);
  };

  const currentPreset = WEB_SIMULATION_PRESETS[selectedPreset];

  return (
    <div className="animate-fade-in" style={{ paddingBottom: 40 }}>
      {/* Header */}
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', flexWrap: 'wrap', gap: 16, marginBottom: 20 }}>
        <div>
          <div style={{ display: 'flex', alignItems: 'center', gap: 10, marginBottom: 6 }}>
            <Badge variant="blue"><Globe size={14} /> Web Engineering Sandbox</Badge>
            <span style={{ fontSize: '0.85rem', color: 'var(--text-muted)' }}>Interactive Multi-Level Web Lab</span>
          </div>
          <h1 style={{ fontSize: '1.85rem', fontWeight: 800 }}>Web Dev Interactive Simulations</h1>
          <p style={{ color: 'var(--text-secondary)', fontSize: '0.95rem' }}>
            Explore progressive simulations from basic DOM reactiveness to high-performance Canvas 2D physics and Micro-Frontend state architecture.
          </p>
        </div>
      </div>

      {/* Simulation Selector Level Cards */}
      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(220px, 1fr))', gap: 12, marginBottom: 20 }}>
        {Object.entries(WEB_SIMULATION_PRESETS).map(([key, item]) => {
          const isActive = selectedPreset === key;
          return (
            <button
              key={key}
              onClick={() => loadPreset(key)}
              style={{
                background: isActive ? 'var(--bg-card)' : 'var(--bg-tertiary)',
                border: isActive ? `2px solid ${item.levelColor}` : '1px solid var(--border-color)',
                padding: '12px 14px',
                borderRadius: '12px',
                textAlign: 'left',
                cursor: 'pointer',
                transition: 'all 0.15s ease',
                boxShadow: isActive ? `0 4px 14px ${item.levelColor}25` : 'none'
              }}
            >
              <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: 4 }}>
                <span style={{ fontSize: '0.7rem', fontWeight: 700, color: item.levelColor, textTransform: 'uppercase' }}>
                  {item.level}
                </span>
                {isActive && <CheckCircle2 size={14} color={item.levelColor} />}
              </div>
              <div style={{ fontSize: '0.85rem', fontWeight: 700, color: 'var(--text-primary)', marginBottom: 2 }}>
                {item.title}
              </div>
              <div style={{ fontSize: '0.75rem', color: 'var(--text-muted)', lineHeight: 1.3 }}>
                {item.description}
              </div>
            </button>
          );
        })}
      </div>

      {/* Main Split Grid: Editor (Left) & Live Preview (Right) */}
      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(420px, 1fr))', gap: 20 }}>
        {/* Editor Panel */}
        <div className="card" style={{ padding: 0, overflow: 'hidden', display: 'flex', flexDirection: 'column', height: '620px' }}>
          {/* Tab Bar */}
          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', background: 'var(--bg-tertiary)', borderBottom: '1px solid var(--border-color)', padding: '6px 12px' }}>
            <div style={{ display: 'flex', gap: 6 }}>
              <button
                onClick={() => setActiveTab('html')}
                className={`btn btn-sm ${activeTab === 'html' ? 'btn-primary' : 'btn-ghost'}`}
                style={{ borderRadius: 6, gap: 6 }}
              >
                <Code2 size={14} /> index.html
              </button>
              <button
                onClick={() => setActiveTab('css')}
                className={`btn btn-sm ${activeTab === 'css' ? 'btn-primary' : 'btn-ghost'}`}
                style={{ borderRadius: 6, gap: 6 }}
              >
                <Palette size={14} /> style.css
              </button>
              <button
                onClick={() => setActiveTab('js')}
                className={`btn btn-sm ${activeTab === 'js' ? 'btn-primary' : 'btn-ghost'}`}
                style={{ borderRadius: 6, gap: 6 }}
              >
                <Sparkles size={14} /> app.js
              </button>
            </div>

            <button
              onClick={() => loadPreset(selectedPreset)}
              className="btn btn-ghost btn-sm"
              style={{ padding: '4px 8px', fontSize: '0.75rem', gap: 4 }}
              title="Reset code to default"
            >
              <RotateCcw size={12} /> Reset
            </button>
          </div>

          {/* Monaco Editor */}
          <div style={{ flex: 1 }}>
            {activeTab === 'html' && (
              <Editor
                height="100%"
                language="html"
                theme="vs-dark"
                value={htmlCode}
                onChange={(val) => setHtmlCode(val || '')}
                options={{ minimap: { enabled: false }, fontSize: 13, wordWrap: 'on' }}
              />
            )}
            {activeTab === 'css' && (
              <Editor
                height="100%"
                language="css"
                theme="vs-dark"
                value={cssCode}
                onChange={(val) => setCssCode(val || '')}
                options={{ minimap: { enabled: false }, fontSize: 13, wordWrap: 'on' }}
              />
            )}
            {activeTab === 'js' && (
              <Editor
                height="100%"
                language="javascript"
                theme="vs-dark"
                value={jsCode}
                onChange={(val) => setJsCode(val || '')}
                options={{ minimap: { enabled: false }, fontSize: 13, wordWrap: 'on' }}
              />
            )}
          </div>
        </div>

        {/* Live Preview Panel */}
        <div className="card" style={{ padding: 0, overflow: 'hidden', display: 'flex', flexDirection: 'column', height: '620px' }}>
          {/* Header Bar */}
          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', background: 'var(--bg-tertiary)', borderBottom: '1px solid var(--border-color)', padding: '8px 16px' }}>
            <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
              <span style={{ width: 10, height: 10, borderRadius: '50%', background: '#10b981' }} />
              <span style={{ fontSize: '0.85rem', fontWeight: 600, color: 'var(--text-secondary)' }}>Live Interactive Preview</span>
            </div>
            <span style={{ fontSize: '0.75rem', color: 'var(--text-muted)' }}>Hot-reloaded sandbox</span>
          </div>

          {/* Iframe View */}
          <iframe
            title="Web Sandbox Live Preview"
            srcDoc={previewSrcDoc}
            style={{ width: '100%', height: '100%', border: 'none', background: '#ffffff' }}
            sandbox="allow-scripts"
          />
        </div>
      </div>
    </div>
  );
}

