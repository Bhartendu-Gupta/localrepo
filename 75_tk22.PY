#exit() code ko run na krane ke liye exit() ka use krte hai
from tkinter import*

def update():
    print("Updating the gui")
    root.geometry(f"{width.get()}x{height.get()}")
root=Tk()
root.geometry("344x233")

width=StringVar()
height=StringVar()
Entry(root, textvariable=width).pack()
Entry(root, textvariable=height).pack()
Button(root, text="Apply", command=update).pack()
root.mainloop()

