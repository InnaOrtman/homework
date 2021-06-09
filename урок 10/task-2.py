# Task 2
# Doggy age
# Create a class Dog with class attribute `age_factor` equals to 7.
# Make __init__() which takes values for a dog’s age.
# Then create a method `human_age` which returns the dog’s age in human equivalent.

class Dog():

    def __init__(self, dogs_age):
        self.age_factor = 7
        self.dogs_age = dogs_age

    def human_age(self):
        resalt = self.dogs_age * self.age_factor
        print(f"The human age of your dog will be {resalt}")

pug = Dog(4)
pug.human_age()

