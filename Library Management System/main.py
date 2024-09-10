"""
from library_module import Library,LibraryUser,Book

def main():
    library=Library()
    user1=LibraryUser(1001,"Alice")
    user2=LibraryUser(1002,"Chinchu")

    while True:
        print("\nLibrary Management System \n1. Add Books \n2. Remove Books \n3. Search Books \n4. Display Book List \n5. Borrow Book \n6. Return Borrowed Book \n7. Display Borrowed Books \n8. Exit")

        ch=input("Enter the choice: ")

        if ch=="1":
            try:
                book_id=input("Enter the book id: ")
                author=input("Enter the author: ")
                title=input("Enter the title: ")
                book=Book(book_id,author,title)
                library.add_book(book)
            except ValueError as e:
                print(f"Error: {e}")

        elif ch=="2":
            try:
                book_id=input("Enter the book id:")
                library.remove_book(book_id)
            except ValueError as e:
                print(f"Error: {e}")
        
        elif ch=="3":
            try:
                title=input("Enter the title:")
                for book in library.search_book(title):
                    print(book.display_book_details())
                
            except ValueError as e:
                print(f"Error: {e}")
        
        elif ch=="4":
            try:
                for book in library.list_books():
                    print(book)
            except ValueError as e:
                print(f"Error: {e}")
        
        elif ch=="5":
            try:
                book_id=input("Enter the book id: ")
                user1.borrow_book(book_id,library)
            except ValueError as e:
                print(f"Error: {e}")
        
        elif ch=="6":
            try:
                book_id=input("Enter the book_id: ")
                user1.return_book(book_id,library)
            except ValueError as e:
                print(f"Error: {e}")
        
        elif ch=="7":
            for book in user1.get_borrowed_books():
                print(book.display_book_details())

        elif ch=="8":
            break

        else:
            print("Invalid choice")

if __name__=="__main__":
    main() 
 
"""

from library_module import Library,LibraryUser,Book

def main():
    library=Library()
    user1=LibraryUser(1001,"Alice")
    user2=LibraryUser(1002,"Chinchu")

    while True:
        print("\nLibrary Management System \n1. Add Books \n2. Remove Books \n3. Search Books \n4. Display Book List \n5. Borrow Book \n6. Return Borrowed Book \n7. Display Borrowed Books \n8. Exit")

        ch=input("Enter the choice: ")

        if ch=="1":
            try:
                book_id=input("Enter the book id: ")
                author=input("Enter the author: ")
                title=input("Enter the title: ")
                book=Book(book_id,author,title)
                library.add_book(book)
            except ValueError as e:
                print(f"Error: {e}")

        elif ch=="2":
            try:
                book_id=input("Enter the book id:")
                library.remove_book(book_id)
            except ValueError as e:
                print(f"Error: {e}")
        
        elif ch=="3":
            try:
                title=input("Enter the title:")
                for book in library.search_book(title):
                    print(book.display_book_details())
                
            except ValueError as e:
                print(f"Error: {e}")
        
        elif ch=="4":
            try:
                for book in library.list_books():
                    print(book)
            except ValueError as e:
                print(f"Error: {e}")

        elif ch=="5":
            try:
                book_id=input("Enter the book id: ")
                user1.borrow_book(book_id,library)
            except ValueError as e:
                print(f"Error: {e}")
        
        elif ch=="6":
            try:
                book_id=input("Enter the book_id: ")
                user1.return_book(book_id,library)
            except ValueError as e:
                print(f"Error: {e}")
        
        elif ch=="7":
            for book in user1.get_borrowed_books():
                print(book.display_book_details())

        elif ch=="8":
            break

        else:
            print("Invalid choice")

if __name__=="__main__":
    main() 
 