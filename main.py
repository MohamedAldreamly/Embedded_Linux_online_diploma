
import employee

def main():
    while True:
        print("\n===== Employee Management System =====")
        print("1. Add Employee")
        print("2. View All Employees")
        print("3. Search Employee")
        print("4. Update Employee")
        print("5. Delete Employee")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            employee.add_employee()

        elif choice == "2":
            employee.view_employees()

        elif choice == "3":
            employee.search_employees()

        elif choice == "4":
            employee.update_employee()

        elif choice == "5":
            employee.delete_employee()

        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid choice! Try again.")


if __name__ == "__main__":
    main() 