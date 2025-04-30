import os

DATABASE_URL = os.environ.get("DATABASE_URL")

if not DATABASE_URL:
    # fallback para SQLite local
    DATABASE_URL = "sqlite:///local.db"