# import the required libraries
from tkinter import *
def Deepak(event):
    print(f"You clicked on the button at {event.x}, {event.y}")
# create an instance of tkinter frame or window
root = Tk()
 
root.title("Events in Tkinter")

# set the size of the window
root.geometry("644x234")

# define a function to display a message
widget=Button(root, text='Click me please')
widget.pack()

# bind a mouse button event (widget ke saath bind krenge)
widget.bind('<Button-1> ', Deepak)  
widget.bind('<Double-1> ', quit)  

root.mainloop()