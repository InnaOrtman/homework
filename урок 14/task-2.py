# Task 2

# Write a decorator that takes a list of stop words and replaces them with * inside the decorated function

from functools import wraps


def stop_words(words: list):
    def change_string(func):
        def wrapper(*args, **kwargs):
            new_str = str(func(*args, **kwargs))
            for word in words:
                if word in new_str:
                    new_str = new_str.replace(word, '*')
            return new_str

        return wrapper

    return change_string


@stop_words(['pepsi', 'BMW'])
def create_slogan(name: str):
    return f'{name} drinks pepsi in his brand new BMW!'


print(create_slogan('Steve'))
