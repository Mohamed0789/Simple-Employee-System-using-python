def input_validate(msg, start=0, end=None):
    while True:
        inp = input(msg)
        if not inp.isdecimal():
            print("Invalid input. Try again!")
        elif start is not None and end is not None:
            if int(inp) in range(start, end + 1):
                return int(inp)
            else:
                print("Invalid Range. Try again!")
        else:
            return int(inp)


class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __str__(self):
        return f'Employee: {self.name} has {self.age} age and salary {self.salary}'

    def __repr__(self):
        return F'Employee(name="{self.name}", age={self.age}, salary = {self.salary})'


class EmployeeManager:
    def __init__(self):
        self.employees = []

    def add_employee(self):
        print("\nEnter Employee data: ")
        name = input("Enter the name: ")
        age = input_validate("enter the age: ")
        salary = input_validate("Enter the salary: ")

        self.employees.append(Employee(name, age, salary))

    def list_all_employee(self):
        if len(self.employees) == 0:
            print("\nNo employees at the moment!")
            return

        print('\n**Employees list**')
        for emp in self.employees:
            print(emp)

    def delete_employee_by_age(self, age_from, age_to):
        # delete from the back
        for idx in range(len(self.employees) - 1, -1, -1):
            emp = self.employees[idx]
            if age_from <= emp.age <= age_to:
                print("Deleting ", emp.name)
                self.employees.pop(idx)

    def find_emp_by_name(self, name):
        for emp in self.employees:
            if emp.name == name:
                return emp
        return None

    def update_salary_by_name(self, emp_name, updated_salary):
        emp = self.find_emp_by_name(emp_name)
        if emp is None:
            print('Error: No employee with such a name')
        else:
            emp.salary = updated_salary


class FrontEnd:
    def __init__(self):
        self.employee_manager = EmployeeManager()

    def print_menu(self):
        print("\nProgram Options:")
        message = [
            '1) Add new employee',
            '2) List all employees',
            '3) Delete by age',
            '4) Update Salary by name',
            '5) End the program'
        ]
        print('\n'.join(message))
        msg = f'Enter your choice (from 1 to {len(message)}): '
        return input_validate(msg, 1, len(message))

    def run(self):
        while True:
            choice = self.print_menu()
            if choice == 1:
                self.employee_manager.add_employee()
            elif choice == 2:
                self.employee_manager.list_all_employee()
            elif choice == 3:
                age_from = input_validate("Enter age from: ")
                age_to = input_validate("Enter age to: ")
                self.employee_manager.delete_employee_by_age(age_from, age_to)
            elif choice == 4:
                emp_name = input("Enter name")
                updated_salary = input_validate("Enter new salary")
                self.employee_manager.update_salary_by_name(emp_name, updated_salary)
            else:
                break


if __name__ == '__main__':
    emp_app = FrontEnd()
    emp_app.run()
