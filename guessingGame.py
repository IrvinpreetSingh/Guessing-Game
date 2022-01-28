import random
number = random.randint(1,9)
guess = int(input("Guess any number between 1 to 9 :"))
chances = 0
while chances < 5:
    if guess == number:
        print("CONGRATULATIONS YOU WON ")
        break
if not chances < 5:
    print("YOU LOSE !!! The number is : ", number)

