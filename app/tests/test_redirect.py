import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from fastapi.testclient import TestClient
from main import app
from core.config import settings

client = TestClient(app)

def test_not_found_url():
    response = client.get(f"/abc123", allow_redirects=False)

    assert response.status_code == 404
    
    
    
def test_success_redirect_url():
    create = client.post("/shorten", json={"original_url": "https://google.com"})
    code = create.json()["short_code"].split("/")[-1]
    print(code)
    
    response = client.get(f"/{code}", allow_redirects=False)

    assert response.status_code == 302
    assert response.headers["location"] == "https://google.com"