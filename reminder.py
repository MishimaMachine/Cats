from tkinter import *
from tkinter import messagebox as mb
from tkinter import simpledialog as sd
import datetime
import time
import pygame

def sety():
    global t
    rem=sd.askstring("Время напоминания",
                     "Введите время напоминания в формате ЧЧ:ММ")
    if rem:
        try:
            hour=int((rem.split(":")[0]))
            minute=int((rem.split(":")[1]))
            now=datetime.datetime.now()
            print(now)
            dt=now.replace(hour=hour, minute=minute, second=0)
            print(dt)
            t=dt.timestamp()
            print(t)
            label.config(text=f"Напоминание установлено на {hour:02}:{minute:02}")
        except ValueError:
            mb.showerror("Упс","Неподходящий формат времени")
        except Exception as e:
            print(e)

def check():
    global t
    if t:
        now=time.time()
        print(now)
        if now>=t:
            play_snd()
            t=None
    window.after(10000,check)


def play_snd():
    pygame.mixer.init()
    pygame.mixer.music.load("dzyn.mp3")
    pygame.mixer.music.play()


window=Tk()
window.title("Звуковая напоминалка")

label=Label(text="Установите напоминание", font=("Monotype Corsiva",30))
label.pack(pady=30)

button=Button(text="Установить", font=("Impact", 20), command=sety)
button.pack()

t=None

check()

window.mainloop()

