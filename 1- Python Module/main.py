from authentication import login
from operations import display_info, calculate_bonus, calculate_discount, remind_holidays


def main():
    print("Welcome to Employee Management System")
    employee = login()
    if employee is None:
        return

    while True:
        print("\n1. Display Employee Information")
        print("2. Calculate Bonus")
        print("3. Calculate Discount")
        print("4. Remind Legal Holidays")
        print("5. Exit")
        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            display_info(employee)
        elif choice == "2":
            calculate_bonus(employee)
        elif choice == "3":
            calculate_discount(employee)
        elif choice == "4":
            remind_holidays(employee)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")
            continue
        input("\nPress Enter to return to the menu...")


if __name__ == "__main__":
    main()
