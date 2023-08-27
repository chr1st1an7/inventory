import database


class Room:
    def __init__(self, room_name, categories):
        self.room_name = room_name
        self.categories = categories

    def get_all_rooms():
        import mysql.connector
        try:

            # Establish the database connection
            connection = database.connection

            if connection.is_connected():
                cursor = connection.cursor()

                # SQL query to insert a new room into the database
                query = "SELECT * FROM rooms"
                cursor.execute(query)

                return cursor.fetchall()

        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return None

        return None

    def create_room(room_name, room_categories):
        # Establish the database connection
        connection = database.connection

        if connection.is_connected():
            cursor = connection.cursor()

            # SQL query to insert a new room into the database
            insert_room_query = "INSERT INTO rooms (room_name, room_categories) VALUES (%s, %s)"
            cursor.execute(insert_room_query, (room_name, room_categories))

            connection.commit()
            cursor.close()
            return connection

    # Define a method to convert the object to a JSON-serializable dictionary

    def to_json(self):
        return {
            'room_name': self.room_name,
            'categories': self.categories
        }
