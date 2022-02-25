# find_divPerAnnum.py
# import sys
import mysql.connector

# import configparser
# import os
mydb = mysql.connector.connect(
    host="192.168.2.1",
    port=3307,
    user="jim",
    password="SladeDigger",
    database="stocks"
)

mycursor = mydb.cursor()
msymbol = "MBB"
mdate= "2019-05-13"

sql1 = """SELECT sum(DividendPerShare) INTO @mvar FROM dividend WHERE symbol=%s AND YEAR(date)= %s """
sql2 = "SELECT @mvar AS manswer"

mycursor.execute(sql1,(msymbol,mdate))
myresult1 = mycursor.fetchone()
# print(msymbol, myresult1)

mycursor.execute(sql2)
row = mycursor.fetchone()

while row is not None:
    # print("row: ",row)
    mvar = row[0]
    print(msymbol, "sum DivPerShare: ", mvar)
    row = mycursor.fetchone()
