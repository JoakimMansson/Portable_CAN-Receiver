import tkinter
from tkinter import *
from tkinter.ttk import Panedwindow

from PIL import Image, ImageTk


class test(Tk):

    def __init__(self):
        super().__init__()

        #Setting dimensions and resizability
        self.geometry("800x480")
        self.resizable(False,False)
        self.title("CAN debugger")
        self.img = ImageTk.PhotoImage(Image.open(("HUST_logo.png")).resize((100, 100)))

        self.receive_frame = Frame(self, width=800, height=480)
        self.send_frame = Frame(self, width=800, height=480)


        self.receive_screen()




    def receive_screen(self) -> None:

        logo = Label(self.receive_frame, image=self.img)
        logo.place(relx=0.5, rely=0.12, anchor="center")
        #logo.pack()

        receiving_can = Label(self.receive_frame, text="Receive Can", font=("Arial", 25))
        receiving_can.place(relx=0.5, rely=0.3, anchor="center")
        #receiving_can.pack()

        btn_to_send = Button(self.receive_frame, text="Send CAN", font=("Arial", 15), command=lambda: self.switch_screen(True))
        btn_to_send.place(relx=0.15, rely=0.15, anchor="center")
        #btn_to_send.pack()

        # BMS
        pack_current = Label(self.receive_frame, text="pack current:", font=("Arial", 15))
        pack_current.place(relx=0.3, rely=0.45, anchor="center")
        #pack_current.pack()

        pack_voltage = Label(self.receive_frame, text="pack voltage:", font=("Arial", 15))
        pack_voltage.place(relx=0.3, rely=0.57, anchor="center")
        #pack_voltage.pack()

        temp_BMS = Label(self.receive_frame, text="temp BMS:", font=("Arial", 15))
        temp_BMS.place(relx=0.3, rely=0.69, anchor="center")
        #temp_BMS.pack()

        cell_voltage = Label(self.receive_frame, text="cell voltage:", font=("Arial", 15))
        cell_voltage.place(relx=0.3, rely=0.81, anchor="center")
        #cell_voltage.pack()

        # MC
        velocity_ms = Label(self.receive_frame, text="velocity ms:", font=("Arial", 15))
        velocity_ms.place(relx=0.7, rely=0.45, anchor="center")
        #velocity_ms.pack()

        velocity_rpm = Label(self.receive_frame, text="velocity rpm:", font=("Arial", 15))
        velocity_rpm.place(relx=0.7, rely=0.57, anchor="center")
        #velocity_rpm.pack()

        heatsink_temp = Label(self.receive_frame, text="heatsink temp", font=("Arial", 15))
        heatsink_temp.place(relx=0.7, rely=0.69, anchor="center")
        #heatsink_temp.pack()

        motor_temp = Label(self.receive_frame, text="motor temp:", font=("Arial", 15))
        motor_temp.place(relx=0.7, rely=0.81, anchor="center")
        #motor_temp.pack()

        self.receive_frame.pack()


    def send_screen(self) -> None:
        logo = Label(self.send_frame, image=self.img)
        logo.place(relx=0.5, rely=0.12, anchor="center")
        #logo.pack()

        receiving_can = Label(self.send_frame, text="Send Can", font=("Arial", 25))
        receiving_can.place(relx=0.5, rely=0.3, anchor="center")
        #receiving_can.pack()

        btn_to_send = Button(self.send_frame, font=("Arial", 15), text="Receive CAN", command=lambda: self.switch_screen(False))
        btn_to_send.place(relx=0.15, rely=0.15, anchor="center")
        #btn_to_send.pack()

        self.send_frame.pack()

    def switch_screen(self, to_frame_send:bool) -> None:
        if to_frame_send:
            self.receive_frame.pack_forget()
            self.send_screen()
            print("switching to send frame")
        else:
            self.send_frame.pack_forget()
            self.receive_screen()
            print("switching to receive frame")



if __name__ == "__main__":
    t = test()
    #t.receive_screen()
    t.mainloop()