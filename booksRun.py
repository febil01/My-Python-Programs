from booksClass import Book
import booksSDK

def menu():
    print("""************BOOK DATABASE************
    1. ---> Display All Books 
    2. ---> Add a Book
    3. ---> Update a book
    4. ---> Delete a book
    5. ---> Search for a book
    6. ---> Exit the Application
    """)
    choice=int(input("CHOOSE AN OPTION (1-6):"))
    return choice

while True:
    choice=menu()
    i=0
    if choice==1:
        print("Displaying all the books:")
        print("--------------------------------------------")
        for book in booksSDK.get_books():         
            print("TITLE OF THE BOOK:",book[0])
            print("NUMBER OF PAGES:",book[1])
            print("--------------------------------------------")
    
    elif choice==2:
        book_name=input("Enter the name of the book:")
        book_pages=int(input("Enter the number of pages:"))
        book_name=book_name.strip()
        book=Book(book_name,book_pages)
        booksSDK.add_book(book)
        print("Book has been successfully added to the database...")
    
    elif choice==3:
        book_name=input("Enter the name of the book to be updated:")
        book_pages=input("Enter the number of pages of the book that is to be updated:")
        book=Book(book_name,book_pages)
        print("------------ENTER UPDATED DETAILS------------")
        updated_book_name=input("Enter the name of the updated book (Leave empty for no change):")
        updated_pages=input("Enter the number of pages to be updated (Leave empty for no change):")
        if updated_book_name == "":
            updated_book_name=book_name
        if updated_pages == "":
            updated_pages=book_pages
        booksSDK.update_book(book,updated_book_name,updated_pages)

    elif choice==4:
        title=input("Enter the name of the book to be deleted:")
        booksSDK.delete_books(title)
    
    elif choice==5:
        search=input("Enter the name of the book to be searched:")
        books=booksSDK.get_book_by_title(search)
        if len(books) > 0:
            print("-------------SEARCH RESULT-------------")
            for book in books:
                print(book)
        else:
            print(f"ERROR: Book \"{search}\" not found. Please try again....")

    elif choice==6:
        exit()

    else:
        print("Invalid choice Entered. Please try again......")

    input("Press any key to continue.....")