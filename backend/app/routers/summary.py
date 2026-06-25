from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas import UserSummary
from app.services.summary_service import get_user_summary

router = APIRouter(
    prefix="/summary",
    tags=["Summary"]
)


@router.get(
    "/{user_id}",
    response_model=UserSummary
)
def summary(
    user_id: str,
    db: Session = Depends(get_db)
):

    data = get_user_summary(db, user_id)

    if not data:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return data