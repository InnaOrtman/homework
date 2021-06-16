# Task 2
#
# Library
#
# Write a class structure that implements a library. Classes:
#
# 1) Library - name, books = [], authors = []
#
# 2) Book - name, year, author (author must be an instance of Author class)
#
# 3) Author - name, country, birthday, books = []

class Library:
    books = []
    authors = []

    def addBook(self, name, author, year):
        self.name = name
        self.author = author
        self.year = int(year)
        Library.books.append((self.name, self.author, self.year))

    def group_by_author(self, author):
        for book in Library.books:
            if book[1] == author:
                Library.authors.append(book)
        print(Library.authors)

    def group_by_year(self, year):
        for book in Library.books:
            if book[2] == year:
                Library.books.append(book)
        print(Library.books)

    def get_librery(self):
        print(f'The list of books in the library: {Library.books}')
        print(f'Author`s information: {Library.authors}')

    def __repr__(self):
        return f"Library({self.books})"

    def __str__(self):
        return f"Library has {len(self.books)} books"


class Author(Library):
      def add_author(self, author, country, birthday):
          self.country = country
          self.birthday = birthday
          self.author = author
          Library.authors.append((self.author, self.country.upper(), self.birthday),)

class Book(Author):
    pass


book = Library()
book1 = Author()
book2 = Book()
book.addBook('Math', 'George Harr', 2010)
book1.addBook('Math', 'George Horr', 2012)
book2.addBook('Math', 'George Hurr', 2014)
book1.add_author('George Harr', 'Usa', 1988)
book2.group_by_author('George Harr')
book.get_librery()
print(book.__repr__())
print(book.__str__())


