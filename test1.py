import mysql.connector as conn

mydb = conn.connect(host = "localhost" , user = "root" , passwd = "arpitmysql")
cursor = mydb.cursor()
#cursor.execute("create database Arpit")
cursor.execute ("show databases")
s =  ("create table Arpit.ineuron(employee_id int(10) , emp_name varchar(80) , emp_mailid varchar(20) , emp_salary int(6) , emp_attendence int(3)")
cursor.execute(s)
