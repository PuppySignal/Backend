from fastapi import APIRouter, Depends
from simplelimiter import Limiter
from sqlalchemy.orm import Session

from server.schemas.services import (
    DataSpeciesResponse,
    DataBreedResponse,
)
from server.models import Specie, Breed
from server.utils import get_db

router = APIRouter()

# Should we only let auth people to request data? I mean, this information is general and pretty vague
# But letting anyone request these endpoints could lead to an incident in the future?


@router.get(
    "/species",
    response_model=DataSpeciesResponse,
    dependencies=[Depends(Limiter("5/minute"))],
)
def get_species(limit: int = 10, offset: int = 0, db: Session = Depends(get_db)):
    species = db.query(Specie).limit(limit).offset(offset).all()

    return {"data": species}


@router.get(
    "/breeds",
    response_model=DataBreedResponse,
    dependencies=[Depends(Limiter("5/minute"))],
)
def get_breeds(specie_id: int, db: Session = Depends(get_db)):
    breeds = db.query(Breed).filter(Breed.specie_id == specie_id).all()

    return {"data": breeds}
