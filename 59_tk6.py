from tkinter import *
root=Tk()
root.geometry("744x234")
root.title("my gui with Deepak")
#important label option
# text- add the text
# bg- background
# fg- foreground
# 1.font = "comicsansms 19 bold"
# 2.font=("comicsansms", 19, "bold")
# font- sets the font
# padx- x padding
# pady- y padding
# relief-border styling- SUNKEN,RAISED,GROOVE,RIDGE
title_label= Label(text='''
\nKalam was elected as the 11th president of India in 2002 with the
\nsupport of both the ruling Bharatiya Janata Party and the then-opposition Indian National Congress.
\nWidely referred to as the "People's President", he returned to his civilian life of education,   
\nwriting and public service after a single term. He was a recipient of several prestigious awards,
\nincluding the Bharat Ratna, India's highest civilian honour.''', bg ="black", fg= "yellow", padx=13,
pady=94, font="comicsansms 19 bold", borderwidth=3, relief=SUNKEN)

#IMPORTANT PACK OPTIONS
# anchor=nw(north,west),ne(north,east)etc.
# side= top,bottom,left,right
# fill
# padx 
# pady
title_label.pack(side=BOTTOM,anchor = "nw",fill=X)
#title_label.pack(side=LEFT,fill=Y,padx=34,pady=34)



root.mainloop()
                                                                                             
 