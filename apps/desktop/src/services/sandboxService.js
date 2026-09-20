import { apiRequest } from './api';

export const sandboxService = {
  async executeCode(code, timeout_seconds = 5.0, filenames = null, stdin_input = null) {
    return await apiRequest('/sandbox/execute', {
      method: 'POST',
      body: JSON.stringify({
        code,
        timeout_seconds,
        filenames,
        stdin_input,
      }),
    });
  }
};
