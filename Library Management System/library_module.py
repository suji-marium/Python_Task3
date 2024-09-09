class Book:
    def __init__(self, book_id, author, title):
        self.book_id = book_id
        self.author = author
        self.title = title
        self.status=False

    def display_book_details(self):
        return f"Book_id: {self.book_id}, Author: {self.author}, Title: {self.title}"
    
class Library:
    def __init__(self):
        self.books = {}
    
    def add_book(self, book):
        if book.book_id in self.books:
            raise ValueError(f"Book with ID {book.book_id} already exists.")
        self.books[book.book_id] = book
    
    def remove_book(self, book_id):
        if book_id not in self.books:
            raise ValueError(f"Book ID {book_id} doesn't exist.")
        del self.books[book_id]
    
    def search_book(self, title):
        sorted_books = [book for book in self.books.values() if title.lower() in book.title.lower()]
        if not sorted_books:
            raise ValueError(f"No books found with title containing '{title}'.")
        return sorted_books

    def list_books(self):
        for book in self.books.values():
            yield book.display_book_details()

class User:
    def __init__(self, user_id, user_name):
        self.user_id = user_id
        self.user_name = user_name
    
    def display_user_details(self):
        print(f"User Id: {self.user_id}, Name: {self.user_name}")
"""
class LibraryUser(User):
    
    def __init__(self, user_id, user_name):
        super().__init__(user_id, user_name)
        self.borrowedbooks = set()

    def borrow_book(self, book_id, library):
        if not isinstance(library, Library):
            raise TypeError("Expected a Library instance.")
        if book_id not in library.books:
            raise ValueError("Book with this ID does not exist in the library.")
        if book_id in self.borrowedbooks:
            raise ValueError(f"{self.user_name}, you have already borrowed this book.")
        self.borrowedbooks.add(book_id)
    
    def return_book(self, book_id, library):
        if not isinstance(library, Library):
            raise TypeError("Expected a Library instance.")
        if book_id not in self.borrowedbooks:
            raise ValueError("You have not borrowed this book.")
        self.borrowedbooks.remove(book_id)
    
    def get_borrowed_books(self):
        return self.borrowedbooks
"""

class LibraryUser(User):
    
    def __init__(self, user_id, user_name):
        super().__init__(user_id, user_name)
        self.borrowedbooks=list()

    def borrow_book(self, book_id, library):
        if not isinstance(library, Library):
            raise TypeError("Expected a Library instance.")
        if book_id not in library.books:
            raise ValueError("Book with this ID does not exist in the library.")
        if book_id in self.borrowedbooks:
            raise ValueError(f"{self.user_name}, this book has already borrowed.")
        
        for book in library.books.values():
            if book.book_id==book_id:
                if book.status==True:
                    raise ValueError(f"{self.user_name}, this book has already borrowed.")
                self.borrowedbooks.append(book)
                book.status=True
    
    def return_book(self, book_id, library):
        if not isinstance(library, Library):
            raise TypeError("Expected a Library instance.")
        if book_id not in self.borrowedbooks:
            raise ValueError("You have not borrowed this book.")
        for book in self.borrowedbooks:
            if book.book_id==book_id:
                self.borrowedbooks.remove(book_id)
            book.status=False
    
    def get_borrowed_books(self):
        return self.borrowedbooks