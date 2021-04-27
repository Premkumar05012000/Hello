newuser=input("Are u new user(yes/no):")
c = ['arun','denna']
d = ['123','234']
if newuser=="yes":
    a = []
    b = []
    c = ['as']
    d = ['df']
    e = input("enter the  name:")
    f = input("enter the phone number:")
    g = input("enter the username:")
    h = input("enter the pw:")
    a.append(e)
    b.append(f)
    c.append(g)
    d.append(h)
    print("successfully registered")
    con=input("If u contine to login page(please select yes/no): ")
if (newuser =="no") or (con=="yes"):
    a1 = input("enter the userid:")
    a2 = input("enter the password:")
    if (a1 and a2) in (c and d):
        dict1 = {
            1: ["Watermelon", 50],
            2: ["onions", 100],
            3: ["Tomatoes", 150],
            4: ["bananas", 200],
        }
        print("{:<10} {:<10}".format('Name', 'Cost'))
        for key, value in dict1.items():
            name, cost = value
            print("{:<10} {:<10}".format(name, cost))
    else:
        print("Invalid UserName and Password")
elif con=="no":
        print("Thankyou for registration")

