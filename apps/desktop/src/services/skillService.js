import { apiRequest } from './api';

export const skillService = {
  async getSkillTree() {
    return await apiRequest('/skills/tree');
  }
};
