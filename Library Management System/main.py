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
    book1 = Book(1,"Author1","Title1")
    book2 = Book(2,"Author2","Title2")
    book3 = Book(3,"Author3","Title3")
    book4 = Book(4,"Author4","Title4")
    
    try:
        library.add_book(book1)
        library.add_book(book2)
        library.add_book(book3)
        library.add_book(book4)

    except ValueError as e:
        print(f"Error: {e}")

    

    user1=LibraryUser(52,"Suji")
    user2=LibraryUser(59,"Kumar")

    try:
        user1.borrow_book(1,library)
        print(f"\n{user1.user_name} borrowed Book ID 1")
        print("hello")
    except ValueError as e:
        print(f"Error: {e}")

    try:
        user2.borrow_book(1,library)
        print(f"\n{user1.user_name} borrowed Book ID 1")
        print("hello")
    except ValueError as e:
        print(f"Error: {e}")

    try:
        user2.borrow_book(2,library)
        print(f"\n{user2.user_name} borrowed Book ID 2")
        #user2.return_book(2,library)

    except ValueError as e:
        print(f"Error: {e}")

    print("\nBorrowed Books:")
    print(user1.get_borrowed_books())


if __name__=="__main__":
    main() 
    
    

   """ 

    