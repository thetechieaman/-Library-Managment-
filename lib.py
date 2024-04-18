import qrcode

# Define the list of books
books = [
    {
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
        "available": True,
        "suggestion": "If you liked this book, you might also enjoy 'The Great Gatsby's contemporary, 'Tender is the Night'."
    },
    {
        "title": "To Kill a Mockingbird",
        "author": "Harper Lee",
        "available": False,
        "suggestion": "If you liked this book, you might also enjoy 'The Help' by Kathryn Stockett."
    },
    # Add more books here...
]

# Define the QR code information
qr_data = ""
for book in books:
    qr_data += f"Title: {book['title']}\nAuthor: {book['author']}\nAvailability: {'Available' if book['available'] else 'Not available'}\nSuggestion: {book['suggestion']}\n\n"

qr_filename = "books_info.png"

# Generate the QR code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(qr_data)
qr.make(fit=True)
img = qr.make_image(fill='black', back_color='white')
img.save(qr_filename)

# Function to mark a book as issued
def issue_book(title):
    for book in books:
        if book["title"] == title and book["available"]:
            book["available"] = False
            print(f"{title} has been issued.")
            return
    print(f"{title} is not available or not found.")

# Prompt the user to enter the search term
search_term = input("Enter the author or title of the book you want to search or issue: ")

# Search for the book in the list of books
books_found = [b for b in books if search_term.lower() in b["title"].lower() or search_term.lower() in b["author"].lower()]

# Display the book information if books are found
if books_found:
    for book in books_found:
        print(f"Title: {book['title']}\nAuthor: {book['author']}\nAvailability: {'Available' if book['available'] else 'Not available'}\nSuggestion: {book['suggestion']}\n")
    issue_book_input = input("Do you want to issue a book (yes/no)? ")
    if issue_book_input.lower() == "yes":
        issue_book(search_term)
else:
    print(f"No books found with the search term '{search_term}'.")

# Display the QR code
print(f"QR code saved as {qr_filename}")
