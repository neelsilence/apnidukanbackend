from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.db.session import init_db
from app.api.routes import products

app = FastAPI(title=settings.APP_NAME)

# CORS - allow all by default (good for dev; tighten for prod)
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOW_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize DB & tables
init_db()

# Routers
app.include_router(products.router, prefix="/api/v1")


@app.get("/")
def root():
    return {"message": "OK", "app": settings.APP_NAME}


@app.get("/health")
def health():
    return {"status": "healthy"}
