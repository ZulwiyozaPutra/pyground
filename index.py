# declaring variable
my_variable = "this is a string variable"


# declaring a method
def hello_world():
    print("Hellow World!")


# run a method
hello_world()


# declaring a method with argument
def hello(my_name):
    print("Hello %s!" % my_name)


# run a method with argument
hello("Putra")


# declaring multi argument method
def multiply(num1, num2):
    return num1 * num2


# run a multi argument method
multiplication_result = multiply(2, 3)
print(multiplication_result)

# collection

# declaring an array/list ordered & mutable
array_grades = [77, 80, 90, 95, 100, 105, 107]  # ordered and mutable
array_grades.append(200)


# declaring a tuple
tuple_grades = (77, 80, 90, 95, 100, 105, 107)  # ordered and immutable
tuple_grades = tuple_grades + (200,)


# declaring a set
set_grades = {77, 80, 90, 95, 100, 105, 107}  # unordered and mutable
set_grades.add(200)


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
