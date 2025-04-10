#Ainsley Pyle
from book import Book 

books=[]
with open("books.txt") as file:
    for line in file:
        line=line.strip().split(",")
        book=Book(line[0],line[1], line[2])
        print(book)
        books.append(book)

#Calling methods on first book 
print(books[0].get_title())
print(books[0].get_author())
print(books[0].get_genre())
print(books[0].is_checked_out())

#Checking out and returning first book 
books[0].check_out()
print(books[0])
books[0].return_book()
print(books[0])
