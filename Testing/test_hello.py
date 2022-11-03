from hello import hello

def test_default():
    assert hello("raju") == "hello,raju"
    assert hello("prasad") == "hello,prasad"
def test_argument():
    assert hello() == "hello,world"