#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 08:11:57 2020

@author: amaury et matthieu
"""
largeur=1350
hauteur=700

def deplacer():
    global x0, y0, dx
    x0=x0+dx
    canevas.coords(ennemie,x0,y0,x0+30,y0+30)
    
    if x0<0 or x0>largeur:
        dx=-dx
    canevas.after(20,deplacer)
    return

def left(event):
    x=-20
    y=0
    canevas.move(playeur, x, y)
    return
    
def right(event):
    x=20
    y=0
    canevas.move(playeur, x, y)
    return

def tirer():
    global x1, y1, dy, lazer
    y1=y1-dy
    canevas.coords(lazer,x1+14,y1,x1+16,y1+16)
    
    canevas.after(10,tirer)
    return

def startTirer(event):
    lazer=canevas.create_rectangle(x1+14,y1,x1+16,y1+16,width=2,outline="green")
    tirer()
    return
#---------fenetre tkinter-------------------
from tkinter import Tk, Button, Canvas, PhotoImage, Label

fenetre=Tk()
fenetre.title('Space Invaders')
fenetre.geometry("1350x700")

canevas = Canvas(fenetre, bg='white', height=hauteur, width=largeur)
canevas.pack(fill="both", expand=True)

#---------background--------------
#photo=PhotoImage(file="image/Yavin_4.png")
#image_space = Label(canevas, image=photo)
#image_space.place(x=0,y=0,relwidth=1,relheight=1)

#---------objet-------------------
x0,y0=660,50
dx=+5
dy=+5
ennemie=canevas.create_rectangle(x0,y0,x0+30,y0+30,width=2,fill="red")
x1,y1=660,550
playeur=canevas.create_rectangle(x1,y1,x1+30,y1+30,width=2,fill="red")
#--------touche bind-------------
fenetre.bind("<Left>",left)
fenetre.bind("<Right>",right)
fenetre.bind("<Up>",startTirer)
#--------bouton------------------
boutonQuit=Button(canevas, text ='Quitter', command=fenetre.quit)
boutonQuit.pack(side="bottom",padx=5, pady=5)

boutonPlay=Button(canevas, text ='New Game', command=deplacer)
boutonPlay.pack(side="bottom",padx=5, pady=5)

fenetre.mainloop()
fenetre.destroy()