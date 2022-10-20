# introduction match statement in conditional statement

# TYPE -1 

name = input("enter ur name: ")

match name:
    case "Prasad":
        print("Kommuchikkala")
    case "Ravi surya":
        print("Kakinada")
    case "Ramana":
        print("Kakinada")
    case "Karthik":
        print("Rajol")
# To handle the any other name not in this code
    case _:
        print("Who ?")


# TYPE -2

name = input("enter ur name: ")

match name:
    case "Prasad":
        print("Kommuchikkala")
    case "Ravi surya" | "Ramana":
        print("Kakinada")
    case "Karthik":
        print("Rajol")
# To handle the any other name not in this code
    case _:
        print("Who ?")

