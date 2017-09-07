# # print "Hello World"
# # print ("Hello W0rld");


# # vaiable - string, letters, numberr, or any other stuff you can make with a keyboard.
# #a variable is just a fast way to refer to something else. It DOES NOT make the computer faster.
# #it makes the cmoputer slower
# #In python, there is no declartion, it is dynamic, it exists when you make it.

# theBestClassInAtlanta = "This Class";
# name = "Jason Li"


# #Data Type
# #String - english stuff, for people to read
# #Numbers - something with digits and the stuff that goes with them (- or . or e)
# # A floats, integers
# 	# -- float has a . in it
# 	# -- integer - has no .
# # Boolean -- true or false, 1 or 0, off or on
# # List(arrays) -- list of things, a single variable with a bunch of like parts
# # dictionary -- variable of variables
# # Objects -- we will deal with this later

# name_1 = "Jason" + " Li"; # + is a concateanate symbol with strings
# first = "Jason";
# last = "Li";
# full_name = first + " " +last;

# print full_name;


# meaning_of_life = 20+2; # + is not an addition symbol

# forty_two = 84/2;
# forty_two = 21 *2;
# one = 83 % 2;
# print one;

# # cannot add different data types such as strings with numbers

# #By argument
# first_name = "Jason";
# last_name = "Li";
# #Intermingle english and vars : way 1
# print "hello {} {}".format(first_name, last_name);

# # Float
# pi = 3.14
# print type(pi);

# #booleans
# the_truth = True;
# print type(the_truth);

# # order of opertions 
#  #() overrides everything. Use ()
# print("what is your name");
# name = raw_input(">");
# print("your name is %s" %name);


# #CONDITIONALs

# # == 	- compare left and right
# # === - compare left and right as well as data type
# # 16 = "16"	True	
# # 16 === "16" False

# if(16 == 16):
# 	print("True");
# if(1 == 2):
# 	print("True");
# else:
# 	print("False");

# Random is a python Module that comes with python
import random;
rand_number = random.randint(1,10);
print(rand_number)


#Loops
# a while loop, will run forever until the condition is met
keep_going = True;
while(keep_going):
	get_answer = raw_input("please hit any key");
	keep_going = False;
print("you are no longer in the loop");
