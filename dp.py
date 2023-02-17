import sqlite3
connect= sqlite3.connect("users.db")
    
def insertdata(name,age,city):
    values="insert into users(NAME,AGE,CITY) values(?,?,?);"
    connect.execute(values,(name,age,city))
    connect.commit()
    print("your details was added ")
   
    
def updatedata(name,age,city,id):
    values="update users set NAME=? ,AGE=? ,CITY=? where id=?;"
    connect.execute(values,(name,age,city,id))
    connect.commit()
    print("ypur data was updatated")
    
def deletdata(id):
    qry="delete from users where id=?;"
    connect.execute(qry,(id))
    connect.commit()
    print("delete data succesfully")
    
def selcetdata():
    qry = "select * from users "
    data = connect.execute(qry,)
    for row in data:
        print(row)
    

    
print(""" 
1.insert
2.update
3.delete
4.select

""")
chose=1

while chose==1:
    c=int(input("enter ur choose : "))
    if (c==1):
        print("you select the insert option")
        name=input("enter ur name : ")
        age =int(input("enter ur age :"))
        city=input("enterv ur city :")
        insertdata(name,age,city)
       
        
    elif (c==2):
        print("you slect the uptate ")
        id= input('enter ur id ')
        name=input("enter ur name : ")
        age =int(input("enter ur age :"))
        city=input("enterv ur city :")
        updatedata(name,age,city,id)
    elif (c==3):
        print("you slect the delete ")
        id=input("enter ur id to conform the delete table : ")
        deletdata(id)
        
    elif (c==4):
        print("you slect the selcet all ")
        selcetdata()
    else:
        print("enter ur corrct number ")
        print("thank you ")       