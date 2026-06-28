secret_code = "42"
max_attempts = 3

for attempt in range(1, max_attempts + 1):
    guess = input(f"Attempt {attempt}/{max_attempts} - Enter the secret code: ")
    
    if guess == secret_code:
        print("Access granted! You cracked the code!")
        break
    else:
        remaining = max_attempts - attempt
        if remaining > 0:
            print(f"Wrong code. You have {remaining} attempt(s) left.")
        else:
            print("Access denied. You've used all your attempts. The code was 42.")
