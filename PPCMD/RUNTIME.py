import time
import shutil
import os

time_log_time = time.strftime("%H-%M-%S")

while True:
    if time_log_time == "00:00:00":
        shutil.copy(
            r"C:\Users\jbd\Desktop\PPCMD\logs.txt",
            fr"C:\Users\jbd\Desktop\PPCMD\logs\logs_backup_{time_log_time}.txt"
        )
    time.sleep(1)