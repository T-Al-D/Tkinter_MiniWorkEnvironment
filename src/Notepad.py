from tkinter import END, filedialog
from Tkinter_MiniWorkEnvironment.src.GUI import GUI


class Notepad:

    def __init__(self):
        gui = GUI.get_gui()
        self.textbox = GUI.add_text_box(gui, 30, 15, 2, 3, 1, 6, 5, 5)
        self.save_button = GUI.add_button(gui, "OPEN", self.open_text, "white", "#3905a8", 3, 6, 5)
        self.clear_button = GUI.add_button(gui, "CLEAR", self.clear_text, "white", "purple", 3, 7, 2)
        self.open_button = GUI.add_button(gui, "SAVE", self.save_text, "white", "#88a805", 3, 8, 5)

    def clear_text(self):
        self.textbox.delete(1.0, END)

    def save_text(self):
        text_file = filedialog.asksaveasfilename(title="Select place to save file.", filetypes=[("Text Files", "*.txt")])
        if text_file != "":
            text_file = open(text_file, "w")
            contents = self.textbox.get(1.0, END)
            text_file.write(contents)
            text_file.close()

    def open_text(self):
        self.clear_text()
        text_file = filedialog.askopenfilename(title="Select file to open.", filetypes=[("Text Files", "*.txt")])
        if text_file != "":
            text_file = open(text_file, "r+")
            contents = text_file.read()
            self.textbox.insert(END, contents)
            text_file.close()
