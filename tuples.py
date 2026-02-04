#Tuples are like lists but they are immutable (Cannot change)
#Defined with () instead of []

winter_months = ("December", "January", "February")

#ask the user for a month name
#if it is a winter month, print "Winter", otherwise print "Not Winter"

user_month = input ("Enter a month name: ")

if user_month in winter_months:
    print ("Winter")
else:
    print("Not Winter")