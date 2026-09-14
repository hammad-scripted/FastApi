from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hammad")
async def root():
    return {
        "message": "Hello Hammad",
        "name": "Hammad",
        "age": 25,
        "gender": "male",
        "country": "India",
        "city": "New Delhi",
    }
