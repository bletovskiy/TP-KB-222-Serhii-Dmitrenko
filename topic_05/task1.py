import random

options = ["stone", "scissors", "paper"]

while True:
    userChoice = input("Your choice 'stone', 'scissors', 'paper': ").strip().lower()
    
    if userChoice not in options:
        print("Invalid choice.")
    else:
        break

compChoice = random.choice(options)

print(f"Your choice: {userChoice}")
print(f"Computer choice: {compChoice}")

results = {
    ("stone", "scissors"): "You win!",
    ("scissors", "paper"): "You win!",
    ("paper", "stone"): "You win!",
    ("scissors", "stone"): "Computer wins!",
    ("paper", "scissors"): "Computer wins!",
    ("stone", "paper"): "Computer wins!",
}

if userChoice == compChoice:
    print("Tie")
else:
    result = results.get((userChoice, compChoice))
    print(result)