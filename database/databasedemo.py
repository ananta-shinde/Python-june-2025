import mysql.connector

conn = mysql.connector.connect(host="localhost",user="root",password="Demo@123",database="banking_db")

cursor = conn.cursor()
# cursor.execute("create table user (id int not null unique, name varchar(40) not null,primary key(id))")
# cursor.execute("insert into user values(13,'Rahul')")
# cursor.execute("update user set name='Rahul' where id=11")
# cursor.execute("delete from user where id=11")
conn.commit()
cursor.execute("select * from user")
result =cursor.fetchall()
for user in result:
    print(user[1])
# cursor.execute("select * from user")
