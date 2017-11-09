def method(anothermethod):
    return anothermethod()


def addition():
    return 35 + 77


method(addition())

# anonymous function will return same value
method(lambda: 35 + 77)

my_list = [13, 56, 77, 484]

filtered_list = list(filter(lambda x: x != 13, my_list))
# filtered list will return [56, 77, 484]


def not_13(x):
    return x != 13

the_same_filtered_list = list(filter(not_13, my_list))
