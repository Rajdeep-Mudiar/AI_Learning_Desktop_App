const API_BASE_URL = '/api/v1';

export async function apiRequest(endpoint, options = {}) {
  const token = localStorage.getItem('ailearn_token');
  const headers = {
    'Content-Type': 'application/json',
    ...(token ? { Authorization: `Bearer ${token}` } : {}),
    ...options.headers,
  };

  const response = await fetch(`${API_BASE_URL}${endpoint}`, {
    ...options,
    headers,
  });

  if (response.status === 401) {
    // If unauthorized and has token, clear expired token
    if (token) {
      localStorage.removeItem('ailearn_token');
      localStorage.removeItem('ailearn_user');
      window.dispatchEvent(new Event('auth:unauthorized'));
    }
  }

  const data = await response.json().catch(() => ({}));

  if (!response.ok) {
    const errorMsg = data.detail || 'An unexpected error occurred';
    throw new Error(typeof errorMsg === 'string' ? errorMsg : JSON.stringify(errorMsg));
  }

  return data;
}
