from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.models.farmer import Farmer
from app.schemas.farmer import FarmerCreate, FarmerResponse

router = APIRouter(
    prefix="/farmers",
    tags=["Farmers"]
)


@router.post("/", response_model=FarmerResponse)
def create_farmer(
    farmer: FarmerCreate,
    db: Session = Depends(get_db)
):
    new_farmer = Farmer(
        name=farmer.name,
        location=farmer.location
    )

    db.add(new_farmer)
    db.commit()
    db.refresh(new_farmer)

    return new_farmer


@router.get("/", response_model=list[FarmerResponse])
def get_farmers(db: Session = Depends(get_db)):
    return db.query(Farmer).all()