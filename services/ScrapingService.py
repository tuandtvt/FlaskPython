
import argparse
import json
import instaloader
import json
loader = instaloader.Instaloader()
from common.helper import open_selenium_to_get_data
from selenium_insta import open_insta
from models.user import User

def ScrapingInstagram(list_username):
    # Follower Count
    # Feed Count
    # Story Count
    # Reel Count
    # Feed Content
    # Feed Likes Count
    # Feed Comments Count
    # Story Content
    # Reel Content
    # Reel Likes Count
    # Reel Comments Count
    data = open_selenium_to_get_data(list_username)
    response = None
    outputs = {
                "meta": {
                    "code": 200,
                }, 
                "data": data
            }
    response = json.dumps(outputs, ensure_ascii=False, indent=4)
    return response
def GetDataUser():
    # get data user from user table 
    users = User.query.all()
    users = [user.to_dict() for user in users]
    return users