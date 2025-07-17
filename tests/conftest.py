from fastapi.testclient import TestClient
from fast_api.app import app
import pytest


@pytest.fixture
def client():
    # Arrange
    return TestClient(app)
