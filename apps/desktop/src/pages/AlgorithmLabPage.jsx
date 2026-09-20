import React, { useState } from 'react';
import { TrendingUp, GitBranch, Share2, Grid, Layers, Sparkles } from 'lucide-react';
import LinearRegressionCanvas from '../components/visualizers/LinearRegressionCanvas';
import KNNBoundaryCanvas from '../components/visualizers/KNNBoundaryCanvas';
import DecisionTreeCanvas from '../components/visualizers/DecisionTreeCanvas';
import KMeansCanvas from '../components/visualizers/KMeansCanvas';
import PCACanvas from '../components/visualizers/PCACanvas';

const LAB_TABS = [
  { id: 'linear_regression', label: 'Linear Regression & OLS', icon: TrendingUp },
  { id: 'knn', label: 'K-Nearest Neighbors (KNN)', icon: Grid },
  { id: 'decision_tree', label: 'Decision Tree & Gini', icon: GitBranch },
  { id: 'kmeans', label: 'K-Means Clustering', icon: Share2 },
  { id: 'pca', label: 'Principal Component Analysis (PCA)', icon: Layers },
];

export default function AlgorithmLabPage() {
  const [activeTab, setActiveTab] = useState('linear_regression');

  return (
    <div className="animate-fade-in">
      <div style={{ marginBottom: 24 }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: 8, marginBottom: 4 }}>
          <span className="badge badge-purple">Phase 2 Interactive Laboratory</span>
        </div>
        <h1 style={{ fontSize: '1.75rem', marginBottom: 6 }}>Interactive Algorithm Simulations</h1>
        <p style={{ color: 'var(--text-secondary)', fontSize: '0.925rem' }}>
          Explore core machine learning mechanics through dynamic parameter manipulation and visual step execution.
        </p>
      </div>

      {/* Algorithm Tabs */}
      <div style={{ display: 'flex', gap: 8, overflowX: 'auto', paddingBottom: 12, marginBottom: 24 }}>
        {LAB_TABS.map((tab) => {
          const Icon = tab.icon;
          const isActive = tab.id === activeTab;
          return (
            <button
              key={tab.id}
              onClick={() => setActiveTab(tab.id)}
              className={isActive ? 'btn btn-primary' : 'btn btn-secondary'}
              style={{ padding: '9px 16px', borderRadius: 999, fontSize: '0.85rem' }}
            >
              <Icon size={16} />
              <span>{tab.label}</span>
            </button>
          );
        })}
      </div>

      {/* Active Lab Viewport */}
      <div>
        {activeTab === 'linear_regression' && <LinearRegressionCanvas />}
        {activeTab === 'knn' && <KNNBoundaryCanvas />}
        {activeTab === 'decision_tree' && <DecisionTreeCanvas />}
        {activeTab === 'kmeans' && <KMeansCanvas />}
        {activeTab === 'pca' && <PCACanvas />}
      </div>
    </div>
  );
}
