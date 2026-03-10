from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .schemas import CodeRequest
from .llm_service import analyze_code, generate_docstring

app = FastAPI(title="AI Code Assistant")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "AI Code Assistant API running"}

@app.post("/review")
async def review_code(data: CodeRequest):
    result = await analyze_code(data.code)
    return {"review": result}

@app.post("/document")
async def document_code(data: CodeRequest):
    result = await generate_docstring(data.code)
    return {"documentation": result}
