import requests


class Swapi:
    """Работа с новой локацией"""

    def __init__(self):
        self.base_url = "https://swapi.dev"  # базовая url
        # self.key = "?key=qaclick123"  # Параметр для всех запросов

    def check_new(self):
        get_resource = "/api/people/4/"
        get_url = self.base_url + get_resource
        print(get_url)
        result_get = requests.get(get_url)
        print(result_get.text)

    # def write_place_id_to_file(self):
    #     """Создаем файл и записываем в него 5шт place_id"""
    #     with open("list_place_id.txt", "w", encoding='utf-8') as file:
    #         [file.write(self.create_new_location() + "\n") for _ in range(5)]


new_place = Swapi()
new_place.check_new()

