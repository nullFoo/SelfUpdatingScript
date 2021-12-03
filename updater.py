from time import sleep
import requests

sleep(1)
with open("main.py", "w") as f:
    r = requests.get("https://raw.githubusercontent.com/nullFoo/SelfUpdatingScript/main/main.py")
    f.write(r.text)
    f.close()
