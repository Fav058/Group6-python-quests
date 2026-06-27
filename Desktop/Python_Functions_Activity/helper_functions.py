# Author: Favour

def validate_input(user_input):
    """
    Checks if the input is not empty and is a valid string.
    Returns True if valid, otherwise False.
    """
    if isinstance(user_input, str) and user_input.strip() != "":
        return True
    return False


def create_message(name, age):
    """
    Returns a greeting message with the user's name and age.
    """
    return f"Hello {name}, you are {age} years old!"