#This is a number guessing game


import random

guess='bugfix'

def GuessingGame():

    print ('Hello, what is your name?')

    name=input()

    print ('Well, '+name+', I am thinking of a number between 1 and 100. Lets see if you can guess it in 6 tries or less.')

    secretnumber=random.randint(1,100)

    for guessestaken in range(1,7):

        try:

            print ('Take a guess.')
            
            global guess
            
            guess=int(input())

            if guess<secretnumber:

                print('Your guess is too low.')

            elif guess>secretnumber:

                print('Your guess is too high.')

            elif guess==secretnumber:

                break #this is for correct guesses

        except ValueError:

            print ('Thats not a number. I hope you enjoyed that because it counted as a guess.')
            

    if guess==secretnumber:

        print ('Good job '+name+'! You guessed my number in '+str(guessestaken)+' guesses.')

        PlayAgain=input('Would you like to play again? Press Y or N and hit enter.').lower()

        if PlayAgain=='y' or PlayAgain=='yes':

            print ('Alright, lets try again!')
            GuessingGame()

        else:

            print ('Thanks for playing. See you later!')


    else:

        print('Better luck next time. The number I was thinking of was '+str(+secretnumber)+'.')

        PlayAgain=input('Would you like to play again? Press Y or N and hit enter.').lower()

        if PlayAgain=='y' or PlayAgain=='yes':

            print ('Alright, lets try again!')
            GuessingGame()

        else:

            print ('Thanks for playing. See you later!')

GuessingGame()
