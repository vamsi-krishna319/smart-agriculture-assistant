import os

from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.models.report import Report

router = APIRouter(
    prefix="/reports",
    tags=["Reports"]
)


@router.get("/{analysis_id}")
def download_report(
    analysis_id: int,
    db: Session = Depends(get_db)
):
    """
    Download AI Generated PDF Report
    """

    report = (
        db.query(Report)
        .filter(Report.analysis_id == analysis_id)
        .first()
    )

    if report is None:
        raise HTTPException(
            status_code=404,
            detail="Report not found."
        )

    if not report.pdf_path:
        raise HTTPException(
            status_code=404,
            detail="PDF not generated."
        )

    if not os.path.exists(report.pdf_path):
        raise HTTPException(
            status_code=404,
            detail="PDF file does not exist."
        )

    return FileResponse(
        path=report.pdf_path,
        filename=f"Crop_Report_{analysis_id}.pdf",
        media_type="application/pdf"
    )