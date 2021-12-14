import pytest
from starlette.testclient import TestClient

from app.main import app


@pytest.fixture(scope="module")
def test_app():
    ''' Define test client '''
    client = TestClient(app)
    yield client  # testing happens here
