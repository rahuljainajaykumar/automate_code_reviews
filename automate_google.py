from selenium import webdrive

# Start a webdriver (e.g. Chrome)
driver = webdriver.Chrome()

# Navigate to the Google search page
driver.get("https://www.google.com")

# Find the search box element and enter a search query
search_box = driver.find_element_by_name("q")
search_box.send_keys("Selenium automation")

# Find the search button element and click it
search_button = driver.find_element_by_name("btnK")
search_button.click()

# Wait for the search results to load
driver.implicitly_wait(10)

# Print the title of the search results page
print(driver.title)

# Close the browser
driver.close()
