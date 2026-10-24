import tkinter as tk
from tkinter import messagebox

from authentication import authenticate
from operations import (
    get_employee_info,
    get_bonus,
    get_discount,
    get_remaining_holidays,
    is_employee_id_valid,
)


def start_gui():
    window = tk.Tk()
    window.title("Employee Management System")
    window.geometry("520x520")
    window.resizable(False, False)

    attempts = 0
    logged_in_employee = None

    def clear_window():
        for widget in window.winfo_children():
            widget.destroy()

    def add_title(text):
        tk.Label(window, text=text, font=("Arial", 17, "bold")).pack(pady=24)

    def show_login():
        clear_window()
        add_title("Employee Management System")
        tk.Label(window, text="Employee ID").pack()
        id_entry = tk.Entry(window, width=30)
        id_entry.pack(pady=7)
        tk.Label(window, text="Password").pack()
        password_entry = tk.Entry(window, show="*", width=30)
        password_entry.pack(pady=7)

        def submit_login():
            nonlocal attempts, logged_in_employee
            employee = authenticate(id_entry.get(), password_entry.get())
            if employee is not None:
                logged_in_employee = employee
                messagebox.showinfo("Success", "Login successful!")
                show_menu()
                return
            attempts += 1
            if attempts >= 3:
                messagebox.showerror("Access denied", "Too many failed attempts.")
                window.destroy()
            else:
                messagebox.showerror("Login failed", f"Invalid ID or password. {3 - attempts} attempts left.")

        tk.Button(window, text="Login", command=submit_login, width=22).pack(pady=20)

    def show_menu():
        clear_window()
        add_title("Employee Main Menu")
        options = [
            ("Display Employee Information", "info"),
            ("Calculate Bonus", "bonus"),
            ("Calculate Discount", "discount"),
            ("Remind Legal Holidays", "holidays"),
        ]
        for title, kind in options:
            tk.Button(
                window,
                text=title,
                width=32,
                height=2,
                command=lambda t=title, k=kind: show_operation(t, k),
            ).pack(pady=7)
        tk.Button(window, text="Exit", width=32, command=window.destroy).pack(pady=12)

    def show_operation(title, kind):
        clear_window()
        add_title(title)
        tk.Label(window, text="Enter Employee ID:").pack()
        id_entry = tk.Entry(window, width=30)
        id_entry.pack(pady=10)
        result_label = tk.Label(window, text="", font=("Arial", 12), justify="left")
        result_label.pack(pady=20)

        def submit():
            if not is_employee_id_valid(logged_in_employee, id_entry.get()):
                messagebox.showerror("Access denied", "Invalid Employee ID!")
                return

            if kind == "info":
                info = get_employee_info(logged_in_employee)
                result = (
                    f"Name: {info['name']}\n"
                    f"Department: {info['department']}\n"
                    f"Salary: ${info['salary']}\n"
                    f"Days of Absence: {info['absence_days']}"
                )
            elif kind == "bonus":
                result = f"Bonus: ${get_bonus(logged_in_employee):.2f}"
            elif kind == "discount":
                result = f"Discount: ${get_discount(logged_in_employee):.2f}"
            else:
                result = f"Remaining Legal Holidays: {get_remaining_holidays(logged_in_employee)}"
            result_label.config(text=result)

        tk.Button(window, text="Submit", command=submit, width=20).pack(pady=8)
        tk.Button(window, text="Back to Menu", command=show_menu, width=20).pack(pady=8)

    show_login()
    window.mainloop()


if __name__ == "__main__":
    start_gui()
