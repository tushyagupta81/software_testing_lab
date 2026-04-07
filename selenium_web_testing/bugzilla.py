import os

import requests
from dotenv import load_dotenv
from rich import print

load_dotenv()

# ----- CONFIG -----
BUGZILLA_URL = "http://localhost:8080/rest"
API_KEY = os.environ.get("API")

PRODUCT = "TestProduct"
COMPONENT = "TestComponent"
VERSION = "unspecified"
# -------------------

headers = {"Content-Type": "application/json", "X-BUGZILLA-API-KEY": API_KEY}


def login():
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
        "description": "Bug lifecycle test",
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

    print(r.text)
    bug_id = r.json()["id"]
    print("Created bug:", bug_id)
    return bug_id




def update_bug(bug_id, data, label, token):
    url = f"{BUGZILLA_URL}/bug/{bug_id}"

    r = requests.put(url, params={"token": token}, json=data, headers=headers)

    if r.status_code != 200:
        print(f"{label} failed:", r.text)
        return False

    print(f"{label} OK")
    return True




def get_history(bug_id, token):
    url = f"{BUGZILLA_URL}/bug/{bug_id}/history"
    r = requests.get(url, params={"token": token}, headers=headers)

    if r.status_code != 200:
        print("History fetch failed:", r.text)
        return

    history = r.json()["bugs"][0]["history"]
    # print(history)

    print("\nActivity Log:")
    print("----------------------")
    for entry in history:
        for change in entry["changes"]:
            print(
                f"{change['field_name']} -> {change['added']} (was {change['removed']})"
            )


# %%

token = login()

# %%

bug_id = create_bug("Lifecycle test bug", token)

if not bug_id:
    exit()

# %%

# ASSIGN
update_bug(bug_id, {"status": "CONFIRMED"}, "Assign", token)
info = get_bug(bug_id, token)
print("Changed bug status to", info["bugs"][0]["status"])


# %%

# RESOLVE
update_bug(bug_id, {"assigned_to": "admin@bugzilla.test"}, "Assign to user", token)
update_bug(bug_id, {"status": "RESOLVED", "resolution": "FIXED"}, "Resolve", token)
info = get_bug(bug_id, token)
print("Changed resolution to", info["bugs"][0]["resolution"])
print("Changed status to", info["bugs"][0]["status"])
print("Changed assigned_to to", info["bugs"][0]["assigned_to"])


# %%

# VERIFY
update_bug(bug_id, {"status": "VERIFIED"}, "Verify", token)
info = get_bug(bug_id, token)
print("Changed status to", info["bugs"][0]["status"])


# %%

# Fetch activity log
get_history(bug_id, token)
