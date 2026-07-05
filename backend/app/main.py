from fastapi import FastAPI

from app.database.database import Base, engine

# Import models so SQLAlchemy creates tables
from app.models import Farmer, Analysis, Report

# Import routers
from app.api.farmer import router as farmer_router
from app.api.analysis import router as analysis_router
from app.api.report import router as report_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Smart Agriculture Assistant API")

app.include_router(farmer_router)
app.include_router(analysis_router)
app.include_router(report_router)


@app.get("/")
def home():
    return {
        "message": "Smart Agriculture Assistant API is running 🚀"
    }