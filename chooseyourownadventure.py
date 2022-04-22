name=input("Enter your name:")
print("Hello",name,"!"
"Welcome to the game")
print("")
print("You are in a dark room.")
print("There is a door to your right and left.")
print("Which one do you take?"
"")
choice=input("Enter R for right or L for Left:")
if choice=="R":
    print("You have chosen the right door.")
    print("There is a giant bear here eating a cheese cake.")
    print("What do you do?")
    print("")
    print("1. Take the cake.")
    print("2.Scream at the bear.")
    print("")
    choice=input("Enter 1 or 2:")
    if choice=="1":
        print("The bear eats your face off. Good job!")
    elif choice=="2":
        print("The bear eats your legs off.Good job!")
    else:
        print("Well,doing %s is probably better.Bear runs away."%choice)
elif choice=="L":
        print("You have chosen the left door.")
        print("There is giant spider here eating pizza.")
        print("What do you do?")
        print("")
        print("1. Take the pizza.")
        print("2.pass out.")
        print("")
        choice=input("Enter 1 or 2:")
        if choice=="1":
            print("The spider bites your face off.Good job!")
        elif choice=="2":
            print("The spider abducts you.Good job!")
        else:
            print("Well,doing %s is probably better.Spider runs away."%choice)
else:
    print("You stumble around and fall on a knife and die.Good job!")
    print("")
    print("Game Over")
    print("")






    



        
    










