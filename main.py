from fastapi import FastAPI

app = FastAPI()

# Hello World API method
@app.get("/")
async def root():
    return {"message": "Hello World"}