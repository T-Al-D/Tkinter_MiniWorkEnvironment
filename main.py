from Tkinter_MiniWorkEnvironment.src.Calculator import Calculator
from Tkinter_MiniWorkEnvironment.src.GUI import GUI
from Tkinter_MiniWorkEnvironment.src.Notepad import Notepad
from Tkinter_MiniWorkEnvironment.src.ToDoList import ToDoList
from Tkinter_MiniWorkEnvironment.src.WebScraper import WebScraper

if __name__ == "__main__":

    gui = GUI.get_gui()

    # build the surface
    gui.add_label("ToDo", None, 2, 0, 1, 5, 5)
    gui.add_label("Calculator", None, 3, 0, 3, 5, 5)
    gui.add_label("Notepad", None, 4, 0, 6, 5, 5)
    gui.add_label("Database", None, 3, 0, 10, 5, 5)
    gui.display_date(2, 0, 14, 5, 5)
    gui.display_time(2, 0, 16, 5, 5)


    gui.add_label("Web Scraper", None, 2, 8, 1, 5, 0)

    ToDoList()
    Calculator()
    Notepad()
    WebScraper()

    # keep the window going
    gui.mainloop()
