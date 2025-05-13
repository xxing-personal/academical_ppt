import { render, screen } from '@testing-library/react';
import PresentationOutline from '../PresentationOutline';

const mockSlides = [
  {
    title: "Introduction",
    points: ["Point 1", "Point 2", "Point 3"]
  },
  {
    title: "Methods",
    points: ["Method 1", "Method 2"]
  }
];

describe('PresentationOutline', () => {
  it('renders the presentation title', () => {
    render(<PresentationOutline title="Test Presentation" slides={mockSlides} />);
    expect(screen.getByText('Test Presentation')).toBeInTheDocument();
  });

  it('renders all slides with their titles', () => {
    render(<PresentationOutline title="Test Presentation" slides={mockSlides} />);
    expect(screen.getByText('1. Introduction')).toBeInTheDocument();
    expect(screen.getByText('2. Methods')).toBeInTheDocument();
  });

  it('renders all bullet points for each slide', () => {
    render(<PresentationOutline title="Test Presentation" slides={mockSlides} />);
    expect(screen.getByText('Point 1')).toBeInTheDocument();
    expect(screen.getByText('Point 2')).toBeInTheDocument();
    expect(screen.getByText('Point 3')).toBeInTheDocument();
    expect(screen.getByText('Method 1')).toBeInTheDocument();
    expect(screen.getByText('Method 2')).toBeInTheDocument();
  });

  it('renders correctly with empty slides array', () => {
    render(<PresentationOutline title="Test Presentation" slides={[]} />);
    expect(screen.getByText('Test Presentation')).toBeInTheDocument();
    expect(screen.getByText('Test Presentation').nextSibling).toBeEmpty();
  });
}); 