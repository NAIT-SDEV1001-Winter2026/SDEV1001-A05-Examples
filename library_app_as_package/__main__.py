#Make the entire app a package
# It allows the app to be installed using package managers (pip)
#Makes the entry point to the app clearer
#To run the package you must use python -m package_name from the terminal
#Cannot run a package from VS Code

#1. Change the name of the mainline py file to __main__.py
#2. To place __init__.py file in the parent directory for the app
#Change pathing to be relative to the package
from .library_utilities.book import *
from .library_utilities.library import *
from pathlib import Path

base_dir = Path(__file__).parent
print(f"Same folder as __main__.py: {base_dir}")
file_path =  base_dir/"books.csv"

#one folder up from __main__ (same folder as package)
base_dir = Path(__file__).parent.parent
print(f"One folder up from __main__.py(same folder as the package): {base_dir}")
file_path =  base_dir/"books.csv"

#A common way to get the path folder the package is in
#cwd() - current working directory
#where are you calling the package from?
base_dir = Path.cwd()
print(f"One folder up from __main__.py(same folder as the package): {base_dir}")
file_path =  base_dir/"books.csv"

if __name__ == "__main__":
    library1 = Library("Library of Alexandria")

    book1 = Book("House of leaves","Mark Z Daniel.....",800)

    library1.add_book(book1)
    #Shortcut
    library1.add_book(Book("Good stuff", "Shane Bell",2))
    library1.list_books()
    
    #In the library class create a get_book_by_title(self, title) method
    #if the title is in the library, return the book object
    #if it does not exist return None

    #test in the mainline
    #Display "Not found" if not in the library
    #Display the title by Author if in the library

    search_book = input("Enter the title to search for: ")
    found_book = library1.get_book_by_name(search_book)

    if found_book is None:
        print("Not found")
    else:
         print(found_book)

    #Write the books list to the csv file
    library1.write_books_to_csv(file_path)
    #Read the csv file into a list of objects
    new_list = library1.read_books_from_file(file_path)
    #loop through and print each book by author
    print("Books in list after import from file")
    for book in new_list:
        print(book)
