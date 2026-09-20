import { apiRequest } from './api';

export const tutorService = {
  async chat(payload) {
    return apiRequest('/tutor/chat', {
      method: 'POST',
      body: JSON.stringify(payload),
    });
  },

  async getModels(baseUrl) {
    const params = baseUrl ? `?base_url=${encodeURIComponent(baseUrl)}` : '';
    return apiRequest(`/tutor/models${params}`);
  },

  async getPresets() {
    return apiRequest('/tutor/presets');
  },
};
