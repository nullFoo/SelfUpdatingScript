while(True):
    update = input("Update? (Y/N)")
    if(update == "Y"):
        exec(open('updater.py').read())
        exit()
