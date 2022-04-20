youname = input("Whats Your Name")
yesno = input("Is this your name")
if yesno == "yes":
    print("Acsess Granted")
    doingsuff = input("What would you like to do")
    if doingsuff == ("Deactivate the mainframe"):
        print("Shuting down")
        print( )
        print( )
        print("Mainframe off")
        whatnow = input("what Now")
        if whatnow == (" "):
            print("Please Put in a valid character")
        else:
            print ("okay")
        if whatnow == ("Die"):
            print("Gunshots echo in the background")
        if whatnow == ("Actiave the mainframe"):
            print("Turning on")
            print("Its on")
        else:
            print("okay")
            whatnow = input("What would you like to do")
        if whatnow == ("off"):
            print("Bye")
    else:
        print ("okay")
        doingsuff = input("What would you like to do")
elif yesno == "no":
    print("Acsess Dined")
else:
    print("Acsess Dined")