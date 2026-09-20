import { apiRequest } from './api';

export const careerService = {
  async getCareerOverview() {
    return apiRequest('/career/overview');
  },
};
