# collection

# declaring an array/list ordered & mutable
array_grades = [77, 80, 90, 95, 100, 105, 107]  # ordered and mutable
array_grades.append(200)  # adding a value in the last value


# declaring a tuple
tuple_grades = (77, 80, 90, 95, 100, 105, 107)  # ordered and immutable
tuple_grades = tuple_grades + (200,)  # because it's immutable so create new!


# declaring a set
set_grades = {77, 80, 90, 95, 100, 105, 107}  # unordered and mutable
set_grades.add(200)  # adding a value into unordered set of collection


# declaring a method to find mean of an array & tuple
def mean_from_array(array):
    mean = sum(array) / len(array)
    return mean


def mean_from_tuple(tuple):
    mean = sum(tuple) / len(tuple)
    return mean


# both are works almost exactly alike
grades_mean_from_array = mean_from_array(array_grades)
print(grades_mean_from_array)

grades_mean_from_tuple = mean_from_tuple(tuple_grades)
print(grades_mean_from_tuple)


# Set operations
your_nums = {1, 2, 3, 4, 5}
winning_nums = {1, 3, 5, 7, 9, 11}

# intersection
your_winning_nums = your_nums.intersection(winning_nums)
# -> will return 1, 3, and 5

# union
all_nums = your_nums.union(winning_nums)
# -> will return 1, 2, 3, 4, 5, 7, 9, and 11

# difference
lose_nums = your_nums.difference(winning_nums)
# -> will return 2, 4, 7, 9, and 11
