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