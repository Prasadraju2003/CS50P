# introduction to regular expressions

# creating valid email address.

# In this code there are some corner cases which makes code buggy.
# By giving email as "@" only . it shows it's valid.
email = input("enter your email: ").strip()

if "@" in email:
    print("valid")
else:
    print("Invalid")

# checking domain name in email.

email = input("enter your email: ").strip()

if "@" and "." in email:
    print("valid")
else:
    print("Invalid")
# it shows valid when we type "@."


email = input("enter your email:").strip()
if "@" and "." in email:
    username,domain = email.split("@")
    if username and "." in domain:
        print("valid")
    else:
        print("Invalid")
else:
    print("Invalid")

# Intro to (re) regular expession library.
# For more information Visit(https://docs.python.org/3/library/re.html)

# re.search(pattern,string,flags=0)

import re

# using re.search function.

email = input("enter your email:").strip()

if re.search("@",email):
    print("valid")

else:
    print("Invalid")
# But this not proper code for valid the email adrress.

# symbols in regular expressions.
"""  
    1) .   any character except a newline
    2) *   0 or more repetitions
    3) +   1 or more repetitions
    4) ?   0 or 1 repetition
    5) {m}  m repetitions
    6) {m,n} m-n repetitions
                                """
# using symbols
import re

# using re.search function.

email = input("enter your email:").strip()

if re.search(".+@.+",email):
    print("valid")

else:
    print("Invalid")
# But this not proper code for valid the email adrress.

#                  (OR)


import re

# using re.search function.

email = input("enter your email:").strip()
# Here (..* = .+)
if re.search("..*@..*",email):
    print("valid")

else:
    print("Invalid")

# validating domain of gamil.com.
import re

# using re.search function.
# re.search(pattern,string,flags=0)

email = input("enter your email:").strip()

# r = raw string.
# This raw string used to identify the special character in patternss.
if re.search(r".+@gmail\.com",email):
    print("valid")

else:
    print("Invalid")
# but this is not proper code.
# if user enters enter more than there username
# EX : my email is prasad@gmail.com - it shows valid.


"""  
        ^   matches the start of the string
        $   matches the end of the string or just
            just before the newline at the end of the string

            """
import re

# using re.search function.

email = input("enter your email:").strip()

# r = raw string.
# This raw string used to identify the special character in patternss.
if re.search(r"^.+@gmail\.com$",email):
    print("valid")

else:
    print("Invalid")
# This code also not proper syntax.
# when email ex: prasad@@@gmail.com - takes as valid.

# other symbols.

# []     set of characters.
# [^]    complementing the set.

import re


email = input("enter your email:").strip()

if re.search(r"^[^@]+@gmail\.com$",email):
    print("valid")

else:
    print("Invalid")
# This code also not proper syntax.
# when email ex: _prasad@gmail.com  or  .com@gmail.com

# shortcuts for set of characters.
"""
    \d      decimal digit
    \D      not a decimal digit
    \s      whitespace characters
    \S      not a whitespace character
    \w      word chracter ... as well as [a-zA-z0-9_]
            numbers and underscore
    \W      not a word character
                                    """
import re

# .lower() for because email are case insensitive.
email = input("enter your email:").strip().lower()
# we can change domain name from (com|org|edu|gov|etc...). "|" represent "or".
if re.search(r"^[a-zA-Z0-9.]+@gmail\.com$",email):
    print("valid")

else:
    print("Invalid")

#                (OR)

import re

email = input("enter your email:").strip()

if re.search(r"^[a-zA-Z0-9.]+@gmail\.com$",email.lower()):
    print("valid")

else:
    print("Invalid")

#               (OR)

# re.search(pattern,string,flags=0)
# re.search inbuilt varibles.
# re.IGNORECASE
# re.MULTILINE
# re.DOTALL

import re

email = input("enter your email:").strip().lower()

if re.search(r"^[a-zA-Z0-9\.]+@gmail\.com$",email,re.IGNORECASE):
    print("valid")

else:
    print("Invalid")
# This is syntax valid email address for gmail.com

# if email has multiple domain names

# A|B       either A or B
# (...)     a group
# (?:...)   non-capturing version

import re

email = input("enter your email:").strip()
# ? -- optional 
# ([a-zA-Z0-9\.]+\.)? -- is there or not it show true.
if re.search(r"^\w+@(\w+\.)?\w+\.edu$",email,re.IGNORECASE):
    print("valid")

else:
    print("Invalid")


# generally browsers use this regular ex to valid the email.

#  ^[a-zA-Z0-9.!#$%&'*+\/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA -Z theta-9-] \{0, 61\}[a - zA - Z*theta - 9] )?( ?:\.[a-zA-Z0-9](?:[a-zA-Z09-] \{0, 61\}[a - zA - Z*theta - 9] )?)*8
  
# taking valid name from user re library
import re

name = input("what's your name:").strip()
matches = re.search(r"^(.+),(.+)$",name)
if matches:
    last,first = matches.groups()
    name = f"{first} {last}".title()
print(f"hello, {name}")

#            (OR)

import re

name = input("what's your name:").strip()
matches = re.search(r"^(.+),(.+)$",name)
if matches:
    last = matches.group(1)
    first = matches.group(2)
    name = f"{first} {last}".title()
print(f"hello, {name}")

#           (Or)

import re

name = input("what's your name:").strip()
matches = re.search(r"^(.+),(.+)$",name)
if matches:
    name = matches.group(2)+" "+matches.group(1 )
print(f"hello, {name.title()}")

#       (Or)

import re

name = input("what's your name:")
# Here ":=" is called as valrence operator. it can do both variable assignment and give boolean value at a time.
if matches:= re.search(r"^(.+),(.+)"):
    name = matches.group(1) +" "+ matches.group(2)
print(f"hello, {name.title()}")

# code for validate twitter url. and getting username from it .

url = input("URL: ").strip()

username = url.replace("https://twitter.com/","")
print(f"username:{username}")
# this is not propre code.

url = input("URL: ").strip()

username = url.removeprefix("https://twitter.com/","")
print(f"username:{username}")
# this is not propre code.

# To solve this re.sub(pattern,repl,string,count,flags=0)
import re
url = input("URL: ").strip()

username = re.sub(r"https://twitter.com/","",url)

print(f"username:{username}")
# this is not propre code.


import re
url = input("URL: ").strip()

username = re.sub(r"^((https?://)?(www\.)?)?twitter\.com/","",url)

print(f"username:{username}")
# this is also not propre code.
# But when we give "www.google.com" it gives username as www.google.com

import re
url = input("URL: ").strip()
if match:=re.search(r"^((?:https?\://)?(?:www\.)?)?twitter\.com/(\w+)$",url,re.IGNORECASE):
    print(f"username:",match.group(2)) 
else:
    print("Invalid")
