# Author: Gatete Irene Hodali
# Quest 14: The Logical Gatekeeper
# Concept: Logical Operators (and, or, not) - combining multiple conditions

age = int(input("Enter your age: "))
gold = int(input("How many gold coins do you have? "))

if age >= 18 and gold >= 20:
    print("Welcome! You may enter the club.")
else:
    if age < 18:
        print("Sorry, you must be at least 18 years old to enter.")
    elif gold < 20:
        print("Sorry, you need at least 20 gold coins to enter.")
