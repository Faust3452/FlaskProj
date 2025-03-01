import mysql.connector
import pandas as pd


mysql_conn = mysql.connector.connect(user='root', password='34521678',
                                     host='127.0.0.1')
print(mysql_conn.is_connected())
query0 = """
USE test_db;
"""

query1 = """
SHOW TABLES;
"""

query2 = """
INSERT INTO test_db.test_table
(id, name)
VALUES(1, 'ALEX');
"""
query3 = """
CREATE TABLE table_name 
(
    column_name_1 column_type_1,
    column_name_2 column_type_2,
    ...,
    column_name_N column_type_N,
);

"""
with mysql_conn.cursor() as cursor:
    cursor.execute(query0)
    cursor.execute(query1)
    tables = cursor.fetchall()
    print(tables)


# mysql_conn.commit() - for adding new data in table

mysql_conn.close()