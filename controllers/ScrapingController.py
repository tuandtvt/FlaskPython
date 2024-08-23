# import app 
from flask import Blueprint, request, jsonify, make_response
from services.ScrapingService import ScrapingInstagram,GetDataUser
# Import user model from app

# Define the blueprint: 'auth', set its url prefix: app.url/auth
scraping = Blueprint('scraping', __name__, url_prefix='/scraping')

@scraping.route('/get-data-profile', methods=['POST'])
def GetDataProfile():
  # get data user from user table 
  # users = GetDataUser()
  # print("users",users)
  data = request.get_json()
  key = data['key']
  # print(list_username)
  try:
    if key == "wbjLZeCU4f4ccMNZBmrSGhRQs8Mu4OM0":
      extract_data = ScrapingInstagram(data)
      return make_response(extract_data, 200)
    else:
      return make_response(jsonify({'message': "Key not found", "code": 403}), 403)
  except Exception as e:
    return make_response(jsonify({'message': str(e), "code": 403}), 403)
# Configure the SQLAlchemy part of the app instance
