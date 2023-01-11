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

        """Проверка создания новой локации"""

        get_resource = "/maps/api/place/get/json"
        get_url = base_url + get_resource + key + "&place_id=" + place_id
        print(get_url)
        result_get = requests.get(get_url)
        print(result_get.text)
        # [print(k) for k in result_get.text.split(',')]

        print(f'Статус код ответа : {result_get.status_code}')
        assert 200 == result_get.status_code
        print("Успешно!!! Проверка создания новой локации")

        """Изменение новой локации"""
        put_resource = "/maps/api/place/update/json"
        put_url = base_url + put_resource + key
        print(put_url)
        json_for_update_new_location = {
                                        "place_id": place_id,
                                        "address": "100 Lenina street, RU",
                                        "key": "qaclick123"
                                        }
        result_put = requests.put(put_url, json=json_for_update_new_location)
        print(result_put.text)
        print(f'Статус код ответа : {result_put.status_code}')
        assert 200 == result_put.status_code
        print("Успешно!!! Изменение новой локации прошло успешно")
        check_put = result_put.json()
        check_put_info = check_put.get("msg")
        print(f'Сообщение : {check_put_info}')
        assert check_put_info == "Address successfully updated"
        print("Сообщение верно")

        """Проверка изменения новой локации"""
        result_get = requests.get(get_url)
        print(result_get.text)
        # [print(k) for k in result_get.text.split(',')]
        print(f'Статус код ответа : {result_get.status_code}')
        assert 200 == result_get.status_code
        print("Успешно!!! Проверка изменения новой локации")

        check_address = result_get.json()
        check_address_info = check_address.get("address")
        print(f'Сообщение : {check_address_info}')
        # print(json_for_update_new_location["address"])
        assert check_address_info == json_for_update_new_location["address"]
        print("Адрес верный")

        """Удаление новой локации"""
        delete_resource = "/maps/api/place/delete/json"
        delete_url = base_url + delete_resource + key
        print(delete_url)
        json_for_delete_new_location = {"place_id": place_id}
        result_delete = requests.put(delete_url, json=json_for_delete_new_location)
        print(result_delete.text)
        print(f'Статус код ответа : {result_put.status_code}')
        assert 200 == result_delete.status_code
        print("Успешно!!! Удаление новой локации прошло успешно")
        check_delete = result_delete.json()
        check_delete_info = check_delete.get("status")
        print(f'Сообщение : {check_delete_info}')
        assert check_delete_info == "OK"
        print("Сообщение верно")


new_place = Test_new_location()
new_place.ntest_create_new_location()
