import requests
from jsonschema import validate

from shemas.response_clubs_id_shema import clubs_response_id


def test_status_code():
    response = requests.get("https://book-club.qa.guru/api/v1/clubs/1")

    body = response.json()
    validate(body, schema=clubs_response_id)
    assert response.status_code == 200


def test_search_clubs_id():
    response = requests.get("https://book-club.qa.guru/api/v1/clubs/1/")

    body = response.json()
    validate(body, schema=clubs_response_id)

    assert body["id"] == 1
    print("Тест пройден: поиск клуба по id работает корректно")
