from fastapi import FastAPI
app=FastAPI(
    
    title="Chai Menu API",
    description="This is a menu for chai ",
    version="1.0.0",
    openapi_url="/openapi.json",
    docs_url="/docs",
    redoc_url="/redoc",
)


@app.get("/")
def root():
    return {"message": "Welcome to Chai Menu API"}

