def normal_total(arg1, arg2, arg3):
    return arg1 + arg2 + arg3


total = normal_total(32, 21, 27)


def argsified_total(*args):
    return sum(args)


if argsified_total(32, 21, 27) == total:
    print("args is so powerful for multiple number argument")


# kwargs stands for keyword arguments
