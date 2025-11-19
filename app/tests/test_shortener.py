import sys
from pathlib import Path


sys.path.insert(0, str(Path(__file__).parent.parent))

from fastapi.testclient import TestClient

from main import app




def test_success_shorten_url_creation():
    client = TestClient(app)
    response = client.post("/shorten", json={"original_url": "https://www.google.com"})
    assert response.status_code == 200
    assert response.json()["message"] == "Short url created successfully"
    short_code = response.json()["short_code"]
    assert len(short_code) > 0
    
def test_duplicate_url_return_same_record():
    client = TestClient(app)
    first = client.post("/shorten", json={"original_url": "https://google.com"})
    second = client.post("/shorten", json={"original_url": "https://google.com"})

    assert first.status_code == 200
    assert second.status_code == 200

    assert first.json()["id"] == second.json()["id"]