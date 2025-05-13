import { render, screen, fireEvent, waitFor } from '@testing-library/react';
import PDFUpload from '../PDFUpload';
import axios from 'axios';

// Mock axios
jest.mock('axios');
const mockedAxios = axios as jest.Mocked<typeof axios>;

describe('PDFUpload', () => {
  beforeEach(() => {
    // Clear all mocks before each test
    jest.clearAllMocks();
  });

  it('renders upload button and file input', () => {
    render(<PDFUpload />);
    expect(screen.getByText('PDF Presentation Generator')).toBeInTheDocument();
    expect(screen.getByRole('button')).toBeInTheDocument();
    expect(screen.getByLabelText(/file/i)).toBeInTheDocument();
  });

  it('shows error for non-PDF file', async () => {
    render(<PDFUpload />);
    
    const file = new File(['test'], 'test.txt', { type: 'text/plain' });
    const input = screen.getByLabelText(/file/i);
    
    fireEvent.change(input, { target: { files: [file] } });
    
    expect(screen.getByText('Please select a PDF file')).toBeInTheDocument();
  });

  it('handles successful presentation generation', async () => {
    const mockResponse = {
      data: {
        content: {
          title: 'Test Presentation',
          slides: [
            {
              title: 'Introduction',
              points: ['Point 1', 'Point 2']
            }
          ]
        },
        message: 'Presentation content generated successfully'
      },
      status: 200,
      statusText: 'OK',
      headers: {},
      config: { url: '' },
    };

    mockedAxios.post.mockResolvedValueOnce(mockResponse);

    render(<PDFUpload />);
    
    const file = new File(['test'], 'test.pdf', { type: 'application/pdf' });
    const input = screen.getByLabelText(/file/i);
    
    fireEvent.change(input, { target: { files: [file] } });
    fireEvent.click(screen.getByRole('button'));

    await waitFor(() => {
      expect(screen.getByText('Test Presentation')).toBeInTheDocument();
      expect(screen.getByText('1. Introduction')).toBeInTheDocument();
      expect(screen.getByText('Point 1')).toBeInTheDocument();
      expect(screen.getByText('Point 2')).toBeInTheDocument();
    });
  });

  it('handles API error', async () => {
    mockedAxios.post.mockRejectedValueOnce({
      response: {
        data: {
          detail: 'Error processing file'
        }
      }
    });

    render(<PDFUpload />);
    
    const file = new File(['test'], 'test.pdf', { type: 'application/pdf' });
    const input = screen.getByLabelText(/file/i);
    
    fireEvent.change(input, { target: { files: [file] } });
    fireEvent.click(screen.getByRole('button'));

    await waitFor(() => {
      expect(screen.getByText('Error processing file')).toBeInTheDocument();
    });
  });

  it('shows loading state during upload', async () => {
    mockedAxios.post.mockResolvedValueOnce({
      data: {
        content: {
          title: 'Loading Test',
          slides: []
        },
        message: 'Presentation content generated successfully'
      },
      status: 200,
      statusText: 'OK',
      headers: {},
      config: { url: '' },
    });

    render(<PDFUpload />);
    
    const file = new File(['test'], 'test.pdf', { type: 'application/pdf' });
    const input = screen.getByLabelText(/file/i);
    
    fireEvent.change(input, { target: { files: [file] } });
    fireEvent.click(screen.getByRole('button'));

    expect(screen.getByText('Generating Presentation...')).toBeInTheDocument();
  });
}); 