from tkinter import *
def add():
    global i
    lbx.insert(ACTIVE,f"{i}") 
    i+=1
i=0

root = Tk()
root.geometry("433x216")
root.title("Listbox Tutorial")

lbx= Listbox(root)
lbx.pack()
lbx.insert(END, "Fist item  of our listbox")

Button(root,text="Add Item", command=add).pack()
 
root.mainloop()