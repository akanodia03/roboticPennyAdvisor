import mysql.connector

mydb = mysql.connector.connect( host="localhost", user="root", passwd="goodwill", database="penny_store")

myCursor = mydb.cursor()
myCursor.execute("select * from payments")
result = myCursor.fetchall()
for i in result:
    print(i)