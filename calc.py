from tkinter import Tk, Button, Canvas, PhotoImage, Entry
 

class Calc(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("300x300")
        self.title("calc 0.0.1")

        self.draw_interface()


    def draw_interface(self):
        #button
        button = Button(self, text="hello hi hi", width=8, height=2)
        button.place(x = 1, y = 2)

        #canvas
        canvas = Canvas(
        self,
        bg = "#FFFFFF",
        height = 610,
        width = 311,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
        )
        canvas.place(x = 0, y = 0)

        #entry
        entry_bg_1 = canvas.create_image(
            158.0,
            201.0,
            image=PhotoImage(file="assets/entry_1.png")
        )
        entry_1 = Entry(
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0,
            font=("Arial", 25),
        )
        entry_1.place(
            x=40.0,
            y=171.0,
            width=236.0,
            height=58.0
        )


calc = Calc()
calc.mainloop()