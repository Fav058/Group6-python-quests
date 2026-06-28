# Author: Gatete Irene Hodali
# Quest 24: The Master Spell
# Concept: Calling a function from within another function

def ask_for_age():
    """Asks the user for their age and returns it as an integer."""
    age = int(input("Please enter your age: "))
    return age

def can_they_vote(age):
    """Receives an age and prints whether the person can vote."""
    if age >= 18:
        print(f"At {age} years old, you ARE eligible to vote. Make your voice heard!")
    else:
        print(f"At {age} years old, you are NOT yet eligible to vote. You'll be able to in {18 - age} year(s).")

# Call ask_for_age() first, then pass its result to can_they_vote()
user_age = ask_for_age()
can_they_vote(user_age)
