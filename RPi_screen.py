import tkinter
from tkinter import *
from PIL import Image, ImageTk


class test(Tk):

    def __init__(self):
        super().__init__()

        #Setting dimensions and resizability
        self.geometry("500x500")
        self.resizable(False,False)
        self.title("CAN debugger")

        self.canvas = Canvas(self, width=500,height=500)

        self.frame = Frame(self.canvas, width=500, height=500)
        self.frame.pack()
        self.frame.place(anchor="center", relx=0.5, rely=0.15)

        #Logo
        self.img = ImageTk.PhotoImage(Image.open(("HUST_logo.png")).resize((100,100)))

        #Adding logo to a label which is added to the frame
        label = Label(self.frame, image=self.img)
        label.pack()

    def testing(self):
        self.canvas.create_text(250,200, text="Receiving CAN", fill="black", font=("Arial",25))

        #BMS
        self.canvas.create_text(125, 275, text="pack current:", font=("Arial", 15))
        self.canvas.create_text(125, 325, text="pack voltage:", font=("Arial", 15))
        self.canvas.create_text(125, 375, text="temp BMS:", font=("Arial", 15))
        self.canvas.create_text(125, 425, text="cell voltage:", font=("Arial", 15))

        #MC
        self.canvas.create_text(350, 275, text="velocity ms:", font=("Arial", 15))
        self.canvas.create_text(350, 325, text="velocity rpm:", font=("Arial", 15))
        self.canvas.create_text(350, 375, text="heatsink temp", font=("Arial", 15))
        self.canvas.create_text(350, 425, text="motor temp:", font=("Arial", 15))

        self.canvas.pack()


if __name__ == "__main__":
    t = test()
    t.testing()
    t.mainloop()