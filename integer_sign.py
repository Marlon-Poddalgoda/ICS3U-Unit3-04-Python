#!/usr/bin/env python3

# Created by Marlon Poddalgoda
# Created on December 2020
# This program identifies the sign of an integer

import random


def main():
    # this function identifies the sign of an integer

    print("This program reads and identifies integers.")

    # input
    user_integer = int(input("Enter a positive or negative integer: "))
    print("")

    # process
    if user_integer > 0:
        # output
        print("This integer is positive (+)")
    elif user_integer < 0:
        # output
        print("This integer is negative (-)")
    elif user_integer == 0:
        # output
        print("This integer is 0")
    else:
        # output
        print("Error, please enter an integer next time.")


if __name__ == "__main__":
    main()
