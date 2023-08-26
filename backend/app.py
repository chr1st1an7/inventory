from flask import Flask
from flask_restful import Api
from routes.room_routes import room_bp
from routes.category_routes import category_bp
from routes.item_routes import item_bp

app = Flask(__name__)
api = Api(app)

app.register_blueprint(room_bp)
app.register_blueprint(category_bp)
app.register_blueprint(item_bp)

if __name__ == '__main__':
    app.run(debug=True)
