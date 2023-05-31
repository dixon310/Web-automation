from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.get("https://www.google.com")

search_input = driver.find_element(By.NAME, "q")
search_input.send_keys("abc news")
search_input.send_keys(Keys.RETURN)

# Wait for the search results to load
search_results = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.g"))
)

# Get the URL of the first search result
first_result_url = search_results[0].find_element(By.TAG_NAME, "a").get_attribute("href")
print(first_result_url)
driver.get (first_result_url)

