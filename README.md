# Reward Ranking System

## Live Demo

**Frontend (Vercel):**

> *(Insert your Vercel URL here)*

**Backend (Render):**

> https://internship-task-api-q3a8.onrender.com

---

# Project Overview

The Reward Ranking System is a full-stack application built using **FastAPI**, **React**, and **SQLite** that allows users to submit purchase transactions, calculate reward points, view user summaries, and display a ranked leaderboard.

The application focuses on backend engineering fundamentals including:

* REST API design
* Request validation
* Duplicate transaction prevention
* Database consistency
* Ranking fairness
* Clean architecture
* Deployment

---

# Tech Stack

## Backend

* FastAPI
* SQLAlchemy
* SQLite
* Pydantic
* Uvicorn

## Frontend

* React
* Vite
* Axios
* CSS

## Deployment

* Backend: Render
* Frontend: Vercel

---

# Project Structure

```
backend/
│
├── app/
│   ├── routers/
│   ├── services/
│   ├── utils/
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   └── main.py
│
├── tests/
└── requirements.txt

frontend/
│
├── src/
│   ├── components/
│   ├── services/
│   └── App.jsx
```

---

# API Endpoints

## POST /transaction

Creates a new transaction.

Example Request

```json
{
    "transaction_id":"txn001",
    "user_id":"john",
    "amount":1500
}
```

Response

```json
{
    "message":"Transaction created successfully"
}
```

---

## GET /summary/{user_id}

Returns

* Total amount spent
* Reward points
* Number of transactions
* Average transaction amount

---

## GET /ranking

Returns all users ranked according to their reward score.

---

# Ranking Logic

Each transaction earns reward points based on purchase amount.

The leaderboard score considers multiple factors:

* Total reward points
* Transaction count

This prevents users with only one large transaction from unfairly dominating the leaderboard.

---

# Duplicate Request Prevention

Every transaction requires a unique transaction_id.

If a duplicate transaction ID is submitted:

* HTTP 409 Conflict is returned.
* Transaction is not processed again.

This prevents accidental duplicate submissions.

---

# Validation

The backend validates:

* Required fields
* Positive transaction amounts
* Unique transaction IDs

Invalid requests return appropriate HTTP status codes.

---

# Data Consistency

The application uses SQLAlchemy transactions to ensure atomic database updates.

If any operation fails, the transaction is rolled back automatically.

---

# Error Handling

The application gracefully handles:

* Invalid inputs
* Missing users
* Duplicate transactions
* Database failures

---

# Running Locally

Backend

```bash
cd backend

pip install -r requirements.txt

uvicorn app.main:app --reload
```

Backend URL

```
http://127.0.0.1:8000
```

Swagger

```
http://127.0.0.1:8000/docs
```

Frontend

```bash
cd frontend

npm install

npm run dev
```

Frontend URL

```
http://localhost:5173
```

---

# Testing

Run

```bash
pytest
```

---

# Deployment

Backend deployed using Render.

Frontend deployed using Vercel.

---

# Future Improvements

* JWT Authentication
* Redis caching
* PostgreSQL
* Docker
* CI/CD using GitHub Actions
* Rate limiting
* Pagination
* Advanced analytics dashboard
