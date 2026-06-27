import random 

number = random.randint(0,100)
print(number)
while True:

  while True:

    try:

      guess = int(input("Enter your guess(0-100): "))
      if guess in range(0,101):
        break
      else:
        raise ValueError
    except ValueError:
      print("Please enter a valid number between(0-100)!")

  if guess > number:
    print("Too high!")
  elif guess < number:
    print("Too low!")
  elif guess == number:
    print("Wahooooo! You got it !")
    break