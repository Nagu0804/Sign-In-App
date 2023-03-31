import mysql.connector
from tabulate import tabulate


con=mysql.connector.connect(host='localhost',user='root',password='my@root',database='person_details')

def insert(uname,age,city):
    cur=con.cursor()
    sql='insert into details(uname,age,city) values(%s,%s,%s) '
    user=(uname,age,city)
    cur.execute(sql,user)
    con.commit()
    print('Data insert successfull')


def update(uname,age,city,id):
    cur=con.cursor()
    sql = 'update details set uname=%s,age=%s,city=%s where id=%s '
    user = (uname, age, city,id)
    cur.execute(sql, user)
    con.commit()
    print('Data update successfull')

def select():
    cur=con.cursor()
    sql='select * from details'
    cur.execute(sql)
    result=cur.fetchall()
    print(tabulate(result,headers=['ID','Name','Age','City']))


def delete(id):
    cur=con.cursor()
    sql='delete from details where id=%s'
    user=(id,)
    cur.execute(sql,user)
    con.commit()
    print('Data delete successfull')

while True:
    print('1.insert Data')
    print('2.update Data')
    print('3.select Data')
    print('4.delete Data')
    print('5.Exit')
    c=int(input('Enter your choice:'))
    if c==1:
        name=input('Enter your name:')
        age=int(input('Enter your age:'))
        city=input('Enter your city:')
        insert(name,age,city)
    elif c==2:
        id=input('Enter Id:')
        name=input('Enter your name:')
        age=int(input('Enter your age:'))
        city=input('Enter your city:')
        update(name,age,city,id)
    elif c==3:
        select()
    elif c==4:
        id=input('Enter Id:')
        delete(id)
    elif c==5:
        quit()
    else:
        print('Entered invalid data')