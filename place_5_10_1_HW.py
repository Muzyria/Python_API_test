import requests


class Test_new_location:
    """Работа с новой локацией"""

    def __init__(self):
        self.base_url = "https://rahulshettyacademy.com"  # базовая url
        self.key = "?key=qaclick123"  # Параметр для всех запросов

    def delete_new_location(self, place_id):
        """Удаление новой локации методом DELETE"""
        delete_resource = "/maps/api/place/delete/json"
        delete_url = self.base_url + delete_resource + self.key
        print(delete_url)
        json_for_delete_new_location = {"place_id": place_id}
        result_delete = requests.put(delete_url, json=json_for_delete_new_location)
        print(result_delete.text)
        print(f'Статус код ответа : {result_delete.status_code}')
        assert 200 == result_delete.status_code
        print(f"Успешно!!! Удаление локации {place_id} прошло успешно")
        check_delete = result_delete.json()
        check_delete_info = check_delete.get("status")
        print(f'Сообщение : {check_delete_info}')
        assert check_delete_info == "OK"
        print("Сообщение верно")

    def check_new_location(self, num, place_id):
        """Проверка локации метод GET"""
        print(f'Проверка №{num} для {place_id}')
        get_resource = "/maps/api/place/get/json"
        get_url = self.base_url + get_resource + self.key + "&place_id=" + place_id
        print(get_url)
        result_get = requests.get(get_url)
        print(result_get.text)
        print(f'Статус код ответа : {result_get.status_code}')
        try:
            assert 200 == result_get.status_code
            print(f"Успешно!!! Проверка локации №{num} для {place_id}")
            print()
            return place_id
        except Exception:
            print(f"Провал!!! Локация №{num} для {place_id} не найдена !!!")
            print()

    def read_place_id_from_file(self):
        """Чтение place_id из файла и вызов метода GE, если локация есть то записывает place_id в list_place_id_2.txt"""
        with open("list_place_id.txt", "r", encoding='utf-8') as file, \
                open("list_place_id_2.txt", "w", encoding='utf-8') as file_w:
            [file_w.write(self.check_new_location(num, line)) for num, line in enumerate(file.read().split("\n"), 1) if line != '']

    def read_place_id_and_delete(self):
        """Чтение place_id из файла и вызов метода DELETE"""
        with open("list_place_id.txt", "r", encoding='utf-8') as file:
            [self.delete_new_location(line) for num, line in enumerate(file.read().split("\n"), 1)
             if num in (2, 4) and line != '']


new_place = Test_new_location()
new_place.read_place_id_and_delete()  # Удаление 2 и 4 локации
new_place.read_place_id_from_file()  # Проверка локаций и запись в новый файл
