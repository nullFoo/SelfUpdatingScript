import requests

print("Hello World")

with open("main.py", "r") as f:
    r = requests.get("https://raw.githubusercontent.com/nullFoo/SelfUpdatingScript/main/main.py")
    if(f.read !=  r.text):
        update = input("New update available! Update? (Y/N)")
        if(update == "Y"):
            exec(open('updater.py').read())
            exit()

while(True):
    h = input("type X to exit")
    if(h == "X"):
        exit()
