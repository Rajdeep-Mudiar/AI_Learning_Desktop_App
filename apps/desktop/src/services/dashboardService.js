import { apiRequest } from './api';

export const dashboardService = {
  async getDashboardSummary() {
    return await apiRequest('/dashboard/summary');
  },

  async getSystemStatus() {
    return await apiRequest('/settings/system-status');
  }
};
