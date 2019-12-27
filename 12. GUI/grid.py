from tkinter import *

app = Tk()

app.geometry("1000x500")

l1=Label(app,text="Username")
l2=Label(app,text="Password")

e1=Entry(app)
e2=Entry(app)

b=Button(app,text="Login")

l1.grid(column=0, row=0)
l2.grid(column=0, row=1)
e1.grid(column=1, row=0)
e2.grid(column=1, row=1)
b.grid(column=0, row=2)

app.mainloop()
