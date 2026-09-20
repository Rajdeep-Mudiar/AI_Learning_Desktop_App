import React, { useState, useEffect, useRef } from 'react';
import { tutorService } from '../services/tutorService';
import ChatMessageBubble from '../components/tutor/ChatMessageBubble';
import TutorContextSelector from '../components/tutor/TutorContextSelector';
import TutorSettingsDrawer from '../components/tutor/TutorSettingsDrawer';
import { Send, Sparkles, Settings as SettingsIcon, Trash2, Bot } from 'lucide-react';

export default function TutorPage() {
  const [messages, setMessages] = useState([]);
  const [inputPrompt, setInputPrompt] = useState('');
  const [loading, setLoading] = useState(false);
  const [activeMode, setActiveMode] = useState('socratic'); // 'socratic' | 'explain_mistake' | 'math_derivation' | 'code_review'

  // Settings state
  const [showSettings, setShowSettings] = useState(false);
  const [provider, setProvider] = useState('auto');
  const [modelName, setModelName] = useState('llama3:latest');
  const [ollamaUrl, setOllamaUrl] = useState('http://localhost:11434');
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
      setModelsList(data.available_models);
      setIsOllamaOnline(data.is_ollama_online);
      if (data.default_model) {
        setModelName(data.default_model);
      }
    } catch (err) {
      console.error(err);
    } finally {
      setRefreshingModels(false);
    }
  };

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
        context: {
          ...context,
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
    { id: 'explain_mistake', name: 'Explain My Mistake', icon: '🔍', desc: 'Pinpoints flawed math/code' },
    { id: 'math_derivation', name: 'Math & Derivations', icon: '📐', desc: 'Step-by-step proofs & dimensions' },
    { id: 'code_review', name: 'Code Review', icon: '⚡', desc: 'NumPy/PyTorch vectorization checks' },
  ];

  return (
    <div className="container" style={{ height: 'calc(100vh - 100px)', display: 'flex', flexDirection: 'column' }}>
      {/* Header & Mode Bar */}
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: 'var(--space-md)' }}>
        <div>
          <h1 style={{ fontSize: 'var(--font-xl)', fontWeight: 800, margin: '0 0 2px 0', color: 'var(--color-text-main)', display: 'flex', alignItems: 'center', gap: '8px' }}>
            <Sparkles size={20} color="var(--color-primary-400)" /> Context-Aware AI Tutor
          </h1>
          <p style={{ margin: 0, color: 'var(--color-text-muted)', fontSize: 'var(--font-xs)' }}>
            Grounded in your active lessons, coding playground, and diagnostic challenges.
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
            <span>{isOllamaOnline ? 'Ollama: Online' : 'Settings'}</span>
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
          border: '1px solid var(--color-border)',
          borderRadius: 'var(--radius-lg)',
          display: 'flex',
          flexDirection: 'column',
          marginBottom: 'var(--space-md)',
        }}
      >
        {messages.length === 0 ? (
          <div style={{ margin: 'auto', textAlign: 'center', maxWidth: '600px', padding: 'var(--space-xl)' }}>
            <div
              style={{
                width: 54,
                height: 54,
                borderRadius: 'var(--radius-full)',
                background: 'linear-gradient(135deg, #6366f1, #38bdf8)',
                display: 'inline-flex',
                alignItems: 'center',
                justifyContent: 'center',
                color: '#ffffff',
                boxShadow: 'var(--shadow-md)',
                marginBottom: 'var(--space-md)',
              }}
            >
              <Bot size={28} />
            </div>
            <h3 style={{ margin: '0 0 var(--space-xs) 0', fontSize: 'var(--font-lg)', color: 'var(--color-text-main)' }}>
              How can I assist your AI learning today?
            </h3>
            <p style={{ margin: '0 0 var(--space-lg) 0', fontSize: 'var(--font-xs)', color: 'var(--color-text-muted)' }}>
              Ask questions about backpropagation mathematics, debug PyTorch/NumPy broadcasting bugs, or request Socratic guidance.
            </p>

            {/* Quick Prompt Starters */}
            <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: 'var(--space-sm)', textAlign: 'left' }}>
              {(presets.quick_questions.length > 0 ? presets.quick_questions : [
                "Why does Scaled Dot-Product Attention divide by √d_k?",
                "Derive the Ordinary Least Squares (OLS) Normal Equation",
                "Why did my gradient explode to NaN during training?",
                "What is the mathematical difference between Gini Impurity and Entropy?"
              ]).map((q, idx) => (
                <button
                  key={idx}
                  onClick={() => handleSendMessage(q)}
                  style={{
                    padding: '10px 12px',
                    borderRadius: 'var(--radius-md)',
                    background: 'var(--color-surface-elevated)',
                    border: '1px solid var(--color-border)',
                    fontSize: '11px',
                    color: 'var(--color-text-main)',
                    cursor: 'pointer',
                    transition: 'border 0.15s ease',
                    textAlign: 'left',
                  }}
                >
                  💡 {q}
                </button>
              ))}
            </div>
          </div>
        ) : (
          <>
            {messages.map((msg, idx) => (
              <ChatMessageBubble key={idx} message={msg} onFollowupClick={handleSendMessage} />
            ))}
            {loading && (
              <div style={{ display: 'flex', gap: '8px', alignItems: 'center', padding: 'var(--space-md)', color: 'var(--color-text-muted)', fontSize: 'var(--font-xs)' }}>
                <Bot size={18} color="var(--color-primary-400)" />
                <span>AI Tutor is formulating a Socratic explanation...</span>
              </div>
            )}
            <div ref={chatEndRef} />
          </>
        )}
      </div>

      {/* Input Box & Context Attachment */}
      <div className="card" style={{ padding: 'var(--space-sm) var(--space-md)', display: 'flex', flexDirection: 'column', gap: 'var(--space-xs)' }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: 'var(--space-sm)' }}>
          <TutorContextSelector context={context} onContextChange={setContext} />
          <span style={{ fontSize: '11px', color: 'var(--color-text-muted)' }}>
            Active Mode: <strong>{MODES_CONFIG.find((m) => m.id === activeMode)?.name}</strong>
          </span>
        </div>

        <div style={{ display: 'flex', gap: 'var(--space-sm)', alignItems: 'flex-end' }}>
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
        modelsList={modelsList}
        isOllamaOnline={isOllamaOnline}
        onRefreshModels={loadModels}
        refreshing={refreshingModels}
      />
    </div>
  );
}
