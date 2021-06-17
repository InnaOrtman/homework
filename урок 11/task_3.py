# Task 4
# Custom exception
# Create your custom exception named `CustomException`,
# you can inherit from base Exception class,
# but extend its functionality to log every error message
# to a file named `logs.txt`.
# Tips: Use __init__ method to extend functionality for saving messages to file

class CustomException(Exception):
    def __init__(self, msg):
        if msg:
            self.message = msg
            with open(r"my_file.txt", 'w') as hello_file:
                hello_file.write(self.message)
        else:
            self.message = None

    def __str__(self):
        print('We have a problem!')
        if self.message:
            return 'MyError, {0} '.format(self.message)
        else:
            return 'MyError has been raised'


raise CustomException('We have a problem')


