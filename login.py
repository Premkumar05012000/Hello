Username=input("enter the username:")
password=input("enter the pw:")
name=["prem","kumar","pk","premkumar"]
pw=['123','456','789','134']
if (Username in name):
    if(password in pw):
        thisdict = {
            "Watermelon" :50,
            "onions" :100,
            "Tomatoes" :150,
            "bananas" :200

        }
        print(thisdict)

    else:
        print("pw is incorrect")
else:
    print("username is incorrect")
