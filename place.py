import requests


class Test_new_location:
    """Работа с новой локацией"""

    def ntest_create_new_location(self):
        """Создание новой локации"""

        base_url = "https://rahulshettyacademy.com"  # базовая url
        key = "?key=qaclick123"  # Параметр для всех запросов

        """Создание новой локации"""
        post_resource = "/maps/api/place/add/json"  # Ресурс метода пост

        post_url = base_url + post_resource + key
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
        [print(k) for k in result_post.text.split(',')]

        assert 200 == result_post.status_code
        print("Успешно!!! Создана новая локация")

        check_post = result_post.json()
        check_info_post = check_post.get("status")
        print(f'Статус код ответа {check_info_post}')
        assert check_info_post == "OK"
        print("Статус код ответа верен")


new_place = Test_new_location()
new_place.ntest_create_new_location()
