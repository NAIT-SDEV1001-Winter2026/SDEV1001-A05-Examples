#List is a collection of values
#Each value in a list is stored in an element
#can hold different datatypes (including other lists!)

colors = ["red", "blue", "green", "yellow"]#4 elements
#Display the list
print (colors)

#access elements of a list through a zero based index
print (colors[1])

#from end of list
print (colors[-2])

#change a value
colors[3] = "Beige"
print(colors)

#slicing
#get values from a range in the list
letters = ["a","b","c","d","e"]
print (f"First three letters: {letters[0:3]}")
#with slices, the lower boundary is inclusive, the upper boundary is exclusive
#if you are starting at the beginning of the list you can omit the starting index
print (f"First three letters: {letters[:3]}")
#if you are starting at the end of the list you can omit the ending index
print (f"First three letters: {letters[-2:]}")

#length of a list
print(len(letters))

#Accessing a list outside its boundaries is an error
print(letters[4])