from booksClass import Book
import booksSDK

book=Book("Sherlock holmes",200)
print(booksSDK.add_book(book))
print("DISPLAYING ALL THE BOOKS:")
print(booksSDK.get_books())