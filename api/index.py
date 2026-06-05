from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "AI App Compiler Running"}

@app.post("/generate")
def generate(prompt: str):
    return {
        "prompt": prompt,
        "status": "success"
    }