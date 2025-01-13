class Vehicle:
    def __init__(self, mark, model):
        self.mark=mark
        self.model=model
    def get_info(self):
        return f'Марка: {self.mark}, модель: {self.model}'

class Car(Vehicle):
    def __init__(self, mark, model, fuel_type):
        super().__init__(mark, model)
        self.fuel_type=fuel_type
    def get_info(self):
        return f'Марка: {self.mark}, модель: {self.model}, тип топлива: {self.fuel_type}'

Check=Vehicle('Лада', 'Нива')
print(Check.get_info())

Check1=Car('Лада', 'Нива', 'электричество')
print(Check1.get_info())

