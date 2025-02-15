from tkinter import *
root=Tk()
root.geometry("655x333")
def hello():
    print("Hello tkinter Buttons")
def name():
    print("my name is bhartendu")
def nickname():
    print("my nick name is deepak")  
frame=Frame(root,borderwidth=6,bg="gray",relief=SUNKEN)
frame.pack(side=LEFT,anchor="nw")
b1=Button(frame, fg="red", text="Print now",command=hello)
b1.pack(side=LEFT,padx=22)
b2=Button(frame, fg="red", text="Tell me name now",command=name)
b2.pack(side=LEFT,padx=22)
b3=Button(frame, fg="red", text="tell me nick name",command=nickname)
b3.pack(side=LEFT,padx=22)
b4=Button(frame, fg="red", text="Print now")
b4.pack(side=LEFT,padx=22)
root.mainloop()
