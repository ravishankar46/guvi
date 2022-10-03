import re


def register():
    db = open("database.txt", "r")
    Username = input("create Username:")
    password = input("create password:")
    password1 = input("create password1:")
    flag = 0
    user = 0
    d = []
    f = []
    for i in db:
        a,b = i.split(", ")
        b = b.strip()
        d.append(a)
        f.append(b)
    data = dict(zip(d, f))

    if password != password1:
        print("passwords doesn't match,restart")
        register()
    else:
        if Username in d:
            print("Username exist")
            register()
        if not re.search('[!@#$%.]', Username):
            user = 1
        if not re.search('[a-z]', Username):
            user = 1
        if not re.search('[0-9]', Username):
            user = 1
        if (user == 0):
            print("valid Username")
        if (user != 0):
            print("invalid Username")
        if not re.search('[!@#$%]', password):
            flag = 1
        if not re.search('[a-z]', password):
            flag = 1
        if not re.search('[0-9]', password):
            flag = 1
        if not re.search('[A-Z]', password):
            flag = 1
        if len(password) <=6:
            flag = 1
        if (flag == 0):
            print("valid password")
        if (flag != 0):
            print("invalid password")

        # if Username in d:
        #     print("Username esist")
        #     register()
        else:
            db= open("database.txt", "a")
            db.write(Username+", "+password+"\n")
            print("success!")

def access():
    db = open("database.txt", "r")
    Username = input("enter your Username:")
    password = input("enter your password:")

    if not len(Username or password)<1:
        d = []
        f = []
        for i in db:
            a, b = i.split(", ")
            b = b.strip()
            d.append(a)
            f.append(b)
        data = dict(zip(d, f))

        try:
            if data[Username]:
                try:
                    if password == data[Username]:
                        print("login success")
                    else:
                        print("password or Username incorrect")
                except:
                    print("incorrect password or Username")
            else:
                print("Username or password doesn't exist")
        except:
            print("Username or password doesn't exist")
    else:
        print("please enter a value")

def home(option=None):
    option = input("login | signup:")
    if option == "login":
        access()
    elif option == "signup":
        register()
    #else:
        #print("please enter an option")
        #Username = input("enter your Username:")
        #password = input("enter your password:")
home()




