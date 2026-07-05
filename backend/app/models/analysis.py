from datetime import datetime

from sqlalchemy import (
    Column,
    Integer,
    String,
    Float,
    ForeignKey,
    DateTime,
    Text
)
from sqlalchemy.orm import relationship

from app.database.database import Base


class Analysis(Base):
    __tablename__ = "analysis"

    id = Column(Integer, primary_key=True, index=True)

    farmer_id = Column(
        Integer,
        ForeignKey("farmers.id"),
        nullable=False
    )

    crop_name = Column(
        String(100),
        nullable=False
    )

    image_path = Column(
        String,
        nullable=False
    )

    # Gemini Output
    disease = Column(String(200))
    confidence = Column(Float)
    severity = Column(String(50))
    symptoms = Column(Text)

    # CrewAI Output
    weather = Column(Text)
    fertilizer = Column(Text)
    irrigation = Column(Text)
    prevention = Column(Text)
    organic_treatment = Column(Text)
    chemical_treatment = Column(Text)
    soil_recommendation = Column(Text)

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )

    farmer = relationship(
        "Farmer",
        back_populates="analyses"
    )

    report = relationship(
        "Report",
        back_populates="analysis",
        uselist=False,
        cascade="all, delete-orphan"
    )