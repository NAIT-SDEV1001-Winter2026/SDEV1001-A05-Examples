#sorting
numbers = [42,7,19,100,3]
numbers.sort()
print(numbers)

numbers.sort(reverse = True)#sort descending
print(numbers)

#Add a single value
animals = ["python", "dogs", "cats","fish"]
animals.append ("lizard")
print(animals)

#Insert at a location
animals.insert(2,"bird")
print(animals)

#Add a list to a list
additional_animals = ["tiger","panda"]
animals.append(additional_animals)
print(animals)

#Extend
additional_animals = ["snake","dragon"]
animals.extend(additional_animals)
print(animals)

#add the values from a list into another list at an index
animals.insert(1,["cow","goat"])
print(animals)

#Use slice assignment to insert values from another list
animals [1:1] = ["cow","goat"]
print(animals)

#Removing values
#pop() removes by index AND returns the value at that index 
animals.pop(11)
print(animals)

removed = animals.pop(7)
print(f"The animal {removed} has been removed")

#Remove by value
animals.remove("snake")
print(animals)

#is a value in a list?
check_for_animal = input("Enter an animal name: ")
result = check_for_animal in animals
print(f"Is {check_for_animal} in the list? {result}")

animals.append("goat")

#count the occurences of a value
print(animals.count("goat"))

#index of a value
animal_name = input("name of animal to change: ")
found_index = animals.index(animal_name)
animals[found_index] = "crazy " + animal_name
print(animals)

#Clear the list
animals.clear()
print (f"The length of the list is : {len(animals)}")