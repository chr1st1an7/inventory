class Item:
    def __init__(self, name, room, category, subcategory, location, quantity, price):
        self.name = name
        self.room = room
        self.category = category
        self.subcategory = subcategory
        self.location = location
        self.quantity = quantity
        self.price = price


    def get_all_items():
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
                query = "SELECT * FROM items"
                cursor.execute(query)

                return cursor.fetchall()

        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return None

        return None
    def create_item(name, room, category, subcategory, location, quantity, price):
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
                insert_item_query = "INSERT INTO items (name, room, category, subcategory, location, quantity, price) VALUES (%s, %s, %s, %s, %s, %s, %s)"
                cursor.execute(insert_item_query, (name, room, category, subcategory, location, quantity, price))

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
            'name': self.name,
            'room': self.room,
            'category': self.category,
            'subcategory': self.subcategory,
            'location': self.location
        }
    

