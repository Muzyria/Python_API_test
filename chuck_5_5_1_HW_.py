import requests


class Test_new_joke:
    """Создание новой шутки"""

    def __init__(self):
        self.list_category = requests.get("https://api.chucknorris.io/jokes/categories").json()  # список категорий

    def check_category(self, category):
        """Проверка что категория есть в списке категорий"""
        if category in self.list_category:
            return True
        return False

    def ntest_run_categories_joke(self, category):
        """Создание случайной шутки на определенную тему"""
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


run_category_joke = Test_new_joke()
[print(f'{num} : {item}', sep="\n") for num, item in enumerate(run_category_joke.list_category, 1)]

while True:
    select_category = input('Введите название категории шутки ')
    if run_category_joke.check_category(select_category):
        run_category_joke.ntest_run_categories_joke(select_category)
        break
    print('Ткакой категории нет в списке !')
    continue
