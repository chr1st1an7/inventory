import database


class Category:
    def __init__(self, category_name, items):
        self.category_name = category_name
        self.items = items

    def get_all_categories():
        connection = database.connection
        if connection.is_connected():
            cursor = connection.cursor()

            # SQL query to insert a new room into the database
            query = "SELECT * FROM categories"
            cursor.execute(query)

            return cursor.fetchall()

    def create_category(category_name, items):

        # Establish the database connection
        connection = database.connection

        if connection.is_connected():
            cursor = connection.cursor()

            # SQL query to insert a new room into the database
            insert_category_query = "INSERT INTO categories (category_name, items) VALUES (%s, %s)"
            cursor.execute(insert_category_query, (category_name, items))

            connection.commit()
            cursor.close()
            return connection

    # Define a method to convert the object to a JSON-serializable dictionary

    def to_json(self):
        return {
            'category_name': self.category_name,
            'items': self.items
        }
