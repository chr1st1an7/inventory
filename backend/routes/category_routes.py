from flask import Blueprint, request, jsonify
from flask_restful import Resource, Api
from models.category import Category

category_bp = Blueprint('category_bp', __name__)
api = Api(category_bp)

class CategoryList(Resource):
    def get(self):
        # Your code to fetch all categorys from the database
        categories = Category.get_all_categories()
        return {'categories': categories}, 200

@category_bp.route('/api/category', methods=['POST'])
def create_category():
    data = request.get_json()

    # Check if the required fields are present in the data
    if 'category_name' not in data or 'items' not in data:
        return jsonify({'error': 'Missing required fields'}), 400

    category_name = data['category_name']
    items = f"{data['items']}"

    # Create a new category
    new_category = Category(category_name, items)
    Category.create_category(category_name, items)


    # Add the new category to the database (replace with your database operation)
    # For example, you can call a function like category.create_category(new_category)

    # Convert the category object to a JSON-serializable dictionary
    category_data = new_category.to_json()

    # Return a JSON response with the serialized data
    return jsonify({'message': 'category created successfully', 'category': category_data}), 201


api.add_resource(CategoryList, '/api/category')
