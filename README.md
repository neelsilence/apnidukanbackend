# Grocery Backend (FastAPI)

A clean FastAPI starter to power your grocery app. Includes:
- Product API matching your Flutter model
- SQLite by default (easy local dev), swappable to Postgres/MySQL
- CORS enabled (works with Flutter Web)
- Seed script with sample products
- Ready for more APIs as you grow

## Project Structure
```
fastapi-grocery-backend/
├─ app/
│  ├─ api/
│  │  ├─ routes/
│  │  │  └─ products.py
│  │  └─ deps.py
│  ├─ core/
│  │  └─ config.py
│  ├─ db/
│  │  ├─ base.py
│  │  ├─ session.py
│  │  └─ init_db.py (inlined in session.py:init_db)
│  ├─ models/
│  │  └─ product.py
│  ├─ schemas/
│  │  └─ product.py
│  └─ main.py
├─ scripts/
│  └─ seed_data.py
├─ tests/
│  └─ test_products.py
├─ .env.example
├─ requirements.txt
└─ README.md
```

## Quick Start

> Requirements: Python 3.11+ recommended

1) **Create & activate a virtualenv**
```bash
python -m venv .venv
# Windows
.\.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
```

2) **Install dependencies**
```bash
pip install -r requirements.txt
```

3) **(Optional) Configure environment**
```bash
cp .env.example .env
# Edit .env if you want to change DB to Postgres/MySQL, or set CORS origins.
```

4) **Seed the database with sample products**
```bash
python -m scripts.seed_data
```

5) **Run the server**
```bash
uvicorn app.main:app --reload --port 8000
```
Open the interactive API docs at: `http://127.0.0.1:8000/docs`

## Endpoints

- `GET /health` – health check
- `GET /api/v1/products` – list products
  - Query params: `q, tag, min_price, max_price, sort_by (id|name|price|rating), order (asc|desc), limit, offset`
- `GET /api/v1/products/{id}` – get one
- `POST /api/v1/products` – create one (payload matches your Flutter model)

### Response shape (matches your Flutter `Product`)
```json
{
  "id": 1,
  "name": "Aashirvaad Atta",
  "imageUrl": "https://example.com/img.jpg",
  "tag": "Best Sale",
  "weight": "5kg",
  "price": 289.0,
  "rating": 4.5,
  "oldPrice": 320.0
}
```

## Switch to Postgres (later)
1. Run a Postgres instance
2. Set `SQLALCHEMY_DATABASE_URI="postgresql+psycopg://user:pass@host:5432/db"` in `.env`
3. Restart the server. SQLAlchemy will create tables automatically on first run.

> Tip: For production use, add migrations (Alembic).

## Run tests
```bash
pip install pytest
pytest -q
```

## Notes
- CORS is `*` by default so your Flutter web app can call it during dev.
- The Pydantic schema uses aliases so the JSON field names exactly match your Dart model (`imageUrl`, `oldPrice`).
```
