

class Book(object):
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.read_patron = None
        self.wait_read_patron = []


class Patron(object):
    def __init__(self, name):
        self.name = name
        self.read_book = []

    def can_borrow(self):
        return len(self.read_book) <= 3

    def borrow_book(self, book):
        if self.can_borrow():
            if book.read_patron:
                book.wait_read_patron.append(self)
            else:
                book.read_patron = self
                self.read_book.append(book)
            return True
        else:
            print("借书不能超过3本！！！")
            return False


class Library(object):
    def __init__(self, books=[], patrons= []):
        self.books = books
        self.patrons = patrons

    def add_book(self, book:Book):
        self.books.append(book)

    def del_book(self, book:Book):
        self.books.remove(book)

    def find_book(self, book:Book):
        return self.books.index(book)

    def add_patron(self, patron):
        self.patrons.append(patron)

    def del_patron(self, patron):
        self.patrons.remove(patron)

    def find_patron(self, patron):
        self.patrons.index(patron)

    def borrow_book(self, partron, book):
        flag = partron.borrow_book(book)
        if flag and book in self.books:
            self.del_book(book)

    def return_book(self,partron, book):
        partron.read_book.remove(book)
        if book.wait_read_patron:
            book.read_patron = book.wait_read_patron.pop(0)
        else:
            book.read_patron = None
            self.books.append(book)




