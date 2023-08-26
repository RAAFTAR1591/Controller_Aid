import pyautogui as p
import time as t
import os
import os_test as ot

""" These functions are mainly for Ubuntu, some of these functions may not work for Windows. 
You can customize your shortcuts according to your system and preference. 
You may also include other functions. 
You just need to change the key bindings in the hotkey function. """


def display(string):
    p.write(string)


def clearall():
    p.hotkey('ctrl', 'a')
    p.hotkey('del')


def undo_b():
    p.hotkey('ctrl', 'z')


def redo_b():
    p.hotkey('ctrl', 'y')


def l_side_b():
    p.hotkey('win', 'left')


def r_side_b():
    p.hotkey('win', 'right')


def desktop():
    p.hotkey('win', 'd')


def change_window():
    p.hotkey('alt', 'tab')


def shutdown():
    if(ot==1):
        os.system("init 0")
    elif(ot==0):
        os.system("shutdown /s")
    else:
        print("This feature is not available for your system. Please wait for further improvement.")


def menu():
    p.hotkey('win', 'a')


def wind():
    p.hotkey('win')


def fun():
    os.system("sl")


def closew():
    p.hotkey('atl', 'f4')


def arduino():
    p.hotkey('win', '3')


def upb():
    p.hotkey('up')


def downb():
    p.hotkey('down')


def leftb():
    p.hotkey('left')


def rightb():
    p.hotkey('right')
