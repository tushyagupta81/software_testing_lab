from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

driver = Chrome()

# %%

driver.get("https://the-internet.herokuapp.com/login")

# %%

input_el = driver.find_element(By.ID, "username")
pasword_ed = driver.find_element(By.ID, "password")

input_el.send_keys("tomsmith")
pasword_ed.send_keys("SuperSecretPassword!")

# %%

submit_btn = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/form/button")

submit_btn.click()

# %%

succ_text = driver.find_element(By.XPATH, '//*[@id="content"]/div/h2').text

if succ_text != "Secure Area":
    sc = driver.get_screenshot_as_png()
    with open("screenshot.png", "wb") as f:
        f.write(sc)
