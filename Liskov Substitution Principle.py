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
