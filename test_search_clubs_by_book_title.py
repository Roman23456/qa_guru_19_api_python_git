import requests
from jsonschema import validate

from shemas.response_shema import status_response


def test_search_clubs_litle():
    response = requests.get('https://book-club.qa.guru/api/v1/clubs/?search=Сети')

    print("\nHeaders:", response.headers)
    print("\nStatus code:", response.status_code)
    print("\nBody", response.text)

    assert response.status_code == 200

    body = response.json()
    validate(body, schema=status_response)

    assert body['results'][0]['bookTitle'] == 'Сети'