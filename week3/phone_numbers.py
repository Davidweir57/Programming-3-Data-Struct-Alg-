#!/usr/bin/env python3

def main():

    phonebook = {}

    print("Enter a name and number, or a name and ? to query (!! to exit)")

    command = input()

    while command != "!!":
        name, query = command.split()

        if (name not in phonebook) and (query != "?"):
            phonebook[name] = query

        elif (name in phonebook) and (query != "?"):
            phonebook[name] = query

        elif (name in phonebook) and (query == "?"):
            print("{} has number {}".format(name, phonebook[name]))

        elif (name not in phonebook) and (query == "?"):
            print("Sorry, there is no {}".format(name))

        command = input()

    print("Bye")

if __name__ == '__main__':
    main()