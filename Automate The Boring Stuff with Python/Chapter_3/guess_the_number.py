import random

print("I am thinking of a number between 1 and 20")
magic_number = random.randint(1, 20)

for i in range(1, 7):
    print("Take a guess: ")
    my_number = int(input())
    
    if my_number < magic_number:
        print("You are too low.")
    elif my_number > magic_number:
        print("You are too high.")
    else:
        break

if my_number == magic_number:
    print("Good Job! You made it!")
else:
    print("Badly :( , my number was " + str(magic_number))