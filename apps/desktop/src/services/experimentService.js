import { apiRequest } from './api';

export const experimentService = {
  async trainExperiment(payload) {
    return apiRequest('/experiments/train', {
      method: 'POST',
      body: JSON.stringify(payload),
    });
  },

  async getExperiments() {
    return apiRequest('/experiments');
  },

  async compareExperiments(experimentIds) {
    return apiRequest('/experiments/compare', {
      method: 'POST',
      body: JSON.stringify({ experiment_ids: experimentIds }),
    });
  },
};
