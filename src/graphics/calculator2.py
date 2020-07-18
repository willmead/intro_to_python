from tkinter import *


class Calculator:
    def __init__(self, parent):
        self.parent = parent

        self.container = Frame()
        self.container.grid()

        self.string = ''

        self.entry(0, 0)

        self.button('1', 1, 0)
        self.button('2', 1, 1)
        self.button('3', 1, 2)

        self.button('4', 2, 0)
        self.button('5', 2, 1)
        self.button('6', 2, 2)

        self.button('7', 3, 0)
        self.button('8', 3, 1)
        self.button('9', 3, 2)

        self.button('0', 4, 0)

        self.button('+', 1, 3)
        self.button('-', 1, 4)
        self.button('*', 2, 3)
        self.button('/', 2, 4)

        self.button('(', 3, 3)
        self.button(')', 3, 4)

        self.button_eq('=', 4, 1)

        self.button_clear('clear', 4, 3)
        self.button_rem('<', 4, 4)

    def display(self, text_):
        self.entry.config(state=NORMAL)
        self.entry.delete('1.0', END)
        self.entry.insert('1.0', text_)
        self.entry.config(state=DISABLED)

    def normal_button_click(self, text_):
        self.string = '' + self.string + text_
        self.display(self.string)

    def equal_button_click(self):
        self.display(eval(self.string))
        self.string = ''

    def rem_button_click(self):
        self.string = '' + self.string[0:-1]
        self.display(self.string)

    def clear_button_click(self):
        self.display('')
        self.string = ''


root = Tk()
calculator = Calculator(root)
root.geometry("300x300")

root.mainloop()
