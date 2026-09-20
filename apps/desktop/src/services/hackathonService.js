import { apiRequest } from './api';

export const hackathonService = {
  async getHackathons() {
    return apiRequest('/hackathons');
  },

  async submitEntry(payload) {
    return apiRequest('/hackathons/submit', {
      method: 'POST',
      body: JSON.stringify(payload),
    });
  },
};
