from tkinter import *

def add():
    num1=int(e1.get())
    num2=int(e2.get())
    result=num1+num2
    l3["text"]=result

def sub():
    num1=int(e1.get())
    num2=int(e2.get())
    result=num1-num2
    l3["text"]=result

def mul():
    num1=int(e1.get())
    num2=int(e2.get())
    result=num1*num2
    l3["text"]=result

def div():
    num1=int(e1.get())
    num2=int(e2.get())
    result=num1/num2
    l3["text"]=result

app = Tk()

app.geometry("1000x500")

l1=Label(app,text="Num1")
l2=Label(app,text="Num2")
l3=Label(app)

e1=Entry(app)
e2=Entry(app)

b1=Button(app,text="ADD",command=add)
b2=Button(app,text="SUB",command=sub)
b3=Button(app,text="MUL",command=mul)
b4=Button(app,text="DIV",command=div)

l1.place(x=40,y=40)
l2.place(x=40,y=70)

e1.place(x=120,y=40,width=200)
e2.place(x=120,y=70,width=200)

b1.place(x=40,y=110)
b2.place(x=120,y=110)
b3.place(x=200,y=110)
b4.place(x=280,y=110)
l3.place(x=50,y=150)

app.mainloop()
