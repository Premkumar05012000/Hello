from tabulate import tabulate
import mysql.connector
con=mysql.connector.connect(host="localhost",user="root",password="root",database="py_db1")
def insert (name , age , phonenum):
    res = con.cursor()
    sql = "insert into users(name,age,phonenum) values (%s,%s,%s)"
    user = (name,age,phonenum)
    res.execute(sql,user)
    con.commit()
    print("data insert success")

def update (name, age, phonenum,id):
       res = con.cursor()
       sql = "update users set name=%s,age=%s,phonenum=%s where id=%s"
       user = (name, age, phonenum,id)
       res.execute(sql, user)
       con.commit()
       print("data update success")
def select():
    res = con.cursor()
    sql = "Select ID,NAME,AGE,PHONENUM from users"
    res.execute(sql)
    result = res.fetchall()
    print(tabulate(result, headers=["ID", "NAME", "AGE", "PHONENUM"]))
def delete(id):
    res=con.cursor()
    sql="delete from users where id=%s"
    user=(id)
    res.execute(sql,user)
    con.commit()
    print("Data delete success")
while True:
    print("1.Insert Data")
    print("2.Update Data")
    print("3.Select Data")
    print("4.Delete Data")
    print("5.Exit")
    choice=int(input("Enter your choice:"))
    if choice==1:
        name=input("Enter Name:")
        age=input("Enter age:")
        phonenum=input("Enter phonenum:")
        insert(name,age,phonenum)
    elif choice == 2:
        id=input("Enter the Id:")
        name = input("Enter Name:")
        age = input("Enter age:")
        phonenum = input("Enter phonenum:")
        update(name, age, phonenum,id)
    elif choice==3:
        select()
    elif choice==4:
        id=input("Enter the Id to Delete:")
        delete(id)
    elif choice==5:
        quit()
else:
        print("Invalid Selection . Plese Try Again!")
