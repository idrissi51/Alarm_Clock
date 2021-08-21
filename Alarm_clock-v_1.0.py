
from tkinter import *
import time
import datetime
import winsound
noow = datetime.datetime.now().strftime("%H:%M:%S")


def alarm(set_alarm_timer):
    while True:
        time.sleep(1)
        current_time = datetime.datetime.now()
        now = current_time.strftime("%H:%M:%S")
        date = current_time.strftime("%d:%m:%y")
        print("The Set Date is:", date)
        print(now)
        if set_alarm_timer == now:
            print("Time to Wake up")
            winsound.PlaySound("sound wav", winsound.SND_ASYNC)
            break


def actual_time():
    set_alarm_timer = f"{hour.get()}:{min.get()}:{sec.get()}"
    alarm(set_alarm_timer)


root = Tk()
root.geometry("400x200")
root.title("Alarm clock")
time_format = Label(root, text="Enter time in 24 hour format!",
                    fg="red", bg="black", font="Arial").place(x=100, y=120)
addTime = Label(root, text="  Hour         Min         Sec",
                font=60).place(x=110)
setYourAlarm = Label(root, text="When to wake you up", bg="orange", fg="blue", font=(
    "Helevetica", 7, "bold")).place(x=0, y=29)
Timenew = Label(root, text=f"Time now: {noow}", fg="black",
                font="arial 10 ").place(x=140, y=170)
hour = StringVar()
min = StringVar()
sec = StringVar()
hourTime = Entry(root, textvariable=hour, bg="green",
                 width=10).place(x=110, y=30)
minTime = Entry(root, textvariable=min, bg="green",
                width=10).place(x=170, y=30)
secTime = Entry(root, textvariable=sec, bg="green",
                width=10).place(x=230, y=30)

Button(root, text="Set Alarm", fg="red", width=10,
       command=actual_time).place(x=160, y=70)
root.mainloop()
