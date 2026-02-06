# Remove "Edmonton" from the list. Add a city to the list that is input from the user. Sort the list in ascending order and display the list. The output should look like the following:
# Enter a city that interests you: London
# Our list of interesting cities in alphabetical order is:
# ['Amsterdam', 'Berlin', 'London', 'Munich', 'Paris', 'Prague']

interesting_cities = [
    'Edmonton',
    'Paris',
    'Munich',
    'Berlin',
    'Amsterdam',
    'Prague',
]

interesting_cities.remove('Edmonton')
new_city = input("Enter a city that interests you: ")
interesting_cities.append(new_city)
interesting_cities.sort()
print (interesting_cities)