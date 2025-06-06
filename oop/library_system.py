class Book:
    def __init__(self, title, author):
        """
        Initialize the Book class with title and author.
        :param title: str, the title of the book
        :param author: str, the author of the book
        """
        self.title = title
        self.author = author

    def __str__(self):
        """
        String representation of the Book object.
        :return: str, book details
        """
        return f"Book: {self.title} by {self.author}"


class EBook(Book):
    def __init__(self, title, author, file_size):
        """
        Initialize the EBook class with title, author, and file size.
        :param title: str, the title of the book
        :param author: str, the author of the book
        :param file_size: int, the file size of the ebook in KB
        """
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        """
        String representation of the EBook object.
        :return: str, ebook details
        """
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"


class PrintBook(Book):
    def __init__(self, title, author, page_count):
        """
        Initialize the PrintBook class with title, author, and page count.
        :param title: str, the title of the book
        :param author: str, the author of the book
        :param page_count: int, the number of pages in the book
        """
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        """
        String representation of the PrintBook object.
        :return: str, print book details
        """
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


class Library:
    def __init__(self):
        """
        Initialize the Library class with an empty list of books.
        """
        self.books = []

    def add_book(self, book):
        """
        Add a book to the library.
        :param book: Book, EBook, or PrintBook instance
        """
        self.books.append(book)

    def list_books(self):
        """
        List all books in the library with their details.
        """
        for book in self.books:
            print(book)

