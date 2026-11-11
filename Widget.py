from tkinter import *
from datetime import date

root = Tk()

root.title('Getting started with widgets')
root.geometry('400x300')

l = Label(text='Hey there !',fg='white', bg="#E33A0C",height= 1,width=300)

name_l = Label(text='Full name',bg="#514FBF")
name_en = Entry()

def display():
    name = name_en.get()
    global message
    message = "Welcome to the Appplication\n today's date is: "
    greet = "Hello "+name+"\n"
    text_box.insert(END, greet)
    text_box.insert(END, message)
    text_box.insert(END,date.today())

text_box = Text(height=3)

btn = Button(text='Begin',command=display,height=1, bg="#7AE0C7",fg= 'black')

l.pack()
name_l.pack()
name_en.pack()
btn.pack()
text_box.pack()

root.mainloop()