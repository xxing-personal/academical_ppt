# Academical PPT Generator

A web application that generates presentation slides from academic papers using AI. The application uses OpenAI's GPT model to analyze academic papers and create structured presentations, which are then rendered using Slidev.

## Features

- PDF upload and text extraction
- AI-powered presentation generation
- Interactive slide preview with Slidev
- Support for multiple presentation formats
- Automatic slide organization and storage

## Project Structure

```
academical_ppt/
├── backend/
│   ├── app/
│   │   ├── api/
│   │   ├── core/
│   │   ├── schemas/
│   │   ├── services/
│   │   └── utils/
│   ├── slidev_output/
│   │   └── public/
│   └── uploads/
└── frontend/
    ├── src/
    │   ├── components/
    │   └── types/
    └── public/
```

## Prerequisites

- Python 3.8+
- Node.js 16+
- OpenAI API key

## Installation

1. Clone the repository:
```bash
git clone https://github.com/xxing-personal/academical_ppt.git
cd academical_ppt
```

2. Set up the backend:
```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\activate
pip install -r requirements.txt
```

3. Set up the frontend:
```bash
cd frontend
npm install
```

4. Configure environment variables:
Create a `.env` file in the backend directory with:
```
OPENAI_API_KEY=your_api_key_here
```

## Running the Application

1. Start the backend server:
```bash
cd backend
uvicorn app.main:app --reload
```

2. Start the frontend development server:
```bash
cd frontend
npm run dev
```

3. Access the application at `http://localhost:5173`

## Using Slidev

The application uses Slidev for rendering presentations. To start Slidev manually:

1. Navigate to the frontend directory:
```bash
cd frontend
```

2. Set the presentation title:
```bash
export PRESENTATION_TITLE="Your Presentation Title"
```

3. Start Slidev:
```bash
npm run start-slidev
```

The presentation will be available at:
- Main view: http://localhost:3030/
- Presenter mode: http://localhost:3030/presenter/
- Overview: http://localhost:3030/overview/

## Presentation Storage

- Generated presentations are stored in `backend/slidev_output/public/`
- Each presentation has its own directory named after the presentation title
- The most recent presentation is also saved as `slides.md` in the main `slidev_output/public/` directory

## Development

### Backend

- FastAPI for the API server
- OpenAI GPT for presentation generation
- PDF text extraction utilities
- Slidev integration for presentation rendering

### Frontend

- React with TypeScript
- Vite for development and building
- Axios for API communication
- Slidev for presentation rendering

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details. 