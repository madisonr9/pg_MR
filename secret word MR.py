import random

number = random.randint (0,3)

words = ["MONKEY","ABRACADABRA","CHURRO","HAT"]
hint1 = ["tail","magic","dessert","warm"]
hint2 = ["bananas","wand","cinnamon and sugar","for head during the winter"]

secretword = words[number]
guess = ""
counter = 1

while True:
    print("Guess the secret word")
    print("Type 'hint1', 'hint2', 'first letter', or 'give up' for answer.")
    guess = input().upper()

    if guess == secretword:
        print("Congrats! you guessed the secret word")
        print("It took you " + str(counter) + " guesses.")
        break

    elif guess == "HINT1":
        print( hint1[number] )

    elif guess == "HINT2":
        print( hint2[number] )

    elif guess == "FIRST LETTER":
        print( secretword[0] )

    elif guess == "GIVE UP":
        print("Wow you are super sad.The secret word was " + secretword)
        print("You failed " + str(counter) + " times. Play again!")
        break

    else:
        counter += 1
        print("Guess again")
        
        
