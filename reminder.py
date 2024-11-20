from tkinter import *
from tkinter import messagebox as mb
from tkinter import simpledialog as sd
import datetime
import time
import pygame

def sety():
    rem=sd.askstring("Время напоминания",
                     "Введите время напоминания в формате ЧЧ:ММ")
    if rem:
        try:
            hour=int((rem.split(":")[0]))
            minute=int((rem.split(":")[2]))
            now=datetime.datetime.now()
            print(now)
            dt=now.replace(hour=hour, minute=minute, second=0)
            print(dt)
            label.config(text=f"Напоминание установлено на {hour}:{minute}")
        except ValueError:
            mb.showerror("Упс","Неподходящий формат времени")
        except Exception as e:
            print(e)


window=Tk()
window.title("Звуковая напоминалка")

label=Label(text="Установите напоминание", font=("Lobster",30))
label.pack(pady=30)

button=Button(text="Установить", font=("Lobster", 20), command=sety)
button.pack()


window.mainloop()

