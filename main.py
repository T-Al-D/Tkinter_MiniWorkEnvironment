from Tkinter_MiniWorkEnvironment.src.Calculator import Calculator
from Tkinter_MiniWorkEnvironment.src.GUI import GUI
from Tkinter_MiniWorkEnvironment.src.ToDoList import ToDoList


if __name__ == "__main__":

    gui = GUI.get_gui()

    # build the surface
    gui.add_label("ToDo", None, 2, 0, 1, 5, 5, "ew", None)
    gui.add_label("Calculator", None, 3, 0, 3, 5, 5, "ew", None)

    to_do = ToDoList()
    calc = Calculator()

    # keep the window going
    gui.mainloop()
