import mysql.connector

my_db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = '1A2s3D4f5G6h7J8k9L0z1Z2x3C4v5B6n7M'
)

my_cursor = my_db.cursor()

my_cursor.execute("CREATE DATABASE adoption")

# my_cursor.execute("SHOW DATABASES")
# for db in my_cursor:
#     print(db)