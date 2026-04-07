from selenium.webdriver import Chrome
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


def report_to_bugzilla(driver, error_msg, url):
    # 'echo "Asia/Kolkata" > /etc/timezone' into container if timezone not found
    driver.get("http://localhost:8080/enter_bug.cgi")
    email_el = driver.find_element(By.ID, "Bugzilla_login")
    password_el = driver.find_element(By.ID, "Bugzilla_password")
    login_btn = driver.find_element(By.ID,"log_in")
    
    email_el.send_keys("admin@bugzilla.test")
    password_el.send_keys("password01!")
    login_btn.click()
    WebDriverWait(driver, 5).until(ec.presence_of_element_located((By.ID, "short_desc")))

    summary_el = driver.find_element(By.ID, "short_desc")
    desc_el = driver.find_element(By.ID, "comment")

    summary_el.send_keys(error_msg)
    desc_el.send_keys(url)

    submit_btn = driver.find_element(By.ID, "commit")
    submit_btn.click()

#%%

driver = Chrome()

# %%

url = "https://the-internet.herokuapp.com/login"
driver.get(url)

# %%

input_el = driver.find_element(By.ID, "username")
pasword_ed = driver.find_element(By.ID, "password")

input_el.send_keys("omsmith")
pasword_ed.send_keys("SuperSecretPassword!")

# %%

submit_btn = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/form/button")

submit_btn.click()

# %%

succ_text = driver.find_element(By.XPATH, '//*[@id="content"]/div/h2').text

if succ_text != "Secure Area":
    report_to_bugzilla(driver, "Login failed", url)
