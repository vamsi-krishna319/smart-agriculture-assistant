from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel


class AnalysisResponse(BaseModel):

    analysis_id: int

    crop_name: str

    farmer: str

    location: str

    disease: str

    confidence: float

    severity: str

    symptoms: List[str]

    weather: dict

    weather_advice: str

    soil_recommendation: str

    fertilizer: str

    irrigation: str

    prevention: str

    organic_treatment: str

    chemical_treatment: str

    report: str


class AnalysisDB(BaseModel):

    id: int

    farmer_id: int

    crop_name: str

    image_path: str

    disease: Optional[str] = None

    confidence: Optional[float] = None

    severity: Optional[str] = None

    symptoms: Optional[str] = None

    weather: Optional[str] = None

    fertilizer: Optional[str] = None

    irrigation: Optional[str] = None

    prevention: Optional[str] = None

    organic_treatment: Optional[str] = None

    chemical_treatment: Optional[str] = None

    soil_recommendation: Optional[str] = None

    created_at: datetime

    class Config:
        from_attributes = True