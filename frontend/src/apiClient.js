// src/apiClient.js
import axios from 'axios';

const apiClient = axios.create({
  baseURL: import.meta.env.VITE_API_URL,
});

// Add a request interceptor
apiClient.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem('token');
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  },
  (error) => Promise.reject(error)
);

// Add a response interceptor for handling token expiration
apiClient.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response && error.response.status === 401) {
      // If the token is expired, remove it and redirect to login
      localStorage.removeItem('token');
      window.location.href = '/login';
    }
    return Promise.reject(error);
  }
);

// Questionnaire related API calls
export const getWeaknessesByGroup = async (group) => {
  const response = await apiClient.get(`/weaknesses/?group=${group}`);
  return response.data;
};

export const getRandomQuestions = async (groupAWeaknesses, groupBWeaknesses, groupCWeaknesses) => {
  const response = await apiClient.post('/questionnaires/get-random-questions', {
    group_a_weaknesses: groupAWeaknesses,
    group_b_weaknesses: groupBWeaknesses,
    group_c_weaknesses: groupCWeaknesses,
  });
  return response.data;
};

export const submitQuestionnaire = async (questionnaireData) => {
  console.log(JSON.stringify(questionnaireData, null, 2));
  const response = await apiClient.post('/questionnaires/', questionnaireData);
  return response.data;
};

export const getUserQuestionnaires = async () => {
  const response = await apiClient.get('/questionnaires/me');
  return response.data;
};

export const getQuestionnaireById = async (id) => {
  const response = await apiClient.get(`/questionnaires/${id}`);
  return response.data;
};

export const deleteQuestionnaire = async (id) => {
  const response = await apiClient.delete(`/questionnaires/${id}`);
  return response.data;
};

export default apiClient;