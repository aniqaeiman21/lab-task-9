class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display_info(self):
        print("Book Title:", self.title)
        print("Author:", self.author)

book1 = Book("Harry Potter", "J.K. Rowling")
book2 = Book("The Alchemist", "Paulo Coelho")
book3 = Book("Wings of Fire", "A.P.J. Abdul Kalam")

book1.display_info()
print()

book2.display_info()
print()

book3.display_info()