from tkinter import *

def greet():
    username=e1.get()
    password=e2.get()

    l3["text"]=username+" "+password

app = Tk()

app.geometry("1000x500")

l1=Label(app,text="Username")
l2=Label(app,text="Password")
l3=Label(app)

e1=Entry(app)
e2=Entry(app)

b=Button(app,text="Login",command=greet)

l1.place(x=40,y=40)
l2.place(x=40,y=70)
l3.place(x=40,y=150)
e1.place(x=120,y=40,width=200)
e2.place(x=120,y=70,width=200)

b.place(x=40,y=110,width=100)

app.mainloop()
