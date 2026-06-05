from fastapi import FastAPI
from pydantic import BaseModel

from app.gateway.router import AIGateway

app = FastAPI(
    title="OpsMind",
    version="0.1.0"
)


class GenerateRequest(BaseModel):
    prompt: str


@app.get("/")
def health():

    return {
        "status": "healthy",
        "service": "OpsMind"
    }


@app.post("/api/v1/generate")
def generate(request: GenerateRequest):

    result = AIGateway.route(
        request.prompt
    )

    return {
        "terraform": result
    }
