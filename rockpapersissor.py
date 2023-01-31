import random_1

user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissor"]
options[0]
while True:
    user_input = input("Type Rock/ Paper/ Scissors or Q to quit: ").lower()
    if user_input == "q":
        break
    
    if user_input not in options:
        continue

    random_number = random_1.randint(0, 2)
    # rock:0, paper: 1, scissors: 2 
    computer_pick = options[random_number]
    print("computer picked", computer_pick + ".")

    if user_input == "rock" and computer_pick == "scissors":
        print("Jeet gaye!! waah")
        user_wins += 1
        

    if user_input == "paper" and computer_pick == "rock":
        print("Jeet gaye!! waah")
        user_wins += 1
        

    if user_input == "scissors" and computer_pick == "paper":
        print("Jeet gaye!! waah")
        user_wins += 1
    
    elif user_input==computer_pick:
        print('Us bhai us...')
    else:
        print("nahi ho rha kya?? lol")
        computer_wins += 1


print("Waah!!", user_wins, "baar jeet gaye.")
print("Computer", computer_wins, "baar jeetaa.")
print("nikal!!")
