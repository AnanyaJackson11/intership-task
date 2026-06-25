def normalize(value, maximum):
    if maximum == 0:
        return 0
    return value / maximum


def calculate_score(
    user,
    max_points,
    max_transactions,
    max_avg_spend,
):
    point_score = normalize(
        user.total_points,
        max_points
    )

    transaction_score = normalize(
        user.transaction_count,
        max_transactions
    )

    average_spend = (
        user.total_spent / user.transaction_count
        if user.transaction_count
        else 0
    )

    spend_score = normalize(
        average_spend,
        max_avg_spend
    )

    score = (
        point_score * 0.5
        + transaction_score * 0.3
        + spend_score * 0.2
    )

    return round(score * 100, 2)