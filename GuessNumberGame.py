import random;
counter = 0;
secret_number = random.randint(1,10);
number_of_guesses = 5;
print(secret_number); #so i know what it is
print("I'm thinking of a number between 1 and 10");
while(counter == 0):
	print("You have " + str(number_of_guesses) + " guess(es) left");
	print("What's the number?");
	answer = raw_input(" >");
	if(number_of_guesses == 1):
		print("you lose the game");
		print("Do you want to play again? (Y or N)");
		play_again = raw_input(" >");
		if(play_again == "Y"):
			counter == 0;
			print("I'm thinking of a number between 1 and 10");
			number_of_guesses = 5;
		else:
			counter = -1;
	else:
		if(int(answer) < secret_number):
			print(answer + " is too low");
			number_of_guesses-=1;
		elif(int(answer) > secret_number):
			print(answer + " is too high");
			number_of_guesses-=1;
		else:
			print("Yes, you win!");
			print("Do you want to play again? (Y or N)");
			play_again1 = raw_input(" >");
			if(play_again1 == "Y"):
				counter == 0;
				print("I'm thinking of a number between 1 and 10");
			else:
				counter = -1;


