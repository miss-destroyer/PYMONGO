import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

 
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://www.daraz.pk/')
driver.maximize_window()

box = driver.find_element(By.ID, "q")
box.clear()
box.send_keys("Boya M1")
driver.find_element(By.CLASS_NAME, "search-box__button--1oH7").click()

mic_name = []
mic_price = []
reviews = []

time.sleep(5)

all_products = driver.find_elements(By.XPATH, '//div[@class = "_17mcb"]')

for product in all_products:

    mic_names = product.find_elements(By.XPATH, './/div[@class="RfADt"]')
    mic_name = [mic.text for mic in mic_names]
    

    mic_price = product.find_elements(By.XPATH, './/span[@class="ooOxS"]')
    mic_price = [mic.text for mic in mic_price]


    mic_reviews = product.find_elements(By.XPATH, './/span[@class="qzqFw"]')
    reviews = [mic_review.text for mic_review in mic_reviews] if mic_reviews else ["0"]


    print(mic_name)
    print(mic_price)
    print(reviews)


with open('mic_data.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Mic Name", "Mic Price", "Reviews"])
    for i in range(len(mic_name)):
        writer.writerow([mic_name[i], mic_price[i], reviews[i]])