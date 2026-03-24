import requests


def test_clubs_page_size():
    print("\n=== Тест на проверку page_size=2 ===")

    params = {'page_size': 2}
    print(f"Параметры запроса: {params}")

    response = requests.get('https://book-club.qa.guru/api/v1/clubs/', params=params)

    print(f"Status code: {response.status_code}")
    print(f"Response body: {response.text}")

    assert response.status_code == 200

    body = response.json()
    print(f"Количество элементов в results: {len(body['results'])}")
    print(f"Всего записей (count): {body['count']}")

    assert len(body['results']) <= 2
    print("Тест пройден: page_size=2 работает корректно")