from random import randint

def randomGenerator(base,n):
    r=int(input(f"Enter a number from {base} to {n}:"))
    rand=randint(base,n)
    print("The randomly generated number is",rand)
    if r > rand:
        print("The entered number is greater than the randomly generated number :(")
    if r < rand:
        print("The entered number is smaller than the randomly generated number :(")
    if r == rand:
        print("Wow you must be the luckiest person in the world. You guessed it right :)")

while True:
    print("--------------RANDOM NUMBER GENERATOR GAME-----------------")
    print("----------------------DIFFICULTY---------------------------")
    print("1. Easy difficulty  (For people who just want to try the game)")
    print("2. Medium difficuly (For people who wants a challenge)")
    print("3. Hard difficulty  (For people who think they have the craziest luck in the world)")
    choice=int(input("Enter your choice (1-3):"))
    if choice==1:
        randomGenerator(0,10)
    elif choice==2:
        randomGenerator(0,100)
    elif choice==3:
        randomGenerator(0,1000)
    else:
        print("Wrong input entered...Please try again")
    ch=input("Continue? Enter 'y' to continue or any other key to exit the game...")
    if ch == 'y' or ch == 'Y':
        continue
    else:
        exit()