# reading data from the file

with open("names.txt","r") as file:
    lines = file.readlines()

for line in lines:
    print("hello,",line.rstrip())


# let's first sort the names in .txt file and print them by using lists>

names = []

with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip())
for name in sorted(names):
    print(f"hello,{name}")
