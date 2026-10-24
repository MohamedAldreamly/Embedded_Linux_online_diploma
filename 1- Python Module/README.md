# Employee Management System (CLI + GUI)

Python standard library only. Tested syntax and CLI flow; GUI requires a desktop with Tkinter.

## Run
- `python run.py` to choose CLI or GUI
- `python main.py` for CLI
- `python gui.py` for GUI

Sample login: Employee ID `101`, password `1234`.

`operations.py` preserves the original CLI operation functions and adds shared pure helpers that the GUI calls. `authentication.py` shares authentication rules between CLI and GUI. Every operation asks for the logged-in employee's ID again.

Educational demo only: employee data and plaintext passwords are in memory and not suitable for production.
