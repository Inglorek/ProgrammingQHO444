import random

def play_guess_number():
    min=int(input("Enter a number: "))
    max=int(input("Enter a number: "))


    secret_number=random.randint(min,max)

    print(f"i am thinking of a number between {min} and {max}.Can you guess what it is?")

    guess= None

    while guess != secret_number:
        guess=int(input("Enter a guess: "))

        if guess < secret_number:
            print("your guess is too low")
        elif guess > secret_number:
            print("your guess is too high")
        else:
                print("Congratulations, you guessed the number")

play_guess_number()




