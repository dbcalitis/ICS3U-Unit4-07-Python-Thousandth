#!/usr/bin/env python3

# Created by: Daria Bernice Calitis
# Created on: Oct 2021
# This program prints all numbers from 1000 to 2000


def main():
    # This function prints all numbers from 1000 to 2000
    output = ""
    end_range = 2000

    # process & output
    for num in range(1000, end_range + 1):
        if num % 5 == 0:
            output = str(num)
        else:
            output += " " + str(num)

        if num % 5 == 4 or num == end_range:
            print(output)

    print("\nDone.")


if __name__ == "__main__":
    main()
