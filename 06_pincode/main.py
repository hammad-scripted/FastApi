from fastapi import FastAPI
app=FastAPI(
    
    title="Pincode API",
    description="Auto fill city and state from Indian pincode during checkout",
    version="1.0.0",
    openapi_url="/openapi.json",
    docs_url="/docs",
    redoc_url="/redoc",
)


@app.get("/")
def root():
    return {"message": "Welcome to Pincode API"}





