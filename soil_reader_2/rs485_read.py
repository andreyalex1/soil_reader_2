#!/usr/bin/env python3

#Developed by Andrei Smirnov. 2024
#MSU Rover Team. Voltbro. NIIMech 

import serial
#print(list(serial.tools.list_ports.comports()))
ser = serial.Serial('/dev/ttyUSB0', 4800, timeout=1)
print(ser.name) 
ser.write(b'\x01\x03\x00\x00\x00\x07\x04\x08')
bt = ser.read(19)
ba = bytearray(bt)
humidity = int.from_bytes(ba[3:5], "big") / 10
temperature = int.from_bytes(ba[5:7], "big") / 10
conductivity = int.from_bytes(ba[7:9], "big") / 10
ph = int.from_bytes(ba[9:11], "big") / 10
n = int.from_bytes(ba[11:13], "big") / 10
p = int.from_bytes(ba[13:15], "big") / 10
k = int.from_bytes(ba[15:17], "big") / 10
print("temperature:\t" + str(temperature) + " C")
print("humidity:\t" + str(humidity) + " %")
print("conductivity:\t" + str(conductivity) + " us/cm")
print("ph:\t\t" + str(ph))
print("nitrogen:\t" + str(n) + " mg/kg")
print("phosphorus:\t" + str(p) + " mg/kg")
print("potassium:\t" + str(k)+ " mg/kg")
#ser.write(b'hello')


