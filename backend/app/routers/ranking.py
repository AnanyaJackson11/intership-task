from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas import RankingEntry
from app.services.ranking_service import get_rankings

router = APIRouter(
    prefix="/ranking",
    tags=["Ranking"]
)


@router.get(
    "",
    response_model=List[RankingEntry]
)
def ranking(
    db: Session = Depends(get_db)
):
    return get_rankings(db)