import argparse
import json
import instaloader
import json
loader = instaloader.Instaloader()
from common.helper import open_selenium_to_get_data
from selenium_insta import open_insta

def custom_error(code):
    outputs = {
                "meta": {
                    "code": code
                }
            }
    response = json.dumps(outputs, ensure_ascii=False, indent=4)
    print(response)
    return response

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
# def GetDataStory(list_username):
   
#     # Story Count
#     # Story Content
#     data = get_data_story(list_username)
#     response = None
#     outputs = {
#                 "meta": {
#                     "code": 200,
#                 }, 
#                 "data": data
#             }
#     response = json.dumps(outputs, ensure_ascii=False, indent=4)
#     return response

def test_selenium_open():
    dataRes =  open_insta("mk1vn09@gmail.com","mk123456")
    return dataRes
    # selenium open instagram and add cookies
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--usernames', type=str, help='URL', required=True)

    args = parser.parse_args()
    try:
        ScrapingInstagram(args.usernames)
    except:
        custom_error(500)