import random
from enum import Enum

import sys


class RPS(Enum):
    rock = 1
    paper = 2
    scissors = 3

print("welcome to rock paper and scissors")
choices = input("1. rock🪨\n2. paper📄\n3. scissors✂️\n ")
choice = int(choices)

computer_choice = random.choice(["rock 🪨", "paper 📄", "scissors ✂️"])
print("you chose "+str(RPS(choice)).replace("RPS.rock", "rock 🪨").replace("RPS.paper", "paper 📄").replace("RPS.scissors", "scissors ✂️"))
print("python chose",computer_choice)

if choice == 1 and computer_choice == "scissors ✂️":
    print("you win 🎊")
elif choice == 2 and computer_choice == "rock 🪨":
    print("you win 🎊")
elif  choice == 3 and computer_choice == "paper 📄":
    print("you win 🎊")
elif choice == 1 and computer_choice == "rock 🪨":
    print("it`s a draw 🤝")
elif choice == 2 and computer_choice == "paper 📄":
    print("it`s a draw 🤝")
elif choice == 3 and computer_choice == "scissors ✂️":
    print("it`s a draw 🤝")
else:
    print("Python Win 🐍")