number = 9
guess_count = 0
guess_limit = 3

while guess_count < guess_limit:
    guess = int(input("Guess: "))
    guess_count += 1
    if guess == number:
        print("you won")
        break
else:
    print("max limit reached")


"""
The else statement above works only if the while loop completes without breaking it.
Once it is broken using break statement, the else will not be implemented
"""