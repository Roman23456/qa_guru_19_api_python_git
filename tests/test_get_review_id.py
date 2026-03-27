import requests
from jsonschema import validate

from shemas.response_get_reviews_id_shema import reviews_response_id


def test_status_code():
    response = requests.get("https://book-club.qa.guru/api/v1/clubs/reviews/17/")

    body = response.json()
    validate(body, schema=reviews_response_id)
    assert response.status_code == 200
    print("\nТест пройден: статус код 200")


def test_search_review_id():
    response = requests.get("https://book-club.qa.guru/api/v1/clubs/reviews/17/")

    body = response.json()
    validate(body, schema=reviews_response_id)

    assert body["id"] == 17
    assert body["user"]["username"] == "Rebbecca"
    assert body["readPages"] == 45
    assert body["created"] == "2026-03-24T17:49:26.403013Z"
    print("\nТест пройден: поиск по review id работает корректно")
