from fastapi import FastAPI
from app.db import Base, engine
from app.routes import payments

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Card Payments System")

app.include_router(payments.router)

@app.get("/")
def root():
    return {"message": "Card Payment System API"}
