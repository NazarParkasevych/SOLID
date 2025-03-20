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