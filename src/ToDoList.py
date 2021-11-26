from tkinter import END
from Tkinter_MiniWorkEnvironment.src.GUI import GUI


class ToDoList:

    def __init__(self):
        gui = GUI.get_gui()
        self.scroll_list = GUI.add_scroll_list(gui, 40, 2, 1, 1, 1, 10, 5, "ew")
        self.entry = GUI.add_entry(gui, 35, 5, "dotbox", "blue", "white", 2, 3, 1, 5, 2)
        self.add_button = GUI.add_button(gui, "ADD", self.add_item, "white", "green", 4, 1, 5, 0, "w")
        self.delete_button = GUI.add_button(gui, "DELETE", self.delete_item, "white", "red", 4, 2, 5, 0, "ew")

    def add_item(self):
        input_text = self.entry.get()
        self.scroll_list.insert(END, input_text)
        self.entry.delete(0, END)

    def delete_item(self):
        selection = self.scroll_list.curselection()
        self.scroll_list.delete(selection)
