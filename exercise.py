import sys

names_list = []


def who_do_you_know():
    names = input("Who do you know? \n")
    if type(names) is str:
        for name in names.split():
            names_list.append(name)
        ask_user()
    else:
        print("Please input a sequence of name separated by space \n")
        sys.exit()


def ask_user():
    name = input("What name you still remember? \n")
    if name in names_list:
        print("Yay you still remember %s" % name)
        sys.exit()
    else:
        print("Please try again!")
        sys.exit()


who_do_you_know()
