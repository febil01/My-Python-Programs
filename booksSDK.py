from booksClass import Book
import sqlite3

def cursor():
    return sqlite3.connect('books.db').cursor()

c=cursor()
with c.connection:
    c.execute('CREATE TABLE IF NOT EXISTS books (title TEXT, pages INTEGER)')
c.connection.close()

def add_book(book):
    c=cursor()
    with c.connection:
        c.execute('INSERT INTO books VALUES (?,?)', (book.title, book.pages))
    c.connection.close()

def get_book_by_title(title):
    c=cursor()
    books=[]
    with c.connection:
        for book in c.execute('SELECT * FROM books WHERE title=?',(title,)):
            books.append(Book(book[0],book[1]))
    c.connection.close()
    return books
    
def get_books():
    c=cursor()
    books=[]
    with c.connection:
        for book in c.execute('SELECT * FROM books'):
            books.append(book)
    c.connection.close()
    return books

def delete_books(title):
    c=cursor()
    with c.connection:
        c.execute('DELETE FROM books WHERE title=?',(title,))
    c.connection.close()

def update_book(book,updated_book_name,updated_pages):
    c=cursor()
    with c.connection:
        c.execute('UPDATE books SET title=?, pages=? WHERE title=? AND pages=?',(updated_book_name,updated_pages,book.title,book.pages))
    c.connection.close()
    print("--------------------------SUCCESSFULLY UPDATED--------------------------------")