from selenium import webdriver
from selenium.webdriver.common.by import By

# %%

driver = webdriver.Chrome()

driver.get("https://www.selenium.dev/selenium/web/web-form.html")

# %%

text_input = driver.find_element(by=By.ID, value="my-text-id")
password_input = driver.find_element(by=By.NAME, value="my-password")
text_area = driver.find_element(by=By.NAME, value="my-textarea")
radio_button = driver.find_element(by=By.ID, value="my-radio-2")
submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")

#%%

text_input.send_keys("Input field")
password_input.send_keys("password")
text_area.send_keys("Text area")
radio_button.click()

#%%

submit_button.click()

# %%

message = driver.find_element(by=By.ID, value="message")
text = message.text
print(text)

# %%

driver.quit()
