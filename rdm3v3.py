#!/usr/bin/env python
# -*- coding: utf-8 -*- 

from Tkinter import *
import random
import ttk

heroes = [
        { 'hero': 'Genji', 'portrait': 'assets/Genji_portrait.gif', 'pickable': True },
        { 'hero': 'McCree', 'portrait': 'assets/McCree_portrait.gif', 'pickable': True },
        { 'hero': 'Pharah', 'portrait': 'assets/Pharah_portrait.gif', 'pickable': True },
        { 'hero': 'Reaper', 'portrait': 'assets/Reaper_portrait.gif', 'pickable': True },
        { 'hero': 'Soldier76', 'portrait': 'assets/Soldier76_portrait.gif', 'pickable': True },
        { 'hero': 'Sombra', 'portrait': 'assets/Sombra_portrait.gif', 'pickable': True },
        { 'hero': 'Tracer', 'portrait': 'assets/Tracer_portrait.gif', 'pickable': True },
        { 'hero': 'Bastion', 'portrait': 'assets/Bastion_portrait.gif', 'pickable': True },
        { 'hero': 'Hanzo', 'portrait': 'assets/Hanzo_portrait.gif', 'pickable': True },
        { 'hero': 'Junkrat', 'portrait': 'assets/Junkrat_portrait.gif', 'pickable': True },
        { 'hero': 'Mei', 'portrait': 'assets/Mei_portrait.gif', 'pickable': True },
        { 'hero': 'Torbjorn', 'portrait': 'assets/Torbjörn_portrait.gif', 'pickable': True },
        { 'hero': 'Widowmaker', 'portrait': 'assets/Widowmaker_portrait.gif', 'pickable': True },
        { 'hero': 'D.va', 'portrait': 'assets/D.va_portrait.gif', 'pickable': True },
        { 'hero': 'Orisa', 'portrait': 'assets/Orisa_portrait.gif', 'pickable': True },
        { 'hero': 'Reinhardt', 'portrait': 'assets/Reinhardt_portrait.gif', 'pickable': True },
        { 'hero': 'Roadhog', 'portrait': 'assets/Roadhog_portrait.gif', 'pickable': True },
        { 'hero': 'Winston', 'portrait': 'assets/Winston_portrait.gif', 'pickable': True },
        { 'hero': 'Zarya', 'portrait': 'assets/Zarya_portrait.gif', 'pickable': True },
        { 'hero': 'Ana', 'portrait': 'assets/Ana_portrait.gif', 'pickable': True },
        { 'hero': 'Lucio', 'portrait': 'assets/Lúcio_portrait.gif', 'pickable': True },
        { 'hero': 'Mercy', 'portrait': 'assets/Mercy_portrait.gif', 'pickable': True },
        { 'hero': 'Symmetra', 'portrait': 'assets/Symmetra_portrait.gif', 'pickable': True },
        { 'hero': 'Zenyatta', 'portrait': 'assets/Zenyatta_portrait.gif', 'pickable': True }
    ]

def pickHero():
    global heroes
    pickedHero = random.choice(heroes)
    while (pickedHero['pickable'] != True):
        pickedHero = random.choice(heroes)
        
    return pickedHero

def renderPlaceholders():
    x_coord = 0
    y_coord = 0
    for num in range(0,3):
        photo=PhotoImage(file='assets/Empty_portrait.gif')
        l = Label(master, image=photo)
        l.image = photo
        l.place(x=x_coord, y=y_coord)
        x_coord += 184

def renderHeroes():
    alreadyPicked = []
    x_coord = 0
    y_coord = 0
    for num in range(0,3):
        pickedHero = pickHero()
        while (pickedHero in alreadyPicked):
            pickedHero = pickHero()
        photo=PhotoImage(file=pickedHero['portrait'])
        l = Label(master, image=photo)
        l.image = photo
        l.place(x=x_coord, y=y_coord)
        alreadyPicked.append(pickedHero)
        x_coord += 184

def renderOptions():
    global heroes
    index = 1
    width = 0
    height = 30
    v_diff = 120
    h_diff = 30
        
    optionsWindow = Tk()
    optionsWindow.title("Options")
    optionsWindow.geometry('{}x{}'.format(445, 260))
    optionsWindow.resizable(width=False, height=False)
    
    Label(optionsWindow, text='Attack', font = "Helvetica 14 bold underline").place(x=(width+0*v_diff), y=0)
    Label(optionsWindow, text='Defense', font = "Helvetica 14 bold underline").place(x=(width+1*v_diff), y=0)
    Label(optionsWindow, text='Tank', font = "Helvetica 14 bold underline").place(x=(width+2*v_diff), y=0)
    Label(optionsWindow, text='Support', font = "Helvetica 14 bold underline").place(x=(width+3*v_diff), y=0)
    Button(optionsWindow, text='Select all', command= lambda: selectAll(optionsWindow, True)).place(x=265, y=230)
    Button(optionsWindow, text='Unselect all', command= lambda: selectAll(optionsWindow, False)).place(x=325, y=230)
    Button(optionsWindow, text='Save', command= lambda: saveOptions(optionsWindow)).place(x=400, y=230)
    
    for hero in heroes:
        chk = ttk.Checkbutton(optionsWindow, text=hero['hero'])
        chk.state(['!alternate'])

        if (hero['pickable'] == True):
            chk.state(['selected'])
        
        chk.place(x=width, y=height)
        height += h_diff
        if (index == 7 or index == 13 or index == 19):
            width += v_diff
            height = h_diff
        index += 1

def saveOptions(window):
    for child in window.winfo_children():
        if child.winfo_class() == 'TCheckbutton':
            if child.instate(['selected']) :
                setPickable(child.cget('text'), True)
            else:
                setPickable(child.cget('text'), False)
    window.destroy()

def setPickable(heroName, pickable):
    global heroes
    for hero in heroes:
        if (hero['hero'] == heroName):
            hero['pickable'] = pickable

def selectAll(window, selected):
    for child in window.winfo_children():
        if child.winfo_class() == 'TCheckbutton':
            if selected == True:
                child.state(['selected'])
            else:
                child.state(['!selected'])
    
window_width = 556
window_height = 250
master = Tk()

renderPlaceholders()
Button(master, text='Generate comp', command= lambda: renderHeroes(), width=16).place(x=((window_width/2)-60), y=(window_height-30))

menubar = Menu(master)
menubar.add_command(label="Options", command= lambda: renderOptions())

master.config(menu=menubar)
master.title('3v3 comp generator')
master.geometry('{}x{}'.format(window_width, window_height))
master.resizable(width=False, height=False)
master.mainloop()
