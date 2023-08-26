class Category:
    def __init__(self, category_name, items):
        self.category_name = category_name
        self.items = items


    def get_all_categories():
        import mysql.connector
        try:
            # Define the connection parameters
            config = {
                'host': '192.168.1.100',        # Change to your MySQL server hostname
                'port': 3306,               # Change to your MySQL server port
                'user': 'christian',    # Change to your MySQL username
                'password': '',  # Change to your MySQL password
                'database': 'inventory'     # Change to your database name
            }

            # Establish the database connection
            connection = mysql.connector.connect(**config)

            if connection.is_connected():
                cursor = connection.cursor()

                # SQL query to insert a new room into the database
                query = "SELECT * FROM categories"
                cursor.execute(query)

                return cursor.fetchall()

        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return None

        return None
    def create_category(category_name, items):
        import mysql.connector
        try:
            # Define the connection parameters
            config = {
                'host': '192.168.1.100',        # Change to your MySQL server hostname
                'port': 3306,               # Change to your MySQL server port
                'user': 'christian',    # Change to your MySQL username
                'password': '',  # Change to your MySQL password
                'database': 'inventory'     # Change to your database name
            }

            # Establish the database connection
            connection = mysql.connector.connect(**config)

            if connection.is_connected():
                cursor = connection.cursor()

                # SQL query to insert a new room into the database
                insert_category_query = "INSERT INTO categories (category_name, items) VALUES (%s, %s)"
                cursor.execute(insert_category_query, (category_name, items))

                connection.commit()
                cursor.close()
                return connection

        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return None

        return None
    



    # Define a method to convert the object to a JSON-serializable dictionary
    def to_json(self):
        return {
            'category_name': self.category_name,
            'items': self.items
        }
    

