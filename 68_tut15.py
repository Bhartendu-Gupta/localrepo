from tkinter import *
root = Tk()
root.geometry("733x566")
root.title("vs code")

def myfunc():
    print("mai ek bahut hi smart func hoon")

# use these to create a non dropdown menu
# mymenu = Menu(root)
# mymenu.add_command(label="file", command= myfunc)
# mymenu.add_command(label="Exit", command=quit)
# root.config(menu=mymenu)

mainmenubar = Menu(root)

m1= Menu(mainmenubar, tearoff=0) # file me se horizontal(dotted lines----) line ko hatane ke liye tearoff ka use krte hai
m1.add_command(label="New project", command = myfunc)
m1.add_command(label="Save", command = myfunc)
m1.add_separator()
m1.add_command(label="Save as", command = myfunc)
m1.add_command(label="Print", command = myfunc)
root.config(menu=mainmenubar)
mainmenubar.add_cascade(label="file", menu=m1)

m2= Menu(mainmenubar, tearoff=0) 
m2.add_command(label="Cut", command = myfunc)
m2.add_command(label="Copy", command = myfunc)
m2.add_separator()
m2.add_command(label="Paste", command = myfunc)
m2.add_command(label="Find", command = myfunc)
root.config(menu=mainmenubar)
mainmenubar.add_cascade(label="Edit", menu=m2)


root.mainloop()