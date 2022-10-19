#Adding Two numbers
x = input("x: ")
y = input("y: ")
# This code throws error because "+" works as concetenation
z = x + y
print(z)

# SOLUTION
x = int(input("x: "))
y = int(input("y: "))
z = x + y
print(z)

# Adding Two float numbers
x = float(input("x: "))
y = float(input("y: "))
z = x + y
print(z)

# Rounding a flaoting number
# Real means of round function "round(number[, ndigits])"
x = float(input("x: "))
y = float(input("y: "))
z = round(x + y)
print(z)
#--------------------------------
x = float(input("x: "))
y = float(input("y: "))
z = round(x + y)
# it will commas after thousand place and ten thousand
# ex: 100000 to 100,000
print(f"{z:,}")

# Division on float numbers and rounding the Result
x = float(input("x: "))
y = float(input("y: "))
# Rounding floating number upto two decimal digits
z = round(x / y,2)
print(z)

           #  ANOTHER WAY #
x = float(input("x: "))
y = float(input("y: "))
z = x / y
print(f"{z:.2f}")











