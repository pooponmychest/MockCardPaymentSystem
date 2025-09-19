import stripe
from app.config import STRIPE_SECRET_KEY

stripe.api_key = STRIPE_SECRET_KEY

ZERO_DECIMAL_CURRENCIES = {"jpy", "krw"}

def create_payment(amount: float, currency: str = "usd"):
  normalized_currency = currency.lower()

  if normalized_currency in ZERO_DECIMAL_CURRENCIES:
    stripe_amount = int(amount)
  else:
    stripe_amount = int(amount * 100)

  intent = stripe.PaymentIntent.create(
    amount=stripe_amount,
    currency=normalized_currency,
    payment_method_types=["card"],
  )
  ## For future real payments instead of Stripe Test Token
  #return intent
  
  # **Optional for testing only**: immediately confirm with Stripe test token
  confirmed = stripe.PaymentIntent.confirm(
    intent.id,
    payment_method="pm_card_visa"  # Stripe test card token
  )

  return confirmed