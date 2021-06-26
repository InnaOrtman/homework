# Task 1

# Create a class method named `validate`, which should be called from the `__init__`
# method to validate parameter email, passed to the constructor. The logic inside the `validate`
# method could be to check if the passed email parameter is a valid email string.

import re
from pip._vendor.pyparsing import Regex


class Validator:
    def __init__(self, email):
        self.email = email

    @property
    def validate(self):
        regex = '(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)'
        if not re.match(regex, self.email):
            print(self.email, " is incorrect")
        else:
            print(self.email, " is correct")


validator_1 = Validator('innalevko1987@gmail.com')
validator_2 = Validator('innalevko1987gmail.com')

print(validator_1.validate)
print(validator_2.validate)

