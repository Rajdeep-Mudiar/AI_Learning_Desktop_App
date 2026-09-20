import React, { useState, useEffect } from 'react';
import { deepLearningService } from '../services/deepLearningService';
import NeuralNetworkGraphCanvas from '../components/neural/NeuralNetworkGraphCanvas';
import CNNKernelVisualizer from '../components/neural/CNNKernelVisualizer';
import TransformerAttentionVisualizer from '../components/neural/TransformerAttentionVisualizer';

export default function DeepLearningLabPage() {
  const [activeTab, setActiveTab] = useState('regression'); // 'regression' | 'mlp' | 'cnn' | 'transformer'

  // --- Regression State (Level 1 Basics) ---
  const [slope, setSlope] = useState(1.5);
  const [bias, setBias] = useState(0.5);
  const [regDataPoints, setRegDataPoints] = useState([
    { x: -2, y: -2.4, class: 0 },
    { x: -1, y: -0.8, class: 0 },
    { x: 0, y: 0.6, class: 0 },
    { x: 1, y: 2.1, class: 1 },
    { x: 2, y: 3.4, class: 1 },
    { x: 3, y: 5.1, class: 1 }
  ]);

  // Compute Mean Squared Error (MSE)
  const mseLoss = (
    regDataPoints.reduce((acc, p) => {
      const pred = slope * p.x + bias;
      return acc + Math.pow(pred - p.y, 2);
    }, 0) / regDataPoints.length
  ).toFixed(3);

  // --- MLP State (Level 2) ---
  const [layerSizes, setLayerSizes] = useState([2, 4, 4, 1]);
  const [activation, setActivation] = useState('relu');
  const [learningRate, setLearningRate] = useState(0.08);
  const [epochs, setEpochs] = useState(120);
  const [datasetType, setDatasetType] = useState('xor');
  const [mlpData, setMlpData] = useState(null);
  const [mlpLoading, setMlpLoading] = useState(false);

  // --- CNN State (Level 3) ---
  const [selectedKernel, setSelectedKernel] = useState('sobel_horizontal');
  const [poolingType, setPoolingType] = useState('max');
  const [stride, setStride] = useState(1);
  const [cnnData, setCnnData] = useState(null);
  const [cnnLoading, setCnnLoading] = useState(false);

  // --- Transformer State (Level 4) ---
  const [sentence, setSentence] = useState('The transformer model calculates attention weights across tokens');
  const [numHeads, setNumHeads] = useState(4);
  const [transformerData, setTransformerData] = useState(null);
  const [transformerLoading, setTransformerLoading] = useState(false);

  useEffect(() => {
    runMLPSimulation();
    runCNN();
    runTransformer();
  }, []);

  const runMLPSimulation = async () => {
    try {
      setMlpLoading(true);
      const res = await deepLearningService.simulateMLP({
        layer_sizes: layerSizes,
        activation,
        learning_rate: parseFloat(learningRate),
        epochs: parseInt(epochs),
        dataset_type: datasetType,
      });
      setMlpData(res);
    } catch (err) {
      console.error(err);
    } finally {
      setMlpLoading(false);
    }
  };

  const runCNN = async (kName = selectedKernel, pType = poolingType, sVal = stride) => {
    try {
      setCnnLoading(true);
      const res = await deepLearningService.runCNNConvolution({
        kernel_name: kName,
        pooling_type: pType,
        stride: sVal,
      });
      setCnnData(res);
    } catch (err) {
      console.error(err);
    } finally {
      setCnnLoading(false);
    }
  };

  const runTransformer = async () => {
    try {
      setTransformerLoading(true);
      const res = await deepLearningService.computeTransformerAttention({
        sentence,
        num_heads: numHeads,
        d_model: 32,
      });
      setTransformerData(res);
    } catch (err) {
      console.error(err);
    } finally {
      setTransformerLoading(false);
    }
  };

  return (
    <div className="container" style={{ paddingBottom: 'var(--space-2xl)' }}>
      {/* Header */}
      <div style={{ marginBottom: 'var(--space-xl)' }}>
        <h1 style={{ fontSize: 'var(--font-2xl)', fontWeight: 800, margin: '0 0 var(--space-xs) 0', color: 'var(--color-text-main)' }}>
          Neural Network & Deep Learning Architecture Lab
        </h1>
        <p style={{ margin: 0, color: 'var(--color-text-muted)', fontSize: 'var(--font-sm)' }}>
          Inspect mathematical forward activations, backpropagation gradient updates, spatial convolution feature maps, and multi-head self-attention mechanisms.
        </p>
      </div>

      {/* Top Architecture Mode Tabs */}
      <div style={{ display: 'flex', gap: 'var(--space-sm)', borderBottom: '1px solid var(--color-border)', marginBottom: 'var(--space-xl)' }}>
        {[
          { id: 'regression', label: '📈 1. Linear & Logistic Boundary (Basics)' },
          { id: 'mlp', label: '🧠 2. Multi-Layer Perceptron (MLP) Graph' },
          { id: 'cnn', label: '🖼️ 3. CNN 2D Feature Map & Pooling' },
          { id: 'transformer', label: '✨ 4. Transformer Multi-Head Attention' },
        ].map((tab) => (
          <button
            key={tab.id}
            onClick={() => setActiveTab(tab.id)}
            style={{
              background: 'none',
              border: 'none',
              padding: '12px 18px',
              color: activeTab === tab.id ? 'var(--color-primary-400)' : 'var(--color-text-muted)',
              borderBottom: activeTab === tab.id ? '2px solid var(--color-primary-400)' : '2px solid transparent',
              fontWeight: activeTab === tab.id ? 700 : 500,
              fontSize: 'var(--font-sm)',
              cursor: 'pointer',
              transition: 'all 0.15s ease',
            }}
          >
            {tab.label}
          </button>
        ))}
      </div>

      {/* Tab 1: Regression (Basics Level 1) */}
      {activeTab === 'regression' && (
        <div style={{ display: 'grid', gap: 'var(--space-xl)' }}>
          <div className="card" style={{ padding: 'var(--space-xl)', background: '#090d16', border: '1px solid #1e293b' }}>
            <h3 style={{ margin: '0 0 var(--space-md) 0', color: 'var(--color-text-main)', fontSize: 'var(--font-lg)' }}>
              Interactive Linear Regression & Loss Minimization
            </h3>
            <p style={{ fontSize: 'var(--font-xs)', color: 'var(--color-text-muted)', margin: '0 0 var(--space-lg) 0' }}>
              Formula: <code>y_pred = w * x + b</code>. Adjust weight slope ($w$) and bias ($b$) to minimize the Mean Squared Error (MSE).
            </p>

            <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: 'var(--space-xl)', alignItems: 'center' }}>
              <div style={{ background: '#1e293b', padding: '24px', borderRadius: '14px', border: '1px solid #334155', textAlign: 'center' }}>
                <div style={{ fontSize: 'var(--font-xs)', color: '#94a3b8' }}>Calculated Mean Squared Error (MSE):</div>
                <div style={{ fontSize: '3rem', fontWeight: 800, color: mseLoss < 0.5 ? '#10b981' : '#f59e0b', margin: '8px 0' }}>
                  {mseLoss}
                </div>
                <div style={{ fontSize: '11px', color: '#94a3b8' }}>
                  Model equation: <strong>y = {slope}x + {bias}</strong>
                </div>
              </div>

              <div style={{ display: 'flex', flexDirection: 'column', gap: 'var(--space-md)' }}>
                <div>
                  <div style={{ display: 'flex', justifyContent: 'space-between', fontSize: 'var(--font-xs)', marginBottom: '4px' }}>
                    <span>Weight Slope ($w$): <strong>{slope}</strong></span>
                  </div>
                  <input
                    type="range"
                    min="-3"
                    max="5"
                    step="0.1"
                    value={slope}
                    onChange={(e) => setSlope(parseFloat(e.target.value))}
                    style={{ width: '100%' }}
                  />
                </div>

                <div>
                  <div style={{ display: 'flex', justifyContent: 'space-between', fontSize: 'var(--font-xs)', marginBottom: '4px' }}>
                    <span>Bias Intercept ($b$): <strong>{bias}</strong></span>
                  </div>
                  <input
                    type="range"
                    min="-5"
                    max="5"
                    step="0.1"
                    value={bias}
                    onChange={(e) => setBias(parseFloat(e.target.value))}
                    style={{ width: '100%' }}
                  />
                </div>

                <button
                  onClick={() => { setSlope(1.5); setBias(0.5); }}
                  className="btn btn-secondary btn-sm"
                  style={{ alignSelf: 'flex-start' }}
                >
                  ⚡ Auto-Fit Optimal Gradient
                </button>
              </div>
            </div>
          </div>
        </div>
      )}

      {/* Tab 1: MLP */}
      {activeTab === 'mlp' && (
        <div style={{ display: 'flex', flexDirection: 'column', gap: 'var(--space-lg)' }}>
          {/* Controls Form */}
          <div className="card" style={{ padding: 'var(--space-md)', display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(180px, 1fr))', gap: 'var(--space-md)', alignItems: 'end' }}>
            <div>
              <label style={{ fontSize: '11px', color: 'var(--color-text-muted)', display: 'block', marginBottom: '2px' }}>Synthetic 2D Dataset</label>
              <select className="input" value={datasetType} onChange={(e) => setDatasetType(e.target.value)} style={{ fontSize: 'var(--font-xs)' }}>
                <option value="xor">XOR Non-Linear Problem</option>
                <option value="circles">Concentric Rings</option>
                <option value="moons">Interleaved Moons</option>
                <option value="spiral">Two-Armed Spiral</option>
              </select>
            </div>

            <div>
              <label style={{ fontSize: '11px', color: 'var(--color-text-muted)', display: 'block', marginBottom: '2px' }}>Activation Function (σ)</label>
              <select className="input" value={activation} onChange={(e) => setActivation(e.target.value)} style={{ fontSize: 'var(--font-xs)' }}>
                <option value="relu">ReLU (max(0, z))</option>
                <option value="sigmoid">Sigmoid (1 / (1 + e^-z))</option>
                <option value="tanh">Hyperbolic Tangent (tanh)</option>
                <option value="leaky_relu">Leaky ReLU (max(0.1z, z))</option>
              </select>
            </div>

            <div>
              <div style={{ display: 'flex', justifyContent: 'space-between', fontSize: '11px', color: 'var(--color-text-muted)' }}>
                <span>Learning Rate ($\eta$)</span>
                <strong>{learningRate}</strong>
              </div>
              <input
                type="range"
                min="0.01"
                max="0.3"
                step="0.01"
                value={learningRate}
                onChange={(e) => setLearningRate(parseFloat(e.target.value))}
                style={{ width: '100%', marginTop: '4px' }}
              />
            </div>

            <div>
              <div style={{ display: 'flex', justifyContent: 'space-between', fontSize: '11px', color: 'var(--color-text-muted)' }}>
                <span>Training Epochs</span>
                <strong>{epochs}</strong>
              </div>
              <input
                type="range"
                min="30"
                max="300"
                step="10"
                value={epochs}
                onChange={(e) => setEpochs(parseInt(e.target.value))}
                style={{ width: '100%', marginTop: '4px' }}
              />
            </div>

            <button
              onClick={runMLPSimulation}
              disabled={mlpLoading}
              className="btn btn-primary"
              style={{ padding: '10px', fontSize: 'var(--font-xs)', fontWeight: 700 }}
            >
              {mlpLoading ? 'Simulating Backprop...' : '⚡ Train MLP Graph'}
            </button>
          </div>

          {/* Graph visualizer */}
          {mlpData ? (
            <NeuralNetworkGraphCanvas simulationData={mlpData} />
          ) : (
            <div style={{ padding: 'var(--space-2xl)', textAlign: 'center', color: 'var(--color-text-muted)' }}>
              Loading MLP simulation...
            </div>
          )}
        </div>
      )}

      {/* Tab 2: CNN */}
      {activeTab === 'cnn' && (
        <CNNKernelVisualizer
          data={cnnData}
          selectedKernel={selectedKernel}
          onKernelChange={(k) => {
            setSelectedKernel(k);
            runCNN(k, poolingType, stride);
          }}
          poolingType={poolingType}
          onPoolingChange={(p) => {
            setPoolingType(p);
            runCNN(selectedKernel, p, stride);
          }}
          stride={stride}
          onStrideChange={(s) => {
            setStride(s);
            runCNN(selectedKernel, poolingType, s);
          }}
        />
      )}

      {/* Tab 3: Transformer */}
      {activeTab === 'transformer' && (
        <TransformerAttentionVisualizer
          data={transformerData}
          sentence={sentence}
          onSentenceChange={setSentence}
          numHeads={numHeads}
          onNumHeadsChange={setNumHeads}
          onCompute={runTransformer}
          loading={transformerLoading}
        />
      )}
    </div>
  );
}
