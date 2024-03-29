import tkinter
import re
import linecache
import time

from threading import Thread
from Database import database
from tkinter import *
from tkinter.ttk import Panedwindow

from excel_automation import ExcelAutomation
from PIL import Image, ImageTk

#   Adda slider för att kontroller motorhastighet
#   Skicka custom CAN meddelande
#

cluster = re.sub("\n", "", linecache.getline("confidential", 2))
collection = re.sub("\n", "", linecache.getline("confidential", 4))
dataB = re.sub("\n", "", linecache.getline("confidential", 6))

db = database(cluster, collection, dataB)

"""
Lägg till flera data_sets om du lägger till fler rader
i excel
"""
#excel = ExcelAutomation("excel_blad.xlsx")
class Receive_GUI(Tk):

    def __init__(self):
        super().__init__()
        self.script_start_time = time.time()


        # Fetching MC values
        self.bus_voltage_db, self.bus_current_db = 0, 0
        self.heat_sink_temp_db, self.motor_temp_db = 0, 0
        self.motor_velocity_db, self.vehicle_velocity_db = 0, 0
        self.acceleration_db, self.motor_efficiency_db = 0, 0

        # Fetching BMS values
        self.pack_current_db, self.pack_voltage_db = 0, 0
        self.temp_BMS_db, self.cell_voltage_db = 0, 0


        #Setting dimensions and resizability
        #self.attributes('-fullscreen', True)
        self.geometry("800x480")
        self.title("CAN debugger")
        self.img = ImageTk.PhotoImage(Image.open(("HUST_logo.png")).resize((100, 100)))

        self.receive_frame = Frame(self, width=800, height=480)
        self.send_frame = Frame(self, width=800, height=480)

        self.receive_screen()


    def receive_screen(self) -> None:
        self.in_main_screen = True

        logo = Label(self.receive_frame, image=self.img)
        logo.place(relx=0.5, rely=0.12, anchor="center")

        receiving_can = Label(self.receive_frame, text="Receive Can", font=("Arial", 25))
        receiving_can.place(relx=0.5, rely=0.3, anchor="center")

        # BMS
        self.pack_current = Label(self.receive_frame, text="Pack current:", font=("Arial", 15))
        self.pack_current.place(relx=0.15, rely=0.45, anchor="center")

        self.pack_voltage = Label(self.receive_frame, text="Pack voltage:", font=("Arial", 15))
        self.pack_voltage.place(relx=0.15, rely=0.57, anchor="center")

        self.temp_BMS = Label(self.receive_frame, text="Temp BMS:", font=("Arial", 15))
        self.temp_BMS.place(relx=0.35, rely=0.45, anchor="center")

        self.cell_voltage = Label(self.receive_frame, text="Cell voltage:", font=("Arial", 15))
        self.cell_voltage.place(relx=0.35, rely=0.57, anchor="center")

        # MC
        self.vehicle_velocity = Label(self.receive_frame, text="Vehicle velocity:", font=("Arial", 15))
        self.vehicle_velocity.place(relx=0.6, rely=0.45, anchor="center")

        self.motor_velocity = Label(self.receive_frame, text="Motor velocity:" + str(self.motor_velocity_db), font=("Arial", 15))
        self.motor_velocity.place(relx=0.6, rely=0.57, anchor="center")

        self.acceleration = Label(self.receive_frame, text="Acceleration:", font=("Arial", 15))
        self.acceleration.place(relx=0.6, rely=0.69, anchor="center")

        self.heatsink_temp = Label(self.receive_frame, text="Heatsink temp:", font=("Arial", 15))
        self.heatsink_temp.place(relx=0.85, rely=0.45, anchor="center")

        self.motor_temp = Label(self.receive_frame, text="Motor temp: " + str(self.motor_temp_db), font=("Arial", 15))
        self.motor_temp.place(relx=0.85, rely=0.57, anchor="center")

        self.motor_efficiency = Label(self.receive_frame, text="Motor efficiency:", font=("Arial", 15))
        self.motor_efficiency.place(relx=0.85, rely=0.69, anchor="center")

        self.receive_frame.pack()


    def send_screen(self) -> None:
        logo = Label(self.send_frame, image=self.img)
        logo.place(relx=0.5, rely=0.12, anchor="center")

        receiving_can = Label(self.send_frame, text="Send Can", font=("Arial", 25))
        receiving_can.place(relx=0.5, rely=0.3, anchor="center")

        btn_to_send = Button(self.send_frame, font=("Arial", 15), text="Receive CAN", command=lambda: self.switchScreen(False))
        btn_to_send.place(relx=0.15, rely=0.15, anchor="center")

        btn_to_exit = Button(self.send_frame, font=("Arial", 15), text="Exit", command=lambda: self.exitScreen())
        btn_to_exit.place(relx=0.15, rely=0.2, anchor="center")

        self.send_frame.pack()


    def exitScreen(self):
        self.destroy()


    def switchScreen(self, to_frame_send: bool) -> None:
        if to_frame_send:
            self.receive_frame.pack_forget()
            self.send_screen()
            print("switching to send frame")
        else:
            self.send_frame.pack_forget()
            self.receive_screen()
            print("switching to receive frame")


    def update_main_screen(self):

        self.vehicle_velocity["text"] = "Vehicle velocity: " + str(round(self.vehicle_velocity_db, 2))
        self.motor_velocity["text"] = "Motor velocity: " + str(round(self.motor_velocity_db, 2))
        self.motor_temp["text"] = "Motor temp: " + str(round(self.motor_temp_db, 2))
        self.heatsink_temp["text"] = "Heatsink temp: " + str(round(self.heat_sink_temp_db, 2))
        self.acceleration["text"] = "Acceleration: " + str(round(self.acceleration_db, 2))
        self.motor_efficiency["text"] = "Motor efficiency: " + str(round(self.motor_efficiency_db, 2))


    def update_CAN_values(self):
        update_thread = Thread(target=self.update_CAN_values)

        self.bus_voltage_db, self.bus_current_db = db.get_element(0, "bus_voltage"), db.get_element(0, "bus_current")
        self.heat_sink_temp_db, self.motor_temp_db = db.get_element(0, "heat_sink_temp"), db.get_element(0, "motor_temp")
        self.motor_velocity_db, self.vehicle_velocity_db = db.get_element(0, "motor_velocity"), db.get_element(0, "vehicle_velocity")
        self.acceleration_db, self.motor_efficiency_db = db.get_element(0, "acceleration"), db.get_element(0, "motor_efficiency")

        self.pack_current_db, self.pack_voltage_db = 0, 0
        self.temp_BMS_db, self.cell_voltage_db = 0, 0

        #self.update_excel_sheet_MC()

        if self.in_main_screen:
            self.update_main_screen()

        update_thread.start()


    def update_excel_sheet_MC(self):
        """
        current_time = time.time() - self.script_start_time
        excel.update_multiple_cells([current_time,
                                     self.bus_current_db,
                                     self.bus_voltage_db,
                                     self.motor_efficiency_db,
                                     self.heat_sink_temp_db,
                                     self.motor_temp_db,
                                     self.motor_velocity_db,
                                     self.vehicle_velocity_db,
                                     self.acceleration_db])
        """
        pass


    def update_excel_sheet_BMS(self):
        pass

if __name__ == "__main__":
    receive_can = Receive_GUI()
    receive_can.update_CAN_values()
    receive_can.mainloop()