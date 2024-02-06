# PROJECT: CRYPTOWHISPER: Secret Messaging

# Topic: Cryptography
# About: This project is all about encrypting and descrypting of hidden/secret messages.
# Functionality:  The users can send personal messages and information with privacy. 

from tkinter import*
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

window.overrideredirect(1)

screen = ttk.Style()
screen.theme_use('clam')
screen.configure("red.Horizontal.TProgressbar", foreground='red', background='red')
progress=Progressbar(window,style="red.Horizontal.TProgressbar",orient=HORIZONTAL,length=500,mode='determinate',)
progress.place(x=-10,y=235)

# Progress Bar 
def bar():
    loading_text = Label(window,text='Loading...', fg='white', bg="#17204d")
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

# Screen Frame 
Frame(window,width=427,height=241,bg="#17204d").place(x=0,y=0)  
screen_button = Button(window, text="Get Started", command=bar)
screen_button.config(width=10, height=1, border=0, fg='black', bg='white')
screen_button.place(x=170,y=200)

# Screen Labels 

first_label=Label(window,text='CRYPTO',fg='white',bg="#17204d")
first_label_format=('Calibri (Body)',18,'bold')
first_label.config(font=first_label_format)
first_label.place(x=50,y=80)

second_label=Label(window,text='WHISPER',fg='white',bg="#17204d")
second_label_format=('Calibri (Body)',18,'bold')
second_label.config(font=second_label_format)
second_label.place(x=155,y=82)

third_label=Label(window,text='Secret Messaging',fg='white',bg="#17204d")
third_label_format=('Calibri (Body)',13)
third_label.config(font=third_label_format)
third_label.place(x=50,y=110)

window.mainloop()



