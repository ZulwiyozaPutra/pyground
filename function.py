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
def multiply(num, other_num):
    return num * other_num


# run a multi argument method
multiplication_result = multiply(2, 3)
print(multiplication_result)
