import { apiRequest } from './api';

export const challengeService = {
  async listChallenges() {
    return await apiRequest('/challenges');
  },

  async getChallenge(challengeId) {
    return await apiRequest(`/challenges/${challengeId}`);
  },

  async submitChallenge(challengeId, code) {
    return await apiRequest(`/challenges/${challengeId}/submit`, {
      method: 'POST',
      body: JSON.stringify({
        challenge_id: challengeId,
        code,
      }),
    });
  }
};
