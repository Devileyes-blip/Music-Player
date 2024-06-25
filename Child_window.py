'''
from tkinter import Toplevel,Button

def xyz():
    1+2


def open_window(parent):
    child = Toplevel(parent)
    child.title("CHutiyye ")
    pause_btn = Button(child,text = 'Pause')
    pause_btn.pack(pady=50)
'''
import tkinter as tk
from tkinter import Toplevel, Button

def xyz():
    print("Pause button clicked")  # Placeholder for actual functionality

def open_window(parent):
    child = Toplevel(parent)
    child.title("Child Window")
    pause_btn = Button(child, text='Pause', command=xyz)
    pause_btn.pack(pady=20, padx=50)  # Adjust padding as needed
    child.mainloop()
    # Create a button inside the child window
    

