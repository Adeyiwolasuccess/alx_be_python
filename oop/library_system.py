# library_system.py

class Book:
    """
    Base class representing a generic book.
    """
    def __init__(self, title: str, author: str):
        """
        Initializes a new Book instance.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
        """
        self.title = title
        self.author = author

    def __str__(self):
        """
        Returns a string representation of the Book.
        """
        return f"Book: {self.title} by {self.author}"

class EBook(Book):
    """
    Derived class representing an electronic book, inheriting from Book.
    """
    def __init__(self, title: str, author: str, file_size: int):
        """
        Initializes a new EBook instance.

        Args:
            title (str): The title of the e-book.
            author (str): The author of the e-book.
            file_size (int): The file size of the e-book in KB.
        """
        # Call the constructor of the base class (Book)
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        """
        Returns a string representation of the EBook.
        """
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"

class PrintBook(Book):
    """
    Derived class representing a physical print book, inheriting from Book.
    """
    def __init__(self, title: str, author: str, page_count: int):
        """
        Initializes a new PrintBook instance.

        Args:
            title (str): The title of the print book.
            author (str): The author of the print book.
            page_count (int): The number of pages in the print book.
        """
        # Call the constructor of the base class (Book)
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        """
        Returns a string representation of the PrintBook.
        """
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"

class Library:
    """
    Class representing a library, demonstrating composition by managing a collection of books.
    """
    def __init__(self):
        """
        Initializes a new Library instance with an empty list of books.
        """
        self.books = [] # This list will store instances of Book, EBook, and PrintBook

    def add_book(self, book):
        """
        Adds a book (Book, EBook, or PrintBook instance) to the library's collection.

        Args:
            book: An instance of Book, EBook, or PrintBook.
        """
        if isinstance(book, Book):
            self.books.append(book)
        else:
            print("Error: Only instances of Book, EBook, or PrintBook can be added to the library.")

    def list_books(self):
        """
        Prints the details of each book currently in the library.
        """
        print("Books in the Library:")
        for book in self.books:
            # The __str__ method of each book object will be called automatically
            # to provide the appropriate string representation.
            print(book)
