import { apiRequest } from './api';

export const achievementService = {
  async getAchievements() {
    return apiRequest('/achievements');
  },
};
