# Write a Python program to get a string made of the first 2 and the last 2 chars from a given string.
# If the string length is less than 2, return instead of the empty string.
# Sample String: 'helloworld'
# Expected Result : 'held'
# Sample String: 'my'
# Expected Result : 'mymy'
# Sample String: ' x'
# Expected Result: Empty String

s1 = 'my'

if len(s1) < 2:
    print(' ')
else:
    print(s1[:2]+s1[-2:])

