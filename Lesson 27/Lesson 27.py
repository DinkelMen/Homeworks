import mysql.connector as mysql
"""Class Work"""
db = mysql.connect(host="localhost",
                   user="Dima",
                   passwd="cnfkrth",
                   database='test_db')

cursor = db.cursor()
# cursor.execute("CREATE DATABASE test_db")
# cursor.execute("SHOW DATABASES")
# cursor.execute("CREATE TABLE users (name VARCHAR(255), user_name VARCHAR(255))")
# cursor.execute("CREATE TABLE users_key (id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), "
#                "user_name VARCHAR(255))")
# cursor.execute("SHOW TABLES")
# print(cursor.fetchall())
# cursor.execute("ALTER TABLE users ADD COLUMN id INT(11) NOT NULL AUTO INCREMENT PRIMARY KEY FIRST")
# cursor.execute("DESC users_key")
# print(cursor.fetchall())
# query = "INSERT INTO users_key (name, user_name) VALUES (%s, %s)"
# values = [
#     ("Peter", "peter"),
#     ("Amy", "amy"),
#     ("Michael", "michael"),
#     ("Hennah", "hennah")
# ]
#
# cursor.executemany(query, values)
# db.commit()
# print(cursor.rowcount, "records inserted")
#
# cursor = db.cursor()
# query = "SELECT * FROM users_key"
# cursor.execute(query)
# print(cursor.fetchall())
# cursor.execute("DESC salesman")
# print(cursor.fetchall())

# print(cursor.fetchall())
# cursor.execute("""CREATE TABLE salesman (salesman_id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
#                 name VARCHAR(255), city VARCHAR(255), commission FLOAT(11), grade INT(11))""")
# cursor.execute("""CREATE TABLE salesman_id (id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
#                                     name VARCHAR(255),
#                                     city VARCHAR(255),
#                                     comission FLOAT,
#                                     grade INT(11))""")

# query = "INSERT INTO salesman (name, city, commission, grade) VALUES (%s, %s, %s, %s)"
# values = [
#     ("James Hoog", "New York", "0.15", "100"),
#     ("Nail Knite", "Paris", "0.13", "200"),
#     ("Pit Alex", "London", "0.11", "150"),
#     ("Mc Lyon", "Paris", "0.14", "50"),
#     ("Paul Adam", "Rome", "0.13", "200"),
#     ("Lauson Hen", "San Jose", "0.12", "300")
# ]
# cursor.executemany(query, values)
#
# db.commit()

"""Homework"""
# cursor.execute("""CREATE TABLE orders1 (id INT(11) AUTO_INCREMENT PRIMARY KEY,
#                                       ord_no INT(11) ,
#                                       purch_amt FLOAT,
#                                       ord_date DATE,
#                                       customer_id INT(11),
#                                       salesman_id INT(11))""")
query = "INSERT INTO orders1 (ord_no, purch_amt, ord_date, customer_id, salesman_id) VALUES (%s, %s, %s, %s, %s)"
values = [
    ("70001", "150.5", "2012-10-5", "3005", "5002"),
    ("70009", "270.65", "2012-09-10", "3001", "5005"),
    ("70002", "65.26", "2012-10-05", "3002", "5001"),
    ("70004", "110.5", "2012-08-17", "3009", "5003"),
    ("70007", "948.5", "2012-09-10", "3005", "5002"),
    ("70005", "2400.6", "2012-07-27", "3007", "5001"),
    ("70008", "5760", "2012-09-10", "3002", "5001"),
    ("70010", "1983.43", "2012-10-10", "3004", "5006"),
    ("70003", "2480.4", "2012-10-10", "3009", "5003"),
    ("70012", "250.45", "2012-06-27", "3008", "5002")
]
# cursor.executemany(query, values)
# db.commit()

# cursor.execute("DELETE FROM orders WHERE ord_no > 10")
# cursor.execute("SELECT * FROM orders1")
# 1 задание
# cursor.execute("SELECT ord_no, ord_date, purch_amt FROM orders1 WHERE salesman_id = 5002")
# 2 задание
# cursor.execute("SELECT DISTINCT salesman_id FROM orders1")
# 3 задание
# cursor.execute("SELECT ord_date, salesman_id, ord_no, purch_amt FROM orders1")
# 4 задание
cursor.execute("SELECT * FROM orders1 WHERE ord_no between 70001 AND 70007")
print(cursor.fetchall())
db.close()
