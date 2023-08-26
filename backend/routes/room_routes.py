from flask import Blueprint, request, jsonify
from flask_restful import Resource, Api
from models.room import Room

room_bp = Blueprint('room_bp', __name__)
api = Api(room_bp)

class RoomList(Resource):
    def get(self):
        # Your code to fetch all rooms from the database
        rooms = Room.get_all_rooms()
        return {'rooms': rooms}, 200

@room_bp.route('/api/rooms', methods=['POST'])
def create_room():
    data = request.get_json()

    # Check if the required fields are present in the data
    if 'room_name' not in data or 'categories' not in data:
        return jsonify({'error': 'Missing required fields'}), 400

    room_name = data['room_name']
    categories = f"{data['categories']}"

    # Create a new room
    new_room = Room(room_name, categories)
    Room.create_room(room_name, categories)


    # Add the new room to the database (replace with your database operation)
    # For example, you can call a function like Room.create_room(new_room)

    # Convert the Room object to a JSON-serializable dictionary
    room_data = new_room.to_json()

    # Return a JSON response with the serialized data
    return jsonify({'message': 'Room created successfully', 'room': room_data}), 201


api.add_resource(RoomList, '/api/room')
