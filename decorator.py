import functools


def my_decorator(func):
    @functools.wraps(func)
    def function_that_runs_func():
        print("In the decorator!")
        func()
        print("printing after the decorator")
    return function_that_runs_func


@my_decorator
def my_function():
    print("I'm the function")


# my_function()

#####

def decorator_with_arg(number):
    def my_decorator(func):
        @functools.wraps(func)
        def function_that_runs_func(*args, **kwargs):
            print("In the decorator")
            if number == 56:
                print("Not running the function")
            else:
                func(*args, **kwargs)
            print("After the decorator")
        return function_that_runs_func
    return my_decorator


@decorator_with_arg(56)
def my_another_function(x, y):
    print("Hello")


my_another_function(56, 57)
