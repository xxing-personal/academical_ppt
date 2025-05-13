import { Slide } from '../types/presentation';

interface PresentationOutlineProps {
  title: string;
  slides: Slide[];
}

const PresentationOutline = ({ title, slides }: PresentationOutlineProps) => {
  return (
    <div className="presentation-outline">
      <h2 className="presentation-title">{title}</h2>
      <div className="slides-container">
        {slides.map((slide, index) => (
          <div key={index} className="slide-card">
            <h3 className="slide-title">
              {index + 1}. {slide.title}
            </h3>
            <ul className="slide-points">
              {slide.points.map((point, pointIndex) => (
                <li key={pointIndex} className="slide-point">
                  {point}
                </li>
              ))}
            </ul>
          </div>
        ))}
      </div>
    </div>
  );
};

export default PresentationOutline; 