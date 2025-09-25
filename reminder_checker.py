import ctypes
import time
from datetime import datetime
import os

# Load reminder.so
class ReminderStruct(ctypes.Structure):
    _fields_ = [
        ("title", ctypes.c_char * 50),
        ("date", ctypes.c_char * 11),
        ("time", ctypes.c_char * 6),
        ("repeat", ctypes.c_char * 10),
        ("sound", ctypes.c_char * 256)
    ]

reminder = ctypes.CDLL('./reminder.so')
reminder.getReminderCount.restype = ctypes.c_int
reminder.getReminders.restype = ctypes.POINTER(ReminderStruct)

# Fungsi main
def play_sound(path):
    os.system(f'ffplay -nodisp -autoexit "{path}" > /dev/null 2>&1')

def show_notification(title, time_):
    os.system(f'notify-send "Reminder ⏰" "{title} - {time_}"')

def main():
    shown = set()
    while True:
        count = reminder.getReminderCount()
        ptr = reminder.getReminders()
        now = datetime.now().strftime("%H:%M")

        for i in range(count):
            rem = ptr[i]
            title = rem.title.decode()
            time_ = rem.time.decode()
            sound = rem.sound.decode()

            unique_key = f"{title}-{time_}"
            if time_ == now and unique_key not in shown:
                show_notification(title, time_)
                play_sound(sound)
                shown.add(unique_key)

        time.sleep(30)

if __name__ == "__main__":
    main()
