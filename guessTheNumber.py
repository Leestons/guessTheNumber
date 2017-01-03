import random, sys
parsed = False
difficulty = int(input('What number would you like to go up to? '))

def game():
	secretNumber = random.randint(1, difficulty)
	print('I am thinking of a number between 1 and ' + str(difficulty))
	while parsed == False:
		try:
			for guessesTaken in range(1,7):
				guess = int(input('Take a guess '))
				if guess < secretNumber:
					print('Your guess is too low')
				elif guess > secretNumber:
					print('Your guess is too high')
				else:
					break
			if guess == secretNumber:
				print('Good job! You guessed my number in ' + str(guessesTaken) + ' guesses!')
			else:
				print('The number I was thinking of was ' +str(secretNumber))
			replay = input('Press Y to play again, press any other key to quit: ')
			if replay == 'y':
				game()
			else:
				print('Goodbye!')
				sys.exit()
		except ValueError:
			print('Please enter a number')	

game()
