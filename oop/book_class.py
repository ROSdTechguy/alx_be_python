# book_class.py

class Book:
    """A class representing a book with a title, author, and publication year."""

    def __init__(self, title, author, year):
        """Constructor to initialize the book's title, author, and publication year."""
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """Destructor to print a message when the book object is deleted."""
        print(f"Deleting {self.title}")

    def __str__(self):
        """String representation for informal output."""
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """Official string representation for debugging and object recreation."""
        return f"Book('{self.title}', '{self.author}', {self.year})"
