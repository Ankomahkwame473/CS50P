import random
x = True
while x == True:
    try:
        level = int(input("Level: "))
        if level > 0:
            number = random.randint(1,level)
            while True:
                guess = input("Guess: ")
                if int(guess) <= 0:
                    pass
                elif int(guess) > number:
                    print("Too large!")
                elif int(guess) < number:
                    print("Too small!")
                elif int(guess) == number:
                    print("Just right!")
                    x = False
                    break
        else:
            pass
    except ValueError:
        pass
