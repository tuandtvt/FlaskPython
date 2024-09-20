from flask import Flask
from controllers.ScrapingController import scraping
from controllers.AuthController import auth_bp
from models.databaseConfig import db
import os
from dotenv import load_dotenv
from flask_migrate import Migrate

load_dotenv()
app = Flask(__name__)

migrate = Migrate(app, db)

# Get the values
DB_DATABASE = os.getenv('DB_DATABASE')
DB_USERNAME = os.getenv('DB_USERNAME')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_APPNAME = os.getenv('DB_APPNAME')
DB_PORT = os.getenv('DB_PORT')

#sub string the values URI 
DB_URI = f'mysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_APPNAME}:{DB_PORT}/{DB_DATABASE}'
# Configure the SQLAlchemy part of the app instance
# Get config settings from .env file
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the SQLAlchemy db instance with the app
db.init_app(app)

# Register blueprints
app.register_blueprint(scraping)
app.register_blueprint(auth_bp)

@app.route("/", methods=['GET'])
def hello_world():
    return "Hello, World!"  

if __name__ == "__main__":
    app.run(debug=True,threaded=True)
