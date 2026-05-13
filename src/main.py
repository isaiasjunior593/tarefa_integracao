from fastapi import FastAPI
from src.routes import router

app = FastAPI(title='API Trabalho N703', version='1.0.0')
app.include_router(router, prefix='/api/v1')