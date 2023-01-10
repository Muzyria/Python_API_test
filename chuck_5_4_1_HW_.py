import requests


class Test_new_joke:
    """Создание новой шутки"""

    def __init__(self):
        self.list_category = requests.get("https://api.chucknorris.io/jokes/categories").json()

    def ntest_create_new_random_categories_joke(self):
        """Создание случайной шутки на определенную тему"""
        for category in self.list_category:
            url = f"https://api.chucknorris.io/jokes/random?category={category}"
            print(url)
            result = requests.get(url)
            print("Статус код : " + str(result.status_code))
            assert 200 == result.status_code
            if result.status_code == 200:
                print(f"Успешно, Мы получили новую шутку в категории {category}")
            else:
                print("Провал. Запрос не верный")
            result.encoding = 'utf-8'
            print(result.text)
            check = result.json()
            check_info = check.get("categories")
            print(check_info)
            assert check_info == [category]
            print("Категория верна")
        # check_info_value = check.get("value")
        # print(check_info_value)
        # name = "Chuck"
        # if name in check_info_value:
        #     print("Chuck присутствует")
        # else:
        #     print("Сhuck отсутствует")


run_category_joke = Test_new_joke()
run_category_joke.ntest_create_new_random_categories_joke()