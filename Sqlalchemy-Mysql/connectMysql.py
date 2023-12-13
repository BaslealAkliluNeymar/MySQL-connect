import mysql.connector
connect = mysql.connector.connect(host='localhost',password='neybas10marleal',user='root')

cur = connect.cursor()
cur.execute("Select * from md_water_services.auditor_report")
table = cur.fetchone()
print(table)

cur.close()
connect.closer()
