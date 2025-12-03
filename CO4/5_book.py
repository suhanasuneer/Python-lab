class Publisher:  # Parent class
    def __init__(self, name):
        self.name = name

    def display(self):
        print("Publisher Name:", self.name)


class Book(Publisher):  # Derived class from Publisher
    def __init__(self, name, title, author):
        super().__init__(name)  # invoking base constructor
        self.title = title
        self.author = author

    def display(self):
        super().display()  # calling parent display()
        print("Title:", self.title)
        print("Author:", self.author)


class Python(Book):  # Derived class from Book
    def __init__(self, name, title, author, price, no_of_pages):
        super().__init__(name, title, author)
        self.price = price
        self.no_of_pages = no_of_pages

    def display(self):
        super().display()  # calling parent display()
        print("Price: Rs.", self.price)
        print("Number of Pages:", self.no_of_pages)


# Main Program
publisher_name = input("Enter the publisher's name: ")
book_title = input("Enter the book's title: ")
book_author = input("Enter the author's name: ")
book_price = float(input("Enter the price of the book: "))
book_pages = int(input("Enter the number of pages: "))

Pbook = Python(publisher_name, book_title, book_author, book_price, book_pages)

# Displaying book information
print("\n--- Python Book Details ---")
Pbook.display()
