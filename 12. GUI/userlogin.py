from tkinter import *

app = Tk()

def add():
    add=Toplevel()
    add.geometry("400x200")
    add.title("New Register")
         
    l4=Label(add, text="User Details")
    l4.grid(column=2,row=0)
    l5=Label(add, text="Username")
    l5.grid(column=0,row=2)
    l6=Label(add, text="Password")
    l6.grid(column=0,row=3)
    l7=Label(add, text="Contact")
    l7.grid(column=0,row=4)
    l8=Label(add, text="")
    l8.grid(column=0,row=5)
    
    def submit():
        l8.configure(text="User Added successfully")
    
    b3=Button(add, text="Submit", command=submit)
    b3.grid(column=2,row=6)

    l8=Label(add, text="User Adding")
    l8.grid(column=2,row=7)
        
    e3=Entry(add,width=30)
    e3.grid(column=2,row=2)
    e4=Entry(add,width=30)
    e4.grid(column=2,row=3)
    e5=Entry(add,width=30)
    e5.grid(column=2,row=4)
    
def login():
    Top=Toplevel()
    Top.geometry("800x400")
    Top.title("User Details")
    

app.geometry("400x200")

l1=Label(app,text="Uesrname:")
l2=Label(app,text="Password:")
l3=Label(app)


e1=Entry(app)
e2=Entry(app)

b1=Button(app,text="Login",command=login)
b2=Button(app,text="New Register",command=add)

l1.place(x=40,y=40)
l2.place(x=40,y=70)

e1.place(x=120,y=40,width=200)
e2.place(x=120,y=70,width=200)

b1.place(x=190,y=110,width=130)
b2.place(x=40,y=110,width=130)
l3.place(x=50,y=150)

app.mainloop()
