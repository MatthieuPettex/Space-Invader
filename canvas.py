#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 08:11:57 2020

@author: amaury et matthieu
"""
#---------fenetre tkinter-------------------
from tkinter import Tk, Label, StringVar, Entry, Button, Canvas, PhotoImage, Frame

fenetre=Tk()
fenetre.title('Space Invaders')
fenetre.geometry("1500x700")

canevas = Canvas(fenetre, bg='white', height=800, width=800)
canevas.pack(side='left')
#---------background--------------
photo=PhotoImage(file="image/Yavin_4.png")
image_space = Label(canevas, image=photo, border=0)
image_space.pack()

#--------bouton------------------
boutonPlay=Button(fenetre, text ='New Game')
boutonPlay.pack(side='top', padx=5, pady=5)

boutonQuit=Button(fenetre, text ='Abandonner', command=fenetre.destroy)
boutonQuit.pack(side='top', padx=5, pady=5)

fenetre.mainloop()
fenetre.destroy()