#Basic steps for working with a file
    #Open the file
    #Work with the file
    #Close the file

#Write to a file in the same folder as the py file
from pathlib import Path

base_dir = Path(__file__).parent#what is the path to the folder this py file is in. Where am I now?
file_path = base_dir/"movies.txt"#path to the text file we will work with

#with will open the file at the file_path for appending "a" and close the connection when it is done
#appending adds to the current content of the file
#if the file does not exist, it will be created 
with open(file_path,"a") as f:
    f.write("Star Wars\n")#write this text to the file
    f.write("grease\n")

#Overwrite the current file content
with open(file_path,"w") as f:
    f.write("Truman Show\n")#write this text to the file
    f.write("The Lord of the Rings\n")
    f.write("Sinners\n")


#Exercise
#Using a new file called food.py, write to a file called food_items.txt
#In a loop, as for a food item and add to a list.
#Keep looping until the user enters "socks"
#Add the items in the list to the text file.
#If the user enters nothing or spaces keep prompting

#Challenge
#Create a reusable function to call to add each value to the file
#def add_to_file(file_path,text):






