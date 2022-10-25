# command-line argument takes input(arguments) to the program on just execution of program
# for command-line argument their is module (sys) and function(sys.argv)

import sys
# Here argv[1] indicets name after name of code
# Here argv[0] indicets name of code
print("hello,my name is",sys.argv[1])


# if user don't a input after name of code
import sys

try:
    print("hello,my name is",sys.argv[1])
except IndexError:
    print("Too few arguments")

#  if the user too many arguments or too few arguments after name of the program 

import sys
if len(sys.argv)<2:
    print("Too few arguments")
elif len(sys.argv)>2:
    print("Too many arguments")
else:
    print("Hello,my name is",sys.argv[1])

# Note: (To give two or more arguments as one argument u add quotes to that arguments) 
# ex : python sample.py "prasad raju" 

import sys
if len(sys.argv)<2:
    print("Too few arguments")
elif len(sys.argv)>2:
    print("Too many arguments")
# it through indexerror.Because if block only  tells at expression is True or False
# And it comes this print function .so error will occur
print("Hello,my name is",sys.argv[1])

# To solve error the sys module contains a function(sys.exit)
import sys
if len(sys.argv)<2:
    sys.exit("Too few arguments")
elif len(sys.argv)>2:
    sys.exit("Too many arguments")
print("Hello,my name is",sys.argv[1])


# To print and take two or more arguments by using for loop.
import sys
if len(sys.argv)<2:
    sys.exit("Too few arguments")
# Here we using slicing (sys.argv[1:]) it use to don't print name of code as ur name.
for arg in sys.argv[1:]:
    print("Hello,my name is",arg)

import sys
if len(sys.argv)<2:
    sys.exit("Too few arguments")
# Here we using slicing (sys.argv[1:-1]) it use to don't print name of code as ur name and remove last name in command line.
for arg in sys.argv[1:-1]:
    print("Hello,my name is",arg)
