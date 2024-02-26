from tkinter import Tk, Button

class Calc(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("300x300")
        self.title("calc 0.0.1")

        #button
        button = Button(self, text="hello hi hi", width=8, height=2)
        button.place(x = 1, y = 2)

calc = Calc()
calc.mainloop()