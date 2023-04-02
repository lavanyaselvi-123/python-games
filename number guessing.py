import random

name=input("Hello, Welcome to Number guessing\nWhat is your name?\n")
start=True

while start:
    number=random.randint(1,10)
    ans=input("Do you want to continue(Yes/No)?\n")
    if ans.lower()=='yes':
        print("Please enter the number between 1 and 10")
        number_of_guesses=0
        while number_of_guesses<5:
            guess=int(input())
            number_of_guesses+=1
            if guess<number:
                print("Your guessing is too low")
            elif guess>number:
                print("Your guessing is too high")
            elif guess==number:
                print("You guessed the number in "+str(number_of_guesses)+"tries")
                break
        print("You didn't guess the number, the number is "+str(number))
    else:
        print("Thanks for Participating\n")
        start=False    

