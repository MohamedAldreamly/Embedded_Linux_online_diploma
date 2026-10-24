def main():
    print("Employee Management System")
    print("1. CLI")
    print("2. GUI")
    choice = input("Choose interface (1-2): ").strip()
    if choice == "1":
        from main import main as cli_main
        cli_main()
    elif choice == "2":
        from gui import start_gui
        start_gui()
    else:
        print("Invalid choice!")


if __name__ == "__main__":
    main()
