import sys

if len(sys.argv) != 2:
    print(f"{sys.argv[0]} expected exactly one argument.")
    sys.exit(1)

password = sys.argv[1]
is_valid = False

# Do all the requirement checks here.
low = False
upper = False
special = False
length = False

for letter in password:
    if letter.islower():
        low = True
    if letter.isupper():
        upper = True
    if letter in "$#@":
        special = True
    if len(password) >= 6 and len(password) <=16:
        length = True

if (low == True) and (upper == True) and (special == True) and (length == True):
    is_valid = True


print(is_valid)
