import os
from contextlib import closing

import pymysql
from pymysql.cursors import DictCursor
from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(title="ExpenseTrack API")


def get_conn():
    return pymysql.connect(
        host=os.getenv("DB_HOST", "127.0.0.1"),
        port=int(os.getenv("DB_PORT", "3306")),
        user=os.getenv("DB_USER", "app"),
        password=os.getenv("DB_PASSWORD", "app"),
        database=os.getenv("DB_NAME", "expenses"),
        cursorclass=DictCursor,
    )


class ExpenseIn(BaseModel):
    title: str = Field(min_length=1, max_length=100)
    amount: float = Field(gt=0)
    category: str = Field(min_length=1, max_length=50)


@app.get("/api/health")
def health():
    return {"status": "ok"}


@app.get("/api/expenses")
def list_expenses():
    with closing(get_conn()) as conn, conn.cursor() as cur:
        cur.execute(
            "SELECT id, title, amount, category, created_at "
            "FROM expenses ORDER BY created_at DESC, id DESC"
        )
        return cur.fetchall()


@app.post("/api/expenses", status_code=201)
def add_expense(e: ExpenseIn):
    with closing(get_conn()) as conn, conn.cursor() as cur:
        cur.execute(
            "INSERT INTO expenses (title, amount, category) VALUES (%s, %s, %s)",
            (e.title, e.amount, e.category),
        )
        conn.commit()
        return {"id": cur.lastrowid}


@app.get("/api/summary")
def summary():
    with closing(get_conn()) as conn, conn.cursor() as cur:
        cur.execute(
            "SELECT category, COUNT(*) AS count, SUM(amount) AS total "
            "FROM expenses GROUP BY category ORDER BY total DESC"
        )
        return cur.fetchall()
