import json
from utils.api import GoogleMapsApi


class TestCreatePlace:
    """Класс, содержащий тест по работе с локацией"""

    def test_create_new_place(self):
        """Тест по созданию и проверке новой локации"""
        print("Метод POST по созданию новой локации")
        result_post = GoogleMapsApi.create_new_place()  # вызов метода по созданию новой локации

        check_post = result_post.json()
        place_id = check_post.get("place_id")  # получения place_id для метода GET

        print("Метод GET POST для проверки созданной локации")
        result_get = GoogleMapsApi.get_new_place(place_id)  # отправка метода Get

