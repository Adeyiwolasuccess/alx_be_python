# Book_class.py

class Book:
    """
        Represents a book with a title, author, and publication year.
        This class demonstrates the use if special (magic) methods in python.
    """

    def __init__(self, title: str, author: str, year: int):
        """
        Initializes a new book instance.

        Args:
            title (str): The title of the Book.
            author (str): The author of the Book.
             Year (int): The Year the book was published
        """
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """
            Destructor for the Book instance.
            This method is called when an object is about to be destroyed.
            It prints a message indicating which book is being deleted.
        """
        print(f"Deleting {self.title}")

    def __str__(self):
        """
              Provides a user-friendly string representation of the book instance.
              This is called by functions like str() and print().

            :return:
              str: A formatted string showing book details.
        """
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """
               Provides an official, unambiguous string representation of the Book instance.
               The returned string should be a valid Python expression that can recreate the object.

               Returns:
                   str: The official representation of the Book instance.
               """
        return f"Book('{self.title}', '{self.author}', '{self.year}')"