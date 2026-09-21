import React, { useState, useEffect, useRef } from 'react';
import { tutorService } from '../services/tutorService';
import { useDomain } from '../contexts/DomainContext';
import ChatMessageBubble from '../components/tutor/ChatMessageBubble';
import TutorContextSelector from '../components/tutor/TutorContextSelector';
import TutorSettingsDrawer from '../components/tutor/TutorSettingsDrawer';
import { Send, Sparkles, Settings as SettingsIcon, Trash2, Bot, Cpu } from 'lucide-react';

export default function TutorPage() {
  const { currentDomain, activeDomainInfo } = useDomain();
  const [messages, setMessages] = useState([]);
  const [inputPrompt, setInputPrompt] = useState('');
  const [loading, setLoading] = useState(false);
  const [activeMode, setActiveMode] = useState('socratic'); // 'socratic' | 'explain_mistake' | 'math_derivation' | 'code_review'

  // Persistent Settings
  const [showSettings, setShowSettings] = useState(false);
  const [provider, setProvider] = useState(() => localStorage.getItem('ai_tutor_provider') || 'auto');
  const [modelName, setModelName] = useState(() => localStorage.getItem('ai_tutor_model') || 'llama3.2:1b');
  const [ollamaUrl, setOllamaUrl] = useState(() => localStorage.getItem('ai_tutor_ollama_url') || 'http://localhost:11434');
  const [apiKey, setApiKey] = useState(() => localStorage.getItem('ai_tutor_api_key') || '');
  const [apiBase, setApiBase] = useState(() => localStorage.getItem('ai_tutor_api_base') || '');
  
  const [modelsList, setModelsList] = useState([]);
  const [isOllamaOnline, setIsOllamaOnline] = useState(false);
  const [refreshingModels, setRefreshingModels] = useState(false);

  // Context State
  const [context, setContext] = useState({
    current_lesson_title: null,
    current_lesson_slug: null,
    active_code: null,
    active_error: null,
    recent_quiz_mistake: null,
  });

  const [presets, setPresets] = useState({
    modes: [],
    quick_questions: [],
  });

  const chatEndRef = useRef(null);

  useEffect(() => {
    localStorage.setItem('ai_tutor_provider', provider);
  }, [provider]);

  useEffect(() => {
    localStorage.setItem('ai_tutor_model', modelName);
  }, [modelName]);

  useEffect(() => {
    localStorage.setItem('ai_tutor_ollama_url', ollamaUrl);
  }, [ollamaUrl]);

  useEffect(() => {
    localStorage.setItem('ai_tutor_api_key', apiKey);
  }, [apiKey]);

  useEffect(() => {
    localStorage.setItem('ai_tutor_api_base', apiBase);
  }, [apiBase]);

  useEffect(() => {
    loadPresets();
    loadModels();
  }, []);

  useEffect(() => {
    chatEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [messages, loading]);

  const loadPresets = async () => {
    try {
      const data = await tutorService.getPresets();
      setPresets(data);
    } catch (err) {
      console.error(err);
    }
  };

  const loadModels = async () => {
    try {
      setRefreshingModels(true);
      const data = await tutorService.getModels(ollamaUrl);
      setModelsList(data.available_models || []);
      setIsOllamaOnline(data.is_ollama_online);
      if (data.default_model) {
        // If current model isn't set or not available, use the online default
        const names = (data.available_models || []).map((m) => m.name);
        if (!modelName || !names.includes(modelName)) {
          setModelName(data.default_model);
        }
      }
    } catch (err) {
      console.error(err);
    } finally {
      setRefreshingModels(false);
    }
  };

  const DOMAIN_QUESTIONS = {
    'all': [
      "Explain the event loop and microtask queues in JavaScript",
      "How does backpropagation calculate weight gradients?",
      "Design a scalable distributed rate-limiter with Redis & Token Bucket",
      "What is the difference between git merge --squash and git rebase?"
    ],
    'dsa': [
      "How do Two Pointers optimize Two Sum in a sorted array to O(N)?",
      "Explain why Binary Search Tree In-order traversal gives sorted order",
      "How do I formulate the DP state recurrence for 0/1 Knapsack?",
      "Compare the time and space complexity of QuickSort vs MergeSort"
    ],
    'cybersecurity': [
      "How do Prepared Statements eliminate SQL Injection vulnerabilities?",
      "Explain how the SHA-256 Avalanche Effect guarantees integrity",
      "What is the difference between Symmetric (AES) and Asymmetric (RSA) encryption?",
      "How does Cross-Site Scripting (XSS) steal session cookies and how does CSP stop it?"
    ],
    'web-dev': [
      "How does React 18 Concurrent Mode work under the hood?",
      "Explain CSS Stacking Contexts and z-index calculation",
      "How to prevent CSRF and XSS in modern full-stack web apps?",
      "What is the difference between SSR, SSG, and ISR in Next.js?"
    ],
    'app-dev': [
      "How does Flutter's rendering pipeline (Widget, Element, RenderObject) work?",
      "Explain the differences between React Native Fabric renderer and the old bridge",
      "How to optimize 60/120 FPS scrolling performance on mobile devices?",
      "What are best practices for offline-first data sync in mobile apps?"
    ],
    'system-design': [
      "Design a globally distributed URL shortener (TinyURL) handling 100k QPS",
      "Explain CAP Theorem vs PACELC Theorem with real-world database examples",
      "How do distributed consensus algorithms (Raft / Paxos) achieve leader election?",
      "Design an idempotent payment processing pipeline with at-least-once messaging"
    ],
    'github': [
      "What is the difference between git reset --soft, --mixed, and --hard?",
      "How do you resolve complex merge conflicts in interactive rebasing?",
      "Design a GitHub Actions CI/CD matrix build with automated caching and deployment",
      "Explain Git internals: Blobs, Trees, Commits, and Annotated Tags"
    ],
    'ai-ml': [
      "Why does Scaled Dot-Product Attention divide by √d_k?",
      "Derive the Ordinary Least Squares (OLS) Normal Equation",
      "Why did my gradient explode to NaN during training?",
      "What is the mathematical difference between Gini Impurity and Entropy?"
    ]
  };

  const quickQuestions = DOMAIN_QUESTIONS[currentDomain] || DOMAIN_QUESTIONS['all'];

  const handleSendMessage = async (textToSend) => {
    const text = (textToSend || inputPrompt).trim();
    if (!text || loading) return;

    const userMsg = {
      role: 'user',
      content: text,
      timestamp: new Date().toISOString(),
    };

    const newHistory = [...messages, userMsg];
    setMessages(newHistory);
    setInputPrompt('');
    setLoading(true);

    try {
      const payload = {
        message: text,
        history: messages.map((m) => ({ role: m.role, content: m.content })),
        mode: activeMode,
        provider,
        model_name: modelName,
        ollama_base_url: ollamaUrl,
        api_key: apiKey || undefined,
        api_base: apiBase || undefined,
        context: {
          ...context,
          active_domain: currentDomain,
          student_level: 'intermediate',
        },
      };

      const res = await tutorService.chat(payload);

      const botMsg = {
        role: 'assistant',
        content: res.response,
        metadata: res,
        timestamp: new Date().toISOString(),
      };

      setMessages((prev) => [...prev, botMsg]);
    } catch (err) {
      const errorMsg = {
        role: 'assistant',
        content: `⚠️ Failed to connect to AI tutor: ${err.message || 'Unknown error occurred.'}`,
        timestamp: new Date().toISOString(),
      };
      setMessages((prev) => [...prev, errorMsg]);
    } finally {
      setLoading(false);
    }
  };

  const handleKeyDown = (e) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      handleSendMessage();
    }
  };

  const handleClearChat = () => {
    setMessages([]);
  };

  const MODES_CONFIG = [
    { id: 'socratic', name: 'Socratic Guide', icon: '🦉', desc: 'Prompts with questions & intuition' },
    { id: 'explain_mistake', name: 'Explain My Mistake', icon: '🔍', desc: 'Pinpoints flawed code/logic' },
    { id: 'math_derivation', name: 'Architecture & Proofs', icon: '📐', desc: 'Step-by-step logic & diagrams' },
    { id: 'code_review', name: 'Code Review', icon: '⚡', desc: 'Performance, clean code & security checks' },
  ];

  return (
    <div className="container" style={{ height: 'calc(100vh - 100px)', display: 'flex', flexDirection: 'column' }}>
      {/* Header & Mode Bar */}
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: 'var(--space-md)' }}>
        <div>
          <h1 style={{ fontSize: 'var(--font-xl)', fontWeight: 800, margin: '0 0 2px 0', color: 'var(--color-text-main)', display: 'flex', alignItems: 'center', gap: '8px' }}>
            <Sparkles size={20} color="var(--color-primary-400)" /> Context-Aware {activeDomainInfo?.label || 'Engineering'} AI Tutor
          </h1>
          <p style={{ margin: 0, color: 'var(--color-text-muted)', fontSize: 'var(--font-xs)' }}>
            Grounded in your active {activeDomainInfo?.label || 'engineering'} lessons, coding playground, and diagnostic challenges.
          </p>
        </div>

        <div style={{ display: 'flex', gap: 'var(--space-xs)', alignItems: 'center' }}>
          {messages.length > 0 && (
            <button onClick={handleClearChat} className="btn btn-secondary" style={{ padding: '6px 10px', fontSize: 'var(--font-xs)' }} title="Clear Chat History">
              <Trash2 size={14} />
            </button>
          )}
          <button onClick={() => setShowSettings(true)} className="btn btn-secondary" style={{ padding: '6px 12px', fontSize: 'var(--font-xs)', display: 'flex', alignItems: 'center', gap: '6px' }}>
            <SettingsIcon size={14} />
            <span>{isOllamaOnline ? `Ollama: ${modelName || 'Online'}` : 'AI Settings'}</span>
          </button>
        </div>
      </div>

      {/* Mode Selector Tabs */}
      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(4, 1fr)', gap: 'var(--space-sm)', marginBottom: 'var(--space-md)' }}>
        {MODES_CONFIG.map((m) => {
          const isActive = activeMode === m.id;
          return (
            <button
              key={m.id}
              onClick={() => setActiveMode(m.id)}
              style={{
                padding: '8px 12px',
                borderRadius: 'var(--radius-md)',
                background: isActive ? 'rgba(99, 102, 241, 0.15)' : 'var(--color-surface)',
                border: isActive ? '1.5px solid var(--color-primary-400)' : '1px solid var(--color-border)',
                display: 'flex',
                alignItems: 'center',
                gap: '8px',
                cursor: 'pointer',
                textAlign: 'left',
                transition: 'all 0.15s ease',
              }}
            >
              <span style={{ fontSize: '18px' }}>{m.icon}</span>
              <div style={{ overflow: 'hidden' }}>
                <div style={{ fontSize: 'var(--font-xs)', fontWeight: isActive ? 700 : 500, color: isActive ? 'var(--color-primary-400)' : 'var(--color-text-main)', whiteSpace: 'nowrap' }}>
                  {m.name}
                </div>
                <div style={{ fontSize: '10px', color: 'var(--color-text-muted)', overflow: 'hidden', textOverflow: 'ellipsis', whiteSpace: 'nowrap' }}>
                  {m.desc}
                </div>
              </div>
            </button>
          );
        })}
      </div>

      {/* Chat Messages Scroll Area */}
      <div
        style={{
          flex: 1,
          overflowY: 'auto',
          padding: 'var(--space-md)',
          background: 'var(--color-surface)',
          borderRadius: 'var(--radius-lg)',
          border: '1px solid var(--color-border)',
          display: 'flex',
          flexDirection: 'column',
          gap: 'var(--space-md)',
          marginBottom: 'var(--space-sm)',
        }}
      >
        {messages.length === 0 ? (
          <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center', height: '100%', textAlign: 'center', color: 'var(--color-text-muted)', gap: 'var(--space-md)' }}>
            <div style={{ width: '56px', height: '56px', borderRadius: '50%', background: 'rgba(99, 102, 241, 0.12)', display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
              <Bot size={28} color="var(--color-primary-400)" />
            </div>
            <div>
              <h3 style={{ margin: '0 0 4px', fontSize: 'var(--font-md)', color: 'var(--color-text-main)' }}>
                Ask Your {activeDomainInfo?.label || 'Engineering'} AI Tutor
              </h3>
              <p style={{ margin: 0, fontSize: 'var(--font-xs)', maxWidth: '440px' }}>
                Ask conceptual questions, request architectural proofs, or paste errors from your coding playground.
              </p>
            </div>

            {/* Quick Prompts */}
            <div style={{ display: 'flex', flexDirection: 'column', gap: '6px', width: '100%', maxWidth: '520px', marginTop: 'var(--space-xs)' }}>
              <div style={{ fontSize: '11px', fontWeight: 600, color: 'var(--color-text-muted)', textAlign: 'left' }}>
                Recommended Inquiries for {activeDomainInfo?.label || 'Active Track'}:
              </div>
              {quickQuestions.map((q, idx) => (
                <button
                  key={idx}
                  onClick={() => handleSendMessage(q)}
                  style={{
                    padding: '8px 12px',
                    borderRadius: 'var(--radius-sm)',
                    background: 'var(--color-surface-elevated)',
                    border: '1px solid var(--color-border)',
                    fontSize: '11px',
                    color: 'var(--color-text-main)',
                    textAlign: 'left',
                    cursor: 'pointer',
                    transition: 'all 0.15s ease',
                  }}
                  onMouseOver={(e) => (e.currentTarget.style.borderColor = 'var(--color-primary-400)')}
                  onMouseOut={(e) => (e.currentTarget.style.borderColor = 'var(--color-border)')}
                >
                  💬 {q}
                </button>
              ))}
            </div>
          </div>
        ) : (
          messages.map((msg, index) => (
            <ChatMessageBubble
              key={index}
              message={msg}
              onFollowupClick={(followupText) => handleSendMessage(followupText)}
            />
          ))
        )}
        {loading && (
          <div style={{ display: 'flex', gap: '8px', alignItems: 'center', color: 'var(--color-text-muted)', fontSize: 'var(--font-xs)', padding: '10px' }}>
            <div className="spinner" style={{ width: '16px', height: '16px', border: '2px solid rgba(99,102,241,0.2)', borderTopColor: 'var(--color-primary-400)', borderRadius: '50%', animation: 'spin 0.8s linear infinite' }} />
            <span>AI Tutor ({modelName || 'Neural Engine'}) is reasoning...</span>
          </div>
        )}
        <div ref={chatEndRef} />
      </div>

      {/* Input Area with Context Selector */}
      <div style={{ display: 'flex', flexDirection: 'column', gap: '6px' }}>
        <TutorContextSelector
          context={context}
          onContextChange={setContext}
          activeMode={activeMode}
        />

        <div style={{ display: 'flex', gap: 'var(--space-xs)' }}>
          <textarea
            className="input"
            rows={2}
            value={inputPrompt}
            onChange={(e) => setInputPrompt(e.target.value)}
            onKeyDown={handleKeyDown}
            placeholder="Ask a question or describe your coding error... (Enter to send, Shift+Enter for newline)"
            style={{ flex: 1, resize: 'none', fontSize: 'var(--font-sm)', padding: '8px 12px' }}
          />
          <button
            onClick={() => handleSendMessage()}
            disabled={loading || !inputPrompt.trim()}
            className="btn btn-primary"
            style={{ padding: '12px 18px', display: 'flex', alignItems: 'center', justifyContent: 'center' }}
          >
            <Send size={16} />
          </button>
        </div>
      </div>

      {/* Settings Drawer */}
      <TutorSettingsDrawer
        isOpen={showSettings}
        onClose={() => setShowSettings(false)}
        provider={provider}
        onProviderChange={setProvider}
        modelName={modelName}
        onModelNameChange={setModelName}
        ollamaUrl={ollamaUrl}
        onOllamaUrlChange={setOllamaUrl}
        apiKey={apiKey}
        onApiKeyChange={setApiKey}
        apiBase={apiBase}
        onApiBaseChange={setApiBase}
        modelsList={modelsList}
        isOllamaOnline={isOllamaOnline}
        onRefreshModels={loadModels}
        refreshing={refreshingModels}
      />
    </div>
  );
}
