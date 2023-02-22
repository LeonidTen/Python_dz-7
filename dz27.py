# Создать информационную систему позволяющую работать с сотрудниками некой компании \ студентами вуза \ учениками школы

class Employee:
    def __init__(self, name, age, departament, position, salary):
        self.name = name
        self.age = age
        self.departament = departament
        self.position = position
        self.salary

class Company:
    def __init__(self):
        self.empoyees =[]
    
    def add_employee(self, employee):
        self.add_employees.append(employee)

    def remove_employee(self, employee):
        self.employees.remove(employee)

    def find_employee_by_name(self, name):
        for employee in self.emloyees:
            if employee.name == name:
                return employee
        return None

    def find_employee_by_departament(self, departament):
        departament_employees = []
        for employee in self.emplotees:
            if employee.departament == departament:
                departament_employees.append(employee)
        return departament_employees

    def total_salary(self):
        total_salary = 0
        for employee in self.employee:
            total_salary += employee.salary
        return total_salary

