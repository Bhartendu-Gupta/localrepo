from tkinter import *
root=Tk()
def getvals():
    print("It works!")
root.geometry("655x333")
# Heading
Label(root, text="Welcome to Bhartendu Travels", font="comicsansms 13 bold", pady=20, padx=15).grid(row=0,column=3)

# Text for our form
name=Label(root,text="Name")
phone=Label(root,text="Gender")
gender=Label(root,text="Phone")
emergency=Label(root,text="Emergency contact")
paymentmode=Label(root,text="Payment mode")

# Pack text for our form
name.grid(row=1 ,column=2)
phone.grid(row=2 ,column=2)
gender.grid(row=3 ,column=2)
emergency.grid(row=4 ,column=2)
paymentmode.grid(row=5 ,column=2)

# Tkinter variable for storing entries
namevalue=StringVar()
phonevalue=StringVar()
gendervalue=StringVar()
emergencyvalue=StringVar()
paymentmodevalue=StringVar()
foodservicevalue=IntVar() #ye checkbox hoga(ye 0 ya phir 1 hoga)

# Enteries for our form
nameentry=Entry(root,textvariable=namevalue)
phoneentry=Entry(root,textvariable=phonevalue)
genderentry=Entry(root,textvariable=gendervalue)
emergencyentry=Entry(root,textvariable=emergencyvalue)
paymentmodeentry=Entry(root,textvariable=paymentmodevalue)

# Packing the enteries
nameentry.grid(row=1, column=3)
phoneentry.grid(row=2, column=3)
genderentry.grid(row=3, column=3)
emergencyentry.grid(row=4, column=3)
paymentmodeentry.grid(row=5, column=3)

# Checkbox & Packing it
foodservice= Checkbutton(text="Want to prebook your meals?", variable = foodservicevalue)
foodservice.grid(row=6,column=3)

# Button & packing it and assigning it a command
Button(text="Submit to Bhartendu Travels", command=getvals).grid(row=7, column=3)


root.mainloop()
