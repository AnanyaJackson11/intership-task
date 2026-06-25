from app.models import User
from app.utils.scoring import calculate_score


def get_rankings(db):

    users = db.query(User).all()

    if not users:
        return []

    max_points = max(u.total_points for u in users)

    max_transactions = max(
        u.transaction_count for u in users
    )

    max_avg_spend = max(
        (
            u.total_spent / u.transaction_count
            if u.transaction_count
            else 0
        )
        for u in users
    )

    rankings = []

    for user in users:

        score = calculate_score(
            user,
            max_points,
            max_transactions,
            max_avg_spend
        )

        rankings.append({

            "user_id": user.id,

            "score": score,

            "total_points": user.total_points,

            "transaction_count": user.transaction_count

        })

    rankings.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    for i, row in enumerate(rankings):
        row["rank"] = i + 1

    return rankings