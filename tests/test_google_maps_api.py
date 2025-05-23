import json
from utils.api import GoogleMapsApi
from utils.checking import Checking


class TestCreatePlace:
    """Класс, содержащий тест по работе с локацией"""

    def test_create_new_place(self):
        """
        Тест по работе с локацией.
        Post - Создали локацию
        Gеt - Проверили, что локация создалась
        Put - Изменили данные по локации
        Gеt - Проверили, что данные локации изменились
        Get - Проверили, что локация удалена
        """
        print("Метод POST по созданию новой локации")
        result_post = GoogleMapsApi.create_new_place()  # вызов метода по созданию новой локации
        Checking.check_status_code(result_post, 200)  # вызов метода по проверке статус-кода

        check_post = result_post.json()
        place_id = check_post.get("place_id")  # получения place_id для метода GET

        print("Метод GET для проверки созданной локации")
        result_get = GoogleMapsApi.get_new_place(place_id)  # отправка метода Get
        Checking.check_status_code(result_get, 200)  # вызов метода по проверке статус-кода

        print("Метод PUT для изменения локации")
        result_put = GoogleMapsApi.put_new_place(place_id)  # изменение данных о созданной локации
        Checking.check_status_code(result_put, 200)  # вызов метода по проверке статус-кода

        print("Метод GET для проверки измененной локации")
        result_get = GoogleMapsApi.get_new_place(place_id)  # отправка метода Get
        Checking.check_status_code(result_get, 200)  # вызов метода по проверке статус-кода

        print("Метод DELETE для удаления локации")
        result_delete = GoogleMapsApi.delete_new_place(place_id)  # удаление данных о созданной локации
        Checking.check_status_code(result_delete, 200)  # вызов метода по проверке статус-кода

        print("Метод GET для проверки удаленной локации")
        result_get = GoogleMapsApi.get_new_place(place_id)  # отправка метода Get
        Checking.check_status_code(result_get, 404)  # вызов метода по проверке статус-кода
