# printing a column of bricks(#)

print("#")
print("#")
print("#")

# same problem by for loop

for i in range(3):
    print("#")

# Defining a function to print a column of bricks.

def main():
    print_column(3)

def print_column(n):
    for i in range(n):
        print("#")
main()


# another way

def main():
    i = int(input("enter value:"))
    print_column(i)

def print_column(n):
    print("#\n"*n,end="")
main()

# printing bricks in a row

def main():
    i = int(input("enter value:"))
    print_row(i)

def print_row(n):
    print("#"*n,end="")
main()


# printing bricks in a row by for loop

def main():
    i = int(input("enter value:"))
    print_row(i)

def print_row(n):
    for i in range(n):
        print("#",end="")
main()


# printing a square

def main():
    i = int(input("enter value:"))
    print_square(i)

def print_square(size):
    for i in range(size):
        for j in range(size):
            print("#",end="")
        print()
main()

# Another way

def main():
    i = int(input("enter value:"))
    print_square(i)

def print_square(size):
    for i in range(size):
        print("#"*size)
main()