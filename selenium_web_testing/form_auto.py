from selenium import webdriver
from pathlib import Path
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

#%%

driver = webdriver.Chrome()
driver.get("https://www.selenium.dev/selenium/web/web-form.html")

#%%

text_input = driver.find_element(By.ID, "my-text-id")
password_input = driver.find_element(By.NAME, "my-password")
textarea = driver.find_element(By.NAME, "my-textarea")

text_input.send_keys("Sample text")
password_input.send_keys("mypassword123")
textarea.send_keys("Testing textarea automation")

select_element = Select(driver.find_element(By.NAME, "my-select"))
select_element.select_by_visible_text("Two")

datalist = driver.find_element(By.NAME, "my-datalist")
datalist.send_keys("Seattle")

file_input = driver.find_element(By.NAME, "my-file")
file_input.send_keys(str(Path("./main.py").absolute()))

checkbox1 = driver.find_element(By.ID, "my-check-1")
checkbox2 = driver.find_element(By.ID, "my-check-2")

if not checkbox1.is_selected():
    checkbox1.click()

if not checkbox2.is_selected():
    checkbox2.click()

radio1 = driver.find_element(By.ID, "my-radio-1")
radio2 = driver.find_element(By.ID, "my-radio-2")

radio1.click()
radio2.click()

color_picker = driver.find_element(By.NAME, "my-colors")
driver.execute_script("arguments[0].value='#ff0000'", color_picker)

date_picker = driver.find_element(By.NAME, "my-date")
date_picker.send_keys("12/31/2024")

range_slider = driver.find_element(By.NAME, "my-range")
driver.execute_script("arguments[0].value=7", range_slider)

#%%

submit_button = driver.find_element(By.CSS_SELECTOR, "button")
submit_button.click()

message = driver.find_element(By.ID, "message")
print("Result:", message.text)

#%%

driver.quit()
