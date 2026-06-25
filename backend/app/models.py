from sqlalchemy import Column, Integer, Float, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.database import Base


class User(Base):
    __tablename__ = "users"

    # Primary Key
    id = Column(String, primary_key=True, index=True)

    # User Statistics
    total_spent = Column(Float, default=0.0, nullable=False)
    total_points = Column(Float, default=0.0, nullable=False)
    transaction_count = Column(Integer, default=0, nullable=False)

    # Timestamp
    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False
    )

    # One User -> Many Transactions
    transactions = relationship(
        "Transaction",
        back_populates="user",
        cascade="all, delete-orphan"
    )


class Transaction(Base):
    __tablename__ = "transactions"

    # Internal Database ID
    id = Column(Integer, primary_key=True, index=True)

    # Idempotency Key (Provided by Client)
    transaction_id = Column(
        String,
        unique=True,
        nullable=False,
        index=True
    )

    # Foreign Key
    user_id = Column(
        String,
        ForeignKey("users.id"),
        nullable=False,
        index=True
    )

    # Transaction Details
    amount = Column(Float, nullable=False)
    points = Column(Float, nullable=False)

    # Optional: helps with future expansion
    status = Column(
        String,
        default="SUCCESS",
        nullable=False
    )

    # Timestamp
    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False
    )

    # Relationship back to User
    user = relationship(
        "User",
        back_populates="transactions"
    )