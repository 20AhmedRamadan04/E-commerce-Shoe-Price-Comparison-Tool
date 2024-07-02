import requests as RE
from bs4 import BeautifulSoup as BS
import csv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

header_written = False

# Function to scrape data from Shoeroom website using Selenium for scrolling
def scrape_shoeroom_with_selenium():
    shoeroom_sneakers_details = []
    
    # Set up the Selenium web driver (make sure to have the correct driver installed for your browser)
    driver = webdriver.Chrome()  # Or webdriver.Firefox() or any other browser driver you have
    
    try:
        driver.get("https://shoeroom.shoes/product-category/shoes/sneakers/")
        
        # Simulate scrolling down to load more content
        last_height = driver.execute_script("return document.body.scrollHeight")
        
        while True:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(3)  # Adjust this timing as needed
            new_height = driver.execute_script("return document.body.scrollHeight")
            
            if new_height == last_height:
                break
            last_height = new_height
        
        time.sleep(5)  # Add additional wait time after scrolling (adjust as necessary)
        
        shoeroom_src = driver.page_source
        shoeroom_soup = BS(shoeroom_src, "lxml")
        all_shoeroom_sneakers = shoeroom_soup.find_all("li", {"class": "col-xs-6"})
        
        for sneaker in all_shoeroom_sneakers:
            shoeroom_sneaker_name = sneaker.find("h2").text.strip()
            shoeroom_sneaker_price = sneaker.find("span", {"class": "price"}).text.strip()
            shoeroom_sneakers_details.append({"Website": "Shoeroom", "Name": shoeroom_sneaker_name, "Price": shoeroom_sneaker_price})
    
    finally:
        driver.quit()  # Ensure the driver is closed even if an exception occurs
    
    return shoeroom_sneakers_details

# Function to scrape data from Jumia website
def scrape_jumia():
    jumia_sneakers_details = []
    header_written = False

    for i in range(1, 51):
        jumia_sneakers = RE.get(f"https://www.jumia.com.eg/ar/catalog/?q=سنيكرز&page={i}#catalog-listing")
        jumia_src = jumia_sneakers.content
        jumia_soup = BS(jumia_src, 'lxml')
        all_jumia_sneakers = jumia_soup.find("div", {"class": "-paxs row _no-g _4cl-3cm-shs"}).find_all("article", {"class": "prd _fb col c-prd"})

        for jumia_sneakers_loop in all_jumia_sneakers:
            jumia_sneakers_name = jumia_sneakers_loop.find("h3").text.strip()
            jumia_sneakers_price = jumia_sneakers_loop.find("div", {"class": "prc"}).text.strip()
            jumia_sneakers_details.append({"Website": "Jumia", "Name": jumia_sneakers_name, "Price": jumia_sneakers_price})
    
    return jumia_sneakers_details

# Main function to combine and write data to CSV
def main():
    shoeroom_data = scrape_shoeroom_with_selenium()
    jumia_data = scrape_jumia()
    
    combined_data = shoeroom_data + jumia_data

    keys = combined_data[0].keys()
    with open('combined_sneakers.csv', 'w', newline='', encoding='utf-8-sig') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(combined_data)

    print("File Created")

# Execute the main function
main()
