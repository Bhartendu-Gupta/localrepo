from tkinter import *
root= Tk()
root.geometry("655x444")
root.title("Deepak- Title of my Gui")
root.wm_iconbitmap("1_ico.png")
root.configure(bg="yellow")   #bg means background

width = root.winfo_screenwidth()
height= root.winfo_screenheight()
print(f"{width}x{height}")


Button(text="close", command = "root.destroy").pack()

root.mainloop()