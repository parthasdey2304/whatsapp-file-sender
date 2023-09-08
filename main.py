from selenium import webdriver

# Set up the Selenium WebDriver (make sure you have chromedriver installed)
driver = webdriver.Chrome('path_to_chromedriver.exe')  # Replace with the path to your chromedriver executable

# Open the web page
driver.get("https://form.new")

# Wait for the page to load (you can adjust the waiting time as needed)
driver.implicitly_wait(10)

# Find the Google Form link element by its tag name (assuming it's an anchor tag)
google_form_link = driver.find_element_by_tag_name("a")

# Get the link URL from the element
google_form_url = google_form_link.get_attribute("href")

# Print the link URL
print("Google Form Link:", google_form_url)

# Now, you can continue to target other elements and make changes as needed using Selenium.
# For example, you can interact with form fields, buttons, etc., on the Google Form.

# Close the browser when you're done
driver.quit()
