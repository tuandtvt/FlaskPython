import json
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.proxy import Proxy, ProxyType

# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.keys import Keys
import time
# Load cookies from the file
def load_cookies_from_file(file_path):
    with open(file_path, 'r') as f:
        cookies = json.load(f)
    return cookies
# Initialize the WebDriver
# Load cookies from the file
def open_insta(username, password):
    # Open Instagram
    # Configure the Proxy settings
    # proxy_ip_port = '14.160.32.23:8080'  # Replace 'your_proxy_ip:port' with your actual proxy IP and port
    # proxy = Proxy({
    #     'proxyType': ProxyType.MANUAL,
    #     'httpProxy': proxy_ip_port,
    #     'sslProxy': proxy_ip_port,
    # })
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
        # Provide path to the geckodriver executable
        
        # Initialize the WebDriver
        driver = webdriver.Firefox(options=options)
        # cookies = load_cookies_from_file(cookie_file_path)
        # Load the Instagram login page
        driver.get("https://www.instagram.com")
        time.sleep(4)  # Adjust the sleep time as necessary
        # Load cookies from the JSON file
        # Load session cookies
        # Login to Instagram by username and password
        # username = "mk1vn09@gmail.com"
        # password = "mk123456"
        username = username
        password = password
        # Find the username and password fields and enter the login credentials
        username_field = driver.find_element("name", "username")
        password_field = driver.find_element("name", "password")
        
        username_field.send_keys(username)
        password_field.send_keys(password)
        
        # Find and click the login button
        login_button = driver.find_element("xpath", "//button[@type='submit']")
        login_button.click()

        time.sleep(4)  # Wait for the login process to complete
        #process save info button
        try:
            save_info = driver.find_element("xpath", "//button[text()='Lưu thông tin']")
            if save_info:
                save_info.click()
        except:
            pass
        try:
            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//div[@role='button' and @aria-label='Bỏ qua']"))
            ).click()
        except Exception as e:
            print(f"Error: {str(e)}")
            pass
        try:
            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//div[@role='button' and @aria-label='Dismiss']"))
            ).click()
        except:
            pass
        try:
            save_info = driver.find_element("xpath", "//button[text()='Lúc khác']")
            if save_info:
                save_info.click()
        except:
            pass
        # Get data cookies instagram
        time.sleep(4)  # Adjust the sleep time as necessary
        cookies = driver.get_cookies()
        # Convert cookies to JSON format
        cookies_json = json.dumps(cookies)
        cookies_dict = json.loads(cookies_json)
        # If you want to save this JSON data to a file
        with open('cookie.json', 'w') as f:
            f.write(cookies_json)
        time.sleep(3)
        driver.quit()
        response = {
            "message": "Cookies saved successfully!",
            "status_code": 200, 
            "data": cookies_dict
        }
        data = json.dumps(response, ensure_ascii=False, indent=4)
        return data
    except Exception as e:
        print(f"Error: {str(e)}")
        driver.quit()
        response = {
            "message": {str(e)},
            "status_code": 401
        }
        return response


