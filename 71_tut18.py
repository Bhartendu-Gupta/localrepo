from tkinter import *
import tkinter.messagebox as tmsg
root = Tk()
root.geometry("433x216")
root.title("Radiobutton")

def order():
    tmsg.showinfo("order Recieved",f"We have received your order for {var.get()} Thanks for ordering")
        
#var= IntVar()
var=StringVar()
var.set("Radio")
#var.set(1)
Label(root,text="What would you like to have friends?",justify=LEFT,padx=14, font="lucida 19 bold" ).pack()
radio=Radiobutton(root,text="Paneer Dosa", padx=14, variable=var, value="paneer Dosa").pack(anchor="w")
radio=Radiobutton(root,text="Pizza", padx=14, variable=var, value="Pizza").pack(anchor="w")
radio=Radiobutton(root,text="Samosa", padx=14, variable=var, value="samosa").pack(anchor="w")
radio=Radiobutton(root,text="Paratha", padx=14, variable=var, value="Paratha").pack(anchor="w")
# ise for loop se bhi kr skte hai aur value ko aur textes ko list se retrive krana hai

Button(text="order now",command =order).pack()
root.mainloop()