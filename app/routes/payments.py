from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.payment_schema import PaymentRequest, PaymentResponse
from app.models.transaction import Transaction
from app.services.stripe_services import create_payment
from app.db import SessionLocal

router = APIRouter(prefix="/payments", tags=["Payments"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=PaymentResponse)
def process_payment(request: PaymentRequest, db: Session = Depends(get_db)):
    intent = create_payment(request.amount, request.currency)

    transaction = Transaction(
        stripe_payment_id=intent["id"],
        amount=request.amount,
        currency=request.currency.lower(),
        status=intent["status"],
    )    
    db.add(transaction)
    db.commit()
    db.refresh(transaction)

    return PaymentResponse(
        transaction_id=transaction.id,
        stripe_payment_id=transaction.stripe_payment_id,
        status=transaction.status,
        currency=transaction.currency,
        amount=transaction.amount,
    )
