import { apiRequest } from './api';

export const interviewService = {
  async getTracks() {
    return apiRequest('/interviews/tracks');
  },

  async getTrack(trackId) {
    return apiRequest(`/interviews/tracks/${trackId}`);
  },

  async evaluateInterview(trackId, answers) {
    return apiRequest(`/interviews/tracks/${trackId}/evaluate`, {
      method: 'POST',
      body: JSON.stringify({ answers }),
    });
  },
};
