#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 08:11:57 2020

@author: amaury
"""

from tkinter import Tk, Label, StringVar, Entry, Button, Canvas, PhotoImage, Frame

fenetre=Tk()
fenetre.title('Space Invaders')

canevas = Canvas(fenetre, bg='white', height=300, width=320)
canevas.pack(side='top')

photo=PhotoImage(file="image/Yavin_4.png")
image_pendu = Label(canevas, image=photo, border=0)
image_pendu.pack()

Proposition= StringVar()
Champ=Entry(fenetre, textvariable = Proposition, bg='light sky blue')
Champ.pack(side='bottom',padx=5,pady=5)

MotEnCour=Label(fenetre, text='hello')
MotEnCour.pack(side='left',padx=10,pady=10)
VotreLettre=Label(fenetre, text="Proposez une lettre :")
VotreLettre.pack(side='left',padx=5,pady=5)

boutonVal=Button(fenetre, text ='Valider')
boutonVal.pack(side='bottom', padx=5, pady=5)

boutonQuit=Button(fenetre, text ='Abandonner', command=fenetre.destroy)
boutonQuit.pack(side='right', padx=5, pady=5)


fenetre.mainloop()
fenetre.destroy()