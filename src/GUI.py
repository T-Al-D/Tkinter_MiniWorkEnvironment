import datetime
from tkinter.ttk import *
from tkinter import *
import tkinter as tk


# initialization with tk.Tk__init__(self) all Methods are being inherited
# this class contains all methods needed to create Objects on the GUI
class GUI(tk.Tk):
    entry: Entry  # type hint

    # the class itself becomes the ROOT
    def __init__(self):
        tk.Tk.__init__(self)  # instead super()...
        self.title("Mini Work Environment")  # window title
        self.geometry("1280x720")  # window size
        self.resizable(width=True, height=True)  # resizable window
        self.config(bg="#06505c")  # background_color
        icon_image = PhotoImage(file="res/icon.png")  # Icon from .png
        self.wm_iconphoto(True, icon_image)
        self.gui = None

    # this method is used to give other classes a gui to build on
    @staticmethod
    def get_gui():
        return gui

    def add_label(self, string, c_span, row, column, pad_x="0", pad_y="0", stick="ew", font=("Calibri", 12, "bold")):
        label = Label(self, text=str(string), font=font)
        label.grid(columnspan=c_span, row=row, column=column, padx=pad_x, pady=pad_y, sticky=stick)
        return label

    def add_entry(self, width, b_width, cur, fore_ground, back_ground, row, column, pad_x="0", pad_y="0", stick="ew"):
        self.entry = tk.Entry(self, width=width, borderwidth=b_width, fg=fore_ground, bg=back_ground, cursor=cur)
        self.entry.grid(row=row, column=column, padx=pad_x, pady=pad_y, sticky=stick)

    def add_button(self, string, com, fore_ground, back_ground, row, column, pad_x="0", pad_y="0", stick="ew"):
        button = tk.Button(self, text=string, command=com, fg=fore_ground, bg=back_ground)
        button.grid(row=row, column=column, padx=pad_x, pady=pad_y, sticky=stick)
        return button

    def add_radio_button(self, string, var, val, com, row, column, pad_x="0", pad_y="0", stick="ew"):
        radio_button = Radiobutton(self, text=string, variable=var, value=val, command=com)
        radio_button.grid(row=row, column=column, padx=pad_x, pady=pad_y, sticky=stick)
        return radio_button

    def add_drop_menu(self, var, row, column, pad_x="0", pad_y="0", stick="ew", *args):
        option_menu = OptionMenu(self, var, *args, command=self.add_drop_menu_label)
        option_menu.config(bg='light blue')
        option_menu.grid(row=row, column=column, padx=pad_x, pady=pad_y, sticky=stick)
        return option_menu

    def add_checkbox(self, string, var, row, column, pad_x="0", pad_y="0", stick="ew"):
        check_box = Checkbutton(self, text=string, variable=str(var), onvalue="YES", offvalue="NO")
        check_box.deselect()
        check_box.grid(row=row, column=column, padx=pad_x, pady=pad_y, sticky=stick)
        return check_box

    # scrollbar is created and a list is bound in it
    def add_scroll_list(self, width, column_span, row, column, pad_x="0", pad_y="0", stick="ew"):
        scrollbar = Scrollbar(self, orient=VERTICAL)
        scrollbar.grid(columnspan=column_span, row=row, column=column + 1, padx=0, pady=pad_y, sticky="ns")
        listbox = Listbox(self, width=width, selectmode=MULTIPLE, yscrollcommand=scrollbar.set)
        listbox.grid(row=row, column=column, columnspan=column_span, padx=pad_x, pady=pad_y, sticky=stick)
        scrollbar.config(command=listbox.yview)
        return listbox

    # display an image on label
    def display_img(self, file_name, r_span, c_span, row, column, pad_x="0", pad_y="0", stick="ew"):
        img = PhotoImage(file=file_name)
        panel = Label(self, image=img)
        panel.image = img
        panel.grid(rowspan=r_span, columnspan=c_span, row=row, column=column, padx=pad_x, pady=pad_y, sticky=stick)

    # display time on label and update it
    def display_time(self, span_of_column, row, column, pad_x="0", pad_y="0", stick="ew", font=("Calibri", 12, "bold")):
        now = datetime.datetime.now()
        now_str = now.strftime(str("%H:%M:%S"))
        time_label = self.add_label(now_str, span_of_column, row, column, pad_x, pad_y, font)
        time_label.after(1000, lambda: self.display_time(span_of_column, row, column, pad_x, pad_y, stick, font))

    # display date on label
    def display_date(self, span_of_column, row, column, pad_x="0", pad_y="0", stick="ew", font=("Calibri", 12, "bold")):
        now = datetime.datetime.now()
        now_str = now.strftime(str("%d.%m.%y"))
        self.add_label(now_str, span_of_column, row, column, pad_x, pad_y, stick, font)

    # label that changes with drop menu, value is needed for the global variable to change
    def add_drop_menu_label(self, value):
        self.add_label(self.drop_down_menu_option.get(), 1, 2, 3, "", "", "ew")


gui = GUI()
