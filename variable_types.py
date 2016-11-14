# Today we're going to look at VARIABLES
# Here is a simple INT or Integer variable:

number = 9
print(type(number))   # print type of variable "number"

# FLOAT variables are numbers with decimal points:
float_number = 9.0
print (type(float_number))

# Here's a STRING variable:
foo = "hi there"

# Here we're changing it to an INT:
foo = 1000000

print (type(foo))

# What kind of variable is shopping?
shopping = ["Ham", "Eggs", "bread", "dogfood"]
print (type(shopping))

# It's a LIST variable!

# Here's how we get the first element of the list called shopping:
print(shopping[0])

# things is a list that contains another list, shopping

things = [ shopping, 'chemistry', 1997, 2000];


####################################
# Assign a new value to the 4th value in shopping, using things:
things[0][3] = "CatFood"

# Print some other values:

print(things[0][3])
print (shopping[3])
print(type(shopping[3]))
####################################

foo = "This is the new foo"

print(things[0])

print(foo)
