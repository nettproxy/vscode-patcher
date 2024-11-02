import serial
import tkinter as tk
from tkinter import messagebox
ser = serial.Serial('COM6', 115200, timeout=1)

def main():
    while True:
        if ser.in_waiting > 0:
            try:
                line = ser.readline().decode('utf-8', errors='ignore').strip()
                print(f"Received from ESP8266: {line}")
                if "ON" in line:
                    print("ON")
                elif "OFF" in line:
                    print("OFF")

            except UnicodeDecodeError:
                print("Received non-UTF-8 encoded data; ignoring this line.")
            except Exception as e:
                print("no workos!")

if __name__ == "__main__":
    main()
