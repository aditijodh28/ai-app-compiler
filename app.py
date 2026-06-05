from fastapi import FastAPI
from pipeline import *
from validator import *
from repair import *

app = FastAPI()

@app.get("/")
def home():
    return {
        "message": "AI App Compiler Running"
    }

@app.post("/generate")
def generate(prompt: str):

    intent = extract_intent(prompt)

    design = system_design(intent)

    spec = generate_schema(design)

    errors = validate(spec)

    if errors:
        spec = repair(spec, errors)

    return {
        "intent": intent,
        "design": design,
        "spec": spec,
        "errors": errors
    }