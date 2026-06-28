# ===== Quest 15: The Nested Riddle =====

# Ask the player to choose a direction; .lower() handles uppercase input
direction = input("Do you go 'left' or 'right'? ").lower()

if direction == "left":
    # Only ask the next question if the player chose left
    action = input("Do you 'swim' or 'wait'? ").lower()
    if action == "swim":
        # Only this specific path leads to treasure
        print("You dive in and discover a hidden treasure chest! You win!")
    else:
        # Any choice other than swim leads here
        print("You wait patiently, but nothing happens. The path grows cold.")
else:
    # Any direction other than left leads to this dead end
    print("You head right and find yourself at a dead end. Try a different path next time.")
