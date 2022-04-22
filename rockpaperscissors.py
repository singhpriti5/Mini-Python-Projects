import random

user_wins=0
computer_wins=0
 
while True:
    user_input=input("Type Rock/Paper/Scissors or Q to Quit: ")
    if user_input.lower()=="q":
        print("Thanks for playing!")
        break
    elif user_input.lower()=="rock":
        user_input="R"
    elif user_input.lower()=="paper":
        user_input="P"
    elif user_input.lower()=="scissors":
        user_input="S"
    else:
        print("Invalid input. Try again.")
        continue
    computer_input=random.choice(["R","P","S"])
    if user_input==computer_input:
        print("It's a tie!")
    elif user_input=="R" and computer_input=="S":
        print("You win!")
        user_wins+=1
    elif user_input=="S" and computer_input=="P":
        print("You win!")
        user_wins+=1
    elif user_input=="P" and computer_input=="R":
        print("You win!")
        user_wins+=1
    else:
        print("You lose!")
        computer_wins+=1
    print("You:",user_wins,"Computer:",computer_wins)
    print("")
    
    