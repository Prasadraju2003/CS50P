# let's about dictionaries in python
# by using this dict we can easily solve problem

# Solving a problem using lists

names = ["Raju","Ramana","Ravi"]
place = ["kommuchikkala","kakinada","kakinada"]

name = input("enter name: ")
if name in names:
# here names.index(name) gives index value if the entered string present in this list
    i = names.index(name)
print (place[i])

# Same problem by using dictionary

stu_info = {
    # "Here it is key":"Here it is value"
    # it can take only to values 
    # if u want to give more values u can lists along with dictionaries
    "Raju":"kommuchikkala",
    "Ramana":"kakinada",
    "Ravi":"kakinada"
    }

name = input("enter name:")
if name in stu_info:
    print(stu_info[name])

# printing all keys and value in this dictionary 
stu_info = {
    "Raju":"kommuchikkala",
    "Ramana":"kakinada",
    "Ravi":"kakinada"
    }
for student in stu_info:
    print(student,stu_info[student],sep="-")

# using dic and lists at time.
# printing all element in this

stu_info = [
    {"name":"Raju","place":"kommuchikkala","roll no":"20B21A4560"},
    {"name":"Ravi","place":"kakinada","roll no":"20B21A4554"},
    {"name":"Ramana","place":"kakinada","roll no":"20B21A4543"},
    {"name":"Narendra","place": None,"roll no":"20B21A4584"}
]

for student in stu_info:
    print(student["name"],student["place"],student["roll no"],sep=", ")


