import random

user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissor"]


while True:
    user_input = input("Type Rock/Paper/scissor or Q to quit: ").lower()
    if user_input == "q":
        break
    
    if user_input not in options:
        print("Please enter valid")
        continue

    random_number = random.randint(0,2)
    # 0 = rock, 1 = paper, 2 = scissor
    
    computer_pick = options[random_number]
    print("Computer Picked ", computer_pick + ".")
    
    if user_input == "rock" and computer_pick == "scissor":
        print("You won!!")
        user_wins += 1
        continue
       
    elif user_input == "paper" and computer_pick == "rock":
        print("You won!!")
        user_wins += 1
        continue
       
    elif user_input == "scissor" and computer_pick == "paper":
        print("You won!!")
        user_wins += 1
        continue
    
    else:
        print("You lost")
        computer_wins += 1 

print("You won ", user_wins, "times")
print("Computer won ", computer_wins, "times")

print("Goodbye!!")