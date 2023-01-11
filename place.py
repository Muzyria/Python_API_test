import requests


class Test_new_location:
    """Работа с новой локацией"""

    def ntest_create_new_location(self):
        """Создание новой локации"""

        base_url = "https://rahulshettyacademy.com"  # базовая url
        key = "?key=qaclick123"  # Параметр для всех запросов
        post_resource = "/maps/api/place/add/json"  # Ресурс метода пост

        post_url = base_url + post_resource + key

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
