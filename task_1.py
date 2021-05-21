'''
Write a Python program to get a string made of the first 2 and the last 2 chars from a given string.
If the string length is less than 2, return instead of the empty string.
Sample String: 'helloworld'
Expected Result : 'held'
Sample String: 'my'
Expected Result : 'mymy'
Sample String: ' x'
Expected Result: Empty String
'''
s1 = 'helloworld'
print(s1[0:2]+s1[-2:len(s1)])

s2 = 'my'
print(s2*2)

s3 = 'x'
print(s3[0:-1])