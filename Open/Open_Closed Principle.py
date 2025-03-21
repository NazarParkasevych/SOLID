#  Неправильний код (порушує OCP)
class Discount:  # Клас для розрахунку знижки
    def __init__(self, customer_type):  # Конструктор отримує тип клієнта
        self.customer_type = customer_type  # Збереження типу клієнта

    def get_discount(self, price):  # Метод розрахунку знижки
        if self.customer_type == "regular":  # Якщо звичайний клієнт
            return price * 0.9  # Знижка 10%
        elif self.customer_type == "vip":  # Якщо VIP-клієнт
            return price * 0.8  # Знижка 20%


#  Правильний код (відповідає OCP)
from abc import ABC, abstractmethod  # Імпортуємо модулі для абстрактних класів

class Discount(ABC):  # Абстрактний клас для знижок
    @abstractmethod
    def get_discount(self, price):  # Абстрактний метод для розрахунку знижки
        pass

class RegularDiscount(Discount):  # Клас для знижки звичайних клієнтів
    def get_discount(self, price):  # Реалізація знижки
        return price * 0.9  # Знижка 10%

class VIPDiscount(Discount):  # Клас для знижки VIP-клієнтів
    def get_discount(self, price):  # Реалізація знижки
        return price * 0.8  # Знижка 20%
