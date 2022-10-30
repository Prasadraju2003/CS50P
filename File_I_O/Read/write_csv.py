# writing csv file

import csv

name = input("student name:")
place = input("place:")

with open("student1.csv","a") as file:
# csv.writer use to write value in csv format
    writer = csv.writer(file)
# intially we should add home,place line add to student1.csv file
# based on that we can intialize write([name,place])
    writer.writerow([name,place])

# writing csv file using dictionaries(csv.DictWriter()) function
import csv

name = input("student name:")
place = input("place:")

with open("student1.csv","a") as file:
    writer = csv.DictWriter(file,fieldnames=["name","place"])
    writer.writerow({"name": name,"place":place})
