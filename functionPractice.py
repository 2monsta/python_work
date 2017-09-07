
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

