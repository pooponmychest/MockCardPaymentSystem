import stripe

# 1. Set Stripe test key
stripe.api_key = "sk_test_XXXXXXXXXXXXXXXXXXXX"

# 2. Create a PaymentIntent (like your FastAPI backend)
intent = stripe.PaymentIntent.create(
    amount=5000,  # $50
    currency="usd",
    payment_method_types=["card"]
)

# 3. Confirm the PaymentIntent with Stripe test card
confirmed = stripe.PaymentIntent.confirm(
    intent.id,
    payment_method_data={
        "type": "card",
        "card": {
            "number": "4242424242424242",
            "exp_month": 12,
            "exp_year": 34,
            "cvc": "123"
        }
    }
)

print("PaymentIntent status:", confirmed.status)
