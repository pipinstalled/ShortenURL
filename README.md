# ShortenURL

Short url generator

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Create a `.env` file:
```env
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=localhost
DB_PORT=5432
DB_NAME=shortenurl
APP_NAME=URL Shortener
BASE_URL=http://localhost:8000
SHORT_CODE_LENGTH=6
```

3. Create database:
```bash
createdb shortenurl
```

4. Run migrations:
```bash
cd app
alembic upgrade head
```

## Run

```bash
cd app
uvicorn main:app --reload
```

API available at `http://localhost:8000`
Documentation at `http://localhost:8000/docs`

## API Endpoints

### POST /shorten
Create a short URL.

Request:
```json
{
  "original_url": "https://example.com"
}
```

Response:
```json
{
  "id": 1,
  "original_url": "https://example.com",
  "short_code": "http://localhost:8000/abc123",
  "created_at": "2024-01-01T12:00:00Z",
  "message": "Short url created successfully"
}
```

### GET /{short_code}
Redirect to the original URL.

### GET /stats/{short_code}
Get statistics for a shortened URL.

Response:
```json
{
  "original_url": "https://example.com",
  "short_code": "abc123",
  "created_at": "2024-01-01T12:00:00Z",
  "visits_count": 42
}
```

## Tests

```bash
cd app
pytest tests/
```
