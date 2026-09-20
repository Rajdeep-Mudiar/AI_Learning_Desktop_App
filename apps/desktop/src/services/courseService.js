import { apiRequest } from './api';

export const courseService = {
  async getAllCourses() {
    return await apiRequest('/courses');
  },

  async getCourseBySlug(slug) {
    return await apiRequest(`/courses/${slug}`);
  },

  async getLessonBySlug(slug) {
    return await apiRequest(`/lessons/${slug}`);
  },

  async completeLesson(slug) {
    return await apiRequest(`/lessons/${slug}/complete`, {
      method: 'POST',
    });
  }
};
