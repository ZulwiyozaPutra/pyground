numbers = [0, 1, 2, 3, 4]

if numbers == [x for x in range(5)]:
    print("This is all the same")

some_numbers = [2 ** x for x in range(10)]
print(some_numbers)


def even_numbers(n):
    numbers = [x for x in range(n) if x % 2 == 0]
    return numbers


def print_even_numbers():
    n = input("Even numbers will starting from 0 to ...? \n")
    if type(n) is int:
        numbers = even_numbers(n)
        print(numbers)
    else:
        input_type = type(input)
        print("Your input is a/an %s please input an int!" % repr(input_type))


# print_even_numbers()

names = ["Rolf", " John", "annA", "GREG ", "z Putra"]
normalized_names = [name.strip().lower() for name in names]

print(normalized_names)
