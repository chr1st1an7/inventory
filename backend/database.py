import mysql.connector

config = {
    'host': '192.168.1.100',        # Change to your MySQL server hostname
    'port': 3306,               # Change to your MySQL server port
    'user': 'christian',    # Change to your MySQL username
    'password': 'christianKristijan1',  # Change to your MySQL password
    'database': 'inventory'     # Change to your database name
}
try:
    connection = mysql.connector.connect(**config)

except mysql.connector.Error as err:
    print(f"Error: {err}")
