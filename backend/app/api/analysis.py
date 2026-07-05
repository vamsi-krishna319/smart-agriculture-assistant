import os
import shutil

from fastapi import APIRouter, UploadFile, File, Form, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.models.analysis import Analysis
from app.services.analysis_service import AnalysisService

router = APIRouter(
    prefix="/analysis",
    tags=["Crop Analysis"]
)

UPLOAD_DIR = "uploads"

os.makedirs(UPLOAD_DIR, exist_ok=True)


#@router.post("/")

from app.schemas.analysis import AnalysisResponse


@router.post(
    "/",
    response_model=dict
)
def analyze_crop(
    farmer_id: int = Form(...),
    crop_name: str = Form(...),
    image: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    try:

        # -----------------------------------------
        # Save Uploaded Image
        # -----------------------------------------

        image_path = os.path.join(
            UPLOAD_DIR,
            image.filename
        )

        with open(image_path, "wb") as buffer:
            shutil.copyfileobj(image.file, buffer)

        # -----------------------------------------
        # Create Initial Analysis Record
        # -----------------------------------------

        analysis = Analysis(
            farmer_id=farmer_id,
            crop_name=crop_name,
            image_path=image_path
        )

        db.add(analysis)
        db.commit()
        db.refresh(analysis)

        # -----------------------------------------
        # Run Complete AI Pipeline
        # -----------------------------------------

        result = AnalysisService.analyze_crop(
            analysis.id,
            db
        )

        return {
            "success": True,
            "message": "Crop analysis completed successfully.",
            "data": result
        }

    except Exception as e:

        db.rollback()

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )