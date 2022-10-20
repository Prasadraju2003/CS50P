# let's begin conditions in python
# example program




x = int(input("enter x: "))
y = int(input("enter y: "))

if x<y:
    print("x is less then y.")
elif x>y:
    print("x is greater then y.")
else:
    print("x is equal to y.")



# NOW WE USE OR 

x = int(input("enter x: "))
y = int(input("enter y: "))

if x<y or x>y:
    print("x is not equal to y.")
else:
    print("x is equal to y.")


# WE WRITE SAME CODE DIFFERENT WAYS

x = int(input("enter x: "))
y = int(input("enter y: "))

if x!=y:
    print("x is not equal to y.")
else:
    print("x is equal to y.")

# Another way

x = int(input("enter x: "))
y = int(input("enter y: "))

if x==y:
   print("x is equal to y.")
else:
    print("x is not equal to y.")




# NOW WE USE AND
 
marks = int(input("marks: "))

if marks>=90 and marks<=100:
    print("Grade: A")
elif marks>=79 and marks<90:
    print("Grade: B")
elif marks>=65 and marks<79:
    print("Grade: C")
elif marks>=55 and marks<65:
    print("Grade: D")
elif marks>=35 and marks<55:
    print("Grade: E")
elif marks>=0 and marks<5:
    print("Grade: F")
else:
    print("marks range 0-100")