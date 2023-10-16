import random

options = ["stone", "scissors", "paper"]

while (userChoice := input("Your choice 'stone', 'scissors', 'paper': ").strip().lower()) not in options:
    print("Invalid choice.")

compChoice = random.choice(options)

print(f"Your choice: {userChoice}")
print(f"Computer choice: {compChoice}")

results = {("stone", "scissors"): "You win!", 
           ("scissors", "paper"): "You win!", 
           ("paper", "stone"): "You win!"}

result = "Tie" if userChoice == compChoice else results.get((userChoice, compChoice), "Computer wins!")
print(result)