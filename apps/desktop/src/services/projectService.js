import { apiRequest } from './api';

export const projectService = {
  async getProjects() {
    return apiRequest('/projects');
  },

  async getProject(projectId) {
    return apiRequest(`/projects/${projectId}`);
  },

  async getVivaQuestion(projectId, step = 1) {
    return apiRequest(`/projects/${projectId}/viva/question?step=${step}`);
  },

  async submitVivaAnswer(projectId, payload) {
    return apiRequest(`/projects/${projectId}/viva/submit`, {
      method: 'POST',
      body: JSON.stringify(payload),
    });
  },

  async getPortfolioExport(projectId) {
    return apiRequest(`/projects/${projectId}/portfolio`);
  },
};
