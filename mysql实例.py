import  pymysql
db=pymysql.connect('localhost','root','1999625','python')
cursor=db.cursor()
cursor.execute("select * from taobao")
data=cursor.fetchone()
print(data)
db.close()