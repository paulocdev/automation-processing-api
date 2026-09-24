import axios from 'axios';

export const api = axios.create({
  baseURL: 'http://localhost:8000',
});

export interface HealthResponse {
  status: string;
  service: string;
  version: string;
}

export interface DocumentProcessResponse {
  task_id: string;
  status: string;
  message: string;
}

export interface ApiErrorResponse {
  error: string;
  message: string;
}

export const checkHealth = async (): Promise<HealthResponse> => {
  const response = await api.get<HealthResponse>('/api/health');
  return response.data;
};

// Envio real do arquivo via Multipart FormData
export const processDocument = async (
  file: File,
  priority: number
): Promise<DocumentProcessResponse> => {
  const formData = new FormData();
  formData.append('file', file);
  formData.append('priority', priority.toString());

  const response = await api.post<DocumentProcessResponse>(
    '/api/documents/process',
    formData,
    {
      headers: {
        'Content-Type': 'multipart/form-data',
      },
    }
  );
  return response.data;
};