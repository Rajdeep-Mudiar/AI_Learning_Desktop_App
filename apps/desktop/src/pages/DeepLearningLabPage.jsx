import React, { useState, useEffect } from 'react';
import { deepLearningService } from '../services/deepLearningService';
import NeuralNetworkGraphCanvas from '../components/neural/NeuralNetworkGraphCanvas';
import CNNKernelVisualizer from '../components/neural/CNNKernelVisualizer';
import TransformerAttentionVisualizer from '../components/neural/TransformerAttentionVisualizer';

export default function DeepLearningLabPage() {
  const [activeTab, setActiveTab] = useState('mlp'); // 'mlp' | 'cnn' | 'transformer'

  // --- MLP State ---
  const [layerSizes, setLayerSizes] = useState([2, 4, 4, 1]);
  const [activation, setActivation] = useState('relu');
  const [learningRate, setLearningRate] = useState(0.08);
  const [epochs, setEpochs] = useState(120);
  const [datasetType, setDatasetType] = useState('xor');
  const [mlpData, setMlpData] = useState(null);
  const [mlpLoading, setMlpLoading] = useState(false);

  // --- CNN State ---
  const [selectedKernel, setSelectedKernel] = useState('sobel_horizontal');
  const [poolingType, setPoolingType] = useState('max');
  const [stride, setStride] = useState(1);
  const [cnnData, setCnnData] = useState(null);
  const [cnnLoading, setCnnLoading] = useState(false);

  // --- Transformer State ---
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
          { id: 'mlp', label: '🧠 Multi-Layer Perceptron (MLP) Graph' },
          { id: 'cnn', label: '🖼️ CNN 2D Feature Map & Pooling' },
          { id: 'transformer', label: '✨ Transformer Scaled Dot-Product Attention' },
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
              <label style={{ fontSize: '11px', color: 'var(--color-text-muted)', display: 'block', marginBottom: '2px' }}>Activation Function ($\sigma$)</label>
              <select className="input" value={activation} onChange={(e) => setActivation(e.target.value)} style={{ fontSize: 'var(--font-xs)' }}>
                <option value="relu">ReLU ($\max(0, z)$)</option>
                <option value="sigmoid">Sigmoid ($1 / (1 + e^{-z})$)</option>
                <option value="tanh">Hyperbolic Tangent ($\tanh$)</option>
                <option value="leaky_relu">Leaky ReLU ($\max(0.1z, z)$)</option>
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
