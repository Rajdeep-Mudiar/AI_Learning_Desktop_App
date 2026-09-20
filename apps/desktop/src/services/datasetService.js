import { apiRequest } from './api';

export const datasetService = {
  async getDatasets() {
    return apiRequest('/datasets');
  },

  async getDatasetProfile(datasetId) {
    return apiRequest(`/datasets/${datasetId}`);
  },

  async uploadCustomDataset(payload) {
    return apiRequest('/datasets/upload', {
      method: 'POST',
      body: JSON.stringify(payload),
    });
  },
};
