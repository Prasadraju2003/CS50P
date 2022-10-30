# Reading .csv(comma seperated values) files and printing
with open("students.csv",) as file:
    for line in file:
        row = line.rstrip().split(",")
        print(f"{row[0]} lives in {row[1]}")

# another way

with open("students.csv",) as file:
    for line in file:
        row = line.rstrip().split(",")
        print(f"{row[0]} lives in {row[1]}")

# sorting and print by using list

students = []
with open("students.csv") as file:
    for line in file:
        name,place = line.rstrip().split(",")
        students.append(f"{name} lives in {place}")
for student in students:
    print(student)
# we sorted this list by whole sentence


# now changing to name or place as dics in list

students = []
with open("students.csv") as file:
    for line in file:
        name,place = line.rstrip().split(",")
        # saving that vaules to empty dictionary in list
        student ={}
        student["name"] = name
        student["place"] = place
        students.append(student)
print(students)

# Another way 

students = []
with open("students.csv") as file:
    for line in file:
        name,place = line.rstrip().split(",")
        student ={"name": name,"place":place}
        students.append(student)
print(students)


# Now sorting by name or place in dic in list.

students = []
with open("students.csv") as file:
    for line in file:
        name,place = line.rstrip().split(",")
        student ={"name": name,"place":place}
        students.append(student)
def get_name(student):
    return student["name"]
# get_name manually works without passing argument in sorted function.
for student in sorted(students,key=get_name):
    print(f"{student['name']} lives in {student['place']}" )

# Generally we can't sort dictionaries .But  we can by using lambda keyword in sorted function

students = []
with open("students.csv") as file:
    for line in file:
        name,place = line.rstrip().split(",")
        student ={"name": name,"place":place}
        students.append(student)
for student in sorted(students,key=lambda student: student["name"]):
    print(f"{student['name']} lives in {student['place']}" )

# If .csv file contain more than values u wanted.
# To solve problem python have a module called "csv"

import csv

students =[]

with open("student.csv") as file:
    # which can reads the file excluding expection like commas,quotes etc..
    reader = csv.reader(file)
    for name,address in reader:
        students.append({"name":name,"address":address})
for student in sorted(students,key=lambda student:student["name"]):
    print(f"{student['name']} is from {student['address']}")

# for handle dictionaries csv library contain function DictReader()

import csv

students =[]

with open("student.csv") as file:
    # which can reads the file excluding expection like commas,quotes etc..
    reader = csv.DictReader(file)
    for row in reader:
        # now we add a new line in student.csv (name,address) which intializes as keys
        students.append({"name":row["name"],"address":row["address"]})
for student in sorted(students,key=lambda student:student["name"]):
    print(f"{student['name']} is from {student['address']}")








