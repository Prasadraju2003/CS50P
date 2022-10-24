# let's start expection handling.
# EXAMPLE
# Note : To exception handling u need to know what's the error our code.
x = int(input("value:"))
print(f"x is {x}")

# After running the program and what if when we gave string.it throw some error.
# To handle this type of errors(so many error types are in python) we use exeption handling

# try keyword works, if try block doesn't contain any errors it will execute
try:
    x = int(input("value:"))
    print(f"x is {x}")
# except keyword works, if try block contains a error it come except block and execute code in exception block.
except ValueError:
    print("Only integers allowed")

# some detail error (Nameerror)
# if we moved print statement to end of code(it gives a value error if we gives str as input)
try:
# Generally assignment operator always copy value from right to left side.
# when we give str as input, the value not assign to x.So error will occur
    x = int(input("value:"))
except ValueError:
    print("Only integers allowed")
print(f"x is {x}")


# To solve this problem we use else keyword.
try:
    x = int(input("value:"))
except ValueError:
    print("Only integers allowed")
else:
    print(f"x is {x}")

# same problem using while loop for user until int value as input
while True:
    try:
        x = int(input("value:"))
    except ValueError:
        print("Only integers allowed")
    else:
        break
print(f"x is {x}")

# Another way

while True:
    try:
        x = int(input("value:"))
        break
    except ValueError:
        print("Only integers allowed")
print(f"x is {x}")


# defining a function it get a int from user.

def main():
    x = get_int()
    print(f"x is {x}")
def get_int():
    while True:
        try:
            x = int(input("value:"))
        except ValueError:
            print("Only integers allowed")
        else:
            break
    return x
main()

# Another way

def main():
    x = get_int("what's x?")
    print(f"x is {x}")
def get_int(prompt):
    while True:
        try:
            x = int(input(prompt))
        except ValueError:
            print("Only integers allowed")
        else:
            break
    return x
main()


# introduction to pass keyword

while True:
    try:
        x = int(input("value:"))
    except ValueError:
       pass
print(f"x is {x}")

# Now about raise keyword in exception handling

x = 5
print(f"x is {x}")
if not type(x) is int:
    raise ValueError("enter an integer")