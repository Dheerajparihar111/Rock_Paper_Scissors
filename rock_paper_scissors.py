import random
print("welcome to rock paper and scissors")
choices = input("1. rock\n2. paper\n3. scissors\n ")
choice = int(choices)
computer_choice = random.choice(["rock", "paper", "scissors"])
print("you chose",choice)
print("python chose",computer_choice)

if choice == 1 and computer_choice == "scissors":
    print("you win")
elif choice == 2 and computer_choice == "rock":
    print("you win")
elif choice == 3 and computer_choice == "paper":
    print("you win")
else:
    print("Python Win")