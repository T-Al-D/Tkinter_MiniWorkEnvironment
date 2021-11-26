from Tkinter_MiniWorkEnvironment.src.GUI import GUI


class Calculator:

    def __init__(self):
        gui = GUI.get_gui()
        self.label = GUI.add_label(gui, "Current int:", 2, 1, 3, 5, 5)
