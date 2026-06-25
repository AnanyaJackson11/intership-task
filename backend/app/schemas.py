from pydantic import BaseModel
from pydantic import Field

from typing import List


class RankingEntry(BaseModel):
    rank: int
    user_id: str
    score: float
    total_points: float
    transaction_count: int

class TransactionRequest(BaseModel):
    transaction_id: str

    user_id: str

    amount: float = Field(gt=0)

class TransactionResponse(BaseModel):
    message: str
    transaction_id: str
    points_earned: float
    user: dict

class UserSummary(BaseModel):
    user_id: str
    total_spent: float
    total_points: float
    transaction_count: int
    average_transaction: float



class RankingResponse(BaseModel):
    rank: int

    user_id: str

    score: float