
from authentication import login
from operations import (
    display_info,
    calculate_bonus,
    calculate_discount,
    remind_holidays
)


def main():
    print("====================================")
    print("   EMPLOYEE MANAGEMENT SYSTEM")
    print("====================================")
    print("Welcome! Please login to continue.\n")

    employee = login()

    if employee is None:
        print("Program terminated.")
        return

    while True:
        print("\n====================================")
        print("        EMPLOYEE MAIN MENU")
        print("====================================")
        print("1. Display Employee Information")
        print("2. Calculate Bonus")
        print("3. Calculate Discount")
        print("4. Remind Legal Holidays")
        print("5. Exit")

        choice = input("\nEnter your choice (1-5): ")

        if choice == "1":
            display_info(employee)

        elif choice == "2":
            calculate_bonus(employee)

        elif choice == "3":
            calculate_discount(employee)

        elif choice == "4":
            remind_holidays(employee)

        elif choice == "5":
            print("\nThank you for using the system!")
            break

        else:
            print("Invalid choice! Please try again.")

        input("\nPress Enter to return to Main Menu...")


if __name__ == "__main__":
    main()
