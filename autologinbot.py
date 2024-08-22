from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# Path to your ChromeDriver change the path to the directory where your chromedriver is located
service = Service(r"C:\path\to\chromedriver.exe")

# Initialize the Chrome driver
driver = webdriver.Chrome(service=service)


# replace the website url you want to login to
website_url = "https://www.etsy.com/in-en/signin"

# your email
user_email = "youremail@gmail.com"

# your password for that account
user_password = "*********"

try:
    # Open the website
    driver.get(website_url)

    # Locate the email and password fields by using inspect feature of the chrome in login page
    email_field = driver.find_element(By.ID, "join_neu_email_field")
    password_field = driver.find_element(By.ID, "join_neu_password_field")
    
    # Locate the submit button by using inspect feature of the chrome in login page
    submit_btn = driver.find_element(By.NAME, "submit_attempt")

    # Enter the login credentials 
    email_field.send_keys(user_email)
    password_field.send_keys(user_password)
    
    # uncomment this if you want also the bot to automaticcally click the login button after automatically  entering the credentials
    # Click the submit button
    # submit_btn.click()

    # Wait for a few seconds to allow the page to load
    time.sleep(10)
except Exception as e:
    print(f"Error occurred: {e}")
finally:
    # Close the browser
    driver.quit()
