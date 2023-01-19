import mysql.connector as b
mc=b.connect(host="localhost",user='root',passwd='D!nken2459')
mycur=mc.cursor()
mycur.execute("Create database if not exists Banking")
mycur.execute("Use Banking")

mycur.execute("Create table bank(Acc_No int primary key,Cust_Name varchar(20),Address varchar(30),Phone_No varchar(11),Email varchar(40),Dep_Amt int,With_Amt int, Balance int)")


mycur.execute("Create table password(pwd varchar(10))")
mycur.execute("insert into password values('Project')")
mc.commit()
mc.close()
