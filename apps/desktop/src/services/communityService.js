import { apiRequest } from './api';

export const communityService = {
  async getPosts() {
    return apiRequest('/community/posts');
  },

  async createPost(payload) {
    return apiRequest('/community/posts', {
      method: 'POST',
      body: JSON.stringify(payload),
    });
  },

  async upvotePost(postId) {
    return apiRequest(`/community/posts/${postId}/upvote`, {
      method: 'POST',
    });
  },
};
