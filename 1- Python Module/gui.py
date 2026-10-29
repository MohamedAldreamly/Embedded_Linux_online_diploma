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

# Visual settings: changing these does not change the CLI or calculations.
BG = "#F3F6FB"
CARD = "#FFFFFF"
NAVY = "#172B4D"
BLUE = "#2563EB"
BLUE_HOVER = "#1D4ED8"
TEXT = "#24344D"
MUTED = "#64748B"
BORDER = "#DCE4EF"


def start_gui():
    window = tk.Tk()
    window.title("Employee Management System")
    window.geometry("570x610")
    window.minsize(490, 550)
    window.configure(bg=BG)

    attempts = 0
    logged_in_employee = None

    def clear_window():
        for widget in window.winfo_children():
            widget.destroy()

    def label(parent, text, size=11, bold=False, color=TEXT, bg=CARD):
        return tk.Label(
            parent, text=text, bg=bg, fg=color,
            font=("Segoe UI", size, "bold" if bold else "normal"),
        )

    def button(parent, text, command, primary=True):
        background = BLUE if primary else CARD
        foreground = "white" if primary else NAVY
        widget = tk.Button(
            parent, text=text, command=command,
            bg=background, fg=foreground,
            activebackground=BLUE_HOVER if primary else BG,
            activeforeground="white" if primary else NAVY,
            font=("Segoe UI", 11, "bold"),
            relief="flat", bd=0, cursor="hand2",
            padx=16, pady=12, highlightthickness=0,
        )
        widget.bind("<Enter>", lambda event: widget.config(
            bg=BLUE_HOVER if primary else BG))
        widget.bind("<Leave>", lambda event: widget.config(bg=background))
        return widget

    def entry(parent, show=None):
        widget = tk.Entry(
            parent, font=("Segoe UI", 12),
            bg="#FAFCFF", fg=TEXT, insertbackground=TEXT,
            relief="solid", bd=1, highlightthickness=1,
            highlightbackground=BORDER, highlightcolor=BLUE,
            show=show,
        )
        return widget

    def page(title, subtitle):
        clear_window()
        header = tk.Frame(window, bg=NAVY, height=150)
        header.pack(fill="x")
        header.pack_propagate(False)
        label(header, "EMPLOYEE MANAGEMENT", 10, True, "#BFDBFE", NAVY).pack(
            anchor="w", padx=36, pady=(23, 4))
        label(header, title, 22, True, "white", NAVY).pack(
            anchor="w", padx=36)
        label(header, subtitle, 10, False, "#CBD5E1", NAVY).pack(
            anchor="w", padx=36, pady=(5, 0))

        outer = tk.Frame(window, bg=BG)
        outer.pack(fill="both", expand=True, padx=26, pady=24)
        card = tk.Frame(outer, bg=CARD, highlightbackground=BORDER,
                        highlightthickness=1)
        card.pack(fill="both", expand=True)
        inner = tk.Frame(card, bg=CARD)
        inner.pack(fill="both", expand=True, padx=28, pady=24)
        return inner

    def show_login():
        content = page("Welcome back", "Sign in to access your employee account")
        label(content, "Employee ID", 11, True).pack(anchor="w", pady=(10, 6))
        id_entry = entry(content)
        id_entry.pack(fill="x", ipady=9)

        label(content, "Password", 11, True).pack(anchor="w", pady=(20, 6))
        password_entry = entry(content, show="*")
        password_entry.pack(fill="x", ipady=9)

        status = label(content, "You have 3 login attempts.", 10, color=MUTED)
        status.pack(anchor="w", pady=(14, 24))

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
                remaining = 3 - attempts
                status.config(text=f"{remaining} login attempt(s) remaining.")
                messagebox.showerror(
                    "Login failed",
                    f"Invalid ID or password. {remaining} attempts left.",
                )
                password_entry.delete(0, tk.END)
                password_entry.focus_set()

        button(content, "Log in", submit_login).pack(fill="x")
        password_entry.bind("<Return>", lambda event: submit_login())
        id_entry.bind("<Return>", lambda event: password_entry.focus_set())
        id_entry.focus_set()

    def show_menu():
        content = page("Main menu", "Choose an employee service")
        label(content, f"Signed in as {logged_in_employee['name']}",
              11, True).pack(anchor="w", pady=(2, 18))
        options = [
            ("Display Employee Information", "info"),
            ("Calculate Bonus", "bonus"),
            ("Calculate Discount", "discount"),
            ("Remind Legal Holidays", "holidays"),
        ]
        for title, kind in options:
            button(content, title, lambda t=title, k=kind:
                   show_operation(t, k)).pack(fill="x", pady=6)
        button(content, "Exit", window.destroy, primary=False).pack(
            fill="x", pady=(18, 0))

    def show_operation(title, kind):
        content = page(title, "Verify your Employee ID to continue")
        label(content, "Employee ID", 11, True).pack(
            anchor="w", pady=(8, 6))
        id_entry = entry(content)
        id_entry.pack(fill="x", ipady=9)

        result_label = label(content, "", 12, color=NAVY)
        result_label.config(justify="left", anchor="w", wraplength=390)
        result_label.pack(fill="x", pady=(24, 14))

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
                result = (
                    "Remaining Legal Holidays: "
                    f"{get_remaining_holidays(logged_in_employee)}"
                )
            result_label.config(text=result)

        button(content, "Submit", submit).pack(fill="x", pady=7)
        button(content, "Back to Menu", show_menu, primary=False).pack(
            fill="x", pady=7)
        id_entry.bind("<Return>", lambda event: submit())
        id_entry.focus_set()

    show_login()
    window.mainloop()


if __name__ == "__main__":
    start_gui()
