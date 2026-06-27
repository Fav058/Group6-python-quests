# Author: Favour

from helper_functions import validate_input, create_message


def get_user_info():
    while True:
        name = input("Enter your name: ")

        if not validate_input(name):
            print("Name cannot be empty.")
            continue

        age = input("Enter your age: ")

        if not age.isdigit():
            print("Age must be a number.")
            continue

        return name, int(age)


if __name__ == "__main__":
    name, age = get_user_info()

    message = create_message(name, age)

    print(message)