# Introduction to loops

# WHILE LOOP

# without using while loop
# Example
#printing meow without using while loop
print("meow")
print("meow")
print("meow")

# Another way 

print("meow\n"*3,end="")

# Now with while loop

i = 0
while i<3:
    print("meow")
    i+=1

# Another way but taking input from user

n = int(input("how many times u want to print ?"))
i=0
while i!=n:
    print("meow")
    i+=1

#  FOR LOOP

# printing meow using for loops using lists

for i in [0,1,2]:
    print("meow")

# printing meow using for loops using range feature
# range feature starts from 0 and uto value
for i in range(3):
    print("meow")


#  taking input from user and printing how many times they want
# This while loop helps to take positive input from user
# if the user enter positive num it stops looping
while True:
    n = int(input("how many times u want to print"))
    if n<0:
        continue
    else:
        break
for i in range(n):
    print("meow")


# Another way

while True:
    n = int(input("how many times u want to print"))
    if n>0:
        break
for i in range(n):
    print("meow")

# Another way by def your own function

def main():
    while True:
        n = int(input("enter n value:"))
        if is_positive(n):
            break
    for i in range(n):
        print("meow")
def is_positive(x):
    if x > 0:
        return True
main()

# Another way by def your own function


def main():
    number = get_number()
    meow(number)

def meow(x):
    for i in range(x):
        print("meow")
def get_number():
    x = int(input("enter :"))
    while True:
        if x>0:
            return x
main()



