import mysql. connector
connect_args={
	"host":"192.168.1.115",
	"port":3307,
	"user":"jim",
	"password":"ttaskk",
	"database":"stocks"}

db=mysql.connector.connect(**connect_args)
cursor=db.cursor(named_tuple=True)

sql="SELECT * FROM firms WHERE fid=5"
cursor.execute(sql)
print(cursor.fetchone())

cursor.close()
db.close()
