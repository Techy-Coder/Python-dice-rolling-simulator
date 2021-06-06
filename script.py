# Importing the modules
from random import randint
# Declaring the minimum and maximum
minimum = 1
maximum = 6
# Repeating answer
repeat = "y"
# The loop
while repeat == "y":
    result = randint(minimum, maximum)
    if result == 1:
        print(" _____\n|     |\n|  o  |\n|     |\n|_____|")
        print("\n")
    elif result == 2:
        print(" _____\n|o    |\n|     |\n|    o|\n|_____|")
        print("\n")
    elif result == 3:
        print(" _____\n|o    |\n|  o  |\n|    o|\n|_____|")
        print("\n")
    elif result == 4:
        print(" _____\n|o   o|\n|     |\n|o   o|\n|_____|")
        print("\n")
    elif result == 5:
        print(" _____\n|o   o|\n|  o  |\n|o   o|\n|_____|")
        print("\n")
    elif result == 6:
        print(" _____\n|o   o|\n|o   o|\n|o   o|\n|_____|")
        print("\n")
    repeat = input("Want to roll the dice again? (y/n) ")
    print("\n")
