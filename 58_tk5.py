from tkinter import *
from PIL import Image, ImageTk
ashish_root=Tk()
ashish_root.geometry("1000x700")
#photo=PhotoImage(file="2.png")
#for jpg images
image=Image.open("photo.jpg")
photo=ImageTk.PhotoImage(image)
mohit_label=Label(image=photo)
mohit_label.pack()
ashish_root.mainloop()
