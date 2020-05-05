import cx_Oracle
import csv

username = 'MYONLINEEDU'
password = 'njvf24'
databaseName = 'localhost/xe'
connection = cx_Oracle.connect(username,password, databaseName)
cursor_t = connection.cursor()

tables = ['STORE3', 'CITY3', 'COUNTRY3', 'OWNERSHIP3','BRAND3']

for t in tables:
    with open(f'{t}.csv', 'w', newline='') as file:
        query = f'SELECT * FROM {t}'
        writing = csv.writer(file, delimiter=',')
        cursor_t.execute(query)
        row = cursor_t.fetchone()
        while row:
            writing.writerow(row)
            row = cursor_t.fetchone()
cursor_t.close()
connection.close()
