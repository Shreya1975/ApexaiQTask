class Book:
    """
    A class to represent a book in the library.

    Attributes:
        title (str): The title of the book.
        author (str): The author of the book.
        available (bool): Whether the book is available for borrowing.
    """

    def __init__(self, title, author):
        """Initialize a new book as available by default."""
        self.title = title
        self.author = author
        self.available = True

    def __str__(self):
        """Return a string representation of the book."""
        status = "Available" if self.available else "Borrowed"
        return f"{self.title} by {self.author} ({status})"


class Member:
    """
    A class to represent a library member.

    Attributes:
        name (str): The name of the member.
        borrowed_books (list): The books currently borrowed by the member.
    """

    def __init__(self, name):
        """Initialize a member with no borrowed books."""
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        """
        Borrow a book if it is available.
        
        Args:
            book (Book): The book to borrow.
        """
        if book.available:
            book.available = False
            self.borrowed_books.append(book)
            print(f"{self.name} borrowed '{book.title}'.")
        else:
            print(f"Sorry, '{book.title}' is not available.")

    def return_book(self, book):
        """
        Return a borrowed book to the library.
        
        Args:
            book (Book): The book to return.
        """
        if book in self.borrowed_books:
            book.available = True
            self.borrowed_books.remove(book)
            print(f"{self.name} returned '{book.title}'.")
        else:
            print(f"{self.name} doesn't have '{book.title}' to return.")


class Library:
    """
    A class to represent the library.

    Attributes:
        books (list): A collection of books in the library.
    """

    def __init__(self):
        """Initialize the library with an empty collection of books."""
        self.books = []

    def add_book(self, book):
        """
        Add a book to the library collection.
        
        Args:
            book (Book): The book to add.
        """
        self.books.append(book)

    def show_books(self):
        """Display all books in the library with their availability status."""
        if not self.books:
            print("\nNo books in the library yet!\n")
            return
        print("\nLibrary Collection:")
        for i, book in enumerate(self.books, start=1):
            print(f"{i}. {book}")
        print()


# ------------------- Interactive Menu -------------------
if __name__ == "__main__":
    library = Library()

    # Add some books
    library.add_book(Book("The Great Gatsby", "F. Scott Fitzgerald"))
    library.add_book(Book("1984", "George Orwell"))
    library.add_book(Book("To Kill a Mockingbird", "Harper Lee"))

    # Create one member (for simplicity)
    member_name = input("Enter your name to join the library: ")
    member = Member(member_name)

    while True:
        print("\n------ Library Menu ------")
        print("1. Show all books")
        print("2. Borrow a book")
        print("3. Return a book")
        print("4. Show my borrowed books")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == "1":
            library.show_books()

        elif choice == "2":
            library.show_books()
            if library.books:
                try:
                    book_num = int(input("Enter book number to borrow: "))
                    if 1 <= book_num <= len(library.books):
                        member.borrow_book(library.books[book_num - 1])
                    else:
                        print("Invalid book number.")
                except ValueError:
                    print("Please enter a valid number.")

        elif choice == "3":
            if not member.borrowed_books:
                print("You have no borrowed books.")
            else:
                print("\nYour borrowed books:")
                for i, book in enumerate(member.borrowed_books, start=1):
                    print(f"{i}. {book.title}")
                try:
                    book_num = int(input("Enter book number to return: "))
                    if 1 <= book_num <= len(member.borrowed_books):
                        member.return_book(member.borrowed_books[book_num - 1])
                    else:
                        print("Invalid book number.")
                except ValueError:
                    print("Please enter a valid number.")

        elif choice == "4":
            if member.borrowed_books:
                print("\nYour borrowed books:")
                for book in member.borrowed_books:
                    print(f"- {book.title}")
            else:
                print("You haven't borrowed any books yet.")

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please select from 1-5.")


