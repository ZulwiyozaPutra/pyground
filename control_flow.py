string = "hello"
nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


def print_characters_in_string(string):
    for character in string:
        print(character)


def print_numbers_in_list(numbers):
    for number in numbers:
        print(2 ** numbers)


# this should execute with python3 intrepreter
def print_numbers_from_input():
    user_input = input(
        "How many numbers are we going to count? Please input a number \n"
    )
    if type(user_input) is int:
        print("Starting to count \n")
        for number in range(1, user_input + 1, 1):
            print(number)
    elif type(user_input) is str:
        input("Please input a number and try again")


print_numbers_from_input()
