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
        self.img = ImageTk.PhotoImage(Image.open(("HUST_logo.png")).resize((100, 100)))

        self.receive_canvas = Canvas(self, width=500,height=500)
        self.send_canvas = Canvas(self, width=500, height=500)


    def receive_screen(self):
        #self.send_canvas.delete("all")
        #self.

        self.receive_canvas.create_image(250, 100, image=self.img)

        send_btn = Button(self, text="Send CAN", command=lambda: self.send_screen())
        send_btn.pack(side=BOTTOM, padx=10, pady=10)

        self.receive_canvas.create_text(250,200, text="Receiving CAN", fill="black", font=("Arial",25))

        #BMS
        self.receive_canvas.create_text(125, 275, text="pack current:", font=("Arial", 15))
        self.receive_canvas.create_text(125, 325, text="pack voltage:", font=("Arial", 15))
        self.receive_canvas.create_text(125, 375, text="temp BMS:", font=("Arial", 15))
        self.receive_canvas.create_text(125, 425, text="cell voltage:", font=("Arial", 15))

        #MC
        self.receive_canvas.create_text(350, 275, text="velocity ms:", font=("Arial", 15))
        self.receive_canvas.create_text(350, 325, text="velocity rpm:", font=("Arial", 15))
        self.receive_canvas.create_text(350, 375, text="heatsink temp", font=("Arial", 15))
        self.receive_canvas.create_text(350, 425, text="motor temp:", font=("Arial", 15))

        self.receive_canvas.pack()


    def send_screen(self):
        #self.receive_canvas.delete("all")

        self.send_canvas.create_image(250, 100, image=self.img)

        #send_btn = Button(self, text="Receive CAN", command=lambda: self.receive_screen())
       # send_btn.pack(side=BOTTOM, padx=10, pady=10)

        self.send_canvas.create_text(250,200, text="Sending CAN", fill="black", font=("Arial",25))

        #self.send_canvas.pack()


if __name__ == "__main__":
    t = test()
    t.receive_screen()
    t.mainloop()