import json
from utils.api import GoogleMapsApi


class TestCreatePlace:
    """Класс, содержащий тест по работе с локацией"""

    def test_create_new_place(self):
        """Тест по созданию новой локации"""
        print("Метод POST по созданию новой локации")
        result_post = GoogleMapsApi.create_new_place()  # вызов метода по созданию новой локации
