import { apiRequest } from './api';

export const researchService = {
  async getPapers() {
    return apiRequest('/research/papers');
  },

  async getPaper(paperId) {
    return apiRequest(`/research/papers/${paperId}`);
  },
};
