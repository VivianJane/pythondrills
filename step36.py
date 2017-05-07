# assign an integer to a variable

var = 1

# assign a string to a variable

words = "blue skies save lives"

# assign a float to a variable

doors = 11.11

# task 7: print .format()

print ("What does {} mean".format(doors))

# Use each of these operators +, - , * , / , +=, ­= , %

varadd = var + 1

varmult = var * 2

varsub = var - 1

vardiv = var / 1

var += 1

varequals = var = 2

varmodulo = var % 1

# 6. Use of logical operators: and, or, not
# 7. Use of conditional statements: if, elif, else

if var and doors:
    print ("unicorns")

elif var or doors:
    print ("horses")

elif not var:
    print ("zebras")

var = 1
while var == 1:
    print ("floppy")
    var += 1
    
# for loop, iterating through list, print on new lines

for x in range(5):
    print x

# tuple, iteration

tup = (1,2)
for x in tup:
    print x

# define a function that returns a string variable

def stringFunc():
    print words
    return words

stringFunc()

