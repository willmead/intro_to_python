from tkinter import *

class Calculator:

    def __init__(self, parent):
        self.parent = parent
        self.string = ""
        self.layout()


    def layout(self):
        self.entry = Text(self.parent, state=DISABLED, height=1, width=1, font=('Verdana', 20))
        self.entry.grid(row=0, column=0, columnspan=3, sticky=NSEW)

        self.equals_button = Button(self.parent, text="=", command=self.equal_button_click)
        self.equals_button.grid(row=4, column=1, columnspan=2,  sticky=NSEW)

        self.make_button(" + ", 5, 0)
        self.make_button(" - ", 5, 1)

        self.make_button("1", 1, 0)
        self.make_button("2", 1, 1)
        self.make_button("3", 1, 2)

        self.make_button("4", 2, 0)
        self.make_button("5", 2, 1)
        self.make_button("6", 2, 2)

        self.make_button("7", 3, 0)
        self.make_button("8", 3, 1)
        self.make_button("9", 3, 2)

        self.make_button("0", 4, 0)

    def make_button(self, label, row, column):
        self.button = Button(self.parent, text=label, command=lambda: self.press(label), font=('Verdana', 20))
        self.button.grid(row=row, column=column, sticky=NSEW)

    def display(self, text):
        self.entry.config(state=NORMAL)
        self.entry.delete('1.0', END)
        self.entry.insert('1.0', text)
        self.entry.config(state=DISABLED)

    def press(self, text):
        self.string += text
        self.display(self.string)

    def equal_button_click(self):
        answer = eval(self.string)
        self.display(answer)
        self.string = ''


main = Tk()
main.title("Calculator")
main.geometry("300x300")

for i in range(3):
    main.grid_columnconfigure(i,weight=1)
for i in range(6):
    main.grid_rowconfigure(i,weight=1)

calculator = Calculator(main)
main.mainloop()
