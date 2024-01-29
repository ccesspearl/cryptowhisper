# PROJECT: CRYPTOWHISPER: Secret Messaging

# Topic: Cryptography
# About: This project is all about encrypting and descrypting of hidden/secret messages.
# Functionality:  The users can send personal messages and information with privacy. 

from tkinter import*
from PIL import ImageTk, Image
from tkinter import messagebox
from tkinter.ttk import Progressbar
from tkinter import Tk, ttk
import base64
import os

# Window for Splash Screen 
window=Tk()
window_width = 427
window_height = 250
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x_coordinate = (screen_width/2)-(window_width/2)
y_coordinate = (screen_height/2)-(window_height/2)
window.geometry("%dx%d+%d+%d" %(window_width,window_height,x_coordinate,y_coordinate))

def bar():

    loading_text = Label(window,text='Loading...', fg='white', bg="#249794")
    loading_format = ('Calibri (Body)',10)
    loading_text.config(font = loading_format)
    loading_text.place(x = 18, y = 210)
    
    import time
    num = 0
    for i in range(100):
        progress['value'] = num
        window.update_idletasks()
        time.sleep(0.03)
        num = num + 1
    
    window.destroy()

window.mainloop()
