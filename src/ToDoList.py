from Tkinter_MiniWorkEnvironment.src.GUI import GUI


class ToDoList:

    def __init__(self):
        self.scroll_list = GUI.add_scroll_list(GUI.get_gui(), 40, 1, 1, 1, "20", "10", "ew")
