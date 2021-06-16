# Task 2

# Mathematician
# Implement a class Mathematician which is a helper class for doing math operations on lists
# The class doesn't take any attributes and only has methods:
# square_nums (takes a list of integers and returns the list of squares)
# remove_positives (takes a list of integers and returns it without positive numbers
# filter_leaps (takes a list of dates (integers) and removes those that are not 'leap years'

class Mathematician:

    def square_nums(self, *args):
        self.numbers = []
        for i in args:
            s = i ** 2
            self.numbers.append(s)
        print(self.numbers)

    def remove_positives(self, *args):
        self.numbers = []
        for i in args:
            if i > 0:
              self.numbers.append(i)
        print(self.numbers)

    def filter_leaps(self, *args):
        self.numbers = []
        for i in args:
            if i % 4 == 0:
                if i % 100 == 0:
                    if i % 400 == 0:
                        self.numbers.append(i)
                else:
                    self.numbers.append(i)
        print(self.numbers)



ghj = Mathematician()
ghj.square_nums(111, 22, 3)
ghj.remove_positives(-22, 55, 68)
ghj.filter_leaps(2025, 2020, 2021, 2016)



