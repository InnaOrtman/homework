# Task 3

# Write a function called `choose_func` which takes a list of nums and 2 callback functions.
# If all nums inside the list are positive, execute the first function on that list and return the result of it.
# Otherwise, return the result of the second one

def choose_func(func, func1, nums: list):
    for num in nums:
        if num > 0:
            square_nums(nums)
        if num < 0:
            remove_negatives(nums)


def square_nums(nums: list):
    numbers = []
    for i in nums:
        s = i ** 2
        numbers.append(s)
    print(numbers)


def remove_negatives(nums: list):
    numbers = []
    for i in nums:
        if i > 0:
            numbers.append(i)
    print(numbers)


nums1 = [1, 2, 3, 4, 5]

nums2 = [1, -2, 3, -4, 5]

choose_func(square_nums, remove_negatives, nums1)

choose_func(square_nums, remove_negatives, nums2)


