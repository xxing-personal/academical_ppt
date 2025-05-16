export interface Slide {
  title: string;
  points: string[];
}

export interface PresentationContent {
  title: string;
  slides: Slide[];
}

export interface PresentationResponse {
  content: PresentationContent;
  message: string;
  slidev_url: string;
} 