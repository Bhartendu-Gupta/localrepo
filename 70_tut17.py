from tkinter import *
import tkinter.messagebox as tmsg
root = Tk()
root.geometry("433x216")
root.title("Slider")

def getdollar():
    print(f"You have credited {myslider2.get()} dollar to your bank account")
    tmsg.showinfo("Amount Credited!",f"You have credited {myslider2.get()} dollar to your bank account")
        

# myslider1 = Scale(root, from_ = 0, to= 200)
# myslider1.pack()
Label(root, text="How many dollars do you want?").pack()
myslider2 = Scale(root, from_ = 0, to=200, orient=HORIZONTAL, tickinterval=60)
myslider2.set(9)
myslider2.pack()
Button(root, text="Get dollars!", pady=10, command=getdollar).pack()
root.mainloop()