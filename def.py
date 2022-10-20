# Defining a function (when ever u want to use this function u acn call this.)

# TYPE -1

def main():
    x = int(input("enter x:"))
# if True
    if is_even(x):
        print("x is Even.")
# if False 
    else:
        print("x is Odd.")
def is_even(n):
# if statement always return a boolen value.
    if n%2==0:
        return True
    else:
        return False
main()


# TYPE -2

def main():
    x = int(input("enter x:"))
    is_even(x)
# if statement always return a boolen value.
def is_even(n):
    if n%2==0:
        print("x is Even.")
    else:
        print("x is odd.")
main()


# TYPE -3 


def main():
    x = int(input("enter x:"))
    if is_even(x):
        print("x is Even.")
    else:
        print("x is odd.")
# if statement always return a boolen value.
def is_even(n):
    return True if n%2==0 else False
    
main()


# TYPE - 4

def main():
    x = int(input("enter x:"))
    if is_even(x):
        print("x is Even.")
    else:
        print("x is odd.")
# if statement always return a boolen value.
def is_even(n):
    return (n%2==0)
    
main()


