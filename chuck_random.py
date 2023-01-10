import requests


class Test_new_joke:
    """Создание новой шутки"""

    def __init__(self):
        pass

    def ntest_create_new_random_joke(self):
        """Создание случайной шутки"""
        url = "https://api.chucknorris.io/jokes/random"
        print(url)
        result = requests.get(url)
        print("Статус код : " + str(result.status_code))
        assert 200 == result.status_code
        if result.status_code == 200:
            print("Успешно, Мы получили новую шутку")
        else:
            print("Повал. Запрос не верный")
        result.encoding = 'utf-8'
        print(result.text)
        check = result.json()
        check_info = check.get("categories")
        print(check_info)
        assert check_info == []
        print("Категория верна")


random_joke = Test_new_joke()
random_joke.ntest_create_new_random_joke()
