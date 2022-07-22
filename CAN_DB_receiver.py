import re
import linecache
import numpy
import matplotlib.pyplot as plt
import time
import psutil
import collections

from Database import database
from matplotlib.animation import FuncAnimation


cluster = re.sub("\n", "", linecache.getline("confidential", 2))
collection = re.sub("\n", "", linecache.getline("confidential", 4))
dataB = re.sub("\n", "", linecache.getline("confidential", 6))

db = database(cluster, collection, dataB)

bus_voltage, bus_current = 0, 0
heat_sink_temp, motor_temp = 0, 0
motor_velocity, vehicle_velocity = 0, 0

def update_value():
    global bus_voltage, bus_current, heat_sink_temp, motor_temp, motor_velocity, vehicle_velocity
    bus_voltage, bus_current = db.get_element(0, "bus_voltage"), db.get_element(0, "bus_current")
    heat_sink_temp, motor_temp = db.get_element(0, "heat_sink_temp"), db.get_element(0, "motor_temp")
    motor_velocity, vehicle_velocity = db.get_element(0, "motor_velocity"), db.get_element(0, "vehicle_velocity")
    current_time = time.time()

    #ax.cla()
    #VV_ax.cla()

    MV_ax.plot(current_time-start_time, motor_velocity)
    MV_ax.scatter(current_time-start_time, motor_velocity)
    MV_ax.set_ylim(0, 100)
    MV_ax.set_xlabel("t")
    MV_ax.set_ylabel("RPM")
    MV_ax.set_title("Motor velocity")

    VV_ax.plot(current_time-start_time, vehicle_velocity)
    VV_ax.scatter(current_time-start_time, vehicle_velocity)
    VV_ax.set_ylim(0, 50)
    VV_ax.set_xlabel("t")
    VV_ax.set_ylabel("m/s")
    VV_ax.set_title("Vehicle velocity")

    BV_ax.plot(current_time - start_time, bus_voltage)
    BV_ax.scatter(current_time - start_time, bus_voltage)
    BV_ax.set_ylim(0, 30)
    BV_ax.set_xlabel("t")
    BV_ax.set_ylabel("V")
    BV_ax.set_title("Bus Voltage")

    BC_ax.plot(current_time - start_time, bus_current)
    BC_ax.scatter(current_time - start_time, bus_current)
    BC_ax.set_ylim(0, 30)
    BC_ax.set_xlabel("t")
    BC_ax.set_ylabel("A")
    BC_ax.set_title("Bus Current")

    HST_ax.plot(current_time - start_time, heat_sink_temp)
    HST_ax.scatter(current_time - start_time, heat_sink_temp)
    HST_ax.set_ylim(0, 50)
    HST_ax.set_xlabel("t")
    HST_ax.set_ylabel("C")
    HST_ax.set_title("Heat-sink temp")

    MT_ax.plot(current_time - start_time, motor_temp)
    MT_ax.scatter(current_time - start_time, motor_temp)
    MT_ax.set_ylim(0, 50)
    MT_ax.set_xlabel("t")
    MT_ax.set_ylabel("C")
    MT_ax.set_title("Motor temp")


start_time = time.time()

fig = plt.figure(figsize=(12, 6), facecolor="#DEDEDE")

# MV - Motor velocity
MV_ax = plt.subplot(2, 3, 1)
MV_ax.set_facecolor("#DEDEDE")

# VV - Vehicle velocity
VV_ax = plt.subplot(2, 3, 2)
VV_ax.set_facecolor("#DEDEDE")

# BV - Bus voltage
BV_ax = plt.subplot(2, 3, 3)
BV_ax.set_facecolor("#DEDEDE")

# BC - Bus current
BC_ax = plt.subplot(2, 3, 4)
BC_ax.set_facecolor("#DEDEDE")

# HST - Heat-sink temperature
HST_ax = plt.subplot(2, 3, 5)
HST_ax.set_facecolor("#DEDEDE")

# MT - Motor temperature
MT_ax = plt.subplot(2, 3, 6)
MT_ax.set_facecolor("#DEDEDE")


ani = FuncAnimation(fig, lambda x: update_value(), interval=1)
plt.show()
