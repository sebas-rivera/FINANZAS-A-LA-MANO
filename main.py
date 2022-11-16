from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def home():
    return {"message": "Hello World"}

#uvicorn main:app --reload