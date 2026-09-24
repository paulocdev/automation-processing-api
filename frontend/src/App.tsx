import React, { useState, useEffect } from 'react';
import {
  checkHealth,
  processDocument,
  type HealthResponse,
  type DocumentProcessResponse,
  type ApiErrorResponse,
} from './services/api';
import axios from 'axios';

export function App() {
  const [health, setHealth] = useState<HealthResponse | null>(null);
  const [selectedFile, setSelectedFile] = useState<File | null>(null);
  const [priority, setPriority] = useState(1);
  
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState<DocumentProcessResponse | null>(null);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    checkHealth()
      .then((data) => setHealth(data))
      .catch(() => setHealth(null));
  }, []);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!selectedFile) return;

    setLoading(true);
    setError(null);
    setResult(null);

    try {
      const response = await processDocument(selectedFile, priority);
      setResult(response);
    } catch (err) {
      if (axios.isAxiosError(err) && err.response) {
        const apiError = err.response.data as ApiErrorResponse;
        setError(apiError.message || 'Erro ao processar arquivo.');
      } else {
        setError('Erro de conexão com o servidor backend.');
      }
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={{ maxWidth: '600px', margin: '40px auto', fontFamily: 'sans-serif', padding: '20px' }}>
      <h2>Automation & Document Processing Dashboard</h2>
      
      {/* Banner de Health Check */}
      <div style={{
        padding: '10px 15px',
        borderRadius: '6px',
        marginBottom: '20px',
        backgroundColor: health ? '#e6fffa' : '#ffebe9',
        border: `1px solid ${health ? '#38b2ac' : '#f85149'}`
      }}>
        <strong>Backend Status: </strong>
        {health ? `${health.status.toUpperCase()} (${health.service} v${health.version})` : 'Offline / Erro de conexão'}
      </div>

      {/* Formulário de Upload de Arquivo Real */}
      <form onSubmit={handleSubmit} style={{ display: 'flex', flexDirection: 'column', gap: '12px' }}>
        <div>
          <label style={{ display: 'block', marginBottom: '4px' }}>Selecionar Arquivo (PDF, DOCX, OCR):</label>
          <input
            type="file"
            onChange={(e) => e.target.files && setSelectedFile(e.target.files[0])}
            required
            style={{ width: '100%', padding: '8px', boxSizing: 'border-box' }}
          />
        </div>

        <div>
          <label style={{ display: 'block', marginBottom: '4px' }}>Prioridade (1 a 5):</label>
          <input
            type="number"
            min="1"
            max="5"
            value={priority}
            onChange={(e) => setPriority(Number(e.target.value))}
            style={{ width: '100%', padding: '8px', boxSizing: 'border-box' }}
          />
        </div>

        <button
          type="submit"
          disabled={loading || !health || !selectedFile}
          style={{
            padding: '10px',
            backgroundColor: '#0066cc',
            color: '#fff',
            border: 'none',
            borderRadius: '4px',
            cursor: 'pointer'
          }}
        >
          {loading ? 'Enviando...' : 'Enviar para Processamento'}
        </button>
      </form>

      {/* Sucesso */}
      {result && (
        <div style={{ marginTop: '20px', padding: '15px', backgroundColor: '#f0f9ff', borderLeft: '4px solid #0284c7', color: '#1e293b' }}>
          <h4>Processamento Agendado (HTTP 202):</h4>
          <p><strong>Task ID:</strong> {result.task_id}</p>
          <p><strong>Status:</strong> {result.status}</p>
          <p><strong>Mensagem:</strong> {result.message}</p>
        </div>
      )}

      {/* Erro */}
      {error && (
        <div style={{ marginTop: '20px', padding: '15px', backgroundColor: '#fff1f0', borderLeft: '4px solid #f5222d', color: '#1e293b' }}>
          <h4>Erro de Validação (HTTP 400):</h4>
          <p>{error}</p>
        </div>
      )}
    </div>
  );
}

export default App;