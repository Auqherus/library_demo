from main import *

   
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
        
    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        for lib_book in self.books:
            if lib_book.title == book.title and lib_book.author == book.author:
                self.books.remove(lib_book)

            
    def search_books(self, search_string):
        lower_search = search_string.lower()
        book_list = []
        for book in self.books:
            if lower_search in book.title.lower() or lower_search in book.author.lower():
                book_list.append(book)
                
        return book_list
    
def main():
 
    war_book = Book("World War II And so On", "Franklin Roosvelt")
    sf_book = Book("Star Wars, old Republic Strickes back!", "John Lucas")
    horror_book = Book("Things In Darkness", "Stephen King")
    fantasy_book = Book("Harry Potter and a CHamber of Secrets", "J. K. K. Rowling")
    holy_book = Book("The Old Testament", "Many Authors")
    simple_book = Book("How To Do It Yourself", "by Graffy Blackmarrow")

    library = Library("Auqherus")
    library.add_book(war_book)
    library.add_book(sf_book)
    library.add_book(horror_book)
    library.add_book(fantasy_book)
    library.add_book(holy_book)
    library.add_book(simple_book)


    results = library.search_books("old")

    for r in results:
        print(f"Title: {r.title}, Author: {r.author}")

if __name__ == "__main__":
    main()

        
        
