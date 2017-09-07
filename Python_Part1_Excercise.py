#Hello you
name = input("what is your name? ");
print("hello " + name);


#HELLO YOU
print("hello " + name.upper());

#Day of the week
day = int(input("day (0-6)?"));
if(day == 0):
	print("Sunday");
elif(day ==1):
	print("Monday");
elif(day ==2):
	print("Tuesday");
elif(day ==3):
	print("Wednesday");
elif(day ==4):
	print("Thursday");
elif(day ==5):
	print("Friday");
elif(day ==6):
	print("Saturday");

if(day == 0 or day ==6):
	print("Sleep In");
else:
	print("Go to Work");



#Celsius to Fahrenheit

celciusDegree = int(input("Temperature in C? "));
fahrenheitDegree = str(celciusDegree * 1.8 + 32);
print(fahrenheitDegree + " F");


#Tip Calculator
#============================= need to get the dollar sign to work=======================
good = .20;
fair = .15;
bad = .10;
totalBill = int(input("Total Bill Amount? "));
levelOfService = input("Level of Service (good, fair, bad)?");
split = int(input("split how many ways?"));
if(levelOfService == "good"):
	tip_amount = totalBill * good;
	print(tip_amount);
	final_bill = (totalBill + tip_amount) /split;
	print(final_bill);
elif(levelOfService == "fair"):
	tip_amount = totalBill * fair;
	print(tip_amount);
	final_bill = (totalBill + tip_amount) /split;
	print(final_bill);
else:
	tip_amount = totalBill * bad;
	print(tip_amount);
	final_bill = (totalBill + tip_amount) /split;
	print(final_bill);




# 1 to 10
num = 1;
while(num<=10):
	print(num);
	num+=1;

# How many coins

num_of_coins = 0;
counter = 0;
print("you have " + str(num_of_coins) + " coins");
while(counter == 0):
	print("do you want another one? (Y or N)");
	answer = input("> ");
	if(answer == "Y"):
		num_of_coins +=1;
		print("you have " + str(num_of_coins));
	else:
		print("bye");
		counter = -1;










