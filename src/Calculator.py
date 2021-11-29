from tkinter import END, messagebox, StringVar
from Tkinter_MiniWorkEnvironment.src.GUI import GUI


class Calculator:

    def __init__(self):
        gui = GUI.get_gui()
        self.operators = ["+", "-", "*", "/", "%"]
        self.digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        self.intermediate_result_text = StringVar()
        third_row = 3
        fourth_row = 4
        fifth_row = 5
        sixth_row = 6
        seventh_row = 7
        eighth_row = 8
        self.intermediate_result_label = GUI.add_label(gui, "intermediate result", self.intermediate_result_text,
                                                       2, 2, 3, 5, 5)
        self.entry = GUI.add_entry(gui, 35, 5, "circle", "green", "white", 3, 1, 3, 5, 2)
        self.clear_button = GUI.add_button(gui, "CLEAR", self.clear_entry, "white", "orange", 2, 5, 0, 0)
        self.button_1 = GUI.add_button(gui, "1", lambda: self.input_num(1), "black", "white", third_row, 3, 0, 0)
        self.button_2 = GUI.add_button(gui, "2", lambda: self.input_num(2), "black", "white", third_row, 4, 0, 0)
        self.button_3 = GUI.add_button(gui, "3", lambda: self.input_num(3), "black", "white", third_row, 5, 0, 0)
        self.button_4 = GUI.add_button(gui, "4", lambda: self.input_num(4), "black", "white", fourth_row, 3, 0, 0)
        self.button_5 = GUI.add_button(gui, "5", lambda: self.input_num(5), "black", "white", fourth_row, 4, 0, 0)
        self.button_6 = GUI.add_button(gui, "6", lambda: self.input_num(6), "black", "white", fourth_row, 5, 0, 0)
        self.button_7 = GUI.add_button(gui, "7", lambda: self.input_num(7), "black", "white", fifth_row, 3, 0, 0)
        self.button_8 = GUI.add_button(gui, "8", lambda: self.input_num(8), "black", "white", fifth_row, 4, 0, 0)
        self.button_9 = GUI.add_button(gui, "9", lambda: self.input_num(9), "black", "white", fifth_row, 5, 0, 0)
        self.button_0 = GUI.add_button(gui, "0", lambda: self.input_num(0), "black", "white", sixth_row, 5, 0, 0)
        self.plus_button = GUI.add_button(gui, "+", lambda: self.input_operator("+"), "#ff00ea", "black",
                                          sixth_row, 3, 0, 0)
        self.minus_button = GUI.add_button(gui, "-", lambda: self.input_operator("-"), "#ff00ea", "black",
                                           sixth_row, 4, 0, 0)
        self.multiplication_button = GUI.add_button(gui, "*", lambda: self.input_operator("*"), "#ff00ea", "black",
                                                    seventh_row, 3, 0, 0)
        self.division_button = GUI.add_button(gui, "/", lambda: self.input_operator("/"), "#ff00ea", "black",
                                              seventh_row, 4, 0, 0)
        self.modulo_button = GUI.add_button(gui, "%", lambda: self.input_operator("%"), "#ff00ea", "black",
                                            seventh_row, 5, 0, 0)
        self.result_button = GUI.add_button(gui, "=", self.display_result, "#412763", "#766c82", eighth_row, 5, 0, 0)


    # insert into the entry
    def input_num(self, num):
        if len(self.entry.get()) < 33:
            old_text = self.entry.get()
            self.entry.delete(0, END)
            new_text = old_text + str(num)
            self.entry.insert(0, new_text)
        else:
            messagebox.showwarning("To many Arguments", "Maximum size is 33 !")

    # operators needed to be checked in advance
    def input_operator(self, operator):
        input_text = self.entry.get()
        if input_text == "" and operator in self.operators:
            messagebox.showwarning("False Input", "No number before operator!")
            return None
        for i in input_text:
            if i in self.operators:
                messagebox.showwarning("To many Operators", "Maximum amount of Operators is only one !")
                return None
        else:
            self.input_num(operator)

    # clean entry
    def clear_entry(self):
        self.entry.delete(0, END)

    # checks if input for validity
    def display_result(self):
        input_text = self.entry.get()
        operator = self.operator_and_input_check(input_text)
        if operator is None:
            messagebox.showwarning("False Input", "No Operator found !")
            return None
        else:
            input_numbers = input_text.split(operator)
            if "" in input_numbers:
                input_numbers.remove("")
            if len(input_numbers) == 2:
                self.calculate_result(input_numbers, operator)
                self.entry.delete(0, END)
            else:
                messagebox.showwarning("NoneException", "One of the operators is None !")

    # checks if an operator is there and if the text has invalid input (example alphabet)
    def operator_and_input_check(self, input_text):
        operator = None
        for i in input_text:
            if i in self.operators:
                operator = i
            if i not in self.operators and i not in self.digits:
                messagebox.showwarning("False Input", "Input has other than DIGITS or OPERATORS !")
                self.clear_entry()
                return None
        return operator

    # calculate depending on the operator
    def calculate_result(self, input_numbers, operator):
        first_num = None
        second_num = None
        intermediate_result = None
        for num in input_numbers:
            if first_num is None:
                first_num = int(num)
            else:
                second_num = int(num)

        if operator == "+":
            intermediate_result = first_num + second_num
        elif operator == "-":
            intermediate_result = first_num - second_num
        elif operator == "*":
            intermediate_result = first_num * second_num
        elif operator == "/":
            intermediate_result = first_num / second_num
        elif operator == "%":
            intermediate_result = first_num % second_num
        else:
            messagebox.showwarning("Unknown Error", "Questionable task !")

        self.intermediate_result_text.set(intermediate_result)
