
# a function in python are called definitions, is a piece of code that can be called from 
# somewhere else. they are meant to be re-usable and to make things clea
# if you have complicated code, then you can break it into pieces to make
# eaiser to understand
# reapting your code is bad,
 # - copy and paste errors
 # - odd behavoior
 # - etc...

 # to declare a function in python you use "def"
 # function always has a ()

# this defines a function
def say_Hello():
	print("Hello");
 # this calls the function(tells python to run the code inside say_Hello def)
say_Hello();

#passing variable into functions are called arguments on the way in
# parameters once inside.
def say_Hello_with_name(name):
	print("hello, %s" % name);

say_Hello_with_name("Jamie")

# if you call a function with an argument but doesn't put an arugment inside, it will cause an error
# you can set a defualt for a parameter
def say_Hello_safe(name, in_class ="yes"):
	print("%s, %s is in the class" %(in_class, name));


#function always return a value
#return value is a function chance to send one and only one thing to whoever called it

def return_user_name(name):
	normalized_name = name.upper();
	return normalized_name;
print(return_user_name("Chris"));












