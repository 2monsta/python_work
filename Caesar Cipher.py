
# number_to_shift = 13;
alpha_list = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
print("enter a letter?")
user_input = raw_input(">");
print("enter a number to shift");
number_to_shift= int(raw_input(">"));
user_input_list = list(user_input);




#looping through the user input
for i in range(0, len(user_input_list)):
	#looping through the alpha_list
	for j in range(0, len(alpha_list)):
		if(user_input_list[i] == " "):
			continue;
		else:
		#find if the user input is the same as the alpha_list value
			if(user_input_list[i] == alpha_list[j]):
				#if it is equal, add the index value of j to number of shift
				shift = j + number_to_shift;
				#if shift is greater than 26, 
				if(shift >= 26):
					#minues 26 to get it within range
					shift -=26;
				#make the index value of user input the same as the moved value
				user_input_list[i] = alpha_list[shift];
				break;
decodedWord = "".join(user_input_list);
print(decodedWord)