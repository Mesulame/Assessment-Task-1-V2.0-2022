#Generate random integer value
import random
#SET number to random
number = random.randint(1, 10)

#GET player_name
player_name = input("Hello, What's your name?")
#SET number_of_guesses to 0
number_of_guesses = 0
#DISPLAY 'Okay player_name I am Guessing a number between 1 and 10'
print('okay! '+ player_name+ ' I am Guessing a number between 1 and 10:')
#DO while number_of_guesses < 5
while number_of_guesses < 5:
#GET player_name guess
    guess = int(input())
#SET number_of_guesses to +=1
    number_of_guesses += 1
#IF guess is less than number THEN display 'Your guess is too low'
    if guess < number:
        print('Your guess is too low')
#IF guess is higher than number THEN display 'Your guess is too high'
    if guess > number:
        print('Your guess is too high')
#IF guess equals TRUE than END while 
    if guess == number:
        break
#IF guess equals TRUE THEN display 'You guessed the + number in number_of_guesses + tries'
if guess == number:
    print('You guessed the number in ' + str(number_of_guesses) + ' tries!')
#ELSE display 'You did not guess the number, The number was + number'
else:
    print('You did not guess the number, The number was ' + str(number))
