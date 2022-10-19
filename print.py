#Printing Hello World
print("hello, world")

#Giving input and Printing that input (type 1) Using concetenation
name = input("what's your name? ")
print("hello, "+name)

#Giving input and Printing that input (type 2) Using Comma
#In this method after comma by default Gives space
name = input("what's your name? ")
print("hello,",name)

#The real mean of Print statement
#That's why after print by default it's goes to new line i.e (end="\n")
print("object,sep=' ',end='\n'")

# Example for end="\n"
name = input("what's your name? ")
print("hello, ",end="")
print(name)

#Example for sep=" "
name = input("what's your name? ")
print("hello, ",name,sep="!!!")

#Adding quotation marks in quotation marks
print('hello, "friend"')
print("hello, \"friend\"")

#Printing using Format String
name = input("what's your name? ")
print(f"hello, {name}")

#Remove white space from string Using strip function
name = input("what's your name? ").strip()
print(f"hello, {name}")

           # OR

name = input("what's your name? ")
name = name.strip()
print(f"hello, {name}")

# Capitilazation the string (only first letter of the string will capital)
name = input("what's your name? ")
name = name.capitalize()
print(f"hello, {name}")


# Capitilazation the string (every first letter of the string will capital) Using tilte()
name = input("what's your name? ")
name = name.title()
print(f"hello, {name}")

# Spiit Uesr name into first,second name
name = input("what's your name? ")
first,second=name.split()
print(f"hello, {name}")







