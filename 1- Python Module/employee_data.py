employees = [
    {
        "id": 101,
        "name": "John Doe",
        "department": "IT",
        "salary": 5000,
        "password": "1234",
        "absence_days": 2,
        "remaining_holidays": 10,
    }
]


def find_employee(emp_id):
    for employee in employees:
        if employee["id"] == emp_id:
            return employee
    return None
