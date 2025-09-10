from pynput.mouse import Button, Controller
from dotenv import load_dotenv
from PIL import ImageGrab
from rich import print
import shutil
import tkinter as tk
import keyboard
import time
import os
import subprocess
import logging
import time

load_dotenv()

check1 = os.getenv("Check1")
check2 = os.getenv("Check2")
check3 = os.getenv("Check3")
mouse = Controller()
commands = ["calc <calculation> :: print the output of the calculation",
            "file add <NAME> <TEXT> :: adds the text to the file with the name",
            "    -create <NAME> <TEXT> :: creates a file with the text and name",
            "get pixel <x, y> ::  gives you the color of the position",
            "         -point <Seconds> :: after the seconds it will give you the position and color of the position of your mouse",
            "help :: shows this text",
            "keyboard <key> :: presses a key",
            "   -hold <key> :: holds a key for 3 seconds",
            "logs backup :: creates a backup in logs"
            "python <code> :: executes the code",
            "say <text> :: prints the text",
            "start <FILE NAME or PATH> :: starts a program",
            "sys <original CMD command> :: executes an original cmd command",
            "test :: checks the system",
            "tk geo <0x0> :: sets the geometry of the program",
            "  -start :: starts the application",
            "  -title <Test> :: sets the title of the application"
            ]

if check1 == check2:
    if check2 == check3:
        print("All System are fine")
    else:
        print("virus installed")
else:
    print("virus installed")



logging.basicConfig(level=logging.DEBUG)

with open("Assets.txt", "r") as f0:
    _, _, ASK_ORDER = f0.readline().partition("ASK_ORDER: ")
    _, _, MS_ERROR = f0.readline().partition("MS_ERROR: ")
    _, _, LOGS_TARGET = f0.readline().partition("LOGS_TARGET: ")

with open("Credits.txt", "r") as f1:
    MS_CREDITS = f1.read()

def logging_add_ms(logging_message):
    time_stemp = time.strftime("%H:%M:%S")
    with open("logs.txt", "a") as logs:
        Message = logs.write(f"[{time_stemp}]{logging_message}\n")







def importorder():
    global G1
    G1 = tk.Tk()
    order = input(ASK_ORDER)

    if order.startswith("start "):
        print("starting  <|>")
        subprocess.run([order.replace("start ", "")])
        logging_add_ms(order)

    elif order.startswith("sys "):
        print("executing  <|>")
        os.system(order.replace("sys ", ""))
        logging_add_ms(order)

    elif order.startswith("say "):
        print(order.replace("say ", ""))
        logging_add_ms(order)

    elif order.startswith("keyboard "):
        if order.startswith("keyboard hold"):
            keyboard.press(order.replace("keyboard hold ", ""))
            time.sleep(3)
            keyboard.release(order.replace("keyboard hold ", ""))
        keyboard.press(order.replace("keyboard ", ""))
        logging_add_ms(order)

    elif order.startswith("get "):
        if order == "get pixel":
            x, y = map(int, order.replace("get pixel", "" ).split(","))
            screenshot = ImageGrab.grab()
            color = screenshot.getpixel((x, y))
            print(color)

        elif order.startswith("get pixel point"):
            timep = order.replace("get pixel point ", "")
            time.sleep(float(timep))
            screenshot = ImageGrab.grab()
            colorp = screenshot.getpixel(mouse.position)
            print(f"color code {colorp} | mouse position {mouse.position}")
        logging_add_ms(order)

    elif order.startswith("calc "):
        print("calculating")
        calculation = order.replace("calc ", "")
        output_calc = eval(calculation.replace("pi", "3.14159265359"))
        print(output_calc)
        logging_add_ms(order)

    elif order.startswith("python "):
        print(eval(order.replace("python ", "")))
        logging_add_ms(order)

    elif order.startswith("tk "):
        if order == "tk start":
            tk.mainloop()
        elif order.startswith("tk geo "):
            G1.geometry(order.replace('tk geo ', ""))
        elif order.startswith("tk title "):
            G1.title(order.replace('tk title ', ""))
        logging_add_ms(order)

    elif order.startswith("logs "):
        if order.startswith("logs backup"):
            time_log_name = time.strftime("%H-%M-%S")
            shutil.copy(
                fr"{LOGS_TARGET}".strip(),
                fr"C:\Users\Documents\PP\PPCMD\logs\logs_backup_{time_log_name}.txt"
            )

        print(f"Backup created: logs_backup_{time_log_name}.txt")

    elif order.startswith("credits"):
        print(MS_CREDITS)
        logging_add_ms(order)

    elif order.startswith("file create "):
        global order_striped
        global name, text
        order_striped = order.replace("file create ", "")
        name, text = order_striped.split(" ", 1)
        with open(name, "w") as nf:
            nf.write(text)

    elif order.startswith("file add "):
        global order_striped1
        global name1, text1
        order_striped1 = order.replace("file add ", "")
        name1, text1 = order_striped1.split(" ", 1)
        with open(name1, "a") as nf:
            nf.write(f"{text1}\n")

    elif order == ("test"):
        try:
            print("test succesfully")
        except:
            print("Something went wrong")

    elif order == ("help"):
        print("\n".join(commands))

    else:
#        os.system(order + " >nul 2>&1")
        print("This command is unknown")
    logging_add_ms(order)

    try:
        importorder()
    except Exception as e:
        print(f"ERROR: {e}")

try:
    importorder()
except Exception as e:
    print(f"ERROR: {e}")