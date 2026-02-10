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

germany_cities = ("Munich", "Berlin")

for city in interesting_cities:
    if city not in germany_cities:
         print(f"{city} is an interesting city that we can visit")
           
