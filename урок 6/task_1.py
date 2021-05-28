# Make a program that has some sentence (a string) on input and returns a dict containing all unique words as
# keys and the number of occurrences as values.

sentence = 'hello world hello'

number = dict()
words = str.split(sentence)

for word in words:
    if word in number:
        number[word] += 1
    else:
        number[word] = 1

print(number)



