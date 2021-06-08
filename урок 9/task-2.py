# Task 2
# Functionality of Phonebook application:
#
# Add new entries
# Search by first name
# Search by last name
# Search by full name
# Search by telephone number
# Search by city or state
# Delete a record for a given telephone number
# Update a record for a given telephone number
# An option to exit the program
import itertools
import json
import sys
import os


PHONEBOOK = {}
phone_book = []
temp = []


def initial_phonebook():
    rows, cols = int(input("Enter the number of contacts you want to add: ")), 5

    for i in range(rows):

        for j in range(cols):

            if j == 0:
                temp.append(str(input("Enter name*: ")))
                if temp[j] == '' or temp[j] == ' ':
                    sys.exit(
                        "Name is a mandatory field. Process exiting due to blank field...")

            if j == 1:
                temp.append(int(input("Enter number*: ")))

        PHONEBOOK['name'] = temp[0]
        PHONEBOOK['phone'] = temp[1]
        phone_book.append(temp)

    print(phone_book)
    return phone_book


def menu():
    print("********************************************************************")
    print("\tYou can now perform the following operations on this phonebook\n")
    print("1. Add a new contact")
    print("2. Remove an existing contact")
    print("3. Delete all contacts")
    print("4. Search for a contact")
    print("5. Display all contacts")
    print("6. Exit phonebook")

    choice = int(input("Please enter your choice: "))

    return choice


def add_contact(pb):
    dip = []
    for i in range(len(pb[0])):
        if i == 0:
            dip.append(str(input("Enter name: ")))
        if i == 1:
            dip.append(input("Enter number: "))
        if i == 2:
            dip.append(str(input("Enter city: ")))

    pb.append(dip)
    print(pb)
    return pb


def remove_existing(pb):
    query = str(
        input("Please enter the name of the contact you wish to remove: "))

    temp = 0

    for i in range(len(pb)):
        if query == pb[i][0]:
            temp += 1

            print(pb.pop(i))
            print("This number has now been removed")
            return pb
    if temp == 0:
        print("Sorry, you have entered an invalid value.\
    Please recheck and try again later.")

        return pb


def delete_all(pb):
    return pb.clear()


def search_existing(pb):
    choice = int(input("\nEnter search criteria \n\
    1. Name\n2. Number\n3. City\
    \nPlease enter: "))

    temp = []
    check = -1

    if choice == 1:
        query = str(
            input("Please enter the name of the contact you wish to search: "))
        for i in range(len(pb)):
            if query == pb[i][0]:
                check = i
                temp.append(pb[i])

    elif choice == 2:
        query = int(
            input("Please enter the number of the contact you wish to search: "))
        for i in range(len(pb)):
            if query == pb[i][1]:
                check = i
                temp.append(pb[i])

    else:
        print("Invalid search criteria")
        return -1

    if check == -1:
        return -1
        # returning -1 indicates that the query did not exist in the directory
    else:
        display_all(temp)
        return check


def display_all(pb):
    if not pb:
        print("List is empty: []")
    else:
        for i in range(len(pb)):
            print(pb[i])


def thanks():
    print("********************************************************************")
    print("Thank you for using our app.")
    print("Please visit again!")
    print("********************************************************************")
    sys.exit("Goodbye!!!")


print("********************************************************************")
print("Hello dear user, welcome to our phonebook!")

print("********************************************************************")

ch = 1
pb = initial_phonebook()
while ch in (1, 2, 3, 4, 5):
    ch = menu()
    if ch == 1:
        pb = add_contact(pb)
    elif ch == 2:
        pb = remove_existing(pb)
    elif ch == 3:
        pb = delete_all(pb)
    elif ch == 4:
        d = search_existing(pb)
        if d == -1:
            print("The contact does not exist. Please try again")
    elif ch == 5:
        display_all(pb)
    else:
        thanks()


with open('PHONEBOOK.json', 'w') as file_object:
    json.dump(PHONEBOOK, file_object)
