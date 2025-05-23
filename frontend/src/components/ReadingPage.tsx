import React from 'react';
import type { PresentationResponse } from '../types/presentation';
import './ReadingPage.css';

interface ReadingPageProps {
  pdfUrl: string;
  presentation: PresentationResponse;
}

const ReadingPage: React.FC<ReadingPageProps> = ({ pdfUrl, presentation }) => {
  const baseUrl = `http://localhost:3030`;

  return (
    <div className="reading-page">
      <div className="pdf-container">
        <iframe
          src={pdfUrl}
          title="PDF Viewer"
          className="pdf-viewer"
        />
      </div>
      <div className="slides-container">
        <h3>{presentation.title}</h3>
        <iframe
          src={baseUrl}
          title="Slides Viewer"
          className="slides-viewer"
        />
        <div style={{ display: 'flex', gap: '1rem', marginTop: '1rem' }}>
          <a href={`${baseUrl}/presenter/`} target="_blank" rel="noopener noreferrer">Presenter Mode</a>
          <a href={`${baseUrl}/overview/`} target="_blank" rel="noopener noreferrer">Slides Overview</a>
        </div>
      </div>
    </div>
  );
};

export default ReadingPage; 