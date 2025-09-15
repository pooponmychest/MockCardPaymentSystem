import os
from dotenv import load_dotenv

load_dotenv()

Stripe_Secret_Key = os.getenv("STRIPE_SECRET_KEY")
Database_URL = os.getenv("DATABASE_URL", "sqlite:///./payments.db")