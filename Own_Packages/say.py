# importing our own package from another code
import sys

from own_pac import hello

if len(sys.argv)==2:
    hello(sys.argv[1])

# another way  
from own_pac import hello

x = input("enter ur name:")
hello(x)