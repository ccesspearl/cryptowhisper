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

# Progressing Bar
screen = ttk.Style()
screen.theme_use('clam')
screen.configure("red.Horizontal.TProgressbar", foreground='red', background='red')
progress=Progressbar(window,style="red.Horizontal.TProgressbar",orient=HORIZONTAL,length=500,mode='determinate',)
progress.place(x=-10,y=235)

# Decrypt Function 
def decrypt():
    password=code.get()

    if password=="1234":
        new_screen2=Toplevel(main_window)
        new_screen2.title("Decrypted Message")
        new_screen2.geometry("400x200")
        new_screen2.configure(bg="#00bd56")

        user_message=user_text1.get(1.0,END)
        decode_message=user_message.encode("ascii")
        base64_bytes=base64.b64decode(decode_message)
        decrypt=base64_bytes.decode("ascii")

        Label(new_screen2,text="Decode the mystery! Unveil the secret! 🔓", font=("Calibri", 13, "bold"),fg="white",bg="#00bd56").place(x=10,y=5)
        text2=Text(new_screen2,font="Rpbote 10", bg="white", relief=GROOVE, wrap=WORD, bd=0)
        text2.place(x=10, y=40,width=380,height=150)

        text2.insert(END,decrypt)

    elif password=="":
        messagebox.showerror("Decryption", "Input Password")

    elif password !="1234":
        messagebox.showerror("Decryption", "Invalid Password")


# Enrypt Function 
def encrypt():
    password=code.get()

    if password=="1234":
        new_screen1=Toplevel(main_window)
        new_screen1.title("Encrypted Message")
        new_screen1.geometry("400x200")
        new_screen1.configure(bg="#ed3833")

        user_message=user_text1.get(1.0,END)
        encode_message=user_message.encode("ascii")
        base64_bytes=base64.b64encode(encode_message)
        encrypt=base64_bytes.decode("ascii")

        Label(new_screen1,text="Encrypt a secret message for some mystery fun! 🔒", font=("Calibri", 13, "bold"),fg="white",bg="#ed3833").place(x=10,y=5)
        text2=Text(new_screen1,font="Rpbote 10", bg="white", relief=GROOVE, wrap=WORD, bd=0)
        text2.place(x=10, y=40,width=380,height=150)

        text2.insert(END,encrypt)

    elif password=="":
        messagebox.showerror("Encryption", "Input Password")

    elif password !="1234":
        messagebox.showerror("Encryption", "Invalid Password")

# Main Window for the Cryptography Project 
def main_screen():

    global main_window
    global code 
    global user_text1

    main_window = Tk()
    main_window.geometry("375x398")
    main_window.title("Secret Message")
    main_window.resizable(False,False)
    main_window.configure(bg="#ffcf2f")

    # Reset User Words 
    def reset():
        code.set("")
        user_text1.delete(1.0, END)

    # First Text Label in the Main Window 
    Label(text="Type text for encryption and descryption", bg= "#ffcf2f", fg="black", font=("calibri",13, "bold")).place(x=10,y=10)
    user_text1=Text(font="Robote 20", bg="white", relief=GROOVE, wrap=WORD, bd=0)
    user_text1.place(x=10,y=50,width=355,height=100)

    # Second Text Label  in the Main Window 
    Label(text="Type secret key for encrytion and descryption", bg= "#ffcf2f", fg="black", font=("calibri", 13, "bold")).place(x=10,y=170)
    code=StringVar()
    Entry(textvariable=code,width=19,bd=0,font=("arial",25),show="*").place(x=10,y=200)

    # Buttons in the Main Window 
    Button(text="ENCRYPT", font=("calibri",10, "bold"),height="2", width=24, bg="#B43A17", fg="white",bd=0, command=encrypt).place(x=10,y=255)
    Button(text="DECRYPT", font=("calibri",10, "bold"), height="2", width=24, bg="#208F28", fg="white", bd=0, command=decrypt).place(x=190,y=255)
    Button(text="RESET", font=("calibri",10, "bold"),height="2", width=50,bg="#1089ff", fg="white", bd=0, command=reset).place(x=10,y=300)
        
    main_window.mainloop()  


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
    main_screen()

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