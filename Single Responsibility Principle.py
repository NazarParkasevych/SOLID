#  Неправильний код (порушує SRP)
class Report:  # Клас для роботи зі звітом
    def __init__(self, data):  # Конструктор, отримує дані звіту
        self.data = data  # Збереження даних у змінну

    def generate_report(self):  # Метод для створення звіту
        return f"Report Data: {self.data}"  # Формує текст звіту

    def save_to_file(self, filename):  # Метод для збереження звіту у файл (порушення SRP)
        with open(filename, 'w') as file:  # Відкриває файл у режимі запису
            file.write(self.generate_report())  # Записує текст звіту у файл

#  Правильний код (відповідає SRP)
class Report:  # Клас, який відповідає лише за генерацію звіту
    def __init__(self, data):  # Конструктор, отримує дані звіту
        self.data = data  # Збереження даних у змінну

    def generate_report(self):  # Метод для створення звіту
        return f"Report Data: {self.data}"  # Формує текст звіту

class ReportSaver:  # Клас, який відповідає лише за збереження звіту
    @staticmethod  # Статичний метод, не потребує створення екземпляра класу
    def save_to_file(report: Report, filename):  # Метод для запису звіту у файл
        with open(filename, 'w') as file:  # Відкриває файл у режимі запису
            file.write(report.generate_report())  # Записує текст звіту у файл
