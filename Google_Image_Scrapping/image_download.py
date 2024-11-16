from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import requests
import os

# Set up the path to your WebDriver executable
driver_path = './chromedriver.exe'  # Replace with the correct path to your WebDriver

# Use Service to initialize the driver path
service = Service(driver_path)
driver = webdriver.Chrome(service=service)

# URL of the website to scrape
url = 'https://www.pexels.com/search/nature/'  # Example website

# Open the URL
driver.get(url)
time.sleep(5)  # Wait for the page to load

# Scroll to load more images
scroll_pause_time = 2
for _ in range(5):  # Scroll multiple times as needed
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(scroll_pause_time)

# Create a directory to save images
os.makedirs('downloaded_images', exist_ok=True)

# Find image elements and download images
images = driver.find_elements(By.TAG_NAME, 'img')

for i, img in enumerate(images[:10]):  # Limit to 10 images for demo
    img_url = img.get_attribute('src')
    if img_url and img_url.startswith('http'):  # Check for valid URL
        img_data = requests.get(img_url).content
        with open(f'downloaded_images/image_{i+1}.jpg', 'wb') as img_file:
            img_file.write(img_data)
        print(f'Image {i+1} saved from {img_url}.')

# Close the browser
driver.quit()
