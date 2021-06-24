# Task 1

# Write a decorator that prints function with arguments passed to it.
# NOTE! It
# should
# print
# the
# function, not the
# result
# of
# its
# execution!


def logger(f):
    def wrapper(*args, **kwargs):
        result = f(*args, **kwargs)
        print(f.__name__ + ' is called with ' + str(args))
        return result

    return wrapper


@logger
def add(x, y):
    return x + y


@logger
def square_all(*args):
    return [arg ** 2 for arg in args]


add(4, 5)
square_all(4, 5, 1)
