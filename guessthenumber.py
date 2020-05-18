import random

print("Guess the number!")
print("The number is between 0 to 100")
print("Choosing the number ...")

n = random.randint(0,100)

print("\nLet's get started it \nGuess the numeber\nYou have 10 attempts")

for i in range (10) :
    answer = input()
    answer = int(answer)
    if n == answer :
        print("You are correct!")
        break
    elif n > answer :
        print("The answer is to low")
    elif n < answer :
        print("The answer is to high")
    elif n < 0 or n > 100 :
        print("Invalid number")
    i += 1
    print("You have "+str(10-i)+" attempts left")
    if i == 10 :
        print("No more attempts left :(")
        break