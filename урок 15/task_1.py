# Task 1

# Create a class method named `validate`, which should be called from the `__init__`
# method to validate parameter email, passed to the constructor. The logic inside the `validate`
# method could be to check if the passed email parameter is a valid email string.

from email_validator import validate_email, EmailNotValidError


class Validator:
    def __init__(self, email):
        self.email = email

    @property
    def validate(self):
        try:
            valid = validate_email(self.email)
            self.email = valid.email
            print(valid.email, 'is correct!')

        except EmailNotValidError as e:
            print(str(e))


validator_1 = Validator('innalevko1987@gmail.com')
validator_2 = Validator('innalevko1987gmail.com')

validator_1.validate

validator_2.validate


