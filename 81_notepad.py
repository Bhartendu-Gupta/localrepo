from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os
def newFile():
    global file
    root.title("Untitled - Notepad")
    file=None
    TextArea.delete(1.0,END)

def openFile():
    global file
    file=askopenfilename(defaultextension=".txt",filetypes=[("All files","*.*"), ("Text Documents","*.txt")])
    if file == "":
        file = None
    else:
         root.title(os.path.basename(file)+"-Notepad")
         TextArea.delete(1.0,END)
         f=open(file,"r")
         TextArea.insert(1.0,f.read())
         f.close()

def saveFile():
    global file
    if file==None:
         file=asksaveasfilename(initialfile='Untitled.txt',defaultextension=".txt",filetypes=[("All files","*.*"),
         ("Text Documents","*.txt")])

         if file=="":
              file=None
         else:
              # save as a file
              f= open(file,"w")
              f.write(TextArea.get(1.0,END))
              f.close()
              root.title(os.path.basename(file)+"-Notepad")
              print("File Saved")
    else:
         # save the file
              f= open(file,"w")
              f.write(TextArea.get(1.0,END))
              f.close()

def quitApp():
    root.destroy()


def cut():
    TextArea.event_generate(("<<Cut>>"))

def copy():
       TextArea.event_generate(("<<Copy>>"))

def paste():
       TextArea.event_generate(("<<Paste>>"))


def about():
    showinfo("Notepad", "Notepad by Deepak" )


if__name__='__main__:'
    # basic tkinter setup 
     
root=Tk()
root.title('notpad')
root.wm_iconbitmap("1_ico.png")
root.geometry("644x788")       
   
# Add textarea
TextArea = Text(root, font="lucida 13 bold")
file=None
TextArea.pack(expand=True, fill=BOTH)

# lets create a menubar
MenuBar=Menu(root)
FileMenu=Menu(MenuBar, tearoff=0)

# to open New file
FileMenu.add_command(label="New", command=newFile)

# to open already existing file
FileMenu.add_command(label="open", command=openFile)

# to save  the current file
FileMenu.add_command(label="save", command=saveFile)
FileMenu.add_separator()
FileMenu.add_command(label="Exit", command=quitApp)
MenuBar.add_cascade(label="file", menu=FileMenu)
# Filemenu ends

# Editmenu starts
EditMenu = Menu(MenuBar, tearoff=0)
# To give a fiture of cut, copy, paste
EditMenu.add_command(label="cut", command=cut)
EditMenu.add_command(label="copy", command=copy)
EditMenu.add_command(label="paste", command=paste)

MenuBar.add_cascade(label="Edit",menu=EditMenu)
# editmenu Ends


#Helpmenu starts
HelpMenu=Menu(MenuBar,tearoff=0)
HelpMenu.add_command(label="About Notepad", command=about)
MenuBar.add_cascade(label="Help", menu=HelpMenu)
#Helpmenu ends
root.config(menu=MenuBar)

# Adding scrollbar using rules from Tkinter lecture no 22
Scroll=Scrollbar(TextArea)
Scroll.pack(side=RIGHT, fill=Y)
Scroll.config(command=TextArea.yview)
TextArea.config(yscrollcommand=Scroll.set)
root.mainloop()


