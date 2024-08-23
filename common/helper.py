import instaloader
# from instaloader import Post
import requests
import time
import random
import re
# import instaloader as instaloader_story
import json
from selenium_insta import open_insta
from urllib.parse import urlparse
import json
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.proxy import Proxy, ProxyType
from bs4 import BeautifulSoup
from instagram_private_api import Client, ClientCompatPatch
import time
from googleapiclient.discovery import build
import tweepy
def extract_follower_count(follower_text):
    print("follower_text",follower_text)
    match = re.search(r'([\d,]+) フォロワー', follower_text)
    # Extract and convert follower count
    match万 = re.search(r'([\d,.]+)(万?) フォロワー', follower_text)
    number = 0
    if match:
        # Remove commas and convert to integer
        number = int(match.group(1).replace(',', ''))
        return number
    elif match万:
        # Remove commas and convert to integer
        number = float(match万.group(1).replace(',', ''))
        unit = match万.group(2)
        if unit == '万':
            number *= 10000
            number = int(number)
            return number
    else:
        return number
def extract_follower_count_by_html(content):
    # Regular expression to match the follower count
    match_en = re.search(r'([\d,]+) Followers', content)
    match_large = re.search(r'([\d,.]+)([MK]?) Followers', content)
    match_jp = re.search(r'フォロワー([\d,.]+)([M万]?)人', content)
    
    if match_large:
        number = float(match_large.group(1).replace(',', ''))
        unit = match_large.group(2)
        if unit == 'M':
            number *= 1_000_000
        elif unit == 'K':
            number *= 1_000
        return int(number)
    
    if match_en:
        number = int(match_en.group(1).replace(',', ''))
        return number
    
    if match_jp:
        number = float(match_jp.group(1).replace(',', ''))
        unit = match_jp.group(2)
        if unit == 'M':
            number *= 1_000_000
        elif unit == '万':
            number *= 10_000
        return int(number)
    
    return 0
def GetDataFollowerCountX(username):
    twitter_follower_count = 0
    try:
        bearer_token = 'AAAAAAAAAAAAAAAAAAAAABbQvQEAAAAA7%2BwtWvAXKVOiSYqZA17KRXgjxIM%3DFvN1iJbJRZofOyjHlU4swLFo4j9BQQMTGjUAoCVVvQ5WHYIuA1'
        # Authenticate with the Twitter API v2
        client = tweepy.Client(bearer_token=bearer_token)
        # Fetch the user by username
        user = client.get_user(username=username, user_fields=['public_metrics'])
        # Extract and print the follower count
        twitter_follower_count = user.data.public_metrics['followers_count']
        print(f"User {username} has {twitter_follower_count} followers.")
        return twitter_follower_count
    except Exception as e:
        print(f"An error occurred twitter: {e}")
        return twitter_follower_count
def get_channel_id_by_handle(api_key, handle):
    youtube = build('youtube', 'v3', developerKey=api_key)
    request = youtube.search().list(
        part='snippet',
        q=handle,
        type='channel'
    )
    response = request.execute()
    if 'items' in response and len(response['items']) > 0:
        return response['items'][0]['snippet']['channelId']
    else:
        print("Channel not found")
        return None
def get_youtube_subscribers(api_key, identifier, is_username=True):
    # Build the YouTube service
    youtube = build('youtube', 'v3', developerKey=api_key)

    # Determine the parameter to use based on whether it's a username or channel ID
    if is_username:
        request = youtube.channels().list(
            part='statistics',
            forUsername=identifier
        )
    else:
        request = youtube.channels().list(
            part='statistics',
            id=identifier
        )

    response = request.execute()

    # Extract the number of subscribers
    if 'items' in response and len(response['items']) > 0:
        subscribers = response['items'][0]['statistics']['subscriberCount']
        return int(subscribers)
    else:
        print("Channel not found")
        return None

# Replace with your API key and YouTube username or channel ID
def get_data_youtube_subs(handle):
    follower_count = 0
    api_key = 'AIzaSyBRZGaEfojho9oo4VRrZOMX0iQgOAix04k'
    channel_id = get_channel_id_by_handle(api_key, handle)
    if channel_id:
        # Get the subscriber count using the channel ID
        subscribers = get_youtube_subscribers(api_key, channel_id, is_username=False)
        if subscribers is not None:
            follower_count = subscribers
            return follower_count
        else:
            return follower_count
    else:
        return follower_count

def get_follower_count(username):
    # Generate rank token
    follower_count = 0
    try: 
        user_name = 'caominh2814@gmail.com'
        password = 'Manh1234'

        api = Client(user_name, password)
        result = api.username_info(username)
        follower_count = result['user']['follower_count']
        return follower_count
    except Exception as e:
        print(f"Error: {str(e)}")
        return follower_count


# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.keys import Keys

def open_selenium_to_get_data(data):
    # open_insta("huyenntmk1","Mk123456")
    dataUrl = data['urls']
    print("dataUrl",dataUrl)
    tiktokUrl = dataUrl['tiktokUrl']
    instagramUrl = dataUrl['instagramUrl']
    youtubeUrl = dataUrl['youtubeUrl']
    twitterUrl = dataUrl['twitterUrl']
    try:
        options = Options()
        # options.proxy = proxy
        options.add_argument("--headless")
        options.add_argument("--disable-infobars")
        options.add_argument("start-maximized")
        options.add_argument("--disable-extensions")
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        # fake profile browser
        options.set_preference("dom.webdriver.enabled", False)
        options.set_preference('useAutomationExtension', False)
        options.set_preference("general.useragent.override", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
        options.set_preference("intl.accept_languages", "ja,ja-JP;q=0.9,en;q=0.8,en-US;q=0.7")
        # Provide path to the geckodriver executable
        
        # Initialize the WebDriver
        driver = webdriver.Firefox(options=options)
        # open 4 url to get followers value 
        # open tiktok
        tiktok_followers = 0
        if tiktokUrl == "":
            tiktok_followers = 0
        else:
            driver.get(tiktokUrl)
            time.sleep(2)
            # get content html 
            content = driver.page_source
        # Step 2: Parse the HTML content
            soup = BeautifulSoup(content, 'html.parser')
            # get data in script tag
            script = soup.find_all('script')
            #  find followerCount in script tag
            
            # check empty tiktokUrl 
            for tag in script:
                if "followerCount" in tag.text:
                    data = tag.text
                    #parse data to json
                    data = json.loads(data)
                    data = data['__DEFAULT_SCOPE__']['webapp.user-detail']['userInfo']['stats']
                    tiktok_followers = data['followerCount']
                    # data = data['followerCount']
                    print("Follower count:", data)
                    break
        # extract username from last of youtubeUrl
        if youtubeUrl == "":
            youtube_followers = 0
        else:
            usernameYoutube = youtubeUrl.split("/")[-1]
            youtube_followers = get_data_youtube_subs(usernameYoutube)
            print("youtube_followers",youtube_followers)
        # Get data follower count from twitter
        # open twitter
        # extract username twitter the first element after www.twitter.com https://twitter.com/amatsuki_aisub
        if twitterUrl == "":
            twitter_followers = 0
        else:
            parsed_url = urlparse(twitterUrl)
            usernameTwitter = parsed_url.path.strip('/').split('/')[0]
            print("usrname",usernameTwitter)
            twitter_followers = 0
            twitter_followers = GetDataFollowerCountX(usernameTwitter)
            if twitter_followers == 0:
                driver.get(twitterUrl)
                #extract username from last of url
                usernameTwitter = twitterUrl.split("/")[-1]
                hrefCheck = f"/{usernameTwitter}/verified_followers"
                print("hrefCheck",hrefCheck)
                time.sleep(2)
                content = driver.page_source
                    # Step 2: Parse the HTML content
                soup = BeautifulSoup(content, 'html.parser')
                # save data in file
                # with open('data_twitter.html', 'w',encoding='utf-8') as file:
                #     file.write(soup.prettify())
                # Check if href="/_iam_natsuki/verified_followers" exists
                link = soup.find('a', href=hrefCheck)
                if link:
                    print("text",link.text)
                    # get text value in tag a
                    twitter_followers = extract_follower_count(link.text)
                    print("twitter_followers",twitter_followers)

                else:
                    print("URL /_iam_natsuki/verified_followers does not exist")
                print("twitter_followers",twitter_followers)
        # extract username instagram the first element after www.instagram.com https://www.instagram.com/i.am_natsuki_/?hl=ja
        if instagramUrl == "":
            instagram_followers = 0
        else:
            parsed_url = urlparse(instagramUrl)
            usernameInsta = parsed_url.path.strip('/').split('/')[0]
            print("usernameInsta",usernameInsta)
            instagram_followers = 0
            instagram_followers = get_follower_count(usernameInsta)
            if instagram_followers == 0:
                # get data from get requests
                dataMTML = requests.get(instagramUrl)
                # get content html
                content = dataMTML.text
                # Step 2: Parse the HTML content
                soup = BeautifulSoup(content, 'html.parser')
                # get meta og:description
                meta = soup.find('meta', property='og:description')
                # get content of meta
                content = meta['content']
                # extract follower count from content
                instagram_followers = extract_follower_count_by_html(content)
                print("content",content)
                print("instagram_followers",instagram_followers)

        print("instagram_followers",instagram_followers)
        # get followers from dataInsta
        data = {
            "tiktok_followers": tiktok_followers,
            "instagram_followers": instagram_followers,
            "youtube_followers": youtube_followers,
            "twitter_followers": twitter_followers
        }
        driver.quit()
        return data
    except Exception as e:
        print(f"Error: {str(e)}")
        driver.quit()
        response = {
            "message": {str(e)},
            "status_code": 401
        }
        return response
    






