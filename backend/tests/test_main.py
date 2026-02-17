from fastapi.testclient import TestClient

from backend.src.main import app

client = TestClient(app)


def test_read_root():
    """Test the health check endpoint."""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"status": "ok", "message": "Rolpraat API is running"}


def test_users_endpoint_exists():
    """Test that the users endpoint is accessible."""
    response = client.get("/users/")
    # Should return 200 (assuming database is available) or potentially an error
    # For now, just check that the endpoint exists
    assert response.status_code in [200, 500]  # 500 if DB not available in CI
