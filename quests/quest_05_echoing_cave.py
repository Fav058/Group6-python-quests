# ===== Quest 5: The Echoing Cave =====

# Set the player's starting health to 100
player_health = 100
print(f"Starting health: {player_health}")

# A monster attacks: subtract 25 from health
# We reassign the same variable to update it
player_health = player_health - 25
print(f"A monster attacks! Health after attack: {player_health}")

# Player finds a potion: add 10 to recover some health
player_health = player_health + 10
print(f"You found a potion! Final health: {player_health}")
