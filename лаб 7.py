class Employee:
    def __init__(self, *args):
        self.name = args[0]
        self.id = args[1]

    def get_info(self):
        return f'Имя: {self.name}, Айди: {self.id}'

class Manager(Employee):
    def __init__(self, *args):
        super().__init__(*args)
        self.department = args[2]
    def clear_department(self):
        return f'все сотрудники департамента {self.department} были уволены'


class Technician(Employee):
    def __init__(self, *args):
        super().__init__(*args)
        self.specialisation = args[2]

class TechManager(Manager, Technician):
    def __init__(self, *args):
        Manager.__init__(self, *args)
        Technician.__init__(self, *args)

        self.emp_list = []

    def add_employee(self, employee):
        self.emp_list.append(employee.name)
        return f'Сотрудник {employee.name} добавлен в команду.'

    def get_team_info(self):
        j_list = ', '.join(self.emp_list)
        return j_list

w1 = Employee('Иван', 12345)
w2 = Manager('Сергей', 123455, 'IT')
w3 = Technician('Дмитрий', 12321, 'software engineering')
w4 = TechManager('Дмитрий Иванов', 42422, 'ff', 'работа')

print(w1.get_info())
print(w2.clear_department())
print(w4.add_employee(w1))
print(w4.add_employee(w2))
print(w4.get_team_info())