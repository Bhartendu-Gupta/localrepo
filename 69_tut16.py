from tkinter import *
import tkinter.messagebox as tmsg 
root = Tk()
root.geometry("733x566")
root.title("vs code")

def myfunc():
    print("mai ek bahut hi smart func hoon")

def help():
    print("I will help you")
    tmsg.showinfo("Help", "Deepak will help you with this gui")

def rate():
    print("Rate us")
    value=tmsg.askquestion("Was your experience good?"," you used this gui... Was your experience good?")
    if value=="yes":
        msg="Great.Rate us on appstore please"
    else:
        msg="Tell us what went wrong. We will call you soon"
    tmsg.showinfo("Experience", msg)

def diya():
        ans= tmsg.askretrycancel("diya se dosti kr lo ", "sorry diya nhi banegi aapki dost" )
        if ans:
            print("retry krne pe bhi kuch nhi hoga")
        else:
            print("bhut badhiya bhai cancel kr diye nhi to pitte")
                  

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

m3= Menu(mainmenubar, tearoff=0)
m3.add_command(label="Help",command=help )
m3.add_command(label="Rate us",command=rate )
m3.add_command(label="Befriend Diya",command= diya)
mainmenubar.add_cascade(label="Help", menu=m3)
root.config(menu=mainmenubar)

root.mainloop()