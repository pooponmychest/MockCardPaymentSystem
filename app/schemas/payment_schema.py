from pydantic import BaseModel, Field

class PaymentRequest(BaseModel):
  amount: float
  currency: str = Field(..., min_length=3, max_length=3)  # ISO currency code

class PaymentResponse(BaseModel):
  transaction_id: int
  stripe_payment_id: str
  status: str
  amount: float
  currency: str