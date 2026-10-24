employees = [
    {
        "id": 101,
        "name": "John Doe",
        "department": "IT",
        "salary": 5000,
        "password": "1234",
        "absence_days": 2,
        "remaining_holidays": 10
    }
]

def find_employee(emp_id):
    for employee in employees:
        if employee["id"] == emp_id:
            return employee

    return None

def add_employee():
    emp_id = int(input("Enter Employee ID: "))

    if find_employee(emp_id) is not None:
        print("Employee ID already exists!")
        return

    name = input("Enter Employee Name: ")
    department = input("Enter Department: ")
    salary = float(input("Enter Salary: "))
    password = input("Enter Password: ")
    absence_days = int(input("Enter Days of Absence: "))
    holidays = int(input("Enter Remaining Holidays: "))

    new_employee = {
        "id": emp_id,
        "name": name,
        "department": department,
        "salary": salary,
        "password": password,
        "absence_days": absence_days,
        "remaining_holidays": holidays
    }

    employees.append(new_employee)
    print("Employee added successfully!")



def update_employee():
    emp_id = int(input("Enter Employee ID: "))

    employee = find_employee(emp_id)

    if employee is None:
        print("Employee not found!")
        return

    employee["name"] = input("Enter New Name: ")
    employee["department"] = input("Enter New Department: ")
    employee["salary"] = float(input("Enter New Salary: "))
    employee["password"] = input("Enter New Password: ")
    employee["absence_days"] = int(input("Enter New Days of Absence: "))
    employee["remaining_holidays"] = int(input("Enter New Remaining Holidays: "))

    print("Employee updated successfully!")



def delete_employee():
    emp_id = int(input("Enter Employee ID: "))

    employee = find_employee(emp_id)

    if employee is None:
        print("Employee not found!")
        return

    employees.remove(employee)
    print("Employee deleted successfully!")
