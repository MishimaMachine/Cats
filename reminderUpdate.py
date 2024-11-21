from tkinter import *
from tkinter import messagebox as mb
from tkinter import simpledialog as sd
import datetime
import time
import pygame

t=0
text=0
lbl=0
music = False


def sety():
    global t, text
    rem=sd.askstring("Время напоминания",
                     "Введите время напоминания в формате ЧЧ:ММ")
    if rem:
        try:
            hour=int(rem.split(":")[0])
            minute=int(rem.split(":")[1])
            now=datetime.datetime.now()
            print(now)
            dt=now.replace(hour=hour, minute=minute, second=0)
            print(dt)
            t=dt.timestamp()
            print(t)
            text = sd.askstring("Можешь затекстить","Напиши что-нибудь")
            label.config(text=f"Напоминание установлено на {hour:02}:{minute:02}\n {text}")
        except ValueError:
            mb.showerror("Упс","Неподходящий формат времени")
        except Exception as e:
            print(e)

def check():
    global t
    if t:
        now=time.time()
        if now >=t :
            play_snd(), remin()
            t=0
            #mb.showinfo("Пора!", f"{text}")
    window.after(10000,check)


def play_snd():
    global music
    music = True
    pygame.mixer.init()
    pygame.mixer.music.load("The Jumping Cats - Crocodile Goes For Porto.mp3")
    pygame.mixer.music.play()

def stop_music():
    global music
    if music:
        pygame.mixer.music.stop()
        music=False
    label.config(text="Установить новое напоминание")

def remin():
    global lbl
    root=Toplevel(window)
    root.title("Напоминание")
    root.geometry("1000x1000")
    lbl=Label(root, text=text, font=("Impact",50))
    lbl.pack(pady=100)

window=Tk()
window.title("Звуковая напоминалка")


label=Label(text="Установите напоминание", font=("Impact",30))
label.pack(pady=10)

set_but=Button(text="Установить", font=("Impact", 20), command=sety)
set_but.pack()

stop_but=Button(text="Стоп музыка", font=("Impact", 20), command=stop_music)
stop_but.pack(pady=10)

check()


window.mainloop()

