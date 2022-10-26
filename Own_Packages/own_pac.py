# making my own package
# To use our function we can create some functions 
import sys
def main():

    hello("world")
    goodbye("world")

def hello(name):
    print(f"hello,{name}")

def goodbye(name):
    print(f"goodbye,{name}")
# This line use to use the our own package without calling main function.
if __name__=="__main__":
    main()

