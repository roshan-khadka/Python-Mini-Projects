#: Rock, Paper, Scissors game

import random

ties, wins, losses = 0,0,0

while True:
    options = ["rock", "paper", "scissor"]
    computer_choice = random.choice(options)
    user_choice = input("Please type your choice(rock, paper, scissor): ").lower()

    if user_choice == computer_choice:
        print(f"You choose {user_choice} vs {computer_choice}. Its a tie.")
        ties += 1
    elif user_choice == "rock":
        if computer_choice == "paper":
            print(f"You choose {user_choice} vs {computer_choice}. You loose.")
            losses += 1
        else:
            print(f"You choose {user_choice} vs {computer_choice}. You win.")
            wins += 1
    elif user_choice == "paper":
         if computer_choice == "rock":
            print(f"You choose {user_choice} vs {computer_choice}. You win.")
            wins += 1
         else:
            print(f"You choose {user_choice} vs {computer_choice}. You loose.")
            losses += 1
    elif user_choice == "scissor":
        if computer_choice == "rock":
            print(f"You choose {user_choice} vs {computer_choice}. You win.")
            wins += 1
        else:
            print(f"You choose {user_choice} vs {computer_choice}. You loose.")
            losses += 1
    play_again = input("Do you want to play again?(Yes/No): ").lower()
    if play_again == "yes":
        continue
    else:
        break
print(f"The result of your game is {wins} wins, {losses} losses,and {ties} ties.")
print("The end!")
