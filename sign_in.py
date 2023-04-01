from tkinter import *
import mysql.connector

con=mysql.connector.connect(host='localhost',user='root',password='my@root',database='log_in')

x = Tk()
x.geometry('200x200')
x.title('Email')
x.iconbitmap('mail.ico')
x.config(bg='sky blue')

text = StringVar()
text1 = StringVar()
text2 = StringVar()

login=Label(x,text='SIG IN',bg='sky blue')
login.grid(row=0,columnspan=3)

name=Label(x,text='Name',bg='sky blue')
name.grid(row=1,column=1, pady=10)
mail=Label(x,text='Email Id',bg='sky blue')
mail.grid(row=2,column=1, pady=10)
pwd=Label(x,text='Password',bg='sky blue')
pwd.grid(row=3,column=1,pady=10)

e=Entry(x,textvariable=text)
e.grid(row=1,column=2, pady=10)
e1=Entry(x,textvariable=text1)
e1.grid(row=2,column=2, pady=10)
e2=Entry(x,show='*',textvariable=text2)
e2.grid(row=3,column=2, pady=10)


def save(text,text1,text2):
    cur=con.cursor()
    sql='insert into persons(name,email,pwd) values(%s,%s,%s) '
    user=(text,text1,text2)
    cur.execute(sql,user)
    con.commit()
    clear()
    don = Label(x, text='Sign in Successfull!')
    don.grid(row=7, columnspan=4)

def clear():
    global expression
    expression = ""
    text.set("")
    text1.set("")
    text2.set("")


b=Button(x,text='Submit',command=lambda: save(text.get(), text1.get(), text2.get()))
b.grid(row=5,columnspan=3)

'''
def success():
    print('Log in Successfull!')'''




x.mainloop()

con.close()
