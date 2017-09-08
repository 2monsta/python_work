#UPPER CASE
string_name = raw_input("Anything?")
print(string_name.upper());

#Capitalize
string_name = raw_input("Anything?")
a = string_name.capitalize();
print(a);

#Reverse
string_name = raw_input("Anything?");
a = string_name[::-1];
print(a);


#leetspeak
string_name = raw_input("Anything?").upper();
string_name_list = list(string_name);
print(string_name_list);
for i in range(0,len(string_name_list)):
	if(string_name_list[i] == "A"):
		string_name_list[i] = str(4);
	elif(string_name_list[i] == "E"):
		string_name_list[i] = str(3);
	elif(string_name_list[i] == "G"):
		string_name_list[i] = str(6);
	elif(string_name_list[i] == "I"):
	 	string_name_list[i] = str(1);
	elif(string_name_list[i] == "O"):
		string_name_list[i] = str(0);
	elif(string_name_list[i] == "S"):
	 	string_name_list[i] = str(5);
	elif(string_name_list[i] == "T"):
	 	string_name_list[i] = str(7);
print(string_name_list);
string_name_joined = "".join(string_name_list);
print(string_name_joined);