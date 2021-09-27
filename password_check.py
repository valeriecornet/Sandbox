MIN_LENGTH = 6


def main():
    print("Password must be between 6 and 12 characters in length:")
    password = input("Enter password:")
    length = len(password)
    while length < MIN_LENGTH:
        print("Invalid password")
        password = input("Enter password:")
        length = len(password)
    print(length * "*")


main()
