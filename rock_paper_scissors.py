import random
print("welcome to rock paper and scissors")
choices = input("1. rock\n2. paper\n3. scissors\n ")
choice = int(choices)
computer_choice = random.choice(["rock", "paper", "scissors"])
print("you chose",choice)
print("python chose",computer_choice)