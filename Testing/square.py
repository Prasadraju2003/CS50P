# square of a num
def main():
    x = int(input("what's x ?"))
    print("x squared is",square(x))

def square(n):
    return n*n
# This line use import these function without running main function
if __name__=="__main__":
    main()