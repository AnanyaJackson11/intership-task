from sqlalchemy.orm import Session

from app.models import User


def get_user_summary(db: Session, user_id: str):

    user = (
        db.query(User)
        .filter(User.id == user_id)
        .first()
    )

    if not user:
        return None

    average = (
        user.total_spent / user.transaction_count
        if user.transaction_count
        else 0
    )

    return {
        "user_id": user.id,
        "total_spent": round(user.total_spent, 2),
        "total_points": round(user.total_points, 2),
        "transaction_count": user.transaction_count,
        "average_transaction": round(average, 2)
    }