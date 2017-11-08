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


# declaring array
grades = [77, 80, 90, 95, 100, 105, 107]


# declaring a method to find mean of an array
def mean(array):
    mean = sum(array) / len(array)
    return mean


grades_mean = mean(grades)
print(grades_mean)
