import serial as s
import time as t
import functions as f

""" In the first value of s.Serial, you have to give your own Serial port name where the Arduino UNO is connected. You can get that from Arduino IDE.
Here, I have given the possible ports present in my system. It will change from system to system. """


def work():
    flag = 0

    try:
        ser = s.Serial('/dev/ttyACM1', 9800, timeout=1)
    except:
        flag += 1

    try:
        ser = s.Serial('/dev/ttyACM0', 9800, timeout=1)
    except:
        flag += 1

    try:
        ser = s.Serial('COM4', 9800, timeout=1)
    except:
        flag += 1

    try:
        ser = s.Serial('COM3', 9800, timeout=1)
    except:
        flag += 1

    if (flag == 4):
        print("Device not connected.\nPlease connect the device.")
        print("\U0001f600")
        exit(0)

    t.sleep(2)

    while (1):
        try:
            line = ser.readline()
            if line:
                string = line.decode().strip()
                print(string, end="\n")
                if (string == "F"):
                    raise KeyboardInterrupt
                if (string == "E"):
                    f.shutdown()
                if (string == "+X"):
                    f.r_side_b()
                if (string == "-X"):
                    f.l_side_b()
                if (string == "B"):
                    f.redo_b()
                if (string == "C"):
                    f.menu()
                if (string == "D"):
                    f.undo_b()
                if (string == "K"):
                    f.wind()
                if (string == "+Y"):
                    f.change_window()
                if (string == "-Y"):
                    f.desktop()
                if (string == "A"):
                    f.arduino()
        except:
            print("Device disconnected.")
            exit(0)
