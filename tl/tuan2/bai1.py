# ho = str(input('Input ho: '))
# dem = str(input('Input dem: '))
# ten = str(input('Input ten: '))
# class Name:
#     def __init__(self, tenho, tendem, ten):
#         self.tenho = tenho
#         self.tendem = tendem
#         self.ten = ten
#     def inten(self):
#         print(self.tenho, self.tendem, self.ten)
# lam = Name(ho,dem,ten)
# lam.inten()


class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class FullTimeEmployee(Employee):
    def __init__(self,name, age, basic_salary, salary_multiplier):
        super().__init__(name, age)
        self.basic_salary = basic_salary
        self.salary_multiplier = salary_multiplier

    def calculate_salary(self):
        calculate_salary = self.basic_salary * self.salary_multiplier
        print(calculate_salary)
    
class PartTimeEmployee(Employee):
    def __init__(self, name, age, hours_worked, hourly_rate):
        super().__init__(name, age)
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate
        
    def calculate_salary(self):
            calculate_salary = self.hourly_rate * self.hours_worked
            print(calculate_salary)
# class Nhanvien(FullTimeEmployee, PartTimeEmployee):
#      def __init__(self, name, age):
#           super().__init__(name, age)
#           self.name = name
#           self.age = age
class Department:
    def __init__(self, name):
        self.name = name
        self.employees = [] #Danh sach nhan vien
    def them(self):
        self.employees.append(self.name)
    def xoa(self):
        self.employees.remove(self.name)
    def lietke(self):
        print(self.employees)
lam = FullTimeEmployee('Lam',17,10000,2)
lam.calculate_salary()
HR = Department("HR")
HR.lietke()

# Department.lietke()
        