from pathlib import Path

#DictReader reads CSV rows as dictionaries
#DictWriter writes dictionaries to CSV files
from csv import DictReader, DictWriter

base_dir = Path(__file__).parent
file_path = base_dir/ "Movies.csv"

with open(file_path,"r") as f:
    reader = DictReader(f)
    for row in reader:
        print(row)
        #print just the movie name
        print(row["Movie"])

#Print the name of movies that have a budget over 200
#HINT: VERY similar to last example
print("Budgets over 200")
with open(file_path,"r") as f:
    reader = DictReader(f)
    for row in reader: 
        if int(row["Budget"]) > 200:       
            print(row["Movie"])

#read the csv file into a list of dictionaries
movies = []
with open(file_path,"r") as f:
    reader = DictReader(f)
    movies = list(reader)#convert the reader into a list
    # for row in reader:
    #     movies.append(row)
print("List of dictionaries")
print(movies)

#Loop through the list of movies and print out each movie name and its budget.At the end print the average budget
print("Movie names, budgets, and average budget")
sum = 0
for movie in movies:
    sum += float(movie["Budget"])
    print(f"{movie["Movie"]}: ${float(movie["Budget"]):.2f}")
average =4# sum/len(movies)
print (f"Average: ${average:.2f}")

#List of dictionaries for next example
movies = [
    {"Movie": "Star Wars","Rating":"5","Budget":"100"},
    {"Movie": "Star trek","Rating":"4","Budget":"200"}    
    ]

#Write to a csv file
 
#write a list of dictionaries to a file
#newline = "" prevents the extra line between rows on the file
with open(file_path,"w",newline = "") as f:
    field_names = ["Movie","Rating","Budget"]#Header row
    writer = DictWriter(f,fieldnames=field_names)
    writer.writeheader()#write the header row to the file
    for movie in movies:
        writer.writerow(movie)


