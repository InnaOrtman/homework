stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}
# Create a function which takes as input two dicts with structure mentioned above,
# then computes and returns the total price of stock.

x=0
for fruit in stock.keys():
    x = x + stock[fruit] * prices[fruit]

print(x)

