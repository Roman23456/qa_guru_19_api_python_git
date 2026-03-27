import requests
from jsonschema import validate

from shemas.response_get_clubs_reviews_shema import response_review


def test_status_code():
    response = requests.get("https://book-club.qa.guru/api/v1/clubs/reviews/")

    body = response.json()
    validate(body, schema=response_review)
    assert response.status_code == 200


def test_filter_reviews_by_club_parameter():
    response = requests.get("https://book-club.qa.guru/api/v1/clubs/reviews/?club=169")

    body = response.json()
    validate(body, schema=response_review)

    assert body["results"][0]["club"] == 169
    assert body["results"][0]["review"] == "Пробный отзыв"
    assert body["results"][0]["user"]["username"] == "Hung5233"
    assert body["results"][0]["user"]["id"] == 522
    print("\nТест пройден: фильтрация отзывов по club")

    # Проверка наличия обязательных заголовков
    assert "Date" in response.headers
    assert "Content-Length" in response.headers
    assert "Connection" in response.headers
    print("\nТест пройдет: Проверили наличия обязательных полей")
