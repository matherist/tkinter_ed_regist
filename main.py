import tkinter as tk
from tkinter import *
import settings
from tkinter import messagebox
import base

win = tk.Tk()

win.title('Mini-Class-Project')
win.geometry(f'{settings.WIDTH}x{settings.HEIGHT}+10+10')


w = Label(win, text="Hello, welcome to registration form!", font = "120", fg='blue')
w.pack()

# add an orange frame
frame1 = tk.Frame(master=win, width=settings.WIDTH/3, height=settings.HEIGHT/3, bg="orange")
frame1.pack()
username = Label(frame1, text = "Username").place(x = 22,y = 50) 

email = Label(frame1, text = "Email").place(x = 22, y = 90)

password = Label(frame1, text = "Password").place(x = 22, y = 130)

def click():
    name = (usname.get())  
    passw = (uspassw.get()) 
    if str(name) == base.info['username'] and str(passw) == base.info['password']:
        messagebox.showinfo('Welcome!')
    else:
        messagebox.showwarning('Try again!')


usname = tk.StringVar()  
usemail = tk.StringVar()
uspassw = tk.StringVar()
e1 = Entry(frame1, textvariable=usname).place(x = 81, y = 50)  
e2 = Entry(frame1, textvariable=usemail).place(x = 57.5, y = 90)  
e3 = Entry(frame1, textvariable=uspassw).place(x = 77.5, y = 130)
frame1.pack()

submitbutton = Button(frame1, text = "Submit",activebackground = "red", activeforeground = "blue", command=click).place(x = 22, y = 170)  

f = Label(win, text="Try this for success: \n\n username: Dinaiym \n password: 12345 \n email: {any}", font = "120", fg='green')
f.pack()
win.mainloop()
