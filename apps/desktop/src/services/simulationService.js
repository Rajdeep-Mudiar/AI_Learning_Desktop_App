import { apiRequest } from './api';

export const simulationService = {
  async stepLinearRegression(points, weight, bias, learning_rate = 0.05) {
    return await apiRequest('/simulations/linear-regression/step', {
      method: 'POST',
      body: JSON.stringify({ points, weight, bias, learning_rate }),
    });
  },

  async stepKMeans(points, centroids) {
    return await apiRequest('/simulations/kmeans/step', {
      method: 'POST',
      body: JSON.stringify({ points, centroids }),
    });
  },

  async computePCA(points) {
    return await apiRequest('/simulations/pca/compute', {
      method: 'POST',
      body: JSON.stringify({ points }),
    });
  },

  async listDiagnosticScenarios() {
    return await apiRequest('/diagnostics/scenarios');
  },

  async getDiagnosticScenario(scenarioId) {
    return await apiRequest(`/diagnostics/scenarios/${scenarioId}`);
  },

  async submitDiagnosis(scenarioId, selectedOption) {
    return await apiRequest(`/diagnostics/scenarios/${scenarioId}/submit`, {
      method: 'POST',
      body: JSON.stringify({ scenario_id: scenarioId, selected_option: selectedOption }),
    });
  }
};
