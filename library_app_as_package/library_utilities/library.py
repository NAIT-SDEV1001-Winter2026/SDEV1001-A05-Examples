from csv import DictReader,DictWriter
#When importing from within a package you are importing relative to the file you are in
# . means (this package)
from .book import *

class Library:
    # A constructor that stores the library name and starts with an empty book collection
    def __init__(self,name):
        self.name = name
        self.books = []#list of book objects
    
    # A method to add a Book to the library
    def add_book(self,book):
        self.books.append(book)
    
    # A string representation that prints only the library name(using the __str__ dunder method)
    def __str__(self):
        print(self.name)

#     A method to list books with formatting:
#   - 'Current books in our library:' followed by a dash-prefixed list or a 'No books in our library' message
    def list_books(self):
        print("Current books in our library:")
        if len (self.books) == 0:#empty list
            print("No books in our library")
        else:
            for book in self.books:
                print (f"- {book}")

    def get_book_by_name(self, title):
        return_value = None
        for book in self.books:
            if book.title.lower() == title.lower():
                return_value = book
        return return_value
    
    def write_books_to_csv(self,file_path):
        with open(file_path,"w", newline = "") as f:
            writer = DictWriter(f,fieldnames=["title","author","pages"])
            writer.writeheader()
            #write each book object in the list to a file
            for book in self.books:
                #writerow() writes a dictionary entry to the file
                #We need to make each object look like a dictionary
                writer.writerow({"title": book.title,"author":book.author,"pages":book.pages})
        
    def read_books_from_file(self,file_path):
        self.books.clear()#only needed if you do not want to read the file and ADD to what was already in the list.
        with open(file_path,"r", newline = "") as f:
            reader = DictReader(f)
            for row in reader:
                self.books.append(Book(row["title"],row["author"],row["pages"]))
        return self.books
    