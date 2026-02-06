#for loops allow us to retrieve each value in a collection

bands = ["ABBA", "Journey", "Styx", "The Beatles"]

#loop through the list

for band in bands:
    print(f"{band} is a great band!")

#Enumerate function returns both the value AND the index
for index,band in enumerate(bands,start = 1):
    print (f"Band number {index} is {band}")

#Create a list of 4 options(Add,Delete,Update, Quit)
# 1. Add
# 2. Delete
# 3. Update
# 4. Quit

menu_options = ["Add", "Update", "Delete", "Quit",]
for menu_number, value in enumerate(menu_options, start = 1):
    print (f"{menu_number}. {value}")

#Print only the names that are not bad names
names = ["Han Solo", "Luke", "Darth Vader", "Yoda", "Leia", "Boba Fett", "Chebacca"]

bad_names = ("Darth Vader", "Boba Fett")

for name in names:
   if name not in bad_names: 
      print(f"{name} is a good name!")

#Using continue
#goes to the next value in the list
for name in names:
    if name in bad_names:
        continue#Skips to next iteration of the loop
    print(f"{name} is a good name!") 

#break
#Exists a loop
#print out the first even number in the list
numbers = [1,9,11,4,8,15,10]
count = 0
for number in numbers:
    if number % 2 == 0:     
        print(f"The first even number found is {number}")
        break#Exit the loop here
print ("Have a groovy FryYay!")

#print the numbers in the list while the sum of the numbers is not over 25
numbers = [5,8,12,20,4,6,3,88,4543,23,43]

MAX_SUM = 25
sum = 0

for number in numbers:
    sum += number
    if sum > MAX_SUM:
        break    
    print(number)


