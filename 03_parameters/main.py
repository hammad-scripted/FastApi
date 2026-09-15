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


@app.get("/user/{user_id}")
async def get_user(user_id: int):
    return {"user_id": user_id}

@app.get("/user/{user_id}/name/{name}")
async def get_user_name(user_id: int, name: str):
    return {"user_id": user_id, "name": name}