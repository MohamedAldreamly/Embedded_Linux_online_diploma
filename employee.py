
from tkinter import Menu


employees = []

def add_employee():
    emp_id = int(input("Enter Employee ID: "))

    for employee in employees:
        if employee[0] == emp_id:
            print("Error: Employee ID already exists!")
            return

    name = input("Enter Employee Name: ")
    age = int(input("Enter Employee Age: "))
    department = input("Enter Department: ")
    salary = float(input("Enter Salary: "))

    new_employee = (
        emp_id,
        name,
        age,
        department,
        salary
    )

    employees.append(new_employee)

    print("Employee added successfully!")


def view_employees():
    if len(employees) == 0:
        print("No employees found!")
        return

    print("\n===== Employees List =====")

    for employee in employees:
        print("------------------------")
        print("ID:", employee[0])
        print("Name:", employee[1])
        print("Age:", employee[2])
        print("Department:", employee[3])
        print("Salary:", employee[4])


def search_employees():
    emp_id = int(input("Enter Employee ID: "))

    for employee in employees:
        if employee[0] == emp_id:
            if employee[0] == emp_id:
                print("\n===== Employee Found =====")
                print("ID:", employee[0])
                print("Name:", employee[1])
                print("Age:", employee[2])
                print("Department:", employee[3])
                print("Salary:", employee[4])
                return

        else:
            print("Error: Employee ID already exists!")
            return

def update_employee():
    emp_id = int(input("Enter Employee ID: "))

    for i in range(len(employees)):
        if employees[i][0] == emp_id:

            print("Employee Found!")

            name = input("Enter New Name: ")
            age = int(input("Enter New Age: "))
            department = input("Enter New Department: ")
            salary = float(input("Enter New Salary: "))

            employees[i] = (
                emp_id,
                name,
                age,
                department,
                salary
            )

            print("Employee updated successfully!")
            return

    print("Employee not found!")


def delete_employee():
    emp_id = int(input("Enter Employee ID: "))

    for employee in employees:
        if employee[0] == emp_id:
            employees.remove(employee)
            print("Employee deleted successfully!")
            return

    print("Employee not found!")

    