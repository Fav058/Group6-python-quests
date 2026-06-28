# Author: Gatete Irene Hodali
# Quest 28: The Adventure Begins
# Concept: Text-based "Choose Your Own Adventure" using functions with at least 2 endings

def start():
    """The starting location of the adventure."""
    print("\n========================================")
    print("   WELCOME TO THE LAND OF KIGALI QUEST")
    print("========================================")
    print("\nYou stand at the edge of a mysterious forest.")
    print("Two paths lie before you.")
    print()
    choice = input("Do you go LEFT towards the ancient temple, or RIGHT towards the dark cave? (left/right): ").strip().lower()

    if choice == "left":
        ancient_temple()
    elif choice == "right":
        dark_cave()
    else:
        print("You hesitate too long and a friendly guide appears...")
        start()

def ancient_temple():
    """Location: The Ancient Temple."""
    print("\n--- The Ancient Temple ---")
    print("You enter a grand temple. A glowing chest sits in the center.")
    print("But a riddle is carved on the door: 'What has keys but no locks?'")
    print()
    answer = input("Your answer: ").strip().lower()

    if answer == "a piano" or answer == "piano":
        ending_victory()
    else:
        print("\nThe door seals shut. You are trapped... for now.")
        print("You notice a hidden lever on the wall.")
        choice = input("Do you pull the lever? (yes/no): ").strip().lower()
        if choice == "yes":
            print("\nA secret passage opens! You escape safely into the forest.")
            start()
        else:
            ending_trapped()

def dark_cave():
    """Location: The Dark Cave."""
    print("\n--- The Dark Cave ---")
    print("You cautiously enter the cave. It's dark but you spot two tunnels.")
    print("One smells of fresh air. The other echoes with distant gold coins clinking.")
    print()
    choice = input("Do you follow the FRESH AIR or the GOLD COINS? (air/gold): ").strip().lower()

    if choice == "air":
        print("\nYou follow the fresh air and emerge on the other side of the mountain.")
        ending_victory()
    elif choice == "gold":
        print("\nYou rush toward the coins but fall into a pit!")
        ending_trapped()
    else:
        print("You stand still, unsure. A bat startles you and you run back to the entrance.")
        start()

def ending_victory():
    """ENDING 1 - Victory!"""
    print("\n" + "=" * 40)
    print("  *** ENDING 1: HERO OF KIGALI QUEST ***")
    print("=" * 40)
    print("\nCongratulations, brave adventurer!")
    print("You have conquered the quest and returned home a legend.")
    print("Songs will be sung of your courage. 🎉")
    print()

def ending_trapped():
    """ENDING 2 - Game Over."""
    print("\n" + "=" * 40)
    print("   *** ENDING 2: GAME OVER ***")
    print("=" * 40)
    print("\nYou are trapped deep within the land of Kigali Quest.")
    print("Perhaps wisdom comes from trying again...")
    print()
    retry = input("Would you like to try again? (yes/no): ").strip().lower()
    if retry == "yes":
        start()
    else:
        print("\nFarewell, adventurer. Until next time. 👋")

# --- Start the game ---
start()
