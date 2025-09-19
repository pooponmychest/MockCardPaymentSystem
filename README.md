# MockCardPayment
This project uses Stripe in order to simulate how a real card payment is processed.

## Quick use:
- Clone repo 
- 'python -m venv venv' to isolate dependencies 
- Windows: 'venv\Scripts\activate' 
- pip install -r requirements.txt 
- Manually add a new file .env with real StripeSecretKey (use .env.example as template for .env) 
- Start backend in terminal 'uvicorn app.main:app --reload
- Go to '`<IpAddress>`/docs'

## Features
- Create and confirm Stripe PaymentIntents
- Store transaction records in a SQLite database
- Handle multiple currencies (including zero-decimal)
- Test payments safely using Stripe sandbox
- API documentation with Swagger UI

## For future implementation:
- Frontend collects card info vis Stripe Elements
- Sends payment_method token to backend
- Backend creats/confirms PaymentIntenth with the token instead of placeholder

### Tools: 
- Python 
- FastAPI (Web framework for backend APIs)
- Uvicorn (ASGI server to run FastAPI)
- SQLAlchemy (ORM for managing database models & transactions)
- SQLite (Lightweight database for storing transactions)
- Stripe Python SDK (Payment gateway integration)
- python-dotenv (Manage .env files for secret keys)
- SwaggerUI (Test API endpoints without frontend)