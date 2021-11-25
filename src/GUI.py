import datetime
from tkinter.ttk import *
from tkinter import *
import tkinter as tk


# initialization with tk.Tk__init all Methods are being inherited
# this class contains all methods needed to create Objects on the GUI
from tkinter import Entry


class GUI(tk.Tk):
    entry: Entry                                            # type hint

    # the class itself becomes the ROOT
    def __init__(self):
        tk.Tk.__init__(self)                                # instead super()...
        self.title("Mini Work Environment")                 # window title
        self.geometry("1280x720")                           # window size
        self.resizable(width=True, height=True)             # resizable window
        self.config(bg="#06505c")                           # background_color
        icon_image = PhotoImage(file="res/icon.png")        # Icon from .png
        self.wm_iconphoto(True, icon_image)

    def add_label(self, string, span_of_column, row, column, font=("Calibri", 12, "bold")):
        Label(self, text=str(string), font=font).grid(columnspan=span_of_column, row=row, column=column, sticky='ew')

    def add_entry(self, size, b_width, cur, fore_ground, back_ground, row, column):
        self.entry = tk.Entry(self, width=size, borderwidth=b_width, fg=fore_ground, bg=back_ground, cursor=cur)
        self.entry.grid(row=row, column=column, padx='0', pady='0', sticky='ew')

    def add_button(self, string, com, fore_ground, back_ground, row, column):
        button = tk.Button(self, text=string, command=com, fg=fore_ground, bg=back_ground)
        button.grid(row=row, column=column, padx='0', pady='0', sticky='ew')

    def add_radio_button(self, string, var, val, com, row, column):
        r = Radiobutton(self, text=string, variable=var, value=val, command=com)
        r.grid(row=row, column=column, sticky='ew')

    def add_drop_menu(self, var, row, column, *args):
        o = OptionMenu(self, var, *args, command=self.add_drop_menu_label)
        o.config(bg='light blue')
        o.grid(row=row, column=column, sticky='ew')

    def add_checkbox(self, string, var, row, column):
        c = Checkbutton(self, text=string, variable=str(var), onvalue="Did choose, YAY!", offvalue="Did not choose.")
        c.deselect()
        c.grid(row=row, column=column, sticky='ew')

    # display an image on label
    def display_img(self, file_name, row_span, column_span, row, column):
        img = PhotoImage(file=file_name)
        panel = Label(self, image=img)
        panel.image = img
        panel.grid(row=row, column=column, rowspan=row_span, columnspan=column_span)

    # label that changes with drop menu, value is needed for the global variable to change
    def add_drop_menu_label(self, value):
        self.add_label(self.drop_down_menu_option.get(), 1, 2, 3)

    # display time on label
    def display_time(self, span_of_column, row, column, font=("Calibri", 12, "bold")):
        now = datetime.datetime.now()
        now_str = now.strftime(str("%H:%M:%S"))
        self.add_label(now_str, span_of_column, row, column, font)

    # display date on label
    def display_date(self, span_of_column, row, column, font=("Calibri", 12, "bold")):
        now = datetime.datetime.now()
        now_str = now.strftime(str("%d.%m.%y"))
        self.add_label(now_str, span_of_column, row, column, font)