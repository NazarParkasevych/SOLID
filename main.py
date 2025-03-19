# Принципи SOLID
# Single Responsibility Principle
# Неправильний код:
class Report:
    def __init__(self, data):
        self.data = data
    def generate_report(self):  # Генерація звіту
        return f"Report Data: {self.data}"
    def save_to_file(self, filename):  # Збереження звіту у файл (порушення SRP)
        with open(filename, 'w') as file:
            file.write(self.generate_report())

# Правильний код:
class Report:
    def __init__(self, data):
        self.data = data
    def generate_report(self):  # Тепер клас відповідає тільки за генерацію звіту
        return f"Report Data: {self.data}"
class ReportSaver:
    @staticmethod
    def save_to_file(report: Report, filename):  # Відповідає лише за збереження звіту
        with open(filename, 'w') as file:
            file.write(report.generate_report())

# Open/Closed Principle
# Неправильний код:
class Discount:
    def __init__(self, customer_type):
        self.customer_type = customer_type
    def get_discount(self, price):  # Логіка змінюється при додаванні нового типу клієнтів
        if self.customer_type == "regular":
            return price * 0.9
        elif self.customer_type == "vip":
            return price * 0.8

# Правильний код:
from abc import ABC, abstractmethod
class Discount(ABC):  # Абстрактний клас для знижок
 @abstractmethod
 def get_discount(self, price):
    pass
class RegularDiscount(Discount):
    def get_discount(self, price):  # Реалізація знижки для звичайних клієнтів
        return price * 0.9
class VIPDiscount(Discount):
    def get_discount(self, price):  # Реалізація знижки для VIP-клієнтів
        return price * 0.8


# Liskov Substitution Principle
# Неправильний код:
class Bird:
    def fly(self):
        return "I can fly"
class Penguin(Bird):
    def fly(self):
        raise Exception("Penguins can't fly")  # Пінгвіни не можуть літати, що порушує LSP

# Правильний код:
class Bird:
    pass
class FlyingBird(Bird):
    def fly(self):
        return "I can fly" # Лише птахи, які літають, мають метод fly
class Penguin(Bird):
    def swim(self):
        return "I can swim"  # Пінгвіни мають метод swim, а не fly

# Interface Segregation Principle
# Неправильний код:
class Worker:
    def work(self):
        pass
def eat(self):
        pass
# Правильний код:
class Workable:
    def work(self):
        pass  # Інтерфейс для всіх працівників
class Eatable:
    def eat(self):
        pass  # Окремий інтерфейс для тих, хто може їсти

# Dependency Inversion Principle
# Неправильний код:
class Backend:
    def request(self):
        return "Data"
class Frontend:
    def __init__(self):
        self.backend = Backend()

# Правильний код:
class DataSource:
    def request(self):
        pass  # Абстракція для отримання даних
class Backend(DataSource):
    def request(self):
        return "Data"  # Реалізація джерела даних
class Frontend:
    def __init__(self, backend: DataSource):
        self.backend = backend  # Тепер залежність йде від абстракції