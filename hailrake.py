import winsound
import multiprocessing
import tkinter as tk
from tkinter import *
from winsound import *
from threading import Thread
import tkinter.messagebox
import os
import pygame
import threading


root = Tk()

root.title('ПАПИЧСАУНД')
root['bg']='white'
root.wm_attributes('-alpha', 0.8)
root.geometry('600x800')

def scroll():
    up = True
    down = True

scrollbar = Scrollbar(root, command = scroll)
scrollbar.pack(side = RIGHT, fill = Y)

play = lambda: PlaySound('0iq.wav', SND_FILENAME)
button = Button(root, width=20, height=3, text="НОЛЬ ИНТЕЛЛЕКТА", command = play)

#TODO:Доработать паузу

pause = multiprocessing.Process(target=PlaySound, args=('0iq.wav',))
lambda:start()
input("Нажмите ENTER")
lambda:stop()

#TODO:Доработать паузу

def stop():
    lambda:stop()

paused = FALSE

def pause():
    global paused
    paused = TRUE
    lambda:pygame.cdrom.pause()

button.pack()

#TODO: НАСТРОИТЬ КНОПКИ

playPic = PhotoImage(file='playbutton.png')
playButton = Button(root, image=playPic, command = play)
playButton.pack(side=RIGHT)

stopPic = PhotoImage(file='stopButton.png')
stopButton = Button(root, image=stopPic, command = stop)
stopButton.pack()

pausePic = PhotoImage(file='pausebutton.png')
pauseButton = Button(root, image=pausePic, command = pause)
pauseButton.pack()

#TODO: НАСТРОИТЬ КНОПКИ

play = lambda: PlaySound('sound/soso.wav', SND_FILENAME)
button = Button(root, text = 'ЛЕЖАТЬ ПЛЮС СОСАТЬ', width=20, height=3, command = play)
button.pack(side=LEFT, pady=20)

play = lambda: PlaySound('ebat.wav', SND_FILENAME)
button = Button(root, text = 'ЕБАТЬ Я ТУПОЙ', width=20, height=3, command = play)
button.pack(side=LEFT, padx=10)

play = lambda: PlaySound('air.wav', SND_FILENAME)
button = Button(root, text = 'НАЙС ДЫХАНИЕ', width=20, height=3, command = play)
button.pack(side=LEFT, padx=30)

play = lambda: PlaySound('meow.wav', SND_FILENAME)
button = Button(root, text = 'ПАПИЧ МЯУКАЕТ', width=20, height=3, command = play)
button.pack(side=LEFT)

play = lambda: PlaySound('rage.wav', SND_FILENAME)
button = Button(root, text = 'РЕЙДЖ', width=20, height=3, command = play)
button.pack(side=LEFT)

play = lambda: PlaySound('easy.wav', SND_FILENAME)
button = Button(root, text = 'ЛЕГЧАЙШАЯ', width=20, height=3, command = play)
button.pack(side=LEFT)

play = lambda: PlaySound('nahui.wav', SND_FILENAME)
button = Button(root, text = 'ИДИ НАХУЙ ОТСЮДА', width=20, height=3, command = play)
button.pack(side=LEFT)

play = lambda: PlaySound('easter.wav', SND_FILENAME)
button = Button(root, text = 'ПАСХАЛ ОЧКА', width=20, height=3, command = play)
button.pack()

play = lambda: PlaySound('how.wav', SND_FILENAME)
button = Button(root, text = 'КАК БЛЯТЬ', width=20, height=3, command = play)
button.pack()

play = lambda: PlaySound('once.wav', SND_FILENAME)
button = Button(root, text = 'ОДНАЖДЫ ПАПИЧ', width=20, height=3, command = play)
button.pack()

play = lambda: PlaySound('umnich.wav', SND_FILENAME)
button = Button(root, text = 'Я УМНЫЙ', width=20, height=3, command = play)
button.pack()

play = lambda: PlaySound('pocket.wav', SND_FILENAME)
button = Button(root, text = 'А ЧТО У НАС В КАРМАНАХ', width=20, height=3, command = play)
button.pack()

play = lambda: PlaySound('nahui.wav', SND_FILENAME)
button = Button(root, text = 'ИДИ НАХУЙ ОТСЮДА', width=20, height=3, command = play)
button.pack()

play = lambda: PlaySound('bipolar.wav', SND_FILENAME)
button = Button(root, text = 'БИПОЛЯР ОЧКА', width=20, height=3, command = play)
button.pack()

play = lambda: PlaySound('agree.wav', SND_FILENAME)
button = Button(root, text = 'ТУТ СЫГЛЫ', width=20, height=3, command = play)
button.pack()

button.pack()
root.mainloop()

winsound.PlaySound("hailrake.wav", winsound.SND_ASYNC)
delay = input("ПАПИЧ ПЕРЕДАЕТ ПОКА")
