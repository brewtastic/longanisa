from Tkinter import *


root = Tk()

topframe = Frame(root)
topframe.pack()

bottomframe = Frame(root)
bottomframe.pack(side=BOTTOM)

button1 = Button(topframe, text="Button 1",bg="green", fg="red")
button2 = Button(topframe, text="Button 2", fg="blue")
button3 = Button(bottomframe, text="Button 3", fg="green")
button4 = Button(bottomframe, text="Button 4", fg="purple")

grow1 = Label(root, text="this thing grows", bg="black", fg="white")
grow1.pack(fill=Y)


button1.pack(side=LEFT)
button2.pack(side=RIGHT)
button3.pack(side=LEFT)
button4.pack(side=RIGHT)


root.mainloop()
