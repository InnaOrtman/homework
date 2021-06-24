# Task 3

# Write a decorator `arg_rules` that validates arguments passed to the function.
# A decorator should take 3 arguments:
# max_length: 15
# type_: str
# contains: [] - list of symbols that an argument should contain
# If some of the rules' checks returns False, the function should return False
# and print the reason it failed; otherwise, return the result.


def arg_rules(type_: type, max_length: int, contains: list):
    def decorators(func):
        def wrapper(func1):
            if len(func1) >= 16 or type(func1) != type_:
                print("False")
                return False
            else:
                for i in contains:
                    if i in func1:
                        pass
                    else:
                        print("False")
                        return False
                return func(func1)

        return wrapper

    return decorators


@arg_rules(type_=str, max_length=15, contains=['05', '@'])
def create_slogan(name: str):
    print(f'Hello   {name}  world!')


create_slogan("Hello world05@")

create_slogan("Hello world")
