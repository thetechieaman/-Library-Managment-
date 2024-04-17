class Book:
    def __init__(self, title, author, isbn, availability=True, num_copies=1):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.availability = availability
        self.num_copies = num_copies
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def count_books(self):
        return len(self.books)

    def check_book_availability(self, isbn):
        book = next((b for b in self.books if b.isbn == isbn), None)
        if book:
            return book.availability
        else:
            return None

    def issue_book(self, isbn):
        book = next((b for b in self.books if b.isbn == isbn), None)
        if book and book.availability:
            book.availability = False
            return True
        else:
            return False

    def return_book(self, isbn):
        book = next((b for b in self.books if b.isbn == isbn), None)
        if book and not book.availability:
            book.availability = True
            return True
        else:
            return False

    def mark_book_unavailable(self, isbn):
        book = next((b for b in self.books if b.isbn == isbn), None)
        if book:
            book.availability = False
            return True
        else:
            return False

    def search_books_by_author(self, author):
        return [b for b in self.books if b.author == author]

    def search_books_by_title(self, title):
        return [b for b in self.books if b.title == title]

# Example usage
library = Library()

# Add books
library.add_book(Book("The Great Gatsby", "F. Scott Fitzgerald", "9780743273565"))
library.add_book(Book("To Kill a Mockingbird", "Harper Lee", "9780446310789"))

# Count books
print(f"Number of books: {library.count_books()}")

# Check book availability
print(f"The Great Gatsby availability: {library.check_book_availability('9780743273565')}")

# Issue book
library.issue_book('9780743273565')

# Check book availability again
print(f"The Great Gatsby availability: {library.check_book_availability('9780743273565')}")

# Return book
library.return_book('9780743273565')

# Check book availability again
print(f"The Great Gatsby availability: {library.check_book_availability('9780743273565')}")

# Mark book as unavailable
library.mark_book_unavailable('9780743273565')

# Check book availability
print(f"The Great Gatsby availability: {library.check_book_availability('9780743273565')}")

# Search for books by author
print(f"Books by F. Scott Fitzgerald: {library.search_books_by_author('F. Scott Fitzgerald')}")

# Search for books by title
print(f"Books with title 'To Kill a Mockingbird': {library.search_books_by_title('To Kill a Mockingbird')}")