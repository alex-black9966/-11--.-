import configuration
import requests
import data
# Алексей Чернов, 11-я когорта — Финальный проект. Инженер по тестированию плюс
# Выполнить запрос на создание заказа.
def create_order(body):
    return requests.post (configuration.URL_SERVICE + configuration.CREAT_ORDERS,
                         json=body)

# Выполнить запрос на получения заказа по треку заказа
def get_order(track_number):
    get_order_url = f"{configuration.URL_SERVICE}/api/v1/orders/track?t={track_number}"
    response = requests.get(get_order_url)
    return response


def test_order_creation_and_retrieval():
    response = create_order(data.order_body)

    track_number = response.json()["track"]
    print("Заказ создан. Номер трека:", track_number)


def test_order_creation_and_retrieval():
    response = create_order(data.order_body)

    track_number = response.json()["track"]
    print("Заказ создан. Номер трека:", track_number)

    # Проверяется, что по треку заказа можно получить данные о заказе
    order_response = get_order(track_number)
    # Проверить, что код ответа равен 200
    assert order_response.status_code == 200, f"Ошибка: {order_response.status_code}"
    order_data = order_response.json()
    print("Данные заказа:")
    print(order_data)