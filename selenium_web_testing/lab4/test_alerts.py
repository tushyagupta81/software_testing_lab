from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

global url
url = "https://www.selenium.dev/documentation/webdriver/interactions/alerts/"


def test_alert_popup():
    driver = webdriver.Chrome()
    driver.get(url)
    element = driver.find_element(By.LINK_TEXT, "See an example alert")
    element.click()

    input()
    wait = WebDriverWait(driver, timeout=2)
    alert = wait.until(lambda d : d.switch_to.alert)
    text = alert.text
    alert.accept()
    assert text == "Sample alert"

    input()
    driver.quit()

def test_confirm_popup():
    driver = webdriver.Chrome()
    driver.get(url)
    element = driver.find_element(By.LINK_TEXT, "See a sample confirm")
    driver.execute_script("arguments[0].click();", element)

    input()
    wait = WebDriverWait(driver, timeout=2)
    alert = wait.until(lambda d : d.switch_to.alert)
    text = alert.text
    alert.dismiss()
    assert text == "Are you sure?"

    input()
    driver.quit()

def test_prompt_popup():
    driver = webdriver.Chrome()
    driver.get(url)
    element = driver.find_element(By.LINK_TEXT, "See a sample prompt")
    driver.execute_script("arguments[0].click();", element)

    input()
    wait = WebDriverWait(driver, timeout=2)
    alert = wait.until(lambda d : d.switch_to.alert)
    alert.send_keys("Selenium")
    text = alert.text
    alert.accept()
    assert text == "What is your tool of choice?"
    
    input()
    driver.quit()

if __name__ == "__main__":
    test_prompt_popup()
    test_alert_popup()
    test_confirm_popup()
