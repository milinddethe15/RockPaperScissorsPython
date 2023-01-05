import random
import os
comp_point = 0
user_point = 0

def comp_wins():
    global comp_point
    comp_point = comp_point + 1

def user_wins():
    global user_point
    user_point = user_point + 1

def view_point():
    print(f"{name}'s points: {user_point} \nComputer's points: {comp_point}")

print("ROCK PAPER SCISSORS \n#####GET READY#####")
name = input("Enter your name: ")
os.system('cls')
while True:
    print("For rock, enter 'r' or 'R'")
    print("For paper, enter 'p' or 'P'")
    print("For scissor, enter 's' or 'S'")
    choices = ['s', 'r','p']
    user = input("Enter your choice: ").lower()
    comp = random.choice(choices)
    while(user not in choices):
        print("Invalid choice \nEnter again")
        user = input("Enter your choice: ").lower()
    print(f"{name}'s choice is {user}")
    print(f"Computer's choice is {comp}")

    if user == comp:
        print("It's tie")
    if user == "s" and comp == "r":
        comp_wins()
    if user == "s" and comp == "p":
        user_wins()
    if user == "r" and comp == "s":
        comp_wins()
    if user == "r" and comp == "p":
        comp_wins()      
    if user == "p" and comp == "r":
        user_wins()      
    if user == "p" and comp == "s":
        comp_wins()    
    view_point()   

    again = input("Do you want to play again?(y/n) ")
    if again =="n" or again == "N":
        break 
    elif again =="Y" or again =="y":
        os.system('cls')
    
print("GAME OVER!!")
os.system("taskkill /f /im cmd.exe")