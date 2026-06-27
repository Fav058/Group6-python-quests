while True:

  try:
    score = int(input("Enter the score(0-100): "))
    break
  
  except ValueError:
    print("Please enter a valid number between")

if score in range(90,101):
  print("A")

elif score in range(80,90):
  print("B")

elif score in range(70,80):
  print("C")
  
else:
  print("Needs Improvement")
