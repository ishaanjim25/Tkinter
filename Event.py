from tkinter import *

window = Tk()
window.title("Event Handler")
window.geometry("100x100")

def handle_keypress(event):
    """Print the character assosciated to the keypressed"""
    print(event.char)

window.bind("<Key>", handle_keypress)
print(handle_keypress.__doc__)

def handle_click(event):
    print("\nThe button was clicked !")

button = Button(text= "Click me!")

button.bind("<Button-1> " , handle_click)
button.pack()

window.mainloop()