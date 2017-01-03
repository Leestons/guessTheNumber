import random, sys
parsed = False

def game():
	secretNumber = random.randint(1, 20)
	print('I am thinking of a number between 1 and 20.')
	
	#Ask the player to guess 6 times
	while parsed == False:
		try:
			for guessesTaken in range(1, 7):
				print('Take a guess.')
				guess = int(input())
				
				if guess < secretNumber:
					print('Your guess is too low.')
				elif guess > secretNumber:
					print('Your guess is too high.')
				else:
					break # This is the correct answer!
				
			if guess == secretNumber:
				print('Good job! You guessed my number in ' + str(guessesTaken) + ' guesses!')
			else:
				print('Nope. The number I was thinking of was ' + str(secretNumber))
			print('Press Y to play again, press any other key to exit')
			response = input()
			if response == 'y':
				game()
			else:
				print('Goodbye!')
				sys.exit()
		except ValueError:
			print('Please enter a number')
game()

	

