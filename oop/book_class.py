class Book:
    def __init__(self, title, author, year):
        """
        Constructor to initialize the book attributes.
        :param title: str, the title of the book
        :param author: str, the author of the book
        :param year: int, the publication year of the book
        """
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """
        Destructor to handle object deletion.
        Prints a message upon deletion of the object.
        """
        print(f"Deleting {self.title}")

    def __str__(self):
        """
        String representation of the Book object.
        :return: str, a formatted string describing the book
        """
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """
        Official representation of the Book object.
        :return: str, a string to recreate the Book instance
        """
        return f"Book('{self.title}', '{self.author}', {self.year})"
