
def check_employee_id(employee):
    emp_id = input("Enter Employee ID: ")

    if emp_id != str(employee["id"]):
        print("Access denied! Invalid Employee ID.")
        return False

    return True


def display_info(employee):
    if not check_employee_id(employee):
        return

    print("\nEmployee Information:")
    print("Name:", employee["name"])
    print("Department:", employee["department"])
    print("Salary: $", employee["salary"])
    print("Days of Absence:", employee["absence_days"])


def calculate_bonus(employee):
    if not check_employee_id(employee):
        return

    bonus = employee["salary"] * 0.10

    print("\nBonus Calculation:")
    print("Bonus: $", bonus)


def calculate_discount(employee):
    if not check_employee_id(employee):
        return

    discount = employee["salary"] * 0.05

    print("\nDiscount Calculation:")
    print("Discount: $", discount)


def remind_holidays(employee):
    if not check_employee_id(employee):
        return

    print("\nReminder:")
    print("Remaining Legal Holidays:",
          employee["remaining_holidays"])
