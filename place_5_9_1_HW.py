import requests


class Test_new_location:
    """Работа с новой локацией"""

    def __init__(self):
        self.base_url = "https://rahulshettyacademy.com"  # базовая url
        self.key = "?key=qaclick123"  # Параметр для всех запросов

    def create_new_location(self):
        """Создание новой локации"""

        post_resource = "/maps/api/place/add/json"  # Ресурс метода пост
        post_url = self.base_url + post_resource + self.key
        print(post_url)
        json_for_create_new_location = {
                                        "location": {"lat": -38.383494, "lng": 33.427362},
                                        "accuracy": 50,
                                        "name": "Frontline house",
                                        "phone_number": "(+91) 983 893 3937",
                                        "address": "29, side layout, cohen 09",
                                        "types": ["shoe park", "shop"],
                                        "website": "http://google.com",
                                        "language": "French-IN"
                                         }

        result_post = requests.post(post_url, json=json_for_create_new_location)
        # print(result_post.text)
        [print(k) for k in result_post.text.split(',')]

        assert 200 == result_post.status_code
        print("Успешно!!! Создана новая локация")
        check_post = result_post.json()
        check_info_post = check_post.get("status")
        print(f'Статус код ответа : {check_info_post}')
        assert check_info_post == "OK"
        print("Статус код ответа верен")
        place_id = check_post.get("place_id")
        print(f'place_id ответа : {place_id}')
        return place_id


    def check_new_location(self, place_id):
        """Проверка создания новой локации"""

        get_resource = "/maps/api/place/get/json"
        get_url = self.base_url + get_resource + self.key + "&place_id=" + place_id
        print(get_url)
        result_get = requests.get(get_url)
        print(result_get.text)
        # [print(k) for k in result_get.text.split(',')]

        print(f'Статус код ответа : {result_get.status_code}')
        assert 200 == result_get.status_code
        print("Успешно!!! Проверка создания новой локации")


    def write_place_id_to_file(self):
        """Создаем файл и записываем в него 5 шт place_id"""
        with open("list_place_id.txt", "w", encoding='utf-8') as file:
            [file.write(self.create_new_location() + "\n") for _ in range(5)]


    def read_place_id_from_file(self):
        """Чтение place_id из файла"""
        with open("list_place_id.txt", "r", encoding='utf-8') as file:
            print([line for line in file.read().split("\n")])


new_place = Test_new_location()
new_place.write_place_id_to_file()
new_place.read_place_id_from_file()
