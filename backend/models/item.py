import database


class Item:
    def __init__(self, name, room, category, subcategory, location, quantity, price, url):
        self.name = name
        self.room = room
        self.category = category
        self.subcategory = subcategory
        self.location = location
        self.quantity = quantity
        self.price = price
        self.url = url

    def get_all_items():
        connection = database.connection
        if connection.is_connected():
            cursor = database.connection.cursor()

            # SQL query to insert a new room into the database
            query = "SELECT * FROM items"
            cursor.execute(query)

            return cursor.fetchall()

    def create_item(name, room, category, subcategory, location, quantity, price, url):
        import mysql.connector
        try:

            # Establish the database connection
            connection = database.connection

            if connection.is_connected():
                cursor = connection.cursor()

                # SQL query to insert a new room into the database
                insert_item_query = "INSERT INTO items (name, room, category, subcategory, location, quantity, price, url) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
                cursor.execute(insert_item_query, (name, room, category,
                               subcategory, location, quantity, price, url))

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
            'location': self.location,
            'url': self.url
        }
