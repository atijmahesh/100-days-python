from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = "https://appbrewery.github.io/Zillow-Clone/"
form_url = "https://forms.gle/YyVChK8AGnt5aQEw6"

r = requests.get(url=url)
soup = BeautifulSoup(r.text, "html.parser")
link_elements = soup.find_all('a', class_='property-card-link')
link_list = [link.get('href') for link in link_elements]

price_elements = soup.find_all('span', class_='PropertyCardWrapper__StyledPriceLine')
price_list = []
for price in price_elements:
    clean_price = price.get_text(strip=True)  #
    clean_price = clean_price.split('+')[0] 
    clean_price = clean_price.split('/')[0] 
    clean_price = clean_price.strip() 
    price_list.append(clean_price)

address_elements = soup.find_all('address', attrs={'data-test': 'property-card-addr'})
address_list = []
for address in address_elements:
    clean_address = address.get_text(separator=" ").strip() 
    clean_address = clean_address.replace('|', '') 
    clean_address = ' '.join(clean_address.split())
    address_list.append(clean_address)

# selenium part
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
wait = WebDriverWait(driver, 10)

driver.get("https://forms.gle/YyVChK8AGnt5aQEw6")

for link, price, address in zip(link_list, price_list, address_list):
    # Fill out the address input
    address_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[aria-labelledby='i1']")))
    address_input.send_keys(address)
    
    # Fill out the price input
    price_input = driver.find_element(By.XPATH, "//*[@id='mG61Hd']/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input")
    price_input.send_keys(price)
    
    # Fill out the link input
    link_input = driver.find_element(By.XPATH, "//*[@id='mG61Hd']/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input")
    link_input.send_keys(link)
    
    # Click the submit button
    driver.find_element(By.XPATH, "//span[text()='Submit']").click()
    driver.get("https://forms.gle/YyVChK8AGnt5aQEw6") 

driver.quit()