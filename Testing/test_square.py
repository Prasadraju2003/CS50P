# importing a function from another py code
# Testing the code.
from square import square

def main():
    test_square()

def test_square():
    if square(2) != 4:
        print("2 square was not 4")
    if square(3) != 9:
        print("3 square was not 9")

if __name__=="__main__":
    main()


# introduction to assert() function

from square import square

def main():
    test_square()

def test_square():
# assert used to given statement or expression should be true.
# if it is false it throughs Assertion Error.
    assert square(2) == 4
    assert square(3) == 9 
if __name__=="__main__":
    main()

# excepection error on assert.

from square import square

def main():
    test_square()

def test_square():
    try:
        assert square(2) == 4
    except:
        print("2 squared is not 4")
    try:
        assert square(3) == 9
    except:
        print("3 squared is not 9")
    try:
        assert square(-1) == 1
    except:
        print("-1 squared is not 1")
    try:
        assert square(-2) == 4
    except:
        print("-2 squared is not 4")
if __name__=="__main__":
    main()


# introduction pytest library to test ur code.
# pytest is intalled by command <pip install pytest>
# pytest shows assertion errors in gui in terminal window.

from square import square

def test_square():
    assert square(2) == 4
    assert square(3) == 9
    assert square(-2) == 4
    assert square(-3) == 9
    assert square(0) == 0

test_square()

# Testing code by parts using pytest.

from square import square

def test_positive():
    assert square(2) == 4
    assert square(3) == 9
def test_negative():
    assert square(-2) == 4
    assert square(-3) == 9
def test_zero():
    assert square(0) == 0

from square import square

def test_positive():
    assert square(2) == 4
    assert square(3) == 9
def test_negative():
    assert square(-2) == 4
    assert square(-3) == 9
def test_zero():
    assert square(0) == 0
def test_str(n):
    if type(n)== str:
        raise TypeError

