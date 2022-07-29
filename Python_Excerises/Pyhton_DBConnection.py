import mysql.connector as mariadb
from mysql.connector import Error
import numpy as np
import pandas as pd
import requests

try:
    connection = mariadb.connect(host='localhost',
                                         database='classicmodels',
                                         user='root',
                                         password='root')
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to SQL  version ", db_Info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)
        cursor = connection.cursor()
        sql_select_Query = "select * from offices"
        cursor = connection.cursor()
        cursor.execute(sql_select_Query)
       # get all records
        records = cursor.fetchall()
        print("Total number of rows in table: ", cursor.rowcount)

        print("\nPrinting each row")
        for row in records:
	        print("Id = ", row[0], )
	        print("Name = ", row[1])
	        print("Price  = ", row[2])
	        print("Purchase date  = ", row[3], "\n")


except Error as e:
    print("Error while connecting to Database", e)
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("Database connection is closed")