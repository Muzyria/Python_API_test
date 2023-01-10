import requests


class Test_new_joke:
    """Создание новой шутки"""

    def __init__(self):
        self.list_category = requests.get("https://api.chucknorris.io/jokes/categories").json()

    def ntest_run_categories_joke(self):
        """Создание случайной шутки на определенную тему"""
        for num, category in enumerate(self.list_category, 1):
            print(f'Шутка № {num} в категории {category}')
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
            print()


run_category_joke = Test_new_joke()
run_category_joke.ntest_run_categories_joke()
