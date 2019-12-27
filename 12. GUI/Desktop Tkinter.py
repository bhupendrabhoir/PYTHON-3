from tkinter import *

app = Tk()

app.geometry("1000x500")

b1=Button(app,text="Click")
b2=Button(app,text="Click")
b3=Button(app,text="Click")
b4=Button(app,text="Click")

b1.pack(side=TOP)
b2.pack(side=BOTTOM)
b3.pack(side=RIGHT)
b4.pack(side=LEFT)

app.mainloop()
