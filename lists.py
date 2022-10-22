# let's start lists 

# Example

names = ["Raju","Ramana","Ravi"]
# it's prints all the items in this list
print(names)


# print a name in  list using index value
names = ["Raju","Ramana","Ravi"]
# it's print  the items in first in this list
print(names[0])
# it's print  the items in second in this list
print(names[1])
# it's print  the items in third in this list
print(names[2])

# print a name in  list using for loop
names = ["Raju","Ramana","Ravi"]
for name in names:
    print(name)

# print a name in  list using for loop and range function.
names = ["Raju","Ramana","Ravi"]
# len (length) fuction gives lenght of the list.
for i in range(len(names)):
# Here i+1 gives s.no row (just for fun)
    print(i+1,names[i])

