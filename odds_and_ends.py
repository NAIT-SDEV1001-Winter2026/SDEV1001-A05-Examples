#remove leading and trailing spaces from strings
value = "   abc    "
print(value.lstrip())
print(value.rstrip())
print(value.strip())

#short cut for boolean decisions

#value must be between 1 and 10
value = int(input("Enter a number between 1 and 10: "))

if value >=1 and value <=10:
    is_valid = True
else:
    is_valid = False

if is_valid:
    print ("Valid")
else:
    print ("Invalid")

#Shortcut
is_valid = (value >=1 and value <=10)#Replaces lines 12 - 15
if is_valid:
    print ("Valid")
else:
    print ("Invalid")







