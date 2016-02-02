from random import randint


def begin():

	decision = input("Welcome to the guessing game!"
		     		 "Do you want to [G]uess number or [C]hoose a number and have the ai pick?"
		     		 "Type the letter in the brackets. ").lower()

	decision_maker(decision)
	
	
def decision_maker(decision):

	if decision == 'g':

		you_guess(decision)

	elif decision == 'c':

		while True:

			user_secret_number = convert_int(input("Type a number between 1 and 20 "
										   "for the computer to guess. "), decision)

			if user_secret_number > 20:

				print("Thats not a number between 1 and 20!")

			elif user_secret_number < 1:

				print("Thats not a number between 1 and 20!")

			elif 1 <= user_secret_number <= 20:

				break

		computer_guess(user_secret_number, decision)

	else:

		print("What did you say? That is not a valid command. Try again")
		begin()

def you_guess(decision):

	secret_number = randint(1, 20)
	guesses = 0

	while guesses < 4:

		user_guess = convert_int(input("Guess a number! > "), decision)

		if user_guess == secret_number:

			print("You win! You guessed my number")
			break

		elif user_guess > secret_number:

			wrong_guess('high')
			guesses += 1

		elif user_guess < secret_number:

			wrong_guess('low')
			guesses += 1

	else:

		print("You did not guess my number! The number was {}".format(secret_number))

def convert_int(user_input, decision):

	try:

		user_input = int(user_input)

		return user_input

	except ValueError:

		print("Thats not a number!")

		decision_maker(decision)

def wrong_guess(word):

	print("Wrong! You are too {}! Try again".format(word))

def computer_guess(user_secret_number, decision):

	computer_guesses = 0
	comp_guess = randint(1, 20)

	if comp_guess == user_secret_number:

		comp_victory(user_secret_number)

	else:

		print("The computer was wrong and guessed {}".format(comp_guess))

		smarter_comp(comp_guess, computer_guesses, user_secret_number)

def smarter_comp(comp_guess, computer_guesses, user_secret_number):

	all_guesses = []
	all_guesses.append(comp_guess)

	new_guess = comp_guess

	while computer_guesses < 4:

		feedback = input("Was the ai too [H]igh or too [L]ow? ")

		if feedback == 'h':

			new_guess = randint(0, new_guess)
			all_guesses.append(new_guess)

			if new_guess == user_secret_number:
			
				answers_file(all_guesses)
				comp_victory(user_secret_number)
				break

			else:
				
				print("The computer was wrong and guessed {}".format(new_guess))
				computer_guesses += 1
			
		elif feedback == 'l':

			new_guess = randint(new_guess, 20)
			all_guesses.append(new_guess)

			if new_guess == user_secret_number:

				answers_file(all_guesses)
				comp_victory(user_secret_number)
				break

			else:

				print("The computer was wrong and guessed {}".format(new_guess))
				computer_guesses += 1

	else:

		print("The computer was not able to guess your number! You win!")
		answers_file(all_guesses)

def comp_victory(user_secret_number):

	print("The computer guessed {}! Your number!"
		  "The computer wins!".format(user_secret_number))

def answers_file(all_guesses):

	with open('computer_guesses.txt', 'w') as f:

		f.write("These were the computer guesses: \n")

		for guess in all_guesses:

			f.write(str(guess) + ' ')

		f.close()

begin()