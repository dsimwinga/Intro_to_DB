import mysql.connector
from mysql.connector import Error

def create_database():
    connection = None  # Initialize the connection variable here
    
    try:
        # Establishing a connection to the MySQL server
        connection = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password=''
        )
        
        if connection.is_connected():
            # Create a cursor object to execute SQL queries
            cursor = connection.cursor()
            
            # Query to create the database (only if it doesn't already exist)
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            
            print("Database 'alx_book_store' created successfully!")
        
    except mysql.connector.Error:
        # Print error message if connection or database creation fails
        print("Couldn't connect to the Database")
        
    finally:
        # Ensure the connection is closed, but only if it was successfully established
        if connection is not None and connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed.")

if __name__ == "__main__":
    create_database()
