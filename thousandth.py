#!/usr/bin/env python3

# Created by: Daria Bernice Calitis
# Created on: Oct 2021
# This program prints all numbers from 1000 to 2000

import constants


def main():
    # This function prints all numbers from 1000 to 2000
    output = ""

    # process & output
    for num in range(1000, constants.END_RANGE + 1):
        if num % 5 == 0:
            output = str(num)
        else:
            output += " " + str(num)

        if num % 5 == 4 or num == constants.END_RANGE:
            print(output)

    print("\nDone.")


if __name__ == "__main__":
    main()
