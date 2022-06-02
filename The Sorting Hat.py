import random 
import time
def Sorting_Hat():
    Sorting = input("What is your name?: ")
    # The random number
    if Sorting == 'Alec':
        print('Ah hello')
        print("Hmm you might belong in...")
        num = random.randint(1,4)
        # The houses 
        print(num)
        if num == 1:
            print("You are in...Gryffindor! ")
            time.sleep(1)
            print ("Ah Gryffindor!. The bravest of the houses, also the house of the once great Albus Dumbledore!")
        elif num == 2:
            print("You are in...Hufflepuff! ")
            time.sleep(1)
            print("Ah Hufflepuff!. The most humble of the houses, also the house of Helga Hufflepuff!, the houses founder")
        elif num == 3:
            print("You are in...Ravenclaw! ")
            time.sleep(1)
            print("Ah Ravenclaw!. The most clever of the houses, also the house of the amazing Luna Lovegood! ")
        elif num == 4:
            print("You are in...Slytherin!")
            time.sleep(1)
            print("Ah Slytherin...the most evil of the houses, home to Tom Marvolo Riddle or also known as He who must not be named... ")

Sorting_Hat()