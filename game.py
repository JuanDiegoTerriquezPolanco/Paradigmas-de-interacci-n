from fileinput import close
import turtle
import voice_handler
import tkinter as tk
from tkinter import ttk
from tkinter import *

def mouse():
    wn = turtle.Screen()
    turtle.shape('turtle')
    wn.bgcolor('lightgreen')
    turtle.up()
    voice_handler.speak('Haz clic en la pantalla para comenzar la interacción')
  
    def fxn(x, y): 
        turtle.goto(x, y) 
    
    wn.onclick(fxn) 
    wn.mainloop()

def voice():
    screen = turtle.Screen()

    t = turtle.Turtle()
    t.shape('turtle')
    screen.bgcolor('lightgreen')
    t.up()
    voice_handler.speak('Da órdenes o dí ALTO para finalizar')

    while True:
        voice_handler.speak('¿Hacia dónde quieres moverte?')
        command = voice_handler.get_audio()
        print(command)

        if 'alto' in command:
            break
        
        else:
            if 'izquierda' in command:
                voice_handler.speak('Moviendome a la izquierda')
                print('Moviendome a la izquierda')
                t.left(180)
                t.forward(250)
                t.left(180)
            if 'derecha' in command:
                voice_handler.speak('Moviendome a la derecha')
                print('Moviendome derecha')
                t.forward(250)
            if 'arriba' in command:
                voice_handler.speak('Moviendome arriba')
                print('Moviendome arriba')
                t.left(90)
                t.forward(250)
                t.right(90)
            if 'abajo' in command:
                voice_handler.speak('Moviendome abajo')
                print('Moviendome abajo')
                t.right(90)
                t.forward(250)
                t.left(90)

    screen.mainloop()

frame = tk.Tk()
frame.config(width=300, height=100)
frame.title("Elige tu interfaz")
label = Label(frame,text="Elige tu forma de interacción:")
label.place(x=75, y=10)
btnMouse = ttk.Button(text="Mouse",command=mouse)
btnVoice = ttk.Button(text="Voz",command=voice)
btnMouse.place(x=50, y=50)
btnVoice.place(x=200, y=50)
voice_handler.speak('Elige tu forma de interacción:')
frame.mainloop()