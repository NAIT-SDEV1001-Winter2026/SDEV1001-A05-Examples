#Stores data in key-value pairs (like kwargs)
#Keys are unique and usually strings; values can be any datatype
#The value can be other collections (dictionary, list, tuple)
#dictionaries use {}

#Student
student = {"name":"Bob", "age": 26, "email":"BobRox@gmail.com"}

#accessing values
print(student["name"])
student["age"] = 27

#Add a new Key-value pair
student["grade"] = 95

#Accessing a key that does not exist:
# print(student["shoe_size"])

#check if a key exists:
if "shoe_size" in student:
    print(f"your shoe size is : {student["shoe_size"]}")
else:
    print("We don't know your shoe size!")

#Return a default value if the key does not exist
print(student.get("names","N/A"))

#Inventory dictionary
inventory = {
            "burger":{"price": 1, "stock":40},
            "pasta":{"price":2, "stock":20}
}
#Access nested values
print(f"{inventory["burger"]["price"]}")

#Looping
grades = {"Bart": 40, "Homer":20, "Lisa": 95}
#Show all the keys
print("NAMES")
for name in grades.keys():#keys() is the default
    print(name)
#All the values
print("GRADES")
for grade in grades.values(): 
    print(grade)
#All the keys and the values
for name,grade in grades.items():
    print(f"{name}: {grade}")

#Exercise:
inventory = {"bananas": 0, "kiwis": 0, "oranges": 0}
deliveries = ["bananas","kiwis","oranges","bananas","kiwis","mango"]

#update the inventory in the dictionary from the deliveries list
for item in deliveries:
    #if in inventory
    if item in inventory:
        inventory[item] += 1
    #else new inventory item
    else:
        inventory[item] = 1

for fruit,count in inventory.items():
    print(f"{fruit}: {count}")

#print the the inventory
#bananas: 2
#kiwis: 2
#oranges: 1
