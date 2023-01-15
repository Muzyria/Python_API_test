import requests


class Swapi:
    """Работа с SW"""

    def __init__(self):
        self.base_url = 'https://swapi.dev/api'

    def method_get(self, resource, key):
        get_url = self.base_url + resource
        print(get_url)
        result_get = requests.get(get_url)
        return result_get.json()[key]

    def write_all_characters(self):
        """Создаем файл и записываем в него списрк персонажей"""
        with open("list_characters.txt", "w", encoding='utf-8') as file:
            all_people = set()
            list_characters = []
            all_films = [i.replace(self.base_url, "") for i in self.method_get('/people/4/', 'films')]
            print(all_films)
            for item in all_films:
                [all_people.add(i.replace(self.base_url, "")) for i in self.method_get(item, "characters")]
            for item in all_people:
                list_characters.append(self.method_get(item, 'name'))
            [file.write(line + "\n") for line in sorted(list_characters)]


dw_check = Swapi()
dw_check.write_all_characters()
