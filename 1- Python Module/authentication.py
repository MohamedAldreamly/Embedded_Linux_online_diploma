from employee_data import find_employee

def login():
    attempts = 0

    while attempts < 3:
        emp_id = int(input("Enter your Employee ID: "))
        password = input("Enter your Password: ")

        employee = find_employee(emp_id)

        if employee is not None and employee["password"] == password:
            print("Login successful!")
            return employee

        else:
            attempts += 1
            print("Invalid ID or Password!")
            print("Remaining attempts:", 3 - attempts)

    print("Access denied!")
    return None
