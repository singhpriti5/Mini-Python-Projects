import random

top_of_range=input("Type a number:")

if top_of_range.isdigit():
    top_of_range=int(top_of_range)
    
if top_of_range<=0:
    print("You have to choose a number greater than 0")
    quit()    
else:
    print("Please print the number next time")
    quit()

random_number=random.randint(0,top_of_range)
guesses=0

while True:
    guesses+=1
    user_guess=input("Make a guess:")
    if user_guess.isdigit():
        user_guess=int(user_guess)

    else:
        print("Please type a number next time.")
        continue
    if user_guess==random_number:
        print("You guessed it!")
        break
    elif user_guess>random_number:
        print("Your guess is too high")
    else:
        print("Your guess is too low")

    print("You got it in", guesses, "guesses") 
