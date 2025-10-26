import mysql.connector
from PythonFunctions.config import DB_CONFIG

def createConnection():
    try:
        connection = mysql.connector.connect(
            host=DB_CONFIG['host'],
            user=DB_CONFIG['user'],
            password=DB_CONFIG['password'],
            database=DB_CONFIG['database']
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

def closeConnection(conn):
    if conn:
        conn.close()
