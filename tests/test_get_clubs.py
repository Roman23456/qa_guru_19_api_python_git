import requests
from jsonschema import validate

from shemas.response_get_clubs_shema import clubs_response


def test_status_code():
    response = requests.get("https://book-club.qa.guru/api/v1/clubs/")

    body = response.json()
    validate(body, schema=clubs_response)
    assert response.status_code == 200
    print("\nТест пройден: статус код 200")


def test_search_clubs_title():
    response = requests.get("https://book-club.qa.guru/api/v1/clubs/?search=Сети")

    body = response.json()
    validate(body, schema=clubs_response)

    assert body["results"][0]["bookTitle"] == "Сети"
    assert body["results"][0]["bookAuthors"] == "Таненбаум"
    assert body["results"][0]["publicationYear"] == 1985
    print("\nТест пройден: поиск  работает корректно")


def test_clubs_page_size():
    response = requests.get("https://book-club.qa.guru/api/v1/clubs/")
    body = response.json()

    validate(body, schema=clubs_response)

    assert len(body["results"]) == 50
    print("\nТест пройден: page_size=50 работает корректно")
