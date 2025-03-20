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