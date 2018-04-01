import sys
import re

__book = {}


def add():
    """Function adds a name (str) and a number (int) in the dict.
       Name and number need to be entered. Function checks if the amount
       of digits in number are 6 or 11.

    :raises: ValueError
    """

    key = input("Enter a name: ")
    if not key.isalpha():
        print("Name should be alphabetic.")
    else:
        try:
            number = int(input("Type phone number. It should contain 6 or 11 integers.\n"))
            low = re.search('^[1-9][0-9]{5}$', str(number))
            high = re.search('^[1-9][0-9]{10}$', str(number))
            if low or high:
                if key in __book:
                    __book[key].append(number)
                else:
                    __book[key] = [number]
                print('Contact added.')
            else:
                print("Number should contain 6 or 11 integers.")
        except ValueError:
            print("Number should contain integers only")


def help():
    """Function prints all commands user can input in the program."""

    print("Commands you may use:")
    for t in func_list:
        print(t)


def get():
    """Function asks user to enter a name and prints this name and
    number associated with it from the dict. If there is no such
    name in dict.keys, prints str."""

    name = input("Who are you looking for?\n")
    if name in __book.keys():
        for i in range(len(__book[name])):
            print('{}\t{}'.format(name, __book[name][i]))

    else:
        print("You don't have this contact yet.")


def exit():
    """Function calls built-in function exit()"""

    print("Terminating work..")
    sys.exit()


def delete():
    """Function deletes number from the phonebook."""

    name = input("Who's number would you like to delete?\n")
    if name in __book:
        del(__book[name])
        print("Contact deleted.")
    else:
        print("You don't have this contact.")


# creating a tuple of functions in the program
func_list = dir()
func_list = tuple(i for i in func_list if '__' not in i and i != 'sys' and i != 're')

while True:
    print("Enter a command or type 'help' for information: ")
    command = input()
    if command in func_list:
        f = globals()[command]
        f()
    else:
        print("It seems that you've made a mistake... I'll give you another chance :)")
