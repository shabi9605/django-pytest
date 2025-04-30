import pytest

import logging
logger = logging.getLogger(__name__)

@pytest.mark.django_db
def test_authenticated_cred_create(auth_client):
    data = {"title": "Test Book", "description": "Tester"}
    logger.info(f"{data=}")
    response = auth_client.post("/api/cred/", data, format="json")
    logger.info(f"{response.data=}")
    assert response.status_code == 201
    assert response.data["title"] == "Test Book"