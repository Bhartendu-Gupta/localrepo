
from tkinter import*
def upload():
    statusvar.set("Busy...")
    sbar.update()
    import time
    time.sleep(2)
    statusvar.set("Ready")

root=Tk()
root.geometry("433x234")
root.title("status bar")

statusvar=StringVar()
statusvar.set("Ready")
sbar=Label(root, textvariable=statusvar, relief=SUNKEN, anchor="w")
sbar.pack(side=BOTTOM, fill=X)

Button (root, text="Upload", command=upload).pack()
root.mainloop()

