# student1 = "Mikayla";
# student2 = "Jennifer";
# student3 = "Nikolas";
# student4 = "Zack";

# a list is a single variable with a bunch of numbered (index) parts.
# an index, in a list, is always a number ( integer)
# a list is amde with []. Every element is separated by a ,
students = [
	"Mikayla",
	"Jennifer",
	"Nikolas",
	"Zach"
]

atlanta_teams = [
	'falcons',
	'braves',
	'hawks',
	'thrashers',
	'atlanta_united'
]
# print(atlanta_teams);
# #Remove a list
# atlanta_teams.pop();
# print(atlanta_teams);
#we have another team
# atlanta_teams.append("Atl_united");
# print(atlanta_teams);
atlanta_teams_length = len(atlanta_teams);
for i in range(0, atlanta_teams_length - 1):
	#Check to see if the ith element (the one we are on) is thrasher
	# before we assume there's is an ith element, let's try so we can have a crash test
	# try:
		if(atlanta_teams[i] == "thrashers"):
			atlanta_teams.pop(i);
	# except:
	# 	print("bad index");
print(atlanta_teams);


# atlanta_teams.pop(3);
# print(atlanta_teams);



# split turns a string into a list._
# it expects a "delimiter" which is what it's supposed to use to break up the elements in the string

teams_as_a_string = "falcons, braves, hawks, atl united";
print(teams_as_a_string);
teams_as_as_list = teams_as_a_string.split(",")

print(teams_as_as_list);


# Lists also have a sort method.
# beware, sort will change the list.
teams_as_as_list.sort();
print(teams_as_as_list);

# sorted will sort the list, but will not change the list
# instead, it returns the sorted list

sorted_atlanta_teams = sorted(atlanta_teams);


#if you want to copy a part of the list, you can use [x:y]
# this will create a copy of the array, it will not change the original
#it will start at Xth element, and will stop at the Yth element(not inclusive);
#can print out all but the first which means [1:] if you do not pass the end argument, it will print all but the first

#to delete an index, you can use the remove method
#  alternative to pop(), you can provide the element instead of the index

atlanta_teams.remove("braves");

# insert....we can insert an element, wherever we want;

#====================
#list methods
# 1) sorted --makes a copy of the array and return a copy of it
# 2) .sort --change the array to the sorted
# 3) .pop --removes index from the array, can pass an argument to remove the specific one but if not then default is last
# 4) .split() -- split the array into different thing by (",")
# 5) .reverse() --reverse the array
# 6) .append() -- adds to the end of the element
# 7) [x:y]  or slice() in another language make a copy of the some part of the list you can use this syntax
# 8) remove() -- removes all element that equals the argument
# 9) insert -- taking 2 arguments, first where the index and second what you want it to be. 
