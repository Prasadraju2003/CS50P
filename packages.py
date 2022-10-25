# packages are third party library which install by manually from internet
# The location all these packages called PyPI(python package Index).visit (pypi.org)
# The command to install packages is "pip". It will set path automatically.

# Let's fun on "cowsay" package. For more details visit (pypi.org/project/cowsay)

import cowsay
import sys

if len(sys.argv) == 2:
    cowsay.cow("hello," + sys.argv[1])

# trex function in cowsay library

import cowsay
import sys

if len(sys.argv) == 2:
    cowsay.cow("hello," + sys.argv[1])

# playing with function(char_names) in cowsay module 
import cowsay
import sys
x = input("enter text:")
cowsay.dragon(f"hello,{x}")

# other functions
# >> cowsay.char_names ['beavis', 'cheese', 'cow', 'daemon', 'dragon', 'fox', 'ghostbusters', 'kitty', 'meow', 'miki', 'milk', 'pig', 'stegosaurus', 'stimpy', 'trex', 'turkey', 'turtle', 'tux']