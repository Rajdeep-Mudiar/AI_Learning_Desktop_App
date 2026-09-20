import { apiRequest } from './api';

export const deepLearningService = {
  async simulateMLP(payload) {
    return apiRequest('/deep-learning/mlp/simulate', {
      method: 'POST',
      body: JSON.stringify(payload),
    });
  },

  async runCNNConvolution(payload) {
    return apiRequest('/deep-learning/cnn/convolve', {
      method: 'POST',
      body: JSON.stringify(payload),
    });
  },

  async computeTransformerAttention(payload) {
    return apiRequest('/deep-learning/transformer/attention', {
      method: 'POST',
      body: JSON.stringify(payload),
    });
  },
};
