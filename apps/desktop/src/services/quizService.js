import { apiRequest } from './api';

export const quizService = {
  async getQuiz(quizId) {
    return await apiRequest(`/quizzes/${quizId}`);
  },

  async submitQuiz(quizId, answers) {
    return await apiRequest(`/quizzes/${quizId}/submit`, {
      method: 'POST',
      body: JSON.stringify({ answers }),
    });
  }
};
