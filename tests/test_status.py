import requests


def test_totaL_amount():
    response = requests.get('https://book-club.qa.guru/api/v1/clubs/')

    print("\nHeaders:", response.headers)
    print("\nStatus code:", response.status_code)
    print("\nBody", response.text)

    assert response.status_code == 200
