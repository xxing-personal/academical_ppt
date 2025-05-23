import React from 'react';
import './ReadingPage.css';

interface ReadingPageProps {
  pdfUrl: string;
}

const ReadingPage: React.FC<ReadingPageProps> = ({ pdfUrl }) => {
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
        <h3>Slidev Presentation</h3>
        <iframe
          src="http://localhost:3030/"
          title="Slides Viewer"
          className="slides-viewer"
        />
        <div style={{ display: 'flex', gap: '1rem', marginTop: '1rem' }}>
          <a href="http://localhost:3030/presenter/" target="_blank" rel="noopener noreferrer">Presenter Mode</a>
          <a href="http://localhost:3030/overview/" target="_blank" rel="noopener noreferrer">Slides Overview</a>
        </div>
      </div>
    </div>
  );
};

export default ReadingPage; 