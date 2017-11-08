import sys

usernames = ["admin", "root", "zulwiyozaputra"]
password = "password"
username = input("Enter a username: \n")


def login():
    if username in usernames:
        user_password = input("Enter a password: \n")
        if user_password == password:
            print("Welcome %s! \n" % password)
        else:
            print("Invalid password! Please try again")
            sys.exit()
    else:
        print("Invalid username! Please try again")
        sys.exit()


login()
