from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_health():
    assert client.get("/api/health").json() == {"status": "ok"}


def test_create_and_list_expense():
    r = client.post("/api/expenses",
                    json={"title": "Coffee", "amount": 3.5, "category": "Food"})
    assert r.status_code == 201
    titles = [e["title"] for e in client.get("/api/expenses").json()]
    assert "Coffee" in titles


def test_rejects_negative_amount():
    r = client.post("/api/expenses",
                    json={"title": "Bad", "amount": -5, "category": "Food"})
    assert r.status_code == 422


def test_summary_has_categories():
    assert len(client.get("/api/summary").json()) >= 1
