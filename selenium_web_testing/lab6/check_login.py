import os
import time

import pandas as pd
import requests
from dotenv import load_dotenv
from rich import print
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

load_dotenv()

# ----- CONFIG -----
BUGZILLA_URL = "http://localhost:8080/rest"
API_KEY = os.environ.get("API")

PRODUCT = "TestProduct"
COMPONENT = "TestComponent"
VERSION = "unspecified"
# -------------------

headers = {"Content-Type": "application/json", "X-BUGZILLA-API-KEY": API_KEY}


def login_bug():
    url = f"{BUGZILLA_URL}/login?login=admin@bugzilla.test&password=password01!"
    r = requests.get(url)
    return r.json()["token"]


def get_bug(id, token):
    url = f"{BUGZILLA_URL}/bug/{id}"
    r = requests.get(url, params={"token": token})
    return r.json()


def create_bug(summary, token):
    url = f"{BUGZILLA_URL}/bug"

    data = {
        "product": PRODUCT,
        "component": COMPONENT,
        "summary": summary,
        "version": VERSION,
        # "description": "Bug lifecycle test",
        "severity": "major",
        "status": "UNCONFIRMED",
        "priority": "Highest",
        "op_sys": "All",
        "platform": "All",
    }

    r = requests.post(url, params={"token": token}, json=data, headers=headers)

    if r.status_code != 200:
        print("Create failed:", r.text)
        return None

    bug_id = r.json()["id"]
    print("Created bug:", bug_id)
    return bug_id


token = login_bug()

driver = Chrome()

# %%

df = pd.read_csv("./lab6/creds.csv")

# %%


def login(username, password):
    driver.get("https://the-internet.herokuapp.com/login")

    input_el = driver.find_element(By.ID, "username")
    pasword_ed = driver.find_element(By.ID, "password")

    input_el.send_keys(username)
    pasword_ed.send_keys(password)

    submit_btn = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/form/button")

    submit_btn.click()
    time.sleep(1)

    failed_text = driver.find_element(By.ID, "flash").text

    if "invalid" not in failed_text:
        print(f"Logged in for {username}, {password}")
        create_bug(f"Logged in for {username}, {password}", token)


# %%

for r in df.iloc[:, :].values:
    login(r[0], r[1])
