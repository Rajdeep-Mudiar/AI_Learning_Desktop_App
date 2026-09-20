import { apiRequest } from './api';

export const authService = {
  async login(email, password) {
    const data = await apiRequest('/auth/login', {
      method: 'POST',
      body: JSON.stringify({ email, password }),
    });
    localStorage.setItem('ailearn_token', data.access_token);
    localStorage.setItem('ailearn_user', JSON.stringify(data.user));
    return data;
  },

  async register(name, email, password, preferred_track = 'ai_engineer') {
    const data = await apiRequest('/auth/register', {
      method: 'POST',
      body: JSON.stringify({ name, email, password, preferred_track }),
    });
    localStorage.setItem('ailearn_token', data.access_token);
    localStorage.setItem('ailearn_user', JSON.stringify(data.user));
    return data;
  },

  async getMe() {
    return await apiRequest('/auth/me');
  },

  async updateProfile(profileData) {
    return await apiRequest('/auth/profile', {
      method: 'PUT',
      body: JSON.stringify(profileData),
    });
  },

  logout() {
    localStorage.removeItem('ailearn_token');
    localStorage.removeItem('ailearn_user');
  },

  getStoredUser() {
    const userStr = localStorage.getItem('ailearn_user');
    try {
      return userStr ? JSON.parse(userStr) : null;
    } catch {
      return null;
    }
  },

  getToken() {
    return localStorage.getItem('ailearn_token');
  }
};
