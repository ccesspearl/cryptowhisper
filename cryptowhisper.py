# PROJECT: CRYPTOWHISPER: Secret Messaging

# Topic: Cryptography
# About: This project is all about encrypting and descrypting of hidden/secret messages.
# Functionality:  The users can send personal messages and information with privacy. 

from tkinter.ttk import Progressbar
from tkinter import*

# Window for Screen Splash 
window=Tk()
window_width = 427
window_height = 250
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x_coordinate = (screen_width/2)-(window_width/2)
y_coordinate = (screen_height/2)-(window_height/2)
window.geometry("%dx%d+%d+%d" %(window_width,window_height,x_coordinate,y_coordinate))


window.mainloop()
