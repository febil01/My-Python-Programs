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
    return c.lastrowid

def get_book_by_title(title):
    c=cursor()
    with c.connection:
        c.execute('SELECT * FROM book WHERE title=?',(title,))
    data=c.fetchall()
    if not data:
        return False
    return Book(data[0],data[1])

def get_books():
    c=cursor()
    books=[]
    with c.connection:
        for book in c.execute('SELECT * FROM books'):
            books.append(Book(book[0],book[1]))
    return books