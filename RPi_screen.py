from tkinter import *
from PIL import Image, ImageTk


class test(Tk):

    def __init__(self):
        super().__init__()

        #Setting dimensions and resizability
        self.geometry("500x500")
        self.resizable(False,False)

        self.frame = Frame(self, width=500, height=500)
        self.frame.pack()
        self.frame.place(anchor="center", relx=0.15, rely=0.15)

        #Logo
        self.img = ImageTk.PhotoImage(Image.open(("HUST_logo.png")).resize((150,150)))

        #Adding logo to a label which is added to the frame
        label = Label(self.frame, image=self.img)
        label.pack()

    def logo(self):
        #self.iconphoto = PhotoImage(file="HUST_logo.png")
        self.backGroundImage = PhotoImage(file="HUST_logo.png")
        self.backGroundImageLabel = Label(self, image=self.backGroundImage)
        self.backGroundImageLabel.place(x=0,y=0)


if __name__ == "__main__":
    t = test()
    #t.logo()
    t.mainloop()