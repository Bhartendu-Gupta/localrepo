from tkinter import *
root=Tk()

Canvas_width = 800
Canvas_height = 400

root.geometry(f"{Canvas_width}x{Canvas_height}")
root.title("Deepak 's Gui")
Can_widget = Canvas(root, width=Canvas_width, height=Canvas_height)
Can_widget.pack()

# The line goes from the point x1,y1 to x2,y2
Can_widget.create_line(0,0,800,400, fill="green")
Can_widget.create_line(0,400,800,0, fill="blue")

# To create a rectangle specify parameters- in this order- coordinate of top left & coordinate of bottom right
Can_widget.create_rectangle(3,5,700,300, fill="red")
Can_widget.create_text(200,200,text="Python")
Can_widget.create_oval(344,233,244,345)
Can_widget.create_arc(314,233,444,345)
Can_widget.create_polygon(344,233,244,345)
Can_widget.create_polygon(344,233,244,345)
Can_widget.create_line(344,233,244,345)
root.mainloop()