from book import *
from library import *
from pathlib import Path

base_dir = Path(__file__).parent
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
