direction = input("Do you go 'left' or 'right'? ").lower()

if direction == "left":
    action = input("Do you 'swim' or 'wait'? ").lower()
    if action == "swim":
        print("You dive in and discover a hidden treasure chest! You win!")
    else:
        print("You wait patiently, but nothing happens. The path grows cold.")
else:
    print("You head right and find yourself at a dead end. Try a different path next time.")
