import json
from utils.api import GoogleMapsApi


class TestCreatePlace:
    """Класс, содержащий тест по работе с локацией"""

    def test_create_new_place(self):
        """Тест по созданию, проверке, изменению и удалению новой локации"""
        print("Метод POST по созданию новой локации")
        result_post = GoogleMapsApi.create_new_place()  # вызов метода по созданию новой локации

        check_post = result_post.json()
        place_id = check_post.get("place_id")  # получения place_id для метода GET

        print("Метод GET для проверки созданной локации")
        result_get = GoogleMapsApi.get_new_place(place_id)  # отправка метода Get

        print("Метод PUT для изменения локации")
        result_put = GoogleMapsApi.put_new_place(place_id)  # изменение данных о созданной локации

        print("Метод GET для проверки измененной локации")
        result_get = GoogleMapsApi.get_new_place(place_id)  # отправка метода Get
