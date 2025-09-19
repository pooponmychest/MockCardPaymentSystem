import os
from dotenv import load_dotenv

load_dotenv()

STRIPE_SECRET_KEY = os.getenv("STRIPE_SECRET_KEY")
Database_URL = os.getenv("DATABASE_URL", "sqlite:///./payments.db")