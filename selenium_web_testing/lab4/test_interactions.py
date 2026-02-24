from selenium import webdriver

#%%

driver = webdriver.Chrome()

driver.get("https://www.selenium.dev")

#%%

title = driver.title
print(title)
assert title == "Selenium"

url = driver.current_url
print(url)
assert url == "https://www.selenium.dev/"

#%%

driver.quit()
