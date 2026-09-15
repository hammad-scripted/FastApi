from fastapi import FastAPI

app = FastAPI(
    title="My First API",
    description="This is my first API",
    version="1.0.0",
    openapi_url="/openapi.json",
    docs_url="/docs",
    redoc_url="/redoc",
)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/about")
def about():
    return {"message": "About", "version": "1.0.0", "author": "John Doe"}
