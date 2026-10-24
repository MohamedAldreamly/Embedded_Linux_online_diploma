# Shared logic used by both CLI and GUI.
def get_employee_info(employee):
    return {
        "name": employee["name"],
        "department": employee["department"],
        "salary": employee["salary"],
        "absence_days": employee["absence_days"],
    }


def get_bonus(employee):
    return employee["salary"] * 0.10


def get_discount(employee):
    return employee["salary"] * 0.05


def get_remaining_holidays(employee):
    return employee["remaining_holidays"]


def is_employee_id_valid(employee, emp_id):
    return str(employee["id"]) == str(emp_id).strip()


# Original CLI functions are preserved.
def check_employee_id(employee):
    emp_id = input("Enter Employee ID: ")

    if not is_employee_id_valid(employee, emp_id):
        print("Access denied! Invalid Employee ID.")
        return False

    return True


def display_info(employee):
    if not check_employee_id(employee):
        return

    info = get_employee_info(employee)
    print("\nEmployee Information:")
    print("Name:", info["name"])
    print("Department:", info["department"])
    print("Salary: $", info["salary"])
    print("Days of Absence:", info["absence_days"])


def calculate_bonus(employee):
    if not check_employee_id(employee):
        return

    bonus = get_bonus(employee)
    print("\nBonus Calculation:")
    print("Bonus: $", bonus)


def calculate_discount(employee):
    if not check_employee_id(employee):
        return

    discount = get_discount(employee)
    print("\nDiscount Calculation:")
    print("Discount: $", discount)


def remind_holidays(employee):
    if not check_employee_id(employee):
        return

    print("\nReminder:")
    print("Remaining Legal Holidays:", get_remaining_holidays(employee))
