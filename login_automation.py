# Hey, let's automate logging into a website!

# First, we need a magic tool called Selenium.
from selenium import webdriver

# Okay, now we pick our favorite browser. We choose Chrome!
browser = webdriver.Chrome()

# Next, we visit the login page of our secret website.
browser.get("https://www.example.com/login")

# Now, we look for the username and password boxes and the 'Login' button.
username = browser.find_element_by_id("username")
password = browser.find_element_by_id("password")
login_button = browser.find_element_by_id("login-button")

# Time to enter our super-secret credentials.
username.send_keys("your_username")
password.send_keys("your_password")

# And we click the magical 'Login' button.
login_button.click()

# We wait for a few seconds to make sure the computer understands.
import time
time.sleep(2)

# Time to check if we made it to the secret dashboard.
if "Dashboard" in browser.title:
    print("Hooray! We're in!")
else:
    print("Oops, something went wrong!")

# Finally, we close the browser. Phew!
browser.quit()
