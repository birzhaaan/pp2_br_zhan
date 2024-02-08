import random
def Guess_the_number():
    print("Hello! What is your name?")
    name = input()

    print("Well,", name, " I am thinking of a number between 1 and 20.")
    count = 0
    a = random.randint(1,20)

    while True:
        print("Take a guess.")
        san = int(input())
        count+=1

        if a>san:
            print("Your guess is too low.")
        elif a<san:
            print("Your guess is too high.")
        else:
            print("Good job,", name,"! You guessed my number in ", count, "guesses!")
            break


Guess_the_number()