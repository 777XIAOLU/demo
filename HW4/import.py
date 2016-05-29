import PostgreSQl
conn = PostgreSQL.connect('localhost','dbo','123456','hw04')
curs = conn.cursor()
curs.execute('''CREATE TABLE A(sn VARCHAR(20) PRIMARY KEY,sn INT Name CHAR)''')
curs.excute('INSERT INTO A VALUES("10,A10")')
curs.excute('INSERT INTO A VALUES("20,A20")')
curs.excute('INSERT INTO A VALUES("30,A30")')
curs.excute('INSERT INTO A VALUES("40,A40")')
curs.excute('INSERT INTO A VALUES("50,A50")')
curs.excute('INSERT INTO A VALUES("60,A60")')
cursor.close();
