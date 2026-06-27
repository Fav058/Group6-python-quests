while True:

  try:
    
    score = int(input("Enter the score(0-100): "))
    if score in range(0,101):
      break
    else:
      raise ValueError
  
  except ValueError:
    print("Please enter a valid number between(0-100)")

if score in range(90,101):
  print("A")

elif score in range(80,90):
  print("B")

elif score in range(70,80):
  print("C")

else:
  print("Needs Improvement")
