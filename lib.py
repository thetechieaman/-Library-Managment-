import qrcode

# Define the book information
book_title = "The Great Gatsby"
book_author = "F. Scott Fitzgerald"
book_available = True
book_suggestion = "If you liked this book, you might also enjoy 'The Great Gatsby's contemporary, 'Tender is the Night'."

# Define the QR code information
qr_data = f"Title: {book_title}\nAuthor: {book_author}\nAvailability: {'Available' if book_available else 'Not available'}\nSuggestion: {book_suggestion}"
qr_filename = "book_info.png"

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

# Display the QR code
print(f"QR code saved as {qr_filename}")
