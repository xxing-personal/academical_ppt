import React from 'react';
import type { PresentationResponse } from '../types/presentation';
import './ReadingPage.css';

interface ReadingPageProps {
  pdfUrl: string;
  presentation: PresentationResponse;
}

const ReadingPage: React.FC<ReadingPageProps> = ({ pdfUrl, presentation }) => {
  return (
    <div className="reading-page">
      <div className="pdf-container" style={{margin: 0, padding: 0}}>
        <iframe
          src={pdfUrl}
          title="PDF Viewer"
          className="pdf-viewer"
          style={{margin: 0, padding: 0, display: 'block'}}
        />
      </div>
      <div className="slides-container">
        <iframe
          src={presentation.slidev_url}
          title="Slides Viewer"
          className="slides-viewer"
        />
      </div>
    </div>
  );
};

export default ReadingPage; 