#!/usr/local/bin/python3

import mysql.connector
from mysql.connector import Error

try:
    # Establish a connection to the database
    connection = mysql.connector.connect(
        host='localhost',         # Your database host
        user='root',              # Your database username
        password='test12345',   # Your database password
        database='test_db'        # Name of the database
    )

    if connection.is_connected():
        print("Connected to MySQL database")

        # Create a cursor object
        cursor = connection.cursor()

        # Create a table
        create_table_query = """
        CREATE TABLE IF NOT EXISTS employees (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            salary FLOAT NOT NULL
        );
        """
        cursor.execute(create_table_query)
        print("Table created successfully")

        # Insert data into the table
        insert_query = "INSERT INTO employees (name, salary) VALUES (%s, %s)"
        data_to_insert = [
            ("Alice", 75000),
            ("Bob", 50000),
            ("Charlie", 60000)
        ]
        cursor.executemany(insert_query, data_to_insert)
        connection.commit()
        print(f"{cursor.rowcount} rows inserted")

        # Query data from the table
        select_query = "SELECT * FROM employees"
        cursor.execute(select_query)
        results = cursor.fetchall()
        print("Employee Data:")
        for row in results:
            print(row)

except Error as e:
    print(f"Error: {e}")

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection closed")
