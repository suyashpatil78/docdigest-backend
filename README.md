# PDF Summarizer API

A Flask-based API service that provides AI-powered summarization for PDF documents. This service leverages both OpenAI's GPT-4o and Google's Gemini models to generate concise, bullet-pointed summaries of PDF content.

## Features

- PDF text extraction and processing
- AI-powered summarization using multiple models:
  - OpenAI GPT-4o
  - Google Gemini 2.0 Flash
- Rate limiting to prevent abuse
- CORS support for cross-origin requests
- Self-pinging mechanism to keep the service alive

## API Endpoints

### `POST /api/summarize/pdf`

#### Request Body

- `file`: The PDF file to summarize
- `pdf_text`: The text extracted from the PDF

#### Response

- `summary`: The summary of the PDF file

### `POST /api/summarize/chat`

#### Request Body

- `pdf_text`: The text extracted from the PDF
- `question`: Question asked in the chat

#### Response

- `summary`: The answer to the question asked to the AI

## Setup and Installation

### Prerequisites

- Python 3.8+

### Environment Variables

Create a `.env` file with the following variables:

- `REDIS_URI`: The URI for the Redis instance
- `OPENAI_API_KEY`: The API key for the OpenAI instance
- `GEMINI_API_KEY`: The API key for the Gemini instance
- `SELF_URL`: your-deployed-app-url/ping

### Installation

1. Clone the repository
   ```
   git clone https://github.com/yourusername/pdf-summarizer-api.git
   cd pdf-summarizer-api
   ```

2. Install dependencies
   ```
   pip install -r requirements.txt
   ```

3. Run the application
   ```
   flask run
   ```

## Technical Details

### Architecture

- **Flask**: Web framework
- **OpenAI API**: For GPT-4o summarization
- **Google Genai**: For Gemini summarization
- **PyMuPDF (fitz)**: PDF text extraction
- **Flask-Limiter**: Rate limiting

### Rate Limiting

The API is configured with rate limiting to prevent abuse:
- Default: 15 requests per minute per IP address
- OPTIONS requests are exempt from rate limiting

## Deployment

The application is configured to work with Gunicorn for production deployment. The included `gunicorn_config.py` provides sensible defaults. You can run `gunicorn --config gunicorn_config.py app:app` as build command to deploy the application.
