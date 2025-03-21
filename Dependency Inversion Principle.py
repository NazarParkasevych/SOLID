#  Неправильний код (порушує DIP)
class Backend:  # Клас для отримання даних
    def request(self):
        return "Data"  # Повертає дані

class Frontend:  # Клас інтерфейсу (залежить від Backend)
    def __init__(self):
        self.backend = Backend()  # Прямо створює об'єкт Backend (жорстка залежність)

#  Правильний код (відповідає DIP)
class DataSource:  # Абстрактний клас (джерело даних)
    def request(self):
        pass  # Оголошуємо метод без реалізації

class Backend(DataSource):  # Реалізація джерела даних
    def request(self):
        return "Data"  # Повертає дані

class Frontend:  # Клас інтерфейсу
    def __init__(self, backend: DataSource):  # Залежність передається через конструктор
        self.backend = backend  # Використовує абстракцію, а не конкретний клас