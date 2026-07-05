from pydantic import BaseModel


class FarmerCreate(BaseModel):
    name: str
    location: str


class FarmerResponse(BaseModel):
    id: int
    name: str
    location: str

    class Config:
        from_attributes = True