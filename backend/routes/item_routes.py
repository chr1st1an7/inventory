from flask import Blueprint, request, jsonify
from flask_restful import Resource, Api
from models.item import Item

item_bp = Blueprint('item_bp', __name__)
api = Api(item_bp)

class ItemList(Resource):
    def get(self):
        # Your code to fetch all Items from the database
        items = Item.get_all_items()
        return {'Items': items}, 200

@item_bp.route('/api/item', methods=['POST'])
def create_item():
    data = request.get_json()

    # Check if the required fields are present in the data
    # if 'name' or 'room' or 'category' or 'location' not in data:
    #     return jsonify({'error': 'Missing required fields'}), 400

    name = data['name']
    room = data['room']
    category = data['category']
    subcategory = data['subcategory']
    location = data['location']
    quantity = data['quantity']
    price = data['price']
    url = data['url']

    # Create a new Item
    new_item = Item(name, room, category, subcategory, location, quantity, price, url)
    Item.create_item(name, room, category, subcategory, location, quantity, price, url)


    # Add the new Item to the database (replace with your database operation)
    # For example, you can call a function like Item.create_Item(new_Item)

    # Convert the Item object to a JSON-serializable dictionary
    item_data = new_item.to_json()

    # Return a JSON response with the serialized data
    return jsonify({'message': 'Item created successfully', 'Item': item_data}), 201


api.add_resource(ItemList, '/api/item')
