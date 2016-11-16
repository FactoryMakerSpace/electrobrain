#!/usr/bin/python

# Let's declare a couple of variables, foo and bar:
foo = 12
bar = 2

# Now we're going to test them, using "Greater Than" that uses this
# symbol: "2 > 1"
# "Less Than" goes the other way: "1 < 2"
# A fun way to remember which is which is to think of it like a
# crocodile's mouth, always biting the bigger value

if foo > bar:
    print("Foo is greater!")
    #Let's print a couple of 'newlines' to make it readable:
    print('\n\n')

else:
    print ("Foo is not greater")
    print("Because this line is indented it only runs when the 'else' is matched")
    #Let's print a couple of 'newlines' to make it readable:
    print('\n\n')

print("This line runs after the conditional, regardless of the result")
print ("Indenting is important in python!")

