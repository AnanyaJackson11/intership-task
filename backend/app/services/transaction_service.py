from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from app.models import User, Transaction
from app.schemas import TransactionRequest
from app.logger import logger


class DuplicateTransactionError(Exception):
    """Raised when a transaction with the same transaction_id already exists."""
    pass


def create_transaction(db: Session, transaction: TransactionRequest):
    """
    Creates a transaction atomically.

    Features:
    - Prevent duplicate transactions
    - Automatically create user if needed
    - Update user statistics
    - Prevent transaction abuse
    """

    # -------------------------
    # Prevent duplicate request
    # -------------------------
    existing = (
        db.query(Transaction)
        .filter(Transaction.transaction_id == transaction.transaction_id)
        .first()
    )

    if existing:
        logger.warning(
            f"Duplicate transaction attempted: {transaction.transaction_id}"
        )
        raise DuplicateTransactionError()

    # -------------------------
    # Prevent abuse
    # -------------------------
    if transaction.amount < 10:
        raise ValueError("Minimum transaction amount is ₹10.")

    if transaction.amount > 100000:
        raise ValueError("Transaction amount exceeds allowed limit.")

    # -------------------------
    # Find or create user
    # -------------------------
    user = (
        db.query(User)
        .filter(User.id == transaction.user_id)
        .first()
    )

    if not user:
        user = User(id=transaction.user_id)
        db.add(user)
        db.flush()

    # -------------------------
    # Reward calculation
    # -------------------------
    points = round(transaction.amount * 0.10, 2)

    # -------------------------
    # Create transaction
    # -------------------------
    new_transaction = Transaction(
        transaction_id=transaction.transaction_id,
        user_id=transaction.user_id,
        amount=transaction.amount,
        points=points,
    )

    db.add(new_transaction)

    # -------------------------
    # Update user stats
    # -------------------------
    user.total_spent += transaction.amount
    user.total_points += points
    user.transaction_count += 1

    try:
        db.commit()

    except IntegrityError:
        db.rollback()
        logger.warning(
            f"Duplicate transaction detected by DB: {transaction.transaction_id}"
        )
        raise DuplicateTransactionError()

    db.refresh(user)

    logger.info(
        f"Transaction {transaction.transaction_id} created for {user.id}"
    )

    return {
        "message": "Transaction created successfully",
        "transaction_id": transaction.transaction_id,
        "points_earned": points,
        "user": {
            "user_id": user.id,
            "total_spent": user.total_spent,
            "total_points": user.total_points,
            "transaction_count": user.transaction_count,
        },
    }