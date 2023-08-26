class Room:
    def __init__(self, room_name, categories):
        self.room_name = room_name
        self.categories = categories

    def get_all_rooms():
        import mysql.connector
        try:
            # Define the connection parameters
            config = {
                'host': '192.168.1.100',        # Change to your MySQL server hostname
                'port': 3306,               # Change to your MySQL server port
                'user': 'christian',    # Change to your MySQL username
                'password': 'christianKristijan1',  # Change to your MySQL password
                'database': 'inventory'     # Change to your database name
            }

            # Establish the database connection
            connection = mysql.connector.connect(**config)

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
        import mysql.connector
        try:
            # Define the connection parameters
            config = {
                'host': '192.168.1.100',        # Change to your MySQL server hostname
                'port': 3306,               # Change to your MySQL server port
                'user': 'christian',    # Change to your MySQL username
                'password': 'christianKristijan1',  # Change to your MySQL password
                'database': 'inventory'     # Change to your database name
            }

            # Establish the database connection
            connection = mysql.connector.connect(**config)

            if connection.is_connected():
                cursor = connection.cursor()

                # SQL query to insert a new room into the database
                insert_room_query = "INSERT INTO rooms (room_name, room_categories) VALUES (%s, %s)"
                cursor.execute(insert_room_query, (room_name, room_categories))

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
            'room_name': self.room_name,
            'categories': self.categories
        }
    

