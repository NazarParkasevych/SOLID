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