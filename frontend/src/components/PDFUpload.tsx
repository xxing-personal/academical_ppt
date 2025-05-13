import { useState } from 'react';
import axios from 'axios';
import PresentationOutline from './PresentationOutline';
import type { PresentationResponse } from '../types/presentation';
import './PDFUpload.css';

const PDFUpload = () => {
  const [file, setFile] = useState<File | null>(null);
  const [error, setError] = useState<string>('');
  const [loading, setLoading] = useState<boolean>(false);
  const [presentation, setPresentation] = useState<PresentationResponse | null>(null);

  const handleFileChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    const selectedFile = event.target.files?.[0];
    if (selectedFile) {
      if (selectedFile.type !== 'application/pdf') {
        setError('Please select a PDF file');
        setFile(null);
        return;
      }
      setFile(selectedFile);
      setError('');
      setPresentation(null);
    }
  };

  const handleUpload = async () => {
    if (!file) {
      setError('Please select a file first');
      return;
    }

    setLoading(true);
    setError('');

    const formData = new FormData();
    formData.append('file', file);

    try {
      const response = await axios.post<PresentationResponse>(
        'http://localhost:8000/api/v1/pdf/generate_presentation',
        formData,
        {
          headers: {
            'Content-Type': 'multipart/form-data',
          },
        }
      );

      setPresentation(response.data);
    } catch (error: unknown) {
      if (error && typeof error === 'object' && 'response' in error) {
        const axiosError = error as { response?: { data?: { detail?: string } } };
        setError(axiosError.response?.data?.detail || 'Error uploading file');
      } else {
        setError('An unexpected error occurred');
      }
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="pdf-upload-container">
      <h2>PDF Presentation Generator</h2>
      
      <div className="upload-section">
        <label htmlFor="pdf-upload" className="file-label">Select PDF file</label>
        <input
          id="pdf-upload"
          type="file"
          accept=".pdf"
          onChange={handleFileChange}
          className="file-input"
        />
        <button 
          onClick={handleUpload}
          disabled={!file || loading}
          className="upload-button"
        >
          {loading ? 'Generating Presentation...' : 'Generate Presentation'}
        </button>
      </div>

      {error && (
        <div className="error-message">
          {error}
        </div>
      )}

      {presentation && (
        <PresentationOutline
          title={presentation.content.title}
          slides={presentation.content.slides}
        />
      )}
    </div>
  );
};

export default PDFUpload; 