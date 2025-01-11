# PYMONGO
# **Scrape data Using Selenium:** 

In this project I am doing web scraping using Selenium library and store scrape data on pymongo. I have scraped the data of Mic including name, price and ratings from daraz.pk using Selenium library. I did not scrape the URL because each product link on the site is given a separate tag name. That's why it was getting difficult for me to scrape the URL. 

Below I have mentioned all the steps which I followed

1. **Web Scraping with Selenium:**  
- I used Selenium to automate the extraction of the required data product name, price, and ratings from Daraz.pk and store it in csv file. 

2. **CSV to JSON:**  
- All the scrape data that are store in csv file, I convert it in JSON file.

   - (First I created a CSV file here and then converted all the data into JSON file. This was because if I directly converted the data from CSV to JSON, first all the names would be printed, then prices and then the ratings.)  

3. **Data Store in PYMongo:** 
- Imported the JSON data into PyMongo, storing it in a collection named test-collection

