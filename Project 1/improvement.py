import random

# Generate computer's choice
computer = random.choice([-1, 0, 1])

# Get user's input and validate
user = input("Enter your choice (s for Snake, w for Water, g for Gun): ").strip().lower()
dic = {"s": 1, "w": -1, "g": 0}
reverse_dic = {1: "Snake", -1: "Water", 0: "Gun"}

if user not in dic:
    print("Invalid choice. Please enter 's', 'w', or 'g'.")
else:
    you = dic[user]
    print(f"User chose {reverse_dic[you]}")
    print(f"Computer chose {reverse_dic[computer]}")

    # Determine the result
    if computer == you:
        print("It's a draw!")
    else:
        outcome = {
            (-1, 1): "You win!",
            (-1, 0): "You lose!",
            (1, -1): "You lose!",
            (1, 0): "You win!",
            (0, -1): "You win!",
            (0, 1): "You lose!"
        }
        print(outcome.get((computer, you), "Something went wrong!"))
