from employee_data import find_employee


def authenticate(emp_id, password):
    try:
        emp_id = int(str(emp_id).strip())
    except ValueError:
        return None

    employee = find_employee(emp_id)
    if employee is not None and employee["password"] == password:
        return employee
    return None


def login():
    for attempt in range(3):
        emp_id = input("Enter Employee ID: ")
        password = input("Enter Password: ")
        employee = authenticate(emp_id, password)
        if employee is not None:
            print("Login successful!")
            return employee
        print("Invalid ID or password. Attempts remaining:", 2 - attempt)
    print("Access denied! Too many failed attempts.")
    return None
