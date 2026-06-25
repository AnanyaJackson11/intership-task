from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.schemas import TransactionRequest, TransactionResponse
from app.database import get_db
from app.schemas import TransactionRequest
from app.services.transaction_service import (
    create_transaction,
    DuplicateTransactionError,
)

router = APIRouter(
    prefix="/transaction",
    tags=["Transaction"],
)


@router.post(
    "",
    response_model=TransactionResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_new_transaction(
    request: TransactionRequest,
    db: Session = Depends(get_db),
):
    try:
        return create_transaction(db, request)

    except DuplicateTransactionError:
        raise HTTPException(
            status_code=409,
            detail="Duplicate transaction ID",
        )

    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e),
        )